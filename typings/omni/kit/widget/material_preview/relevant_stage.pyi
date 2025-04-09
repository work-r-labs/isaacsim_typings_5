from __future__ import annotations
import asyncio as asyncio
import carb as carb
import functools as functools
import omni as omni
from omni.kit.widget.material_preview.stage_duplicate_utils import copy_prim
from omni.kit.widget.material_preview.stage_duplicate_utils import copy_property
from omni.usd.commands.stage_helper import UsdStageHelper
from pxr import Sdf
import pxr.Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
import traceback as traceback
__all__ = ['DELAY_FRAMES', 'RelevantStage', 'Sdf', 'Tf', 'Trace', 'Usd', 'UsdStageHelper', 'asyncio', 'carb', 'copy_prim', 'copy_property', 'functools', 'handle_exception', 'omni', 'traceback']
class RelevantStage:
    @staticmethod
    def _RelevantStage__delayed_prim_changed(*args, **kwargs):
        """
        Called to update the dirty data in the next frame
        """
    @staticmethod
    def _on_objects_changed(*args, **kwargs):
        """
        
                Called by Usd.Notice.ObjectsChanged. It's critically important to
                return ASAP.
                
        """
    def __init__(self, target_context_name: str, source_context_name: str = ''):
        """
        
                Construct RelevantStage
        
                ### Arguments:
        
                    `target_context_name : str`
                        The target context name
        
                    `source_context_name : str`
                        The source context name
                
        """
    def _on_stage_closing(self):
        """
        Called when close the stage
        """
    def _on_stage_opened(self):
        """
        Called when opening a new stage
        """
    def _on_usd_context_event(self, event: carb.events._events.IEvent):
        """
        Called on USD Context event
        """
    def clear(self):
        ...
    def destroy(self):
        ...
    def set_listen_root(self, root: typing.Optional[pxr.Sdf.Path]):
        """
        
                Specify the path this object listens changes of and sends deltas to
                teh remote Kit
                
        """
    def set_root_changed_fn(self, fn: typing.Callable[[typing.List[pxr.Sdf.Path]], NoneType]):
        ...
    def submit_layer(self, delta_layer: pxr.Sdf.Layer):
        """
        Send the given layer to the own context
        """
    def submit_text(self, delta_text: str):
        """
        Send the given layer to the own context
        """
    def update_dirty(self):
        """
        
                Create/remove dirty items that was collected from TfNotice. Can be
                called any time to pump changes.
                
        """
def handle_exception(func):
    """
    
        Decorator to print exception in async functions
        
    """
DELAY_FRAMES: int = 1
