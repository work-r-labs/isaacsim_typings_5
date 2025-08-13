from __future__ import annotations
import pxr.Tf
import typing
__all__: list[str] = ['ArcType', 'ArcTypeInherit', 'ArcTypePayload', 'ArcTypeReference', 'ArcTypeRelocate', 'ArcTypeRoot', 'ArcTypeSpecialize', 'ArcTypeVariant', 'Cache', 'Dependency', 'DependencyType', 'DependencyTypeAncestral', 'DependencyTypeAnyIncludingVirtual', 'DependencyTypeAnyNonVirtual', 'DependencyTypeDirect', 'DependencyTypeNonVirtual', 'DependencyTypeNone', 'DependencyTypePartlyDirect', 'DependencyTypePurelyDirect', 'DependencyTypeRoot', 'DependencyTypeVirtual', 'DynamicFileFormatDependencyData', 'ErrorArcCycle', 'ErrorArcPermissionDenied', 'ErrorBase', 'ErrorCapacityExceeded', 'ErrorInconsistentAttributeType', 'ErrorInconsistentAttributeVariability', 'ErrorInconsistentPropertyType', 'ErrorInvalidAssetPath', 'ErrorInvalidAssetPathBase', 'ErrorInvalidAuthoredRelocation', 'ErrorInvalidConflictingRelocation', 'ErrorInvalidExternalTargetPath', 'ErrorInvalidInstanceTargetPath', 'ErrorInvalidPrimPath', 'ErrorInvalidReferenceOffset', 'ErrorInvalidSameTargetRelocations', 'ErrorInvalidSublayerOffset', 'ErrorInvalidSublayerOwnership', 'ErrorInvalidSublayerPath', 'ErrorInvalidTargetPath', 'ErrorMutedAssetPath', 'ErrorOpinionAtRelocationSource', 'ErrorPrimPermissionDenied', 'ErrorPropertyPermissionDenied', 'ErrorRelocationBase', 'ErrorSublayerCycle', 'ErrorTargetPathBase', 'ErrorTargetPermissionDenied', 'ErrorType', 'ErrorType_ArcCapacityExceeded', 'ErrorType_ArcCycle', 'ErrorType_ArcNamespaceDepthCapacityExceeded', 'ErrorType_ArcPermissionDenied', 'ErrorType_InconsistentAttributeType', 'ErrorType_InconsistentAttributeVariability', 'ErrorType_InconsistentPropertyType', 'ErrorType_IndexCapacityExceeded', 'ErrorType_InternalAssetPath', 'ErrorType_InvalidAssetPath', 'ErrorType_InvalidAuthoredRelocation', 'ErrorType_InvalidConflictingRelocation', 'ErrorType_InvalidExternalTargetPath', 'ErrorType_InvalidInstanceTargetPath', 'ErrorType_InvalidPrimPath', 'ErrorType_InvalidReferenceOffset', 'ErrorType_InvalidSameTargetRelocations', 'ErrorType_InvalidSublayerOffset', 'ErrorType_InvalidSublayerOwnership', 'ErrorType_InvalidSublayerPath', 'ErrorType_InvalidTargetPath', 'ErrorType_InvalidVariantSelection', 'ErrorType_MutedAssetPath', 'ErrorType_OpinionAtRelocationSource', 'ErrorType_PrimPermissionDenied', 'ErrorType_PropertyPermissionDenied', 'ErrorType_SublayerCycle', 'ErrorType_TargetPermissionDenied', 'ErrorType_UnresolvedPrimPath', 'ErrorType_VariableExpressionError', 'ErrorUnresolvedPrimPath', 'ErrorVariableExpressionError', 'ExpressionVariables', 'ExpressionVariablesSource', 'InstanceKey', 'LayerStack', 'LayerStackIdentifier', 'LayerStackSite', 'MapExpression', 'MapFunction', 'NodeRef', 'PrimIndex', 'PropertyIndex', 'Site']
class ArcType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Pcp.ArcTypeRoot, Pcp.ArcTypeInherit, Pcp.ArcTypeRelocate, Pcp.ArcTypeVariant, Pcp.ArcTypeReference, Pcp.ArcTypePayload, Pcp.ArcTypeSpecialize)
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
class Cache(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 376
    @staticmethod
    def ComputeAttributeConnectionPaths(*args, **kwargs):
        ...
    @staticmethod
    def ComputeLayerStack(*args, **kwargs):
        ...
    @staticmethod
    def ComputePrimIndex(*args, **kwargs):
        ...
    @staticmethod
    def ComputePropertyIndex(*args, **kwargs):
        ...
    @staticmethod
    def ComputeRelationshipTargetPaths(*args, **kwargs):
        ...
    @staticmethod
    def FindAllLayerStacksUsingLayer(*args, **kwargs):
        ...
    @staticmethod
    def FindPrimIndex(*args, **kwargs):
        ...
    @staticmethod
    def FindPropertyIndex(*args, **kwargs):
        ...
    @staticmethod
    def FindSiteDependencies(*args, **kwargs):
        ...
    @staticmethod
    def GetDynamicFileFormatArgumentDependencyData(*args, **kwargs):
        ...
    @staticmethod
    def GetExpressionVariablesFromLayerStackUsedByPrim(*args, **kwargs):
        ...
    @staticmethod
    def GetLayerStackIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def GetMutedLayers(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimsUsingExpressionVariablesFromLayerStack(*args, **kwargs):
        ...
    @staticmethod
    def GetUsedLayers(*args, **kwargs):
        ...
    @staticmethod
    def GetUsedLayersRevision(*args, **kwargs):
        ...
    @staticmethod
    def GetVariantFallbacks(*args, **kwargs):
        ...
    @staticmethod
    def HasAnyDynamicFileFormatArgumentAttributeDependencies(*args, **kwargs):
        ...
    @staticmethod
    def HasAnyDynamicFileFormatArgumentFieldDependencies(*args, **kwargs):
        ...
    @staticmethod
    def HasRootLayerStack(*args, **kwargs):
        ...
    @staticmethod
    def IsInvalidAssetPath(*args, **kwargs):
        ...
    @staticmethod
    def IsInvalidSublayerIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def IsLayerMuted(*args, **kwargs):
        ...
    @staticmethod
    def IsPayloadIncluded(*args, **kwargs):
        ...
    @staticmethod
    def IsPossibleDynamicFileFormatArgumentAttribute(*args, **kwargs):
        ...
    @staticmethod
    def IsPossibleDynamicFileFormatArgumentField(*args, **kwargs):
        ...
    @staticmethod
    def PrintStatistics(*args, **kwargs):
        ...
    @staticmethod
    def Reload(*args, **kwargs):
        ...
    @staticmethod
    def RequestLayerMuting(*args, **kwargs):
        ...
    @staticmethod
    def RequestPayloads(*args, **kwargs):
        ...
    @staticmethod
    def SetVariantFallbacks(*args, **kwargs):
        ...
    @staticmethod
    def UsesLayerStack(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def fileFormatTarget(*args, **kwargs):
        ...
    @property
    def layerStack(*args, **kwargs):
        ...
class Dependency(Boost.Python.instance):
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
    def indexPath(*args, **kwargs):
        ...
    @indexPath.setter
    def indexPath(*args, **kwargs):
        ...
    @property
    def mapFunc(*args, **kwargs):
        ...
    @mapFunc.setter
    def mapFunc(*args, **kwargs):
        ...
    @property
    def sitePath(*args, **kwargs):
        ...
    @sitePath.setter
    def sitePath(*args, **kwargs):
        ...
class DependencyType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Pcp.DependencyTypeNone, Pcp.DependencyTypeRoot, Pcp.DependencyTypePurelyDirect, Pcp.DependencyTypePartlyDirect, Pcp.DependencyTypeDirect, Pcp.DependencyTypeAncestral, Pcp.DependencyTypeVirtual, Pcp.DependencyTypeNonVirtual, Pcp.DependencyTypeAnyNonVirtual, Pcp.DependencyTypeAnyIncludingVirtual)
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
class DynamicFileFormatDependencyData(Boost.Python.instance):
    @staticmethod
    def CanAttributeDefaultValueChangeAffectFileFormatArguments(*args, **kwargs):
        ...
    @staticmethod
    def CanFieldChangeAffectFileFormatArguments(*args, **kwargs):
        ...
    @staticmethod
    def GetRelevantAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetRelevantFieldNames(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
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
class ErrorArcCycle(ErrorBase):
    """
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
class ErrorArcPermissionDenied(ErrorBase):
    """
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
class ErrorBase(Boost.Python.instance):
    """
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def errorType(*args, **kwargs):
        ...
class ErrorCapacityExceeded(ErrorBase):
    """
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
class ErrorInconsistentAttributeType(ErrorBase):
    """
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
class ErrorInconsistentAttributeVariability(ErrorBase):
    """
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
class ErrorInconsistentPropertyType(ErrorBase):
    """
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
class ErrorInvalidAssetPath(ErrorInvalidAssetPathBase):
    """
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
class ErrorInvalidAssetPathBase(ErrorBase):
    """
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
class ErrorInvalidAuthoredRelocation(ErrorRelocationBase):
    """
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
class ErrorInvalidConflictingRelocation(ErrorRelocationBase):
    """
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
class ErrorInvalidExternalTargetPath(ErrorTargetPathBase):
    """
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
class ErrorInvalidInstanceTargetPath(ErrorTargetPathBase):
    """
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
class ErrorInvalidPrimPath(ErrorBase):
    """
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
class ErrorInvalidReferenceOffset(ErrorBase):
    """
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
class ErrorInvalidSameTargetRelocations(ErrorRelocationBase):
    """
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
class ErrorInvalidSublayerOffset(ErrorBase):
    """
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
class ErrorInvalidSublayerOwnership(ErrorBase):
    """
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
class ErrorInvalidSublayerPath(ErrorBase):
    """
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
class ErrorInvalidTargetPath(ErrorTargetPathBase):
    """
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
class ErrorMutedAssetPath(ErrorInvalidAssetPathBase):
    """
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
class ErrorOpinionAtRelocationSource(ErrorBase):
    """
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
class ErrorPrimPermissionDenied(ErrorBase):
    """
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
class ErrorPropertyPermissionDenied(ErrorBase):
    """
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
class ErrorRelocationBase(ErrorBase):
    """
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
class ErrorSublayerCycle(ErrorBase):
    """
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
class ErrorTargetPathBase(ErrorBase):
    """
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
class ErrorTargetPermissionDenied(ErrorTargetPathBase):
    """
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
class ErrorType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Pcp.ErrorType_ArcCycle, Pcp.ErrorType_ArcPermissionDenied, Pcp.ErrorType_IndexCapacityExceeded, Pcp.ErrorType_ArcCapacityExceeded, Pcp.ErrorType_ArcNamespaceDepthCapacityExceeded, Pcp.ErrorType_InconsistentPropertyType, Pcp.ErrorType_InconsistentAttributeType, Pcp.ErrorType_InconsistentAttributeVariability, Pcp.ErrorType_InternalAssetPath, Pcp.ErrorType_InvalidPrimPath, Pcp.ErrorType_InvalidAssetPath, Pcp.ErrorType_InvalidInstanceTargetPath, Pcp.ErrorType_InvalidExternalTargetPath, Pcp.ErrorType_InvalidTargetPath, Pcp.ErrorType_InvalidReferenceOffset, Pcp.ErrorType_InvalidSublayerOffset, Pcp.ErrorType_InvalidSublayerOwnership, Pcp.ErrorType_InvalidSublayerPath, Pcp.ErrorType_InvalidVariantSelection, Pcp.ErrorType_MutedAssetPath, Pcp.ErrorType_InvalidAuthoredRelocation, Pcp.ErrorType_InvalidConflictingRelocation, Pcp.ErrorType_InvalidSameTargetRelocations, Pcp.ErrorType_OpinionAtRelocationSource, Pcp.ErrorType_PrimPermissionDenied, Pcp.ErrorType_PropertyPermissionDenied, Pcp.ErrorType_SublayerCycle, Pcp.ErrorType_TargetPermissionDenied, Pcp.ErrorType_UnresolvedPrimPath, Pcp.ErrorType_VariableExpressionError)
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
class ErrorUnresolvedPrimPath(ErrorBase):
    """
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
class ErrorVariableExpressionError(ErrorBase):
    """
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
class ExpressionVariables(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Compute(*args, **kwargs):
        ...
    @staticmethod
    def GetSource(*args, **kwargs):
        ...
    @staticmethod
    def GetVariables(*args, **kwargs):
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
class ExpressionVariablesSource(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def GetLayerStackIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def IsRootLayerStack(*args, **kwargs):
        ...
    @staticmethod
    def ResolveLayerStackIdentifier(*args, **kwargs):
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
class InstanceKey(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 80
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
    def __str__(*args, **kwargs):
        ...
class LayerStack(Boost.Python.instance):
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def expressionVariableDependencies(*args, **kwargs):
        ...
    @property
    def expressionVariables(*args, **kwargs):
        ...
    @property
    def identifier(*args, **kwargs):
        ...
    @property
    def incrementalRelocatesSourceToTarget(*args, **kwargs):
        ...
    @property
    def incrementalRelocatesTargetToSource(*args, **kwargs):
        ...
    @property
    def layerOffsets(*args, **kwargs):
        ...
    @property
    def layerTree(*args, **kwargs):
        ...
    @property
    def layers(*args, **kwargs):
        ...
    @property
    def localErrors(*args, **kwargs):
        ...
    @property
    def mutedLayers(*args, **kwargs):
        ...
    @property
    def pathsToPrimsWithRelocates(*args, **kwargs):
        ...
    @property
    def relocatesSourceToTarget(*args, **kwargs):
        ...
    @property
    def relocatesTargetToSource(*args, **kwargs):
        ...
    @property
    def sessionLayerTree(*args, **kwargs):
        ...
class LayerStackIdentifier(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 104
    @staticmethod
    def __bool__(*args, **kwargs):
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
    @property
    def expressionVariablesOverrideSource(*args, **kwargs):
        ...
    @property
    def pathResolverContext(*args, **kwargs):
        ...
    @property
    def rootLayer(*args, **kwargs):
        ...
    @property
    def sessionLayer(*args, **kwargs):
        ...
class LayerStackSite(Boost.Python.instance):
    """
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def layerStack(*args, **kwargs):
        ...
    @layerStack.setter
    def layerStack(*args, **kwargs):
        ...
    @property
    def path(*args, **kwargs):
        ...
    @path.setter
    def path(*args, **kwargs):
        ...
class MapExpression(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def AddRootIdentity(*args, **kwargs):
        ...
    @staticmethod
    def Compose(*args, **kwargs):
        ...
    @staticmethod
    def Constant(*args, **kwargs):
        ...
    @staticmethod
    def Evaluate(*args, **kwargs):
        ...
    @staticmethod
    def Identity(*args, **kwargs):
        ...
    @staticmethod
    def Inverse(*args, **kwargs):
        ...
    @staticmethod
    def MapSourceToTarget(*args, **kwargs):
        ...
    @staticmethod
    def MapTargetToSource(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def isIdentity(*args, **kwargs):
        ...
    @property
    def isNull(*args, **kwargs):
        ...
    @property
    def timeOffset(*args, **kwargs):
        ...
class MapFunction(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 80
    @staticmethod
    def Compose(*args, **kwargs):
        ...
    @staticmethod
    def ComposeOffset(*args, **kwargs):
        ...
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def Identity(*args, **kwargs):
        ...
    @staticmethod
    def IdentityPathMap(*args, **kwargs):
        ...
    @staticmethod
    def MapSourceToTarget(*args, **kwargs):
        ...
    @staticmethod
    def MapTargetToSource(*args, **kwargs):
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
    def isIdentity(*args, **kwargs):
        ...
    @property
    def isIdentityPathMapping(*args, **kwargs):
        ...
    @property
    def isNull(*args, **kwargs):
        ...
    @property
    def sourceToTargetMap(*args, **kwargs):
        ...
    @property
    def timeOffset(*args, **kwargs):
        ...
class NodeRef(Boost.Python.instance):
    @staticmethod
    def CanContributeSpecs(*args, **kwargs):
        ...
    @staticmethod
    def GetDepthBelowIntroduction(*args, **kwargs):
        ...
    @staticmethod
    def GetIntroPath(*args, **kwargs):
        ...
    @staticmethod
    def GetOriginRootNode(*args, **kwargs):
        ...
    @staticmethod
    def GetPathAtIntroduction(*args, **kwargs):
        ...
    @staticmethod
    def GetRootNode(*args, **kwargs):
        ...
    @staticmethod
    def GetSpecContributionRestrictedDepth(*args, **kwargs):
        ...
    @staticmethod
    def IsDueToAncestor(*args, **kwargs):
        ...
    @staticmethod
    def IsRootNode(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getattribute__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def arcType(*args, **kwargs):
        ...
    @property
    def children(*args, **kwargs):
        ...
    @property
    def hasSpecs(*args, **kwargs):
        ...
    @property
    def hasSymmetry(*args, **kwargs):
        ...
    @property
    def isCulled(*args, **kwargs):
        ...
    @property
    def isInert(*args, **kwargs):
        ...
    @property
    def isRestricted(*args, **kwargs):
        ...
    @property
    def layerStack(*args, **kwargs):
        ...
    @property
    def mapToParent(*args, **kwargs):
        ...
    @property
    def mapToRoot(*args, **kwargs):
        ...
    @property
    def namespaceDepth(*args, **kwargs):
        ...
    @property
    def origin(*args, **kwargs):
        ...
    @property
    def parent(*args, **kwargs):
        ...
    @property
    def path(*args, **kwargs):
        ...
    @property
    def permission(*args, **kwargs):
        ...
    @property
    def siblingNumAtOrigin(*args, **kwargs):
        ...
    @property
    def site(*args, **kwargs):
        ...
class PrimIndex(Boost.Python.instance):
    """
    """
    @staticmethod
    def ComposeAuthoredVariantSelections(*args, **kwargs):
        ...
    @staticmethod
    def ComputePrimChildNames(*args, **kwargs):
        ...
    @staticmethod
    def ComputePrimPropertyNames(*args, **kwargs):
        ...
    @staticmethod
    def DumpToDotGraph(*args, **kwargs):
        ...
    @staticmethod
    def DumpToString(*args, **kwargs):
        ...
    @staticmethod
    def GetNodeProvidingSpec(*args, **kwargs):
        ...
    @staticmethod
    def GetSelectionAppliedForVariantSet(*args, **kwargs):
        ...
    @staticmethod
    def IsInstanceable(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        ...
    @staticmethod
    def PrintStatistics(*args, **kwargs):
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
    @property
    def hasAnyPayloads(*args, **kwargs):
        ...
    @property
    def localErrors(*args, **kwargs):
        ...
    @property
    def primStack(*args, **kwargs):
        ...
    @property
    def rootNode(*args, **kwargs):
        ...
class PropertyIndex(Boost.Python.instance):
    """
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
    @property
    def localErrors(*args, **kwargs):
        ...
    @property
    def localPropertyStack(*args, **kwargs):
        ...
    @property
    def propertyStack(*args, **kwargs):
        ...
class Site(Boost.Python.instance):
    """
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def layerStack(*args, **kwargs):
        ...
    @layerStack.setter
    def layerStack(*args, **kwargs):
        ...
    @property
    def path(*args, **kwargs):
        ...
    @path.setter
    def path(*args, **kwargs):
        ...
class _TestChangeProcessor(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def GetPrimChanges(*args, **kwargs):
        ...
    @staticmethod
    def GetSignificantChanges(*args, **kwargs):
        ...
    @staticmethod
    def GetSpecChanges(*args, **kwargs):
        ...
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
def _TestPrimIndex(primIndex, expected):
    """
    Generator for verifying the expected structure and
        values throughout the given prim index.
    
        The "expected" parameter is a list that mirrors the tree
        structure of the prim index:
    
        expected  : [nodeEntry]
        nodeEntry : (tuple of arbitrary data), [nodeEntry, ...]
    
        The first item in a nodeEntry is a tuple of arbitrary data
        associated with a node in the prim index. The second item is
        a list of nodeEntries corresponding to the children of that
        node.
    
        This generator will visit each node in the prim index and
        yield the node and the associated data tuple.
    
        For example:
    
        expected = [
            (Pcp.ArcTypeRoot, "/Root"), [
                (Pcp.ArcTypeReference, "/Ref1"), [],
                (Pcp.ArcTypeReference, "/Ref2"), []
            ]
        ]
              
        for node, entry in Pcp._TestPrimIndex(primIndex, expected):
            assert node.arcType == entry.arcType
            assert node.path == entry.path
    
        
    """
ArcTypeInherit: ArcType  # value = Pcp.ArcTypeInherit
ArcTypePayload: ArcType  # value = Pcp.ArcTypePayload
ArcTypeReference: ArcType  # value = Pcp.ArcTypeReference
ArcTypeRelocate: ArcType  # value = Pcp.ArcTypeRelocate
ArcTypeRoot: ArcType  # value = Pcp.ArcTypeRoot
ArcTypeSpecialize: ArcType  # value = Pcp.ArcTypeSpecialize
ArcTypeVariant: ArcType  # value = Pcp.ArcTypeVariant
DependencyTypeAncestral: DependencyType  # value = Pcp.DependencyTypeAncestral
DependencyTypeAnyIncludingVirtual: DependencyType  # value = Pcp.DependencyTypeAnyIncludingVirtual
DependencyTypeAnyNonVirtual: DependencyType  # value = Pcp.DependencyTypeAnyNonVirtual
DependencyTypeDirect: DependencyType  # value = Pcp.DependencyTypeDirect
DependencyTypeNonVirtual: DependencyType  # value = Pcp.DependencyTypeNonVirtual
DependencyTypeNone: DependencyType  # value = Pcp.DependencyTypeNone
DependencyTypePartlyDirect: DependencyType  # value = Pcp.DependencyTypePartlyDirect
DependencyTypePurelyDirect: DependencyType  # value = Pcp.DependencyTypePurelyDirect
DependencyTypeRoot: DependencyType  # value = Pcp.DependencyTypeRoot
DependencyTypeVirtual: DependencyType  # value = Pcp.DependencyTypeVirtual
ErrorType_ArcCapacityExceeded: ErrorType  # value = Pcp.ErrorType_ArcCapacityExceeded
ErrorType_ArcCycle: ErrorType  # value = Pcp.ErrorType_ArcCycle
ErrorType_ArcNamespaceDepthCapacityExceeded: ErrorType  # value = Pcp.ErrorType_ArcNamespaceDepthCapacityExceeded
ErrorType_ArcPermissionDenied: ErrorType  # value = Pcp.ErrorType_ArcPermissionDenied
ErrorType_InconsistentAttributeType: ErrorType  # value = Pcp.ErrorType_InconsistentAttributeType
ErrorType_InconsistentAttributeVariability: ErrorType  # value = Pcp.ErrorType_InconsistentAttributeVariability
ErrorType_InconsistentPropertyType: ErrorType  # value = Pcp.ErrorType_InconsistentPropertyType
ErrorType_IndexCapacityExceeded: ErrorType  # value = Pcp.ErrorType_IndexCapacityExceeded
ErrorType_InternalAssetPath: ErrorType  # value = Pcp.ErrorType_InternalAssetPath
ErrorType_InvalidAssetPath: ErrorType  # value = Pcp.ErrorType_InvalidAssetPath
ErrorType_InvalidAuthoredRelocation: ErrorType  # value = Pcp.ErrorType_InvalidAuthoredRelocation
ErrorType_InvalidConflictingRelocation: ErrorType  # value = Pcp.ErrorType_InvalidConflictingRelocation
ErrorType_InvalidExternalTargetPath: ErrorType  # value = Pcp.ErrorType_InvalidExternalTargetPath
ErrorType_InvalidInstanceTargetPath: ErrorType  # value = Pcp.ErrorType_InvalidInstanceTargetPath
ErrorType_InvalidPrimPath: ErrorType  # value = Pcp.ErrorType_InvalidPrimPath
ErrorType_InvalidReferenceOffset: ErrorType  # value = Pcp.ErrorType_InvalidReferenceOffset
ErrorType_InvalidSameTargetRelocations: ErrorType  # value = Pcp.ErrorType_InvalidSameTargetRelocations
ErrorType_InvalidSublayerOffset: ErrorType  # value = Pcp.ErrorType_InvalidSublayerOffset
ErrorType_InvalidSublayerOwnership: ErrorType  # value = Pcp.ErrorType_InvalidSublayerOwnership
ErrorType_InvalidSublayerPath: ErrorType  # value = Pcp.ErrorType_InvalidSublayerPath
ErrorType_InvalidTargetPath: ErrorType  # value = Pcp.ErrorType_InvalidTargetPath
ErrorType_InvalidVariantSelection: ErrorType  # value = Pcp.ErrorType_InvalidVariantSelection
ErrorType_MutedAssetPath: ErrorType  # value = Pcp.ErrorType_MutedAssetPath
ErrorType_OpinionAtRelocationSource: ErrorType  # value = Pcp.ErrorType_OpinionAtRelocationSource
ErrorType_PrimPermissionDenied: ErrorType  # value = Pcp.ErrorType_PrimPermissionDenied
ErrorType_PropertyPermissionDenied: ErrorType  # value = Pcp.ErrorType_PropertyPermissionDenied
ErrorType_SublayerCycle: ErrorType  # value = Pcp.ErrorType_SublayerCycle
ErrorType_TargetPermissionDenied: ErrorType  # value = Pcp.ErrorType_TargetPermissionDenied
ErrorType_UnresolvedPrimPath: ErrorType  # value = Pcp.ErrorType_UnresolvedPrimPath
ErrorType_VariableExpressionError: ErrorType  # value = Pcp.ErrorType_VariableExpressionError
__MFB_FULL_PACKAGE_NAME: str = 'pcp'
