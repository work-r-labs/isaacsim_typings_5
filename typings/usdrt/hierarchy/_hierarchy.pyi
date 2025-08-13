from __future__ import annotations
import omni.core._core
import typing
import usdrt.Gf._Gf
import usdrt.helpers._helpers
__all__: list[str] = ['IFabricHierarchy']
class IFabricHierarchy(_IFabricHierarchy):
    @typing.overload
    def __init__(self, arg0: omni.core._core.IObject) -> None:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    def get_fabric_hierarchy(self, fabric_id: usdrt.helpers._helpers.FabricId, stage_id: usdrt.helpers._helpers.UsdStageId) -> IFabricHierarchy:
        ...
    def get_fabric_id(self: _IFabricHierarchy) -> usdrt.helpers._helpers.FabricId:
        ...
    def get_local_xform(self: _IFabricHierarchy, path: usdrt.helpers._helpers.PathC) -> usdrt.Gf._Gf.Matrix4d:
        ...
    def get_reset_xform_stack(self: _IFabricHierarchy, path: usdrt.helpers._helpers.PathC) -> bool:
        ...
    def get_world_xform(self: _IFabricHierarchy, path: usdrt.helpers._helpers.PathC) -> usdrt.Gf._Gf.Matrix4d:
        ...
    def mark_time_sampled_xform_dirty(self: _IFabricHierarchy, path: usdrt.helpers._helpers.PathC) -> None:
        ...
    def set_local_xform(self: _IFabricHierarchy, path: usdrt.helpers._helpers.PathC, xform: usdrt.Gf._Gf.Matrix4d) -> bool:
        ...
    def set_reset_xform_stack(self: _IFabricHierarchy, path: usdrt.helpers._helpers.PathC, reset: bool) -> bool:
        ...
    def set_time_sampled_xform_hint(self: _IFabricHierarchy, new_time: float, resync_occurred: bool) -> None:
        ...
    def set_world_xform(self: _IFabricHierarchy, path: usdrt.helpers._helpers.PathC, xform: usdrt.Gf._Gf.Matrix4d) -> bool:
        ...
    def track_local_xform_changes(self: _IFabricHierarchy, enabled: bool) -> None:
        ...
    def track_reset_xform_stack_changes(self: _IFabricHierarchy, enabled: bool) -> None:
        ...
    def track_world_xform_changes(self: _IFabricHierarchy, enabled: bool) -> None:
        ...
    def update_world_xforms(self: _IFabricHierarchy) -> None:
        ...
    def update_world_xforms_gpu(self: _IFabricHierarchy, no_structural_changes_hint: bool = False) -> bool:
        """
        Update world transforms and extents from local transforms on the GPU.
        
        This function is meant to be used after only GPU local transform updates happened in Fabric.
        
        noStructuralChangesHint - Hint to indicate that there were no structural changes since the last call
                                  When set to true but there were structural changes the behavior is undefined
        
        Returns: true if the update was successful, false otherwise
        """
class _IFabricHierarchy(omni.core._core.IObject):
    pass
