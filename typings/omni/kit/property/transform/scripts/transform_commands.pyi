"""
Provides commands for manipulating transformation properties of USD prims within the Omniverse Kit.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.property.transform.scripts import xform_op_utils
from omni.kit.usd_undo.layer_undo import UsdLayerUndo
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
import typing
__all__ = ['AddXformOpCommand', 'ChangeRotationOpCommand', 'EnableXformOpCommand', 'Gf', 'RemoveXformOpAndAttrbuteCommand', 'RemoveXformOpCommand', 'Sdf', 'Usd', 'UsdGeom', 'UsdLayerUndo', 'carb', 'omni', 'xform_op_utils']
class AddXformOpCommand(omni.kit.commands.command.Command):
    """
    A class that encapsulates a command to add various transformation operations (xformOps) to a USD prim's xformOpOrder.
    
        This command allows for adding translation, rotation, scaling, orientation, transformation matrix, and pivot operations. The precision for these operations can be specified. It also handles the proper ordering of these operations within the xformOpOrder attribute of the prim.
    
            Args:
                payload: The payload containing information about the stage and prims to modify.
                precision (UsdGeom.XformOp.Precision): The precision of the xformOps to be added.
                rotation_order (str): The order of rotation components (e.g., 'XYZ').
                add_translate_op (bool): Whether to add a translate operation.
                add_orient_op (bool): Whether to add an orientation operation.
                add_scale_op (bool): Whether to add a scale operation.
                add_transform_op (bool): Whether to add a transform operation (4x4 matrix).
                add_pivot_op (bool): Whether to add a pivot operation.
                add_rotateXYZ_op (bool, optional): Whether to add a rotate operation in XYZ order. Deprecated in favor of add_rotate_xyz_op.
                add_rotate_xyz_op (bool, optional): Whether to add a rotate operation in specified order.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, payload, precision, rotation_order, add_translate_op, add_orient_op, add_scale_op, add_transform_op, add_pivot_op, add_rotateXYZ_op = None, add_rotate_xyz_op = None):
        """
        Initializes the command to add a transformation operation.
        """
    def do(self):
        """
        Executes the command to add the specified transformation operation.
        """
    def undo(self):
        """
        Reverts the addition of the transformation operation.
        """
class ChangeRotationOpCommand(omni.kit.commands.command.Command):
    """
    A command to change the rotation XformOp in a USD stage.
    
        This command updates the xformOpOrder, deletes the source xformOp attribute, creates a destination xformOp attribute, and copies the values from the source to the destination. If the operation is an inverse operation, it will add '!invert!' in the xformOpOrder.
    
            Args:
                src_op_attr_path (str): Path of the source xformOp attribute.
                op_name (str): Name of the operation.
                dst_op_attr_name (str): Path of the destination xformOp attribute.
                is_inverse_op (bool): Indicates if the operation is an inverse operation.
                auto_target_layer (bool): Automatically target the correct layer for changes.
    
            Example:
                To change from xformOp:rotateZYX to xformOp:rotateXYZ, this command will:
                    1) Update the xformOpOrder.
                    2) Delete the xformOp:rotateZYX attribute.
                    3) Create the xformOp:rotateXYZ attribute.
                    4) Copy the values from xformOp:rotateZYX to xformOp:rotateXYZ.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, src_op_attr_path: str, op_name: str, dst_op_attr_name: str, is_inverse_op: bool, auto_target_layer: bool = True):
        """
        Initializes the ChangeRotationOpCommand instance.
        """
    def _change_rotation_op(self):
        ...
    def _get_undo(self, layer):
        ...
    def do(self):
        """
        Executes the rotation operation change.
        """
    def undo(self):
        """
        Reverts the rotation operation change.
        """
class EnableXformOpCommand(omni.kit.commands.command.Command):
    """
    A command to add an attribute's corresponding XformOp to the xformOpOrder array.
    
        Args:
            op_attr_path (str): The path of the xformOp attribute to be added to the xformOpOrder.
    
        Example:
            To add xformOp:translate to the xformOpOrder token array, ensure that the xformOp:translate attribute exists
            and is not already present in the xformOpOrder.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, op_attr_path: str):
        """
        Initializer for the EnableXformOpCommand object.
        """
    def do(self):
        """
        Executes the command, enabling the specified transformation operation.
        """
    def undo(self):
        """
        Reverts the changes made by the `do` method, effectively undoing the command.
        """
class RemoveXformOpAndAttrbuteCommand(omni.kit.commands.command.Command):
    """
    A command to remove an XformOp and its attribute from the xformOpOrder array.
    
        Args:
            op_order_attr_path (str): Path of the xformOpOrder attribute.
            op_name (str): Name of the xformOp to be removed.
            op_order_index (int): Index of the xformOp in the xformOpOrder array.
    
        Example:
            To remove xformOp:translate from the xformOpOrder token array while keeping the xformOp:translate attribute itself.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, op_order_attr_path: str, op_name: str, op_order_index: int):
        """
        Constructor for the command that removes an XformOp and its attribute.
        """
    def do(self):
        """
        Executes the command to remove the specified xformOp and its attribute.
        """
    def undo(self):
        """
        Undoes the removal of the specified xformOp and its attribute.
        """
class RemoveXformOpCommand(omni.kit.commands.command.Command):
    """
    A command to remove an XformOp from the xformOpOrder attribute without deleting the attribute itself.
    
        Args:
            op_order_attr_path (str): The path of the xformOpOrder attribute.
            op_name (str): The name of the xformOp to be removed.
            op_order_index (int): The index of the xformOp in the xformOpOrder array.
    
        Example:
            If one needs to remove xformOp:translate from the xformOpOrder token array,
            this command would be used while keeping the xformOp:translate attribute intact.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, op_order_attr_path: str, op_name: str, op_order_index: int):
        """
        Initializes the RemoveXformOpCommand.
        
                Detailed documentation is optional.
        """
    def do(self):
        """
        Executes the command to remove a specific XformOp.
        """
    def undo(self):
        """
        Reverts the removal of a specific XformOp.
        """
