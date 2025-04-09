from __future__ import annotations
import omni as omni
from omni import ui
import weakref as weakref
__all__ = ['PrimNameModel', 'omni', 'ui', 'weakref']
class PrimNameModel(omni.ui._ui.AbstractValueModel):
    def __init__(self, prim_item):
        ...
    def destroy(self):
        ...
    def get_value_as_string(self):
        ...
    def set_value(self, value):
        ...
