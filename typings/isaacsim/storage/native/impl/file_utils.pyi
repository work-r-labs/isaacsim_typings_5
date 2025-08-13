from __future__ import annotations
import os as os
from pxr import Sdf
from pxr import UsdUtils
__all__: list[str] = ['Sdf', 'UsdUtils', 'count_asset_references', 'find_absolute_paths_in_usds', 'find_external_references', 'find_files_recursive', 'find_missing_references', 'get_stage_references', 'is_absolute_path', 'is_mdl_file', 'is_path_external', 'is_valid_usd_file', 'layer_has_missing_references', 'os', 'path_dirname', 'path_exists', 'path_join', 'path_relative', 'prim_has_missing_references', 'prim_spec_has_missing_references']
def count_asset_references(base_path):
    """
    Get reference counts for all assets in a base path.
    
        Args:
            base_path: Base path to search for assets.
    
        Returns:
            Dictionary mapping asset paths to their reference counts, sorted by count.
        
    """
def find_absolute_paths_in_usds(base_path):
    """
    Check for absolute paths in USD files.
    
        Args:
            base_path: Base path to search for USD files.
    
        Returns:
            Dictionary mapping file paths to lists of absolute references they contain.
        
    """
def find_external_references(base_path):
    """
    Check for external references in USD files.
    
        Args:
            base_path: Base path to search for USD files.
    
        Returns:
            Dictionary mapping file paths to lists of external references they contain.
        
    """
def find_files_recursive(abs_path, filter_fn = ...):
    """
    Recursively list all files under given path(s) that match the filter function.
    
        Args:
            abs_path: List of absolute paths to search.
            filter_fn: Filter function that takes a path and returns boolean indicating if path should be included.
    
        Returns:
            List of file paths that match the filter criteria.
        
    """
def find_missing_references(base_path):
    """
    Check for missing references in USD files.
    
        Args:
            base_path: Base path to search for USD files.
        
    """
def get_stage_references(stage_path, resolve_relatives = True):
    """
    List all references in a USD stage.
    
        Args:
            stage_path: Path to the USD stage.
            resolve_relatives: If True, resolve all relative paths to absolute.
    
        Returns:
            List of path strings to referenced assets.
        
    """
def is_absolute_path(path):
    """
    Check if a path is absolute, including Omniverse URLs.
    
        Args:
            path: Path string to check.
    
        Returns:
            Boolean indicating if path is absolute.
        
    """
def is_mdl_file(item):
    """
    Check if a path is an MDL file.
    
        Args:
            item: Path to check.
    
        Returns:
            Boolean indicating if the path is an MDL file.
        
    """
def is_path_external(path, base_path):
    """
    Check if a path is external to a base path.
    
        Args:
            path: Path to check.
            base_path: Base path to compare against.
    
        Returns:
            Boolean indicating if path is external to base_path.
    
        Raises:
            Exception: If there's an error comparing the paths.
        
    """
def is_valid_usd_file(item, excludes):
    """
    Check if a path is a USD file and doesn't contain excluded substrings.
    
        Args:
            item: Path to check.
            excludes: List of substrings that should not be present in the path.
    
        Returns:
            Boolean indicating if the path is a valid USD file.
        
    """
def layer_has_missing_references(layer_identifier):
    """
    Check if a layer has any missing references.
    
        Args:
            layer_identifier: Identifier for the layer to check.
    
        Returns:
            Boolean indicating if the layer has missing references.
        
    """
def path_dirname(path):
    """
    URL friendly version of os.path.dirname.
    
        Args:
            path: Path to get the directory name from.
    
        Returns:
            Directory path string.
        
    """
def path_exists(path):
    """
    Check if a path exists.
    
        Args:
            path: Path to check.
    
        Returns:
            Boolean indicating if the path exists.
        
    """
def path_join(base, name):
    """
    Join two path components intelligently handling Omniverse URLs.
    
        Args:
            base: Base path, can be local or Omniverse URL.
            name: Path component to append to the base.
    
        Returns:
            Joined path string.
    
        Example:
    
        .. code-block:: python
    
            >>> path_join("omniverse://server/folder", "file.usd")
            'omniverse://server/folder/file.usd'
            >>> path_join("/local/path", "file.usd")
            '/local/path/file.usd'
        
    """
def path_relative(path, start):
    """
    URL friendly version of os.path.relpath.
    
        Args:
            path: Path to make relative.
            start: Start path to make the path relative to.
    
        Returns:
            Relative path string.
    
        Raises:
            ValueError: If URL scheme or domain doesn't match.
        
    """
def prim_has_missing_references(prim):
    """
    Check if a prim has any missing references.
    
        Args:
            prim: Prim to check.
    
        Returns:
            Boolean indicating if the prim has missing references.
        
    """
def prim_spec_has_missing_references(prim_spec):
    """
    Check if a prim specification has any missing references.
    
        Args:
            prim_spec: Prim specification to check.
    
        Returns:
            Boolean indicating if the prim specification has missing references.
        
    """
