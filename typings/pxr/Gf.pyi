"""

Graphics Foundation
This package defines classes for fundamental graphics types and operations.
"""
from __future__ import annotations
import pxr.Tf
import typing
__all__ = ['BBox3d', 'Camera', 'DualQuatd', 'DualQuatf', 'DualQuath', 'Frustum', 'Interval', 'Line', 'LineSeg', 'MIN_ORTHO_TOLERANCE', 'MIN_VECTOR_LENGTH', 'Matrix2d', 'Matrix2f', 'Matrix3d', 'Matrix3f', 'Matrix4d', 'Matrix4f', 'MultiInterval', 'Plane', 'Quatd', 'Quaternion', 'Quatf', 'Quath', 'Range1d', 'Range1f', 'Range2d', 'Range2f', 'Range3d', 'Range3f', 'Ray', 'Rect2i', 'Rotation', 'Size2', 'Size3', 'Transform', 'Vec2d', 'Vec2f', 'Vec2h', 'Vec2i', 'Vec3d', 'Vec3f', 'Vec3h', 'Vec3i', 'Vec4d', 'Vec4f', 'Vec4h', 'Vec4i']
class BBox3d(Boost.Python.instance):
    """
    Arbitrarily oriented 3D bounding box
    """
    __instance_size__: typing.ClassVar[int] = 328
    @staticmethod
    def Combine(*args, **kwargs):
        """
        
        **classmethod** Combine(b1, b2) -> BBox3d
        
        
        Combines two bboxes, returning a new bbox that contains both.
        
        
        This uses the coordinate space of one of the two original boxes as the
        space of the result; it uses the one that produces whe smaller of the
        two resulting boxes.
        
        
        Parameters
        ----------
        b1 : BBox3d
        
        b2 : BBox3d
        
        
        """
    @staticmethod
    def ComputeAlignedBox(*args, **kwargs):
        """
        
        ComputeAlignedBox() -> Range3d
        
        
        Returns the axis-aligned range (as a ``GfRange3d`` ) that results from
        applying the transformation matrix to the axis-aligned box and
        aligning the result.
        
        
        This synonym for ``ComputeAlignedRange`` exists for compatibility
        purposes.
        
        
        
        """
    @staticmethod
    def ComputeAlignedRange(*args, **kwargs):
        """
        
        ComputeAlignedRange() -> Range3d
        
        
        Returns the axis-aligned range (as a ``GfRange3d`` ) that results from
        applying the transformation matrix to the wxis-aligned box and
        aligning the result.
        
        
        
        """
    @staticmethod
    def ComputeCentroid(*args, **kwargs):
        """
        
        ComputeCentroid() -> Vec3d
        
        
        Returns the centroid of the bounding box.
        
        
        The centroid is computed as the transformed centroid of the range.
        
        
        
        """
    @staticmethod
    def GetBox(*args, **kwargs):
        """
        
        GetBox() -> Range3d
        
        
        Returns the range of the axis-aligned untransformed box.
        
        
        This synonym of ``GetRange`` exists for compatibility purposes.
        
        
        
        """
    @staticmethod
    def GetInverseMatrix(*args, **kwargs):
        """
        
        GetInverseMatrix() -> Matrix4d
        
        
        Returns the inverse of the transformation matrix.
        
        
        This will be the identity matrix if the transformation matrix is not
        invertible.
        
        
        
        """
    @staticmethod
    def GetMatrix(*args, **kwargs):
        """
        
        GetMatrix() -> Matrix4d
        
        
        Returns the transformation matrix.
        
        
        
        """
    @staticmethod
    def GetRange(*args, **kwargs):
        """
        
        GetRange() -> Range3d
        
        
        Returns the range of the axis-aligned untransformed box.
        
        
        
        """
    @staticmethod
    def GetVolume(*args, **kwargs):
        """
        
        GetVolume() -> float
        
        
        Returns the volume of the box (0 for an empty box).
        
        
        
        """
    @staticmethod
    def HasZeroAreaPrimitives(*args, **kwargs):
        """
        
        HasZeroAreaPrimitives() -> bool
        
        
        Returns the current state of the zero-area primitives flag".
        
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(box, matrix) -> None
        
        
        Sets the axis-aligned box and transformation matrix.
        
        
        Parameters
        ----------
        box : Range3d
        
        matrix : Matrix4d
        
        
        """
    @staticmethod
    def SetHasZeroAreaPrimitives(*args, **kwargs):
        """
        
        SetHasZeroAreaPrimitives(hasThem) -> None
        
        
        Sets the zero-area primitives flag to the given value.
        
        
        Parameters
        ----------
        hasThem : bool
        
        
        """
    @staticmethod
    def SetMatrix(*args, **kwargs):
        """
        
        SetMatrix(matrix) -> None
        
        
        Sets the transformation matrix only.
        
        
        The axis-aligned box is not modified.
        
        
        Parameters
        ----------
        matrix : Matrix4d
        
        
        """
    @staticmethod
    def SetRange(*args, **kwargs):
        """
        
        SetRange(box) -> None
        
        
        Sets the range of the axis-aligned box only.
        
        
        The transformation matrix is not modified.
        
        
        Parameters
        ----------
        box : Range3d
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(matrix) -> None
        
        
        Transforms the bounding box by the given matrix, which is assumed to
        be a global transformation to apply to the box.
        
        
        Therefore, this just post-multiplies the box's matrix by ``matrix`` .
        
        
        Parameters
        ----------
        matrix : Matrix4d
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        The default constructor leaves the box empty, the transformation
        matrix identity, and the zero-area primitives flag" ``false`` .
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rhs)
        
        
        Copy constructor.
        
        
        Parameters
        ----------
        rhs : BBox3d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(box)
        
        
        This constructor takes a box and sets the matrix to identity.
        
        
        Parameters
        ----------
        box : Range3d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(box, matrix)
        
        
        This constructor takes a box and a transformation matrix.
        
        
        Parameters
        ----------
        box : Range3d
        
        matrix : Matrix4d
        
        
        """
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
    """
    """
    class FOVDirection(pxr.Tf.Tf_PyEnumWrapper):
        """
        
        Direction used for Field of View or orthographic size.
        
        """
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
        """
        
        Projection type.
        
        """
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
    __instance_size__: typing.ClassVar[int] = 208
    @staticmethod
    def GetFieldOfView(*args, **kwargs):
        """
        
        GetFieldOfView(direction) -> float
        
        
        Returns the horizontal or vertical field of view in degrees.
        
        
        Parameters
        ----------
        direction : FOVDirection
        
        
        """
    @staticmethod
    def SetFromViewAndProjectionMatrix(*args, **kwargs):
        """
        
        SetFromViewAndProjectionMatrix(viewMatrix, projMatix, focalLength) -> None
        
        
        Sets the camera from a view and projection matrix.
        
        
        Note that the projection matrix does only determine the ratio of
        aperture to focal length, so there is a choice which defaults to 50mm
        (or more accurately, 50 tenths of a world unit).
        
        
        Parameters
        ----------
        viewMatrix : Matrix4d
        
        projMatix : Matrix4d
        
        focalLength : float
        
        
        """
    @staticmethod
    def SetOrthographicFromAspectRatioAndSize(*args, **kwargs):
        """
        
        SetOrthographicFromAspectRatioAndSize(aspectRatio, orthographicSize, direction) -> None
        
        
        Sets the frustum to be orthographic such that it has the given
        ``aspectRatio`` and such that the orthographic width, respectively,
        orthographic height (in cm) is equal to ``orthographicSize``
        (depending on direction).
        
        
        Parameters
        ----------
        aspectRatio : float
        
        orthographicSize : float
        
        direction : FOVDirection
        
        
        """
    @staticmethod
    def SetPerspectiveFromAspectRatioAndFieldOfView(*args, **kwargs):
        """
        
        SetPerspectiveFromAspectRatioAndFieldOfView(aspectRatio, fieldOfView, direction, horizontalAperture) -> None
        
        
        Sets the frustum to be projective with the given ``aspectRatio`` and
        horizontal, respectively, vertical field of view ``fieldOfView``
        (similar to gluPerspective when direction = FOVVertical).
        
        
        Do not pass values for ``horionztalAperture`` unless you care about
        DepthOfField.
        
        
        Parameters
        ----------
        aspectRatio : float
        
        fieldOfView : float
        
        direction : FOVDirection
        
        horizontalAperture : float
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(transform, projection, horizontalAperture, verticalAperture, horizontalApertureOffset, verticalApertureOffset, focalLength, clippingRange, clippingPlanes, fStop, focusDistance)
        
        
        Parameters
        ----------
        transform : Matrix4d
        
        projection : Projection
        
        horizontalAperture : float
        
        verticalAperture : float
        
        horizontalApertureOffset : float
        
        verticalApertureOffset : float
        
        focalLength : float
        
        clippingRange : Range1f
        
        clippingPlanes : list[Vec4f]
        
        fStop : float
        
        focusDistance : float
        
        
        """
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
        """
        type : float
        
        
        Returns the projector aperture aspect ratio.
        """
    @property
    def clippingPlanes(*args, **kwargs):
        """
        type : list[Vec4f]
        
        
        Returns additional clipping planes.
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets additional arbitrarily oriented clipping planes.
        
        
        A vector (a,b,c,d) encodes a clipping plane that clips off points
        (x,y,z) with a \\* x + b \\* y + c \\* z + d \\* 1<0
        
        where (x,y,z) are the coordinates in the camera's space.
        """
    @clippingPlanes.setter
    def clippingPlanes(*args, **kwargs):
        ...
    @property
    def clippingRange(*args, **kwargs):
        """
        type : Range1f
        
        
        Returns the clipping range in world units.
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets the clipping range in world units.
        """
    @clippingRange.setter
    def clippingRange(*args, **kwargs):
        ...
    @property
    def fStop(*args, **kwargs):
        """
        type : float
        
        
        Returns the lens aperture.
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets the lens aperture, unitless.
        """
    @fStop.setter
    def fStop(*args, **kwargs):
        ...
    @property
    def focalLength(*args, **kwargs):
        """
        type : float
        
        
        Returns the focal length in tenths of a world unit (e.g., mm if the
        world unit is assumed to be cm).
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        These are the values actually stored in the class and they correspond
        to measurements of an actual physical camera (in mm).
        
        
        Together with the clipping range, they determine the camera frustum.
        Sets the focal length in tenths of a world unit (e.g., mm if the world
        unit is assumed to be cm).
        """
    @focalLength.setter
    def focalLength(*args, **kwargs):
        ...
    @property
    def focusDistance(*args, **kwargs):
        """
        type : float
        
        
        Returns the focus distance in world units.
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets the focus distance in world units.
        """
    @focusDistance.setter
    def focusDistance(*args, **kwargs):
        ...
    @property
    def frustum(*args, **kwargs):
        """
        type : Frustum
        
        
        Returns the computed, world-space camera frustum.
        
        
        The frustum will always be that of a Y-up, -Z-looking camera.
        """
    @property
    def horizontalAperture(*args, **kwargs):
        """
        type : float
        
        
        Returns the width of the projector aperture in tenths of a world unit
        (e.g., mm if the world unit is assumed to be cm).
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets the width of the projector aperture in tenths of a world unit
        (e.g., mm if the world unit is assumed to be cm).
        """
    @horizontalAperture.setter
    def horizontalAperture(*args, **kwargs):
        ...
    @property
    def horizontalApertureOffset(*args, **kwargs):
        """
        type : float
        
        
        Returns the horizontal offset of the projector aperture in tenths of a
        world unit (e.g., mm if the world unit is assumed to be cm).
        
        
        In particular, an offset is necessary when writing out a stereo camera
        with finite convergence distance as two cameras.
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets the horizontal offset of the projector aperture in tenths of a
        world unit (e.g., mm if the world unit is assumed to be cm).
        """
    @horizontalApertureOffset.setter
    def horizontalApertureOffset(*args, **kwargs):
        ...
    @property
    def horizontalFieldOfView(*args, **kwargs):
        ...
    @property
    def projection(*args, **kwargs):
        """
        type : Projection
        
        
        Returns the projection type.
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets the projection type.
        """
    @projection.setter
    def projection(*args, **kwargs):
        ...
    @property
    def transform(*args, **kwargs):
        """
        type : Matrix4d
        
        
        Returns the transform of the filmback in world space.
        
        
        This is exactly the transform specified via SetTransform() .
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets the transform of the filmback in world space to ``val`` .
        """
    @transform.setter
    def transform(*args, **kwargs):
        ...
    @property
    def verticalAperture(*args, **kwargs):
        """
        type : float
        
        
        Returns the height of the projector aperture in tenths of a world unit
        (e.g., mm if the world unit is assumed to be cm).
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets the height of the projector aperture in tenths of a world unit
        (e.g., mm if the world unit is assumed to be cm).
        """
    @verticalAperture.setter
    def verticalAperture(*args, **kwargs):
        ...
    @property
    def verticalApertureOffset(*args, **kwargs):
        """
        type : float
        
        
        Returns the vertical offset of the projector aperture in tenths of a
        world unit (e.g., mm if the world unit is assumed to be cm).
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets the vertical offset of the projector aperture in tenths of a
        world unit (e.g., mm if the world unit is assumed to be cm).
        """
    @verticalApertureOffset.setter
    def verticalApertureOffset(*args, **kwargs):
        ...
    @property
    def verticalFieldOfView(*args, **kwargs):
        ...
