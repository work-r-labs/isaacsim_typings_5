"""

Pixar OSD implementation.
"""
from __future__ import annotations
import pxr.Tf
import typing
__all__ = ['MeshTopology', 'MeshTopologyValidation', 'OpenSubdivTokens', 'SubdivTags']
class MeshTopology(Boost.Python.instance):
    """
    
    Topology data for meshes.
    
    Once constructed, this class is immutable (except when assigned or
    moved).
    
    To make changing certain properties easier, several methods are
    provided. WithScheme, WithHoleIndices, and WithSubdivTags will return
    copies of the object with certain specific properites changed.
    
    .. code-block:: text
    
      PxOsdMeshTopology otherTopology =
          originalTopology.WithScheme(PxOsdOpenSubdivTokens->catmullClark);
      TF_VERIFY(otherTopology.GetScheme() ==
                PxOsdOpenSubdivTokens->catmullClark);
      TF_VERIFY(otherTopology.GetOrientation() ==
                originalTopology.GetOrientation());
      TF_VERIFY(otherTopology.GetSubdivTags() ==
                originalTopology.GetSubdivTags());
      TF_VERIFY(otherTopology.GetFaceVertexCounts() ==
                originalTopology.GetFaceVertexCounts());
      TF_VERIFY(otherTopology.GetFaceVertexIndices() ==
                originalTopology.GetFaceVertexIndices());
    
    The cost of copying should be mitigated by the copy semantics of
    VtArray and TfToken.
    
    """
    __instance_size__: typing.ClassVar[int] = 392
    @staticmethod
    def ComputeHash(*args, **kwargs):
        """
        
        ComputeHash() -> ID
        
        
        Returns the hash value of this topology to be used for instancing.
        
        
        
        """
    @staticmethod
    def GetFaceVertexCounts(*args, **kwargs):
        """
        
        GetFaceVertexCounts() -> IntArray
        
        
        Returns face vertex counts.
        
        
        
        """
    @staticmethod
    def GetFaceVertexIndices(*args, **kwargs):
        """
        
        GetFaceVertexIndices() -> IntArray
        
        
        Returns face vertex indices.
        
        
        
        """
    @staticmethod
    def GetHoleIndices(*args, **kwargs):
        """
        
        GetHoleIndices() -> IntArray
        
        
        
        """
    @staticmethod
    def GetOrientation(*args, **kwargs):
        """
        
        GetOrientation() -> str
        
        
        Returns orientation.
        
        
        
        """
    @staticmethod
    def GetScheme(*args, **kwargs):
        """
        
        GetScheme() -> str
        
        
        Returns the subdivision scheme.
        
        
        
        """
    @staticmethod
    def GetSubdivTags(*args, **kwargs):
        """
        
        GetSubdivTags() -> SubdivTags
        
        
        Returns subdivision tags.
        
        
        
        """
    @staticmethod
    def Validate(*args, **kwargs):
        """
        
        Validate() -> MeshTopologyValidation
        
        
        Returns a validation object which is empty if the topology is valid.
        
        
        
        .. code-block:: text
        
          // Validation with minimal reporting
          if (!topology.Validate()) TF_CODING_ERROR("Invalid topology.");
        
        .. code-block:: text
        
          {
             PxOsdMeshTopologyValidation validation = topology.Validate();
             if (!validation){
                 for (auto const &  elem: validation){
                      TF_WARN(elem.message);
                 }
             }
          }
        
        Internally caches the result of the validation if the topology is
        valid
        
        
        
        """
    @staticmethod
    def WithHoleIndices(*args, **kwargs):
        """
        
        WithHoleIndices(holeIndices) -> MeshTopology
        
        
        Return a copy of the topology, changing only the hole indices.
        
        
        Parameters
        ----------
        holeIndices : IntArray
        
        
        """
    @staticmethod
    def WithScheme(*args, **kwargs):
        """
        
        WithScheme(scheme) -> MeshTopology
        
        
        Return a copy of the topology, changing only the scheme.
        
        
        Valid values include: catmullClark, loop, bilinear.
        
        Note that the token"catmark"is also supported for backward
        compatibility, but has been deprecated.
        
        
        Parameters
        ----------
        scheme : str
        
        
        """
    @staticmethod
    def WithSubdivTags(*args, **kwargs):
        """
        
        WithSubdivTags(tags) -> MeshTopology
        
        
        Return a copy of the topology, changing only the subdiv tags.
        
        
        Parameters
        ----------
        tags : SubdivTags
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : MeshTopology
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : MeshTopology
        
        
        
        ----------------------------------------------------------------------
        
        __init__(scheme, orientation, faceVertexCounts, faceVertexIndices)
        
        
        Construct a topology without holes or subdiv tags.
        
        
        Parameters
        ----------
        scheme : str
        
        orientation : str
        
        faceVertexCounts : IntArray
        
        faceVertexIndices : IntArray
        
        
        
        ----------------------------------------------------------------------
        
        __init__(scheme, orientation, faceVertexCounts, faceVertexIndices, holeIndices)
        
        
        Construct a topology with holes.
        
        
        Parameters
        ----------
        scheme : str
        
        orientation : str
        
        faceVertexCounts : IntArray
        
        faceVertexIndices : IntArray
        
        holeIndices : IntArray
        
        
        
        ----------------------------------------------------------------------
        
        __init__(scheme, orientation, faceVertexCounts, faceVertexIndices, holeIndices, subdivTags)
        
        
        Construct a topology with holes and subdiv tags.
        
        
        Parameters
        ----------
        scheme : str
        
        orientation : str
        
        faceVertexCounts : IntArray
        
        faceVertexIndices : IntArray
        
        holeIndices : IntArray
        
        subdivTags : SubdivTags
        
        
        
        ----------------------------------------------------------------------
        
        __init__(scheme, orientation, faceVertexCounts, faceVertexIndices, subdivTags)
        
        
        Construct a topology with subdiv tags.
        
        
        Parameters
        ----------
        scheme : str
        
        orientation : str
        
        faceVertexCounts : IntArray
        
        faceVertexIndices : IntArray
        
        subdivTags : SubdivTags
        
        
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
class MeshTopologyValidation(Boost.Python.instance):
    """
    
    Utility to help validate an OpenSubdiv Mesh topology.
    
    
    This class is created by PxOsdMeshTopology 's Validate method.
    
    Internally, this will avoid dynamic allocations as long as the
    topology is valid (currently using std::unique_ptr but targeting
    std::optional for C++17).
    
    This class does a set of basic validation tests on the topology of a
    mesh. This set of tests isn't necessarily complete. There are other
    cases like invalid primvar size that this will not check for.
    
    Topology is considered valid if it passes a series of checks
    enumerated by the Code class enum.
    
    \\warn This doesn't currently validate that the topology of crease
    indices match valid edges.
    
    This class is convertable to bool and converts to true if the the
    topology is valid and false if any invalidations were found. That is
    to say, a conversion to true implies an empty invalidation vector and
    false implies a non-empty invalidation vector.
    
    """
    class Code(pxr.Tf.Tf_PyEnumWrapper):
        """
        
        Codes for various invalid states for PxOsdMeshTopology.
        
        """
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
    __instance_size__: typing.ClassVar[int] = 24
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : MeshTopology
        
        
        
        ----------------------------------------------------------------------
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : MeshTopologyValidation
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Parameters
        ----------
        other : MeshTopologyValidation
        
        
        """
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
    """
    
    Tags for non-hierarchial subdiv surfaces.
    
    """
    __instance_size__: typing.ClassVar[int] = 248
    @staticmethod
    def ComputeHash(*args, **kwargs):
        """
        
        ComputeHash() -> ID
        
        
        Returns the hash value of this topology to be used for instancing.
        
        
        
        """
    @staticmethod
    def GetCornerIndices(*args, **kwargs):
        """
        
        GetCornerIndices() -> IntArray
        
        
        Returns the edge corner indices.
        
        
        
        """
    @staticmethod
    def GetCornerWeights(*args, **kwargs):
        """
        
        GetCornerWeights() -> FloatArray
        
        
        Returns the edge corner weights.
        
        
        
        """
    @staticmethod
    def GetCreaseIndices(*args, **kwargs):
        """
        
        GetCreaseIndices() -> IntArray
        
        
        Returns the edge crease indices.
        
        
        
        """
    @staticmethod
    def GetCreaseLengths(*args, **kwargs):
        """
        
        GetCreaseLengths() -> IntArray
        
        
        Returns the edge crease loop lengths.
        
        
        
        """
    @staticmethod
    def GetCreaseMethod(*args, **kwargs):
        """
        
        GetCreaseMethod() -> str
        
        
        Returns the creasing method.
        
        
        
        """
    @staticmethod
    def GetCreaseWeights(*args, **kwargs):
        """
        
        GetCreaseWeights() -> FloatArray
        
        
        Returns the edge crease weights.
        
        
        
        """
    @staticmethod
    def GetFaceVaryingInterpolationRule(*args, **kwargs):
        """
        
        GetFaceVaryingInterpolationRule() -> str
        
        
        Returns the face-varying boundary interpolation rule.
        
        
        
        """
    @staticmethod
    def GetTriangleSubdivision(*args, **kwargs):
        """
        
        GetTriangleSubdivision() -> str
        
        
        Returns the triangle subdivision method.
        
        
        
        """
    @staticmethod
    def GetVertexInterpolationRule(*args, **kwargs):
        """
        
        GetVertexInterpolationRule() -> str
        
        
        Returns the vertex boundary interpolation rule.
        
        
        
        """
    @staticmethod
    def SetCornerIndices(*args, **kwargs):
        """
        
        SetCornerIndices(cornerIndices) -> None
        
        
        Set the edge corner indices.
        
        
        Parameters
        ----------
        cornerIndices : IntArray
        
        
        """
    @staticmethod
    def SetCornerWeights(*args, **kwargs):
        """
        
        SetCornerWeights(cornerWeights) -> None
        
        
        Set the edge corner weights.
        
        
        Parameters
        ----------
        cornerWeights : FloatArray
        
        
        """
    @staticmethod
    def SetCreaseIndices(*args, **kwargs):
        """
        
        SetCreaseIndices(creaseIndices) -> None
        
        
        Set the edge crease indices.
        
        
        Parameters
        ----------
        creaseIndices : IntArray
        
        
        """
    @staticmethod
    def SetCreaseLengths(*args, **kwargs):
        """
        
        SetCreaseLengths(creaseLengths) -> None
        
        
        Set the edge crease loop lengths.
        
        
        Parameters
        ----------
        creaseLengths : IntArray
        
        
        """
    @staticmethod
    def SetCreaseMethod(*args, **kwargs):
        """
        
        SetCreaseMethod(creaseMethod) -> None
        
        
        Set the creasing method.
        
        
        Parameters
        ----------
        creaseMethod : str
        
        
        """
    @staticmethod
    def SetCreaseWeights(*args, **kwargs):
        """
        
        SetCreaseWeights(creaseWeights) -> None
        
        
        Set the edge crease weights.
        
        
        Parameters
        ----------
        creaseWeights : FloatArray
        
        
        """
    @staticmethod
    def SetFaceVaryingInterpolationRule(*args, **kwargs):
        """
        
        SetFaceVaryingInterpolationRule(fvarInterp) -> None
        
        
        Set the face-varying boundary interpolation rule.
        
        
        Parameters
        ----------
        fvarInterp : str
        
        
        """
    @staticmethod
    def SetTriangleSubdivision(*args, **kwargs):
        """
        
        SetTriangleSubdivision(triangleSubdivision) -> None
        
        
        Set the triangle subdivision method.
        
        
        Parameters
        ----------
        triangleSubdivision : str
        
        
        """
    @staticmethod
    def SetVertexInterpolationRule(*args, **kwargs):
        """
        
        SetVertexInterpolationRule(vtxInterp) -> None
        
        
        Set the vertex boundary interpolation rule.
        
        
        Parameters
        ----------
        vtxInterp : str
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : SubdivTags
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : SubdivTags
        
        
        
        ----------------------------------------------------------------------
        
        __init__(vertexInterpolationRule, faceVaryingInterpolationRule, creaseMethod, triangleSubdivision, creaseIndices, creaseLengths, creaseWeights, cornerIndices, cornerWeights)
        
        
        Parameters
        ----------
        vertexInterpolationRule : str
        
        faceVaryingInterpolationRule : str
        
        creaseMethod : str
        
        triangleSubdivision : str
        
        creaseIndices : IntArray
        
        creaseLengths : IntArray
        
        creaseWeights : FloatArray
        
        cornerIndices : IntArray
        
        cornerWeights : FloatArray
        
        
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
__MFB_FULL_PACKAGE_NAME: str = 'pxOsd'
