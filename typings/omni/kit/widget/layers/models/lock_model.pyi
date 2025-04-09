from __future__ import annotations
from omni.kit.widget.layers.layer_model_utils import LayerModelUtils
from omni import ui
import omni.ui._ui
__all__ = ['LayerModelUtils', 'LockModel', 'ui']
class LockModel(omni.ui._ui.AbstractValueModel):
    def __init__(self, layer_item):
        ...
    def destroy(self):
        ...
    def get_value_as_bool(self):
        ...
    def set_value(self, value):
        ...
