from langchain.tools import tool
import logging
from langchain_openai.embeddings import OpenAIEmbeddings
from qdrant_client import QdrantClient
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__name__)

qdrant_client = QdrantClient(url=os.getenv('QDRANT_URL'))
mongo_client = MongoClient(os.getenv('MONGO_URI'))
embedding_model = os.getenv('MODEL_EMBEDDING_MODEL')
model_api_key = os.getenv('MODEL_API_KEY')
qdrant_collection = os.getenv('QDRANT_COLLECTION', 'infrastructure')
mongo_db_name = os.getenv('MONGO_DB')
mongo_collection_name = os.getenv('MONGO_COLLECTION', 'infrastructure')

@tool
def read_infrastructure(query: str) -> list:
    """Tool to extract current infrastructure information related to a query.
        Pass in a query and this tool will return relevant information about the current infrastructure based on the query. 
        The tool uses a vector search to find relevant information in the infrastructure collection.

    Args:
        query: Query to search for infrastructure information
    """
    logger.info('Calling tool read_infrastructure')
    embeddings = OpenAIEmbeddings(model=embedding_model)
    vector = embeddings.embed_query(query)
    logger.info(f'Embedding vector created for query: {query} with length {len(vector)}')

    result = qdrant_client.query_points(
        collection_name=qdrant_collection,
        query=vector,
        limit=20
    )

    logger.info(f'Calling mongodb database {mongo_db_name}, collection {mongo_collection_name} for additional infrastructure details')
    if not mongo_db_name:
        return []

    db = mongo_client[mongo_db_name]
    collection = db[mongo_collection_name]

    normalized_paths = []
    for point in result.points:
        file_path = point.payload.get('file_path') if point.payload else None
        if not file_path:
            continue
        file_path = file_path.lstrip('files/code')
        normalized_paths.append(file_path)

    if not normalized_paths:
        logger.info('No file_path values found in qdrant results')
        return []

    logger.info(f'Retrieved qdrant results: {result}')
    logger.info(f'Querying MongoDB for file paths: {normalized_paths}')

    infrastructure_records = list(collection.find({'file_path': {'$in': normalized_paths}}))
    return infrastructure_records

@tool
def read_all_infrastructure() -> list:
    """Tool to extract all current infrastructure information. 
        Use this tool to get all the information about the current infrastructure. 
        This is useful for getting a complete overview of the infrastructure setup."""
    
    logger.info('Calling tool read_all_infrastructure')

    db = None
    if mongo_db_name:
        db = mongo_client[mongo_db_name]
    else:
        return []

    collection = db[mongo_collection_name]
    infrastructure_records = list(collection.find({}))
    mongo_client.close()
    return infrastructure_records

def get_tools()->list:
    return [read_infrastructure]