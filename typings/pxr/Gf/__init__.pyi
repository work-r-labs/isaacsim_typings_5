"""

Graphics Foundation
This package defines classes for fundamental graphics types and operations.
"""
from __future__ import annotations
import pxr.Tf
import typing
__all__: list[str] = ['BBox3d', 'Camera', 'DualQuatd', 'DualQuatf', 'DualQuath', 'Frustum', 'Interval', 'Line', 'LineSeg', 'MIN_ORTHO_TOLERANCE', 'MIN_VECTOR_LENGTH', 'Matrix2d', 'Matrix2f', 'Matrix3d', 'Matrix3f', 'Matrix4d', 'Matrix4f', 'MultiInterval', 'Plane', 'Quatd', 'Quaternion', 'Quatf', 'Quath', 'Range1d', 'Range1f', 'Range2d', 'Range2f', 'Range3d', 'Range3f', 'Ray', 'Rect2i', 'Rotation', 'Size2', 'Size3', 'Transform', 'Vec2d', 'Vec2f', 'Vec2h', 'Vec2i', 'Vec3d', 'Vec3f', 'Vec3h', 'Vec3i', 'Vec4d', 'Vec4f', 'Vec4h', 'Vec4i']
class BBox3d(Boost.Python.instance):
    """
    Arbitrarily oriented 3D bounding box
    """
    __instance_size__: typing.ClassVar[int] = 336
    @staticmethod
    def Combine(*args, **kwargs):
        ...
    @staticmethod
    def ComputeAlignedBox(*args, **kwargs):
        ...
    @staticmethod
    def ComputeAlignedRange(*args, **kwargs):
        ...
    @staticmethod
    def ComputeCentroid(*args, **kwargs):
        ...
    @staticmethod
    def GetBox(*args, **kwargs):
        ...
    @staticmethod
    def GetInverseMatrix(*args, **kwargs):
        ...
    @staticmethod
    def GetMatrix(*args, **kwargs):
        ...
    @staticmethod
    def GetRange(*args, **kwargs):
        ...
    @staticmethod
    def GetVolume(*args, **kwargs):
        ...
    @staticmethod
    def HasZeroAreaPrimitives(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def SetHasZeroAreaPrimitives(*args, **kwargs):
        ...
    @staticmethod
    def SetMatrix(*args, **kwargs):
        ...
    @staticmethod
    def SetRange(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def box(*args, **kwargs):
        ...
    @box.setter
    def box(*args, **kwargs):
        ...
    @property
    def hasZeroAreaPrimitives(*args, **kwargs):
        ...
    @hasZeroAreaPrimitives.setter
    def hasZeroAreaPrimitives(*args, **kwargs):
        ...
    @property
    def matrix(*args, **kwargs):
        ...
    @matrix.setter
    def matrix(*args, **kwargs):
        ...
class Camera(Boost.Python.instance):
    class FOVDirection(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'Camera'
        allValues: typing.ClassVar[tuple]  # value = (Gf.Camera.FOVHorizontal, Gf.Camera.FOVVertical)
        @staticmethod
        def GetValueFromName(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class Projection(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'Camera'
        allValues: typing.ClassVar[tuple]  # value = (Gf.Camera.Perspective, Gf.Camera.Orthographic)
        @staticmethod
        def GetValueFromName(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    APERTURE_UNIT: typing.ClassVar[float] = 0.1
    DEFAULT_HORIZONTAL_APERTURE: typing.ClassVar[float] = 20.955
    DEFAULT_VERTICAL_APERTURE: typing.ClassVar[float] = 15.290799999999999
    FOCAL_LENGTH_UNIT: typing.ClassVar[float] = 0.1
    FOVHorizontal: typing.ClassVar[FOVDirection]  # value = Gf.Camera.FOVHorizontal
    FOVVertical: typing.ClassVar[FOVDirection]  # value = Gf.Camera.FOVVertical
    Orthographic: typing.ClassVar[Projection]  # value = Gf.Camera.Orthographic
    Perspective: typing.ClassVar[Projection]  # value = Gf.Camera.Perspective
    __instance_size__: typing.ClassVar[int] = 216
    @staticmethod
    def GetFieldOfView(*args, **kwargs):
        ...
    @staticmethod
    def SetFromViewAndProjectionMatrix(*args, **kwargs):
        ...
    @staticmethod
    def SetOrthographicFromAspectRatioAndSize(*args, **kwargs):
        ...
    @staticmethod
    def SetPerspectiveFromAspectRatioAndFieldOfView(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def aspectRatio(*args, **kwargs):
        ...
    @property
    def clippingPlanes(*args, **kwargs):
        ...
    @clippingPlanes.setter
    def clippingPlanes(*args, **kwargs):
        ...
    @property
    def clippingRange(*args, **kwargs):
        ...
    @clippingRange.setter
    def clippingRange(*args, **kwargs):
        ...
    @property
    def fStop(*args, **kwargs):
        ...
    @fStop.setter
    def fStop(*args, **kwargs):
        ...
    @property
    def focalLength(*args, **kwargs):
        ...
    @focalLength.setter
    def focalLength(*args, **kwargs):
        ...
    @property
    def focusDistance(*args, **kwargs):
        ...
    @focusDistance.setter
    def focusDistance(*args, **kwargs):
        ...
    @property
    def frustum(*args, **kwargs):
        ...
    @property
    def horizontalAperture(*args, **kwargs):
        ...
    @horizontalAperture.setter
    def horizontalAperture(*args, **kwargs):
        ...
    @property
    def horizontalApertureOffset(*args, **kwargs):
        ...
    @horizontalApertureOffset.setter
    def horizontalApertureOffset(*args, **kwargs):
        ...
    @property
    def horizontalFieldOfView(*args, **kwargs):
        ...
    @property
    def projection(*args, **kwargs):
        ...
    @projection.setter
    def projection(*args, **kwargs):
        ...
    @property
    def transform(*args, **kwargs):
        ...
    @transform.setter
    def transform(*args, **kwargs):
        ...
    @property
    def verticalAperture(*args, **kwargs):
        ...
    @verticalAperture.setter
    def verticalAperture(*args, **kwargs):
        ...
    @property
    def verticalApertureOffset(*args, **kwargs):
        ...
    @verticalApertureOffset.setter
    def verticalApertureOffset(*args, **kwargs):
        ...
    @property
    def verticalFieldOfView(*args, **kwargs):
        ...
class DualQuatd(Boost.Python.instance):
    @staticmethod
    def GetConjugate(*args, **kwargs):
        ...
    @staticmethod
    def GetDual(*args, **kwargs):
        ...
    @staticmethod
    def GetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetReal(*args, **kwargs):
        ...
    @staticmethod
    def GetTranslation(*args, **kwargs):
        ...
    @staticmethod
    def GetZero(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def SetDual(*args, **kwargs):
        ...
    @staticmethod
    def SetReal(*args, **kwargs):
        ...
    @staticmethod
    def SetTranslation(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def dual(*args, **kwargs):
        ...
    @dual.setter
    def dual(*args, **kwargs):
        ...
    @property
    def real(*args, **kwargs):
        ...
    @real.setter
    def real(*args, **kwargs):
        ...
class DualQuatf(Boost.Python.instance):
    @staticmethod
    def GetConjugate(*args, **kwargs):
        ...
    @staticmethod
    def GetDual(*args, **kwargs):
        ...
    @staticmethod
    def GetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetReal(*args, **kwargs):
        ...
    @staticmethod
    def GetTranslation(*args, **kwargs):
        ...
    @staticmethod
    def GetZero(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def SetDual(*args, **kwargs):
        ...
    @staticmethod
    def SetReal(*args, **kwargs):
        ...
    @staticmethod
    def SetTranslation(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def dual(*args, **kwargs):
        ...
    @dual.setter
    def dual(*args, **kwargs):
        ...
    @property
    def real(*args, **kwargs):
        ...
    @real.setter
    def real(*args, **kwargs):
        ...
class DualQuath(Boost.Python.instance):
    @staticmethod
    def GetConjugate(*args, **kwargs):
        ...
    @staticmethod
    def GetDual(*args, **kwargs):
        ...
    @staticmethod
    def GetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetReal(*args, **kwargs):
        ...
    @staticmethod
    def GetTranslation(*args, **kwargs):
        ...
    @staticmethod
    def GetZero(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def SetDual(*args, **kwargs):
        ...
    @staticmethod
    def SetReal(*args, **kwargs):
        ...
    @staticmethod
    def SetTranslation(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def dual(*args, **kwargs):
        ...
    @dual.setter
    def dual(*args, **kwargs):
        ...
    @property
    def real(*args, **kwargs):
        ...
    @real.setter
    def real(*args, **kwargs):
        ...
class Frustum(Boost.Python.instance):
    """
    Basic view frustum
    """
    class ProjectionType(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'Frustum'
        allValues: typing.ClassVar[tuple]  # value = (Gf.Frustum.Orthographic, Gf.Frustum.Perspective)
        @staticmethod
        def GetValueFromName(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    Orthographic: typing.ClassVar[ProjectionType]  # value = Gf.Frustum.Orthographic
    Perspective: typing.ClassVar[ProjectionType]  # value = Gf.Frustum.Perspective
    __instance_size__: typing.ClassVar[int] = 152
    @staticmethod
    def ComputeAspectRatio(*args, **kwargs):
        ...
    @staticmethod
    def ComputeCorners(*args, **kwargs):
        ...
    @staticmethod
    def ComputeCornersAtDistance(*args, **kwargs):
        ...
    @staticmethod
    def ComputeLookAtPoint(*args, **kwargs):
        ...
    @staticmethod
    def ComputeNarrowedFrustum(*args, **kwargs):
        ...
    @staticmethod
    def ComputePickRay(*args, **kwargs):
        ...
    @staticmethod
    def ComputeProjectionMatrix(*args, **kwargs):
        ...
    @staticmethod
    def ComputeUpVector(*args, **kwargs):
        ...
    @staticmethod
    def ComputeViewDirection(*args, **kwargs):
        ...
    @staticmethod
    def ComputeViewFrame(*args, **kwargs):
        ...
    @staticmethod
    def ComputeViewInverse(*args, **kwargs):
        ...
    @staticmethod
    def ComputeViewMatrix(*args, **kwargs):
        ...
    @staticmethod
    def FitToSphere(*args, **kwargs):
        ...
    @staticmethod
    def GetFOV(*args, **kwargs):
        """
        
        
        Returns the horizontal fov of the frustum. The fov of the
        frustum is not necessarily the same value as displayed in
        the viewer. The displayed fov is a function of the focal
        length or FOV avar. The frustum's fov may be different due
        to things like lens breathing.
        
        If the frustum is not of type GfFrustum::Perspective, the
        returned FOV will be 0.0.
        """
    @staticmethod
    def GetNearFar(*args, **kwargs):
        ...
    @staticmethod
    def GetOrthographic(*args, **kwargs):
        ...
    @staticmethod
    def GetPerspective(*args, **kwargs):
        """
        
        
        Returns the current perspective frustum values suitable
        for use by SetPerspective.  If the current frustum is a
        perspective projection, the return value is a tuple of
        fieldOfView, aspectRatio, nearDistance, farDistance).
        If the current frustum is not perspective, the return
        value is None.
        """
    @staticmethod
    def GetPosition(*args, **kwargs):
        ...
    @staticmethod
    def GetProjectionType(*args, **kwargs):
        ...
    @staticmethod
    def GetReferencePlaneDepth(*args, **kwargs):
        ...
    @staticmethod
    def GetRotation(*args, **kwargs):
        ...
    @staticmethod
    def GetViewDistance(*args, **kwargs):
        ...
    @staticmethod
    def GetWindow(*args, **kwargs):
        ...
    @staticmethod
    def Intersects(*args, **kwargs):
        ...
    @staticmethod
    def IntersectsViewVolume(*args, **kwargs):
        ...
    @staticmethod
    def SetNearFar(*args, **kwargs):
        ...
    @staticmethod
    def SetOrthographic(*args, **kwargs):
        ...
    @staticmethod
    def SetPerspective(*args, **kwargs):
        ...
    @staticmethod
    def SetPosition(*args, **kwargs):
        ...
    @staticmethod
    def SetPositionAndRotationFromMatrix(*args, **kwargs):
        ...
    @staticmethod
    def SetProjectionType(*args, **kwargs):
        ...
    @staticmethod
    def SetRotation(*args, **kwargs):
        ...
    @staticmethod
    def SetViewDistance(*args, **kwargs):
        ...
    @staticmethod
    def SetWindow(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def nearFar(*args, **kwargs):
        ...
    @nearFar.setter
    def nearFar(*args, **kwargs):
        ...
    @property
    def position(*args, **kwargs):
        ...
    @position.setter
    def position(*args, **kwargs):
        ...
    @property
    def projectionType(*args, **kwargs):
        ...
    @projectionType.setter
    def projectionType(*args, **kwargs):
        ...
    @property
    def rotation(*args, **kwargs):
        ...
    @rotation.setter
    def rotation(*args, **kwargs):
        ...
    @property
    def viewDistance(*args, **kwargs):
        ...
    @viewDistance.setter
    def viewDistance(*args, **kwargs):
        ...
    @property
    def window(*args, **kwargs):
        ...
    @window.setter
    def window(*args, **kwargs):
        ...
class Interval(Boost.Python.instance):
    """
    Basic mathematical interval class
    """
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        
        Returns true if x is inside the interval.
        
        Returns true if x is inside the interval.
        """
    @staticmethod
    def GetFullInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetMax(*args, **kwargs):
        """
        
        
        Get the maximum value.
        """
    @staticmethod
    def GetMin(*args, **kwargs):
        """
        
        
        Get the minimum value.
        """
    @staticmethod
    def GetSize(*args, **kwargs):
        """
        
        
        The width of the interval
        """
    @staticmethod
    def In(*args, **kwargs):
        """
        
        
        Returns true if x is inside the interval.
        """
    @staticmethod
    def Intersects(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        
        True if the interval is empty.
        """
    @staticmethod
    def IsFinite(*args, **kwargs):
        ...
    @staticmethod
    def IsMaxClosed(*args, **kwargs):
        ...
    @staticmethod
    def IsMaxFinite(*args, **kwargs):
        ...
    @staticmethod
    def IsMaxOpen(*args, **kwargs):
        ...
    @staticmethod
    def IsMinClosed(*args, **kwargs):
        ...
    @staticmethod
    def IsMinFinite(*args, **kwargs):
        ...
    @staticmethod
    def IsMinOpen(*args, **kwargs):
        ...
    @staticmethod
    def SetMax(*args, **kwargs):
        """
        
        
        Set the maximum value.
        
        Set the maximum value and boundary condition.
        """
    @staticmethod
    def SetMin(*args, **kwargs):
        """
        
        
        Set the minimum value.
        
        Set the minimum value and boundary condition.
        """
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __and__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __iand__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        
        Create a closed interval representing the single point [val,val].
        
        Create a closed interval representing the range [v1,v2].
        
        Create the interval.
        
        Create the interval.
        """
    @staticmethod
    def __ior__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __or__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @property
    def finite(*args, **kwargs):
        ...
    @property
    def isEmpty(*args, **kwargs):
        """
        True if the interval is empty.
        """
    @property
    def max(*args, **kwargs):
        """
        The maximum value.
        """
    @property
    def maxClosed(*args, **kwargs):
        ...
    @property
    def maxFinite(*args, **kwargs):
        ...
    @property
    def maxOpen(*args, **kwargs):
        ...
    @property
    def min(*args, **kwargs):
        """
        The minimum value.
        """
    @property
    def minClosed(*args, **kwargs):
        ...
    @property
    def minFinite(*args, **kwargs):
        ...
    @property
    def minOpen(*args, **kwargs):
        ...
    @property
    def size(*args, **kwargs):
        """
        The width of the interval.
        """
class Line(Boost.Python.instance):
    """
    Line class
    """
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def FindClosestPoint(*args, **kwargs):
        ...
    @staticmethod
    def GetDirection(*args, **kwargs):
        ...
    @staticmethod
    def GetPoint(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def direction(*args, **kwargs):
        ...
    @direction.setter
    def direction(*args, **kwargs):
        ...
class LineSeg(Boost.Python.instance):
    """
    Line segment class
    """
    __instance_size__: typing.ClassVar[int] = 80
    @staticmethod
    def FindClosestPoint(*args, **kwargs):
        ...
    @staticmethod
    def GetDirection(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetPoint(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def direction(*args, **kwargs):
        ...
    @property
    def length(*args, **kwargs):
        ...
class Matrix2d(Boost.Python.instance):
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (2, 2)
    @staticmethod
    def GetColumn(*args, **kwargs):
        ...
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetRow(*args, **kwargs):
        ...
    @staticmethod
    def GetTranspose(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def SetColumn(*args, **kwargs):
        ...
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        ...
    @staticmethod
    def SetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def SetRow(*args, **kwargs):
        ...
    @staticmethod
    def SetZero(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        """
        
        
        Check rows against GfVec
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        """
        
        
        Return number of rows
        """
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Matrix2f(Boost.Python.instance):
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (2, 2)
    @staticmethod
    def GetColumn(*args, **kwargs):
        ...
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetRow(*args, **kwargs):
        ...
    @staticmethod
    def GetTranspose(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def SetColumn(*args, **kwargs):
        ...
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        ...
    @staticmethod
    def SetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def SetRow(*args, **kwargs):
        ...
    @staticmethod
    def SetZero(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        """
        
        
        Check rows against GfVec
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        """
        
        
        Return number of rows
        """
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Matrix3d(Boost.Python.instance):
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (3, 3)
    @staticmethod
    def ExtractRotation(*args, **kwargs):
        ...
    @staticmethod
    def GetColumn(*args, **kwargs):
        ...
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        ...
    @staticmethod
    def GetHandedness(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetOrthonormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetRow(*args, **kwargs):
        ...
    @staticmethod
    def GetTranspose(*args, **kwargs):
        ...
    @staticmethod
    def IsLeftHanded(*args, **kwargs):
        ...
    @staticmethod
    def IsRightHanded(*args, **kwargs):
        ...
    @staticmethod
    def Orthonormalize(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def SetColumn(*args, **kwargs):
        ...
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        ...
    @staticmethod
    def SetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def SetRotate(*args, **kwargs):
        ...
    @staticmethod
    def SetRow(*args, **kwargs):
        ...
    @staticmethod
    def SetScale(*args, **kwargs):
        ...
    @staticmethod
    def SetZero(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        """
        
        
        Check rows against GfVec
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        """
        
        
        Return number of rows
        """
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Matrix3f(Boost.Python.instance):
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (3, 3)
    @staticmethod
    def ExtractRotation(*args, **kwargs):
        ...
    @staticmethod
    def GetColumn(*args, **kwargs):
        ...
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        ...
    @staticmethod
    def GetHandedness(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetOrthonormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetRow(*args, **kwargs):
        ...
    @staticmethod
    def GetTranspose(*args, **kwargs):
        ...
    @staticmethod
    def IsLeftHanded(*args, **kwargs):
        ...
    @staticmethod
    def IsRightHanded(*args, **kwargs):
        ...
    @staticmethod
    def Orthonormalize(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def SetColumn(*args, **kwargs):
        ...
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        ...
    @staticmethod
    def SetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def SetRotate(*args, **kwargs):
        ...
    @staticmethod
    def SetRow(*args, **kwargs):
        ...
    @staticmethod
    def SetScale(*args, **kwargs):
        ...
    @staticmethod
    def SetZero(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        """
        
        
        Check rows against GfVec
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        """
        
        
        Return number of rows
        """
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Matrix4d(Boost.Python.instance):
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (4, 4)
    @staticmethod
    def ExtractRotation(*args, **kwargs):
        ...
    @staticmethod
    def ExtractRotationMatrix(*args, **kwargs):
        ...
    @staticmethod
    def ExtractRotationQuat(*args, **kwargs):
        ...
    @staticmethod
    def ExtractTranslation(*args, **kwargs):
        ...
    @staticmethod
    def Factor(*args, **kwargs):
        ...
    @staticmethod
    def GetColumn(*args, **kwargs):
        ...
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        ...
    @staticmethod
    def GetDeterminant3(*args, **kwargs):
        ...
    @staticmethod
    def GetHandedness(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetOrthonormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetRow(*args, **kwargs):
        ...
    @staticmethod
    def GetRow3(*args, **kwargs):
        ...
    @staticmethod
    def GetTranspose(*args, **kwargs):
        ...
    @staticmethod
    def HasOrthogonalRows3(*args, **kwargs):
        ...
    @staticmethod
    def IsLeftHanded(*args, **kwargs):
        ...
    @staticmethod
    def IsRightHanded(*args, **kwargs):
        ...
    @staticmethod
    def Orthonormalize(*args, **kwargs):
        ...
    @staticmethod
    def RemoveScaleShear(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def SetColumn(*args, **kwargs):
        ...
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        ...
    @staticmethod
    def SetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def SetLookAt(*args, **kwargs):
        ...
    @staticmethod
    def SetRotate(*args, **kwargs):
        ...
    @staticmethod
    def SetRotateOnly(*args, **kwargs):
        ...
    @staticmethod
    def SetRow(*args, **kwargs):
        ...
    @staticmethod
    def SetRow3(*args, **kwargs):
        ...
    @staticmethod
    def SetScale(*args, **kwargs):
        ...
    @staticmethod
    def SetTransform(*args, **kwargs):
        ...
    @staticmethod
    def SetTranslate(*args, **kwargs):
        ...
    @staticmethod
    def SetTranslateOnly(*args, **kwargs):
        ...
    @staticmethod
    def SetZero(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def TransformAffine(*args, **kwargs):
        ...
    @staticmethod
    def TransformDir(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        """
        
        
        Check rows against GfVec
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        """
        
        
        Return number of rows
        """
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Matrix4f(Boost.Python.instance):
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (4, 4)
    @staticmethod
    def ExtractRotation(*args, **kwargs):
        ...
    @staticmethod
    def ExtractRotationMatrix(*args, **kwargs):
        ...
    @staticmethod
    def ExtractRotationQuat(*args, **kwargs):
        ...
    @staticmethod
    def ExtractTranslation(*args, **kwargs):
        ...
    @staticmethod
    def Factor(*args, **kwargs):
        ...
    @staticmethod
    def GetColumn(*args, **kwargs):
        ...
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        ...
    @staticmethod
    def GetDeterminant3(*args, **kwargs):
        ...
    @staticmethod
    def GetHandedness(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetOrthonormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetRow(*args, **kwargs):
        ...
    @staticmethod
    def GetRow3(*args, **kwargs):
        ...
    @staticmethod
    def GetTranspose(*args, **kwargs):
        ...
    @staticmethod
    def HasOrthogonalRows3(*args, **kwargs):
        ...
    @staticmethod
    def IsLeftHanded(*args, **kwargs):
        ...
    @staticmethod
    def IsRightHanded(*args, **kwargs):
        ...
    @staticmethod
    def Orthonormalize(*args, **kwargs):
        ...
    @staticmethod
    def RemoveScaleShear(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def SetColumn(*args, **kwargs):
        ...
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        ...
    @staticmethod
    def SetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def SetLookAt(*args, **kwargs):
        ...
    @staticmethod
    def SetRotate(*args, **kwargs):
        ...
    @staticmethod
    def SetRotateOnly(*args, **kwargs):
        ...
    @staticmethod
    def SetRow(*args, **kwargs):
        ...
    @staticmethod
    def SetRow3(*args, **kwargs):
        ...
    @staticmethod
    def SetScale(*args, **kwargs):
        ...
    @staticmethod
    def SetTransform(*args, **kwargs):
        ...
    @staticmethod
    def SetTranslate(*args, **kwargs):
        ...
    @staticmethod
    def SetTranslateOnly(*args, **kwargs):
        ...
    @staticmethod
    def SetZero(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def TransformAffine(*args, **kwargs):
        ...
    @staticmethod
    def TransformDir(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        """
        
        
        Check rows against GfVec
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        """
        
        
        Return number of rows
        """
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class MultiInterval(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def Add(*args, **kwargs):
        ...
    @staticmethod
    def ArithmeticAdd(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        
        Returns true if x is inside the multi-interval.
        
        Returns true if x is inside the multi-interval.
        
        Returns true if x is inside the multi-interval.
        """
    @staticmethod
    def GetBounds(*args, **kwargs):
        ...
    @staticmethod
    def GetComplement(*args, **kwargs):
        ...
    @staticmethod
    def GetContainingInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetFullInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetNextNonContainingInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetPriorNonContainingInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetSize(*args, **kwargs):
        ...
    @staticmethod
    def Intersect(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def Remove(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def bounds(*args, **kwargs):
        ...
    @property
    def isEmpty(*args, **kwargs):
        ...
    @property
    def size(*args, **kwargs):
        ...
class Plane(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def GetDistance(*args, **kwargs):
        ...
    @staticmethod
    def GetDistanceFromOrigin(*args, **kwargs):
        ...
    @staticmethod
    def GetEquation(*args, **kwargs):
        ...
    @staticmethod
    def GetNormal(*args, **kwargs):
        ...
    @staticmethod
    def IntersectsPositiveHalfSpace(*args, **kwargs):
        ...
    @staticmethod
    def Project(*args, **kwargs):
        ...
    @staticmethod
    def Reorient(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def distanceFromOrigin(*args, **kwargs):
        ...
    @property
    def normal(*args, **kwargs):
        ...
class Quatd(Boost.Python.instance):
    @staticmethod
    def GetConjugate(*args, **kwargs):
        ...
    @staticmethod
    def GetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def GetImaginary(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetReal(*args, **kwargs):
        ...
    @staticmethod
    def GetZero(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def SetImaginary(*args, **kwargs):
        ...
    @staticmethod
    def SetReal(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def imaginary(*args, **kwargs):
        ...
    @imaginary.setter
    def imaginary(*args, **kwargs):
        ...
    @property
    def real(*args, **kwargs):
        ...
    @real.setter
    def real(*args, **kwargs):
        ...
class Quaternion(Boost.Python.instance):
    """
    Quaternion class
    """
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def GetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def GetImaginary(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetReal(*args, **kwargs):
        ...
    @staticmethod
    def GetZero(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def imaginary(*args, **kwargs):
        ...
    @imaginary.setter
    def imaginary(*args, **kwargs):
        ...
    @property
    def real(*args, **kwargs):
        ...
    @real.setter
    def real(*args, **kwargs):
        ...
class Quatf(Boost.Python.instance):
    @staticmethod
    def GetConjugate(*args, **kwargs):
        ...
    @staticmethod
    def GetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def GetImaginary(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetReal(*args, **kwargs):
        ...
    @staticmethod
    def GetZero(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def SetImaginary(*args, **kwargs):
        ...
    @staticmethod
    def SetReal(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def imaginary(*args, **kwargs):
        ...
    @imaginary.setter
    def imaginary(*args, **kwargs):
        ...
    @property
    def real(*args, **kwargs):
        ...
    @real.setter
    def real(*args, **kwargs):
        ...
class Quath(Boost.Python.instance):
    @staticmethod
    def GetConjugate(*args, **kwargs):
        ...
    @staticmethod
    def GetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def GetImaginary(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetReal(*args, **kwargs):
        ...
    @staticmethod
    def GetZero(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def SetImaginary(*args, **kwargs):
        ...
    @staticmethod
    def SetReal(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def imaginary(*args, **kwargs):
        ...
    @imaginary.setter
    def imaginary(*args, **kwargs):
        ...
    @property
    def real(*args, **kwargs):
        ...
    @real.setter
    def real(*args, **kwargs):
        ...
class Range1d(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 40
    dimension: typing.ClassVar[int] = 1
    @staticmethod
    def Contains(*args, **kwargs):
        ...
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        ...
    @staticmethod
    def GetIntersection(*args, **kwargs):
        ...
    @staticmethod
    def GetMax(*args, **kwargs):
        ...
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        ...
    @staticmethod
    def GetMin(*args, **kwargs):
        ...
    @staticmethod
    def GetSize(*args, **kwargs):
        ...
    @staticmethod
    def GetUnion(*args, **kwargs):
        ...
    @staticmethod
    def IntersectWith(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetMax(*args, **kwargs):
        ...
    @staticmethod
    def SetMin(*args, **kwargs):
        ...
    @staticmethod
    def UnionWith(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def max(*args, **kwargs):
        ...
    @max.setter
    def max(*args, **kwargs):
        ...
    @property
    def min(*args, **kwargs):
        ...
    @min.setter
    def min(*args, **kwargs):
        ...
class Range1f(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    dimension: typing.ClassVar[int] = 1
    @staticmethod
    def Contains(*args, **kwargs):
        ...
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        ...
    @staticmethod
    def GetIntersection(*args, **kwargs):
        ...
    @staticmethod
    def GetMax(*args, **kwargs):
        ...
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        ...
    @staticmethod
    def GetMin(*args, **kwargs):
        ...
    @staticmethod
    def GetSize(*args, **kwargs):
        ...
    @staticmethod
    def GetUnion(*args, **kwargs):
        ...
    @staticmethod
    def IntersectWith(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetMax(*args, **kwargs):
        ...
    @staticmethod
    def SetMin(*args, **kwargs):
        ...
    @staticmethod
    def UnionWith(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def max(*args, **kwargs):
        ...
    @max.setter
    def max(*args, **kwargs):
        ...
    @property
    def min(*args, **kwargs):
        ...
    @min.setter
    def min(*args, **kwargs):
        ...
class Range2d(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 56
    dimension: typing.ClassVar[int] = 2
    unitSquare: typing.ClassVar[Range2d]  # value = Gf.Range2d(Gf.Vec2d(0.0, 0.0), Gf.Vec2d(1.0, 1.0))
    @staticmethod
    def Contains(*args, **kwargs):
        ...
    @staticmethod
    def GetCorner(*args, **kwargs):
        ...
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        ...
    @staticmethod
    def GetIntersection(*args, **kwargs):
        ...
    @staticmethod
    def GetMax(*args, **kwargs):
        ...
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        ...
    @staticmethod
    def GetMin(*args, **kwargs):
        ...
    @staticmethod
    def GetQuadrant(*args, **kwargs):
        ...
    @staticmethod
    def GetSize(*args, **kwargs):
        ...
    @staticmethod
    def GetUnion(*args, **kwargs):
        ...
    @staticmethod
    def IntersectWith(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetMax(*args, **kwargs):
        ...
    @staticmethod
    def SetMin(*args, **kwargs):
        ...
    @staticmethod
    def UnionWith(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def max(*args, **kwargs):
        ...
    @max.setter
    def max(*args, **kwargs):
        ...
    @property
    def min(*args, **kwargs):
        ...
    @min.setter
    def min(*args, **kwargs):
        ...
class Range2f(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 40
    dimension: typing.ClassVar[int] = 2
    unitSquare: typing.ClassVar[Range2f]  # value = Gf.Range2f(Gf.Vec2f(0.0, 0.0), Gf.Vec2f(1.0, 1.0))
    @staticmethod
    def Contains(*args, **kwargs):
        ...
    @staticmethod
    def GetCorner(*args, **kwargs):
        ...
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        ...
    @staticmethod
    def GetIntersection(*args, **kwargs):
        ...
    @staticmethod
    def GetMax(*args, **kwargs):
        ...
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        ...
    @staticmethod
    def GetMin(*args, **kwargs):
        ...
    @staticmethod
    def GetQuadrant(*args, **kwargs):
        ...
    @staticmethod
    def GetSize(*args, **kwargs):
        ...
    @staticmethod
    def GetUnion(*args, **kwargs):
        ...
    @staticmethod
    def IntersectWith(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetMax(*args, **kwargs):
        ...
    @staticmethod
    def SetMin(*args, **kwargs):
        ...
    @staticmethod
    def UnionWith(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def max(*args, **kwargs):
        ...
    @max.setter
    def max(*args, **kwargs):
        ...
    @property
    def min(*args, **kwargs):
        ...
    @min.setter
    def min(*args, **kwargs):
        ...
class Range3d(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 72
    dimension: typing.ClassVar[int] = 3
    unitCube: typing.ClassVar[Range3d]  # value = Gf.Range3d(Gf.Vec3d(0.0, 0.0, 0.0), Gf.Vec3d(1.0, 1.0, 1.0))
    @staticmethod
    def Contains(*args, **kwargs):
        ...
    @staticmethod
    def GetCorner(*args, **kwargs):
        ...
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        ...
    @staticmethod
    def GetIntersection(*args, **kwargs):
        ...
    @staticmethod
    def GetMax(*args, **kwargs):
        ...
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        ...
    @staticmethod
    def GetMin(*args, **kwargs):
        ...
    @staticmethod
    def GetOctant(*args, **kwargs):
        ...
    @staticmethod
    def GetSize(*args, **kwargs):
        ...
    @staticmethod
    def GetUnion(*args, **kwargs):
        ...
    @staticmethod
    def IntersectWith(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetMax(*args, **kwargs):
        ...
    @staticmethod
    def SetMin(*args, **kwargs):
        ...
    @staticmethod
    def UnionWith(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def max(*args, **kwargs):
        ...
    @max.setter
    def max(*args, **kwargs):
        ...
    @property
    def min(*args, **kwargs):
        ...
    @min.setter
    def min(*args, **kwargs):
        ...
class Range3f(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    dimension: typing.ClassVar[int] = 3
    unitCube: typing.ClassVar[Range3f]  # value = Gf.Range3f(Gf.Vec3f(0.0, 0.0, 0.0), Gf.Vec3f(1.0, 1.0, 1.0))
    @staticmethod
    def Contains(*args, **kwargs):
        ...
    @staticmethod
    def GetCorner(*args, **kwargs):
        ...
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        ...
    @staticmethod
    def GetIntersection(*args, **kwargs):
        ...
    @staticmethod
    def GetMax(*args, **kwargs):
        ...
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        ...
    @staticmethod
    def GetMin(*args, **kwargs):
        ...
    @staticmethod
    def GetOctant(*args, **kwargs):
        ...
    @staticmethod
    def GetSize(*args, **kwargs):
        ...
    @staticmethod
    def GetUnion(*args, **kwargs):
        ...
    @staticmethod
    def IntersectWith(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetMax(*args, **kwargs):
        ...
    @staticmethod
    def SetMin(*args, **kwargs):
        ...
    @staticmethod
    def UnionWith(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def max(*args, **kwargs):
        ...
    @max.setter
    def max(*args, **kwargs):
        ...
    @property
    def min(*args, **kwargs):
        ...
    @min.setter
    def min(*args, **kwargs):
        ...
class Ray(Boost.Python.instance):
    """
    """
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def FindClosestPoint(*args, **kwargs):
        ...
    @staticmethod
    def GetPoint(*args, **kwargs):
        ...
    @staticmethod
    def Intersect(*args, **kwargs):
        """
        
        
        Intersect( p0, p1, p2 ) -> tuple<intersects = bool, dist =
        float, barycentric = GfVec3d, frontFacing = bool>
        
        Intersects the ray with the triangle formed by points p0,
        p1, and p2.  The first item in the tuple is true if the ray
        intersects the triangle. dist is the the parametric
        distance to the intersection point, the barycentric
        coordinates of the intersection point, and the front-facing
        flag. The barycentric coordinates are defined with respect
        to the three vertices taken in order.  The front-facing
        flag is True if the intersection hit the side of the
        triangle that is formed when the vertices are ordered
        counter-clockwise (right-hand rule).
        
        Barycentric coordinates are defined to sum to 1 and satisfy
        this relationsip:
        
            intersectionPoint = (barycentricCoords[0] * p0 +
                                 barycentricCoords[1] * p1 +
                                 barycentricCoords[2] * p2);
        ----------------------------------------------------------------------
        
        Intersect( plane ) -> tuple<intersects = bool, dist = float,
        frontFacing = bool>
        
        Intersects the ray with the Gf.Plane.  The first item in
        the returned tuple is true if the ray intersects the plane.
        dist is the parametric distance to the intersection point
        and frontfacing is true if the intersection is on the side
        of the plane toward which the plane's normal points.
        ----------------------------------------------------------------------
        
        Intersect( range3d ) -> tuple<intersects = bool, enterDist
        = float, exitDist = float>
        Intersects the plane with an axis-aligned box in a
        Gf.Range3d.  intersects is true if the ray intersects it at
        all within bounds. If there is an intersection then enterDist
        and exitDist will be the parametric distances to the two
        intersection points.
        ----------------------------------------------------------------------
        
        Intersect( bbox3d ) -> tuple<intersects = bool, enterDist
        = float, exitDist = float>
        Intersects the plane with an oriented box in a Gf.BBox3d.
        intersects is true if the ray intersects it at all within
        bounds. If there is an intersection then enterDist and
        exitDist will be the parametric distances to the two
        intersection points.
        ----------------------------------------------------------------------
        
        Intersect( center, radius ) -> tuple<intersects = bool,
        enterDist = float, exitDist = float>
        
        Intersects the plane with an sphere. intersects is true if
        the ray intersects it at all within the sphere. If there is
        an intersection then enterDist and exitDist will be the
        parametric distances to the two intersection points.
        ----------------------------------------------------------------------
        
        Intersect( origin, axis, radius ) -> tuple<intersects = bool,
        enterDist = float, exitDist = float>
        
        Intersects the plane with an infinite cylinder. intersects
        is true if the ray intersects it at all within the
        sphere. If there is an intersection then enterDist and
        exitDist will be the parametric distances to the two
        intersection points.
        ----------------------------------------------------------------------
        
        Intersect( origin, axis, radius, height ) -> 
        tuple<intersects = bool, enterDist = float, exitDist = float>
        
        Intersects the plane with an cylinder. intersects
        is true if the ray intersects it at all within the
        sphere. If there is an intersection then enterDist and
        exitDist will be the parametric distances to the two
        intersection points.
        ----------------------------------------------------------------------
        """
    @staticmethod
    def SetEnds(*args, **kwargs):
        ...
    @staticmethod
    def SetPointAndDirection(*args, **kwargs):
        ...
    @staticmethod
    def Transform(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def direction(*args, **kwargs):
        ...
    @direction.setter
    def direction(*args, **kwargs):
        ...
    @property
    def startPoint(*args, **kwargs):
        ...
    @startPoint.setter
    def startPoint(*args, **kwargs):
        ...
class Rect2i(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Contains(*args, **kwargs):
        ...
    @staticmethod
    def GetArea(*args, **kwargs):
        ...
    @staticmethod
    def GetCenter(*args, **kwargs):
        ...
    @staticmethod
    def GetHeight(*args, **kwargs):
        ...
    @staticmethod
    def GetIntersection(*args, **kwargs):
        ...
    @staticmethod
    def GetMax(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxX(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxY(*args, **kwargs):
        ...
    @staticmethod
    def GetMin(*args, **kwargs):
        ...
    @staticmethod
    def GetMinX(*args, **kwargs):
        ...
    @staticmethod
    def GetMinY(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetSize(*args, **kwargs):
        ...
    @staticmethod
    def GetUnion(*args, **kwargs):
        ...
    @staticmethod
    def GetWidth(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def IsNull(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        ...
    @staticmethod
    def SetMax(*args, **kwargs):
        ...
    @staticmethod
    def SetMaxX(*args, **kwargs):
        ...
    @staticmethod
    def SetMaxY(*args, **kwargs):
        ...
    @staticmethod
    def SetMin(*args, **kwargs):
        ...
    @staticmethod
    def SetMinX(*args, **kwargs):
        ...
    @staticmethod
    def SetMinY(*args, **kwargs):
        ...
    @staticmethod
    def Translate(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def max(*args, **kwargs):
        ...
    @max.setter
    def max(*args, **kwargs):
        ...
    @property
    def maxX(*args, **kwargs):
        ...
    @maxX.setter
    def maxX(*args, **kwargs):
        ...
    @property
    def maxY(*args, **kwargs):
        ...
    @maxY.setter
    def maxY(*args, **kwargs):
        ...
    @property
    def min(*args, **kwargs):
        ...
    @min.setter
    def min(*args, **kwargs):
        ...
    @property
    def minX(*args, **kwargs):
        ...
    @minX.setter
    def minX(*args, **kwargs):
        ...
    @property
    def minY(*args, **kwargs):
        ...
    @minY.setter
    def minY(*args, **kwargs):
        ...
class Rotation(Boost.Python.instance):
    """
    3-space rotation
    """
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Decompose(*args, **kwargs):
        ...
    @staticmethod
    def DecomposeRotation(*args, **kwargs):
        ...
    @staticmethod
    def DecomposeRotation3(*args, **kwargs):
        ...
    @staticmethod
    def GetAngle(*args, **kwargs):
        ...
    @staticmethod
    def GetAxis(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def GetQuat(*args, **kwargs):
        ...
    @staticmethod
    def GetQuaternion(*args, **kwargs):
        ...
    @staticmethod
    def MatchClosestEulerRotation(*args, **kwargs):
        ...
    @staticmethod
    def RotateOntoProjected(*args, **kwargs):
        ...
    @staticmethod
    def SetAxisAngle(*args, **kwargs):
        ...
    @staticmethod
    def SetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def SetQuat(*args, **kwargs):
        ...
    @staticmethod
    def SetQuaternion(*args, **kwargs):
        ...
    @staticmethod
    def SetRotateInto(*args, **kwargs):
        ...
    @staticmethod
    def TransformDir(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @property
    def angle(*args, **kwargs):
        ...
    @angle.setter
    def angle(*args, **kwargs):
        ...
    @property
    def axis(*args, **kwargs):
        ...
    @axis.setter
    def axis(*args, **kwargs):
        ...
class Size2(Boost.Python.instance):
    """
    A 2D size class
    """
    __instance_size__: typing.ClassVar[int] = 40
    dimension: typing.ClassVar[int] = 2
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Size3(Boost.Python.instance):
    """
    A 3D size class
    """
    __instance_size__: typing.ClassVar[int] = 48
    dimension: typing.ClassVar[int] = 3
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Transform(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 160
    @staticmethod
    def GetMatrix(*args, **kwargs):
        ...
    @staticmethod
    def GetPivotOrientation(*args, **kwargs):
        ...
    @staticmethod
    def GetPivotPosition(*args, **kwargs):
        ...
    @staticmethod
    def GetRotation(*args, **kwargs):
        ...
    @staticmethod
    def GetScale(*args, **kwargs):
        ...
    @staticmethod
    def GetTranslation(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        
        Set method used by old 2x code. (Deprecated)
        """
    @staticmethod
    def SetIdentity(*args, **kwargs):
        ...
    @staticmethod
    def SetMatrix(*args, **kwargs):
        ...
    @staticmethod
    def SetPivotOrientation(*args, **kwargs):
        ...
    @staticmethod
    def SetPivotPosition(*args, **kwargs):
        ...
    @staticmethod
    def SetRotation(*args, **kwargs):
        ...
    @staticmethod
    def SetScale(*args, **kwargs):
        ...
    @staticmethod
    def SetTranslation(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        
        Initializer used by 3x code.
        
        Initializer used by old 2x code. (Deprecated)
        
        Initializer used by old 2x code. (Deprecated)
        """
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def pivotOrientation(*args, **kwargs):
        ...
    @pivotOrientation.setter
    def pivotOrientation(*args, **kwargs):
        ...
    @property
    def pivotPosition(*args, **kwargs):
        ...
    @pivotPosition.setter
    def pivotPosition(*args, **kwargs):
        ...
    @property
    def rotation(*args, **kwargs):
        ...
    @rotation.setter
    def rotation(*args, **kwargs):
        ...
    @property
    def scale(*args, **kwargs):
        ...
    @scale.setter
    def scale(*args, **kwargs):
        ...
    @property
    def translation(*args, **kwargs):
        ...
    @translation.setter
    def translation(*args, **kwargs):
        ...
class Vec2d(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 2
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def GetComplement(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetProjection(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Vec2f(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 2
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def GetComplement(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetProjection(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Vec2h(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 2
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def GetComplement(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetProjection(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Vec2i(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 2
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Vec3d(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 3
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def BuildOrthonormalFrame(*args, **kwargs):
        ...
    @staticmethod
    def GetComplement(*args, **kwargs):
        ...
    @staticmethod
    def GetCross(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetProjection(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def OrthogonalizeBasis(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def ZAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @staticmethod
    def __xor__(*args, **kwargs):
        ...
class Vec3f(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 3
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def BuildOrthonormalFrame(*args, **kwargs):
        ...
    @staticmethod
    def GetComplement(*args, **kwargs):
        ...
    @staticmethod
    def GetCross(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetProjection(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def OrthogonalizeBasis(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def ZAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @staticmethod
    def __xor__(*args, **kwargs):
        ...
class Vec3h(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 3
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def BuildOrthonormalFrame(*args, **kwargs):
        ...
    @staticmethod
    def GetComplement(*args, **kwargs):
        ...
    @staticmethod
    def GetCross(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetProjection(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def OrthogonalizeBasis(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def ZAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
    @staticmethod
    def __xor__(*args, **kwargs):
        ...
class Vec3i(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 3
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def ZAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Vec4d(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 4
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def GetComplement(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetProjection(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def WAxis(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def ZAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Vec4f(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 4
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def GetComplement(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetProjection(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def WAxis(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def ZAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Vec4h(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 4
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def GetComplement(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalized(*args, **kwargs):
        ...
    @staticmethod
    def GetProjection(*args, **kwargs):
        ...
    @staticmethod
    def Normalize(*args, **kwargs):
        ...
    @staticmethod
    def WAxis(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def ZAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class Vec4i(Boost.Python.instance):
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 4
    @staticmethod
    def Axis(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def WAxis(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        ...
    @staticmethod
    def YAxis(*args, **kwargs):
        ...
    @staticmethod
    def ZAxis(*args, **kwargs):
        ...
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getinitargs__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __isub__(*args, **kwargs):
        ...
    @staticmethod
    def __itruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __neg__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
MIN_ORTHO_TOLERANCE: float = 1e-06
MIN_VECTOR_LENGTH: float = 1e-10
__MFB_FULL_PACKAGE_NAME: str = 'gf'
