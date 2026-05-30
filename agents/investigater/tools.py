from langchain.tools import tool
import logging

logger = logging.getLogger(__name__)

@tool
def read_infrastructure(query: str) -> list:
    """Tool to extract current infrastructure information

    Args:
        subreddit: Subreddit to search (without the `r/`)
    """
    logger.info('Calling tool read_infrastructure')

    return [
        "User is running a homelab with 3 servers, using Proxmox for virtualization, and has a mix of AMD and Intel hardware. They are interested in optimizing their setup for AI workloads and are looking for community insights on best practices and new technologies in the homelab space."
    ]

def get_tools()->list:
    return [read_infrastructure]