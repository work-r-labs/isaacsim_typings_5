from __future__ import annotations
import pxr.Sdf
import pxr.Tf
import typing
__all__: list[str] = ['APISchemaBase', 'AssetInfoKeys', 'Attribute', 'AttributeQuery', 'BlockStageCachePopulation', 'BlockStageCaches', 'ClipsAPI', 'CollectionAPI', 'CompositionArc', 'CrateInfo', 'EditContext', 'EditTarget', 'FlattenResolveAssetPathContext', 'Inherits', 'InterpolationType', 'InterpolationTypeHeld', 'InterpolationTypeLinear', 'ListPosition', 'ListPositionBackOfAppendList', 'ListPositionBackOfPrependList', 'ListPositionFrontOfAppendList', 'ListPositionFrontOfPrependList', 'LoadPolicy', 'LoadWithDescendants', 'LoadWithoutDescendants', 'ModelAPI', 'NamespaceEditor', 'Notice', 'Object', 'Payloads', 'Prim', 'PrimAllPrimsPredicate', 'PrimCompositionQuery', 'PrimDefaultPredicate', 'PrimDefinition', 'PrimHasDefiningSpecifier', 'PrimIsAbstract', 'PrimIsActive', 'PrimIsDefined', 'PrimIsGroup', 'PrimIsInstance', 'PrimIsLoaded', 'PrimIsModel', 'PrimRange', 'PrimTypeInfo', 'Property', 'References', 'Relationship', 'ResolveInfo', 'ResolveInfoSource', 'ResolveInfoSourceDefault', 'ResolveInfoSourceFallback', 'ResolveInfoSourceNone', 'ResolveInfoSourceTimeSamples', 'ResolveInfoSourceValueClips', 'ResolveTarget', 'SchemaBase', 'SchemaKind', 'SchemaRegistry', 'Specializes', 'Stage', 'StageCache', 'StageCacheContext', 'StageCacheContextBlockType', 'StageLoadRules', 'StagePopulationMask', 'TimeCode', 'Tokens', 'Typed', 'UsdCollectionMembershipQuery', 'UsdFileFormat', 'VariantSet', 'VariantSets', 'ZipFile', 'ZipFileWriter']
class APISchemaBase(SchemaBase):
    """
    """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
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
class AssetInfoKeys(Boost.Python.instance):
    identifier: typing.ClassVar[str] = 'identifier'
    name: typing.ClassVar[str] = 'name'
    payloadAssetDependencies: typing.ClassVar[str] = 'payloadAssetDependencies'
    version: typing.ClassVar[str] = 'version'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Attribute(Property):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def AddConnection(*args, **kwargs):
        ...
    @staticmethod
    def Block(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearAtTime(*args, **kwargs):
        ...
    @staticmethod
    def ClearColorSpace(*args, **kwargs):
        ...
    @staticmethod
    def ClearConnections(*args, **kwargs):
        ...
    @staticmethod
    def ClearDefault(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetBracketingTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetColorSpace(*args, **kwargs):
        ...
    @staticmethod
    def GetConnections(*args, **kwargs):
        ...
    @staticmethod
    def GetNumTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetResolveInfo(*args, **kwargs):
        ...
    @staticmethod
    def GetRoleName(*args, **kwargs):
        ...
    @staticmethod
    def GetTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetTimeSamplesInInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetTypeName(*args, **kwargs):
        ...
    @staticmethod
    def GetUnionedTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetUnionedTimeSamplesInInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetVariability(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredConnections(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredValue(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredValueOpinion(*args, **kwargs):
        ...
    @staticmethod
    def HasColorSpace(*args, **kwargs):
        ...
    @staticmethod
    def HasFallbackValue(*args, **kwargs):
        ...
    @staticmethod
    def HasValue(*args, **kwargs):
        ...
    @staticmethod
    def RemoveConnection(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def SetColorSpace(*args, **kwargs):
        ...
    @staticmethod
    def SetConnections(*args, **kwargs):
        ...
    @staticmethod
    def SetTypeName(*args, **kwargs):
        ...
    @staticmethod
    def SetVariability(*args, **kwargs):
        ...
    @staticmethod
    def ValueMightBeTimeVarying(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class AttributeQuery(Boost.Python.instance):
    @staticmethod
    def CreateQueries(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAttribute(*args, **kwargs):
        ...
    @staticmethod
    def GetBracketingTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetNumTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetTimeSamplesInInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetUnionedTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetUnionedTimeSamplesInInterval(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredValue(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredValueOpinion(*args, **kwargs):
        ...
    @staticmethod
    def HasFallbackValue(*args, **kwargs):
        ...
    @staticmethod
    def HasValue(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        ...
    @staticmethod
    def ValueMightBeTimeVarying(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ClipsAPI(APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def ComputeClipAssetPaths(*args, **kwargs):
        ...
    @staticmethod
    def GenerateClipManifest(*args, **kwargs):
        ...
    @staticmethod
    def GenerateClipManifestFromLayers(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetClipActive(*args, **kwargs):
        ...
    @staticmethod
    def GetClipAssetPaths(*args, **kwargs):
        ...
    @staticmethod
    def GetClipManifestAssetPath(*args, **kwargs):
        ...
    @staticmethod
    def GetClipPrimPath(*args, **kwargs):
        ...
    @staticmethod
    def GetClipSets(*args, **kwargs):
        ...
    @staticmethod
    def GetClipTemplateActiveOffset(*args, **kwargs):
        ...
    @staticmethod
    def GetClipTemplateAssetPath(*args, **kwargs):
        ...
    @staticmethod
    def GetClipTemplateEndTime(*args, **kwargs):
        ...
    @staticmethod
    def GetClipTemplateStartTime(*args, **kwargs):
        ...
    @staticmethod
    def GetClipTemplateStride(*args, **kwargs):
        ...
    @staticmethod
    def GetClipTimes(*args, **kwargs):
        ...
    @staticmethod
    def GetClips(*args, **kwargs):
        ...
    @staticmethod
    def GetInterpolateMissingClipValues(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def SetClipActive(*args, **kwargs):
        ...
    @staticmethod
    def SetClipAssetPaths(*args, **kwargs):
        ...
    @staticmethod
    def SetClipManifestAssetPath(*args, **kwargs):
        ...
    @staticmethod
    def SetClipPrimPath(*args, **kwargs):
        ...
    @staticmethod
    def SetClipSets(*args, **kwargs):
        ...
    @staticmethod
    def SetClipTemplateActiveOffset(*args, **kwargs):
        ...
    @staticmethod
    def SetClipTemplateAssetPath(*args, **kwargs):
        ...
    @staticmethod
    def SetClipTemplateEndTime(*args, **kwargs):
        ...
    @staticmethod
    def SetClipTemplateStartTime(*args, **kwargs):
        ...
    @staticmethod
    def SetClipTemplateStride(*args, **kwargs):
        ...
    @staticmethod
    def SetClipTimes(*args, **kwargs):
        ...
    @staticmethod
    def SetClips(*args, **kwargs):
        ...
    @staticmethod
    def SetInterpolateMissingClipValues(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class CollectionAPI(APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def BlockCollection(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CanContainPropertyName(*args, **kwargs):
        ...
    @staticmethod
    def ComputeIncludedObjects(*args, **kwargs):
        ...
    @staticmethod
    def ComputeIncludedPaths(*args, **kwargs):
        ...
    @staticmethod
    def ComputeMembershipQuery(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollectionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExcludesRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateExpansionRuleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateIncludeRootAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateIncludesRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateMembershipExpressionAttr(*args, **kwargs):
        ...
    @staticmethod
    def ExcludePath(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetAllCollections(*args, **kwargs):
        ...
    @staticmethod
    def GetCollection(*args, **kwargs):
        ...
    @staticmethod
    def GetCollectionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCollectionPath(*args, **kwargs):
        ...
    @staticmethod
    def GetExcludesRel(*args, **kwargs):
        ...
    @staticmethod
    def GetExpansionRuleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetIncludeRootAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetIncludesRel(*args, **kwargs):
        ...
    @staticmethod
    def GetMembershipExpressionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetName(*args, **kwargs):
        ...
    @staticmethod
    def GetNamedCollectionPath(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def HasNoIncludedPaths(*args, **kwargs):
        ...
    @staticmethod
    def IncludePath(*args, **kwargs):
        ...
    @staticmethod
    def IsCollectionAPIPath(*args, **kwargs):
        ...
    @staticmethod
    def IsSchemaPropertyBaseName(*args, **kwargs):
        ...
    @staticmethod
    def ResetCollection(*args, **kwargs):
        ...
    @staticmethod
    def Validate(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class CompositionArc(Boost.Python.instance):
    @staticmethod
    def GetArcType(*args, **kwargs):
        ...
    @staticmethod
    def GetIntroducingLayer(*args, **kwargs):
        ...
    @staticmethod
    def GetIntroducingListEditor(*args, **kwargs):
        ...
    @staticmethod
    def GetIntroducingNode(*args, **kwargs):
        ...
    @staticmethod
    def GetIntroducingPrimPath(*args, **kwargs):
        ...
    @staticmethod
    def GetTargetLayer(*args, **kwargs):
        ...
    @staticmethod
    def GetTargetNode(*args, **kwargs):
        ...
    @staticmethod
    def GetTargetPrimPath(*args, **kwargs):
        ...
    @staticmethod
    def HasSpecs(*args, **kwargs):
        ...
    @staticmethod
    def IsAncestral(*args, **kwargs):
        ...
    @staticmethod
    def IsImplicit(*args, **kwargs):
        ...
    @staticmethod
    def IsIntroducedInRootLayerPrimSpec(*args, **kwargs):
        ...
    @staticmethod
    def IsIntroducedInRootLayerStack(*args, **kwargs):
        ...
    @staticmethod
    def MakeResolveTargetStrongerThan(*args, **kwargs):
        ...
    @staticmethod
    def MakeResolveTargetUpTo(*args, **kwargs):
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
class CrateInfo(Boost.Python.instance):
    class Section(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 72
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @property
        def name(*args, **kwargs):
            ...
        @name.setter
        def name(*args, **kwargs):
            ...
        @property
        def size(*args, **kwargs):
            ...
        @size.setter
        def size(*args, **kwargs):
            ...
        @property
        def start(*args, **kwargs):
            ...
        @start.setter
        def start(*args, **kwargs):
            ...
    class SummaryStats(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 72
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @property
        def numSpecs(*args, **kwargs):
            ...
        @numSpecs.setter
        def numSpecs(*args, **kwargs):
            ...
        @property
        def numUniqueFieldSets(*args, **kwargs):
            ...
        @numUniqueFieldSets.setter
        def numUniqueFieldSets(*args, **kwargs):
            ...
        @property
        def numUniqueFields(*args, **kwargs):
            ...
        @numUniqueFields.setter
        def numUniqueFields(*args, **kwargs):
            ...
        @property
        def numUniquePaths(*args, **kwargs):
            ...
        @numUniquePaths.setter
        def numUniquePaths(*args, **kwargs):
            ...
        @property
        def numUniqueStrings(*args, **kwargs):
            ...
        @numUniqueStrings.setter
        def numUniqueStrings(*args, **kwargs):
            ...
        @property
        def numUniqueTokens(*args, **kwargs):
            ...
        @numUniqueTokens.setter
        def numUniqueTokens(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def GetFileVersion(*args, **kwargs):
        ...
    @staticmethod
    def GetSections(*args, **kwargs):
        ...
    @staticmethod
    def GetSoftwareVersion(*args, **kwargs):
        ...
    @staticmethod
    def GetSummaryStats(*args, **kwargs):
        ...
    @staticmethod
    def Open(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class EditContext(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 128
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
class EditTarget(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 96
    @staticmethod
    def ComposeOver(*args, **kwargs):
        ...
    @staticmethod
    def ForLocalDirectVariant(*args, **kwargs):
        ...
    @staticmethod
    def GetLayer(*args, **kwargs):
        ...
    @staticmethod
    def GetMapFunction(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimSpecForScenePath(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertySpecForScenePath(*args, **kwargs):
        ...
    @staticmethod
    def GetSpecForScenePath(*args, **kwargs):
        ...
    @staticmethod
    def IsNull(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        ...
    @staticmethod
    def MapToSpecPath(*args, **kwargs):
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
class FlattenResolveAssetPathContext(Boost.Python.instance):
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
    def assetPath(*args, **kwargs):
        ...
    @property
    def expressionVariables(*args, **kwargs):
        ...
    @property
    def sourceLayer(*args, **kwargs):
        ...
class Inherits(Boost.Python.instance):
    @staticmethod
    def AddInherit(*args, **kwargs):
        ...
    @staticmethod
    def ClearInherits(*args, **kwargs):
        ...
    @staticmethod
    def GetAllDirectInherits(*args, **kwargs):
        ...
    @staticmethod
    def GetPrim(*args, **kwargs):
        ...
    @staticmethod
    def RemoveInherit(*args, **kwargs):
        ...
    @staticmethod
    def SetInherits(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
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
class InterpolationType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Usd.InterpolationTypeHeld, Usd.InterpolationTypeLinear)
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
class ListPosition(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Usd.ListPositionFrontOfPrependList, Usd.ListPositionBackOfPrependList, Usd.ListPositionFrontOfAppendList, Usd.ListPositionBackOfAppendList)
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
class LoadPolicy(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Usd.LoadWithDescendants, Usd.LoadWithoutDescendants)
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
class ModelAPI(APISchemaBase):
    class KindValidation(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'ModelAPI'
        allValues: typing.ClassVar[tuple]  # value = (Usd.ModelAPI.KindValidationNone, Usd.ModelAPI.KindValidationModelHierarchy)
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
    KindValidationModelHierarchy: typing.ClassVar[KindValidation]  # value = Usd.ModelAPI.KindValidationModelHierarchy
    KindValidationNone: typing.ClassVar[KindValidation]  # value = Usd.ModelAPI.KindValidationNone
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAssetIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def GetAssetInfo(*args, **kwargs):
        ...
    @staticmethod
    def GetAssetName(*args, **kwargs):
        ...
    @staticmethod
    def GetAssetVersion(*args, **kwargs):
        ...
    @staticmethod
    def GetKind(*args, **kwargs):
        ...
    @staticmethod
    def GetPayloadAssetDependencies(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def IsGroup(*args, **kwargs):
        ...
    @staticmethod
    def IsKind(*args, **kwargs):
        ...
    @staticmethod
    def IsModel(*args, **kwargs):
        ...
    @staticmethod
    def SetAssetIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def SetAssetInfo(*args, **kwargs):
        ...
    @staticmethod
    def SetAssetName(*args, **kwargs):
        ...
    @staticmethod
    def SetAssetVersion(*args, **kwargs):
        ...
    @staticmethod
    def SetKind(*args, **kwargs):
        ...
    @staticmethod
    def SetPayloadAssetDependencies(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class NamespaceEditor(Boost.Python.instance):
    @staticmethod
    def ApplyEdits(*args, **kwargs):
        ...
    @staticmethod
    def CanApplyEdits(*args, **kwargs):
        ...
    @staticmethod
    def DeletePrim(*args, **kwargs):
        ...
    @staticmethod
    def DeletePrimAtPath(*args, **kwargs):
        ...
    @staticmethod
    def DeleteProperty(*args, **kwargs):
        ...
    @staticmethod
    def DeletePropertyAtPath(*args, **kwargs):
        ...
    @staticmethod
    def MovePrimAtPath(*args, **kwargs):
        ...
    @staticmethod
    def MovePropertyAtPath(*args, **kwargs):
        ...
    @staticmethod
    def RenamePrim(*args, **kwargs):
        ...
    @staticmethod
    def RenameProperty(*args, **kwargs):
        ...
    @staticmethod
    def ReparentPrim(*args, **kwargs):
        ...
    @staticmethod
    def ReparentProperty(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Notice(Boost.Python.instance):
    class LayerMutingChanged(StageNotice):
        @staticmethod
        def GetMutedLayers(*args, **kwargs):
            ...
        @staticmethod
        def GetUnmutedLayers(*args, **kwargs):
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
    class ObjectsChanged(StageNotice):
        @staticmethod
        def AffectedObject(*args, **kwargs):
            ...
        @staticmethod
        def ChangedInfoOnly(*args, **kwargs):
            ...
        @staticmethod
        def GetChangedFields(*args, **kwargs):
            ...
        @staticmethod
        def GetChangedInfoOnlyPaths(*args, **kwargs):
            ...
        @staticmethod
        def GetResolvedAssetPathsResyncedPaths(*args, **kwargs):
            ...
        @staticmethod
        def GetResyncedPaths(*args, **kwargs):
            ...
        @staticmethod
        def HasChangedFields(*args, **kwargs):
            ...
        @staticmethod
        def ResolvedAssetPathsResynced(*args, **kwargs):
            ...
        @staticmethod
        def ResyncedObject(*args, **kwargs):
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
    class StageContentsChanged(StageNotice):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class StageEditTargetChanged(StageNotice):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class StageNotice(pxr.Tf.Notice):
        @staticmethod
        def GetStage(*args, **kwargs):
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
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Object(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def ClearAssetInfo(*args, **kwargs):
        ...
    @staticmethod
    def ClearAssetInfoByKey(*args, **kwargs):
        ...
    @staticmethod
    def ClearCustomData(*args, **kwargs):
        ...
    @staticmethod
    def ClearCustomDataByKey(*args, **kwargs):
        ...
    @staticmethod
    def ClearDisplayName(*args, **kwargs):
        ...
    @staticmethod
    def ClearDocumentation(*args, **kwargs):
        ...
    @staticmethod
    def ClearHidden(*args, **kwargs):
        ...
    @staticmethod
    def ClearMetadata(*args, **kwargs):
        ...
    @staticmethod
    def ClearMetadataByDictKey(*args, **kwargs):
        ...
    @staticmethod
    def GetAllAuthoredMetadata(*args, **kwargs):
        ...
    @staticmethod
    def GetAllMetadata(*args, **kwargs):
        ...
    @staticmethod
    def GetAssetInfo(*args, **kwargs):
        ...
    @staticmethod
    def GetAssetInfoByKey(*args, **kwargs):
        ...
    @staticmethod
    def GetCustomData(*args, **kwargs):
        ...
    @staticmethod
    def GetCustomDataByKey(*args, **kwargs):
        ...
    @staticmethod
    def GetDescription(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplayName(*args, **kwargs):
        ...
    @staticmethod
    def GetDocumentation(*args, **kwargs):
        ...
    @staticmethod
    def GetMetadata(*args, **kwargs):
        ...
    @staticmethod
    def GetMetadataByDictKey(*args, **kwargs):
        ...
    @staticmethod
    def GetName(*args, **kwargs):
        ...
    @staticmethod
    def GetNamespaceDelimiter(*args, **kwargs):
        ...
    @staticmethod
    def GetPath(*args, **kwargs):
        ...
    @staticmethod
    def GetPrim(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimPath(*args, **kwargs):
        ...
    @staticmethod
    def GetStage(*args, **kwargs):
        ...
    @staticmethod
    def HasAssetInfo(*args, **kwargs):
        ...
    @staticmethod
    def HasAssetInfoKey(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredAssetInfo(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredAssetInfoKey(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredCustomData(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredCustomDataKey(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredDisplayName(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredDocumentation(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredHidden(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredMetadata(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredMetadataDictKey(*args, **kwargs):
        ...
    @staticmethod
    def HasCustomData(*args, **kwargs):
        ...
    @staticmethod
    def HasCustomDataKey(*args, **kwargs):
        ...
    @staticmethod
    def HasMetadata(*args, **kwargs):
        ...
    @staticmethod
    def HasMetadataDictKey(*args, **kwargs):
        ...
    @staticmethod
    def IsHidden(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        ...
    @staticmethod
    def SetAssetInfo(*args, **kwargs):
        ...
    @staticmethod
    def SetAssetInfoByKey(*args, **kwargs):
        ...
    @staticmethod
    def SetCustomData(*args, **kwargs):
        ...
    @staticmethod
    def SetCustomDataByKey(*args, **kwargs):
        ...
    @staticmethod
    def SetDisplayName(*args, **kwargs):
        ...
    @staticmethod
    def SetDocumentation(*args, **kwargs):
        ...
    @staticmethod
    def SetHidden(*args, **kwargs):
        ...
    @staticmethod
    def SetMetadata(*args, **kwargs):
        ...
    @staticmethod
    def SetMetadataByDictKey(*args, **kwargs):
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
class Payloads(Boost.Python.instance):
    @staticmethod
    def AddInternalPayload(*args, **kwargs):
        ...
    @staticmethod
    def AddPayload(*args, **kwargs):
        ...
    @staticmethod
    def ClearPayloads(*args, **kwargs):
        ...
    @staticmethod
    def GetPrim(*args, **kwargs):
        ...
    @staticmethod
    def RemovePayload(*args, **kwargs):
        ...
    @staticmethod
    def SetPayloads(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
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
class Prim(Object):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def AddAppliedSchema(*args, **kwargs):
        ...
    @staticmethod
    def ApplyAPI(*args, **kwargs):
        ...
    @staticmethod
    def CanApplyAPI(*args, **kwargs):
        ...
    @staticmethod
    def ClearActive(*args, **kwargs):
        ...
    @staticmethod
    def ClearChildrenReorder(*args, **kwargs):
        ...
    @staticmethod
    def ClearInstanceable(*args, **kwargs):
        ...
    @staticmethod
    def ClearPayload(*args, **kwargs):
        ...
    @staticmethod
    def ClearPropertyOrder(*args, **kwargs):
        ...
    @staticmethod
    def ClearTypeName(*args, **kwargs):
        ...
    @staticmethod
    def ComputeExpandedPrimIndex(*args, **kwargs):
        ...
    @staticmethod
    def CreateAttribute(*args, **kwargs):
        ...
    @staticmethod
    def CreateRelationship(*args, **kwargs):
        ...
    @staticmethod
    def FindAllAttributeConnectionPaths(*args, **kwargs):
        ...
    @staticmethod
    def FindAllRelationshipTargetPaths(*args, **kwargs):
        ...
    @staticmethod
    def GetAllChildren(*args, **kwargs):
        ...
    @staticmethod
    def GetAllChildrenNames(*args, **kwargs):
        ...
    @staticmethod
    def GetAppliedSchemas(*args, **kwargs):
        ...
    @staticmethod
    def GetAttribute(*args, **kwargs):
        ...
    @staticmethod
    def GetAttributeAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetAttributes(*args, **kwargs):
        ...
    @staticmethod
    def GetAuthoredAttributes(*args, **kwargs):
        ...
    @staticmethod
    def GetAuthoredProperties(*args, **kwargs):
        ...
    @staticmethod
    def GetAuthoredPropertiesInNamespace(*args, **kwargs):
        ...
    @staticmethod
    def GetAuthoredPropertyNames(*args, **kwargs):
        ...
    @staticmethod
    def GetAuthoredRelationships(*args, **kwargs):
        ...
    @staticmethod
    def GetChild(*args, **kwargs):
        ...
    @staticmethod
    def GetChildren(*args, **kwargs):
        ...
    @staticmethod
    def GetChildrenNames(*args, **kwargs):
        ...
    @staticmethod
    def GetChildrenReorder(*args, **kwargs):
        ...
    @staticmethod
    def GetFilteredChildren(*args, **kwargs):
        ...
    @staticmethod
    def GetFilteredChildrenNames(*args, **kwargs):
        ...
    @staticmethod
    def GetFilteredNextSibling(*args, **kwargs):
        ...
    @staticmethod
    def GetInherits(*args, **kwargs):
        ...
    @staticmethod
    def GetInstances(*args, **kwargs):
        ...
    @staticmethod
    def GetKind(*args, **kwargs):
        ...
    @staticmethod
    def GetNextSibling(*args, **kwargs):
        ...
    @staticmethod
    def GetObjectAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetParent(*args, **kwargs):
        ...
    @staticmethod
    def GetPayloads(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimDefinition(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimInPrototype(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimIndex(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimStack(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimStackWithLayerOffsets(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimTypeInfo(*args, **kwargs):
        ...
    @staticmethod
    def GetProperties(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertiesInNamespace(*args, **kwargs):
        ...
    @staticmethod
    def GetProperty(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyNames(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyOrder(*args, **kwargs):
        ...
    @staticmethod
    def GetPrototype(*args, **kwargs):
        ...
    @staticmethod
    def GetReferences(*args, **kwargs):
        ...
    @staticmethod
    def GetRelationship(*args, **kwargs):
        ...
    @staticmethod
    def GetRelationshipAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetRelationships(*args, **kwargs):
        ...
    @staticmethod
    def GetSpecializes(*args, **kwargs):
        ...
    @staticmethod
    def GetSpecifier(*args, **kwargs):
        ...
    @staticmethod
    def GetTypeName(*args, **kwargs):
        ...
    @staticmethod
    def GetVariantSet(*args, **kwargs):
        ...
    @staticmethod
    def GetVariantSets(*args, **kwargs):
        ...
    @staticmethod
    def GetVersionIfHasAPIInFamily(*args, **kwargs):
        ...
    @staticmethod
    def GetVersionIfIsInFamily(*args, **kwargs):
        ...
    @staticmethod
    def HasAPI(*args, **kwargs):
        ...
    @staticmethod
    def HasAPIInFamily(*args, **kwargs):
        ...
    @staticmethod
    def HasAttribute(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredActive(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredInherits(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredInstanceable(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredPayloads(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredReferences(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredSpecializes(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredTypeName(*args, **kwargs):
        ...
    @staticmethod
    def HasDefiningSpecifier(*args, **kwargs):
        ...
    @staticmethod
    def HasPayload(*args, **kwargs):
        ...
    @staticmethod
    def HasProperty(*args, **kwargs):
        ...
    @staticmethod
    def HasRelationship(*args, **kwargs):
        ...
    @staticmethod
    def HasVariantSets(*args, **kwargs):
        ...
    @staticmethod
    def IsA(*args, **kwargs):
        ...
    @staticmethod
    def IsAbstract(*args, **kwargs):
        ...
    @staticmethod
    def IsActive(*args, **kwargs):
        ...
    @staticmethod
    def IsComponent(*args, **kwargs):
        ...
    @staticmethod
    def IsDefined(*args, **kwargs):
        ...
    @staticmethod
    def IsGroup(*args, **kwargs):
        ...
    @staticmethod
    def IsInFamily(*args, **kwargs):
        ...
    @staticmethod
    def IsInPrototype(*args, **kwargs):
        ...
    @staticmethod
    def IsInstance(*args, **kwargs):
        ...
    @staticmethod
    def IsInstanceProxy(*args, **kwargs):
        ...
    @staticmethod
    def IsInstanceable(*args, **kwargs):
        ...
    @staticmethod
    def IsLoaded(*args, **kwargs):
        ...
    @staticmethod
    def IsModel(*args, **kwargs):
        ...
    @staticmethod
    def IsPathInPrototype(*args, **kwargs):
        ...
    @staticmethod
    def IsPrototype(*args, **kwargs):
        ...
    @staticmethod
    def IsPrototypePath(*args, **kwargs):
        ...
    @staticmethod
    def IsPseudoRoot(*args, **kwargs):
        ...
    @staticmethod
    def IsSubComponent(*args, **kwargs):
        ...
    @staticmethod
    def Load(*args, **kwargs):
        ...
    @staticmethod
    def MakeResolveTargetStrongerThanEditTarget(*args, **kwargs):
        ...
    @staticmethod
    def MakeResolveTargetUpToEditTarget(*args, **kwargs):
        ...
    @staticmethod
    def RemoveAPI(*args, **kwargs):
        ...
    @staticmethod
    def RemoveAppliedSchema(*args, **kwargs):
        ...
    @staticmethod
    def RemoveProperty(*args, **kwargs):
        ...
    @staticmethod
    def SetActive(*args, **kwargs):
        ...
    @staticmethod
    def SetChildrenReorder(*args, **kwargs):
        ...
    @staticmethod
    def SetInstanceable(*args, **kwargs):
        ...
    @staticmethod
    def SetKind(*args, **kwargs):
        ...
    @staticmethod
    def SetPayload(*args, **kwargs):
        ...
    @staticmethod
    def SetPropertyOrder(*args, **kwargs):
        ...
    @staticmethod
    def SetSpecifier(*args, **kwargs):
        ...
    @staticmethod
    def SetTypeName(*args, **kwargs):
        ...
    @staticmethod
    def Unload(*args, **kwargs):
        ...
    @staticmethod
    def _GetSourcePrimIndex(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class PrimCompositionQuery(Boost.Python.instance):
    class ArcIntroducedFilter(Boost.Python.enum):
        All: typing.ClassVar[ArcIntroducedFilter]  # value = pxr.Usd.ArcIntroducedFilter.All
        IntroducedInRootLayerPrimSpec: typing.ClassVar[ArcIntroducedFilter]  # value = pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerPrimSpec
        IntroducedInRootLayerStack: typing.ClassVar[ArcIntroducedFilter]  # value = pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerStack
        __slots__: typing.ClassVar[tuple] = tuple()
        names: typing.ClassVar[dict]  # value = {'All': pxr.Usd.ArcIntroducedFilter.All, 'IntroducedInRootLayerStack': pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerStack, 'IntroducedInRootLayerPrimSpec': pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerPrimSpec}
        values: typing.ClassVar[dict]  # value = {0: pxr.Usd.ArcIntroducedFilter.All, 1: pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerStack, 2: pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerPrimSpec}
    class ArcTypeFilter(Boost.Python.enum):
        All: typing.ClassVar[ArcTypeFilter]  # value = pxr.Usd.ArcTypeFilter.All
        Inherit: typing.ClassVar[ArcTypeFilter]  # value = pxr.Usd.ArcTypeFilter.Inherit
        InheritOrSpecialize: typing.ClassVar[ArcTypeFilter]  # value = pxr.Usd.ArcTypeFilter.InheritOrSpecialize
        NotInheritOrSpecialize: typing.ClassVar[ArcTypeFilter]  # value = pxr.Usd.ArcTypeFilter.NotInheritOrSpecialize
        NotReferenceOrPayload: typing.ClassVar[ArcTypeFilter]  # value = pxr.Usd.ArcTypeFilter.NotReferenceOrPayload
        NotVariant: typing.ClassVar[ArcTypeFilter]  # value = pxr.Usd.ArcTypeFilter.NotVariant
        Payload: typing.ClassVar[ArcTypeFilter]  # value = pxr.Usd.ArcTypeFilter.Payload
        Reference: typing.ClassVar[ArcTypeFilter]  # value = pxr.Usd.ArcTypeFilter.Reference
        ReferenceOrPayload: typing.ClassVar[ArcTypeFilter]  # value = pxr.Usd.ArcTypeFilter.ReferenceOrPayload
        Specialize: typing.ClassVar[ArcTypeFilter]  # value = pxr.Usd.ArcTypeFilter.Specialize
        Variant: typing.ClassVar[ArcTypeFilter]  # value = pxr.Usd.ArcTypeFilter.Variant
        __slots__: typing.ClassVar[tuple] = tuple()
        names: typing.ClassVar[dict]  # value = {'All': pxr.Usd.ArcTypeFilter.All, 'Reference': pxr.Usd.ArcTypeFilter.Reference, 'Payload': pxr.Usd.ArcTypeFilter.Payload, 'Inherit': pxr.Usd.ArcTypeFilter.Inherit, 'Specialize': pxr.Usd.ArcTypeFilter.Specialize, 'Variant': pxr.Usd.ArcTypeFilter.Variant, 'ReferenceOrPayload': pxr.Usd.ArcTypeFilter.ReferenceOrPayload, 'InheritOrSpecialize': pxr.Usd.ArcTypeFilter.InheritOrSpecialize, 'NotReferenceOrPayload': pxr.Usd.ArcTypeFilter.NotReferenceOrPayload, 'NotInheritOrSpecialize': pxr.Usd.ArcTypeFilter.NotInheritOrSpecialize, 'NotVariant': pxr.Usd.ArcTypeFilter.NotVariant}
        values: typing.ClassVar[dict]  # value = {0: pxr.Usd.ArcTypeFilter.All, 1: pxr.Usd.ArcTypeFilter.Reference, 2: pxr.Usd.ArcTypeFilter.Payload, 3: pxr.Usd.ArcTypeFilter.Inherit, 4: pxr.Usd.ArcTypeFilter.Specialize, 5: pxr.Usd.ArcTypeFilter.Variant, 6: pxr.Usd.ArcTypeFilter.ReferenceOrPayload, 7: pxr.Usd.ArcTypeFilter.InheritOrSpecialize, 8: pxr.Usd.ArcTypeFilter.NotReferenceOrPayload, 9: pxr.Usd.ArcTypeFilter.NotInheritOrSpecialize, 10: pxr.Usd.ArcTypeFilter.NotVariant}
    class DependencyTypeFilter(Boost.Python.enum):
        All: typing.ClassVar[DependencyTypeFilter]  # value = pxr.Usd.DependencyTypeFilter.All
        Ancestral: typing.ClassVar[DependencyTypeFilter]  # value = pxr.Usd.DependencyTypeFilter.Ancestral
        Direct: typing.ClassVar[DependencyTypeFilter]  # value = pxr.Usd.DependencyTypeFilter.Direct
        __slots__: typing.ClassVar[tuple] = tuple()
        names: typing.ClassVar[dict]  # value = {'All': pxr.Usd.DependencyTypeFilter.All, 'Direct': pxr.Usd.DependencyTypeFilter.Direct, 'Ancestral': pxr.Usd.DependencyTypeFilter.Ancestral}
        values: typing.ClassVar[dict]  # value = {0: pxr.Usd.DependencyTypeFilter.All, 1: pxr.Usd.DependencyTypeFilter.Direct, 2: pxr.Usd.DependencyTypeFilter.Ancestral}
    class Filter(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 40
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
        @property
        def arcIntroducedFilter(*args, **kwargs):
            ...
        @arcIntroducedFilter.setter
        def arcIntroducedFilter(*args, **kwargs):
            ...
        @property
        def arcTypeFilter(*args, **kwargs):
            ...
        @arcTypeFilter.setter
        def arcTypeFilter(*args, **kwargs):
            ...
        @property
        def dependencyTypeFilter(*args, **kwargs):
            ...
        @dependencyTypeFilter.setter
        def dependencyTypeFilter(*args, **kwargs):
            ...
        @property
        def hasSpecsFilter(*args, **kwargs):
            ...
        @hasSpecsFilter.setter
        def hasSpecsFilter(*args, **kwargs):
            ...
    class HasSpecsFilter(Boost.Python.enum):
        All: typing.ClassVar[HasSpecsFilter]  # value = pxr.Usd.HasSpecsFilter.All
        HasNoSpecs: typing.ClassVar[HasSpecsFilter]  # value = pxr.Usd.HasSpecsFilter.HasNoSpecs
        HasSpecs: typing.ClassVar[HasSpecsFilter]  # value = pxr.Usd.HasSpecsFilter.HasSpecs
        __slots__: typing.ClassVar[tuple] = tuple()
        names: typing.ClassVar[dict]  # value = {'All': pxr.Usd.HasSpecsFilter.All, 'HasSpecs': pxr.Usd.HasSpecsFilter.HasSpecs, 'HasNoSpecs': pxr.Usd.HasSpecsFilter.HasNoSpecs}
        values: typing.ClassVar[dict]  # value = {0: pxr.Usd.HasSpecsFilter.All, 1: pxr.Usd.HasSpecsFilter.HasSpecs, 2: pxr.Usd.HasSpecsFilter.HasNoSpecs}
    @staticmethod
    def GetCompositionArcs(*args, **kwargs):
        ...
    @staticmethod
    def GetDirectInherits(*args, **kwargs):
        ...
    @staticmethod
    def GetDirectReferences(*args, **kwargs):
        ...
    @staticmethod
    def GetDirectRootLayerArcs(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def filter(*args, **kwargs):
        ...
    @filter.setter
    def filter(*args, **kwargs):
        ...
class PrimDefinition(Boost.Python.instance):
    class Attribute(Property):
        __instance_size__: typing.ClassVar[int] = 40
        @staticmethod
        def GetFallbackValue(*args, **kwargs):
            ...
        @staticmethod
        def GetTypeName(*args, **kwargs):
            ...
        @staticmethod
        def GetTypeNameToken(*args, **kwargs):
            ...
        @staticmethod
        def __bool__(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class Property(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 40
        @staticmethod
        def GetDocumentation(*args, **kwargs):
            ...
        @staticmethod
        def GetMetadata(*args, **kwargs):
            ...
        @staticmethod
        def GetMetadataByDictKey(*args, **kwargs):
            ...
        @staticmethod
        def GetName(*args, **kwargs):
            ...
        @staticmethod
        def GetSpecType(*args, **kwargs):
            ...
        @staticmethod
        def GetVariability(*args, **kwargs):
            ...
        @staticmethod
        def IsAttribute(*args, **kwargs):
            ...
        @staticmethod
        def IsRelationship(*args, **kwargs):
            ...
        @staticmethod
        def ListMetadataFields(*args, **kwargs):
            ...
        @staticmethod
        def __bool__(*args, **kwargs):
            ...
        @staticmethod
        def __getattribute__(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class Relationship(Property):
        __instance_size__: typing.ClassVar[int] = 40
        @staticmethod
        def __bool__(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    @staticmethod
    def FlattenTo(*args, **kwargs):
        ...
    @staticmethod
    def GetAppliedAPISchemas(*args, **kwargs):
        ...
    @staticmethod
    def GetAttributeDefinition(*args, **kwargs):
        ...
    @staticmethod
    def GetAttributeFallbackValue(*args, **kwargs):
        ...
    @staticmethod
    def GetDocumentation(*args, **kwargs):
        ...
    @staticmethod
    def GetMetadata(*args, **kwargs):
        ...
    @staticmethod
    def GetMetadataByDictKey(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyDefinition(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyDocumentation(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyMetadata(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyMetadataByDictKey(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyNames(*args, **kwargs):
        ...
    @staticmethod
    def GetRelationshipDefinition(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeSpec(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaPropertySpec(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaRelationshipSpec(*args, **kwargs):
        ...
    @staticmethod
    def GetSpecType(*args, **kwargs):
        ...
    @staticmethod
    def ListMetadataFields(*args, **kwargs):
        ...
    @staticmethod
    def ListPropertyMetadataFields(*args, **kwargs):
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
class PrimRange(Boost.Python.instance):
    class _Iterator(Boost.Python.instance):
        @staticmethod
        def GetCurrentPrim(*args, **kwargs):
            """
            
            
            Since an iterator cannot be dereferenced in python, GetCurrentPrim()
             performs the same function: yielding the currently visited prim.
            """
        @staticmethod
        def IsPostVisit(*args, **kwargs):
            ...
        @staticmethod
        def IsValid(*args, **kwargs):
            """
            
            
            true if the iterator is not yet exhausted
            """
        @staticmethod
        def PruneChildren(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    @staticmethod
    def AllPrims(*args, **kwargs):
        ...
    @staticmethod
    def AllPrimsPreAndPostVisit(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        
        true if the iterator is not yet exhausted
        """
    @staticmethod
    def PreAndPostVisit(*args, **kwargs):
        ...
    @staticmethod
    def Stage(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class PrimTypeInfo(Boost.Python.instance):
    @staticmethod
    def GetAppliedAPISchemas(*args, **kwargs):
        ...
    @staticmethod
    def GetEmptyPrimType(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimDefinition(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaType(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaTypeName(*args, **kwargs):
        ...
    @staticmethod
    def GetTypeName(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
class Property(Object):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def ClearDisplayGroup(*args, **kwargs):
        ...
    @staticmethod
    def FlattenTo(*args, **kwargs):
        ...
    @staticmethod
    def GetBaseName(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplayGroup(*args, **kwargs):
        ...
    @staticmethod
    def GetNamespace(*args, **kwargs):
        ...
    @staticmethod
    def GetNestedDisplayGroups(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyStack(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyStackWithLayerOffsets(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredDisplayGroup(*args, **kwargs):
        ...
    @staticmethod
    def IsAuthored(*args, **kwargs):
        ...
    @staticmethod
    def IsAuthoredAt(*args, **kwargs):
        ...
    @staticmethod
    def IsCustom(*args, **kwargs):
        ...
    @staticmethod
    def IsDefined(*args, **kwargs):
        ...
    @staticmethod
    def SetCustom(*args, **kwargs):
        ...
    @staticmethod
    def SetDisplayGroup(*args, **kwargs):
        ...
    @staticmethod
    def SetNestedDisplayGroups(*args, **kwargs):
        ...
    @staticmethod
    def SplitName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class References(Boost.Python.instance):
    @staticmethod
    def AddInternalReference(*args, **kwargs):
        ...
    @staticmethod
    def AddReference(*args, **kwargs):
        ...
    @staticmethod
    def ClearReferences(*args, **kwargs):
        ...
    @staticmethod
    def GetPrim(*args, **kwargs):
        ...
    @staticmethod
    def RemoveReference(*args, **kwargs):
        ...
    @staticmethod
    def SetReferences(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
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
class Relationship(Property):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def AddTarget(*args, **kwargs):
        ...
    @staticmethod
    def ClearTargets(*args, **kwargs):
        ...
    @staticmethod
    def GetForwardedTargets(*args, **kwargs):
        ...
    @staticmethod
    def GetTargets(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredTargets(*args, **kwargs):
        ...
    @staticmethod
    def RemoveTarget(*args, **kwargs):
        ...
    @staticmethod
    def SetTargets(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class ResolveInfo(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 104
    @staticmethod
    def GetNode(*args, **kwargs):
        ...
    @staticmethod
    def GetSource(*args, **kwargs):
        ...
    @staticmethod
    def ValueIsBlocked(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ResolveInfoSource(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Usd.ResolveInfoSourceNone, Usd.ResolveInfoSourceFallback, Usd.ResolveInfoSourceDefault, Usd.ResolveInfoSourceTimeSamples, Usd.ResolveInfoSourceValueClips)
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
class ResolveTarget(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 120
    @staticmethod
    def GetPrimIndex(*args, **kwargs):
        ...
    @staticmethod
    def GetStartLayer(*args, **kwargs):
        ...
    @staticmethod
    def GetStartNode(*args, **kwargs):
        ...
    @staticmethod
    def GetStopLayer(*args, **kwargs):
        ...
    @staticmethod
    def GetStopNode(*args, **kwargs):
        ...
    @staticmethod
    def IsNull(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class SchemaBase(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def GetPath(*args, **kwargs):
        ...
    @staticmethod
    def GetPrim(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaClassPrimDefinition(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaKind(*args, **kwargs):
        ...
    @staticmethod
    def IsAPISchema(*args, **kwargs):
        ...
    @staticmethod
    def IsAppliedAPISchema(*args, **kwargs):
        ...
    @staticmethod
    def IsConcrete(*args, **kwargs):
        ...
    @staticmethod
    def IsMultipleApplyAPISchema(*args, **kwargs):
        ...
    @staticmethod
    def IsTyped(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __getattribute__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class SchemaKind(Boost.Python.enum):
    AbstractBase: typing.ClassVar[SchemaKind]  # value = pxr.Usd.SchemaKind.AbstractBase
    AbstractTyped: typing.ClassVar[SchemaKind]  # value = pxr.Usd.SchemaKind.AbstractTyped
    ConcreteTyped: typing.ClassVar[SchemaKind]  # value = pxr.Usd.SchemaKind.ConcreteTyped
    Invalid: typing.ClassVar[SchemaKind]  # value = pxr.Usd.SchemaKind.Invalid
    MultipleApplyAPI: typing.ClassVar[SchemaKind]  # value = pxr.Usd.SchemaKind.MultipleApplyAPI
    NonAppliedAPI: typing.ClassVar[SchemaKind]  # value = pxr.Usd.SchemaKind.NonAppliedAPI
    SingleApplyAPI: typing.ClassVar[SchemaKind]  # value = pxr.Usd.SchemaKind.SingleApplyAPI
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'Invalid': pxr.Usd.SchemaKind.Invalid, 'AbstractBase': pxr.Usd.SchemaKind.AbstractBase, 'AbstractTyped': pxr.Usd.SchemaKind.AbstractTyped, 'ConcreteTyped': pxr.Usd.SchemaKind.ConcreteTyped, 'NonAppliedAPI': pxr.Usd.SchemaKind.NonAppliedAPI, 'SingleApplyAPI': pxr.Usd.SchemaKind.SingleApplyAPI, 'MultipleApplyAPI': pxr.Usd.SchemaKind.MultipleApplyAPI}
    values: typing.ClassVar[dict]  # value = {0: pxr.Usd.SchemaKind.Invalid, 1: pxr.Usd.SchemaKind.AbstractBase, 2: pxr.Usd.SchemaKind.AbstractTyped, 3: pxr.Usd.SchemaKind.ConcreteTyped, 4: pxr.Usd.SchemaKind.NonAppliedAPI, 5: pxr.Usd.SchemaKind.SingleApplyAPI, 6: pxr.Usd.SchemaKind.MultipleApplyAPI}
class SchemaRegistry(Boost.Python.instance):
    class SchemaInfo(Boost.Python.instance):
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
        def family(*args, **kwargs):
            ...
        @property
        def identifier(*args, **kwargs):
            ...
        @property
        def kind(*args, **kwargs):
            ...
        @property
        def type(*args, **kwargs):
            ...
        @property
        def version(*args, **kwargs):
            ...
    class VersionPolicy(Boost.Python.enum):
        All: typing.ClassVar[VersionPolicy]  # value = pxr.Usd.VersionPolicy.All
        GreaterThan: typing.ClassVar[VersionPolicy]  # value = pxr.Usd.VersionPolicy.GreaterThan
        GreaterThanOrEqual: typing.ClassVar[VersionPolicy]  # value = pxr.Usd.VersionPolicy.GreaterThanOrEqual
        LessThan: typing.ClassVar[VersionPolicy]  # value = pxr.Usd.VersionPolicy.LessThan
        LessThanOrEqual: typing.ClassVar[VersionPolicy]  # value = pxr.Usd.VersionPolicy.LessThanOrEqual
        __slots__: typing.ClassVar[tuple] = tuple()
        names: typing.ClassVar[dict]  # value = {'All': pxr.Usd.VersionPolicy.All, 'GreaterThan': pxr.Usd.VersionPolicy.GreaterThan, 'GreaterThanOrEqual': pxr.Usd.VersionPolicy.GreaterThanOrEqual, 'LessThan': pxr.Usd.VersionPolicy.LessThan, 'LessThanOrEqual': pxr.Usd.VersionPolicy.LessThanOrEqual}
        values: typing.ClassVar[dict]  # value = {0: pxr.Usd.VersionPolicy.All, 1: pxr.Usd.VersionPolicy.GreaterThan, 2: pxr.Usd.VersionPolicy.GreaterThanOrEqual, 3: pxr.Usd.VersionPolicy.LessThan, 4: pxr.Usd.VersionPolicy.LessThanOrEqual}
    @staticmethod
    def BuildComposedPrimDefinition(*args, **kwargs):
        ...
    @staticmethod
    def FindAppliedAPIPrimDefinition(*args, **kwargs):
        ...
    @staticmethod
    def FindConcretePrimDefinition(*args, **kwargs):
        ...
    @staticmethod
    def FindSchemaInfo(*args, **kwargs):
        ...
    @staticmethod
    def FindSchemaInfosInFamily(*args, **kwargs):
        ...
    @staticmethod
    def GetAPISchemaCanOnlyApplyToTypeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetAPISchemaTypeName(*args, **kwargs):
        ...
    @staticmethod
    def GetAPITypeFromSchemaTypeName(*args, **kwargs):
        ...
    @staticmethod
    def GetAutoApplyAPISchemas(*args, **kwargs):
        ...
    @staticmethod
    def GetConcreteSchemaTypeName(*args, **kwargs):
        ...
    @staticmethod
    def GetConcreteTypeFromSchemaTypeName(*args, **kwargs):
        ...
    @staticmethod
    def GetEmptyPrimDefinition(*args, **kwargs):
        ...
    @staticmethod
    def GetFallbackPrimTypes(*args, **kwargs):
        ...
    @staticmethod
    def GetMultipleApplyNameTemplateBaseName(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaKind(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaTypeName(*args, **kwargs):
        ...
    @staticmethod
    def GetTypeFromName(*args, **kwargs):
        ...
    @staticmethod
    def GetTypeFromSchemaTypeName(*args, **kwargs):
        ...
    @staticmethod
    def GetTypeNameAndInstance(*args, **kwargs):
        ...
    @staticmethod
    def IsAbstract(*args, **kwargs):
        ...
    @staticmethod
    def IsAllowedAPISchemaInstanceName(*args, **kwargs):
        ...
    @staticmethod
    def IsAllowedSchemaFamily(*args, **kwargs):
        ...
    @staticmethod
    def IsAllowedSchemaIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def IsAppliedAPISchema(*args, **kwargs):
        ...
    @staticmethod
    def IsConcrete(*args, **kwargs):
        ...
    @staticmethod
    def IsDisallowedField(*args, **kwargs):
        ...
    @staticmethod
    def IsMultipleApplyAPISchema(*args, **kwargs):
        ...
    @staticmethod
    def IsMultipleApplyNameTemplate(*args, **kwargs):
        ...
    @staticmethod
    def IsTyped(*args, **kwargs):
        ...
    @staticmethod
    def MakeMultipleApplyNameInstance(*args, **kwargs):
        ...
    @staticmethod
    def MakeMultipleApplyNameTemplate(*args, **kwargs):
        ...
    @staticmethod
    def MakeSchemaIdentifierForFamilyAndVersion(*args, **kwargs):
        ...
    @staticmethod
    def ParseSchemaFamilyAndVersionFromIdentifier(*args, **kwargs):
        ...
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
        ...
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
    def __new__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
class Specializes(Boost.Python.instance):
    @staticmethod
    def AddSpecialize(*args, **kwargs):
        ...
    @staticmethod
    def ClearSpecializes(*args, **kwargs):
        ...
    @staticmethod
    def GetPrim(*args, **kwargs):
        ...
    @staticmethod
    def RemoveSpecialize(*args, **kwargs):
        ...
    @staticmethod
    def SetSpecializes(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
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
class Stage(Boost.Python.instance):
    class InitialLoadSet(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'Stage'
        allValues: typing.ClassVar[tuple]  # value = (Usd.Stage.LoadAll, Usd.Stage.LoadNone)
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
    LoadAll: typing.ClassVar[InitialLoadSet]  # value = Usd.Stage.LoadAll
    LoadNone: typing.ClassVar[InitialLoadSet]  # value = Usd.Stage.LoadNone
    @staticmethod
    def ClearDefaultPrim(*args, **kwargs):
        ...
    @staticmethod
    def ClearMetadata(*args, **kwargs):
        ...
    @staticmethod
    def ClearMetadataByDictKey(*args, **kwargs):
        ...
    @staticmethod
    def CreateClassPrim(*args, **kwargs):
        ...
    @staticmethod
    def CreateInMemory(*args, **kwargs):
        ...
    @staticmethod
    def CreateNew(*args, **kwargs):
        ...
    @staticmethod
    def DefinePrim(*args, **kwargs):
        ...
    @staticmethod
    def ExpandPopulationMask(*args, **kwargs):
        ...
    @staticmethod
    def Export(*args, **kwargs):
        ...
    @staticmethod
    def ExportToString(*args, **kwargs):
        ...
    @staticmethod
    def FindLoadable(*args, **kwargs):
        ...
    @staticmethod
    def Flatten(*args, **kwargs):
        ...
    @staticmethod
    def GetAttributeAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetColorConfigFallbacks(*args, **kwargs):
        ...
    @staticmethod
    def GetColorConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def GetColorManagementSystem(*args, **kwargs):
        ...
    @staticmethod
    def GetDefaultPrim(*args, **kwargs):
        ...
    @staticmethod
    def GetEditTarget(*args, **kwargs):
        ...
    @staticmethod
    def GetEditTargetForLocalLayer(*args, **kwargs):
        ...
    @staticmethod
    def GetEndTimeCode(*args, **kwargs):
        ...
    @staticmethod
    def GetFramesPerSecond(*args, **kwargs):
        ...
    @staticmethod
    def GetGlobalVariantFallbacks(*args, **kwargs):
        ...
    @staticmethod
    def GetInterpolationType(*args, **kwargs):
        ...
    @staticmethod
    def GetLayerStack(*args, **kwargs):
        ...
    @staticmethod
    def GetLoadRules(*args, **kwargs):
        ...
    @staticmethod
    def GetLoadSet(*args, **kwargs):
        ...
    @staticmethod
    def GetMetadata(*args, **kwargs):
        ...
    @staticmethod
    def GetMetadataByDictKey(*args, **kwargs):
        ...
    @staticmethod
    def GetMutedLayers(*args, **kwargs):
        ...
    @staticmethod
    def GetObjectAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetPathResolverContext(*args, **kwargs):
        ...
    @staticmethod
    def GetPopulationMask(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetPrototypes(*args, **kwargs):
        ...
    @staticmethod
    def GetPseudoRoot(*args, **kwargs):
        ...
    @staticmethod
    def GetRelationshipAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetRootLayer(*args, **kwargs):
        ...
    @staticmethod
    def GetSessionLayer(*args, **kwargs):
        ...
    @staticmethod
    def GetStartTimeCode(*args, **kwargs):
        ...
    @staticmethod
    def GetTimeCodesPerSecond(*args, **kwargs):
        ...
    @staticmethod
    def GetUsedLayers(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredMetadata(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredMetadataDictKey(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredTimeCodeRange(*args, **kwargs):
        ...
    @staticmethod
    def HasDefaultPrim(*args, **kwargs):
        ...
    @staticmethod
    def HasLocalLayer(*args, **kwargs):
        ...
    @staticmethod
    def HasMetadata(*args, **kwargs):
        ...
    @staticmethod
    def HasMetadataDictKey(*args, **kwargs):
        ...
    @staticmethod
    def IsLayerMuted(*args, **kwargs):
        ...
    @staticmethod
    def IsSupportedFile(*args, **kwargs):
        ...
    @staticmethod
    def Load(*args, **kwargs):
        ...
    @staticmethod
    def LoadAndUnload(*args, **kwargs):
        ...
    @staticmethod
    def MuteAndUnmuteLayers(*args, **kwargs):
        ...
    @staticmethod
    def MuteLayer(*args, **kwargs):
        ...
    @staticmethod
    def Open(*args, **kwargs):
        ...
    @staticmethod
    def OpenMasked(*args, **kwargs):
        ...
    @staticmethod
    def OverridePrim(*args, **kwargs):
        ...
    @staticmethod
    def Reload(*args, **kwargs):
        ...
    @staticmethod
    def RemovePrim(*args, **kwargs):
        ...
    @staticmethod
    def ResolveIdentifierToEditTarget(*args, **kwargs):
        ...
    @staticmethod
    def Save(*args, **kwargs):
        ...
    @staticmethod
    def SaveSessionLayers(*args, **kwargs):
        ...
    @staticmethod
    def SetColorConfigFallbacks(*args, **kwargs):
        ...
    @staticmethod
    def SetColorConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def SetColorManagementSystem(*args, **kwargs):
        ...
    @staticmethod
    def SetDefaultPrim(*args, **kwargs):
        ...
    @staticmethod
    def SetEditTarget(*args, **kwargs):
        ...
    @staticmethod
    def SetEndTimeCode(*args, **kwargs):
        ...
    @staticmethod
    def SetFramesPerSecond(*args, **kwargs):
        ...
    @staticmethod
    def SetGlobalVariantFallbacks(*args, **kwargs):
        ...
    @staticmethod
    def SetInterpolationType(*args, **kwargs):
        ...
    @staticmethod
    def SetLoadRules(*args, **kwargs):
        ...
    @staticmethod
    def SetMetadata(*args, **kwargs):
        ...
    @staticmethod
    def SetMetadataByDictKey(*args, **kwargs):
        ...
    @staticmethod
    def SetPopulationMask(*args, **kwargs):
        ...
    @staticmethod
    def SetStartTimeCode(*args, **kwargs):
        ...
    @staticmethod
    def SetTimeCodesPerSecond(*args, **kwargs):
        ...
    @staticmethod
    def Traverse(*args, **kwargs):
        ...
    @staticmethod
    def TraverseAll(*args, **kwargs):
        ...
    @staticmethod
    def Unload(*args, **kwargs):
        ...
    @staticmethod
    def UnmuteLayer(*args, **kwargs):
        ...
    @staticmethod
    def WriteFallbackPrimTypes(*args, **kwargs):
        ...
    @staticmethod
    def _GetPcpCache(*args, **kwargs):
        ...
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
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
class StageCache(Boost.Python.instance):
    class Id(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 32
        @staticmethod
        def FromLongInt(*args, **kwargs):
            ...
        @staticmethod
        def FromString(*args, **kwargs):
            ...
        @staticmethod
        def IsValid(*args, **kwargs):
            ...
        @staticmethod
        def ToLongInt(*args, **kwargs):
            ...
        @staticmethod
        def ToString(*args, **kwargs):
            ...
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
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def Contains(*args, **kwargs):
        ...
    @staticmethod
    def Erase(*args, **kwargs):
        ...
    @staticmethod
    def EraseAll(*args, **kwargs):
        ...
    @staticmethod
    def Find(*args, **kwargs):
        ...
    @staticmethod
    def FindAllMatching(*args, **kwargs):
        ...
    @staticmethod
    def FindOneMatching(*args, **kwargs):
        ...
    @staticmethod
    def GetAllStages(*args, **kwargs):
        ...
    @staticmethod
    def GetDebugName(*args, **kwargs):
        ...
    @staticmethod
    def GetId(*args, **kwargs):
        ...
    @staticmethod
    def Insert(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def SetDebugName(*args, **kwargs):
        ...
    @staticmethod
    def Size(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class StageCacheContext(Boost.Python.instance):
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
class StageCacheContextBlockType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Usd.BlockStageCaches, Usd.BlockStageCachePopulation, Usd._NoBlock)
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
class StageLoadRules(Boost.Python.instance):
    class Rule(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'StageLoadRules'
        allValues: typing.ClassVar[tuple]  # value = (Usd.StageLoadRules.AllRule, Usd.StageLoadRules.OnlyRule, Usd.StageLoadRules.NoneRule)
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
    AllRule: typing.ClassVar[Rule]  # value = Usd.StageLoadRules.AllRule
    NoneRule: typing.ClassVar[Rule]  # value = Usd.StageLoadRules.NoneRule
    OnlyRule: typing.ClassVar[Rule]  # value = Usd.StageLoadRules.OnlyRule
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def AddRule(*args, **kwargs):
        ...
    @staticmethod
    def GetEffectiveRuleForPath(*args, **kwargs):
        ...
    @staticmethod
    def GetRules(*args, **kwargs):
        ...
    @staticmethod
    def IsLoaded(*args, **kwargs):
        ...
    @staticmethod
    def IsLoadedWithAllDescendants(*args, **kwargs):
        ...
    @staticmethod
    def IsLoadedWithNoDescendants(*args, **kwargs):
        ...
    @staticmethod
    def LoadAll(*args, **kwargs):
        ...
    @staticmethod
    def LoadAndUnload(*args, **kwargs):
        ...
    @staticmethod
    def LoadNone(*args, **kwargs):
        ...
    @staticmethod
    def LoadWithDescendants(*args, **kwargs):
        ...
    @staticmethod
    def LoadWithoutDescendants(*args, **kwargs):
        ...
    @staticmethod
    def Minimize(*args, **kwargs):
        ...
    @staticmethod
    def SetRules(*args, **kwargs):
        ...
    @staticmethod
    def Unload(*args, **kwargs):
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
    @staticmethod
    def swap(*args, **kwargs):
        ...
class StagePopulationMask(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Add(*args, **kwargs):
        ...
    @staticmethod
    def All(*args, **kwargs):
        ...
    @staticmethod
    def GetIncludedChildNames(*args, **kwargs):
        ...
    @staticmethod
    def GetIntersection(*args, **kwargs):
        ...
    @staticmethod
    def GetPaths(*args, **kwargs):
        ...
    @staticmethod
    def GetUnion(*args, **kwargs):
        ...
    @staticmethod
    def Includes(*args, **kwargs):
        ...
    @staticmethod
    def IncludesSubtree(*args, **kwargs):
        ...
    @staticmethod
    def Intersection(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def Union(*args, **kwargs):
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
class TimeCode(Boost.Python.instance):
    class Tokens(Boost.Python.instance):
        DEFAULT: typing.ClassVar[str] = 'DEFAULT'
        EARLIEST: typing.ClassVar[str] = 'EARLIEST'
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def Default(*args, **kwargs):
        ...
    @staticmethod
    def EarliestTime(*args, **kwargs):
        ...
    @staticmethod
    def GetValue(*args, **kwargs):
        ...
    @staticmethod
    def IsDefault(*args, **kwargs):
        ...
    @staticmethod
    def IsEarliestTime(*args, **kwargs):
        ...
    @staticmethod
    def IsNumeric(*args, **kwargs):
        ...
    @staticmethod
    def SafeStep(*args, **kwargs):
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
class Tokens(Boost.Python.instance):
    APISchemaBase: typing.ClassVar[str] = 'APISchemaBase'
    ClipsAPI: typing.ClassVar[str] = 'ClipsAPI'
    CollectionAPI: typing.ClassVar[str] = 'CollectionAPI'
    ModelAPI: typing.ClassVar[str] = 'ModelAPI'
    Typed: typing.ClassVar[str] = 'Typed'
    apiSchemas: typing.ClassVar[str] = 'apiSchemas'
    clipSets: typing.ClassVar[str] = 'clipSets'
    clips: typing.ClassVar[str] = 'clips'
    collection: typing.ClassVar[str] = 'collection'
    collection_MultipleApplyTemplate_: typing.ClassVar[str] = 'collection:__INSTANCE_NAME__'
    collection_MultipleApplyTemplate_Excludes: typing.ClassVar[str] = 'collection:__INSTANCE_NAME__:excludes'
    collection_MultipleApplyTemplate_ExpansionRule: typing.ClassVar[str] = 'collection:__INSTANCE_NAME__:expansionRule'
    collection_MultipleApplyTemplate_IncludeRoot: typing.ClassVar[str] = 'collection:__INSTANCE_NAME__:includeRoot'
    collection_MultipleApplyTemplate_Includes: typing.ClassVar[str] = 'collection:__INSTANCE_NAME__:includes'
    collection_MultipleApplyTemplate_MembershipExpression: typing.ClassVar[str] = 'collection:__INSTANCE_NAME__:membershipExpression'
    exclude: typing.ClassVar[str] = 'exclude'
    expandPrims: typing.ClassVar[str] = 'expandPrims'
    expandPrimsAndProperties: typing.ClassVar[str] = 'expandPrimsAndProperties'
    explicitOnly: typing.ClassVar[str] = 'explicitOnly'
    fallbackPrimTypes: typing.ClassVar[str] = 'fallbackPrimTypes'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Typed(SchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class UsdCollectionMembershipQuery(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 208
    @staticmethod
    def GetAsPathExpansionRuleMap(*args, **kwargs):
        ...
    @staticmethod
    def GetIncludedCollections(*args, **kwargs):
        ...
    @staticmethod
    def HasExcludes(*args, **kwargs):
        ...
    @staticmethod
    def IsPathIncluded(*args, **kwargs):
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
class UsdFileFormat(pxr.Sdf.FileFormat):
    class Tokens(Boost.Python.instance):
        FormatArg: typing.ClassVar[str] = 'format'
        Id: typing.ClassVar[str] = 'usd'
        Target: typing.ClassVar[str] = 'usd'
        Version: typing.ClassVar[str] = '1.0'
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
    def GetUnderlyingFormatForLayer(*args, **kwargs):
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
class VariantSet(Boost.Python.instance):
    @staticmethod
    def AddVariant(*args, **kwargs):
        ...
    @staticmethod
    def BlockVariantSelection(*args, **kwargs):
        ...
    @staticmethod
    def ClearVariantSelection(*args, **kwargs):
        ...
    @staticmethod
    def GetName(*args, **kwargs):
        ...
    @staticmethod
    def GetPrim(*args, **kwargs):
        ...
    @staticmethod
    def GetVariantEditContext(*args, **kwargs):
        ...
    @staticmethod
    def GetVariantEditTarget(*args, **kwargs):
        ...
    @staticmethod
    def GetVariantNames(*args, **kwargs):
        ...
    @staticmethod
    def GetVariantSelection(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredVariant(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredVariantSelection(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        ...
    @staticmethod
    def SetVariantSelection(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
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
class VariantSets(Boost.Python.instance):
    @staticmethod
    def AddVariantSet(*args, **kwargs):
        ...
    @staticmethod
    def GetAllVariantSelections(*args, **kwargs):
        ...
    @staticmethod
    def GetNames(*args, **kwargs):
        ...
    @staticmethod
    def GetVariantSelection(*args, **kwargs):
        ...
    @staticmethod
    def GetVariantSet(*args, **kwargs):
        ...
    @staticmethod
    def HasVariantSet(*args, **kwargs):
        ...
    @staticmethod
    def SetSelection(*args, **kwargs):
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
class ZipFile(Boost.Python.instance):
    class FileInfo(Boost.Python.instance):
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
        def compressionMethod(*args, **kwargs):
            ...
        @property
        def crc(*args, **kwargs):
            ...
        @property
        def dataOffset(*args, **kwargs):
            ...
        @property
        def encrypted(*args, **kwargs):
            ...
        @property
        def size(*args, **kwargs):
            ...
        @property
        def uncompressedSize(*args, **kwargs):
            ...
    @staticmethod
    def DumpContents(*args, **kwargs):
        ...
    @staticmethod
    def GetFile(*args, **kwargs):
        ...
    @staticmethod
    def GetFileInfo(*args, **kwargs):
        ...
    @staticmethod
    def GetFileNames(*args, **kwargs):
        ...
    @staticmethod
    def Open(*args, **kwargs):
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
class ZipFileWriter(Boost.Python.instance):
    @staticmethod
    def AddFile(*args, **kwargs):
        ...
    @staticmethod
    def CreateNew(*args, **kwargs):
        ...
    @staticmethod
    def Discard(*args, **kwargs):
        ...
    @staticmethod
    def Save(*args, **kwargs):
        ...
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
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
class _CanApplyAPIResult(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
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
    def whyNot(*args, **kwargs):
        ...
class _CanApplyResult(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
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
    def whyNot(*args, **kwargs):
        ...
class _NonPopulatingStageCacheWrapper(Boost.Python.instance):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class _PrimFlagsConjunction(_PrimFlagsPredicate):
    @staticmethod
    def __and__(*args, **kwargs):
        ...
    @staticmethod
    def __iand__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __invert__(*args, **kwargs):
        ...
    @staticmethod
    def __rand__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class _PrimFlagsDisjunction(_PrimFlagsPredicate):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __invert__(*args, **kwargs):
        ...
    @staticmethod
    def __ior__(*args, **kwargs):
        ...
    @staticmethod
    def __or__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __ror__(*args, **kwargs):
        ...
class _PrimFlagsPredicate(Boost.Python.instance):
    @staticmethod
    def Contradiction(*args, **kwargs):
        ...
    @staticmethod
    def Tautology(*args, **kwargs):
        ...
    @staticmethod
    def __call__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
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
class _Term(Boost.Python.instance):
    @staticmethod
    def __and__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __invert__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __or__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class _UsdNamespaceEditorCanEditResult(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
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
    def whyNot(*args, **kwargs):
        ...
BlockStageCachePopulation: StageCacheContextBlockType  # value = Usd.BlockStageCachePopulation
BlockStageCaches: StageCacheContextBlockType  # value = Usd.BlockStageCaches
InterpolationTypeHeld: InterpolationType  # value = Usd.InterpolationTypeHeld
InterpolationTypeLinear: InterpolationType  # value = Usd.InterpolationTypeLinear
ListPositionBackOfAppendList: ListPosition  # value = Usd.ListPositionBackOfAppendList
ListPositionBackOfPrependList: ListPosition  # value = Usd.ListPositionBackOfPrependList
ListPositionFrontOfAppendList: ListPosition  # value = Usd.ListPositionFrontOfAppendList
ListPositionFrontOfPrependList: ListPosition  # value = Usd.ListPositionFrontOfPrependList
LoadWithDescendants: LoadPolicy  # value = Usd.LoadWithDescendants
LoadWithoutDescendants: LoadPolicy  # value = Usd.LoadWithoutDescendants
PrimAllPrimsPredicate: _PrimFlagsPredicate  # value = <pxr.Usd._PrimFlagsPredicate object>
PrimDefaultPredicate: _PrimFlagsConjunction  # value = <pxr.Usd._PrimFlagsConjunction object>
PrimHasDefiningSpecifier: _Term  # value = <pxr.Usd._Term object>
PrimIsAbstract: _Term  # value = <pxr.Usd._Term object>
PrimIsActive: _Term  # value = <pxr.Usd._Term object>
PrimIsDefined: _Term  # value = <pxr.Usd._Term object>
PrimIsGroup: _Term  # value = <pxr.Usd._Term object>
PrimIsInstance: _Term  # value = <pxr.Usd._Term object>
PrimIsLoaded: _Term  # value = <pxr.Usd._Term object>
PrimIsModel: _Term  # value = <pxr.Usd._Term object>
ResolveInfoSourceDefault: ResolveInfoSource  # value = Usd.ResolveInfoSourceDefault
ResolveInfoSourceFallback: ResolveInfoSource  # value = Usd.ResolveInfoSourceFallback
ResolveInfoSourceNone: ResolveInfoSource  # value = Usd.ResolveInfoSourceNone
ResolveInfoSourceTimeSamples: ResolveInfoSource  # value = Usd.ResolveInfoSourceTimeSamples
ResolveInfoSourceValueClips: ResolveInfoSource  # value = Usd.ResolveInfoSourceValueClips
_NoBlock: StageCacheContextBlockType  # value = Usd._NoBlock
__MFB_FULL_PACKAGE_NAME: str = 'usd'
