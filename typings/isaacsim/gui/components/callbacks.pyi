from __future__ import annotations
import carb as carb
import os as os
import subprocess as subprocess
import sys as sys
__all__ = ['carb', 'on_copy_to_clipboard', 'on_docs_link_clicked', 'on_open_IDE_clicked', 'on_open_folder_clicked', 'os', 'subprocess', 'sys']
def on_copy_to_clipboard(to_copy: str) -> None:
    """
    
        Copy text to system clipboard
        
    """
def on_docs_link_clicked(doc_link: str) -> None:
    """
    Opens an extension's documentation in a Web Browser
    """
def on_open_IDE_clicked(ext_path: str, file_path: str) -> None:
    """
    Opens the current directory and file in VSCode
    """
def on_open_folder_clicked(file_path: str) -> None:
    """
    Opens the current directory in a File Browser
    """
