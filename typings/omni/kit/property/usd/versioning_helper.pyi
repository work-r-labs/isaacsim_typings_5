from __future__ import annotations
import asyncio as asyncio
import omni as omni
import typing
__all__: list = ['VersioningHelper']
class VersioningHelper:
    """
    
        A class to represent the versioning helper.
        
    """
    server_cache: typing.ClassVar[dict] = {}
    @staticmethod
    def check_server_checkpoint_support(server: str, on_complete: callable):
        """
        
                Checks the server checkpoint support.
        
                Args:
                    server: The server.
                    on_complete: The on complete callback.
                
        """
    @staticmethod
    def extract_server_from_url(url):
        """
        
                Extracts the server from a URL.
        
                Args:
                    url: The URL.
        
                Returns:
                    The server URL.
                
        """
    @staticmethod
    def is_versioning_enabled():
        """
        
                Checks if versioning is enabled.
        
                Returns:
                    True if versioning is enabled, False otherwise.
                
        """
