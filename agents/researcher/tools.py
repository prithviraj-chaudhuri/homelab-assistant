from langchain.tools import tool
import feedparser
import logging

logger = logging.getLogger(__name__)

@tool
def read_reddit(subreddit: str) -> list:
    """Tool to search subreddits

    Args:
        subreddit: Subreddit to search (without the `r/`)
    """
    logger.info('Calling tool read_reddit')
    url = f'https://www.reddit.com/r/{subreddit}/new.rss'
    logger.info(f'Calling {url}')

    feed = feedparser.parse(url)
    feed_list = []
    for index, entry in enumerate(feed.entries, start=1):
        feed_list.append(entry)

    return feed_list

def get_tools()->list:
    return [read_reddit]