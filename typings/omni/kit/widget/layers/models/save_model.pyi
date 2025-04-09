from __future__ import annotations
import omni as omni
from omni.kit.widget.layers.layer_model_utils import LayerModelUtils
from omni import ui
import weakref as weakref
__all__ = ['LayerModelUtils', 'SaveModel', 'omni', 'ui', 'weakref']
class SaveModel(omni.ui._ui.AbstractValueModel):
    def __init__(self, layer_item):
        ...
    def destroy(self):
        ...
    def get_value_as_bool(self):
        ...
    def set_value(self, value):
        ...
