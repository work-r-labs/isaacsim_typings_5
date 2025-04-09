from __future__ import annotations
from omni.kit.usd import layers
from omni import ui
import omni.ui._ui
import weakref as weakref
__all__ = ['MutenessModel', 'layers', 'ui', 'weakref']
class MutenessModel(omni.ui._ui.AbstractValueModel):
    def __init__(self, usd_context, layer_item, local: bool):
        ...
    def destroy(self):
        ...
    def get_value_as_bool(self):
        ...
    def set_value(self, value):
        ...
