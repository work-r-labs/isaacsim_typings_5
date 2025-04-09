"""
This module provides classes and functionality for manipulating primitive data to work with Fabric data accessors in the Omniverse Kit.
"""
from __future__ import annotations
from omni.kit.manipulator.prim.fabric.commands import TransformMultiPrimsFabricSRT
from omni.kit.manipulator.prim.fabric.data_accessor import FabricDataAccessor
from omni.kit.manipulator.prim.fabric.extension import ManipulatorPrim2FabricExt
from . import commands
from . import data_accessor
from . import extension
__all__: list = ['ManipulatorPrim2FabricExt', 'FabricDataAccessor', 'TransformMultiPrimsFabricSRT']
