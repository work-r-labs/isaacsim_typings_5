import __future__
from __future__ import annotations
from contextlib import contextmanager
import glob as glob
import os as os
import shutil as shutil
import sys as sys
import tempfile as tempfile
import zipfile as zipfile
__all__ = ['CheckUsdzCompliance', 'CreateUsdzPackage', 'ExtractUsdzPackage', 'UsdzAssetIterator', 'contextmanager', 'glob', 'os', 'print_function', 'shutil', 'sys', 'tempfile', 'zipfile']
class UsdzAssetIterator:
    """
    
        Class that provides an iterator for usdz assets. Within context, it
        extracts the contents of the usdz package, provides gennerators for all usd
        files and all assets and on exit packs the extracted files back recursively 
        into a usdz package.
        
    """
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
def CheckUsdzCompliance(rootLayer, arkit = False):
    """
    
        Runs UsdUtils.ComplianceChecker on the given layer and reports errors.
        Returns True if no errors or failed checks were reported, False otherwise.
        
    """
def CreateUsdzPackage(usdzFile, filesToAdd, recurse, checkCompliance, verbose):
    """
    
        Creates a usdz package with the files provided in filesToAdd and saves as
        the usdzFile.
        If filesToAdd contains nested subdirectories, recurse flag can be specified,
        which will make sure to recurse through the directory structure and include
        the files in the usdz archive.
        Specifying checkCompliance, will make sure run UsdUtils.ComplianceChecker on
        the rootLayer of the usdz package being created.
        
    """
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
