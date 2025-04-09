from __future__ import annotations
import carb as carb
import os as os
import typing as typing
__all__ = ['Version', 'carb', 'get_version', 'os', 'parse_version', 'typing']
class Version:
    def __init__(self):
        ...
def get_version() -> typing.Tuple[str, str, str, str, str, str, str, str]:
    """
    Retrieve version from the App VERSION file
    
        Returns:
            typing.Tuple[str, str, str, str, str, str, str, str]: [Core version, Pre-release tag and build number, Major version, Minor version, Patch version, Pre-release tag, Build number, Build tag]
        
    """
def parse_version(full_version: str) -> Version:
    """
    Parse a version string into a version object
    
        Args:
            full_version (str): full version string read from a VERSION file
    
        Returns:
            Version: Parsed version object
        
    """
