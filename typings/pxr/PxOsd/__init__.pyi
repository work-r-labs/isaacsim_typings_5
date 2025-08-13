"""

Pixar OSD implementation.
"""
from __future__ import annotations
import pxr.Tf
import typing
__all__: list[str] = ['MeshTopology', 'MeshTopologyValidation', 'OpenSubdivTokens', 'SubdivTags']
class MeshTopology(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 400
    @staticmethod
    def ComputeHash(*args, **kwargs):
        ...
    @staticmethod
    def GetFaceVertexCounts(*args, **kwargs):
        ...
    @staticmethod
    def GetFaceVertexIndices(*args, **kwargs):
        ...
    @staticmethod
    def GetHoleIndices(*args, **kwargs):
        ...
    @staticmethod
    def GetOrientation(*args, **kwargs):
        ...
    @staticmethod
    def GetScheme(*args, **kwargs):
        ...
    @staticmethod
    def GetSubdivTags(*args, **kwargs):
        ...
    @staticmethod
    def Validate(*args, **kwargs):
        ...
    @staticmethod
    def WithHoleIndices(*args, **kwargs):
        ...
    @staticmethod
    def WithScheme(*args, **kwargs):
        ...
    @staticmethod
    def WithSubdivTags(*args, **kwargs):
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
class MeshTopologyValidation(Boost.Python.instance):
    class Code(pxr.Tf.Tf_PyEnumWrapper):
        InvalidCornerIndicesElement: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidCornerIndicesElement
        InvalidCornerWeightsSize: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidCornerWeightsSize
        InvalidCreaseIndicesElement: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidCreaseIndicesElement
        InvalidCreaseIndicesSize: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidCreaseIndicesSize
        InvalidCreaseLengthElement: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidCreaseLengthElement
        InvalidCreaseMethod: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidCreaseMethod
        InvalidCreaseWeightsSize: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidCreaseWeightsSize
        InvalidFaceVaryingInterpolationRule: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidFaceVaryingInterpolationRule
        InvalidFaceVertexCountsElement: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidFaceVertexCountsElement
        InvalidFaceVertexIndicesElement: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidFaceVertexIndicesElement
        InvalidFaceVertexIndicesSize: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidFaceVertexIndicesSize
        InvalidOrientation: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidOrientation
        InvalidScheme: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidScheme
        InvalidTriangleSubdivision: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidTriangleSubdivision
        InvalidVertexInterpolationRule: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.InvalidVertexInterpolationRule
        NegativeCornerWeights: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.NegativeCornerWeights
        NegativeCreaseWeights: typing.ClassVar[Code]  # value = PxOsd.MeshTopologyValidation.Code.NegativeCreaseWeights
        _baseName: typing.ClassVar[str] = 'MeshTopologyValidation.Code'
        allValues: typing.ClassVar[tuple]  # value = (PxOsd.MeshTopologyValidation.Code.InvalidScheme, PxOsd.MeshTopologyValidation.Code.InvalidOrientation, PxOsd.MeshTopologyValidation.Code.InvalidTriangleSubdivision, PxOsd.MeshTopologyValidation.Code.InvalidVertexInterpolationRule, PxOsd.MeshTopologyValidation.Code.InvalidFaceVaryingInterpolationRule, PxOsd.MeshTopologyValidation.Code.InvalidCreaseMethod, PxOsd.MeshTopologyValidation.Code.InvalidCreaseLengthElement, PxOsd.MeshTopologyValidation.Code.InvalidCreaseIndicesSize, PxOsd.MeshTopologyValidation.Code.InvalidCreaseIndicesElement, PxOsd.MeshTopologyValidation.Code.InvalidCreaseWeightsSize, PxOsd.MeshTopologyValidation.Code.NegativeCreaseWeights, PxOsd.MeshTopologyValidation.Code.InvalidCornerIndicesElement, PxOsd.MeshTopologyValidation.Code.NegativeCornerWeights, PxOsd.MeshTopologyValidation.Code.InvalidCornerWeightsSize, PxOsd.MeshTopologyValidation.Code.InvalidFaceVertexCountsElement, PxOsd.MeshTopologyValidation.Code.InvalidFaceVertexIndicesElement, PxOsd.MeshTopologyValidation.Code.InvalidFaceVertexIndicesSize)
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
    class Invalidation(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @property
        def code(*args, **kwargs):
            ...
        @code.setter
        def code(*args, **kwargs):
            ...
        @property
        def message(*args, **kwargs):
            ...
        @message.setter
        def message(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class OpenSubdivTokens(Boost.Python.instance):
    all: typing.ClassVar[str] = 'all'
    bilinear: typing.ClassVar[str] = 'bilinear'
    boundaries: typing.ClassVar[str] = 'boundaries'
    catmullClark: typing.ClassVar[str] = 'catmullClark'
    chaikin: typing.ClassVar[str] = 'chaikin'
    cornersOnly: typing.ClassVar[str] = 'cornersOnly'
    cornersPlus1: typing.ClassVar[str] = 'cornersPlus1'
    cornersPlus2: typing.ClassVar[str] = 'cornersPlus2'
    edgeAndCorner: typing.ClassVar[str] = 'edgeAndCorner'
    edgeOnly: typing.ClassVar[str] = 'edgeOnly'
    leftHanded: typing.ClassVar[str] = 'leftHanded'
    loop: typing.ClassVar[str] = 'loop'
    none: typing.ClassVar[str] = 'none'
    rightHanded: typing.ClassVar[str] = 'rightHanded'
    smooth: typing.ClassVar[str] = 'smooth'
    uniform: typing.ClassVar[str] = 'uniform'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class SubdivTags(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 256
    @staticmethod
    def ComputeHash(*args, **kwargs):
        ...
    @staticmethod
    def GetCornerIndices(*args, **kwargs):
        ...
    @staticmethod
    def GetCornerWeights(*args, **kwargs):
        ...
    @staticmethod
    def GetCreaseIndices(*args, **kwargs):
        ...
    @staticmethod
    def GetCreaseLengths(*args, **kwargs):
        ...
    @staticmethod
    def GetCreaseMethod(*args, **kwargs):
        ...
    @staticmethod
    def GetCreaseWeights(*args, **kwargs):
        ...
    @staticmethod
    def GetFaceVaryingInterpolationRule(*args, **kwargs):
        ...
    @staticmethod
    def GetTriangleSubdivision(*args, **kwargs):
        ...
    @staticmethod
    def GetVertexInterpolationRule(*args, **kwargs):
        ...
    @staticmethod
    def SetCornerIndices(*args, **kwargs):
        ...
    @staticmethod
    def SetCornerWeights(*args, **kwargs):
        ...
    @staticmethod
    def SetCreaseIndices(*args, **kwargs):
        ...
    @staticmethod
    def SetCreaseLengths(*args, **kwargs):
        ...
    @staticmethod
    def SetCreaseMethod(*args, **kwargs):
        ...
    @staticmethod
    def SetCreaseWeights(*args, **kwargs):
        ...
    @staticmethod
    def SetFaceVaryingInterpolationRule(*args, **kwargs):
        ...
    @staticmethod
    def SetTriangleSubdivision(*args, **kwargs):
        ...
    @staticmethod
    def SetVertexInterpolationRule(*args, **kwargs):
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
__MFB_FULL_PACKAGE_NAME: str = 'pxOsd'
