"""
Bind material to prim dialog class
"""
from __future__ import annotations
import omni as omni
from omni.kit.material.library.listbox_widget import MaterialListBoxWidget
from omni.kit.material.library.search_widget import SearchWidget
from omni import ui
import pxr.Usd
from pxr import Usd
from pxr import UsdShade
import weakref as weakref
__all__ = ['LABEL_HEIGHT', 'MaterialDialogs', 'MaterialListBoxWidget', 'SearchWidget', 'Usd', 'UsdShade', 'omni', 'ui', 'weakref']
class MaterialDialogs:
    """
    Bind material to prim dialog class
    """
    def __init__(self):
        """
        Initialize class function.
        """
    def _bind_material_to_prim(self, stage: pxr.Usd.Stage, prims: list, window: weakref, material_path: str, model_strength: omni.ui._ui.AbstractItemModel):
        ...
    def _build_material_popup(self, material_list: typing.List[str], material_index: int, bind_material_fn: callable):
        ...
    def _get_bound_material_info(self, prim: pxr.Usd.Prim, materials_list: list) -> typing.List[str]:
        ...
    def _show_material_popup(self, name_field: omni.ui._ui.StringField, material_index: int, bind_material_fn: callable):
        ...
    def bind_material_to_prims_dialog(self, stage: pxr.Usd.Stage, prims: list) -> None:
        """
        
                Show dialog to user, so they an select material and bind to prims.
        
                Args:
                    stage (Usd.Stage): stage
                    prims (list): list of prims to bind to.
                
        """
    def destroy(self):
        """
        Destroy function. Class cleanup function.
        """
LABEL_HEIGHT: int = 18
_all__: list = ['MaterialDialogs']
