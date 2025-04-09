from __future__ import annotations
import omni as omni
from omni.kit.usd import layers
from omni.kit.widget.stage.stage_item import StageItem
from omni.kit.widget.stage.stage_model import StageModel
from omni import ui
import pxr.Sdf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
import re as re
__all__ = ['PrimItem', 'PrimModel', 'Sdf', 'StageItem', 'StageModel', 'Usd', 'layers', 'omni', 're', 'ui']
class PrimItem(omni.kit.widget.stage.stage_item.StageItem):
    def __init__(self, path: pxr.Sdf.Path, stage: pxr.Usd.Stage, stage_model: omni.kit.widget.stage.stage_model.StageModel, flat = False, root_identifier = None, load_payloads = False, check_missing_references = False):
        ...
    def set_linked_image(self, image: omni.ui._ui.Image):
        ...
    def set_locked_image(self, image: omni.ui._ui.Image):
        ...
    @property
    def linked(self):
        ...
    @linked.setter
    def linked(self, value: bool):
        ...
    @property
    def locked(self):
        ...
    @locked.setter
    def locked(self, value: bool):
        ...
class PrimModel(omni.kit.widget.stage.stage_model.StageModel):
    def __init__(self, stage: pxr.Usd.Stage):
        ...
    def _get_stage_item_from_cache(self, path: pxr.Sdf.Path, create_if_not_existed = False):
        ...
    def _on_layer_events(self, event):
        ...
    def _on_spec_links_changed(self, spec_paths: typing.List[str]):
        ...
    def _on_spec_locks_changed(self, spec_paths: typing.List[str]):
        ...
    def destroy(self):
        ...
    def drop(self, target_item, source):
        ...
    def drop_accepted(self, target_item, source):
        ...
    def find(self, path: pxr.Sdf.Path):
        """
        Return item with the given path
        """
    def get_item_value_model(self, item, column_id):
        """
        Reimplemented from AbstractItemModel
        """
    def get_item_value_model_count(self, item):
        """
        Reimplemented from AbstractItemModel
        """
