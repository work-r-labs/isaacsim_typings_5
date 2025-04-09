"""

Utilities to help image common geometry.
"""
from __future__ import annotations
import typing
__all__ = ['CapsuleMeshGenerator', 'ConeMeshGenerator', 'CuboidMeshGenerator', 'CylinderMeshGenerator', 'SphereMeshGenerator']
class CapsuleMeshGenerator(Boost.Python.instance):
    """
    
    This class provides an implementation for generating topology and
    point positions on a capsule.
    
    
    The simplest form takes a radius and height and is a cylinder capped
    by two hemispheres that is centered at the origin. The generated
    capsule is made up of circular cross-sections in the XY plane. Each
    cross-section has numRadial segments. Successive cross-sections for
    each of the hemispheres are generated at numCapAxial locations along
    the Z and -Z axes respectively. The height is aligned with the Z axis
    and represents the height of just the cylindrical portion.
    
    An optional transform may be provided to GeneratePoints to orient the
    capsule as necessary (e.g., whose height is along the Y axis).
    
    An additional overload of GeneratePoints is provided to specify
    different radii and heights for the bottom and top caps, as well as
    the sweep angle for the capsule about the +Z axis. When the sweep is
    less than 360 degrees, the generated geometry is not closed.
    
    Usage:
    
    .. code-block:: text
    
      const size_t numRadial = 4, numCapAxial = 4;
      const size_t numPoints =
          GeomUtilCapsuleMeshGenerator::ComputeNumPoints(numRadial, numCapAxial);
      const float radius = 1, height = 2;
      
      MyPointContainer<GfVec3f> points(numPoints);
      
      GeomUtilCapsuleMeshGenerator::GeneratePoints(
          points.begin(), numRadial, numCapAxial, radius, height);
    
    
    """
    minNumCapAxial: typing.ClassVar[int] = 1
    minNumRadial: typing.ClassVar[int] = 3
    @staticmethod
    def ComputeNumPoints(*args, **kwargs):
        """
        
        **classmethod** ComputeNumPoints(numRadial, numCapAxial, closedSweep) -> int
        
        
        Parameters
        ----------
        numRadial : int
        
        numCapAxial : int
        
        closedSweep : bool
        
        
        """
    @staticmethod
    def GeneratePoints(*args, **kwargs):
        """
        
        **classmethod** GeneratePoints(iter, numRadial, numCapAxial, radius, height, framePtr) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        numRadial : int
        
        numCapAxial : int
        
        radius : ScalarType
        
        height : ScalarType
        
        framePtr : Matrix4d
        
        
        
        ----------------------------------------------------------------------
        
        GeneratePoints(iter, numRadial, numCapAxial, bottomRadius, topRadius, height, bottomCapHeight, topCapHeight, sweepDegrees, framePtr) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        numRadial : int
        
        numCapAxial : int
        
        bottomRadius : ScalarType
        
        topRadius : ScalarType
        
        height : ScalarType
        
        bottomCapHeight : ScalarType
        
        topCapHeight : ScalarType
        
        sweepDegrees : ScalarType
        
        framePtr : Matrix4d
        
        
        
        ----------------------------------------------------------------------
        
        GeneratePoints(iter, arg2) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        arg2 : ...
        
        
        """
    @staticmethod
    def GenerateTopology(*args, **kwargs):
        """
        
        **classmethod** GenerateTopology(numRadial, numCapAxial, closedSweep) -> MeshTopology
        
        
        Parameters
        ----------
        numRadial : int
        
        numCapAxial : int
        
        closedSweep : bool
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ConeMeshGenerator(Boost.Python.instance):
    """
    
    This class provides an implementation for generating topology and
    point positions on a cone of a given radius and height.
    
    
    The cone is made up of circular cross-sections in the XY plane and is
    centered at the origin. Each cross-section has numRadial segments. The
    height is aligned with the Z axis, with the base of the object at Z =
    \\-h/2 and apex at Z = h/2.
    
    An optional transform may be provided to GeneratePoints to orient the
    cone as necessary (e.g., whose height is along the Y axis).
    
    An additional overload of GeneratePoints is provided to specify the
    sweep angle for the cone about the +Z axis. When the sweep is less
    than 360 degrees, the generated geometry is not closed.
    
    Usage:
    
    .. code-block:: text
    
      const size_t numRadial = 8;
      const size_t numPoints =
          GeomUtilConeMeshGenerator::ComputeNumPoints(numRadial);
      const float radius = 1, height = 2;
      
      MyPointContainer<GfVec3f> points(numPoints);
      
      GeomUtilConeMeshGenerator::GeneratePoints(
          points.begin(), numRadial, radius, height);
    
    
    """
    minNumRadial: typing.ClassVar[int] = 3
    @staticmethod
    def ComputeNumPoints(*args, **kwargs):
        """
        
        **classmethod** ComputeNumPoints(numRadial, closedSweep) -> int
        
        
        Parameters
        ----------
        numRadial : int
        
        closedSweep : bool
        
        
        """
    @staticmethod
    def GeneratePoints(*args, **kwargs):
        """
        
        **classmethod** GeneratePoints(iter, numRadial, radius, height, framePtr) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        numRadial : int
        
        radius : ScalarType
        
        height : ScalarType
        
        framePtr : Matrix4d
        
        
        
        ----------------------------------------------------------------------
        
        GeneratePoints(iter, numRadial, radius, height, sweepDegrees, framePtr) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        numRadial : int
        
        radius : ScalarType
        
        height : ScalarType
        
        sweepDegrees : ScalarType
        
        framePtr : Matrix4d
        
        
        
        ----------------------------------------------------------------------
        
        GeneratePoints(iter, arg2) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        arg2 : ...
        
        
        """
    @staticmethod
    def GenerateTopology(*args, **kwargs):
        """
        
        **classmethod** GenerateTopology(numRadial, closedSweep) -> MeshTopology
        
        
        Parameters
        ----------
        numRadial : int
        
        closedSweep : bool
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class CuboidMeshGenerator(Boost.Python.instance):
    """
    
    This class provides an implementation for generating topology and
    point positions on a rectangular cuboid given the dimensions along the
    X, Y and Z axes.
    
    
    The generated cuboid is centered at the origin.
    
    An optional transform may be provided to GeneratePoints to orient the
    cuboid as necessary.
    
    Usage:
    
    .. code-block:: text
    
      const size_t numPoints =
          GeomUtilCuboidMeshGenerator::ComputeNumPoints();
      const float l = 5, b = 4, h = 3;
      
      MyPointContainer<GfVec3f> points(numPoints);
      
      GeomUtilCuboidMeshGenerator::GeneratePoints(
          points.begin(), l, b, h);
    
    
    """
    @staticmethod
    def ComputeNumPoints(*args, **kwargs):
        """
        
        **classmethod** ComputeNumPoints() -> int
        
        
        
        """
    @staticmethod
    def GeneratePoints(*args, **kwargs):
        """
        
        **classmethod** GeneratePoints(iter, xLength, yLength, zLength, framePtr) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        xLength : ScalarType
        
        yLength : ScalarType
        
        zLength : ScalarType
        
        framePtr : Matrix4d
        
        
        
        ----------------------------------------------------------------------
        
        GeneratePoints(iter, arg2) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        arg2 : ...
        
        
        """
    @staticmethod
    def GenerateTopology(*args, **kwargs):
        """
        
        **classmethod** GenerateTopology() -> MeshTopology
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class CylinderMeshGenerator(Boost.Python.instance):
    """
    
    This class provides an implementation for generating topology and
    point positions on a cylinder with a given radius and height.
    
    
    The cylinder is made up of circular cross-sections in the XY plane and
    is centered at the origin. Each cross-section has numRadial segments.
    The height is aligned with the Z axis, with the base at Z = -h/2.
    
    An optional transform may be provided to GeneratePoints to orient the
    cone as necessary (e.g., whose height is along the Y axis).
    
    An additional overload of GeneratePoints is provided to specify
    different radii for the bottom and top discs of the cylinder and a
    sweep angle for cylinder about the +Z axis. When the sweep is less
    than 360 degrees, the generated geometry is not closed.
    
    Setting one radius to 0 in order to get a cone is inefficient and
    could result in artifacts. Clients should use
    GeomUtilConeMeshGenerator instead. Usage:
    
    .. code-block:: text
    
      const size_t numRadial = 8;
      const size_t numPoints =
          GeomUtilCylinderMeshGenerator::ComputeNumPoints(numRadial);
      const float radius = 1, height = 2;
      
      MyPointContainer<GfVec3f> points(numPoints);
      
      GeomUtilCylinderMeshGenerator::GeneratePoints(
          points.begin(), numRadial, radius, height);
    
    
    """
    minNumRadial: typing.ClassVar[int] = 3
    @staticmethod
    def ComputeNumPoints(*args, **kwargs):
        """
        
        **classmethod** ComputeNumPoints(numRadial, closedSweep) -> int
        
        
        Parameters
        ----------
        numRadial : int
        
        closedSweep : bool
        
        
        """
    @staticmethod
    def GeneratePoints(*args, **kwargs):
        """
        
        **classmethod** GeneratePoints(iter, numRadial, radius, height, framePtr) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        numRadial : int
        
        radius : ScalarType
        
        height : ScalarType
        
        framePtr : Matrix4d
        
        
        
        ----------------------------------------------------------------------
        
        GeneratePoints(iter, numRadial, bottomRadius, topRadius, height, sweepDegrees, framePtr) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        numRadial : int
        
        bottomRadius : ScalarType
        
        topRadius : ScalarType
        
        height : ScalarType
        
        sweepDegrees : ScalarType
        
        framePtr : Matrix4d
        
        
        
        ----------------------------------------------------------------------
        
        GeneratePoints(iter, arg2) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        arg2 : ...
        
        
        """
    @staticmethod
    def GenerateTopology(*args, **kwargs):
        """
        
        **classmethod** GenerateTopology(numRadial, closedSweep) -> MeshTopology
        
        
        Parameters
        ----------
        numRadial : int
        
        closedSweep : bool
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class SphereMeshGenerator(Boost.Python.instance):
    """
    
    This class provides an implementation for generating topology and
    point positions on a sphere with a given radius.
    
    
    The sphere is made up of circular cross-sections in the XY plane and
    is centered at the origin. Each cross-section has numRadial segments.
    Successive cross-sections are generated at numAxial locations along
    the Z axis, with the bottom of the sphere at Z = -r and top at Z = r.
    
    An optional transform may be provided to GeneratePoints to orient the
    sphere as necessary (e.g., cross-sections in the YZ plane).
    
    An additional overload of GeneratePoints is provided to specify a
    sweep angle for the sphere about the +Z axis. When the sweep is less
    than 360 degrees, the generated geometry is not closed.
    
    Usage:
    
    .. code-block:: text
    
      const size_t numRadial = 4, numAxial = 4;
      const size_t numPoints =
          GeomUtilSphereMeshGenerator::ComputeNumPoints(numRadial, numAxial);
      const float radius = 5;
      
      MyPointContainer<GfVec3f> points(numPoints);
      
      GeomUtilSphereMeshGenerator::GeneratePoints(
          points.begin(), numRadial, numAxial, radius);
    
    
    """
    minNumAxial: typing.ClassVar[int] = 2
    minNumRadial: typing.ClassVar[int] = 3
    @staticmethod
    def ComputeNumPoints(*args, **kwargs):
        """
        
        **classmethod** ComputeNumPoints(numRadial, numAxial, closedSweep) -> int
        
        
        Parameters
        ----------
        numRadial : int
        
        numAxial : int
        
        closedSweep : bool
        
        
        """
    @staticmethod
    def GeneratePoints(*args, **kwargs):
        """
        
        **classmethod** GeneratePoints(iter, numRadial, numAxial, radius, framePtr) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        numRadial : int
        
        numAxial : int
        
        radius : ScalarType
        
        framePtr : Matrix4d
        
        
        
        ----------------------------------------------------------------------
        
        GeneratePoints(iter, numRadial, numAxial, radius, sweepDegrees, framePtr) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        numRadial : int
        
        numAxial : int
        
        radius : ScalarType
        
        sweepDegrees : ScalarType
        
        framePtr : Matrix4d
        
        
        
        ----------------------------------------------------------------------
        
        GeneratePoints(iter, arg2) -> None
        
        
        Parameters
        ----------
        iter : PointIterType
        
        arg2 : ...
        
        
        """
    @staticmethod
    def GenerateTopology(*args, **kwargs):
        """
        
        **classmethod** GenerateTopology(numRadial, numAxial, closedSweep) -> MeshTopology
        
        
        Parameters
        ----------
        numRadial : int
        
        numAxial : int
        
        closedSweep : bool
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'geomUtil'
