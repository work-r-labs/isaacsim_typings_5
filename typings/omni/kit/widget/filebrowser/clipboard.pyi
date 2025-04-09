"""

Collection of utility functions to manage the clipboard.
"""
from __future__ import annotations
from omni.kit.widget.filebrowser.model import FileBrowserItem
__all__ = ['FileBrowserItem', 'clear_clipboard', 'get_clipboard_items', 'is_clipboard_cut', 'is_path_cut', 'save_items_to_clipboard']
def clear_clipboard():
    """
    
        Clear the clipboard.
        
    """
def get_clipboard_items() -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
    """
    
        Get browser items.
        
    """
def is_clipboard_cut() -> bool:
    """
    
        Return True if items in the clipboard are cut from other items.
        
    """
def is_path_cut(path: str) -> bool:
    """
    
        Return True if the path are cut from other items or clipboard.
    
        Args:
            path (str): path to check.
        
    """
def save_items_to_clipboard(items: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem], is_cut: bool = False):
    """
    
        Save browser items to clipboard.
    
        Args:
            items (List[:obj:`FileBrowserItem`]): List of browser items.
            is_cut (bool): Specify if items are cut from other items or clipboard, defaults to False.
        
    """
_clipboard_items: list = list()
_is_clipboard_cut: bool = False
