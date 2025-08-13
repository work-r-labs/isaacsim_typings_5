import __future__
from __future__ import annotations
from contextlib import contextmanager
import glob as glob
import os as os
import shutil as shutil
import sys as sys
import tempfile as tempfile
import zipfile as zipfile
__all__: list[str] = ['ExtractUsdzPackage', 'UsdzAssetIterator', 'contextmanager', 'glob', 'os', 'print_function', 'shutil', 'sys', 'tempfile', 'zipfile']
class UsdzAssetIterator:
    """
    
        Class that provides an iterator for usdz assets. Within context, it
        extracts the contents of the usdz package, provides generators for all usd
        files and all assets and on exit packs the extracted files back recursively 
        into a usdz package.
        Note that root layer of the usdz package might not be compliant which can
        cause UsdzAssetIterator to raise an exception while repacking on exit.
        
    """
    @staticmethod
    def _CreateUsdzPackage(usdzFile, filesToAdd, verbose):
        ...
    def AllAssets(self):
        """
        
                Generator for all assets packed in the usdz package, respecting nested
                usdz assets.
                
        """
    def UsdAssets(self):
        """
        
                Generator for UsdAssets respecting nested usdz assets.
                
        """
    def _ExtractedFiles(self):
        ...
    def __enter__(self):
        ...
    def __exit__(self, excType, excVal, excTB):
        ...
    def __init__(self, usdzFile, verbose, parentDir = None):
        ...
def ExtractUsdzPackage(usdzFile, extractDir, recurse, verbose, force):
    """
    
        Given a usdz package usdzFile, extracts the contents of the archive under
        the extractDir directory. Since usdz packages can contain other usdz
        packages, recurse flag can be used to extract the nested structure
        appropriately.
        
    """
def _AllowedUsdExtensions():
    ...
def _AllowedUsdzExtensions():
    ...
def _Err(msg):
    ...
def _Print(msg):
    ...
print_function: __future__._Feature  # value = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 1048576)
