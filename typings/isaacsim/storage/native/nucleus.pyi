from __future__ import annotations
import asyncio as asyncio
import carb as carb
from collections import namedtuple
from isaacsim.core.version.extension import get_version
import json as json
import omni as omni
from omni.client.impl._omniclient import CopyBehavior
from omni.client.impl._omniclient import Result
import os as os
import typing as typing
from urllib.parse import urlparse
__all__ = ['CopyBehavior', 'Result', 'Version', 'asyncio', 'build_server_list', 'carb', 'check_server', 'check_server_async', 'create_folder', 'delete_folder', 'download_assets_async', 'find_nucleus_server', 'get_assets_root_path', 'get_assets_root_path_async', 'get_assets_server', 'get_full_asset_path', 'get_full_asset_path_async', 'get_isaac_asset_root_path', 'get_nvidia_asset_root_path', 'get_server_path', 'get_server_path_async', 'get_url_root', 'get_version', 'is_dir', 'is_dir_async', 'is_file', 'is_file_async', 'json', 'list_folder', 'namedtuple', 'omni', 'os', 'recursive_list_folder', 'typing', 'urlparse', 'verify_asset_root_path']
class Version(Version):
    @classmethod
    def __new__(cls, s):
        ...
    def __repr__(self):
        ...
def _collect_files(url: str) -> typing.Tuple[str, typing.List]:
    """
    Collect files under a URL.
    
        Args:
            url (str): URL of Nucleus server with path to folder
    
        Returns:
            root (str): Root of URL of Nucleus server
            paths (typing.List): List of path to each file
        
    """
def _list_files(url: str) -> typing.Tuple[str, typing.List]:
    """
    List files under a URL
    
        Args:
            url (str): URL of Nucleus server with path to folder
    
        Returns:
            root (str): Root of URL of Nucleus server
            paths (typing.List): List of path to each file
        
    """
def build_server_list() -> typing.List:
    """
    Return list with all known servers to check
    
        Returns:
            all_servers (typing.List): List of servers found
        
    """
def check_server(server: str, path: str, timeout: float = 10.0) -> bool:
    """
    Check a specific server for a path
    
        Args:
            server (str): Name of Nucleus server
            path (str): Path to search
            timeout (float): Default value: 10 seconds
    
        Returns:
            bool: True if folder is found
        
    """
def check_server_async(server: str, path: str, timeout: float = 10.0) -> bool:
    """
    Check a specific server for a path (asynchronous version).
    
        Args:
            server (str): Name of Nucleus server
            path (str): Path to search
            timeout (float): Default value: 10 seconds
    
        Returns:
            bool: True if folder is found
        
    """
def create_folder(server: str, path: str) -> bool:
    """
    Create a folder on server
    
        Args:
            server (str): Name of Nucleus server
            path (str): Path to folder
    
        Returns:
            bool: True if folder is created successfully
        
    """
def delete_folder(server: str, path: str) -> bool:
    """
    Remove folder and all of its contents
    
        Args:
            server (str): Name of Nucleus server
            path (str): Path to folder
    
        Returns:
            bool: True if folder is deleted successfully
        
    """
def download_assets_async(src: str, dst: str, progress_callback, concurrency: int = 10, copy_behaviour: omni.client.impl._omniclient.CopyBehavior = ..., copy_after_delete: bool = True, timeout: float = 300.0) -> omni.client.impl._omniclient.Result:
    """
    Download assets from S3 bucket
    
        Args:
            src (str): URL of S3 bucket as source
            dst (str): URL of Nucleus server to copy assets to
            progress_callback: Callback function to keep track of progress of copy
            concurrency (int): Number of concurrent copy operations. Default value: 3
            copy_behaviour (omni.client._omniclient.CopyBehavior): Behavior if the destination exists. Default value: OVERWRITE
            copy_after_delete (bool): True if destination needs to be deleted before a copy. Default value: True
            timeout (float): Default value: 300 seconds
    
        Returns:
            Result (omni.client._omniclient.Result): Result of copy
        
    """
def find_nucleus_server(suffix: str) -> typing.Tuple[bool, str]:
    """
    Attempts to determine best Nucleus server to use based on existing mountedDrives setting and the
        default server specified in json config at "/persistent/isaac/asset_root/". Call is blocking
    
        Args:
            suffix (str): Path to folder to search for. Default value: /Isaac
    
        Returns:
            bool: True if Nucleus server with suffix is found
            url (str): URL of found Nucleus
        
    """
