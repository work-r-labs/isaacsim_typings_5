from __future__ import annotations
import numpy as np
import os as os
import warp as wp
from xml.etree import ElementTree as ET
__all__: list[str] = ['ET', 'MuscleUnit', 'Skeleton', 'np', 'os', 'parse_snu', 'wp']
class MuscleUnit:
    def __init__(self):
        ...
class Skeleton:
    def __init__(self, root_xform, skeleton_file, muscle_file, builder, filter, armature = 0.0):
        ...
    def parse_muscles(self, filename, builder):
        ...
    def parse_skeleton(self, filename, builder, filter, root_xform, armature):
        ...
def parse_snu(root_xform, skeleton_file, muscle_file, builder, filter, armature = 0.0):
    ...
