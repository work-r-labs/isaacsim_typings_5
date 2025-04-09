"""
Collection of functions to manage thumbnails.
"""
from __future__ import annotations
import asyncio as asyncio
from carb import log_warn
import omni as omni
from omni.kit.helper.file_utils import asset_types
import os as os
__all__: list = ['MissingThumbnailError', 'find_thumbnails_for_files_async', 'list_thumbnails_for_folder_async', 'generate_missing_thumbnails_async']
class MissingThumbnailError(Exception):
    """
     Raised when Moebius server error
        
    """
    def __init__(self, msg: str = '', url: str = None):
        ...
def _find_thumbnail_async(url: str, auto = False):
    ...
def find_thumbnails_for_files_async(urls: typing.List[str], generate_missing: bool = True) -> typing.Dict:
    """
    
        Return a dictionary of thumbnails for the given files.
    
        Args:
            urls (List[str]): List of file Urls.
            generate_missing (bool): When True, emits a carb event for the missing thumbnails. Set to False to
                disable this behavior.
    
        Returns:
            Dict: Dict of all found thumbnails, with file Url as key, and thumbnail Url as value.
    
        
    """
def generate_missing_thumbnails_async(missing_thumbnails: typing.List[str]):
    """
    
        When missing thumbnails are discovered, send an event to have them generated.  The generator
        service is a separate process.  Once generated, a reciprocal event is sent to update the UI.
        The flow is diagramed below::
    
            +-------------------------------+                        +------------------------------+
            |         Filebrowser           |                        |                              |
            |  +-------------------------+  |   Missing thumbnails   |                              |
            |  |                         |  |        event           |                              |
            |  |       update_grid       +--------------------------->     Thumbnail generator      |
            |  |                         |  |                        |          service             |
            |  +-------------------------+  |                        |                              |
            |  +-------------------------+  |      Thumbnails        |                              |
            |  |                         |  |   generated event      |                              |
            |  |    update_cards_on      <---------------------------+                              |
            |  |  thumbnails_generated   |  |                        |                              |
            |  +-------------------------+  |                        |                              |
            |                               |                        |                              |
            +-------------------------------+                        +------------------------------+
    
        
    """
def list_thumbnails_for_folder_async(url: str, timeout: float = 30.0, generate_missing: bool = True) -> typing.Dict:
    """
    
        Return a dictionary of thumbnails for the files in the given folder.
    
        Args:
            url (str): Folder Url.
            generate_missing (bool): When True, emits a carb event for the missing thumbnails. Set to False to
                disable this behavior.
    
        Returns:
            Dict: Dict of all found thumbnails, with file Url as key, and thumbnail Url as value.
    
        
    """
MISSING_IMAGE_THUMBNAILS_EVENT: int = 1346573191877322751
_missing_thumbnails_cache: set = set()
_thumbnails_dir: str = '.thumbs/256x256'
