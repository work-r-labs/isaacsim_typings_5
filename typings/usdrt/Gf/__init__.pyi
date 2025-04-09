from __future__ import annotations
import pxr as _pxr
from usdrt.Gf._Gf import Abs
from usdrt.Gf._Gf import Absf
from usdrt.Gf._Gf import BBox3d
from usdrt.Gf._Gf import Clamp
from usdrt.Gf._Gf import Clampf
from usdrt.Gf._Gf import CompDiv
from usdrt.Gf._Gf import CompMult
from usdrt.Gf._Gf import Cross
from usdrt.Gf._Gf import DegreesToRadians
from usdrt.Gf._Gf import Dot
from usdrt.Gf._Gf import FindClosestPoints
from usdrt.Gf._Gf import FitPlaneToPoints
from usdrt.Gf._Gf import Frustum
from usdrt.Gf._Gf import GetComplement
from usdrt.Gf._Gf import GetLength
from usdrt.Gf._Gf import GetNormalized
from usdrt.Gf._Gf import GetProjection
from usdrt.Gf._Gf import IsClose
from usdrt.Gf._Gf import Lerp
from usdrt.Gf._Gf import Lerpf
from usdrt.Gf._Gf import Line
from usdrt.Gf._Gf import LineSeg
from usdrt.Gf._Gf import Matrix2d
from usdrt.Gf._Gf import Matrix2f
from usdrt.Gf._Gf import Matrix3d
from usdrt.Gf._Gf import Matrix3f
from usdrt.Gf._Gf import Matrix4d
from usdrt.Gf._Gf import Matrix4f
from usdrt.Gf._Gf import Max
from usdrt.Gf._Gf import Min
from usdrt.Gf._Gf import Normalize
from usdrt.Gf._Gf import Plane
from usdrt.Gf._Gf import Quatd
from usdrt.Gf._Gf import Quatf
from usdrt.Gf._Gf import Quath
from usdrt.Gf._Gf import RadiansToDegrees
from usdrt.Gf._Gf import Range1d
from usdrt.Gf._Gf import Range1f
from usdrt.Gf._Gf import Range2d
from usdrt.Gf._Gf import Range2f
from usdrt.Gf._Gf import Range3d
from usdrt.Gf._Gf import Range3f
from usdrt.Gf._Gf import Ray
from usdrt.Gf._Gf import Rect2i
from usdrt.Gf._Gf import Rotation
from usdrt.Gf._Gf import Slerp
from usdrt.Gf._Gf import Sqr
from usdrt.Gf._Gf import Sqrt
from usdrt.Gf._Gf import Transform
from usdrt.Gf._Gf import Vec2d
from usdrt.Gf._Gf import Vec2f
from usdrt.Gf._Gf import Vec2h
from usdrt.Gf._Gf import Vec2i
from usdrt.Gf._Gf import Vec3d
from usdrt.Gf._Gf import Vec3f
from usdrt.Gf._Gf import Vec3h
from usdrt.Gf._Gf import Vec3i
from usdrt.Gf._Gf import Vec4d
from usdrt.Gf._Gf import Vec4f
from usdrt.Gf._Gf import Vec4h
from usdrt.Gf._Gf import Vec4i
from . import _Gf
__all__ = ['Abs', 'Absf', 'BBox3d', 'Clamp', 'Clampf', 'CompDiv', 'CompMult', 'Cross', 'DegreesToRadians', 'Dot', 'FindClosestPoints', 'FitPlaneToPoints', 'Frustum', 'GetComplement', 'GetLength', 'GetNormalized', 'GetProjection', 'IsClose', 'Lerp', 'Lerpf', 'Line', 'LineSeg', 'Matrix2d', 'Matrix2f', 'Matrix3d', 'Matrix3f', 'Matrix4d', 'Matrix4f', 'Max', 'Min', 'Normalize', 'Plane', 'Quatd', 'Quatf', 'Quath', 'RadiansToDegrees', 'Range1d', 'Range1f', 'Range2d', 'Range2f', 'Range3d', 'Range3f', 'Ray', 'Rect2i', 'Rotation', 'Slerp', 'Sqr', 'Sqrt', 'Transform', 'Vec2d', 'Vec2f', 'Vec2h', 'Vec2i', 'Vec3d', 'Vec3f', 'Vec3h', 'Vec3i', 'Vec4d', 'Vec4f', 'Vec4h', 'Vec4i', 'convertToPxr', 'convertToUsdrt']
def convertToPxr(obj):
    """
    
        Convenience helper to convertToPxr from _pxr.Gf to pxr.Gf types.
        
    """
def convertToUsdrt(obj):
    """
    
        Convenience helper to convert from pxr.Gf to usdrt.Gf types.
        
    """
__copyright__: str = 'Copyright (c) 2022, NVIDIA CORPORATION. All rights reserved.'
__license__: str = '\nNVIDIA CORPORATION and its licensors retain all intellectual property\nand proprietary rights in and to this software, related documentation\nand any modifications thereto. Any use, reproduction, disclosure or\ndistribution of this software and related documentation without an express\nlicense agreement from NVIDIA CORPORATION is strictly prohibited.\n'
