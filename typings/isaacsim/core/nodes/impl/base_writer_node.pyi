from __future__ import annotations
import carb as carb
import copy as copy
import isaacsim.core.nodes.impl.base_reset_node
from isaacsim.core.nodes.impl.base_reset_node import BaseResetNode
import omni as omni
from omni.replicator import core as rep
from pxr import Usd
__all__ = ['BaseResetNode', 'BaseWriterNode', 'Usd', 'WriterRequest', 'carb', 'copy', 'omni', 'rep']
class BaseWriterNode(isaacsim.core.nodes.impl.base_reset_node.BaseResetNode):
    """
    
        Base class for nodes that automatically reset when stop is pressed.
        
    """
    def __init__(self, initialize: bool = False):
        ...
    def _append_request(self, request: WriterRequest):
        ...
    def _process_acivation_requests(self, event):
        ...
    def append_writer(self, writer):
        """
        
                Appends deepcopy of provided writer to internal writer list.
                
        """
    def attach_writer(self, writer, render_product_path):
        """
        
                Creates writer request for deepcopy of provided writer to provided render_product_path, and activates it.
                
        """
    def attach_writers(self, render_product_path):
        """
        
                Creates writer request for all stored writers using provided render product,
                and activates them.
                
        """
    def custom_reset(self):
        ...
    def post_attach(self, writer, render_product):
        ...
class WriterRequest:
    def __init__(self, writer: omni.replicator.core.scripts.writers.Writer, render_product_path: typing.Union[str, typing.List[str]], activate: bool = True):
        ...
    def __repr__(self) -> str:
        ...
