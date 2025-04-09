from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni.kit.helper.file_utils.extension import FileEventModel
from omni.kit.window.file_exporter import get_file_exporter
import os as os
from pxr import Gf
import pxr.Gf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
import pxr.UsdGeom
from pxr import UsdGeom
from pxr import UsdUI
import typing
__all__: list = ['export', 'Export']
class ExportPrimUSD:
    """
    Utility class for exporting USD prims.
    """
    def _ExportPrimUSD__on_apply_save(self, prims: typing.List[pxr.Usd.Prim], filename: str, dirname: str, extension: str, selections: typing.List[str] = list()):
        """
        Called when the user presses the Save button in the dialog
        """
    def __init__(self, select_msg = 'Save As', save_msg = 'Save', save_dir = None, postfix_name = None):
        """
        
                Instantiates an instance of this utility class.
        
                Keyword Args:
                    select_msg (str): Title for file exporter dialog, default to "Save As"
                    save_msg (str): Deprecated, used for legacy usd prim export.
                    save_dir (Optional[str]): Deprecated, used for legacy usd prim export.
                    postfix_name (Optional[str]): Deprecated, used for legacy usd prim export.
                
        """
    def destroy(self):
        """
        Destroys the instance.
        """
    def export(self, prims: typing.List[pxr.Usd.Prim]):
        """
        
                Main function for exporting prims. Displays a file exporter dialog for user interaction.
        
                Args:
                    prims (List[Usd.Prim]): Prims to be exported.
                
        """
class ExportPrimUSDLegacy:
    """
    
        It's still used in Material Graph
        
    """
    EXPORT_USD_EXTS: typing.ClassVar[tuple] = ('usd', 'usda', 'usdc')
    def _ExportPrimUSDLegacy__on_apply_save(self, filename: str, dir: str):
        """
        Called when the user presses the Save button in the dialog
        """
    def _ExportPrimUSDLegacy__on_filter_item(self, item: FileBrowserItem) -> bool:
        ...
    def __init__(self, select_msg = 'Save As', save_msg = 'Save', save_dir = None, postfix_name = None):
        ...
    def destroy(self):
        ...
    def export(self, prim):
        ...
def __on_stage_open(event: carb.events._events.IEvent):
    """
    Update default save directory on stage open.
    """
def __set_xform_prim_transform(prim: pxr.UsdGeom.Xformable, transform: pxr.Gf.Matrix4d):
    ...
def _add_to_recent_files(filename: str):
    """
    Utility to add the filename to recent file list.
    """
def _duplicate_variant_sets(source_prim: pxr.Usd.Prim, target_prim: pxr.Usd.Prim):
    """
    Utility function that helps duplication of variant sets from the source prim to the target prim.
    """
def _get_all_children(prim: pxr.Usd.Prim) -> typing.Set[pxr.Usd.Prim]:
    """
    Utility function that gets all children of the given prim.
    """
def _get_stage_open_sub():
    ...
def _remove_duplicate_prims(prim_list: typing.List[pxr.Usd.Prim], stage: pxr.Usd.Stage) -> typing.List[pxr.Usd.Prim]:
    """
    
        Utility function that removes duplicated prims.
        For example, prims that are selected but are children of other selected prims are already included so can be removed.
        
    """
def export(*args, **kwds):
    """
    
        Exports specified prims to an external USD file with the given path.
        If more than one prim is specified, the parent transforms will be exported automatically.
    
        Args:
            path (str): The target layer path.
            prims (List[Usd.Prim]): Prims to export.
        
    """
FILE_SAVED_EVENT: int = 8148521607818097614
_default_save_dir: str = ''
last_dir = None
