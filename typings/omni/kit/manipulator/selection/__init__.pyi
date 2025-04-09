"""
Selection Shape/Box Manipulator
"""
from __future__ import annotations
from omni.kit.manipulator.selection.manipulator import SelectionManipulator
from omni.kit.manipulator.selection.manipulator import SelectionMode
from omni.kit.manipulator.selection.model import SelectionShapeModel
from . import manipulator
from . import model
__all__: list = ['SelectionManipulator', 'SelectionMode', 'SelectionShapeModel']
