from __future__ import annotations
import asyncio as asyncio
import carb as carb
import hashlib as hashlib
import omni as omni
import typing
__all__ = ['DownloadState', 'PredownloadHelper', 'asyncio', 'carb', 'hashlib', 'omni']
class DownloadState:
    DONE: typing.ClassVar[str] = 'Done'
    IN_PROGRESS: typing.ClassVar[str] = 'In Progress'
    PENDING: typing.ClassVar[str] = 'Pending'
class PredownloadHelper:
    """
    
        Pre-download remote folders to local.
        Args:
            save_folder: Folder to save download items in.
        
    """
    def __init__(self, save_folder: str):
        ...
    def _predownload(self, remote_folder: str, save_folder: str) -> None:
        ...
    def _run(self) -> None:
        ...
    def append_folder(self, folder: str, save_folder: typing.Optional[str] = None) -> bool:
        """
        
                Append a remote folder to download.
                Return False if already appended, otherwise True.
                Args:
                    folder: Url of folder to download.
                    save_folder: Url of folder to save. If None, use name from hash of remote folder.
                
        """
    def destroy(self) -> None:
        ...
    def get_download_state(self, folder: str) -> typing.Optional[omni.kit.browser.folder.core.widgets.predownload.DownloadState]:
        """
        
                Get folder download state.
                Return None if never downloaded.
                
        """
