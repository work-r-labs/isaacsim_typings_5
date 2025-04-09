from __future__ import annotations
from omni import ui
import omni.ui._ui
from pxr import Sdf
from pxr import Tf
__all__: list = ['PrimNameModel']
class PrimNameModel(omni.ui._ui.AbstractValueModel):
    """
    The model that changes the prim name
    """
    @staticmethod
    def _get_path_converter() -> typing.Callable:
        """
        
                The Path conversion function to use for prim paths.
        
                Returns:
                    Callable: The path conversion function.
                
        """
    @staticmethod
    def _make_valid_identifier(name: str):
        ...
    def __init__(self, stage_item):
        ...
    def _refresh_name_prefix_and_suffix(self):
        ...
    def begin_edit(self):
        ...
    def destroy(self):
        ...
    def end_edit(self):
        ...
    def get_value_as_string(self):
        """
        Reimplemented get string
        """
    def rebuild(self):
        ...
    def set_value(self, value):
        """
        Reimplemented set
        """
    @property
    def _label_on_begin(self):
        ...
    @property
    def _name_prefix(self):
        """
        Name prefix without suffix number, e.g, `abc_01` will return abc. It's used for column sort.
        """
    @property
    def _old_label(self):
        ...
    @property
    def _prim_path(self):
        """
        DEPRECATED: to ensure back-compatibility.
        """
    @property
    def _suffix_order(self):
        """
        Number suffix, e.g, `abc_01` will return 01. It's used for column sort.
        """
    @property
    def label(self):
        ...
    @label.setter
    def label(self, value: str):
        ...
    @property
    def path(self):
        ...
    @property
    def stage_item(self):
        ...
