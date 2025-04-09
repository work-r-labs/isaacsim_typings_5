from __future__ import annotations
import asyncio as asyncio
import omni as omni
import typing
__all__: list = ['VersioningHelper']
class VersioningHelper:
    server_info_cache: typing.ClassVar[dict] = {}
    @staticmethod
    def check_server_checkpoint_support_async(server: str):
        """
        
                 Check if server supports checkpointing. 
                 
                 Args:
                      server: Server to check support. Can be empty or " ".
                 
                 Returns: 
                      True if support checkpoint False otherwise.
                
        """
    @staticmethod
    def extract_server_from_url(url):
        """
        
                 Extract server URL from URL. 
                 
                 Args:
                      url: URL to extract server from
                 
                 Returns: 
                      Server URL.
                
        """
    @staticmethod
    def get_server_info_async(server: str):
        """
        
                 Get information about server. 
                 
                 Args:
                      server: The server to get information about.
                 
                 Returns: 
                      A dict containing server information or None.
                
        """
    @staticmethod
    def is_versioning_enabled():
        """
        Check if versioning is enabled. 
        """
    @staticmethod
    def menu_checkpoint_dialog(ok_fn: callable, cancel_fn: callable):
        """
        
                 Create and show a dialog to ask for checkpoints.
                 
                 Args:
                      ok_fn: The function to call when the user presses OK.
                      cancel_fn: The function to call when the user presses cancel.
                
        """
