"""
This module provides utilities for working with transform operations in USD, including identifying, manipulating, and querying various aspects of transform operations.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
import pxr.Sdf
from pxr import Sdf
from pxr import UsdGeom
__all__ = ['INVERSE_PREFIX', 'INVERSE_XFORM_OP_PREFIX', 'PrimSelectionPayload', 'RESET_XFORM_STACK', 'Sdf', 'UsdGeom', 'XFROM_OP_PREFIX', 'XFROM_OP_TYPE_NAME', 'carb', 'get_inverse_op_Name', 'get_inverse_op_name', 'get_op_attr_name', 'get_op_name_suffix', 'get_op_precision', 'get_op_type', 'get_op_type_name', 'is_inverse_op', 'is_pivot_op', 'is_reset_xform_stack_op', 'is_valid_op_name', 'omni']
def _add_trs_op(payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload):
    ...
def get_inverse_op_name(ori_op_name, desired_invert):
    """
    Determines the inverse operation name based on the desired inversion state.
    
        Args:
            ori_op_name (str): The original operation name to invert.
            desired_invert (bool): Whether an inverse operation is desired.
    
        Returns:
            str: The inverse operation name or the original name based on the inversion state.
    """
def get_op_attr_name(op_name: str):
    """
    Gets the operation attribute name if it's a valid operation name.
    
        Args:
            op_name (str): The name of the operation.
    
        Returns:
            str or None: The operation attribute name or None if invalid.
    """
def get_op_name_suffix(op_name: str):
    """
    Extracts the suffix from an operation name if present.
    
        Args:
            op_name (str): The full name of the operation.
    
        Returns:
            str or None: The operation name suffix or None if not available.
    """
def get_op_precision(attr_type_name: pxr.Sdf.ValueTypeName):
    """
    Determines the precision of an operation based on its attribute type name.
    
        Args:
            attr_type_name (Sdf.ValueTypeName): The attribute type name.
    
        Returns:
            UsdGeom.XformOp.Precision: The precision of the operation.
    """
def get_op_type(op_name: str):
    """
    Retrieves the USDGeom Xform operation type for a given operation name.
    
        Args:
            op_name (str): The name of the operation.
    
        Returns:
            UsdGeom.XformOp.Type or None: The operation type or None if not found.
    """
def get_op_type_name(op_name: str):
    """
    Extracts the operation type name from an operation name.
    
        Args:
            op_name (str): The full name of the operation.
    
        Returns:
            str or None: The operation type name or None if not extractable.
    """
def is_inverse_op(op_name: str):
    """
    Checks if an operation name represents an inverse operation.
    
        Args:
            op_name (str): The name of the operation to check.
    
        Returns:
            bool: True if it's an inverse operation, otherwise False.
    """
def is_pivot_op(op_name: str):
    """
    Determines if an operation name signifies a pivot operation.
    
        Args:
            op_name (str): The name of the operation to check.
    
        Returns:
            bool: True if it's a pivot operation, otherwise False.
    """
def is_reset_xform_stack_op(op_name: str):
    """
    Checks if an operation name indicates a reset transform stack operation.
    
        Args:
            op_name (str): The name of the operation to check.
    
        Returns:
            bool: True if it resets the transform stack, otherwise False.
    """
def is_valid_op_name(op_name: str):
    """
    Checks if an operation name is valid based on predefined criteria.
    
        Args:
            op_name (str): The name of the operation to validate.
    
        Returns:
            bool: True if the operation name is valid, otherwise False.
    """
INVERSE_PREFIX: str = '!invert!'
INVERSE_XFORM_OP_PREFIX: str = '!invert!xformOp:'
RESET_XFORM_STACK: str = '!resetXformStack!'
XFROM_OP_PREFIX: str = 'xformOp:'
XFROM_OP_TYPE_NAME: list = ['translate', 'scale', 'rotateX', 'rotateY', 'rotateZ', 'rotateXYZ', 'rotateXZY', 'rotateYXZ', 'rotateYZX', 'rotateZXY', 'rotateZYX', 'orient', 'transform']
get_inverse_op_Name = get_inverse_op_name
