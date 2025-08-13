from __future__ import annotations
import pxr.Usd
import pxr.UsdGeom
import typing
__all__: list[str] = ['AnimMapper', 'AnimQuery', 'Animation', 'Binding', 'BindingAPI', 'BlendShape', 'BlendShapeQuery', 'Cache', 'InbetweenShape', 'Root', 'Skeleton', 'SkeletonQuery', 'SkinningQuery', 'Tokens', 'Topology']
class AnimMapper(Boost.Python.instance):
    @staticmethod
    def IsIdentity(*args, **kwargs):
        ...
    @staticmethod
    def IsNull(*args, **kwargs):
        ...
    @staticmethod
    def IsSparse(*args, **kwargs):
        ...
    @staticmethod
    def Remap(*args, **kwargs):
        ...
    @staticmethod
    def RemapTransforms(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class AnimQuery(Boost.Python.instance):
    @staticmethod
    def BlendShapeWeightsMightBeTimeVarying(*args, **kwargs):
        ...
    @staticmethod
    def ComputeBlendShapeWeights(*args, **kwargs):
        ...
    @staticmethod
    def ComputeJointLocalTransformComponents(*args, **kwargs):
        ...
    @staticmethod
    def ComputeJointLocalTransforms(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapeOrder(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapeWeightTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapeWeightTimeSamplesInInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetJointOrder(*args, **kwargs):
        ...
    @staticmethod
    def GetJointTransformTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetJointTransformTimeSamplesInInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetPrim(*args, **kwargs):
        ...
    @staticmethod
    def JointTransformsMightBeTimeVarying(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
class Animation(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateBlendShapeWeightsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateBlendShapesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateJointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRotationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateScalesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTranslationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapeWeightsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetJointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRotationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetScalesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTransforms(*args, **kwargs):
        ...
    @staticmethod
    def GetTranslationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def SetTransforms(*args, **kwargs):
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
class Binding(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 88
    @staticmethod
    def GetSkeleton(*args, **kwargs):
        ...
    @staticmethod
    def GetSkinningTargets(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class BindingAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateAnimationSourceRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateBlendShapeTargetsRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateBlendShapesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGeomBindTransformAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateJointIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateJointIndicesPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def CreateJointWeightsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateJointWeightsPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def CreateJointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSkeletonRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateSkinningMethodAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAnimationSource(*args, **kwargs):
        ...
    @staticmethod
    def GetAnimationSourceRel(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapeTargetsRel(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGeomBindTransformAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetInheritedAnimationSource(*args, **kwargs):
        ...
    @staticmethod
    def GetInheritedSkeleton(*args, **kwargs):
        ...
    @staticmethod
    def GetJointIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetJointIndicesPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def GetJointWeightsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetJointWeightsPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def GetJointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSkeleton(*args, **kwargs):
        ...
    @staticmethod
    def GetSkeletonRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSkinningMethodAttr(*args, **kwargs):
        ...
    @staticmethod
    def SetRigidJointInfluence(*args, **kwargs):
        ...
    @staticmethod
    def ValidateJointIndices(*args, **kwargs):
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
class BlendShape(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateInbetween(*args, **kwargs):
        ...
    @staticmethod
    def CreateNormalOffsetsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOffsetsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePointIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAuthoredInbetweens(*args, **kwargs):
        ...
    @staticmethod
    def GetInbetween(*args, **kwargs):
        ...
    @staticmethod
    def GetInbetweens(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalOffsetsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOffsetsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPointIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def HasInbetween(*args, **kwargs):
        ...
    @staticmethod
    def ValidatePointIndices(*args, **kwargs):
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
class BlendShapeQuery(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 128
    @staticmethod
    def ComputeBlendShapePointIndices(*args, **kwargs):
        ...
    @staticmethod
    def ComputeDeformedPoints(*args, **kwargs):
        ...
    @staticmethod
    def ComputeSubShapePointOffsets(*args, **kwargs):
        ...
    @staticmethod
    def ComputeSubShapeWeights(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShape(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapeIndex(*args, **kwargs):
        ...
    @staticmethod
    def GetInbetween(*args, **kwargs):
        ...
    @staticmethod
    def GetNumBlendShapes(*args, **kwargs):
        ...
    @staticmethod
    def GetNumSubShapes(*args, **kwargs):
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
class Cache(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ComputeSkelBinding(*args, **kwargs):
        ...
    @staticmethod
    def ComputeSkelBindings(*args, **kwargs):
        ...
    @staticmethod
    def GetAnimQuery(*args, **kwargs):
        ...
    @staticmethod
    def GetSkelQuery(*args, **kwargs):
        ...
    @staticmethod
    def GetSkinningQuery(*args, **kwargs):
        ...
    @staticmethod
    def Populate(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class InbetweenShape(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def CreateNormalOffsetsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalOffsets(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalOffsetsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOffsets(*args, **kwargs):
        ...
    @staticmethod
    def GetWeight(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredWeight(*args, **kwargs):
        ...
    @staticmethod
    def IsDefined(*args, **kwargs):
        ...
    @staticmethod
    def IsInbetween(*args, **kwargs):
        ...
    @staticmethod
    def SetNormalOffsets(*args, **kwargs):
        ...
    @staticmethod
    def SetOffsets(*args, **kwargs):
        ...
    @staticmethod
    def SetWeight(*args, **kwargs):
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
    def __reduce__(*args, **kwargs):
        ...
class Root(pxr.UsdGeom.Boundable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Find(*args, **kwargs):
        ...
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
class Skeleton(pxr.UsdGeom.Boundable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateBindTransformsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateJointNamesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateJointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRestTransformsAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetBindTransformsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetJointNamesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetJointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRestTransformsAttr(*args, **kwargs):
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
class SkeletonQuery(Boost.Python.instance):
    @staticmethod
    def ComputeJointLocalTransforms(*args, **kwargs):
        ...
    @staticmethod
    def ComputeJointRestRelativeTransforms(*args, **kwargs):
        ...
    @staticmethod
    def ComputeJointSkelTransforms(*args, **kwargs):
        ...
    @staticmethod
    def ComputeJointWorldTransforms(*args, **kwargs):
        ...
    @staticmethod
    def ComputeSkinningTransforms(*args, **kwargs):
        ...
    @staticmethod
    def GetAnimQuery(*args, **kwargs):
        ...
    @staticmethod
    def GetJointOrder(*args, **kwargs):
        ...
    @staticmethod
    def GetJointWorldBindTransforms(*args, **kwargs):
        ...
    @staticmethod
    def GetMapper(*args, **kwargs):
        ...
    @staticmethod
    def GetPrim(*args, **kwargs):
        ...
    @staticmethod
    def GetSkeleton(*args, **kwargs):
        ...
    @staticmethod
    def GetTopology(*args, **kwargs):
        ...
    @staticmethod
    def HasBindPose(*args, **kwargs):
        ...
    @staticmethod
    def HasRestPose(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
class SkinningQuery(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 424
    @staticmethod
    def ComputeExtentsPadding(*args, **kwargs):
        ...
    @staticmethod
    def ComputeJointInfluences(*args, **kwargs):
        ...
    @staticmethod
    def ComputeSkinnedPoints(*args, **kwargs):
        ...
    @staticmethod
    def ComputeSkinnedTransform(*args, **kwargs):
        ...
    @staticmethod
    def ComputeVaryingJointInfluences(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapeMapper(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapeOrder(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapeTargetsRel(*args, **kwargs):
        ...
    @staticmethod
    def GetBlendShapesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGeomBindTransform(*args, **kwargs):
        ...
    @staticmethod
    def GetGeomBindTransformAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetInterpolation(*args, **kwargs):
        ...
    @staticmethod
    def GetJointIndicesPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def GetJointMapper(*args, **kwargs):
        ...
    @staticmethod
    def GetJointOrder(*args, **kwargs):
        ...
    @staticmethod
    def GetJointWeightsPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def GetMapper(*args, **kwargs):
        ...
    @staticmethod
    def GetNumInfluencesPerComponent(*args, **kwargs):
        ...
    @staticmethod
    def GetPrim(*args, **kwargs):
        ...
    @staticmethod
    def GetSkinningMethod(*args, **kwargs):
        ...
    @staticmethod
    def GetSkinningMethodAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetTimeSamplesInInterval(*args, **kwargs):
        ...
    @staticmethod
    def HasBlendShapes(*args, **kwargs):
        ...
    @staticmethod
    def HasJointInfluences(*args, **kwargs):
        ...
    @staticmethod
    def IsRigidlyDeformed(*args, **kwargs):
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
    def __str__(*args, **kwargs):
        ...
class Tokens(Boost.Python.instance):
    BlendShape: typing.ClassVar[str] = 'BlendShape'
    SkelAnimation: typing.ClassVar[str] = 'SkelAnimation'
    SkelBindingAPI: typing.ClassVar[str] = 'SkelBindingAPI'
    SkelRoot: typing.ClassVar[str] = 'SkelRoot'
    Skeleton: typing.ClassVar[str] = 'Skeleton'
    bindTransforms: typing.ClassVar[str] = 'bindTransforms'
    blendShapeWeights: typing.ClassVar[str] = 'blendShapeWeights'
    blendShapes: typing.ClassVar[str] = 'blendShapes'
    classicLinear: typing.ClassVar[str] = 'classicLinear'
    dualQuaternion: typing.ClassVar[str] = 'dualQuaternion'
    jointNames: typing.ClassVar[str] = 'jointNames'
    joints: typing.ClassVar[str] = 'joints'
    normalOffsets: typing.ClassVar[str] = 'normalOffsets'
    offsets: typing.ClassVar[str] = 'offsets'
    pointIndices: typing.ClassVar[str] = 'pointIndices'
    primvarsSkelGeomBindTransform: typing.ClassVar[str] = 'primvars:skel:geomBindTransform'
    primvarsSkelJointIndices: typing.ClassVar[str] = 'primvars:skel:jointIndices'
    primvarsSkelJointWeights: typing.ClassVar[str] = 'primvars:skel:jointWeights'
    primvarsSkelSkinningMethod: typing.ClassVar[str] = 'primvars:skel:skinningMethod'
    restTransforms: typing.ClassVar[str] = 'restTransforms'
    rotations: typing.ClassVar[str] = 'rotations'
    scales: typing.ClassVar[str] = 'scales'
    skelAnimationSource: typing.ClassVar[str] = 'skel:animationSource'
    skelBlendShapeTargets: typing.ClassVar[str] = 'skel:blendShapeTargets'
    skelBlendShapes: typing.ClassVar[str] = 'skel:blendShapes'
    skelJoints: typing.ClassVar[str] = 'skel:joints'
    skelSkeleton: typing.ClassVar[str] = 'skel:skeleton'
    translations: typing.ClassVar[str] = 'translations'
    weight: typing.ClassVar[str] = 'weight'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Topology(Boost.Python.instance):
    @staticmethod
    def GetNumJoints(*args, **kwargs):
        ...
    @staticmethod
    def GetParent(*args, **kwargs):
        ...
    @staticmethod
    def GetParentIndices(*args, **kwargs):
        ...
    @staticmethod
    def IsRoot(*args, **kwargs):
        ...
    @staticmethod
    def Validate(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
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
__MFB_FULL_PACKAGE_NAME: str = 'usdSkel'
