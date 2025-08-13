from __future__ import annotations
import asyncio as asyncio
import carb as carb
import concurrent as concurrent
import functools as functools
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.widget.stage.stage_helper import UsdStageHelper
from omni import ui
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
import pxr.Usd
import traceback as traceback
import typing
from typing import Any
__all__: list[str] = ['Any', 'Sdf', 'Tf', 'Trace', 'Usd', 'UsdPropertyWatch', 'UsdPropertyWatchModel', 'UsdStageHelper', 'asyncio', 'carb', 'concurrent', 'functools', 'handle_exception', 'omni', 'run_coroutine', 'traceback', 'ui']
class UsdPropertyWatch(omni.kit.widget.stage.stage_helper.UsdStageHelper):
    """
    
        DEPRECATED: The purpose of this class is to keep a large number of models.
        `Usd.Notice.ObjectsChanged` is pretty slow, and to remain fast, we need
        to register as few `Tf.Notice` as possible. Thus, we can't put the
        `Tf.Notice` logic to the model. Instead, this class creates and
        coordinates the models.
        
    """
    @staticmethod
    def _UsdPropertyWatch__delayed_prim_changed(*args, **kwargs):
        """
        Called in the next frame when the object is changed
        """
    @staticmethod
    def _on_objects_changed(*args, **kwargs):
        """
        Called by Tf.Notice
        """
    def __init__(self, stage: pxr.Usd.Stage, property_name: str, model_type: typing.Type[omni.kit.widget.stage.usd_property_watch.UsdPropertyWatchModel] = UsdPropertyWatchModel):
        """
        
                ## Arguments:
                    `stage`: USD Stage
                    `property_name`: The name of the property to watch
                    `model_type`: The name of the property to watch
                
        """
    def _create_model(self, path: pxr.Sdf.Path):
        """
        Creates a new model and puts in to the cache
        """
    def destroy(self):
        """
        Called before destroying
        """
    def get_model(self, path):
        ...
    def update_dirty(self):
        """
        
                Create/remove dirty items that was collected from TfNotice. Can be
                called any time to pump changes.
                
        """
class UsdPropertyWatchModel(omni.ui._ui.AbstractValueModel, omni.kit.widget.stage.stage_helper.UsdStageHelper):
    """
    
        DEPRECATED: A helper model of UsdPropertyWatch that behaves like a model that watches
        a USD property. It doesn't work properly if UsdPropertyWatch does not
        create it.
        
    """
    def __init__(self, stage: pxr.Usd.Stage, path: pxr.Sdf.Path):
        """
        
                ## Arguments:
                    `stage`: USD Stage
                    `path`: The full path to the watched property
                
        """
    def _get_prop(self):
        """
        Get the property this model holds
        """
    def destroy(self):
        """
        Called before destroying
        """
    def get_value_as_bool(self) -> typing.Optional[bool]:
        """
        Reimplemented get bool
        """
    def get_value_as_float(self) -> typing.Optional[float]:
        """
        Reimplemented get bool
        """
    def get_value_as_int(self) -> typing.Optional[int]:
        """
        Reimplemented get bool
        """
    def get_value_as_string(self) -> typing.Optional[str]:
        """
        Reimplemented get bool
        """
    def on_usd_changed(self):
        """
        Called by the stage model when the visibility is changed
        """
    def set_value(self, value: typing.Any):
        """
        Reimplemented set bool
        """
def handle_exception(func):
    """
    
        Decorator to print exception in async functions
        
    """