def get_assets_root_path() -> typing.Optional[str]:
    """
    Tries to find the root path to the Isaac Sim assets on a Nucleus server
    
        Raises:
            RuntimeError: if the root path is not found.
    
        Returns:
            typing.Union[str, None]:
                url (str): URL of Nucleus server with root path to assets folder.
                Returns None if Nucleus server not found.
        
    """
def get_assets_root_path_async() -> typing.Optional[str]:
    """
    Tries to find the root path to the Isaac Sim assets on a Nucleus server (asynchronous version).
    
        Raises:
            RuntimeError: if the root path is not found.
    
        Returns:
            url (str): URL of Nucleus server with root path to assets folder.
            Returns None if Nucleus server not found.
        
    """
def get_assets_server() -> typing.Optional[str]:
    """
    Tries to find a server with the Isaac Sim assets
    
        Returns:
            url (str): URL of Nucleus server with the Isaac Sim assets
                Returns None if Nucleus server not found.
        
    """
def get_full_asset_path(path: str) -> typing.Optional[str]:
    """
    Tries to find the full asset path on connected servers
    
        Args:
            path (str): Path of asset from root to verify
    
        Raises:
            RuntimeError: if the root path is not found.
    
        Returns:
            url (str): URL or full path to assets.
            Returns None if assets not found.
        
    """
def get_full_asset_path_async(path: str) -> typing.Optional[str]:
    """
    Tries to find the full asset path on connected servers (asynchronous version).
    
        Args:
            path (str): Path of asset from root to verify
    
        Raises:
            RuntimeError: if the root path is not found.
    
        Returns:
            url (str): URL or full path to assets.
            Returns None if assets not found.
        
    """
def get_isaac_asset_root_path() -> typing.Optional[str]:
    ...
def get_nvidia_asset_root_path() -> typing.Optional[str]:
    ...
def get_server_path(suffix: str = '') -> typing.Optional[str]:
    """
    Tries to find a Nucleus server with specific path.
    
        Args:
            suffix (str): Path to folder to search for.
    
        Raises:
            RuntimeError: if the root path is not found.
    
        Returns:
            url (str): URL of Nucleus server with path to folder.
            Returns None if Nucleus server not found.
        
    """
def get_server_path_async(suffix: str = '') -> typing.Optional[str]:
    """
    Tries to find a Nucleus server with specific path (asynchronous version).
    
        Args:
            suffix (str): Path to folder to search for.
    
        Raises:
            RuntimeError: if the root path is not found.
    
        Returns:
            url (str): URL of Nucleus server with path to folder.
            Returns None if Nucleus server not found.
        
    """
def get_url_root(url: str) -> str:
    """
    Get root from URL or path.
        Args:
            url (str): full http or omniverse path
    
        Raises:
            RuntimeError: if the root path is not found.
    
        Returns:
            str: Root path or URL or Nucleus server
        
    """
def is_dir(path: str) -> bool:
    """
    Check if path is a folder
    
        Args:
            path (str): Path to folder
    
        Returns:
            bool: True if path is a folder
        
    """
def is_dir_async(path: str) -> bool:
    """
    Check if path is a folder
    
        Args:
            path (str): Path to folder
    
        Returns:
            bool: True if path is a folder
        
    """
def is_file(path: str) -> bool:
    """
    Check if path is a file
    
        Args:
            path (str): Path to file
    
        Returns:
            bool: True if path is a file
        
    """
def is_file_async(path: str) -> bool:
    """
    Check if path is a file
    
        Args:
            path (str): Path to file
    
        Returns:
            bool: True if path is a file
        
    """
def list_folder(path: str) -> typing.Tuple[typing.List, typing.List]:
    """
    List files and sub-folders from root path
    
        Args:
            path (str): Path to root folder
    
        Raises:
            Exception: When unable to find files under the path.
    
        Returns:
            files (typing.List): List of path to each file
            dirs (typing.List): List of path to each sub-folder
        
    """
def recursive_list_folder(path: str) -> typing.List:
    """
    Recursively list all files
    
        Args:
            path (str): Path to folder
    
        Returns:
            paths (typing.List): List of path to each file
        
    """
def verify_asset_root_path(path: str) -> typing.Tuple[omni.client.impl._omniclient.Result, str]:
    """
    Attempts to determine Isaac assets version and check if there are updates.
        (asynchronous version)
    
        Args:
            path (str): URL or path of asset root to verify
    
        Returns:
            omni.client.Result: OK if Assets verified
            ver (str): Version of Isaac Sim assets
        
    """
