"""
Keeps a history of file events that is made available via an API to other extensions
"""
from __future__ import annotations
import carb as carb
from omni.kit.helper.file_utils.extension import FileEventHistoryExtension
from omni.kit.helper.file_utils.extension import FileEventModel
from omni.kit.helper.file_utils.extension import get_instance
from . import asset_types
from . import extension
__all__: list = ['FileEventModel', 'get_latest_urls_from_event_queue', 'get_last_url_visited', 'get_last_url_opened', 'get_last_url_saved', 'reset_file_event_queue', 'asset_types', 'FILE_OPENED_EVENT', 'FILE_SAVED_EVENT', 'FILE_EVENT_QUEUE_UPDATED']
def get_last_url_opened(asset_type: str = None, tag: str = None) -> str:
    """
    Retrieves the last URL opened based on asset type and tag.
    
        Args:
            asset_type (str, optional): The type of asset to filter URLs by.
            tag (str, optional): Additional tag to filter the URLs.
    
        Returns:
            str: The last opened URL matching the specified criteria or None if no match found.
    """
def get_last_url_saved(asset_type: str = None, tag: str = None) -> str:
    """
    Retrieves the last URL that was saved for a given asset type and tag.
    
        Args:
            asset_type (str): The type of asset to filter the URL by.
            tag (str): An additional filter to apply based on a tag.
    """
def get_last_url_visited(asset_type: str = None, tag: str = None) -> str:
    """
    Retrieves the last URL visited based on asset type and tag.
    
        Args:
            asset_type (str, optional): The type of asset to filter URLs by.
            tag (str, optional): The tag to further filter URLs.
    
        Returns:
            str: The last visited URL matching the criteria, or None if no URLs found.
    """
def get_latest_urls_from_event_queue(num_latest: int = 1, asset_type: str = None, event_type: int = 0, tag: str = None) -> typing.List[str]:
    """
    Retrieves the urls visited based on asset type, event type and tag.
    
        Args:
            asset_type (str, optional): The type of asset to filter URLs by.
            event_type (int, optional): The type of event to filter URLs by.
            tag (str, optional): The tag to further filter URLs.
    
        Returns:
            List[str]: The visited URLs matching the criteria, or empty list if no URLs found.
    """
def reset_file_event_queue():
    """
    Clear the event queue maintained by this extension.
    """
FILE_EVENT_QUEUE_UPDATED: int = 4806079216508642737
FILE_OPENED_EVENT: int = 3872619916304892462
FILE_SAVED_EVENT: int = 8148521607818097614
