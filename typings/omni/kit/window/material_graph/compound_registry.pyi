from __future__ import annotations
import carb as carb
from pathlib import Path
import pxr.Usd
from pxr import Usd
from pxr import UsdShade
from pxr import UsdUI
__all__: list = ['CompoundShadingNode', 'register_compound', 'nodes']
class CompoundShadingNode:
    def __init__(self, prim: pxr.Usd.Prim, path: str):
        ...
    @property
    def category(self):
        ...
    @property
    def colorSpace(self):
        ...
    @property
    def customData(self):
        ...
    @property
    def description(self):
        ...
    @property
    def displayName(self):
        ...
    @property
    def name(self):
        ...
    @property
    def outputs(self):
        ...
    @property
    def parameters(self):
        ...
    @property
    def sdrMetaData(self):
        ...
    @property
    def sourceAsset(self):
        ...
    @property
    def subIdentifier(self):
        ...
    @property
    def tags(self):
        ...
    @property
    def thumbnail(self):
        ...
    @property
    def uiOrder(self):
        ...
class _CompoundRegistrySubscription:
    """
    
        Registration subscription. The registration exists while this object
        exists.
        
    """
    def __del__(self):
        """
        Called by GC.
        """
    def __init__(self, path: str):
        ...
    @property
    def valid(self):
        ...
def _deregister_compound(identifier: str):
    ...
def _get_shading_nodes(path: str):
    ...
def nodes():
    """
    Get node by identifier
    """
def register_compound(path: str):
    """
    Register path that has a shader compound
    """
_registered_nodes: dict = {}
