from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit import notification_manager as nm
from omni.kit.widget.stage.stage_item import StageItem
from omni.kit.widget.stage.stage_settings import StageSettings
from omni.kit.widget.stage.utils import handle_exception
import os as os
from pathlib import Path
from pxr import Sdf
from pxr import Tf
from pxr import UsdGeom
import re as re
__all__: list = ['StageDragAndDropHandler', 'AssetType']
class AssetType:
    """
    A singleton that determines the type of asset using regex
    """
    def __init__(self):
        ...
    def add_future(self, obj):
        """
        Add a future-like object to the global list, so it's not destroyed
        """
    def destroy(self):
        ...
    def get_first_material_name(self, mdl_file):
        """
        Parse the MDL asset and return the name of the first shader
        """
    def is_audio(self, asset):
        ...
    def is_mdl(self, asset):
        ...
    def is_usd(self, asset):
        ...
class StageDragAndDropHandler:
    children_reorder_supported = ...
    @staticmethod
    def _StageDragAndDropHandler__apply_mdl(*args, **kwargs):
        """
        Import and apply MDL asset to the specified prim
        """
    def _StageDragAndDropHandler__apply_drop(self, target_item, source, drop_location):
        ...
    def _StageDragAndDropHandler__apply_drop_task(self):
        ...
    def _StageDragAndDropHandler__drop_location_to_prim_index(self, prim_path, drop_location, new_item = False):
        """
        
                Gets the real prim index inside the children list of parent as drop location
                only shows the UI location while some of the children are possibly
                hidden in the stage window.
                
        """
    def _StageDragAndDropHandler__reorder_prim_to_drop_location(self, prim_path, drop_location, new_item):
        ...
    def __init__(self, stage_model):
        ...
    def drop(self, target_item, source, drop_location = -1):
        """
        
                Reimplemented from AbstractItemModel. Called when dropping something to the item.
        
                When drop_location is -1, it means to drop the source item on top of the target item.
                When drop_location is not -1, it means to drop the source item between items.
                
        """
    def drop_accepted(self, target_item, source, drop_location = -1):
        """
        Reimplemented from AbstractItemModel. Called to highlight target when drag and drop.
        """
    @property
    def is_reordering_prim(self):
        ...
ASSET_DRAG_EVENT: int = 9130664045132330179
KEEP_TRANSFORM_FOR_REPARENTING: str = '/persistent/app/stage/movePrimInPlace'
STAGE_DRAGDROP_IMPORT: str = '/persistent/app/stage/dragDropImport'
