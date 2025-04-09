from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.usd import layers
from omni.kit.widget.stage.models.name_model import PrimNameModel
from omni.kit.widget.stage.models.type_model import TypeModel
from omni.kit.widget.stage.models.visibility_model import VisibilityModel
from omni import ui
from pxr import Sdf
import pxr.Sdf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
__all__: list = ['StageItem']
class StageItem(omni.ui._ui.AbstractItem):
    """
    
        A single AbstractItemModel item that represents a single prim. StageItem is a cached view of the prim.
        
    """
    def _StageItem__get_auto_reload_status(self):
        ...
    def _StageItem__get_live_status(self):
        ...
    def _StageItem__get_outdated_status(self):
        ...
    def _StageItem__get_payrefs(self):
        ...
    def _StageItem__has_missing_payrefs(self):
        ...
    def __init__(self, path: pxr.Sdf.Path, stage, stage_model, flat = False, root_identifier = None, load_payloads = False, check_missing_references = False):
        """
        
                Creates an instance of StageItem.
        
                Args:
                    path (Sdf.Path): The prim path for the item.
                    stage (Usd.Stage): Unused.
                    stage_model (omni.kit.widget.stage.StageModel): The StageModel of the current item.
                
        """
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def _update_flags_internal(self):
        ...
    def _update_prim(self):
        ...
    def _update_visibility(self):
        ...
    def destroy(self):
        """
        Internal method to release resources.
        """
    def set_default_prim(self, is_default):
        """
        Deprecated.
        """
    def update_flags(self, prim = None):
        """
        
                Refreshes item states from USD.
        
                Keyword Args:
                    prim: Unused.
                
        """
    @property
    def abstract(self) -> bool:
        """
        
                If the prim is abstract. If no prim associated, return False.
        
                Returns:
                    bool: prim abstract
                
        """
    @property
    def active(self) -> bool:
        """
        
                If the prim is active. If no prim associated, return False.
        
                Returns:
                    bool: prim active
                
        """
    @property
    def auto_reload(self) -> bool:
        """
        
                Whether this prim is configured to be auto-reload when its references or payloads are outdated.
        
                Returns:
                    bool: Set to be auto-reloaded or not.
                
        """
    @property
    def check_missing_references(self):
        """
        Deprecated: It will always check missing references now.
        """
    @check_missing_references.setter
    def check_missing_references(self, value):
        """
        Deprecated.
        """
    @property
    def child_filtered(self) -> bool:
        """
        
                Returns if any child of stage item is filtered.
        
                Returns:
                    bool: True if any child is filtered.
                
        """
    @child_filtered.setter
    def child_filtered(self, value: bool):
        """
        
                Sets if any child of the stage item is filtered.
        
                Args:
                    value (bool): Value to set.
                
        """
    @property
    def children(self):
        """
        
                Returns children items. If children are not populated yet, they will be populated.
        
                Returns:
                    List[StageItem]: Child items.
                
        """
    @property
    def display_name(self) -> str:
        """
        
                The display name of prim from the metadata. If not set, default to path name.
        
                Returns:
                    str
                
        """
    @property
    def filtered(self) -> bool:
        """
        
                Whether the current stage item is filtered or not by search string.
        
                Returns:
                    bool: Filtered state.
                
        """
    @filtered.setter
    def filtered(self, value: bool):
        """
        
                Sets the filtered state to the given value.
        
                Args:
                    value (bool): Filtered state.
                
        """
    @property
    def has_missing_references(self) -> bool:
        """
        
                Whether the prim includes any missing references or payloads or not, checked recursively.
        
                Returns:
                    bool: If any descendant of the prim has missing reference of payload.
                
        """
    @property
    def in_session(self) -> bool:
        """
        
                Whether this prim includes references or payloads that are in a live session.
        
                Returns:
                    bool: If the prim includes references or payloads in live session.
                
        """
    @property
    def inherits(self) -> bool:
        """
        
                Whether the prim has authored inherits.
        
                Returns:
                    bool: If prim has authored inherits
                
        """
    @property
    def instance_proxy(self) -> bool:
        """
        
                Whether the prim is an instance proxy or not.
        
                Returns:
                    bool: If the prim is an instance proxy
                
        """
    @property
    def instanceable(self) -> bool:
        """
        
                If the prim is instanceable.
        
                Returns:
                    bool: Prim instanceable
                
        """
    @property
    def is_class(self) -> bool:
        """
        
                If this prim is a Sdf.SpecifierClass. If no prim associated, return False.
        
                Returns:
                    bool:
                
        """
    @property
    def is_default(self) -> bool:
        """
        
                Whether this prim is the default prim or not.
        
                Returns:
                    bool: If this prim is the default prim.
                
        """
    @property
    def is_flat(self) -> bool:
        """
        
                If the stage model is in flat mode. If no stage model associated, returns False.
        
                Returns:
                    bool: If the stage model is in flat mode
                
        """
    @is_flat.setter
    def is_flat(self, flat: bool):
        """
        Unused.
        """
    @property
    def is_outdated(self) -> bool:
        """
        
                Whether this prim includes references or payloads that has new changes to fetch or not.
        
                Returns:
                    bool: If the prim is outdated.
                
        """
    @property
    def load_payloads(self) -> bool:
        """
        
                Whether to load payloads. If no stage model associated, returns False.
        
                Returns:
                    bool: Load payloads or not.
                
        """
    @property
    def name(self) -> str:
        """
        
                The Sdf path name.
        
                Returns:
                    str
                
        """
    @property
    def name_model(self) -> omni.kit.widget.stage.models.name_model.PrimNameModel:
        """
        
                The prim name model.
        
                Returns:
                    PrimNameModel: The prim name model.
                
        """
    @property
    def path(self) -> pxr.Sdf.Path:
        """
        
                Prim path.
        
                Returns:
                    Sdf.Path: The prim path.
                
        """
    @property
    def payloads(self) -> bool:
        """
        
                Whether the prim has authored payloads.
        
                Returns:
                    bool: If prim has authored payloads
                
        """
    @property
    def payrefs(self) -> typing.List[str]:
        """
        
                All external references and payloads that influence this prim.
        
                Returns:
                    List[str]: References and payloads associated with this prim.
                
        """
    @property
    def prim(self) -> pxr.Usd.Prim:
        """
        
                The prim handle.
        
                Returns:
                    Usd.Prim: The prim handle.
                
        """
    @property
    def references(self) -> bool:
        """
        
                Whether the prim has authored references.
        
                Returns:
                    bool: If prim has authored references
                
        """
    @property
    def root_identifier(self) -> typing.Optional[str]:
        """
        
                Returns the root layer's identifier of the stage this prim belongs to.
        
                Returns:
                    Optional[str]: The root layer identifier if stage exists else None
                
        """
    @property
    def specializes(self) -> bool:
        """
        
                Whether the prim has authored specializes.
        
                Returns:
                    bool: If prim has authored specializes
                
        """
    @property
    def stage(self) -> typing.Optional[pxr.Usd.Stage]:
        """
        
                USD stage the prim belongs to.
        
                Returns:
                    Optional[Usd.Stage]: The associated USD stage of the stage model.
                
        """
    @property
    def stage_model(self):
        """
        
                StageModel this StageItem belongs to.
        
                Returns:
                    omni.kit.widget.stage.StageModel: The StageModel
                
        """
    @property
    def type_model(self) -> omni.kit.widget.stage.models.type_model.TypeModel:
        """
        
                The prim type model.
        
                Returns:
                    TypeModel: The prim type model.
                
        """
    @property
    def type_name(self) -> str:
        """
        
                Type name of the prim. Return empty string if no prim associated.
        
                Returns:
                    str: prim type name
                
        """
    @property
    def usd_context(self) -> typing.Optional[omni.usd._usd.UsdContext]:
        """
        
                The usd context for the current stage of the stage model.
        
                Returns:
                    Optional[omni.usd.UsdContext]: The associated usd context of the stage model.
                
        """
    @property
    def visibility_model(self) -> omni.kit.widget.stage.models.visibility_model.VisibilityModel:
        """
        
                The prim visibility model.
        
                Returns:
                    TypeModel: The prim visibility model.
                
        """
    @property
    def visible(self) -> bool:
        """
        
                If the prim is visible.
        
                Returns:
                    bool: visibility
                
        """
