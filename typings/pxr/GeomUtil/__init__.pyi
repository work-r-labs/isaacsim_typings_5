"""

Utilities to help image common geometry.
"""
from __future__ import annotations
import typing
__all__: list[str] = ['CapsuleMeshGenerator', 'ConeMeshGenerator', 'CuboidMeshGenerator', 'CylinderMeshGenerator', 'SphereMeshGenerator']
class CapsuleMeshGenerator(Boost.Python.instance):
    minNumCapAxial: typing.ClassVar[int] = 1
    minNumRadial: typing.ClassVar[int] = 3
    @staticmethod
    def ComputeNumPoints(*args, **kwargs):
        ...
    @staticmethod
    def GeneratePoints(*args, **kwargs):
        ...
    @staticmethod
    def GenerateTopology(*args, **kwargs):
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
class ConeMeshGenerator(Boost.Python.instance):
    minNumRadial: typing.ClassVar[int] = 3
    @staticmethod
    def ComputeNumPoints(*args, **kwargs):
        ...
    @staticmethod
    def GeneratePoints(*args, **kwargs):
        ...
    @staticmethod
    def GenerateTopology(*args, **kwargs):
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
class CuboidMeshGenerator(Boost.Python.instance):
    @staticmethod
    def ComputeNumPoints(*args, **kwargs):
        ...
    @staticmethod
    def GeneratePoints(*args, **kwargs):
        ...
    @staticmethod
    def GenerateTopology(*args, **kwargs):
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
class CylinderMeshGenerator(Boost.Python.instance):
    minNumRadial: typing.ClassVar[int] = 3
    @staticmethod
    def ComputeNumPoints(*args, **kwargs):
        ...
    @staticmethod
    def GeneratePoints(*args, **kwargs):
        ...
    @staticmethod
    def GenerateTopology(*args, **kwargs):
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
class SphereMeshGenerator(Boost.Python.instance):
    minNumAxial: typing.ClassVar[int] = 2
    minNumRadial: typing.ClassVar[int] = 3
    @staticmethod
    def ComputeNumPoints(*args, **kwargs):
        ...
    @staticmethod
    def GeneratePoints(*args, **kwargs):
        ...
    @staticmethod
    def GenerateTopology(*args, **kwargs):
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
__MFB_FULL_PACKAGE_NAME: str = 'geomUtil'