class DualQuatd(Boost.Python.instance):
    """
    """
    @staticmethod
    def GetConjugate(*args, **kwargs):
        """
        
        GetConjugate() -> DualQuatd
        
        
        Returns the conjugate of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetDual(*args, **kwargs):
        """
        
        GetDual() -> Quatd
        
        
        Returns the dual part of the dual quaternion.
        
        
        
        """
    @staticmethod
    def GetIdentity(*args, **kwargs):
        """
        
        **classmethod** GetIdentity() -> DualQuatd
        
        
        Returns the identity dual quaternion, which has a real part of
        (1,0,0,0) and a dual part of (0,0,0,0).
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse() -> DualQuatd
        
        
        Returns the inverse of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> tuple[float, float]
        
        
        Returns geometric length of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> DualQuatd
        
        
        Returns a normalized (unit-length) version of this dual quaternion.
        
        
        If the length of this dual quaternion is smaller than ``eps`` , this
        returns the identity dual quaternion.
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def GetReal(*args, **kwargs):
        """
        
        GetReal() -> Quatd
        
        
        Returns the real part of the dual quaternion.
        
        
        
        """
    @staticmethod
    def GetTranslation(*args, **kwargs):
        """
        
        GetTranslation() -> Vec3d
        
        
        Get the translation component of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetZero(*args, **kwargs):
        """
        
        **classmethod** GetZero() -> DualQuatd
        
        
        Returns the zero dual quaternion, which has a real part of (0,0,0,0)
        and a dual part of (0,0,0,0).
        
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> tuple[float, float]
        
        
        Normalizes this dual quaternion in place.
        
        
        Normalizes this dual quaternion in place to unit length, returning the
        length before normalization. If the length of this dual quaternion is
        smaller than ``eps`` , this sets the dual quaternion to identity.
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def SetDual(*args, **kwargs):
        """
        
        SetDual(dual) -> None
        
        
        Sets the dual part of the dual quaternion.
        
        
        Parameters
        ----------
        dual : Quatd
        
        
        """
    @staticmethod
    def SetReal(*args, **kwargs):
        """
        
        SetReal(real) -> None
        
        
        Sets the real part of the dual quaternion.
        
        
        Parameters
        ----------
        real : Quatd
        
        
        """
    @staticmethod
    def SetTranslation(*args, **kwargs):
        """
        
        SetTranslation(translation) -> None
        
        
        Set the translation component of this dual quaternion.
        
        
        Parameters
        ----------
        translation : Vec3d
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(vec) -> Vec3d
        
        
        Transforms the row vector *vec* by the dual quaternion.
        
        
        Parameters
        ----------
        vec : Vec3d
        
        
        """
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
        """
        
        __init__()
        
        
        The default constructor leaves the dual quaternion undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(realVal)
        
        
        Initialize the real part to ``realVal`` and the imaginary part to zero
        quaternion.
        
        
        Since quaternions typically must be normalized, reasonable values for
        ``realVal`` are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        
        
        Parameters
        ----------
        realVal : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real)
        
        
        Initialize the real part to ``real`` quaternion and the imaginary part
        to zero quaternion.
        
        
        Parameters
        ----------
        real : Quatd
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real, dual)
        
        
        This constructor initializes the real and dual parts.
        
        
        Parameters
        ----------
        real : Quatd
        
        dual : Quatd
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rotation, translation)
        
        
        This constructor initializes from a rotation and a translation
        components.
        
        
        Parameters
        ----------
        rotation : Quatd
        
        translation : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfDualQuatf.
        
        
        Parameters
        ----------
        other : DualQuatf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfDualQuath.
        
        
        Parameters
        ----------
        other : DualQuath
        
        
        """
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
    """
    """
    @staticmethod
    def GetConjugate(*args, **kwargs):
        """
        
        GetConjugate() -> DualQuatf
        
        
        Returns the conjugate of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetDual(*args, **kwargs):
        """
        
        GetDual() -> Quatf
        
        
        Returns the dual part of the dual quaternion.
        
        
        
        """
    @staticmethod
    def GetIdentity(*args, **kwargs):
        """
        
        **classmethod** GetIdentity() -> DualQuatf
        
        
        Returns the identity dual quaternion, which has a real part of
        (1,0,0,0) and a dual part of (0,0,0,0).
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse() -> DualQuatf
        
        
        Returns the inverse of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> tuple[float, float]
        
        
        Returns geometric length of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> DualQuatf
        
        
        Returns a normalized (unit-length) version of this dual quaternion.
        
        
        If the length of this dual quaternion is smaller than ``eps`` , this
        returns the identity dual quaternion.
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def GetReal(*args, **kwargs):
        """
        
        GetReal() -> Quatf
        
        
        Returns the real part of the dual quaternion.
        
        
        
        """
    @staticmethod
    def GetTranslation(*args, **kwargs):
        """
        
        GetTranslation() -> Vec3f
        
        
        Get the translation component of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetZero(*args, **kwargs):
        """
        
        **classmethod** GetZero() -> DualQuatf
        
        
        Returns the zero dual quaternion, which has a real part of (0,0,0,0)
        and a dual part of (0,0,0,0).
        
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> tuple[float, float]
        
        
        Normalizes this dual quaternion in place.
        
        
        Normalizes this dual quaternion in place to unit length, returning the
        length before normalization. If the length of this dual quaternion is
        smaller than ``eps`` , this sets the dual quaternion to identity.
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def SetDual(*args, **kwargs):
        """
        
        SetDual(dual) -> None
        
        
        Sets the dual part of the dual quaternion.
        
        
        Parameters
        ----------
        dual : Quatf
        
        
        """
    @staticmethod
    def SetReal(*args, **kwargs):
        """
        
        SetReal(real) -> None
        
        
        Sets the real part of the dual quaternion.
        
        
        Parameters
        ----------
        real : Quatf
        
        
        """
    @staticmethod
    def SetTranslation(*args, **kwargs):
        """
        
        SetTranslation(translation) -> None
        
        
        Set the translation component of this dual quaternion.
        
        
        Parameters
        ----------
        translation : Vec3f
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(vec) -> Vec3f
        
        
        Transforms the row vector *vec* by the dual quaternion.
        
        
        Parameters
        ----------
        vec : Vec3f
        
        
        """
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
        """
        
        __init__()
        
        
        The default constructor leaves the dual quaternion undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(realVal)
        
        
        Initialize the real part to ``realVal`` and the imaginary part to zero
        quaternion.
        
        
        Since quaternions typically must be normalized, reasonable values for
        ``realVal`` are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        
        
        Parameters
        ----------
        realVal : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real)
        
        
        Initialize the real part to ``real`` quaternion and the imaginary part
        to zero quaternion.
        
        
        Parameters
        ----------
        real : Quatf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real, dual)
        
        
        This constructor initializes the real and dual parts.
        
        
        Parameters
        ----------
        real : Quatf
        
        dual : Quatf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rotation, translation)
        
        
        This constructor initializes from a rotation and a translation
        components.
        
        
        Parameters
        ----------
        rotation : Quatf
        
        translation : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfDualQuatd.
        
        
        Parameters
        ----------
        other : DualQuatd
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfDualQuath.
        
        
        Parameters
        ----------
        other : DualQuath
        
        
        """
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
    """
    """
    @staticmethod
    def GetConjugate(*args, **kwargs):
        """
        
        GetConjugate() -> DualQuath
        
        
        Returns the conjugate of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetDual(*args, **kwargs):
        """
        
        GetDual() -> Quath
        
        
        Returns the dual part of the dual quaternion.
        
        
        
        """
    @staticmethod
    def GetIdentity(*args, **kwargs):
        """
        
        **classmethod** GetIdentity() -> DualQuath
        
        
        Returns the identity dual quaternion, which has a real part of
        (1,0,0,0) and a dual part of (0,0,0,0).
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse() -> DualQuath
        
        
        Returns the inverse of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> tuple[GfHalf, GfHalf]
        
        
        Returns geometric length of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> DualQuath
        
        
        Returns a normalized (unit-length) version of this dual quaternion.
        
        
        If the length of this dual quaternion is smaller than ``eps`` , this
        returns the identity dual quaternion.
        
        
        Parameters
        ----------
        eps : GfHalf
        
        
        """
    @staticmethod
    def GetReal(*args, **kwargs):
        """
        
        GetReal() -> Quath
        
        
        Returns the real part of the dual quaternion.
        
        
        
        """
    @staticmethod
    def GetTranslation(*args, **kwargs):
        """
        
        GetTranslation() -> Vec3h
        
        
        Get the translation component of this dual quaternion.
        
        
        
        """
    @staticmethod
    def GetZero(*args, **kwargs):
        """
        
        **classmethod** GetZero() -> DualQuath
        
        
        Returns the zero dual quaternion, which has a real part of (0,0,0,0)
        and a dual part of (0,0,0,0).
        
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> tuple[GfHalf, GfHalf]
        
        
        Normalizes this dual quaternion in place.
        
        
        Normalizes this dual quaternion in place to unit length, returning the
        length before normalization. If the length of this dual quaternion is
        smaller than ``eps`` , this sets the dual quaternion to identity.
        
        
        Parameters
        ----------
        eps : GfHalf
        
        
        """
    @staticmethod
    def SetDual(*args, **kwargs):
        """
        
        SetDual(dual) -> None
        
        
        Sets the dual part of the dual quaternion.
        
        
        Parameters
        ----------
        dual : Quath
        
        
        """
    @staticmethod
    def SetReal(*args, **kwargs):
        """
        
        SetReal(real) -> None
        
        
        Sets the real part of the dual quaternion.
        
        
        Parameters
        ----------
        real : Quath
        
        
        """
    @staticmethod
    def SetTranslation(*args, **kwargs):
        """
        
        SetTranslation(translation) -> None
        
        
        Set the translation component of this dual quaternion.
        
        
        Parameters
        ----------
        translation : Vec3h
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(vec) -> Vec3h
        
        
        Transforms the row vector *vec* by the dual quaternion.
        
        
        Parameters
        ----------
        vec : Vec3h
        
        
        """
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
        """
        
        __init__()
        
        
        The default constructor leaves the dual quaternion undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(realVal)
        
        
        Initialize the real part to ``realVal`` and the imaginary part to zero
        quaternion.
        
        
        Since quaternions typically must be normalized, reasonable values for
        ``realVal`` are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        
        
        Parameters
        ----------
        realVal : GfHalf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real)
        
        
        Initialize the real part to ``real`` quaternion and the imaginary part
        to zero quaternion.
        
        
        Parameters
        ----------
        real : Quath
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real, dual)
        
        
        This constructor initializes the real and dual parts.
        
        
        Parameters
        ----------
        real : Quath
        
        dual : Quath
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rotation, translation)
        
        
        This constructor initializes from a rotation and a translation
        components.
        
        
        Parameters
        ----------
        rotation : Quath
        
        translation : Vec3h
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfDualQuatd.
        
        
        Parameters
        ----------
        other : DualQuatd
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfDualQuatf.
        
        
        Parameters
        ----------
        other : DualQuatf
        
        
        """
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
        """
        
        This enum is used to determine the type of projection represented by a
        frustum.
        
        """
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
    __instance_size__: typing.ClassVar[int] = 144
    @staticmethod
    def ComputeAspectRatio(*args, **kwargs):
        """
        
        ComputeAspectRatio() -> float
        
        
        Returns the aspect ratio of the frustum, defined as the width of the
        window divided by the height.
        
        
        If the height is zero or negative, this returns 0.
        
        
        
        """
    @staticmethod
    def ComputeCorners(*args, **kwargs):
        """
        
        ComputeCorners() -> list[Vec3d]
        
        
        Returns the world-space corners of the frustum as a vector of 8
        points, ordered as:
        
        
        
           - Left bottom near
        
           - Right bottom near
        
           - Left top near
        
           - Right top near
        
           - Left bottom far
        
           - Right bottom far
        
           - Left top far
        
           - Right top far
        
        
        
        
        """
    @staticmethod
    def ComputeCornersAtDistance(*args, **kwargs):
        """
        
        ComputeCornersAtDistance(d) -> list[Vec3d]
        
        
        Returns the world-space corners of the intersection of the frustum
        with a plane parallel to the near/far plane at distance d from the
        apex, ordered as:
        
        
        
           - Left bottom
        
           - Right bottom
        
           - Left top
        
           - Right top In particular, it gives the partial result of
             ComputeCorners when given near or far distance.
        
        
        
        Parameters
        ----------
        d : float
        
        
        """
    @staticmethod
    def ComputeLookAtPoint(*args, **kwargs):
        """
        
        ComputeLookAtPoint() -> Vec3d
        
        
        Computes and returns the world-space look-at point from the eye point
        (position), view direction (rotation), and view distance.
        
        
        
        """
    @staticmethod
    def ComputeNarrowedFrustum(*args, **kwargs):
        """
        
        ComputeNarrowedFrustum(windowPos, size) -> Frustum
        
        
        Returns a frustum that is a narrowed-down version of this frustum.
        
        
        The new frustum has the same near and far planes, but the other planes
        are adjusted to be centered on ``windowPos`` with the new width and
        height obtained from the existing width and height by multiplying by
        ``size`` [0] and ``size`` [1], respectively. Finally, the new frustum
        is clipped against this frustum so that it is completely contained in
        the existing frustum.
        
        ``windowPos`` is given in normalized coords (-1 to +1 in both
        dimensions). ``size`` is given as a scalar (0 to 1 in both
        dimensions).
        
        If the ``windowPos`` or ``size`` given is outside these ranges, it may
        result in returning a collapsed frustum.
        
        This method is useful for computing a volume to use for interactive
        picking.
        
        
        Parameters
        ----------
        windowPos : Vec2d
        
        size : Vec2d
        
        
        
        ----------------------------------------------------------------------
        
        ComputeNarrowedFrustum(worldPoint, size) -> Frustum
        
        
        Returns a frustum that is a narrowed-down version of this frustum.
        
        
        The new frustum has the same near and far planes, but the other planes
        are adjusted to be centered on ``worldPoint`` with the new width and
        height obtained from the existing width and height by multiplying by
        ``size`` [0] and ``size`` [1], respectively. Finally, the new frustum
        is clipped against this frustum so that it is completely contained in
        the existing frustum.
        
        ``worldPoint`` is given in world space coordinates. ``size`` is given
        as a scalar (0 to 1 in both dimensions).
        
        If the ``size`` given is outside this range, it may result in
        returning a collapsed frustum.
        
        If the ``worldPoint`` is at or behind the eye of the frustum, it will
        return a frustum equal to this frustum.
        
        This method is useful for computing a volume to use for interactive
        picking.
        
        
        Parameters
        ----------
        worldPoint : Vec3d
        
        size : Vec2d
        
        
        """
    @staticmethod
    def ComputePickRay(*args, **kwargs):
        """
        
        ComputePickRay(windowPos) -> Ray
        
        
        Builds and returns a ``GfRay`` that can be used for picking at the
        given normalized (-1 to +1 in both dimensions) window position.
        
        
        Contrasted with ComputeRay() , that method returns a ray whose origin
        is the eyepoint, while this method returns a ray whose origin is on
        the near plane.
        
        
        Parameters
        ----------
        windowPos : Vec2d
        
        
        
        ----------------------------------------------------------------------
        
        ComputePickRay(worldSpacePos) -> Ray
        
        
        Builds and returns a ``GfRay`` that can be used for picking that
        connects the viewpoint to the given 3d point in worldspace.
        
        
        Parameters
        ----------
        worldSpacePos : Vec3d
        
        
        """
    @staticmethod
    def ComputeProjectionMatrix(*args, **kwargs):
        """
        
        ComputeProjectionMatrix() -> Matrix4d
        
        
        Returns a GL-style projection matrix corresponding to the frustum's
        projection.
        
        
        
        """
    @staticmethod
    def ComputeUpVector(*args, **kwargs):
        """
        
        ComputeUpVector() -> Vec3d
        
        
        Returns the normalized world-space up vector, which is computed by
        rotating the y axis by the frustum's rotation.
        
        
        
        """
    @staticmethod
    def ComputeViewDirection(*args, **kwargs):
        """
        
        ComputeViewDirection() -> Vec3d
        
        
        Returns the normalized world-space view direction vector, which is
        computed by rotating the -z axis by the frustum's rotation.
        
        
        
        """
    @staticmethod
    def ComputeViewFrame(*args, **kwargs):
        """
        
        ComputeViewFrame(side, up, view) -> None
        
        
        Computes the view frame defined by this frustum.
        
        
        The frame consists of the view direction, up vector and side vector,
        as shown in this diagram.
        
        .. code-block:: text
        
          up
          ^   ^
          |  / 
          | / view
          |/
          +- - - - > side
        
        
        
        Parameters
        ----------
        side : Vec3d
        
        up : Vec3d
        
        view : Vec3d
        
        
        """
    @staticmethod
    def ComputeViewInverse(*args, **kwargs):
        """
        
        ComputeViewInverse() -> Matrix4d
        
        
        Returns a matrix that represents the inverse viewing transformation
        for this frustum.
        
        
        That is, it returns the matrix that converts points from eye (frustum)
        space to world space.
        
        
        
        """
    @staticmethod
    def ComputeViewMatrix(*args, **kwargs):
        """
        
        ComputeViewMatrix() -> Matrix4d
        
        
        Returns a matrix that represents the viewing transformation for this
        frustum.
        
        
        That is, it returns the matrix that converts points from world space
        to eye (frustum) space.
        
        
        
        """
    @staticmethod
    def FitToSphere(*args, **kwargs):
        """
        
        FitToSphere(center, radius, slack) -> None
        
        
        Modifies the frustum to tightly enclose a sphere with the given center
        and radius, using the current view direction.
        
        
        The planes of the frustum are adjusted as necessary. The given amount
        of slack is added to the sphere's radius is used around the sphere to
        avoid boundary problems.
        
        
        Parameters
        ----------
        center : Vec3d
        
        radius : float
        
        slack : float
        
        
        """
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
        """
        
        GetNearFar() -> Range1d
        
        
        Returns the near/far interval.
        
        
        
        """
    @staticmethod
    def GetOrthographic(*args, **kwargs):
        """
        
        GetOrthographic(left, right, bottom, top, nearPlane, farPlane) -> bool
        
        
        Returns the current frustum in the format used by
        ``SetOrthographic()`` .
        
        
        If the current frustum is not an orthographic projection, this returns
        ``false`` and leaves the parameters untouched.
        
        
        Parameters
        ----------
        left : float
        
        right : float
        
        bottom : float
        
        top : float
        
        nearPlane : float
        
        farPlane : float
        
        
        """
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
        """
        
        GetPosition() -> Vec3d
        
        
        Returns the position of the frustum in world space.
        
        
        
        """
    @staticmethod
    def GetProjectionType(*args, **kwargs):
        """
        
        GetProjectionType() -> Frustum.ProjectionType
        
        
        Returns the projection type.
        
        
        
        """
    @staticmethod
    def GetReferencePlaneDepth(*args, **kwargs):
        """
        
        **classmethod** GetReferencePlaneDepth() -> float
        
        
        Returns the depth of the reference plane.
        
        
        
        """
    @staticmethod
    def GetRotation(*args, **kwargs):
        """
        
        GetRotation() -> Rotation
        
        
        Returns the orientation of the frustum in world space as a rotation to
        apply to the -z axis.
        
        
        
        """
    @staticmethod
    def GetViewDistance(*args, **kwargs):
        """
        
        GetViewDistance() -> float
        
        
        Returns the view distance.
        
        
        
        """
    @staticmethod
    def GetWindow(*args, **kwargs):
        """
        
        GetWindow() -> Range2d
        
        
        Returns the window rectangle in the reference plane.
        
        
        
        """
    @staticmethod
    def Intersects(*args, **kwargs):
        """
        
        Intersects(bbox) -> bool
        
        
        Returns true if the given axis-aligned bbox is inside or intersecting
        the frustum.
        
        
        Otherwise, it returns false. Useful when doing picking or frustum
        culling.
        
        
        Parameters
        ----------
        bbox : BBox3d
        
        
        
        ----------------------------------------------------------------------
        
        Intersects(point) -> bool
        
        
        Returns true if the given point is inside or intersecting the frustum.
        
        
        Otherwise, it returns false.
        
        
        Parameters
        ----------
        point : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        Intersects(p0, p1) -> bool
        
        
        Returns ``true`` if the line segment formed by the given points is
        inside or intersecting the frustum.
        
        
        Otherwise, it returns false.
        
        
        Parameters
        ----------
        p0 : Vec3d
        
        p1 : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        Intersects(p0, p1, p2) -> bool
        
        
        Returns ``true`` if the triangle formed by the given points is inside
        or intersecting the frustum.
        
        
        Otherwise, it returns false.
        
        
        Parameters
        ----------
        p0 : Vec3d
        
        p1 : Vec3d
        
        p2 : Vec3d
        
        
        """
    @staticmethod
    def IntersectsViewVolume(*args, **kwargs):
        """
        
        **classmethod** IntersectsViewVolume(bbox, vpMat) -> bool
        
        
        Returns ``true`` if the bbox volume intersects the view volume given
        by the view-projection matrix, erring on the side of false positives
        for efficiency.
        
        
        This method is intended for cases where a GfFrustum is not available
        or when the view-projection matrix yields a view volume that is not
        expressable as a GfFrustum.
        
        Because it errs on the side of false positives, it is suitable for
        early-out tests such as draw or intersection culling.
        
        
        Parameters
        ----------
        bbox : BBox3d
        
        vpMat : Matrix4d
        
        
        """
    @staticmethod
    def SetNearFar(*args, **kwargs):
        """
        
        SetNearFar(nearFar) -> None
        
        
        Sets the near/far interval.
        
        
        Parameters
        ----------
        nearFar : Range1d
        
        
        """
    @staticmethod
    def SetOrthographic(*args, **kwargs):
        """
        
        SetOrthographic(left, right, bottom, top, nearPlane, farPlane) -> None
        
        
        Sets up the frustum in a manner similar to ``glOrtho()`` .
        
        
        Sets the projection to ``GfFrustum::Orthographic`` and sets the window
        and near/far specifications based on the given values.
        
        
        Parameters
        ----------
        left : float
        
        right : float
        
        bottom : float
        
        top : float
        
        nearPlane : float
        
        farPlane : float
        
        
        """
    @staticmethod
    def SetPerspective(*args, **kwargs):
        """
        
        SetPerspective(fieldOfViewHeight, aspectRatio, nearDistance, farDistance) -> None
        
        
        Sets up the frustum in a manner similar to ``gluPerspective()`` .
        
        
        It sets the projection type to ``GfFrustum::Perspective`` and sets the
        window specification so that the resulting symmetric frustum encloses
        an angle of ``fieldOfViewHeight`` degrees in the vertical direction,
        with ``aspectRatio`` used to figure the angle in the horizontal
        direction. The near and far distances are specified as well. The
        window coordinates are computed as:
        
        .. code-block:: text
        
          top    = tan(fieldOfViewHeight / 2)
          bottom = -top
          right  = top \\* aspectRatio
          left   = -right
          near   = nearDistance
          far    = farDistance
        
        
        
        Parameters
        ----------
        fieldOfViewHeight : float
        
        aspectRatio : float
        
        nearDistance : float
        
        farDistance : float
        
        
        
        ----------------------------------------------------------------------
        
        SetPerspective(fieldOfView, isFovVertical, aspectRatio, nearDistance, farDistance) -> None
        
        
        Sets up the frustum in a manner similar to gluPerspective().
        
        
        It sets the projection type to ``GfFrustum::Perspective`` and sets the
        window specification so that:
        
        If *isFovVertical* is true, the resulting symmetric frustum encloses
        an angle of ``fieldOfView`` degrees in the vertical direction, with
        ``aspectRatio`` used to figure the angle in the horizontal direction.
        
        If *isFovVertical* is false, the resulting symmetric frustum encloses
        an angle of ``fieldOfView`` degrees in the horizontal direction, with
        ``aspectRatio`` used to figure the angle in the vertical direction.
        
        The near and far distances are specified as well. The window
        coordinates are computed as follows:
        
           - if isFovVertical:
        
           - top = tan(fieldOfView / 2)
        
           - right = top \\* aspectRatio
        
           - if NOT isFovVertical:
        
           - right = tan(fieldOfView / 2)
        
           - top = right / aspectRation
        
           - bottom = -top
        
           - left = -right
        
           - near = nearDistance
        
           - far = farDistance
        
        
        
        Parameters
        ----------
        fieldOfView : float
        
        isFovVertical : bool
        
        aspectRatio : float
        
        nearDistance : float
        
        farDistance : float
        
        
        """
    @staticmethod
    def SetPosition(*args, **kwargs):
        """
        
        SetPosition(position) -> None
        
        
        Sets the position of the frustum in world space.
        
        
        Parameters
        ----------
        position : Vec3d
        
        
        """
    @staticmethod
    def SetPositionAndRotationFromMatrix(*args, **kwargs):
        """
        
        SetPositionAndRotationFromMatrix(camToWorldXf) -> None
        
        
        Sets the position and rotation of the frustum from a camera matrix
        (always from a y-Up camera).
        
        
        The resulting frustum's transform will always represent a right-handed
        and orthonormal coordinate sytem (scale, shear, and projection are
        removed from the given ``camToWorldXf`` ).
        
        
        Parameters
        ----------
        camToWorldXf : Matrix4d
        
        
        """
    @staticmethod
    def SetProjectionType(*args, **kwargs):
        """
        
        SetProjectionType(projectionType) -> None
        
        
        Sets the projection type.
        
        
        Parameters
        ----------
        projectionType : Frustum.ProjectionType
        
        
        """
    @staticmethod
    def SetRotation(*args, **kwargs):
        """
        
        SetRotation(rotation) -> None
        
        
        Sets the orientation of the frustum in world space as a rotation to
        apply to the default frame: looking along the -z axis with the +y axis
        as"up".
        
        
        Parameters
        ----------
        rotation : Rotation
        
        
        """
    @staticmethod
    def SetViewDistance(*args, **kwargs):
        """
        
        SetViewDistance(viewDistance) -> None
        
        
        Sets the view distance.
        
        
        Parameters
        ----------
        viewDistance : float
        
        
        """
    @staticmethod
    def SetWindow(*args, **kwargs):
        """
        
        SetWindow(window) -> None
        
        
        Sets the window rectangle in the reference plane that defines the
        left, right, top, and bottom planes of the frustum.
        
        
        Parameters
        ----------
        window : Range2d
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(matrix) -> Frustum
        
        
        Transforms the frustum by the given matrix.
        
        
        The transformation matrix is applied as follows: the position and the
        direction vector are transformed with the given matrix. Then the
        length of the new direction vector is used to rescale the near and far
        plane and the view distance. Finally, the points that define the
        reference plane are transformed by the matrix. This method assures
        that the frustum will not be sheared or perspective-projected.
        
        Note that this definition means that the transformed frustum does not
        preserve scales very well. Do *not* use this function to transform a
        frustum that is to be used for precise operations such as intersection
        testing.
        
        
        Parameters
        ----------
        matrix : Matrix4d
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        This constructor creates an instance with default viewing parameters:
        
        
        
           - The position is the origin.
        
           - The rotation is the identity rotation. (The view is along the -z
             axis, with the +y axis as"up").
        
           - The window is -1 to +1 in both dimensions.
        
           - The near/far interval is (1, 10).
        
           - The view distance is 5.0.
        
           - The projection type is ``GfFrustum::Perspective`` .
        
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(o)
        
        
        Copy constructor.
        
        
        Parameters
        ----------
        o : Frustum
        
        
        
        ----------------------------------------------------------------------
        
        __init__(o)
        
        
        Move constructor.
        
        
        Parameters
        ----------
        o : Frustum
        
        
        
        ----------------------------------------------------------------------
        
        __init__(position, rotation, window, nearFar, projectionType, viewDistance)
        
        
        This constructor creates an instance with the given viewing
        parameters.
        
        
        Parameters
        ----------
        position : Vec3d
        
        rotation : Rotation
        
        window : Range2d
        
        nearFar : Range1d
        
        projectionType : Frustum.ProjectionType
        
        viewDistance : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(camToWorldXf, window, nearFar, projectionType, viewDistance)
        
        
        This constructor creates an instance from a camera matrix (always of a
        y-Up camera, also see SetPositionAndRotationFromMatrix) and the given
        viewing parameters.
        
        
        Parameters
        ----------
        camToWorldXf : Matrix4d
        
        window : Range2d
        
        nearFar : Range1d
        
        projectionType : Frustum.ProjectionType
        
        viewDistance : float
        
        
        """
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
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        
        Returns true if x is inside the interval.
        
        Returns true if x is inside the interval.
        """
    @staticmethod
    def GetFullInterval(*args, **kwargs):
        """
        
        **classmethod** GetFullInterval() -> Interval
        
        
        Returns the full interval (-inf, inf).
        
        
        
        """
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
        """
        
        Intersects(i) -> bool
        
        
        Return true iff the given interval i intersects this interval.
        
        
        Parameters
        ----------
        i : Interval
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        
        True if the interval is empty.
        """
    @staticmethod
    def IsFinite(*args, **kwargs):
        """
        
        IsFinite() -> bool
        
        
        Returns true if both the maximum and minimum value are finite.
        
        
        
        """
    @staticmethod
    def IsMaxClosed(*args, **kwargs):
        """
        
        IsMaxClosed() -> bool
        
        
        Maximum boundary condition.
        
        
        
        """
    @staticmethod
    def IsMaxFinite(*args, **kwargs):
        """
        
        IsMaxFinite() -> bool
        
        
        Returns true if the maximum value is finite.
        
        
        
        """
    @staticmethod
    def IsMaxOpen(*args, **kwargs):
        """
        
        IsMaxOpen() -> bool
        
        
        Maximum boundary condition.
        
        
        
        """
    @staticmethod
    def IsMinClosed(*args, **kwargs):
        """
        
        IsMinClosed() -> bool
        
        
        Minimum boundary condition.
        
        
        
        """
    @staticmethod
    def IsMinFinite(*args, **kwargs):
        """
        
        IsMinFinite() -> bool
        
        
        Returns true if the minimum value is finite.
        
        
        
        """
    @staticmethod
    def IsMinOpen(*args, **kwargs):
        """
        
        IsMinOpen() -> bool
        
        
        Minimum boundary condition.
        
        
        
        """
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
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def FindClosestPoint(*args, **kwargs):
        """
        
        FindClosestPoint(point, t) -> Vec3d
        
        
        Returns the point on the line that is closest to ``point`` .
        
        
        If ``t`` is not ``None`` , it will be set to the parametric distance
        along the line of the returned point.
        
        
        Parameters
        ----------
        point : Vec3d
        
        t : float
        
        
        """
    @staticmethod
    def GetDirection(*args, **kwargs):
        """
        
        GetDirection() -> Vec3d
        
        
        Return the normalized direction of the line.
        
        
        
        """
    @staticmethod
    def GetPoint(*args, **kwargs):
        """
        
        GetPoint(t) -> Vec3d
        
        
        Return the point on the line at ```` ( p0 + t \\* dir).
        
        
        Remember dir has been normalized so t represents a unit distance.
        
        
        Parameters
        ----------
        t : float
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(p0, dir) -> float
        
        
        Parameters
        ----------
        p0 : Vec3d
        
        dir : Vec3d
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        The default constructor leaves line parameters undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p0, dir)
        
        
        Construct a line from a point and a direction.
        
        
        Parameters
        ----------
        p0 : Vec3d
        
        dir : Vec3d
        
        
        """
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
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def FindClosestPoint(*args, **kwargs):
        """
        
        FindClosestPoint(point, t) -> Vec3d
        
        
        Returns the point on the line that is closest to ``point`` .
        
        
        If ``t`` is not ``None`` , it will be set to the parametric distance
        along the line of the closest point.
        
        
        Parameters
        ----------
        point : Vec3d
        
        t : float
        
        
        """
    @staticmethod
    def GetDirection(*args, **kwargs):
        """
        
        GetDirection() -> Vec3d
        
        
        Return the normalized direction of the line.
        
        
        
        """
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> float
        
        
        Return the length of the line.
        
        
        
        """
    @staticmethod
    def GetPoint(*args, **kwargs):
        """
        
        GetPoint(t) -> Vec3d
        
        
        Return the point on the segment specified by the parameter t.
        
        
        p = p0 + t \\* (p1 - p0)
        
        
        Parameters
        ----------
        t : float
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        The default constructor leaves line parameters undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p0, p1)
        
        
        Construct a line segment that spans two points.
        
        
        Parameters
        ----------
        p0 : Vec3d
        
        p1 : Vec3d
        
        
        """
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
    """
    """
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (2, 2)
    @staticmethod
    def GetColumn(*args, **kwargs):
        """
        
        GetColumn(i) -> Vec2d
        
        
        Gets a column of the matrix as a Vec2.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        """
        
        GetDeterminant() -> float
        
        
        Returns the determinant of the matrix.
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse(det, eps) -> Matrix2d
        
        
        Returns the inverse of the matrix, or FLT_MAX \\* SetIdentity() if the
        matrix is singular.
        
        
        (FLT_MAX is the largest value a ``float`` can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        ``\\*det`` is set to the determinant.
        
        
        Parameters
        ----------
        det : float
        
        eps : float
        
        
        """
    @staticmethod
    def GetRow(*args, **kwargs):
        """
        
        GetRow(i) -> Vec2d
        
        
        Gets a row of the matrix as a Vec2.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetTranspose(*args, **kwargs):
        """
        
        GetTranspose() -> Matrix2d
        
        
        Returns the transpose of the matrix.
        
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(m00, m01, m10, m11) -> Matrix2d
        
        
        Sets the matrix from 4 independent ``double`` values, specified in
        row-major order.
        
        
        For example, parameter *m10* specifies the value in row 1 and column
        0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m10 : float
        
        m11 : float
        
        
        
        ----------------------------------------------------------------------
        
        Set(m) -> Matrix2d
        
        
        Sets the matrix from a 2x2 array of ``double`` values, specified in
        row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        """
    @staticmethod
    def SetColumn(*args, **kwargs):
        """
        
        SetColumn(i, v) -> None
        
        
        Sets a column of the matrix from a Vec2.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec2d
        
        
        """
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        """
        
        SetDiagonal(s) -> Matrix2d
        
        
        Sets the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        SetDiagonal(arg1) -> Matrix2d
        
        
        Sets the matrix to have diagonal ( ``v[0], v[1]`` ).
        
        
        Parameters
        ----------
        arg1 : Vec2d
        
        
        """
    @staticmethod
    def SetIdentity(*args, **kwargs):
        """
        
        SetIdentity() -> Matrix2d
        
        
        Sets the matrix to the identity matrix.
        
        
        
        """
    @staticmethod
    def SetRow(*args, **kwargs):
        """
        
        SetRow(i, v) -> None
        
        
        Sets a row of the matrix from a Vec2.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec2d
        
        
        """
    @staticmethod
    def SetZero(*args, **kwargs):
        """
        
        SetZero() -> Matrix2d
        
        
        Sets the matrix to zero.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor. Leaves the matrix component values undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m00, m01, m10, m11)
        
        
        Constructor.
        
        
        Initializes the matrix from 4 independent ``double`` values, specified
        in row-major order. For example, parameter *m10* specifies the value
        in row 1 and column 0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m10 : float
        
        m11 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        Constructor.
        
        
        Initializes the matrix from a 2x2 array of ``double`` values,
        specified in row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s)
        
        
        This explicit constructor initializes the matrix to ``s`` times the
        identity matrix.
        
        
        Parameters
        ----------
        s : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to ``v[i]`` .
        
        
        Parameters
        ----------
        v : Vec2d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of double. The vector
        is expected to be 2x2. If it is too big, only the first 2 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of float. The vector is
        expected to be 2x2. If it is too big, only the first 2 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        This explicit constructor converts a"float"matrix to a"double"matrix.
        
        
        Parameters
        ----------
        m : Matrix2f
        
        
        """
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
    """
    """
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (2, 2)
    @staticmethod
    def GetColumn(*args, **kwargs):
        """
        
        GetColumn(i) -> Vec2f
        
        
        Gets a column of the matrix as a Vec2.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        """
        
        GetDeterminant() -> float
        
        
        Returns the determinant of the matrix.
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse(det, eps) -> Matrix2f
        
        
        Returns the inverse of the matrix, or FLT_MAX \\* SetIdentity() if the
        matrix is singular.
        
        
        (FLT_MAX is the largest value a ``float`` can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        ``\\*det`` is set to the determinant.
        
        
        Parameters
        ----------
        det : float
        
        eps : float
        
        
        """
    @staticmethod
    def GetRow(*args, **kwargs):
        """
        
        GetRow(i) -> Vec2f
        
        
        Gets a row of the matrix as a Vec2.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetTranspose(*args, **kwargs):
        """
        
        GetTranspose() -> Matrix2f
        
        
        Returns the transpose of the matrix.
        
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(m00, m01, m10, m11) -> Matrix2f
        
        
        Sets the matrix from 4 independent ``float`` values, specified in row-
        major order.
        
        
        For example, parameter *m10* specifies the value in row 1 and column
        0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m10 : float
        
        m11 : float
        
        
        
        ----------------------------------------------------------------------
        
        Set(m) -> Matrix2f
        
        
        Sets the matrix from a 2x2 array of ``float`` values, specified in
        row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        """
    @staticmethod
    def SetColumn(*args, **kwargs):
        """
        
        SetColumn(i, v) -> None
        
        
        Sets a column of the matrix from a Vec2.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec2f
        
        
        """
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        """
        
        SetDiagonal(s) -> Matrix2f
        
        
        Sets the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        SetDiagonal(arg1) -> Matrix2f
        
        
        Sets the matrix to have diagonal ( ``v[0], v[1]`` ).
        
        
        Parameters
        ----------
        arg1 : Vec2f
        
        
        """
    @staticmethod
    def SetIdentity(*args, **kwargs):
        """
        
        SetIdentity() -> Matrix2f
        
        
        Sets the matrix to the identity matrix.
        
        
        
        """
    @staticmethod
    def SetRow(*args, **kwargs):
        """
        
        SetRow(i, v) -> None
        
        
        Sets a row of the matrix from a Vec2.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec2f
        
        
        """
    @staticmethod
    def SetZero(*args, **kwargs):
        """
        
        SetZero() -> Matrix2f
        
        
        Sets the matrix to zero.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor. Leaves the matrix component values undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m00, m01, m10, m11)
        
        
        Constructor.
        
        
        Initializes the matrix from 4 independent ``float`` values, specified
        in row-major order. For example, parameter *m10* specifies the value
        in row 1 and column 0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m10 : float
        
        m11 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        Constructor.
        
        
        Initializes the matrix from a 2x2 array of ``float`` values, specified
        in row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s)
        
        
        This explicit constructor initializes the matrix to ``s`` times the
        identity matrix.
        
        
        Parameters
        ----------
        s : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to ``v[i]`` .
        
        
        Parameters
        ----------
        v : Vec2f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of double. The vector
        is expected to be 2x2. If it is too big, only the first 2 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of float. The vector is
        expected to be 2x2. If it is too big, only the first 2 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        This explicit constructor converts a"double"matrix to a"float"matrix.
        
        
        Parameters
        ----------
        m : Matrix2d
        
        
        """
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
    """
    """
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (3, 3)
    @staticmethod
    def ExtractRotation(*args, **kwargs):
        """
        
        ExtractRotation() -> Rotation
        
        
        Returns the rotation corresponding to this matrix.
        
        
        This works well only if the matrix represents a rotation.
        
        For good results, consider calling Orthonormalize() before calling
        this method.
        
        
        
        """
    @staticmethod
    def GetColumn(*args, **kwargs):
        """
        
        GetColumn(i) -> Vec3d
        
        
        Gets a column of the matrix as a Vec3.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        """
        
        GetDeterminant() -> float
        
        
        Returns the determinant of the matrix.
        
        
        
        """
    @staticmethod
    def GetHandedness(*args, **kwargs):
        """
        
        GetHandedness() -> float
        
        
        Returns the sign of the determinant of the matrix, i.e.
        
        
        1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
        singular matrix.
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse(det, eps) -> Matrix3d
        
        
        Returns the inverse of the matrix, or FLT_MAX \\* SetIdentity() if the
        matrix is singular.
        
        
        (FLT_MAX is the largest value a ``float`` can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        ``\\*det`` is set to the determinant.
        
        
        Parameters
        ----------
        det : float
        
        eps : float
        
        
        """
    @staticmethod
    def GetOrthonormalized(*args, **kwargs):
        """
        
        GetOrthonormalized(issueWarning) -> Matrix3d
        
        
        Returns an orthonormalized copy of the matrix.
        
        
        Parameters
        ----------
        issueWarning : bool
        
        
        """
    @staticmethod
    def GetRow(*args, **kwargs):
        """
        
        GetRow(i) -> Vec3d
        
        
        Gets a row of the matrix as a Vec3.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetTranspose(*args, **kwargs):
        """
        
        GetTranspose() -> Matrix3d
        
        
        Returns the transpose of the matrix.
        
        
        
        """
    @staticmethod
    def IsLeftHanded(*args, **kwargs):
        """
        
        IsLeftHanded() -> bool
        
        
        Returns true if the vectors in matrix form a left-handed coordinate
        system.
        
        
        
        """
    @staticmethod
    def IsRightHanded(*args, **kwargs):
        """
        
        IsRightHanded() -> bool
        
        
        Returns true if the vectors in the matrix form a right-handed
        coordinate system.
        
        
        
        """
    @staticmethod
    def Orthonormalize(*args, **kwargs):
        """
        
        Orthonormalize(issueWarning) -> bool
        
        
        Makes the matrix orthonormal in place.
        
        
        This is an iterative method that is much more stable than the previous
        cross/cross method. If the iterative method does not converge, a
        warning is issued.
        
        Returns true if the iteration converged, false otherwise. Leaves any
        translation part of the matrix unchanged. If *issueWarning* is true,
        this method will issue a warning if the iteration does not converge,
        otherwise it will be silent.
        
        
        Parameters
        ----------
        issueWarning : bool
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(m00, m01, m02, m10, m11, m12, m20, m21, m22) -> Matrix3d
        
        
        Sets the matrix from 9 independent ``double`` values, specified in
        row-major order.
        
        
        For example, parameter *m10* specifies the value in row 1 and column
        0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m02 : float
        
        m10 : float
        
        m11 : float
        
        m12 : float
        
        m20 : float
        
        m21 : float
        
        m22 : float
        
        
        
        ----------------------------------------------------------------------
        
        Set(m) -> Matrix3d
        
        
        Sets the matrix from a 3x3 array of ``double`` values, specified in
        row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        """
    @staticmethod
    def SetColumn(*args, **kwargs):
        """
        
        SetColumn(i, v) -> None
        
        
        Sets a column of the matrix from a Vec3.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec3d
        
        
        """
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        """
        
        SetDiagonal(s) -> Matrix3d
        
        
        Sets the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        SetDiagonal(arg1) -> Matrix3d
        
        
        Sets the matrix to have diagonal ( ``v[0], v[1], v[2]`` ).
        
        
        Parameters
        ----------
        arg1 : Vec3d
        
        
        """
    @staticmethod
    def SetIdentity(*args, **kwargs):
        """
        
        SetIdentity() -> Matrix3d
        
        
        Sets the matrix to the identity matrix.
        
        
        
        """
    @staticmethod
    def SetRotate(*args, **kwargs):
        """
        
        SetRotate(rot) -> Matrix3d
        
        
        Sets the matrix to specify a rotation equivalent to *rot*.
        
        
        Parameters
        ----------
        rot : Quatd
        
        
        
        ----------------------------------------------------------------------
        
        SetRotate(rot) -> Matrix3d
        
        
        Sets the matrix to specify a rotation equivalent to *rot*.
        
        
        Parameters
        ----------
        rot : Rotation
        
        
        """
    @staticmethod
    def SetRow(*args, **kwargs):
        """
        
        SetRow(i, v) -> None
        
        
        Sets a row of the matrix from a Vec3.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec3d
        
        
        """
    @staticmethod
    def SetScale(*args, **kwargs):
        """
        
        SetScale(scaleFactors) -> Matrix3d
        
        
        Sets the matrix to specify a nonuniform scaling in x, y, and z by the
        factors in vector *scaleFactors*.
        
        
        Parameters
        ----------
        scaleFactors : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        SetScale(scaleFactor) -> Matrix3d
        
        
        Sets matrix to specify a uniform scaling by *scaleFactor*.
        
        
        Parameters
        ----------
        scaleFactor : float
        
        
        """
    @staticmethod
    def SetZero(*args, **kwargs):
        """
        
        SetZero() -> Matrix3d
        
        
        Sets the matrix to zero.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor. Leaves the matrix component values undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m00, m01, m02, m10, m11, m12, m20, m21, m22)
        
        
        Constructor.
        
        
        Initializes the matrix from 9 independent ``double`` values, specified
        in row-major order. For example, parameter *m10* specifies the value
        in row 1 and column 0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m02 : float
        
        m10 : float
        
        m11 : float
        
        m12 : float
        
        m20 : float
        
        m21 : float
        
        m22 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        Constructor.
        
        
        Initializes the matrix from a 3x3 array of ``double`` values,
        specified in row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s)
        
        
        This explicit constructor initializes the matrix to ``s`` times the
        identity matrix.
        
        
        Parameters
        ----------
        s : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to ``v[i]`` .
        
        
        Parameters
        ----------
        v : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of double. The vector
        is expected to be 3x3. If it is too big, only the first 3 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of float. The vector is
        expected to be 3x3. If it is too big, only the first 3 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rot)
        
        
        Constructor. Initialize matrix from rotation.
        
        
        Parameters
        ----------
        rot : Rotation
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rot)
        
        
        Constructor. Initialize matrix from a quaternion.
        
        
        Parameters
        ----------
        rot : Quatd
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        This explicit constructor converts a"float"matrix to a"double"matrix.
        
        
        Parameters
        ----------
        m : Matrix3f
        
        
        """
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
    """
    """
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (3, 3)
    @staticmethod
    def ExtractRotation(*args, **kwargs):
        """
        
        ExtractRotation() -> Rotation
        
        
        Returns the rotation corresponding to this matrix.
        
        
        This works well only if the matrix represents a rotation.
        
        For good results, consider calling Orthonormalize() before calling
        this method.
        
        
        
        """
    @staticmethod
    def GetColumn(*args, **kwargs):
        """
        
        GetColumn(i) -> Vec3f
        
        
        Gets a column of the matrix as a Vec3.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        """
        
        GetDeterminant() -> float
        
        
        Returns the determinant of the matrix.
        
        
        
        """
    @staticmethod
    def GetHandedness(*args, **kwargs):
        """
        
        GetHandedness() -> float
        
        
        Returns the sign of the determinant of the matrix, i.e.
        
        
        1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
        singular matrix.
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse(det, eps) -> Matrix3f
        
        
        Returns the inverse of the matrix, or FLT_MAX \\* SetIdentity() if the
        matrix is singular.
        
        
        (FLT_MAX is the largest value a ``float`` can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        ``\\*det`` is set to the determinant.
        
        
        Parameters
        ----------
        det : float
        
        eps : float
        
        
        """
    @staticmethod
    def GetOrthonormalized(*args, **kwargs):
        """
        
        GetOrthonormalized(issueWarning) -> Matrix3f
        
        
        Returns an orthonormalized copy of the matrix.
        
        
        Parameters
        ----------
        issueWarning : bool
        
        
        """
    @staticmethod
    def GetRow(*args, **kwargs):
        """
        
        GetRow(i) -> Vec3f
        
        
        Gets a row of the matrix as a Vec3.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetTranspose(*args, **kwargs):
        """
        
        GetTranspose() -> Matrix3f
        
        
        Returns the transpose of the matrix.
        
        
        
        """
    @staticmethod
    def IsLeftHanded(*args, **kwargs):
        """
        
        IsLeftHanded() -> bool
        
        
        Returns true if the vectors in matrix form a left-handed coordinate
        system.
        
        
        
        """
    @staticmethod
    def IsRightHanded(*args, **kwargs):
        """
        
        IsRightHanded() -> bool
        
        
        Returns true if the vectors in the matrix form a right-handed
        coordinate system.
        
        
        
        """
    @staticmethod
    def Orthonormalize(*args, **kwargs):
        """
        
        Orthonormalize(issueWarning) -> bool
        
        
        Makes the matrix orthonormal in place.
        
        
        This is an iterative method that is much more stable than the previous
        cross/cross method. If the iterative method does not converge, a
        warning is issued.
        
        Returns true if the iteration converged, false otherwise. Leaves any
        translation part of the matrix unchanged. If *issueWarning* is true,
        this method will issue a warning if the iteration does not converge,
        otherwise it will be silent.
        
        
        Parameters
        ----------
        issueWarning : bool
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(m00, m01, m02, m10, m11, m12, m20, m21, m22) -> Matrix3f
        
        
        Sets the matrix from 9 independent ``float`` values, specified in row-
        major order.
        
        
        For example, parameter *m10* specifies the value in row 1 and column
        0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m02 : float
        
        m10 : float
        
        m11 : float
        
        m12 : float
        
        m20 : float
        
        m21 : float
        
        m22 : float
        
        
        
        ----------------------------------------------------------------------
        
        Set(m) -> Matrix3f
        
        
        Sets the matrix from a 3x3 array of ``float`` values, specified in
        row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        """
    @staticmethod
    def SetColumn(*args, **kwargs):
        """
        
        SetColumn(i, v) -> None
        
        
        Sets a column of the matrix from a Vec3.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec3f
        
        
        """
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        """
        
        SetDiagonal(s) -> Matrix3f
        
        
        Sets the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        SetDiagonal(arg1) -> Matrix3f
        
        
        Sets the matrix to have diagonal ( ``v[0], v[1], v[2]`` ).
        
        
        Parameters
        ----------
        arg1 : Vec3f
        
        
        """
    @staticmethod
    def SetIdentity(*args, **kwargs):
        """
        
        SetIdentity() -> Matrix3f
        
        
        Sets the matrix to the identity matrix.
        
        
        
        """
    @staticmethod
    def SetRotate(*args, **kwargs):
        """
        
        SetRotate(rot) -> Matrix3f
        
        
        Sets the matrix to specify a rotation equivalent to *rot*.
        
        
        Parameters
        ----------
        rot : Quatf
        
        
        
        ----------------------------------------------------------------------
        
        SetRotate(rot) -> Matrix3f
        
        
        Sets the matrix to specify a rotation equivalent to *rot*.
        
        
        Parameters
        ----------
        rot : Rotation
        
        
        """
    @staticmethod
    def SetRow(*args, **kwargs):
        """
        
        SetRow(i, v) -> None
        
        
        Sets a row of the matrix from a Vec3.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec3f
        
        
        """
    @staticmethod
    def SetScale(*args, **kwargs):
        """
        
        SetScale(scaleFactors) -> Matrix3f
        
        
        Sets the matrix to specify a nonuniform scaling in x, y, and z by the
        factors in vector *scaleFactors*.
        
        
        Parameters
        ----------
        scaleFactors : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        SetScale(scaleFactor) -> Matrix3f
        
        
        Sets matrix to specify a uniform scaling by *scaleFactor*.
        
        
        Parameters
        ----------
        scaleFactor : float
        
        
        """
    @staticmethod
    def SetZero(*args, **kwargs):
        """
        
        SetZero() -> Matrix3f
        
        
        Sets the matrix to zero.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor. Leaves the matrix component values undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m00, m01, m02, m10, m11, m12, m20, m21, m22)
        
        
        Constructor.
        
        
        Initializes the matrix from 9 independent ``float`` values, specified
        in row-major order. For example, parameter *m10* specifies the value
        in row 1 and column 0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m02 : float
        
        m10 : float
        
        m11 : float
        
        m12 : float
        
        m20 : float
        
        m21 : float
        
        m22 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        Constructor.
        
        
        Initializes the matrix from a 3x3 array of ``float`` values, specified
        in row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s)
        
        
        This explicit constructor initializes the matrix to ``s`` times the
        identity matrix.
        
        
        Parameters
        ----------
        s : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to ``v[i]`` .
        
        
        Parameters
        ----------
        v : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of double. The vector
        is expected to be 3x3. If it is too big, only the first 3 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of float. The vector is
        expected to be 3x3. If it is too big, only the first 3 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rot)
        
        
        Constructor. Initialize matrix from rotation.
        
        
        Parameters
        ----------
        rot : Rotation
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rot)
        
        
        Constructor. Initialize matrix from a quaternion.
        
        
        Parameters
        ----------
        rot : Quatf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        This explicit constructor converts a"double"matrix to a"float"matrix.
        
        
        Parameters
        ----------
        m : Matrix3d
        
        
        """
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
    """
    """
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (4, 4)
    @staticmethod
    def ExtractRotation(*args, **kwargs):
        """
        
        ExtractRotation() -> Rotation
        
        
        Returns the rotation corresponding to this matrix.
        
        
        This works well only if the matrix represents a rotation.
        
        For good results, consider calling Orthonormalize() before calling
        this method.
        
        
        
        """
    @staticmethod
    def ExtractRotationMatrix(*args, **kwargs):
        """
        
        ExtractRotationMatrix() -> Matrix3d
        
        
        Returns the rotation corresponding to this matrix.
        
        
        This works well only if the matrix represents a rotation.
        
        For good results, consider calling Orthonormalize() before calling
        this method.
        
        
        
        """
    @staticmethod
    def ExtractRotationQuat(*args, **kwargs):
        """
        
        ExtractRotationQuat() -> Quatd
        
        
        Return the rotation corresponding to this matrix as a quaternion.
        
        
        This works well only if the matrix represents a rotation.
        
        For good results, consider calling Orthonormalize() before calling
        this method.
        
        
        
        """
    @staticmethod
    def ExtractTranslation(*args, **kwargs):
        """
        
        ExtractTranslation() -> Vec3d
        
        
        Returns the translation part of the matrix, defined as the first three
        elements of the last row.
        
        
        
        """
    @staticmethod
    def Factor(*args, **kwargs):
        """
        
        Factor(r, s, u, t, p, eps) -> bool
        
        
        Factors the matrix into 5 components:
        
        
        
           - ``*M* = r \\* s \\* -r \\* u \\* t`` where
        
           - *t* is a translation.
        
           - *u* and *r* are rotations, and *-r* is the transpose (inverse) of
             *r*. The *u* matrix may contain shear information.
        
           - *s* is a scale. Any projection information could be returned in
             matrix *p*, but currently p is never modified.
             Returns ``false`` if the matrix is singular (as determined by *eps*).
             In that case, any zero scales in *s* are clamped to *eps* to allow
             computation of *u*.
        
        
        Parameters
        ----------
        r : Matrix4d
        
        s : Vec3d
        
        u : Matrix4d
        
        t : Vec3d
        
        p : Matrix4d
        
        eps : float
        
        
        """
    @staticmethod
    def GetColumn(*args, **kwargs):
        """
        
        GetColumn(i) -> Vec4d
        
        
        Gets a column of the matrix as a Vec4.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        """
        
        GetDeterminant() -> float
        
        
        Returns the determinant of the matrix.
        
        
        
        """
    @staticmethod
    def GetDeterminant3(*args, **kwargs):
        """
        
        GetDeterminant3() -> float
        
        
        Returns the determinant of the upper 3x3 matrix.
        
        
        This method is useful when the matrix describes a linear
        transformation such as a rotation or scale because the other values in
        the 4x4 matrix are not important.
        
        
        
        """
    @staticmethod
    def GetHandedness(*args, **kwargs):
        """
        
        GetHandedness() -> float
        
        
        Returns the sign of the determinant of the upper 3x3 matrix, i.e.
        
        
        1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
        singular matrix.
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse(det, eps) -> Matrix4d
        
        
        Returns the inverse of the matrix, or FLT_MAX \\* SetIdentity() if the
        matrix is singular.
        
        
        (FLT_MAX is the largest value a ``float`` can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        ``\\*det`` is set to the determinant.
        
        
        Parameters
        ----------
        det : float
        
        eps : float
        
        
        """
    @staticmethod
    def GetOrthonormalized(*args, **kwargs):
        """
        
        GetOrthonormalized(issueWarning) -> Matrix4d
        
        
        Returns an orthonormalized copy of the matrix.
        
        
        Parameters
        ----------
        issueWarning : bool
        
        
        """
    @staticmethod
    def GetRow(*args, **kwargs):
        """
        
        GetRow(i) -> Vec4d
        
        
        Gets a row of the matrix as a Vec4.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetRow3(*args, **kwargs):
        """
        
        GetRow3(i) -> Vec3d
        
        
        Gets a row of the matrix as a Vec3.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetTranspose(*args, **kwargs):
        """
        
        GetTranspose() -> Matrix4d
        
        
        Returns the transpose of the matrix.
        
        
        
        """
    @staticmethod
    def HasOrthogonalRows3(*args, **kwargs):
        """
        
        HasOrthogonalRows3() -> bool
        
        
        Returns true, if the row vectors of the upper 3x3 matrix form an
        orthogonal basis.
        
        
        Note they do not have to be unit length for this test to return true.
        
        
        
        """
    @staticmethod
    def IsLeftHanded(*args, **kwargs):
        """
        
        IsLeftHanded() -> bool
        
        
        Returns true if the vectors in the upper 3x3 matrix form a left-handed
        coordinate system.
        
        
        
        """
    @staticmethod
    def IsRightHanded(*args, **kwargs):
        """
        
        IsRightHanded() -> bool
        
        
        Returns true if the vectors in the upper 3x3 matrix form a right-
        handed coordinate system.
        
        
        
        """
    @staticmethod
    def Orthonormalize(*args, **kwargs):
        """
        
        Orthonormalize(issueWarning) -> bool
        
        
        Makes the matrix orthonormal in place.
        
        
        This is an iterative method that is much more stable than the previous
        cross/cross method. If the iterative method does not converge, a
        warning is issued.
        
        Returns true if the iteration converged, false otherwise. Leaves any
        translation part of the matrix unchanged. If *issueWarning* is true,
        this method will issue a warning if the iteration does not converge,
        otherwise it will be silent.
        
        
        Parameters
        ----------
        issueWarning : bool
        
        
        """
    @staticmethod
    def RemoveScaleShear(*args, **kwargs):
        """
        
        RemoveScaleShear() -> Matrix4d
        
        
        Returns the matrix with any scaling or shearing removed, leaving only
        the rotation and translation.
        
        
        If the matrix cannot be decomposed, returns the original matrix.
        
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33) -> Matrix4d
        
        
        Sets the matrix from 16 independent ``double`` values, specified in
        row-major order.
        
        
        For example, parameter *m10* specifies the value in row 1 and column
        0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m02 : float
        
        m03 : float
        
        m10 : float
        
        m11 : float
        
        m12 : float
        
        m13 : float
        
        m20 : float
        
        m21 : float
        
        m22 : float
        
        m23 : float
        
        m30 : float
        
        m31 : float
        
        m32 : float
        
        m33 : float
        
        
        
        ----------------------------------------------------------------------
        
        Set(m) -> Matrix4d
        
        
        Sets the matrix from a 4x4 array of ``double`` values, specified in
        row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        """
    @staticmethod
    def SetColumn(*args, **kwargs):
        """
        
        SetColumn(i, v) -> None
        
        
        Sets a column of the matrix from a Vec4.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec4d
        
        
        """
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        """
        
        SetDiagonal(s) -> Matrix4d
        
        
        Sets the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        SetDiagonal(arg1) -> Matrix4d
        
        
        Sets the matrix to have diagonal ( ``v[0], v[1], v[2], v[3]`` ).
        
        
        Parameters
        ----------
        arg1 : Vec4d
        
        
        """
    @staticmethod
    def SetIdentity(*args, **kwargs):
        """
        
        SetIdentity() -> Matrix4d
        
        
        Sets the matrix to the identity matrix.
        
        
        
        """
    @staticmethod
    def SetLookAt(*args, **kwargs):
        """
        
        SetLookAt(eyePoint, centerPoint, upDirection) -> Matrix4d
        
        
        Sets the matrix to specify a viewing matrix from parameters similar to
        those used by ``gluLookAt(3G)`` .
        
        
        *eyePoint* represents the eye point in world space. *centerPoint*
        represents the world-space center of attention. *upDirection* is a
        vector indicating which way is up.
        
        
        Parameters
        ----------
        eyePoint : Vec3d
        
        centerPoint : Vec3d
        
        upDirection : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        SetLookAt(eyePoint, orientation) -> Matrix4d
        
        
        Sets the matrix to specify a viewing matrix from a world-space
        *eyePoint* and a world-space rotation that rigidly rotates the
        orientation from its canonical frame, which is defined to be looking
        along the ``-z`` axis with the ``+y`` axis as the up direction.
        
        
        Parameters
        ----------
        eyePoint : Vec3d
        
        orientation : Rotation
        
        
        """
    @staticmethod
    def SetRotate(*args, **kwargs):
        """
        
        SetRotate(rot) -> Matrix4d
        
        
        Sets the matrix to specify a rotation equivalent to *rot*, and clears
        the translation.
        
        
        Parameters
        ----------
        rot : Quatd
        
        
        
        ----------------------------------------------------------------------
        
        SetRotate(rot) -> Matrix4d
        
        
        Sets the matrix to specify a rotation equivalent to *rot*, and clears
        the translation.
        
        
        Parameters
        ----------
        rot : Rotation
        
        
        
        ----------------------------------------------------------------------
        
        SetRotate(mx) -> Matrix4d
        
        
        Sets the matrix to specify a rotation equivalent to *mx*, and clears
        the translation.
        
        
        Parameters
        ----------
        mx : Matrix3d
        
        
        """
    @staticmethod
    def SetRotateOnly(*args, **kwargs):
        """
        
        SetRotateOnly(rot) -> Matrix4d
        
        
        Sets the matrix to specify a rotation equivalent to *rot*, without
        clearing the translation.
        
        
        Parameters
        ----------
        rot : Quatd
        
        
        
        ----------------------------------------------------------------------
        
        SetRotateOnly(rot) -> Matrix4d
        
        
        Sets the matrix to specify a rotation equivalent to *rot*, without
        clearing the translation.
        
        
        Parameters
        ----------
        rot : Rotation
        
        
        
        ----------------------------------------------------------------------
        
        SetRotateOnly(mx) -> Matrix4d
        
        
        Sets the matrix to specify a rotation equivalent to *mx*, without
        clearing the translation.
        
        
        Parameters
        ----------
        mx : Matrix3d
        
        
        """
    @staticmethod
    def SetRow(*args, **kwargs):
        """
        
        SetRow(i, v) -> None
        
        
        Sets a row of the matrix from a Vec4.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec4d
        
        
        """
    @staticmethod
    def SetRow3(*args, **kwargs):
        """
        
        SetRow3(i, v) -> None
        
        
        Sets a row of the matrix from a Vec3.
        
        
        The fourth element of the row is ignored.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec3d
        
        
        """
    @staticmethod
    def SetScale(*args, **kwargs):
        """
        
        SetScale(scaleFactors) -> Matrix4d
        
        
        Sets the matrix to specify a nonuniform scaling in x, y, and z by the
        factors in vector *scaleFactors*.
        
        
        Parameters
        ----------
        scaleFactors : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        SetScale(scaleFactor) -> Matrix4d
        
        
        Sets matrix to specify a uniform scaling by *scaleFactor*.
        
        
        Parameters
        ----------
        scaleFactor : float
        
        
        """
    @staticmethod
    def SetTransform(*args, **kwargs):
        """
        
        SetTransform(rotate, translate) -> Matrix4d
        
        
        Sets matrix to specify a rotation by *rotate* and a translation by
        *translate*.
        
        
        Parameters
        ----------
        rotate : Rotation
        
        translate : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        SetTransform(rotmx, translate) -> Matrix4d
        
        
        Sets matrix to specify a rotation by *rotmx* and a translation by
        *translate*.
        
        
        Parameters
        ----------
        rotmx : Matrix3d
        
        translate : Vec3d
        
        
        """
    @staticmethod
    def SetTranslate(*args, **kwargs):
        """
        
        SetTranslate(trans) -> Matrix4d
        
        
        Sets matrix to specify a translation by the vector *trans*, and clears
        the rotation.
        
        
        Parameters
        ----------
        trans : Vec3d
        
        
        """
    @staticmethod
    def SetTranslateOnly(*args, **kwargs):
        """
        
        SetTranslateOnly(t) -> Matrix4d
        
        
        Sets matrix to specify a translation by the vector *trans*, without
        clearing the rotation.
        
        
        Parameters
        ----------
        t : Vec3d
        
        
        """
    @staticmethod
    def SetZero(*args, **kwargs):
        """
        
        SetZero() -> Matrix4d
        
        
        Sets the matrix to zero.
        
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(vec) -> Vec3d
        
        
        Transforms the row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a 4-component vector whose fourth component
        is 1.
        
        
        Parameters
        ----------
        vec : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        Transform(vec) -> Vec3f
        
        
        Transforms the row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a 4-component vector whose fourth component
        is 1. This is an overloaded method; it differs from the other version
        in that it returns a different value type.
        
        
        Parameters
        ----------
        vec : Vec3f
        
        
        """
    @staticmethod
    def TransformAffine(*args, **kwargs):
        """
        
        TransformAffine(vec) -> Vec3d
        
        
        Transforms the row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a 4-component vector whose fourth component
        is 1 and ignores the fourth column of the matrix (i.e. assumes it is
        (0, 0, 0, 1)).
        
        
        Parameters
        ----------
        vec : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        TransformAffine(vec) -> Vec3f
        
        
        Transforms the row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a 4-component vector whose fourth component
        is 1 and ignores the fourth column of the matrix (i.e. assumes it is
        (0, 0, 0, 1)).
        
        
        Parameters
        ----------
        vec : Vec3f
        
        
        """
    @staticmethod
    def TransformDir(*args, **kwargs):
        """
        
        TransformDir(vec) -> Vec3d
        
        
        Transforms row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a direction vector, so the translation
        information in the matrix is ignored. That is, it treats the vector as
        a 4-component vector whose fourth component is 0.
        
        
        Parameters
        ----------
        vec : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        TransformDir(vec) -> Vec3f
        
        
        Transforms row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a direction vector, so the translation
        information in the matrix is ignored. That is, it treats the vector as
        a 4-component vector whose fourth component is 0. This is an
        overloaded method; it differs from the other version in that it
        returns a different value type.
        
        
        Parameters
        ----------
        vec : Vec3f
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor. Leaves the matrix component values undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33)
        
        
        Constructor.
        
        
        Initializes the matrix from 16 independent ``double`` values,
        specified in row-major order. For example, parameter *m10* specifies
        the value in row 1 and column 0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m02 : float
        
        m03 : float
        
        m10 : float
        
        m11 : float
        
        m12 : float
        
        m13 : float
        
        m20 : float
        
        m21 : float
        
        m22 : float
        
        m23 : float
        
        m30 : float
        
        m31 : float
        
        m32 : float
        
        m33 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        Constructor.
        
        
        Initializes the matrix from a 4x4 array of ``double`` values,
        specified in row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to ``v[i]`` .
        
        
        Parameters
        ----------
        v : Vec4d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of double. The vector
        is expected to be 4x4. If it is too big, only the first 4 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of float. The vector is
        expected to be 4x4. If it is too big, only the first 4 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(r0, r1, r2, r3)
        
        
        Constructor.
        
        
        Initialize the matrix from 4 row vectors of double. Each vector is
        expected to length 4. If it is too big, only the first 4 items will be
        used. If it is too small, uninitialized elements will be filled in
        with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        r0 : list[float]
        
        r1 : list[float]
        
        r2 : list[float]
        
        r3 : list[float]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(r0, r1, r2, r3)
        
        
        Constructor.
        
        
        Initialize the matrix from 4 row vectors of float. Each vector is
        expected to length 4. If it is too big, only the first 4 items will be
        used. If it is too small, uninitialized elements will be filled in
        with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        r0 : list[float]
        
        r1 : list[float]
        
        r2 : list[float]
        
        r3 : list[float]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rotate, translate)
        
        
        Constructor.
        
        
        Initializes a transformation matrix to perform the indicated rotation
        and translation.
        
        
        Parameters
        ----------
        rotate : Rotation
        
        translate : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rotmx, translate)
        
        
        Constructor.
        
        
        Initializes a transformation matrix to perform the indicated rotation
        and translation.
        
        
        Parameters
        ----------
        rotmx : Matrix3d
        
        translate : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        This explicit constructor converts a"float"matrix to a"double"matrix.
        
        
        Parameters
        ----------
        m : Matrix4f
        
        
        """
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
    """
    """
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[tuple] = (4, 4)
    @staticmethod
    def ExtractRotation(*args, **kwargs):
        """
        
        ExtractRotation() -> Rotation
        
        
        Returns the rotation corresponding to this matrix.
        
        
        This works well only if the matrix represents a rotation.
        
        For good results, consider calling Orthonormalize() before calling
        this method.
        
        
        
        """
    @staticmethod
    def ExtractRotationMatrix(*args, **kwargs):
        """
        
        ExtractRotationMatrix() -> Matrix3f
        
        
        Returns the rotation corresponding to this matrix.
        
        
        This works well only if the matrix represents a rotation.
        
        For good results, consider calling Orthonormalize() before calling
        this method.
        
        
        
        """
    @staticmethod
    def ExtractRotationQuat(*args, **kwargs):
        """
        
        ExtractRotationQuat() -> Quatf
        
        
        Return the rotation corresponding to this matrix as a quaternion.
        
        
        This works well only if the matrix represents a rotation.
        
        For good results, consider calling Orthonormalize() before calling
        this method.
        
        
        
        """
    @staticmethod
    def ExtractTranslation(*args, **kwargs):
        """
        
        ExtractTranslation() -> Vec3f
        
        
        Returns the translation part of the matrix, defined as the first three
        elements of the last row.
        
        
        
        """
    @staticmethod
    def Factor(*args, **kwargs):
        """
        
        Factor(r, s, u, t, p, eps) -> bool
        
        
        Factors the matrix into 5 components:
        
        
        
           - ``*M* = r \\* s \\* -r \\* u \\* t`` where
        
           - *t* is a translation.
        
           - *u* and *r* are rotations, and *-r* is the transpose (inverse) of
             *r*. The *u* matrix may contain shear information.
        
           - *s* is a scale. Any projection information could be returned in
             matrix *p*, but currently p is never modified.
             Returns ``false`` if the matrix is singular (as determined by *eps*).
             In that case, any zero scales in *s* are clamped to *eps* to allow
             computation of *u*.
        
        
        Parameters
        ----------
        r : Matrix4f
        
        s : Vec3f
        
        u : Matrix4f
        
        t : Vec3f
        
        p : Matrix4f
        
        eps : float
        
        
        """
    @staticmethod
    def GetColumn(*args, **kwargs):
        """
        
        GetColumn(i) -> Vec4f
        
        
        Gets a column of the matrix as a Vec4.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDeterminant(*args, **kwargs):
        """
        
        GetDeterminant() -> float
        
        
        Returns the determinant of the matrix.
        
        
        
        """
    @staticmethod
    def GetDeterminant3(*args, **kwargs):
        """
        
        GetDeterminant3() -> float
        
        
        Returns the determinant of the upper 3x3 matrix.
        
        
        This method is useful when the matrix describes a linear
        transformation such as a rotation or scale because the other values in
        the 4x4 matrix are not important.
        
        
        
        """
    @staticmethod
    def GetHandedness(*args, **kwargs):
        """
        
        GetHandedness() -> float
        
        
        Returns the sign of the determinant of the upper 3x3 matrix, i.e.
        
        
        1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
        singular matrix.
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse(det, eps) -> Matrix4f
        
        
        Returns the inverse of the matrix, or FLT_MAX \\* SetIdentity() if the
        matrix is singular.
        
        
        (FLT_MAX is the largest value a ``float`` can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        ``\\*det`` is set to the determinant.
        
        
        Parameters
        ----------
        det : float
        
        eps : float
        
        
        """
    @staticmethod
    def GetOrthonormalized(*args, **kwargs):
        """
        
        GetOrthonormalized(issueWarning) -> Matrix4f
        
        
        Returns an orthonormalized copy of the matrix.
        
        
        Parameters
        ----------
        issueWarning : bool
        
        
        """
    @staticmethod
    def GetRow(*args, **kwargs):
        """
        
        GetRow(i) -> Vec4f
        
        
        Gets a row of the matrix as a Vec4.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetRow3(*args, **kwargs):
        """
        
        GetRow3(i) -> Vec3f
        
        
        Gets a row of the matrix as a Vec3.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetTranspose(*args, **kwargs):
        """
        
        GetTranspose() -> Matrix4f
        
        
        Returns the transpose of the matrix.
        
        
        
        """
    @staticmethod
    def HasOrthogonalRows3(*args, **kwargs):
        """
        
        HasOrthogonalRows3() -> bool
        
        
        Returns true, if the row vectors of the upper 3x3 matrix form an
        orthogonal basis.
        
        
        Note they do not have to be unit length for this test to return true.
        
        
        
        """
    @staticmethod
    def IsLeftHanded(*args, **kwargs):
        """
        
        IsLeftHanded() -> bool
        
        
        Returns true if the vectors in the upper 3x3 matrix form a left-handed
        coordinate system.
        
        
        
        """
    @staticmethod
    def IsRightHanded(*args, **kwargs):
        """
        
        IsRightHanded() -> bool
        
        
        Returns true if the vectors in the upper 3x3 matrix form a right-
        handed coordinate system.
        
        
        
        """
    @staticmethod
    def Orthonormalize(*args, **kwargs):
        """
        
        Orthonormalize(issueWarning) -> bool
        
        
        Makes the matrix orthonormal in place.
        
        
        This is an iterative method that is much more stable than the previous
        cross/cross method. If the iterative method does not converge, a
        warning is issued.
        
        Returns true if the iteration converged, false otherwise. Leaves any
        translation part of the matrix unchanged. If *issueWarning* is true,
        this method will issue a warning if the iteration does not converge,
        otherwise it will be silent.
        
        
        Parameters
        ----------
        issueWarning : bool
        
        
        """
    @staticmethod
    def RemoveScaleShear(*args, **kwargs):
        """
        
        RemoveScaleShear() -> Matrix4f
        
        
        Returns the matrix with any scaling or shearing removed, leaving only
        the rotation and translation.
        
        
        If the matrix cannot be decomposed, returns the original matrix.
        
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33) -> Matrix4f
        
        
        Sets the matrix from 16 independent ``float`` values, specified in
        row-major order.
        
        
        For example, parameter *m10* specifies the value in row1 and column 0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m02 : float
        
        m03 : float
        
        m10 : float
        
        m11 : float
        
        m12 : float
        
        m13 : float
        
        m20 : float
        
        m21 : float
        
        m22 : float
        
        m23 : float
        
        m30 : float
        
        m31 : float
        
        m32 : float
        
        m33 : float
        
        
        
        ----------------------------------------------------------------------
        
        Set(m) -> Matrix4f
        
        
        Sets the matrix from a 4x4 array of ``float`` values, specified in
        row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        """
    @staticmethod
    def SetColumn(*args, **kwargs):
        """
        
        SetColumn(i, v) -> None
        
        
        Sets a column of the matrix from a Vec4.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec4f
        
        
        """
    @staticmethod
    def SetDiagonal(*args, **kwargs):
        """
        
        SetDiagonal(s) -> Matrix4f
        
        
        Sets the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        SetDiagonal(arg1) -> Matrix4f
        
        
        Sets the matrix to have diagonal ( ``v[0], v[1], v[2], v[3]`` ).
        
        
        Parameters
        ----------
        arg1 : Vec4f
        
        
        """
    @staticmethod
    def SetIdentity(*args, **kwargs):
        """
        
        SetIdentity() -> Matrix4f
        
        
        Sets the matrix to the identity matrix.
        
        
        
        """
    @staticmethod
    def SetLookAt(*args, **kwargs):
        """
        
        SetLookAt(eyePoint, centerPoint, upDirection) -> Matrix4f
        
        
        Sets the matrix to specify a viewing matrix from parameters similar to
        those used by ``gluLookAt(3G)`` .
        
        
        *eyePoint* represents the eye point in world space. *centerPoint*
        represents the world-space center of attention. *upDirection* is a
        vector indicating which way is up.
        
        
        Parameters
        ----------
        eyePoint : Vec3f
        
        centerPoint : Vec3f
        
        upDirection : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        SetLookAt(eyePoint, orientation) -> Matrix4f
        
        
        Sets the matrix to specify a viewing matrix from a world-space
        *eyePoint* and a world-space rotation that rigidly rotates the
        orientation from its canonical frame, which is defined to be looking
        along the ``-z`` axis with the ``+y`` axis as the up direction.
        
        
        Parameters
        ----------
        eyePoint : Vec3f
        
        orientation : Rotation
        
        
        """
    @staticmethod
    def SetRotate(*args, **kwargs):
        """
        
        SetRotate(rot) -> Matrix4f
        
        
        Sets the matrix to specify a rotation equivalent to *rot*, and clears
        the translation.
        
        
        Parameters
        ----------
        rot : Quatf
        
        
        
        ----------------------------------------------------------------------
        
        SetRotate(rot) -> Matrix4f
        
        
        Sets the matrix to specify a rotation equivalent to *rot*, and clears
        the translation.
        
        
        Parameters
        ----------
        rot : Rotation
        
        
        
        ----------------------------------------------------------------------
        
        SetRotate(mx) -> Matrix4f
        
        
        Sets the matrix to specify a rotation equivalent to *mx*, and clears
        the translation.
        
        
        Parameters
        ----------
        mx : Matrix3f
        
        
        """
    @staticmethod
    def SetRotateOnly(*args, **kwargs):
        """
        
        SetRotateOnly(rot) -> Matrix4f
        
        
        Sets the matrix to specify a rotation equivalent to *rot*, without
        clearing the translation.
        
        
        Parameters
        ----------
        rot : Quatf
        
        
        
        ----------------------------------------------------------------------
        
        SetRotateOnly(rot) -> Matrix4f
        
        
        Sets the matrix to specify a rotation equivalent to *rot*, without
        clearing the translation.
        
        
        Parameters
        ----------
        rot : Rotation
        
        
        
        ----------------------------------------------------------------------
        
        SetRotateOnly(mx) -> Matrix4f
        
        
        Sets the matrix to specify a rotation equivalent to *mx*, without
        clearing the translation.
        
        
        Parameters
        ----------
        mx : Matrix3f
        
        
        """
    @staticmethod
    def SetRow(*args, **kwargs):
        """
        
        SetRow(i, v) -> None
        
        
        Sets a row of the matrix from a Vec4.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec4f
        
        
        """
    @staticmethod
    def SetRow3(*args, **kwargs):
        """
        
        SetRow3(i, v) -> None
        
        
        Sets a row of the matrix from a Vec3.
        
        
        The fourth element of the row is ignored.
        
        
        Parameters
        ----------
        i : int
        
        v : Vec3f
        
        
        """
    @staticmethod
    def SetScale(*args, **kwargs):
        """
        
        SetScale(scaleFactors) -> Matrix4f
        
        
        Sets the matrix to specify a nonuniform scaling in x, y, and z by the
        factors in vector *scaleFactors*.
        
        
        Parameters
        ----------
        scaleFactors : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        SetScale(scaleFactor) -> Matrix4f
        
        
        Sets matrix to specify a uniform scaling by *scaleFactor*.
        
        
        Parameters
        ----------
        scaleFactor : float
        
        
        """
    @staticmethod
    def SetTransform(*args, **kwargs):
        """
        
        SetTransform(rotate, translate) -> Matrix4f
        
        
        Sets matrix to specify a rotation by *rotate* and a translation by
        *translate*.
        
        
        Parameters
        ----------
        rotate : Rotation
        
        translate : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        SetTransform(rotmx, translate) -> Matrix4f
        
        
        Sets matrix to specify a rotation by *rotmx* and a translation by
        *translate*.
        
        
        Parameters
        ----------
        rotmx : Matrix3f
        
        translate : Vec3f
        
        
        """
    @staticmethod
    def SetTranslate(*args, **kwargs):
        """
        
        SetTranslate(trans) -> Matrix4f
        
        
        Sets matrix to specify a translation by the vector *trans*, and clears
        the rotation.
        
        
        Parameters
        ----------
        trans : Vec3f
        
        
        """
    @staticmethod
    def SetTranslateOnly(*args, **kwargs):
        """
        
        SetTranslateOnly(t) -> Matrix4f
        
        
        Sets matrix to specify a translation by the vector *trans*, without
        clearing the rotation.
        
        
        Parameters
        ----------
        t : Vec3f
        
        
        """
    @staticmethod
    def SetZero(*args, **kwargs):
        """
        
        SetZero() -> Matrix4f
        
        
        Sets the matrix to zero.
        
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(vec) -> Vec3d
        
        
        Transforms the row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a 4-component vector whose fourth component
        is 1.
        
        
        Parameters
        ----------
        vec : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        Transform(vec) -> Vec3f
        
        
        Transforms the row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a 4-component vector whose fourth component
        is 1. This is an overloaded method; it differs from the other version
        in that it returns a different value type.
        
        
        Parameters
        ----------
        vec : Vec3f
        
        
        """
    @staticmethod
    def TransformAffine(*args, **kwargs):
        """
        
        TransformAffine(vec) -> Vec3d
        
        
        Transforms the row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a 4-component vector whose fourth component
        is 1 and ignores the fourth column of the matrix (i.e. assumes it is
        (0, 0, 0, 1)).
        
        
        Parameters
        ----------
        vec : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        TransformAffine(vec) -> Vec3f
        
        
        Transforms the row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a 4-component vector whose fourth component
        is 1 and ignores the fourth column of the matrix (i.e. assumes it is
        (0, 0, 0, 1)).
        
        
        Parameters
        ----------
        vec : Vec3f
        
        
        """
    @staticmethod
    def TransformDir(*args, **kwargs):
        """
        
        TransformDir(vec) -> Vec3d
        
        
        Transforms row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a direction vector, so the translation
        information in the matrix is ignored. That is, it treats the vector as
        a 4-component vector whose fourth component is 0.
        
        
        Parameters
        ----------
        vec : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        TransformDir(vec) -> Vec3f
        
        
        Transforms row vector *vec* by the matrix, returning the result.
        
        
        This treats the vector as a direction vector, so the translation
        information in the matrix is ignored. That is, it treats the vector as
        a 4-component vector whose fourth component is 0. This is an
        overloaded method; it differs from the other version in that it
        returns a different value type.
        
        
        Parameters
        ----------
        vec : Vec3f
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor. Leaves the matrix component values undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33)
        
        
        Constructor.
        
        
        Initializes the matrix from 16 independent ``float`` values, specified
        in row-major order. For example, parameter *m10* specifies the value
        in row 1 and column 0.
        
        
        Parameters
        ----------
        m00 : float
        
        m01 : float
        
        m02 : float
        
        m03 : float
        
        m10 : float
        
        m11 : float
        
        m12 : float
        
        m13 : float
        
        m20 : float
        
        m21 : float
        
        m22 : float
        
        m23 : float
        
        m30 : float
        
        m31 : float
        
        m32 : float
        
        m33 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        Constructor.
        
        
        Initializes the matrix from a 4x4 array of ``float`` values, specified
        in row-major order.
        
        
        Parameters
        ----------
        m : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to *s* times the identity matrix.
        
        
        Parameters
        ----------
        s : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to ``v[i]`` .
        
        
        Parameters
        ----------
        v : Vec4f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of double. The vector
        is expected to be 4x4. If it is too big, only the first 4 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Constructor.
        
        
        Initialize the matrix from a vector of vectors of float. The vector is
        expected to be 4x4. If it is too big, only the first 4 rows and/or
        columns will be used. If it is too small, uninitialized elements will
        be filled in with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        v : list[list[float]]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(r0, r1, r2, r3)
        
        
        Constructor.
        
        
        Initialize the matrix from 4 row vectors of double. Each vector is
        expected to length 4. If it is too big, only the first 4 items will be
        used. If it is too small, uninitialized elements will be filled in
        with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        r0 : list[float]
        
        r1 : list[float]
        
        r2 : list[float]
        
        r3 : list[float]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(r0, r1, r2, r3)
        
        
        Constructor.
        
        
        Initialize the matrix from 4 row vectors of float. Each vector is
        expected to length 4. If it is too big, only the first 4 items will be
        used. If it is too small, uninitialized elements will be filled in
        with the corresponding elements from an identity matrix.
        
        
        Parameters
        ----------
        r0 : list[float]
        
        r1 : list[float]
        
        r2 : list[float]
        
        r3 : list[float]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rotate, translate)
        
        
        Constructor.
        
        
        Initializes a transformation matrix to perform the indicated rotation
        and translation.
        
        
        Parameters
        ----------
        rotate : Rotation
        
        translate : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rotmx, translate)
        
        
        Constructor.
        
        
        Initializes a transformation matrix to perform the indicated rotation
        and translation.
        
        
        Parameters
        ----------
        rotmx : Matrix3f
        
        translate : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(m)
        
        
        This explicit constructor converts a"double"matrix to a"float"matrix.
        
        
        Parameters
        ----------
        m : Matrix4d
        
        
        """
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
    """
    """
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def Add(*args, **kwargs):
        """
        
        Add(i) -> None
        
        
        Add the given interval to the multi-interval.
        
        
        Parameters
        ----------
        i : Interval
        
        
        
        ----------------------------------------------------------------------
        
        Add(s) -> None
        
        
        Add the given multi-interval to the multi-interval.
        
        
        Sets this object to the union of the two sets.
        
        
        Parameters
        ----------
        s : MultiInterval
        
        
        """
    @staticmethod
    def ArithmeticAdd(*args, **kwargs):
        """
        
        ArithmeticAdd(i) -> None
        
        
        Uses the given interval to extend the multi-interval in the interval
        arithmetic sense.
        
        
        Parameters
        ----------
        i : Interval
        
        
        """
    @staticmethod
    def Clear(*args, **kwargs):
        """
        
        Clear() -> None
        
        
        Clear the multi-interval.
        
        
        
        """
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        
        Returns true if x is inside the multi-interval.
        
        Returns true if x is inside the multi-interval.
        
        Returns true if x is inside the multi-interval.
        """
    @staticmethod
    def GetBounds(*args, **kwargs):
        """
        
        GetBounds() -> Interval
        
        
        Returns an interval bounding the entire multi-interval.
        
        
        Returns an empty interval if the multi-interval is empty.
        
        
        
        """
    @staticmethod
    def GetComplement(*args, **kwargs):
        """
        
        GetComplement() -> MultiInterval
        
        
        Return the complement of this set.
        
        
        
        """
    @staticmethod
    def GetFullInterval(*args, **kwargs):
        """
        
        **classmethod** GetFullInterval() -> MultiInterval
        
        
        Returns the full interval (-inf, inf).
        
        
        
        """
    @staticmethod
    def GetSize(*args, **kwargs):
        """
        
        GetSize() -> int
        
        
        Returns the number of intervals in the set.
        
        
        
        """
    @staticmethod
    def Intersect(*args, **kwargs):
        """
        
        Intersect(i) -> None
        
        
        Parameters
        ----------
        i : Interval
        
        
        
        ----------------------------------------------------------------------
        
        Intersect(s) -> None
        
        
        Parameters
        ----------
        s : MultiInterval
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Returns true if the multi-interval is empty.
        
        
        
        """
    @staticmethod
    def Remove(*args, **kwargs):
        """
        
        Remove(i) -> None
        
        
        Remove the given interval from this multi-interval.
        
        
        Parameters
        ----------
        i : Interval
        
        
        
        ----------------------------------------------------------------------
        
        Remove(s) -> None
        
        
        Remove the given multi-interval from this multi-interval.
        
        
        Parameters
        ----------
        s : MultiInterval
        
        
        """
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
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(i)
        
        
        Constructs an multi-interval with the single given interval.
        
        
        Parameters
        ----------
        i : Interval
        
        
        
        ----------------------------------------------------------------------
        
        __init__(intervals)
        
        
        Constructs an multi-interval containing the given input intervals.
        
        
        Parameters
        ----------
        intervals : list[Interval]
        
        
        """
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
    """
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def GetDistance(*args, **kwargs):
        """
        
        GetDistance(p) -> float
        
        
        Returns the distance of point ``from`` the plane.
        
        
        This distance will be positive if the point is on the side of the
        plane containing the normal.
        
        
        Parameters
        ----------
        p : Vec3d
        
        
        """
    @staticmethod
    def GetDistanceFromOrigin(*args, **kwargs):
        """
        
        GetDistanceFromOrigin() -> float
        
        
        Returns the distance of the plane from the origin.
        
        
        
        """
    @staticmethod
    def GetEquation(*args, **kwargs):
        """
        
        GetEquation() -> Vec4d
        
        
        Give the coefficients of the equation of the plane.
        
        
        Suitable to OpenGL calls to set the clipping plane.
        
        
        
        """
    @staticmethod
    def GetNormal(*args, **kwargs):
        """
        
        GetNormal() -> Vec3d
        
        
        Returns the unit-length normal vector of the plane.
        
        
        
        """
    @staticmethod
    def IntersectsPositiveHalfSpace(*args, **kwargs):
        """
        
        IntersectsPositiveHalfSpace(box) -> bool
        
        
        Returns ``true`` if the given aligned bounding box is at least
        partially on the positive side (the one the normal points into) of the
        plane.
        
        
        Parameters
        ----------
        box : Range3d
        
        
        
        ----------------------------------------------------------------------
        
        IntersectsPositiveHalfSpace(pt) -> bool
        
        
        Returns true if the given point is on the plane or within its positive
        half space.
        
        
        Parameters
        ----------
        pt : Vec3d
        
        
        """
    @staticmethod
    def Project(*args, **kwargs):
        """
        
        Project(p) -> Vec3d
        
        
        Return the projection of ``p`` onto the plane.
        
        
        Parameters
        ----------
        p : Vec3d
        
        
        """
    @staticmethod
    def Reorient(*args, **kwargs):
        """
        
        Reorient(p) -> None
        
        
        Flip the plane normal (if necessary) so that ``p`` is in the positive
        halfspace.
        
        
        Parameters
        ----------
        p : Vec3d
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(normal, distanceToOrigin) -> None
        
        
        Sets this to the plane perpendicular to ``normal`` and at ``distance``
        units from the origin.
        
        
        The passed-in normal is normalized to unit length first.
        
        
        Parameters
        ----------
        normal : Vec3d
        
        distanceToOrigin : float
        
        
        
        ----------------------------------------------------------------------
        
        Set(normal, point) -> None
        
        
        This constructor sets this to the plane perpendicular to ``normal``
        and that passes through ``point`` .
        
        
        The passed-in normal is normalized to unit length first.
        
        
        Parameters
        ----------
        normal : Vec3d
        
        point : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        Set(p0, p1, p2) -> None
        
        
        This constructor sets this to the plane that contains the three given
        points.
        
        
        The normal is constructed from the cross product of ( ``p1`` - ``p0``
        ) ( ``p2`` - ``p0`` ). Results are undefined if the points are
        collinear.
        
        
        Parameters
        ----------
        p0 : Vec3d
        
        p1 : Vec3d
        
        p2 : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        Set(eqn) -> None
        
        
        This method sets this to the plane given by the equation ``eqn`` [0]
        \\* x + ``eqn`` [1] \\* y + ``eqn`` [2] \\* z + ``eqn`` [3] = 0.
        
        
        Parameters
        ----------
        eqn : Vec4d
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(matrix) -> Plane
        
        
        Transforms the plane by the given matrix.
        
        
        Parameters
        ----------
        matrix : Matrix4d
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        The default constructor leaves the plane parameters undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(normal, distanceToOrigin)
        
        
        This constructor sets this to the plane perpendicular to ``normal``
        and at ``distance`` units from the origin.
        
        
        The passed-in normal is normalized to unit length first.
        
        
        Parameters
        ----------
        normal : Vec3d
        
        distanceToOrigin : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(normal, point)
        
        
        This constructor sets this to the plane perpendicular to ``normal``
        and that passes through ``point`` .
        
        
        The passed-in normal is normalized to unit length first.
        
        
        Parameters
        ----------
        normal : Vec3d
        
        point : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p0, p1, p2)
        
        
        This constructor sets this to the plane that contains the three given
        points.
        
        
        The normal is constructed from the cross product of ( ``p1`` - ``p0``
        ) ( ``p2`` - ``p0`` ). Results are undefined if the points are
        collinear.
        
        
        Parameters
        ----------
        p0 : Vec3d
        
        p1 : Vec3d
        
        p2 : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(eqn)
        
        
        This constructor creates a plane given by the equation ``eqn`` [0] \\*
        x + ``eqn`` [1] \\* y + ``eqn`` [2] \\* z + ``eqn`` [3] = 0.
        
        
        Parameters
        ----------
        eqn : Vec4d
        
        
        """
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
    """
    """
    @staticmethod
    def GetConjugate(*args, **kwargs):
        """
        
        GetConjugate() -> Quatd
        
        
        Return this quaternion's conjugate, which is the quaternion with the
        same real coefficient and negated imaginary coefficients.
        
        
        
        """
    @staticmethod
    def GetIdentity(*args, **kwargs):
        """
        
        **classmethod** GetIdentity() -> Quatd
        
        
        Return the identity quaternion, with real coefficient 1 and an
        imaginary coefficients all zero.
        
        
        
        """
    @staticmethod
    def GetImaginary(*args, **kwargs):
        """
        
        GetImaginary() -> Vec3d
        
        
        Return the imaginary coefficient.
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse() -> Quatd
        
        
        Return this quaternion's inverse, or reciprocal.
        
        
        This is the quaternion's conjugate divided by it's squared length.
        
        
        
        """
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> float
        
        
        Return geometric length of this quaternion.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Quatd
        
        
        length of this quaternion is smaller than ``eps`` , return the
        identity quaternion.
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def GetReal(*args, **kwargs):
        """
        
        GetReal() -> float
        
        
        Return the real coefficient.
        
        
        
        """
    @staticmethod
    def GetZero(*args, **kwargs):
        """
        
        **classmethod** GetZero() -> Quatd
        
        
        Return the zero quaternion, with real coefficient 0 and an imaginary
        coefficients all zero.
        
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> float
        
        
        Normalizes this quaternion in place to unit length, returning the
        length before normalization.
        
        
        If the length of this quaternion is smaller than ``eps`` , this sets
        the quaternion to identity.
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def SetImaginary(*args, **kwargs):
        """
        
        SetImaginary(imaginary) -> None
        
        
        Set the imaginary coefficients.
        
        
        Parameters
        ----------
        imaginary : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        SetImaginary(i, j, k) -> None
        
        
        Set the imaginary coefficients.
        
        
        Parameters
        ----------
        i : float
        
        j : float
        
        k : float
        
        
        """
    @staticmethod
    def SetReal(*args, **kwargs):
        """
        
        SetReal(real) -> None
        
        
        Set the real coefficient.
        
        
        Parameters
        ----------
        real : float
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(point) -> Vec3d
        
        
        Transform the GfVec3d point.
        
        
        If the quaternion is normalized, the transformation is a rotation.
        Given a GfQuatd q, q.Transform(point) is equivalent to: (q \\*
        GfQuatd(0, point) \\* q.GetInverse()).GetImaginary()
        
        but is more efficient.
        
        
        Parameters
        ----------
        point : Vec3d
        
        
        """
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
        """
        
        __init__()
        
        
        Default constructor leaves the quaternion undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(realVal)
        
        
        Initialize the real coefficient to ``realVal`` and the imaginary
        coefficients to zero.
        
        
        Since quaternions typically must be normalized, reasonable values for
        ``realVal`` are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        
        
        Parameters
        ----------
        realVal : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real, i, j, k)
        
        
        Initialize the real and imaginary coefficients.
        
        
        Parameters
        ----------
        real : float
        
        i : float
        
        j : float
        
        k : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real, imaginary)
        
        
        Initialize the real and imaginary coefficients.
        
        
        Parameters
        ----------
        real : float
        
        imaginary : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfQuatf.
        
        
        Parameters
        ----------
        other : Quatf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfQuath.
        
        
        Parameters
        ----------
        other : Quath
        
        
        """
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
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def GetIdentity(*args, **kwargs):
        """
        
        **classmethod** GetIdentity() -> Quaternion
        
        
        Returns the identity quaternion, which has a real part of 1 and an
        imaginary part of (0,0,0).
        
        
        
        """
    @staticmethod
    def GetImaginary(*args, **kwargs):
        """
        
        GetImaginary() -> Vec3d
        
        
        Returns the imaginary part of the quaternion.
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse() -> Quaternion
        
        
        Returns the inverse of this quaternion.
        
        
        
        """
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> float
        
        
        Returns geometric length of this quaternion.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Quaternion
        
        
        Returns a normalized (unit-length) version of this quaternion.
        
        
        direction as this. If the length of this quaternion is smaller than
        ``eps`` , this returns the identity quaternion.
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def GetReal(*args, **kwargs):
        """
        
        GetReal() -> float
        
        
        Returns the real part of the quaternion.
        
        
        
        """
    @staticmethod
    def GetZero(*args, **kwargs):
        """
        
        **classmethod** GetZero() -> Quaternion
        
        
        Returns the zero quaternion, which has a real part of 0 and an
        imaginary part of (0,0,0).
        
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> float
        
        
        Normalizes this quaternion in place to unit length, returning the
        length before normalization.
        
        
        If the length of this quaternion is smaller than ``eps`` , this sets
        the quaternion to identity.
        
        
        Parameters
        ----------
        eps : float
        
        
        """
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
        """
        
        __init__()
        
        
        The default constructor leaves the quaternion undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(realVal)
        
        
        This constructor initializes the real part to the argument and the
        imaginary parts to zero.
        
        
        Since quaternions typically need to be normalized, the only reasonable
        values for ``realVal`` are -1, 0, or 1. Other values are legal but are
        likely to be meaningless.
        
        
        Parameters
        ----------
        realVal : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real, imaginary)
        
        
        This constructor initializes the real and imaginary parts.
        
        
        Parameters
        ----------
        real : float
        
        imaginary : Vec3d
        
        
        """
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
        """
        type : None
        
        
        Sets the imaginary part of the quaternion.
        """
    @imaginary.setter
    def imaginary(*args, **kwargs):
        ...
    @property
    def real(*args, **kwargs):
        """
        type : None
        
        
        Sets the real part of the quaternion.
        """
    @real.setter
    def real(*args, **kwargs):
        ...
class Quatf(Boost.Python.instance):
    """
    """
    @staticmethod
    def GetConjugate(*args, **kwargs):
        """
        
        GetConjugate() -> Quatf
        
        
        Return this quaternion's conjugate, which is the quaternion with the
        same real coefficient and negated imaginary coefficients.
        
        
        
        """
    @staticmethod
    def GetIdentity(*args, **kwargs):
        """
        
        **classmethod** GetIdentity() -> Quatf
        
        
        Return the identity quaternion, with real coefficient 1 and an
        imaginary coefficients all zero.
        
        
        
        """
    @staticmethod
    def GetImaginary(*args, **kwargs):
        """
        
        GetImaginary() -> Vec3f
        
        
        Return the imaginary coefficient.
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse() -> Quatf
        
        
        Return this quaternion's inverse, or reciprocal.
        
        
        This is the quaternion's conjugate divided by it's squared length.
        
        
        
        """
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> float
        
        
        Return geometric length of this quaternion.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Quatf
        
        
        length of this quaternion is smaller than ``eps`` , return the
        identity quaternion.
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def GetReal(*args, **kwargs):
        """
        
        GetReal() -> float
        
        
        Return the real coefficient.
        
        
        
        """
    @staticmethod
    def GetZero(*args, **kwargs):
        """
        
        **classmethod** GetZero() -> Quatf
        
        
        Return the zero quaternion, with real coefficient 0 and an imaginary
        coefficients all zero.
        
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> float
        
        
        Normalizes this quaternion in place to unit length, returning the
        length before normalization.
        
        
        If the length of this quaternion is smaller than ``eps`` , this sets
        the quaternion to identity.
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def SetImaginary(*args, **kwargs):
        """
        
        SetImaginary(imaginary) -> None
        
        
        Set the imaginary coefficients.
        
        
        Parameters
        ----------
        imaginary : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        SetImaginary(i, j, k) -> None
        
        
        Set the imaginary coefficients.
        
        
        Parameters
        ----------
        i : float
        
        j : float
        
        k : float
        
        
        """
    @staticmethod
    def SetReal(*args, **kwargs):
        """
        
        SetReal(real) -> None
        
        
        Set the real coefficient.
        
        
        Parameters
        ----------
        real : float
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(point) -> Vec3f
        
        
        Transform the GfVec3f point.
        
        
        If the quaternion is normalized, the transformation is a rotation.
        Given a GfQuatf q, q.Transform(point) is equivalent to: (q \\*
        GfQuatf(0, point) \\* q.GetInverse()).GetImaginary()
        
        but is more efficient.
        
        
        Parameters
        ----------
        point : Vec3f
        
        
        """
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
        """
        
        __init__()
        
        
        Default constructor leaves the quaternion undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(realVal)
        
        
        Initialize the real coefficient to ``realVal`` and the imaginary
        coefficients to zero.
        
        
        Since quaternions typically must be normalized, reasonable values for
        ``realVal`` are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        
        
        Parameters
        ----------
        realVal : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real, i, j, k)
        
        
        Initialize the real and imaginary coefficients.
        
        
        Parameters
        ----------
        real : float
        
        i : float
        
        j : float
        
        k : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real, imaginary)
        
        
        Initialize the real and imaginary coefficients.
        
        
        Parameters
        ----------
        real : float
        
        imaginary : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfQuatd.
        
        
        Parameters
        ----------
        other : Quatd
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfQuath.
        
        
        Parameters
        ----------
        other : Quath
        
        
        """
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
    """
    """
    @staticmethod
    def GetConjugate(*args, **kwargs):
        """
        
        GetConjugate() -> Quath
        
        
        Return this quaternion's conjugate, which is the quaternion with the
        same real coefficient and negated imaginary coefficients.
        
        
        
        """
    @staticmethod
    def GetIdentity(*args, **kwargs):
        """
        
        **classmethod** GetIdentity() -> Quath
        
        
        Return the identity quaternion, with real coefficient 1 and an
        imaginary coefficients all zero.
        
        
        
        """
    @staticmethod
    def GetImaginary(*args, **kwargs):
        """
        
        GetImaginary() -> Vec3h
        
        
        Return the imaginary coefficient.
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse() -> Quath
        
        
        Return this quaternion's inverse, or reciprocal.
        
        
        This is the quaternion's conjugate divided by it's squared length.
        
        
        
        """
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> GfHalf
        
        
        Return geometric length of this quaternion.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Quath
        
        
        length of this quaternion is smaller than ``eps`` , return the
        identity quaternion.
        
        
        Parameters
        ----------
        eps : GfHalf
        
        
        """
    @staticmethod
    def GetReal(*args, **kwargs):
        """
        
        GetReal() -> GfHalf
        
        
        Return the real coefficient.
        
        
        
        """
    @staticmethod
    def GetZero(*args, **kwargs):
        """
        
        **classmethod** GetZero() -> Quath
        
        
        Return the zero quaternion, with real coefficient 0 and an imaginary
        coefficients all zero.
        
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> GfHalf
        
        
        Normalizes this quaternion in place to unit length, returning the
        length before normalization.
        
        
        If the length of this quaternion is smaller than ``eps`` , this sets
        the quaternion to identity.
        
        
        Parameters
        ----------
        eps : GfHalf
        
        
        """
    @staticmethod
    def SetImaginary(*args, **kwargs):
        """
        
        SetImaginary(imaginary) -> None
        
        
        Set the imaginary coefficients.
        
        
        Parameters
        ----------
        imaginary : Vec3h
        
        
        
        ----------------------------------------------------------------------
        
        SetImaginary(i, j, k) -> None
        
        
        Set the imaginary coefficients.
        
        
        Parameters
        ----------
        i : GfHalf
        
        j : GfHalf
        
        k : GfHalf
        
        
        """
    @staticmethod
    def SetReal(*args, **kwargs):
        """
        
        SetReal(real) -> None
        
        
        Set the real coefficient.
        
        
        Parameters
        ----------
        real : GfHalf
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(point) -> Vec3h
        
        
        Transform the GfVec3h point.
        
        
        If the quaternion is normalized, the transformation is a rotation.
        Given a GfQuath q, q.Transform(point) is equivalent to: (q \\*
        GfQuath(0, point) \\* q.GetInverse()).GetImaginary()
        
        but is more efficient.
        
        
        Parameters
        ----------
        point : Vec3h
        
        
        """
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
        """
        
        __init__()
        
        
        Default constructor leaves the quaternion undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(realVal)
        
        
        Initialize the real coefficient to ``realVal`` and the imaginary
        coefficients to zero.
        
        
        Since quaternions typically must be normalized, reasonable values for
        ``realVal`` are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        
        
        Parameters
        ----------
        realVal : GfHalf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real, i, j, k)
        
        
        Initialize the real and imaginary coefficients.
        
        
        Parameters
        ----------
        real : GfHalf
        
        i : GfHalf
        
        j : GfHalf
        
        k : GfHalf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(real, imaginary)
        
        
        Initialize the real and imaginary coefficients.
        
        
        Parameters
        ----------
        real : GfHalf
        
        imaginary : Vec3h
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfQuatd.
        
        
        Parameters
        ----------
        other : Quatd
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfQuatf.
        
        
        Parameters
        ----------
        other : Quatf
        
        
        """
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
    """
    """
    __instance_size__: typing.ClassVar[int] = 32
    dimension: typing.ClassVar[int] = 1
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        Contains(point) -> bool
        
        
        Returns true if the ``point`` is located inside the range.
        
        
        As with all operations of this type, the range is assumed to include
        its extrema.
        
        
        Parameters
        ----------
        point : float
        
        
        
        ----------------------------------------------------------------------
        
        Contains(range) -> bool
        
        
        Returns true if the ``range`` is located entirely inside the range.
        
        
        As with all operations of this type, the ranges are assumed to include
        their extrema.
        
        
        Parameters
        ----------
        range : Range1d
        
        
        """
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        """
        
        GetDistanceSquared(p) -> float
        
        
        Compute the squared distance from a point to the range.
        
        
        Parameters
        ----------
        p : float
        
        
        """
    @staticmethod
    def GetIntersection(*args, **kwargs):
        """
        
        **classmethod** GetIntersection(a, b) -> Range1d
        
        
        Returns a ``GfRange1d`` that describes the intersection of ``a`` and
        ``b`` .
        
        
        Parameters
        ----------
        a : Range1d
        
        b : Range1d
        
        
        """
    @staticmethod
    def GetMax(*args, **kwargs):
        """
        
        GetMax() -> float
        
        
        Returns the maximum value of the range.
        
        
        
        """
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        """
        
        GetMidpoint() -> float
        
        
        Returns the midpoint of the range, that is, 0.5\\*(min+max).
        
        
        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        
        
        
        """
    @staticmethod
    def GetMin(*args, **kwargs):
        """
        
        GetMin() -> float
        
        
        Returns the minimum value of the range.
        
        
        
        """
    @staticmethod
    def GetSize(*args, **kwargs):
        """
        
        GetSize() -> float
        
        
        Returns the size of the range.
        
        
        
        """
    @staticmethod
    def GetUnion(*args, **kwargs):
        """
        
        **classmethod** GetUnion(a, b) -> Range1d
        
        
        Returns the smallest ``GfRange1d`` which contains both ``a`` and ``b``
        .
        
        
        Parameters
        ----------
        a : Range1d
        
        b : Range1d
        
        
        """
    @staticmethod
    def IntersectWith(*args, **kwargs):
        """
        
        IntersectWith(b) -> Range1d
        
        
        Modifies this range to hold its intersection with ``b`` and returns
        the result.
        
        
        Parameters
        ----------
        b : Range1d
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Returns whether the range is empty (max<min).
        
        
        
        """
    @staticmethod
    def SetEmpty(*args, **kwargs):
        """
        
        SetEmpty() -> None
        
        
        Sets the range to an empty interval.
        
        
        
        """
    @staticmethod
    def SetMax(*args, **kwargs):
        """
        
        SetMax(max) -> None
        
        
        Sets the maximum value of the range.
        
        
        Parameters
        ----------
        max : float
        
        
        """
    @staticmethod
    def SetMin(*args, **kwargs):
        """
        
        SetMin(min) -> None
        
        
        Sets the minimum value of the range.
        
        
        Parameters
        ----------
        min : float
        
        
        """
    @staticmethod
    def UnionWith(*args, **kwargs):
        """
        
        UnionWith(b) -> Range1d
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : Range1d
        
        
        
        ----------------------------------------------------------------------
        
        UnionWith(b) -> Range1d
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : float
        
        
        """
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
        """
        
        __init__()
        
        
        The default constructor creates an empty range.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(min, max)
        
        
        This constructor initializes the minimum and maximum points.
        
        
        Parameters
        ----------
        min : float
        
        max : float
        
        
        """
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
    """
    """
    __instance_size__: typing.ClassVar[int] = 24
    dimension: typing.ClassVar[int] = 1
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        Contains(point) -> bool
        
        
        Returns true if the ``point`` is located inside the range.
        
        
        As with all operations of this type, the range is assumed to include
        its extrema.
        
        
        Parameters
        ----------
        point : float
        
        
        
        ----------------------------------------------------------------------
        
        Contains(range) -> bool
        
        
        Returns true if the ``range`` is located entirely inside the range.
        
        
        As with all operations of this type, the ranges are assumed to include
        their extrema.
        
        
        Parameters
        ----------
        range : Range1f
        
        
        """
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        """
        
        GetDistanceSquared(p) -> float
        
        
        Compute the squared distance from a point to the range.
        
        
        Parameters
        ----------
        p : float
        
        
        """
    @staticmethod
    def GetIntersection(*args, **kwargs):
        """
        
        **classmethod** GetIntersection(a, b) -> Range1f
        
        
        Returns a ``GfRange1f`` that describes the intersection of ``a`` and
        ``b`` .
        
        
        Parameters
        ----------
        a : Range1f
        
        b : Range1f
        
        
        """
    @staticmethod
    def GetMax(*args, **kwargs):
        """
        
        GetMax() -> float
        
        
        Returns the maximum value of the range.
        
        
        
        """
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        """
        
        GetMidpoint() -> float
        
        
        Returns the midpoint of the range, that is, 0.5\\*(min+max).
        
        
        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        
        
        
        """
    @staticmethod
    def GetMin(*args, **kwargs):
        """
        
        GetMin() -> float
        
        
        Returns the minimum value of the range.
        
        
        
        """
    @staticmethod
    def GetSize(*args, **kwargs):
        """
        
        GetSize() -> float
        
        
        Returns the size of the range.
        
        
        
        """
    @staticmethod
    def GetUnion(*args, **kwargs):
        """
        
        **classmethod** GetUnion(a, b) -> Range1f
        
        
        Returns the smallest ``GfRange1f`` which contains both ``a`` and ``b``
        .
        
        
        Parameters
        ----------
        a : Range1f
        
        b : Range1f
        
        
        """
    @staticmethod
    def IntersectWith(*args, **kwargs):
        """
        
        IntersectWith(b) -> Range1f
        
        
        Modifies this range to hold its intersection with ``b`` and returns
        the result.
        
        
        Parameters
        ----------
        b : Range1f
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Returns whether the range is empty (max<min).
        
        
        
        """
    @staticmethod
    def SetEmpty(*args, **kwargs):
        """
        
        SetEmpty() -> None
        
        
        Sets the range to an empty interval.
        
        
        
        """
    @staticmethod
    def SetMax(*args, **kwargs):
        """
        
        SetMax(max) -> None
        
        
        Sets the maximum value of the range.
        
        
        Parameters
        ----------
        max : float
        
        
        """
    @staticmethod
    def SetMin(*args, **kwargs):
        """
        
        SetMin(min) -> None
        
        
        Sets the minimum value of the range.
        
        
        Parameters
        ----------
        min : float
        
        
        """
    @staticmethod
    def UnionWith(*args, **kwargs):
        """
        
        UnionWith(b) -> Range1f
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : Range1f
        
        
        
        ----------------------------------------------------------------------
        
        UnionWith(b) -> Range1f
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : float
        
        
        """
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
        """
        
        __init__()
        
        
        The default constructor creates an empty range.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(min, max)
        
        
        This constructor initializes the minimum and maximum points.
        
        
        Parameters
        ----------
        min : float
        
        max : float
        
        
        """
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
    """
    """
    __instance_size__: typing.ClassVar[int] = 48
    dimension: typing.ClassVar[int] = 2
    unitSquare: typing.ClassVar[Range2d]  # value = Gf.Range2d(Gf.Vec2d(0.0, 0.0), Gf.Vec2d(1.0, 1.0))
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        Contains(point) -> bool
        
        
        Returns true if the ``point`` is located inside the range.
        
        
        As with all operations of this type, the range is assumed to include
        its extrema.
        
        
        Parameters
        ----------
        point : Vec2d
        
        
        
        ----------------------------------------------------------------------
        
        Contains(range) -> bool
        
        
        Returns true if the ``range`` is located entirely inside the range.
        
        
        As with all operations of this type, the ranges are assumed to include
        their extrema.
        
        
        Parameters
        ----------
        range : Range2d
        
        
        """
    @staticmethod
    def GetCorner(*args, **kwargs):
        """
        
        GetCorner(i) -> Vec2d
        
        
        Returns the ith corner of the range, in the following order: SW, SE,
        NW, NE.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        """
        
        GetDistanceSquared(p) -> float
        
        
        Compute the squared distance from a point to the range.
        
        
        Parameters
        ----------
        p : Vec2d
        
        
        """
    @staticmethod
    def GetIntersection(*args, **kwargs):
        """
        
        **classmethod** GetIntersection(a, b) -> Range2d
        
        
        Returns a ``GfRange2d`` that describes the intersection of ``a`` and
        ``b`` .
        
        
        Parameters
        ----------
        a : Range2d
        
        b : Range2d
        
        
        """
    @staticmethod
    def GetMax(*args, **kwargs):
        """
        
        GetMax() -> Vec2d
        
        
        Returns the maximum value of the range.
        
        
        
        """
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        """
        
        GetMidpoint() -> Vec2d
        
        
        Returns the midpoint of the range, that is, 0.5\\*(min+max).
        
        
        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        
        
        
        """
    @staticmethod
    def GetMin(*args, **kwargs):
        """
        
        GetMin() -> Vec2d
        
        
        Returns the minimum value of the range.
        
        
        
        """
    @staticmethod
    def GetQuadrant(*args, **kwargs):
        """
        
        GetQuadrant(i) -> Range2d
        
        
        Returns the ith quadrant of the range, in the following order: SW, SE,
        NW, NE.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetSize(*args, **kwargs):
        """
        
        GetSize() -> Vec2d
        
        
        Returns the size of the range.
        
        
        
        """
    @staticmethod
    def GetUnion(*args, **kwargs):
        """
        
        **classmethod** GetUnion(a, b) -> Range2d
        
        
        Returns the smallest ``GfRange2d`` which contains both ``a`` and ``b``
        .
        
        
        Parameters
        ----------
        a : Range2d
        
        b : Range2d
        
        
        """
    @staticmethod
    def IntersectWith(*args, **kwargs):
        """
        
        IntersectWith(b) -> Range2d
        
        
        Modifies this range to hold its intersection with ``b`` and returns
        the result.
        
        
        Parameters
        ----------
        b : Range2d
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Returns whether the range is empty (max<min).
        
        
        
        """
    @staticmethod
    def SetEmpty(*args, **kwargs):
        """
        
        SetEmpty() -> None
        
        
        Sets the range to an empty interval.
        
        
        
        """
    @staticmethod
    def SetMax(*args, **kwargs):
        """
        
        SetMax(max) -> None
        
        
        Sets the maximum value of the range.
        
        
        Parameters
        ----------
        max : Vec2d
        
        
        """
    @staticmethod
    def SetMin(*args, **kwargs):
        """
        
        SetMin(min) -> None
        
        
        Sets the minimum value of the range.
        
        
        Parameters
        ----------
        min : Vec2d
        
        
        """
    @staticmethod
    def UnionWith(*args, **kwargs):
        """
        
        UnionWith(b) -> Range2d
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : Range2d
        
        
        
        ----------------------------------------------------------------------
        
        UnionWith(b) -> Range2d
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : Vec2d
        
        
        """
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
        """
        
        __init__()
        
        
        The default constructor creates an empty range.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(min, max)
        
        
        This constructor initializes the minimum and maximum points.
        
        
        Parameters
        ----------
        min : Vec2d
        
        max : Vec2d
        
        
        """
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
    """
    """
    __instance_size__: typing.ClassVar[int] = 32
    dimension: typing.ClassVar[int] = 2
    unitSquare: typing.ClassVar[Range2f]  # value = Gf.Range2f(Gf.Vec2f(0.0, 0.0), Gf.Vec2f(1.0, 1.0))
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        Contains(point) -> bool
        
        
        Returns true if the ``point`` is located inside the range.
        
        
        As with all operations of this type, the range is assumed to include
        its extrema.
        
        
        Parameters
        ----------
        point : Vec2f
        
        
        
        ----------------------------------------------------------------------
        
        Contains(range) -> bool
        
        
        Returns true if the ``range`` is located entirely inside the range.
        
        
        As with all operations of this type, the ranges are assumed to include
        their extrema.
        
        
        Parameters
        ----------
        range : Range2f
        
        
        """
    @staticmethod
    def GetCorner(*args, **kwargs):
        """
        
        GetCorner(i) -> Vec2f
        
        
        Returns the ith corner of the range, in the following order: SW, SE,
        NW, NE.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        """
        
        GetDistanceSquared(p) -> float
        
        
        Compute the squared distance from a point to the range.
        
        
        Parameters
        ----------
        p : Vec2f
        
        
        """
    @staticmethod
    def GetIntersection(*args, **kwargs):
        """
        
        **classmethod** GetIntersection(a, b) -> Range2f
        
        
        Returns a ``GfRange2f`` that describes the intersection of ``a`` and
        ``b`` .
        
        
        Parameters
        ----------
        a : Range2f
        
        b : Range2f
        
        
        """
    @staticmethod
    def GetMax(*args, **kwargs):
        """
        
        GetMax() -> Vec2f
        
        
        Returns the maximum value of the range.
        
        
        
        """
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        """
        
        GetMidpoint() -> Vec2f
        
        
        Returns the midpoint of the range, that is, 0.5\\*(min+max).
        
        
        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        
        
        
        """
    @staticmethod
    def GetMin(*args, **kwargs):
        """
        
        GetMin() -> Vec2f
        
        
        Returns the minimum value of the range.
        
        
        
        """
    @staticmethod
    def GetQuadrant(*args, **kwargs):
        """
        
        GetQuadrant(i) -> Range2f
        
        
        Returns the ith quadrant of the range, in the following order: SW, SE,
        NW, NE.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetSize(*args, **kwargs):
        """
        
        GetSize() -> Vec2f
        
        
        Returns the size of the range.
        
        
        
        """
    @staticmethod
    def GetUnion(*args, **kwargs):
        """
        
        **classmethod** GetUnion(a, b) -> Range2f
        
        
        Returns the smallest ``GfRange2f`` which contains both ``a`` and ``b``
        .
        
        
        Parameters
        ----------
        a : Range2f
        
        b : Range2f
        
        
        """
    @staticmethod
    def IntersectWith(*args, **kwargs):
        """
        
        IntersectWith(b) -> Range2f
        
        
        Modifies this range to hold its intersection with ``b`` and returns
        the result.
        
        
        Parameters
        ----------
        b : Range2f
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Returns whether the range is empty (max<min).
        
        
        
        """
    @staticmethod
    def SetEmpty(*args, **kwargs):
        """
        
        SetEmpty() -> None
        
        
        Sets the range to an empty interval.
        
        
        
        """
    @staticmethod
    def SetMax(*args, **kwargs):
        """
        
        SetMax(max) -> None
        
        
        Sets the maximum value of the range.
        
        
        Parameters
        ----------
        max : Vec2f
        
        
        """
    @staticmethod
    def SetMin(*args, **kwargs):
        """
        
        SetMin(min) -> None
        
        
        Sets the minimum value of the range.
        
        
        Parameters
        ----------
        min : Vec2f
        
        
        """
    @staticmethod
    def UnionWith(*args, **kwargs):
        """
        
        UnionWith(b) -> Range2f
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : Range2f
        
        
        
        ----------------------------------------------------------------------
        
        UnionWith(b) -> Range2f
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : Vec2f
        
        
        """
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
        """
        
        __init__()
        
        
        The default constructor creates an empty range.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(min, max)
        
        
        This constructor initializes the minimum and maximum points.
        
        
        Parameters
        ----------
        min : Vec2f
        
        max : Vec2f
        
        
        """
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
    """
    """
    __instance_size__: typing.ClassVar[int] = 64
    dimension: typing.ClassVar[int] = 3
    unitCube: typing.ClassVar[Range3d]  # value = Gf.Range3d(Gf.Vec3d(0.0, 0.0, 0.0), Gf.Vec3d(1.0, 1.0, 1.0))
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        Contains(point) -> bool
        
        
        Returns true if the ``point`` is located inside the range.
        
        
        As with all operations of this type, the range is assumed to include
        its extrema.
        
        
        Parameters
        ----------
        point : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        Contains(range) -> bool
        
        
        Returns true if the ``range`` is located entirely inside the range.
        
        
        As with all operations of this type, the ranges are assumed to include
        their extrema.
        
        
        Parameters
        ----------
        range : Range3d
        
        
        """
    @staticmethod
    def GetCorner(*args, **kwargs):
        """
        
        GetCorner(i) -> Vec3d
        
        
        Returns the ith corner of the range, in the following order: LDB, RDB,
        LUB, RUB, LDF, RDF, LUF, RUF.
        
        
        Where L/R is left/right, D/U is down/up, and B/F is back/front.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        """
        
        GetDistanceSquared(p) -> float
        
        
        Compute the squared distance from a point to the range.
        
        
        Parameters
        ----------
        p : Vec3d
        
        
        """
    @staticmethod
    def GetIntersection(*args, **kwargs):
        """
        
        **classmethod** GetIntersection(a, b) -> Range3d
        
        
        Returns a ``GfRange3d`` that describes the intersection of ``a`` and
        ``b`` .
        
        
        Parameters
        ----------
        a : Range3d
        
        b : Range3d
        
        
        """
    @staticmethod
    def GetMax(*args, **kwargs):
        """
        
        GetMax() -> Vec3d
        
        
        Returns the maximum value of the range.
        
        
        
        """
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        """
        
        GetMidpoint() -> Vec3d
        
        
        Returns the midpoint of the range, that is, 0.5\\*(min+max).
        
        
        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        
        
        
        """
    @staticmethod
    def GetMin(*args, **kwargs):
        """
        
        GetMin() -> Vec3d
        
        
        Returns the minimum value of the range.
        
        
        
        """
    @staticmethod
    def GetOctant(*args, **kwargs):
        """
        
        GetOctant(i) -> Range3d
        
        
        Returns the ith octant of the range, in the following order: LDB, RDB,
        LUB, RUB, LDF, RDF, LUF, RUF.
        
        
        Where L/R is left/right, D/U is down/up, and B/F is back/front.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetSize(*args, **kwargs):
        """
        
        GetSize() -> Vec3d
        
        
        Returns the size of the range.
        
        
        
        """
    @staticmethod
    def GetUnion(*args, **kwargs):
        """
        
        **classmethod** GetUnion(a, b) -> Range3d
        
        
        Returns the smallest ``GfRange3d`` which contains both ``a`` and ``b``
        .
        
        
        Parameters
        ----------
        a : Range3d
        
        b : Range3d
        
        
        """
    @staticmethod
    def IntersectWith(*args, **kwargs):
        """
        
        IntersectWith(b) -> Range3d
        
        
        Modifies this range to hold its intersection with ``b`` and returns
        the result.
        
        
        Parameters
        ----------
        b : Range3d
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Returns whether the range is empty (max<min).
        
        
        
        """
    @staticmethod
    def SetEmpty(*args, **kwargs):
        """
        
        SetEmpty() -> None
        
        
        Sets the range to an empty interval.
        
        
        
        """
    @staticmethod
    def SetMax(*args, **kwargs):
        """
        
        SetMax(max) -> None
        
        
        Sets the maximum value of the range.
        
        
        Parameters
        ----------
        max : Vec3d
        
        
        """
    @staticmethod
    def SetMin(*args, **kwargs):
        """
        
        SetMin(min) -> None
        
        
        Sets the minimum value of the range.
        
        
        Parameters
        ----------
        min : Vec3d
        
        
        """
    @staticmethod
    def UnionWith(*args, **kwargs):
        """
        
        UnionWith(b) -> Range3d
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : Range3d
        
        
        
        ----------------------------------------------------------------------
        
        UnionWith(b) -> Range3d
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : Vec3d
        
        
        """
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
        """
        
        __init__()
        
        
        The default constructor creates an empty range.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(min, max)
        
        
        This constructor initializes the minimum and maximum points.
        
        
        Parameters
        ----------
        min : Vec3d
        
        max : Vec3d
        
        
        """
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
    """
    """
    __instance_size__: typing.ClassVar[int] = 40
    dimension: typing.ClassVar[int] = 3
    unitCube: typing.ClassVar[Range3f]  # value = Gf.Range3f(Gf.Vec3f(0.0, 0.0, 0.0), Gf.Vec3f(1.0, 1.0, 1.0))
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        Contains(point) -> bool
        
        
        Returns true if the ``point`` is located inside the range.
        
        
        As with all operations of this type, the range is assumed to include
        its extrema.
        
        
        Parameters
        ----------
        point : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        Contains(range) -> bool
        
        
        Returns true if the ``range`` is located entirely inside the range.
        
        
        As with all operations of this type, the ranges are assumed to include
        their extrema.
        
        
        Parameters
        ----------
        range : Range3f
        
        
        """
    @staticmethod
    def GetCorner(*args, **kwargs):
        """
        
        GetCorner(i) -> Vec3f
        
        
        Returns the ith corner of the range, in the following order: LDB, RDB,
        LUB, RUB, LDF, RDF, LUF, RUF.
        
        
        Where L/R is left/right, D/U is down/up, and B/F is back/front.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDistanceSquared(*args, **kwargs):
        """
        
        GetDistanceSquared(p) -> float
        
        
        Compute the squared distance from a point to the range.
        
        
        Parameters
        ----------
        p : Vec3f
        
        
        """
    @staticmethod
    def GetIntersection(*args, **kwargs):
        """
        
        **classmethod** GetIntersection(a, b) -> Range3f
        
        
        Returns a ``GfRange3f`` that describes the intersection of ``a`` and
        ``b`` .
        
        
        Parameters
        ----------
        a : Range3f
        
        b : Range3f
        
        
        """
    @staticmethod
    def GetMax(*args, **kwargs):
        """
        
        GetMax() -> Vec3f
        
        
        Returns the maximum value of the range.
        
        
        
        """
    @staticmethod
    def GetMidpoint(*args, **kwargs):
        """
        
        GetMidpoint() -> Vec3f
        
        
        Returns the midpoint of the range, that is, 0.5\\*(min+max).
        
        
        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        
        
        
        """
    @staticmethod
    def GetMin(*args, **kwargs):
        """
        
        GetMin() -> Vec3f
        
        
        Returns the minimum value of the range.
        
        
        
        """
    @staticmethod
    def GetOctant(*args, **kwargs):
        """
        
        GetOctant(i) -> Range3f
        
        
        Returns the ith octant of the range, in the following order: LDB, RDB,
        LUB, RUB, LDF, RDF, LUF, RUF.
        
        
        Where L/R is left/right, D/U is down/up, and B/F is back/front.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetSize(*args, **kwargs):
        """
        
        GetSize() -> Vec3f
        
        
        Returns the size of the range.
        
        
        
        """
    @staticmethod
    def GetUnion(*args, **kwargs):
        """
        
        **classmethod** GetUnion(a, b) -> Range3f
        
        
        Returns the smallest ``GfRange3f`` which contains both ``a`` and ``b``
        .
        
        
        Parameters
        ----------
        a : Range3f
        
        b : Range3f
        
        
        """
    @staticmethod
    def IntersectWith(*args, **kwargs):
        """
        
        IntersectWith(b) -> Range3f
        
        
        Modifies this range to hold its intersection with ``b`` and returns
        the result.
        
        
        Parameters
        ----------
        b : Range3f
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Returns whether the range is empty (max<min).
        
        
        
        """
    @staticmethod
    def SetEmpty(*args, **kwargs):
        """
        
        SetEmpty() -> None
        
        
        Sets the range to an empty interval.
        
        
        
        """
    @staticmethod
    def SetMax(*args, **kwargs):
        """
        
        SetMax(max) -> None
        
        
        Sets the maximum value of the range.
        
        
        Parameters
        ----------
        max : Vec3f
        
        
        """
    @staticmethod
    def SetMin(*args, **kwargs):
        """
        
        SetMin(min) -> None
        
        
        Sets the minimum value of the range.
        
        
        Parameters
        ----------
        min : Vec3f
        
        
        """
    @staticmethod
    def UnionWith(*args, **kwargs):
        """
        
        UnionWith(b) -> Range3f
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : Range3f
        
        
        
        ----------------------------------------------------------------------
        
        UnionWith(b) -> Range3f
        
        
        Extend ``this`` to include ``b`` .
        
        
        Parameters
        ----------
        b : Vec3f
        
        
        """
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
        """
        
        __init__()
        
        
        The default constructor creates an empty range.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(min, max)
        
        
        This constructor initializes the minimum and maximum points.
        
        
        Parameters
        ----------
        min : Vec3f
        
        max : Vec3f
        
        
        """
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
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def FindClosestPoint(*args, **kwargs):
        """
        
        FindClosestPoint(point, rayDistance) -> Vec3d
        
        
        Returns the point on the ray that is closest to ``point`` .
        
        
        If ``rayDistance`` is not ``None`` , it will be set to the parametric
        distance along the ray of the closest point.
        
        
        Parameters
        ----------
        point : Vec3d
        
        rayDistance : float
        
        
        """
    @staticmethod
    def GetPoint(*args, **kwargs):
        """
        
        GetPoint(distance) -> Vec3d
        
        
        Returns the point that is ``distance`` units from the starting point
        along the direction vector, expressed in parametic distance.
        
        
        Parameters
        ----------
        distance : float
        
        
        """
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
        """
        
        SetEnds(startPoint, endPoint) -> None
        
        
        Sets the ray by specifying a starting point and an ending point.
        
        
        Parameters
        ----------
        startPoint : Vec3d
        
        endPoint : Vec3d
        
        
        """
    @staticmethod
    def SetPointAndDirection(*args, **kwargs):
        """
        
        SetPointAndDirection(startPoint, direction) -> None
        
        
        Sets the ray by specifying a starting point and a direction.
        
        
        Parameters
        ----------
        startPoint : Vec3d
        
        direction : Vec3d
        
        
        """
    @staticmethod
    def Transform(*args, **kwargs):
        """
        
        Transform(matrix) -> Ray
        
        
        Transforms the ray by the given matrix.
        
        
        Parameters
        ----------
        matrix : Matrix4d
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        The default constructor leaves the ray parameters undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(startPoint, direction)
        
        
        This constructor takes a starting point and a direction.
        
        
        Parameters
        ----------
        startPoint : Vec3d
        
        direction : Vec3d
        
        
        """
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
        """
        type : Vec3d
        
        
        Returns the direction vector of the segment.
        
        
        This is not guaranteed to be unit length.
        """
    @direction.setter
    def direction(*args, **kwargs):
        ...
    @property
    def startPoint(*args, **kwargs):
        """
        type : Vec3d
        
        
        Returns the starting point of the segment.
        """
    @startPoint.setter
    def startPoint(*args, **kwargs):
        ...
class Rect2i(Boost.Python.instance):
    """
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        Contains(p) -> bool
        
        
        Returns true if the specified point in the rectangle.
        
        
        Parameters
        ----------
        p : Vec2i
        
        
        """
    @staticmethod
    def GetArea(*args, **kwargs):
        """
        
        GetArea() -> int
        
        
        Return the area of the rectangle.
        
        
        
        """
    @staticmethod
    def GetCenter(*args, **kwargs):
        """
        
        GetCenter() -> Vec2i
        
        
        Returns the center point of the rectangle.
        
        
        
        """
    @staticmethod
    def GetHeight(*args, **kwargs):
        """
        
        GetHeight() -> int
        
        
        Returns the height of the rectangle.
        
        
        
        If the min and max y-coordinates are coincident, the height is one.
        
        
        
        """
    @staticmethod
    def GetIntersection(*args, **kwargs):
        """
        
        GetIntersection(that) -> Rect2i
        
        
        Computes the intersection of two rectangles.
        
        
        Parameters
        ----------
        that : Rect2i
        
        
        """
    @staticmethod
    def GetMax(*args, **kwargs):
        """
        
        GetMax() -> Vec2i
        
        
        Returns the max corner of the rectangle.
        
        
        
        """
    @staticmethod
    def GetMaxX(*args, **kwargs):
        """
        
        GetMaxX() -> int
        
        
        Return the X value of the max corner.
        
        
        
        """
    @staticmethod
    def GetMaxY(*args, **kwargs):
        """
        
        GetMaxY() -> int
        
        
        Return the Y value of the max corner.
        
        
        
        """
    @staticmethod
    def GetMin(*args, **kwargs):
        """
        
        GetMin() -> Vec2i
        
        
        Returns the min corner of the rectangle.
        
        
        
        """
    @staticmethod
    def GetMinX(*args, **kwargs):
        """
        
        GetMinX() -> int
        
        
        Return the X value of min corner.
        
        
        
        """
    @staticmethod
    def GetMinY(*args, **kwargs):
        """
        
        GetMinY() -> int
        
        
        Return the Y value of the min corner.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized() -> Rect2i
        
        
        Returns a normalized rectangle, i.e.
        
        
        one that has a non-negative width and height.
        
        ``GetNormalized()`` swaps the min and max x-coordinates to ensure a
        non-negative width, and similarly for the y-coordinates.
        
        
        
        """
    @staticmethod
    def GetSize(*args, **kwargs):
        """
        
        GetSize() -> Vec2i
        
        
        Returns the size of the rectangle as a vector (width,height).
        
        
        
        """
    @staticmethod
    def GetUnion(*args, **kwargs):
        """
        
        GetUnion(that) -> Rect2i
        
        
        Computes the union of two rectangles.
        
        
        Parameters
        ----------
        that : Rect2i
        
        
        """
    @staticmethod
    def GetWidth(*args, **kwargs):
        """
        
        GetWidth() -> int
        
        
        Returns the width of the rectangle.
        
        
        
        If the min and max x-coordinates are coincident, the width is one.
        
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Returns true if the rectangle is empty.
        
        
        An empty rectangle has one or both of its min coordinates strictly
        greater than the corresponding max coordinate.
        
        An empty rectangle is not valid.
        
        
        
        """
    @staticmethod
    def IsNull(*args, **kwargs):
        """
        
        IsNull() -> bool
        
        
        Returns true if the rectangle is a null rectangle.
        
        
        A null rectangle has both the width and the height set to 0, that is
        
        .. code-block:: text
        
          GetMaxX() == GetMinX() - 1
        
         and
        
        .. code-block:: text
        
          GetMaxY() == GetMinY() - 1
        
         Remember that if ``GetMinX()`` and ``GetMaxX()`` return the same
        value then the rectangle has width 1, and similarly for the height.
        
        A null rectangle is both empty, and not valid.
        
        
        
        """
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        IsValid() -> bool
        
        
        Return true if the rectangle is valid (equivalently, not empty).
        
        
        
        """
    @staticmethod
    def SetMax(*args, **kwargs):
        """
        
        SetMax(max) -> None
        
        
        Sets the max corner of the rectangle.
        
        
        Parameters
        ----------
        max : Vec2i
        
        
        """
    @staticmethod
    def SetMaxX(*args, **kwargs):
        """
        
        SetMaxX(x) -> None
        
        
        Set the X value of the max corner.
        
        
        Parameters
        ----------
        x : int
        
        
        """
    @staticmethod
    def SetMaxY(*args, **kwargs):
        """
        
        SetMaxY(y) -> None
        
        
        Set the Y value of the max corner.
        
        
        Parameters
        ----------
        y : int
        
        
        """
    @staticmethod
    def SetMin(*args, **kwargs):
        """
        
        SetMin(min) -> None
        
        
        Sets the min corner of the rectangle.
        
        
        Parameters
        ----------
        min : Vec2i
        
        
        """
    @staticmethod
    def SetMinX(*args, **kwargs):
        """
        
        SetMinX(x) -> None
        
        
        Set the X value of the min corner.
        
        
        Parameters
        ----------
        x : int
        
        
        """
    @staticmethod
    def SetMinY(*args, **kwargs):
        """
        
        SetMinY(y) -> None
        
        
        Set the Y value of the min corner.
        
        
        Parameters
        ----------
        y : int
        
        
        """
    @staticmethod
    def Translate(*args, **kwargs):
        """
        
        Translate(displacement) -> None
        
        
        Move the rectangle by ``displ`` .
        
        
        Parameters
        ----------
        displacement : Vec2i
        
        
        """
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __iadd__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Constructs an empty rectangle.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(min, max)
        
        
        Constructs a rectangle with ``min`` and ``max`` corners.
        
        
        Parameters
        ----------
        min : Vec2i
        
        max : Vec2i
        
        
        
        ----------------------------------------------------------------------
        
        __init__(min, width, height)
        
        
        Constructs a rectangle with ``min`` corner and the indicated ``width``
        and ``height`` .
        
        
        Parameters
        ----------
        min : Vec2i
        
        width : int
        
        height : int
        
        
        """
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
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Decompose(*args, **kwargs):
        """
        
        Decompose(axis0, axis1, axis2) -> Vec3d
        
        
        Decompose rotation about 3 orthogonal axes.
        
        
        If the axes are not orthogonal, warnings will be spewed.
        
        
        Parameters
        ----------
        axis0 : Vec3d
        
        axis1 : Vec3d
        
        axis2 : Vec3d
        
        
        """
    @staticmethod
    def DecomposeRotation(*args, **kwargs):
        """
        
        **classmethod** DecomposeRotation(rot, TwAxis, FBAxis, LRAxis, handedness, thetaTw, thetaFB, thetaLR, thetaSw, useHint, swShift) -> None
        
        
        Parameters
        ----------
        rot : Matrix4d
        
        TwAxis : Vec3d
        
        FBAxis : Vec3d
        
        LRAxis : Vec3d
        
        handedness : float
        
        thetaTw : float
        
        thetaFB : float
        
        thetaLR : float
        
        thetaSw : float
        
        useHint : bool
        
        swShift : float
        
        
        """
    @staticmethod
    def DecomposeRotation3(*args, **kwargs):
        ...
    @staticmethod
    def GetAngle(*args, **kwargs):
        """
        
        GetAngle() -> float
        
        
        Returns the rotation angle in degrees.
        
        
        
        """
    @staticmethod
    def GetAxis(*args, **kwargs):
        """
        
        GetAxis() -> Vec3d
        
        
        Returns the axis of rotation.
        
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse() -> Rotation
        
        
        Returns the inverse of this rotation.
        
        
        
        """
    @staticmethod
    def GetQuat(*args, **kwargs):
        """
        
        GetQuat() -> Quatd
        
        
        Returns the rotation expressed as a quaternion.
        
        
        
        """
    @staticmethod
    def GetQuaternion(*args, **kwargs):
        """
        
        GetQuaternion() -> Quaternion
        
        
        Returns the rotation expressed as a quaternion.
        
        
        
        """
    @staticmethod
    def MatchClosestEulerRotation(*args, **kwargs):
        """
        
        **classmethod** MatchClosestEulerRotation(targetTw, targetFB, targetLR, targetSw, thetaTw, thetaFB, thetaLR, thetaSw) -> None
        
        
        Replace the hint angles with the closest rotation of the given
        rotation to the hint.
        
        
        Each angle in the rotation will be within Pi of the corresponding hint
        angle and the sum of the differences with the hint will be minimized.
        If a given rotation value is null then that angle will be treated as
        0.0 and ignored in the calculations.
        
        All angles are in radians. The rotation order is Tw/FB/LR/Sw.
        
        
        Parameters
        ----------
        targetTw : float
        
        targetFB : float
        
        targetLR : float
        
        targetSw : float
        
        thetaTw : float
        
        thetaFB : float
        
        thetaLR : float
        
        thetaSw : float
        
        
        """
    @staticmethod
    def RotateOntoProjected(*args, **kwargs):
        """
        
        **classmethod** RotateOntoProjected(v1, v2, axis) -> Rotation
        
        
        Parameters
        ----------
        v1 : Vec3d
        
        v2 : Vec3d
        
        axis : Vec3d
        
        
        """
    @staticmethod
    def SetAxisAngle(*args, **kwargs):
        """
        
        SetAxisAngle(axis, angle) -> Rotation
        
        
        Sets the rotation to be ``angle`` degrees about ``axis`` .
        
        
        Parameters
        ----------
        axis : Vec3d
        
        angle : float
        
        
        """
    @staticmethod
    def SetIdentity(*args, **kwargs):
        """
        
        SetIdentity() -> Rotation
        
        
        Sets the rotation to an identity rotation.
        
        
        (This is chosen to be 0 degrees around the positive X axis.)
        
        
        
        """
    @staticmethod
    def SetQuat(*args, **kwargs):
        """
        
        SetQuat(quat) -> Rotation
        
        
        Sets the rotation from a quaternion.
        
        
        Note that this method accepts GfQuatf and GfQuath since they
        implicitly convert to GfQuatd.
        
        
        Parameters
        ----------
        quat : Quatd
        
        
        """
    @staticmethod
    def SetQuaternion(*args, **kwargs):
        """
        
        SetQuaternion(quat) -> Rotation
        
        
        Sets the rotation from a quaternion.
        
        
        Parameters
        ----------
        quat : Quaternion
        
        
        """
    @staticmethod
    def SetRotateInto(*args, **kwargs):
        """
        
        SetRotateInto(rotateFrom, rotateTo) -> Rotation
        
        
        Sets the rotation to one that brings the ``rotateFrom`` vector to
        align with ``rotateTo`` .
        
        
        The passed vectors need not be unit length.
        
        
        Parameters
        ----------
        rotateFrom : Vec3d
        
        rotateTo : Vec3d
        
        
        """
    @staticmethod
    def TransformDir(*args, **kwargs):
        """
        
        TransformDir(vec) -> Vec3f
        
        
        Transforms row vector ``vec`` by the rotation, returning the result.
        
        
        Parameters
        ----------
        vec : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        TransformDir(vec) -> Vec3d
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        vec : Vec3d
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __idiv__(*args, **kwargs):
        ...
    @staticmethod
    def __imul__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        The default constructor leaves the rotation undefined.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(axis, angle)
        
        
        This constructor initializes the rotation to be ``angle`` degrees
        about ``axis`` .
        
        
        Parameters
        ----------
        axis : Vec3d
        
        angle : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(quaternion)
        
        
        This constructor initializes the rotation from a quaternion.
        
        
        Parameters
        ----------
        quaternion : Quaternion
        
        
        
        ----------------------------------------------------------------------
        
        __init__(quat)
        
        
        This constructor initializes the rotation from a quaternion.
        
        
        Note that this constructor accepts GfQuatf and GfQuath since they
        implicitly convert to GfQuatd.
        
        
        Parameters
        ----------
        quat : Quatd
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rotateFrom, rotateTo)
        
        
        This constructor initializes the rotation to one that brings the
        ``rotateFrom`` vector to align with ``rotateTo`` .
        
        
        The passed vectors need not be unit length.
        
        
        Parameters
        ----------
        rotateFrom : Vec3d
        
        rotateTo : Vec3d
        
        
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
    __instance_size__: typing.ClassVar[int] = 32
    dimension: typing.ClassVar[int] = 2
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(v) -> Size2
        
        
        Set to the values in a given array.
        
        
        Parameters
        ----------
        v : int
        
        
        
        ----------------------------------------------------------------------
        
        Set(v0, v1) -> Size2
        
        
        Set to values passed directly.
        
        
        Parameters
        ----------
        v0 : int
        
        v1 : int
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor initializes components to zero.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(o)
        
        
        Copy constructor.
        
        
        Parameters
        ----------
        o : Size2
        
        
        
        ----------------------------------------------------------------------
        
        __init__(o)
        
        
        Conversion from GfVec2i.
        
        
        Parameters
        ----------
        o : Vec2i
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Construct from an array.
        
        
        Parameters
        ----------
        v : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v0, v1)
        
        
        Construct from two values.
        
        
        Parameters
        ----------
        v0 : int
        
        v1 : int
        
        
        """
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
    __instance_size__: typing.ClassVar[int] = 40
    dimension: typing.ClassVar[int] = 3
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(v) -> Size3
        
        
        Set to the values in ``v`` .
        
        
        Parameters
        ----------
        v : int
        
        
        
        ----------------------------------------------------------------------
        
        Set(v0, v1, v2) -> Size3
        
        
        Set to values passed directly.
        
        
        Parameters
        ----------
        v0 : int
        
        v1 : int
        
        v2 : int
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor initializes components to zero.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(o)
        
        
        Copy constructor.
        
        
        Parameters
        ----------
        o : Size3
        
        
        
        ----------------------------------------------------------------------
        
        __init__(o)
        
        
        Conversion from GfVec3i.
        
        
        Parameters
        ----------
        o : Vec3i
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v)
        
        
        Construct from an array.
        
        
        Parameters
        ----------
        v : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(v0, v1, v2)
        
        
        Construct from three values.
        
        
        Parameters
        ----------
        v0 : int
        
        v1 : int
        
        v2 : int
        
        
        """
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
    """
    """
    __instance_size__: typing.ClassVar[int] = 152
    @staticmethod
    def GetMatrix(*args, **kwargs):
        """
        
        GetMatrix() -> Matrix4d
        
        
        Returns a ``GfMatrix4d`` that implements the cumulative
        transformation.
        
        
        
        """
    @staticmethod
    def GetPivotOrientation(*args, **kwargs):
        """
        
        GetPivotOrientation() -> Rotation
        
        
        Returns the pivot orientation component.
        
        
        
        """
    @staticmethod
    def GetPivotPosition(*args, **kwargs):
        """
        
        GetPivotPosition() -> Vec3d
        
        
        Returns the pivot position component.
        
        
        
        """
    @staticmethod
    def GetRotation(*args, **kwargs):
        """
        
        GetRotation() -> Rotation
        
        
        Returns the rotation component.
        
        
        
        """
    @staticmethod
    def GetScale(*args, **kwargs):
        """
        
        GetScale() -> Vec3d
        
        
        Returns the scale component.
        
        
        
        """
    @staticmethod
    def GetTranslation(*args, **kwargs):
        """
        
        GetTranslation() -> Vec3d
        
        
        Returns the translation component.
        
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        
        Set method used by old 2x code. (Deprecated)
        """
    @staticmethod
    def SetIdentity(*args, **kwargs):
        """
        
        SetIdentity() -> Transform
        
        
        Sets the transformation to the identity transformation.
        
        
        
        """
    @staticmethod
    def SetMatrix(*args, **kwargs):
        """
        
        SetMatrix(m) -> Transform
        
        
        Sets the transform components to implement the transformation
        represented by matrix ``m`` , ignoring any projection.
        
        
        This tries to leave the current center unchanged.
        
        
        Parameters
        ----------
        m : Matrix4d
        
        
        """
    @staticmethod
    def SetPivotOrientation(*args, **kwargs):
        """
        
        SetPivotOrientation(pivotOrient) -> None
        
        
        Sets the pivot orientation component, leaving all others untouched.
        
        
        Parameters
        ----------
        pivotOrient : Rotation
        
        
        """
    @staticmethod
    def SetPivotPosition(*args, **kwargs):
        """
        
        SetPivotPosition(pivPos) -> None
        
        
        Sets the pivot position component, leaving all others untouched.
        
        
        Parameters
        ----------
        pivPos : Vec3d
        
        
        """
    @staticmethod
    def SetRotation(*args, **kwargs):
        """
        
        SetRotation(rotation) -> None
        
        
        Sets the rotation component, leaving all others untouched.
        
        
        Parameters
        ----------
        rotation : Rotation
        
        
        """
    @staticmethod
    def SetScale(*args, **kwargs):
        """
        
        SetScale(scale) -> None
        
        
        Sets the scale component, leaving all others untouched.
        
        
        Parameters
        ----------
        scale : Vec3d
        
        
        """
    @staticmethod
    def SetTranslation(*args, **kwargs):
        """
        
        SetTranslation(translation) -> None
        
        
        Sets the translation component, leaving all others untouched.
        
        
        Parameters
        ----------
        translation : Vec3d
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 2
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec2d
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 2.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetComplement(*args, **kwargs):
        """
        
        GetComplement(b) -> Vec2d
        
        
        Returns the orthogonal complement of ``this->GetProjection(b)`` .
        
        
        That is:
        
        .. code-block:: text
        
          \\*this - this->GetProjection(b)
        
        
        
        Parameters
        ----------
        b : Vec2d
        
        
        """
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> float
        
        
        Length.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Vec2d
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def GetProjection(*args, **kwargs):
        """
        
        GetProjection(v) -> Vec2d
        
        
        Returns the projection of ``this`` onto ``v`` .
        
        
        That is:
        
        .. code-block:: text
        
          v \\* (\\*this \\* v)
        
        
        
        Parameters
        ----------
        v : Vec2d
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> float
        
        
        Normalizes the vector in place to unit length, returning the length
        before normalization.
        
        
        If the length of the vector is smaller than ``eps`` , then the vector
        is set to vector/ ``eps`` . The original length of the vector is
        returned. See also GfNormalize() .
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec2d
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec2d
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : float
        
        s1 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec2f.
        
        
        Parameters
        ----------
        other : Vec2f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec2h.
        
        
        Parameters
        ----------
        other : Vec2h
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec2i.
        
        
        Parameters
        ----------
        other : Vec2i
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 2
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec2f
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 2.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetComplement(*args, **kwargs):
        """
        
        GetComplement(b) -> Vec2f
        
        
        Returns the orthogonal complement of ``this->GetProjection(b)`` .
        
        
        That is:
        
        .. code-block:: text
        
          \\*this - this->GetProjection(b)
        
        
        
        Parameters
        ----------
        b : Vec2f
        
        
        """
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> float
        
        
        Length.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Vec2f
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def GetProjection(*args, **kwargs):
        """
        
        GetProjection(v) -> Vec2f
        
        
        Returns the projection of ``this`` onto ``v`` .
        
        
        That is:
        
        .. code-block:: text
        
          v \\* (\\*this \\* v)
        
        
        
        Parameters
        ----------
        v : Vec2f
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> float
        
        
        Normalizes the vector in place to unit length, returning the length
        before normalization.
        
        
        If the length of the vector is smaller than ``eps`` , then the vector
        is set to vector/ ``eps`` . The original length of the vector is
        returned. See also GfNormalize() .
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec2f
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec2f
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : float
        
        s1 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfVec2d.
        
        
        Parameters
        ----------
        other : Vec2d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec2h.
        
        
        Parameters
        ----------
        other : Vec2h
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec2i.
        
        
        Parameters
        ----------
        other : Vec2i
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 2
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec2h
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 2.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetComplement(*args, **kwargs):
        """
        
        GetComplement(b) -> Vec2h
        
        
        Returns the orthogonal complement of ``this->GetProjection(b)`` .
        
        
        That is:
        
        .. code-block:: text
        
          \\*this - this->GetProjection(b)
        
        
        
        Parameters
        ----------
        b : Vec2h
        
        
        """
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> GfHalf
        
        
        Length.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Vec2h
        
        
        Parameters
        ----------
        eps : GfHalf
        
        
        """
    @staticmethod
    def GetProjection(*args, **kwargs):
        """
        
        GetProjection(v) -> Vec2h
        
        
        Returns the projection of ``this`` onto ``v`` .
        
        
        That is:
        
        .. code-block:: text
        
          v \\* (\\*this \\* v)
        
        
        
        Parameters
        ----------
        v : Vec2h
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> GfHalf
        
        
        Normalizes the vector in place to unit length, returning the length
        before normalization.
        
        
        If the length of the vector is smaller than ``eps`` , then the vector
        is set to vector/ ``eps`` . The original length of the vector is
        returned. See also GfNormalize() .
        
        
        Parameters
        ----------
        eps : GfHalf
        
        
        """
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec2h
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec2h
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : GfHalf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : GfHalf
        
        s1 : GfHalf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfVec2d.
        
        
        Parameters
        ----------
        other : Vec2d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfVec2f.
        
        
        Parameters
        ----------
        other : Vec2f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec2i.
        
        
        Parameters
        ----------
        other : Vec2i
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 2
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec2i
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 2.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec2i
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec2i
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : int
        
        s1 : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 3
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec3d
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 3.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def BuildOrthonormalFrame(*args, **kwargs):
        """
        
        BuildOrthonormalFrame(v1, v2, eps) -> None
        
        
        Sets ``v1`` and ``v2`` to unit vectors such that v1, v2 and \\*this
        are mutually orthogonal.
        
        
        If the length L of \\*this is smaller than ``eps`` , then v1 and v2
        will have magnitude L/eps. As a result, the function delivers a
        continuous result as \\*this shrinks in length.
        
        
        Parameters
        ----------
        v1 : Vec3d
        
        v2 : Vec3d
        
        eps : float
        
        
        """
    @staticmethod
    def GetComplement(*args, **kwargs):
        """
        
        GetComplement(b) -> Vec3d
        
        
        Returns the orthogonal complement of ``this->GetProjection(b)`` .
        
        
        That is:
        
        .. code-block:: text
        
          \\*this - this->GetProjection(b)
        
        
        
        Parameters
        ----------
        b : Vec3d
        
        
        """
    @staticmethod
    def GetCross(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> float
        
        
        Length.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Vec3d
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def GetProjection(*args, **kwargs):
        """
        
        GetProjection(v) -> Vec3d
        
        
        Returns the projection of ``this`` onto ``v`` .
        
        
        That is:
        
        .. code-block:: text
        
          v \\* (\\*this \\* v)
        
        
        
        Parameters
        ----------
        v : Vec3d
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> float
        
        
        Normalizes the vector in place to unit length, returning the length
        before normalization.
        
        
        If the length of the vector is smaller than ``eps`` , then the vector
        is set to vector/ ``eps`` . The original length of the vector is
        returned. See also GfNormalize() .
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def OrthogonalizeBasis(*args, **kwargs):
        """
        
        **classmethod** OrthogonalizeBasis(tx, ty, tz, normalize, eps) -> bool
        
        
        Orthogonalize and optionally normalize a set of basis vectors.
        
        
        This uses an iterative method that is very stable even when the
        vectors are far from orthogonal (close to colinear). The number of
        iterations and thus the computation time does increase as the vectors
        become close to colinear, however. Returns a bool specifying whether
        the solution converged after a number of iterations. If it did not
        converge, the returned vectors will be as close as possible to
        orthogonal within the iteration limit. Colinear vectors will be
        unaltered, and the method will return false.
        
        
        Parameters
        ----------
        tx : Vec3d
        
        ty : Vec3d
        
        tz : Vec3d
        
        normalize : bool
        
        eps : float
        
        
        """
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec3d
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec3d
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
    @staticmethod
    def ZAxis(*args, **kwargs):
        """
        
        **classmethod** ZAxis() -> Vec3d
        
        
        Create a unit vector along the Z-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1, s2)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : float
        
        s1 : float
        
        s2 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec3f.
        
        
        Parameters
        ----------
        other : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec3h.
        
        
        Parameters
        ----------
        other : Vec3h
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec3i.
        
        
        Parameters
        ----------
        other : Vec3i
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 3
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec3f
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 3.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def BuildOrthonormalFrame(*args, **kwargs):
        """
        
        BuildOrthonormalFrame(v1, v2, eps) -> None
        
        
        Sets ``v1`` and ``v2`` to unit vectors such that v1, v2 and \\*this
        are mutually orthogonal.
        
        
        If the length L of \\*this is smaller than ``eps`` , then v1 and v2
        will have magnitude L/eps. As a result, the function delivers a
        continuous result as \\*this shrinks in length.
        
        
        Parameters
        ----------
        v1 : Vec3f
        
        v2 : Vec3f
        
        eps : float
        
        
        """
    @staticmethod
    def GetComplement(*args, **kwargs):
        """
        
        GetComplement(b) -> Vec3f
        
        
        Returns the orthogonal complement of ``this->GetProjection(b)`` .
        
        
        That is:
        
        .. code-block:: text
        
          \\*this - this->GetProjection(b)
        
        
        
        Parameters
        ----------
        b : Vec3f
        
        
        """
    @staticmethod
    def GetCross(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> float
        
        
        Length.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Vec3f
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def GetProjection(*args, **kwargs):
        """
        
        GetProjection(v) -> Vec3f
        
        
        Returns the projection of ``this`` onto ``v`` .
        
        
        That is:
        
        .. code-block:: text
        
          v \\* (\\*this \\* v)
        
        
        
        Parameters
        ----------
        v : Vec3f
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> float
        
        
        Normalizes the vector in place to unit length, returning the length
        before normalization.
        
        
        If the length of the vector is smaller than ``eps`` , then the vector
        is set to vector/ ``eps`` . The original length of the vector is
        returned. See also GfNormalize() .
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def OrthogonalizeBasis(*args, **kwargs):
        """
        
        **classmethod** OrthogonalizeBasis(tx, ty, tz, normalize, eps) -> bool
        
        
        Orthogonalize and optionally normalize a set of basis vectors.
        
        
        This uses an iterative method that is very stable even when the
        vectors are far from orthogonal (close to colinear). The number of
        iterations and thus the computation time does increase as the vectors
        become close to colinear, however. Returns a bool specifying whether
        the solution converged after a number of iterations. If it did not
        converge, the returned vectors will be as close as possible to
        orthogonal within the iteration limit. Colinear vectors will be
        unaltered, and the method will return false.
        
        
        Parameters
        ----------
        tx : Vec3f
        
        ty : Vec3f
        
        tz : Vec3f
        
        normalize : bool
        
        eps : float
        
        
        """
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec3f
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec3f
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
    @staticmethod
    def ZAxis(*args, **kwargs):
        """
        
        **classmethod** ZAxis() -> Vec3f
        
        
        Create a unit vector along the Z-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1, s2)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : float
        
        s1 : float
        
        s2 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfVec3d.
        
        
        Parameters
        ----------
        other : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec3h.
        
        
        Parameters
        ----------
        other : Vec3h
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec3i.
        
        
        Parameters
        ----------
        other : Vec3i
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 3
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec3h
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 3.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def BuildOrthonormalFrame(*args, **kwargs):
        """
        
        BuildOrthonormalFrame(v1, v2, eps) -> None
        
        
        Sets ``v1`` and ``v2`` to unit vectors such that v1, v2 and \\*this
        are mutually orthogonal.
        
        
        If the length L of \\*this is smaller than ``eps`` , then v1 and v2
        will have magnitude L/eps. As a result, the function delivers a
        continuous result as \\*this shrinks in length.
        
        
        Parameters
        ----------
        v1 : Vec3h
        
        v2 : Vec3h
        
        eps : GfHalf
        
        
        """
    @staticmethod
    def GetComplement(*args, **kwargs):
        """
        
        GetComplement(b) -> Vec3h
        
        
        Returns the orthogonal complement of ``this->GetProjection(b)`` .
        
        
        That is:
        
        .. code-block:: text
        
          \\*this - this->GetProjection(b)
        
        
        
        Parameters
        ----------
        b : Vec3h
        
        
        """
    @staticmethod
    def GetCross(*args, **kwargs):
        ...
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> GfHalf
        
        
        Length.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Vec3h
        
        
        Parameters
        ----------
        eps : GfHalf
        
        
        """
    @staticmethod
    def GetProjection(*args, **kwargs):
        """
        
        GetProjection(v) -> Vec3h
        
        
        Returns the projection of ``this`` onto ``v`` .
        
        
        That is:
        
        .. code-block:: text
        
          v \\* (\\*this \\* v)
        
        
        
        Parameters
        ----------
        v : Vec3h
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> GfHalf
        
        
        Normalizes the vector in place to unit length, returning the length
        before normalization.
        
        
        If the length of the vector is smaller than ``eps`` , then the vector
        is set to vector/ ``eps`` . The original length of the vector is
        returned. See also GfNormalize() .
        
        
        Parameters
        ----------
        eps : GfHalf
        
        
        """
    @staticmethod
    def OrthogonalizeBasis(*args, **kwargs):
        """
        
        **classmethod** OrthogonalizeBasis(tx, ty, tz, normalize, eps) -> bool
        
        
        Orthogonalize and optionally normalize a set of basis vectors.
        
        
        This uses an iterative method that is very stable even when the
        vectors are far from orthogonal (close to colinear). The number of
        iterations and thus the computation time does increase as the vectors
        become close to colinear, however. Returns a bool specifying whether
        the solution converged after a number of iterations. If it did not
        converge, the returned vectors will be as close as possible to
        orthogonal within the iteration limit. Colinear vectors will be
        unaltered, and the method will return false.
        
        
        Parameters
        ----------
        tx : Vec3h
        
        ty : Vec3h
        
        tz : Vec3h
        
        normalize : bool
        
        eps : float
        
        
        """
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec3h
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec3h
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
    @staticmethod
    def ZAxis(*args, **kwargs):
        """
        
        **classmethod** ZAxis() -> Vec3h
        
        
        Create a unit vector along the Z-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : GfHalf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1, s2)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : GfHalf
        
        s1 : GfHalf
        
        s2 : GfHalf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfVec3d.
        
        
        Parameters
        ----------
        other : Vec3d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfVec3f.
        
        
        Parameters
        ----------
        other : Vec3f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec3i.
        
        
        Parameters
        ----------
        other : Vec3i
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 3
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec3i
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 3.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec3i
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec3i
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
    @staticmethod
    def ZAxis(*args, **kwargs):
        """
        
        **classmethod** ZAxis() -> Vec3i
        
        
        Create a unit vector along the Z-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1, s2)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : int
        
        s1 : int
        
        s2 : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 4
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec4d
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 4.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetComplement(*args, **kwargs):
        """
        
        GetComplement(b) -> Vec4d
        
        
        Returns the orthogonal complement of ``this->GetProjection(b)`` .
        
        
        That is:
        
        .. code-block:: text
        
          \\*this - this->GetProjection(b)
        
        
        
        Parameters
        ----------
        b : Vec4d
        
        
        """
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> float
        
        
        Length.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Vec4d
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def GetProjection(*args, **kwargs):
        """
        
        GetProjection(v) -> Vec4d
        
        
        Returns the projection of ``this`` onto ``v`` .
        
        
        That is:
        
        .. code-block:: text
        
          v \\* (\\*this \\* v)
        
        
        
        Parameters
        ----------
        v : Vec4d
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> float
        
        
        Normalizes the vector in place to unit length, returning the length
        before normalization.
        
        
        If the length of the vector is smaller than ``eps`` , then the vector
        is set to vector/ ``eps`` . The original length of the vector is
        returned. See also GfNormalize() .
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def WAxis(*args, **kwargs):
        """
        
        **classmethod** WAxis() -> Vec4d
        
        
        Create a unit vector along the W-axis.
        
        
        
        """
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec4d
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec4d
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
    @staticmethod
    def ZAxis(*args, **kwargs):
        """
        
        **classmethod** ZAxis() -> Vec4d
        
        
        Create a unit vector along the Z-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1, s2, s3)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : float
        
        s1 : float
        
        s2 : float
        
        s3 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec4f.
        
        
        Parameters
        ----------
        other : Vec4f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec4h.
        
        
        Parameters
        ----------
        other : Vec4h
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec4i.
        
        
        Parameters
        ----------
        other : Vec4i
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 4
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec4f
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 4.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetComplement(*args, **kwargs):
        """
        
        GetComplement(b) -> Vec4f
        
        
        Returns the orthogonal complement of ``this->GetProjection(b)`` .
        
        
        That is:
        
        .. code-block:: text
        
          \\*this - this->GetProjection(b)
        
        
        
        Parameters
        ----------
        b : Vec4f
        
        
        """
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> float
        
        
        Length.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Vec4f
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def GetProjection(*args, **kwargs):
        """
        
        GetProjection(v) -> Vec4f
        
        
        Returns the projection of ``this`` onto ``v`` .
        
        
        That is:
        
        .. code-block:: text
        
          v \\* (\\*this \\* v)
        
        
        
        Parameters
        ----------
        v : Vec4f
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> float
        
        
        Normalizes the vector in place to unit length, returning the length
        before normalization.
        
        
        If the length of the vector is smaller than ``eps`` , then the vector
        is set to vector/ ``eps`` . The original length of the vector is
        returned. See also GfNormalize() .
        
        
        Parameters
        ----------
        eps : float
        
        
        """
    @staticmethod
    def WAxis(*args, **kwargs):
        """
        
        **classmethod** WAxis() -> Vec4f
        
        
        Create a unit vector along the W-axis.
        
        
        
        """
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec4f
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec4f
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
    @staticmethod
    def ZAxis(*args, **kwargs):
        """
        
        **classmethod** ZAxis() -> Vec4f
        
        
        Create a unit vector along the Z-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1, s2, s3)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : float
        
        s1 : float
        
        s2 : float
        
        s3 : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfVec4d.
        
        
        Parameters
        ----------
        other : Vec4d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec4h.
        
        
        Parameters
        ----------
        other : Vec4h
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec4i.
        
        
        Parameters
        ----------
        other : Vec4i
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 4
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec4h
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 4.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetComplement(*args, **kwargs):
        """
        
        GetComplement(b) -> Vec4h
        
        
        Returns the orthogonal complement of ``this->GetProjection(b)`` .
        
        
        That is:
        
        .. code-block:: text
        
          \\*this - this->GetProjection(b)
        
        
        
        Parameters
        ----------
        b : Vec4h
        
        
        """
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def GetLength(*args, **kwargs):
        """
        
        GetLength() -> GfHalf
        
        
        Length.
        
        
        
        """
    @staticmethod
    def GetNormalized(*args, **kwargs):
        """
        
        GetNormalized(eps) -> Vec4h
        
        
        Parameters
        ----------
        eps : GfHalf
        
        
        """
    @staticmethod
    def GetProjection(*args, **kwargs):
        """
        
        GetProjection(v) -> Vec4h
        
        
        Returns the projection of ``this`` onto ``v`` .
        
        
        That is:
        
        .. code-block:: text
        
          v \\* (\\*this \\* v)
        
        
        
        Parameters
        ----------
        v : Vec4h
        
        
        """
    @staticmethod
    def Normalize(*args, **kwargs):
        """
        
        Normalize(eps) -> GfHalf
        
        
        Normalizes the vector in place to unit length, returning the length
        before normalization.
        
        
        If the length of the vector is smaller than ``eps`` , then the vector
        is set to vector/ ``eps`` . The original length of the vector is
        returned. See also GfNormalize() .
        
        
        Parameters
        ----------
        eps : GfHalf
        
        
        """
    @staticmethod
    def WAxis(*args, **kwargs):
        """
        
        **classmethod** WAxis() -> Vec4h
        
        
        Create a unit vector along the W-axis.
        
        
        
        """
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec4h
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec4h
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
    @staticmethod
    def ZAxis(*args, **kwargs):
        """
        
        **classmethod** ZAxis() -> Vec4h
        
        
        Create a unit vector along the Z-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : GfHalf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1, s2, s3)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : GfHalf
        
        s1 : GfHalf
        
        s2 : GfHalf
        
        s3 : GfHalf
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfVec4d.
        
        
        Parameters
        ----------
        other : Vec4d
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct from GfVec4f.
        
        
        Parameters
        ----------
        other : Vec4f
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Implicitly convert from GfVec4i.
        
        
        Parameters
        ----------
        other : Vec4i
        
        
        """
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
    """
    """
    __isGfVec: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    dimension: typing.ClassVar[int] = 4
    @staticmethod
    def Axis(*args, **kwargs):
        """
        
        **classmethod** Axis(i) -> Vec4i
        
        
        Create a unit vector along the i-th axis, zero-based.
        
        
        Return the zero vector if ``i`` is greater than or equal to 4.
        
        
        Parameters
        ----------
        i : int
        
        
        """
    @staticmethod
    def GetDot(*args, **kwargs):
        ...
    @staticmethod
    def WAxis(*args, **kwargs):
        """
        
        **classmethod** WAxis() -> Vec4i
        
        
        Create a unit vector along the W-axis.
        
        
        
        """
    @staticmethod
    def XAxis(*args, **kwargs):
        """
        
        **classmethod** XAxis() -> Vec4i
        
        
        Create a unit vector along the X-axis.
        
        
        
        """
    @staticmethod
    def YAxis(*args, **kwargs):
        """
        
        **classmethod** YAxis() -> Vec4i
        
        
        Create a unit vector along the Y-axis.
        
        
        
        """
    @staticmethod
    def ZAxis(*args, **kwargs):
        """
        
        **classmethod** ZAxis() -> Vec4i
        
        
        Create a unit vector along the Z-axis.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor does no initialization.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Initialize all elements to a single value.
        
        
        Parameters
        ----------
        value : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(s0, s1, s2, s3)
        
        
        Initialize all elements with explicit arguments.
        
        
        Parameters
        ----------
        s0 : int
        
        s1 : int
        
        s2 : int
        
        s3 : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(p)
        
        
        Construct with pointer to values.
        
        
        Parameters
        ----------
        p : Scl
        
        
        """
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
