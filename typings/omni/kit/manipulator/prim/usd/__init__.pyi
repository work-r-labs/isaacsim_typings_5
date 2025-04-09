"""
This module provides classes and functions for manipulating USD prims within the Omniverse Kit using data accessors for the Universal Scene Description (USD) contexts.
"""
from __future__ import annotations
from omni.kit.manipulator.prim.usd.data_accessor import UsdDataAccessor
from omni.kit.manipulator.prim.usd.extension import ManipulatorPrim2UsdExt
from . import data_accessor
from . import extension
__all__: list = ['UsdDataAccessor']
