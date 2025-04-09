from __future__ import annotations
import carb as carb
import omni as omni
import typing
import usdrt as usdrt
__all__: list = ['TransformMultiPrimsFabricSRT']
class TransformMultiPrimsFabricSRT(omni.kit.commands.command.Command):
    """
    
        Transform Fabric primitives in Fabric stage.
        Args:
            paths (List[usdrt.Sdf._Sdf.Path]): List of path strings for selected prims.
            new_translations (List[usdrt.Gf.Vec3d]): List of new translation values for prims.
            new_rotation_eulers (List[usdrt.Gf.Vec3d]): List of new rotation euler angles for prims.
            new_rotation_orders (List[usdrt.Gf.Vec3i]): List of new rotation orders for prims.
            new_scales (List[usdrt.Gf.Vec3d]): List of new scale values for prims.
            old_translations (List[usdrt.Gf.Vec3d]): Previous translations for undo functionality.
            old_rotation_eulers (List[usdrt.Gf.Vec3d]): Previous rotations in Euler form for undo.
            old_rotation_orders (List[usdrt.Gf.Vec3i]): Previous rotation orders for undo functionality.
            old_scales (List[usdrt.Gf.Vec3d]): Previous scale values for undo functionality.
            stage (usdrt.Usd.Stage): The stage to operate.
            time_code (usdrt.Usd.TimeCode): The timecode to change. Default is usdrt.Usd.TimeCode.Default().
            write_to_stage (bool):Whether to write the prim after it's transformed.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, paths: list[usdrt.Sdf._Sdf.Path], new_translations: typing.List[usdrt.Gf._Gf.Vec3d] = None, new_rotation_eulers: typing.List[usdrt.Gf._Gf.Vec3d] = None, new_rotation_orders: typing.List[usdrt.Gf._Gf.Vec3i] = None, new_scales: typing.List[usdrt.Gf._Gf.Vec3d] = None, old_translations: typing.List[usdrt.Gf._Gf.Vec3d] = None, old_rotation_eulers: typing.List[usdrt.Gf._Gf.Vec3d] = None, old_rotation_orders: typing.List[usdrt.Gf._Gf.Vec3i] = None, old_scales: typing.List[usdrt.Gf._Gf.Vec3d] = None, stage = None, time_code: usdrt.Usd._Usd.TimeCode = ..., write_to_stage: bool = False):
        """
        Initializes the command for transforming multiple primitives in a Fabric stage.
        """
    def _matrix_from_euler(self, eulers: typing.Tuple[float, ...], ro: usdrt.Gf._Gf.Vec3i):
        ...
    def _set_transform(self, prim, translation, rotation_order, rotation_eulers, scale, time_code):
        ...
    def do(self):
        """
        Performs the transformation on multiple primitives.
        """
    def undo(self):
        """
        Reverts the transformation applied to the primitives.
        """
