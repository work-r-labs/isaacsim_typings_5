from __future__ import annotations
import pxr.Tf
import pxr.Usd
import typing
__all__: list[str] = ['BBoxCache', 'BasisCurves', 'Boundable', 'Camera', 'Capsule', 'Capsule_1', 'Cone', 'ConstraintTarget', 'Cube', 'Curves', 'Cylinder', 'Cylinder_1', 'Gprim', 'HermiteCurves', 'Imageable', 'LinearUnits', 'Mesh', 'ModelAPI', 'MotionAPI', 'NurbsCurves', 'NurbsPatch', 'Plane', 'PointBased', 'PointInstancer', 'Points', 'Primvar', 'PrimvarsAPI', 'Scope', 'Sphere', 'Subset', 'TetMesh', 'Tokens', 'VisibilityAPI', 'Xform', 'XformCache', 'XformCommonAPI', 'XformOp', 'XformOpTypes', 'Xformable']
class BBoxCache(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 504
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearBaseTime(*args, **kwargs):
        ...
    @staticmethod
    def ComputeLocalBound(*args, **kwargs):
        ...
    @staticmethod
    def ComputePointInstanceLocalBound(*args, **kwargs):
        ...
    @staticmethod
    def ComputePointInstanceLocalBounds(*args, **kwargs):
        ...
    @staticmethod
    def ComputePointInstanceRelativeBound(*args, **kwargs):
        ...
    @staticmethod
    def ComputePointInstanceRelativeBounds(*args, **kwargs):
        ...
    @staticmethod
    def ComputePointInstanceUntransformedBound(*args, **kwargs):
        ...
    @staticmethod
    def ComputePointInstanceUntransformedBounds(*args, **kwargs):
        ...
    @staticmethod
    def ComputePointInstanceWorldBound(*args, **kwargs):
        ...
    @staticmethod
    def ComputePointInstanceWorldBounds(*args, **kwargs):
        ...
    @staticmethod
    def ComputeRelativeBound(*args, **kwargs):
        ...
    @staticmethod
    def ComputeUntransformedBound(*args, **kwargs):
        ...
    @staticmethod
    def ComputeWorldBound(*args, **kwargs):
        ...
    @staticmethod
    def ComputeWorldBoundWithOverrides(*args, **kwargs):
        ...
    @staticmethod
    def GetBaseTime(*args, **kwargs):
        ...
    @staticmethod
    def GetIncludedPurposes(*args, **kwargs):
        ...
    @staticmethod
    def GetTime(*args, **kwargs):
        ...
    @staticmethod
    def GetUseExtentsHint(*args, **kwargs):
        ...
    @staticmethod
    def HasBaseTime(*args, **kwargs):
        ...
    @staticmethod
    def SetBaseTime(*args, **kwargs):
        ...
    @staticmethod
    def SetIncludedPurposes(*args, **kwargs):
        ...
    @staticmethod
    def SetTime(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class BasisCurves(Curves):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ComputeInterpolationForSize(*args, **kwargs):
        ...
    @staticmethod
    def ComputeUniformDataSize(*args, **kwargs):
        ...
    @staticmethod
    def ComputeVaryingDataSize(*args, **kwargs):
        ...
    @staticmethod
    def ComputeVertexDataSize(*args, **kwargs):
        ...
    @staticmethod
    def CreateBasisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWrapAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetBasisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWrapAttr(*args, **kwargs):
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
class Boundable(Xformable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ComputeExtent(*args, **kwargs):
        ...
    @staticmethod
    def ComputeExtentFromPlugins(*args, **kwargs):
        ...
    @staticmethod
    def CreateExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetExtentAttr(*args, **kwargs):
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
class Camera(Xformable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateClippingPlanesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateClippingRangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExposureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFStopAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFocalLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFocusDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHorizontalApertureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHorizontalApertureOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateProjectionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShutterCloseAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShutterOpenAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStereoRoleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVerticalApertureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVerticalApertureOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCamera(*args, **kwargs):
        ...
    @staticmethod
    def GetClippingPlanesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetClippingRangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExposureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFStopAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFocalLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFocusDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHorizontalApertureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHorizontalApertureOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetProjectionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetShutterCloseAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShutterOpenAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetStereoRoleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVerticalApertureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVerticalApertureOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def SetFromCamera(*args, **kwargs):
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
class Capsule(Gprim):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
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
class Capsule_1(Gprim):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRadiusBottomAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRadiusTopAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusBottomAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusTopAttr(*args, **kwargs):
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
class Cone(Gprim):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
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
class ConstraintTarget(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def ComputeInWorldSpace(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetConstraintAttrName(*args, **kwargs):
        ...
    @staticmethod
    def GetIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def IsDefined(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def SetIdentifier(*args, **kwargs):
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
class Cube(Gprim):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSizeAttr(*args, **kwargs):
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
class Curves(PointBased):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ComputeExtent(*args, **kwargs):
        ...
    @staticmethod
    def CreateCurveVertexCountsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWidthsAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCurveCount(*args, **kwargs):
        ...
    @staticmethod
    def GetCurveVertexCountsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetWidthsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWidthsInterpolation(*args, **kwargs):
        ...
    @staticmethod
    def SetWidthsInterpolation(*args, **kwargs):
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
class Cylinder(Gprim):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
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
class Cylinder_1(Gprim):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRadiusBottomAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRadiusTopAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusBottomAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusTopAttr(*args, **kwargs):
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
class Gprim(Boundable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateDisplayColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisplayColorPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisplayOpacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisplayOpacityPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def CreateDoubleSidedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOrientationAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplayColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplayColorPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplayOpacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplayOpacityPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def GetDoubleSidedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOrientationAttr(*args, **kwargs):
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
class HermiteCurves(Curves):
    class PointAndTangentArrays(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 104
        @staticmethod
        def GetPoints(*args, **kwargs):
            ...
        @staticmethod
        def GetTangents(*args, **kwargs):
            ...
        @staticmethod
        def Interleave(*args, **kwargs):
            ...
        @staticmethod
        def IsEmpty(*args, **kwargs):
            ...
        @staticmethod
        def Separate(*args, **kwargs):
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
        def __ne__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateTangentsAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTangentsAttr(*args, **kwargs):
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
class Imageable(pxr.Usd.Typed):
    class PurposeInfo(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 40
        @staticmethod
        def GetInheritablePurpose(*args, **kwargs):
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
        def __ne__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @property
        def isInheritable(*args, **kwargs):
            ...
        @isInheritable.setter
        def isInheritable(*args, **kwargs):
            ...
        @property
        def purpose(*args, **kwargs):
            ...
        @purpose.setter
        def purpose(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ComputeEffectiveVisibility(*args, **kwargs):
        ...
    @staticmethod
    def ComputeLocalBound(*args, **kwargs):
        ...
    @staticmethod
    def ComputeLocalToWorldTransform(*args, **kwargs):
        ...
    @staticmethod
    def ComputeParentToWorldTransform(*args, **kwargs):
        ...
    @staticmethod
    def ComputeProxyPrim(*args, **kwargs):
        """
        
        
        Returns None if neither this prim nor any of its ancestors has a valid renderProxy prim.  Otherwise, returns a tuple of (proxyPrim, renderPrimWithAuthoredProxyPrimRel)
        """
    @staticmethod
    def ComputePurpose(*args, **kwargs):
        ...
    @staticmethod
    def ComputePurposeInfo(*args, **kwargs):
        ...
    @staticmethod
    def ComputeUntransformedBound(*args, **kwargs):
        ...
    @staticmethod
    def ComputeVisibility(*args, **kwargs):
        ...
    @staticmethod
    def ComputeWorldBound(*args, **kwargs):
        ...
    @staticmethod
    def CreateProxyPrimRel(*args, **kwargs):
        ...
    @staticmethod
    def CreatePurposeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVisibilityAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetOrderedPurposeTokens(*args, **kwargs):
        ...
    @staticmethod
    def GetProxyPrimRel(*args, **kwargs):
        ...
    @staticmethod
    def GetPurposeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPurposeVisibilityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetVisibilityAttr(*args, **kwargs):
        ...
    @staticmethod
    def MakeInvisible(*args, **kwargs):
        ...
    @staticmethod
    def MakeVisible(*args, **kwargs):
        ...
    @staticmethod
    def SetProxyPrim(*args, **kwargs):
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
class LinearUnits(Boost.Python.instance):
    centimeters: typing.ClassVar[float] = 0.01
    feet: typing.ClassVar[float] = 0.3048
    inches: typing.ClassVar[float] = 0.0254
    kilometers: typing.ClassVar[float] = 1000.0
    lightYears: typing.ClassVar[float] = 9460730472580800.0
    meters: typing.ClassVar[float] = 1.0
    micrometers: typing.ClassVar[float] = 1e-06
    miles: typing.ClassVar[float] = 1609.344
    millimeters: typing.ClassVar[float] = 0.001
    nanometers: typing.ClassVar[float] = 1e-09
    yards: typing.ClassVar[float] = 0.9144
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Mesh(PointBased):
    SHARPNESS_INFINITE: typing.ClassVar[float] = 10.0
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateCornerIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCornerSharpnessesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCreaseIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCreaseLengthsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCreaseSharpnessesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFaceVaryingLinearInterpolationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFaceVertexCountsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFaceVertexIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHoleIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateInterpolateBoundaryAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSubdivisionSchemeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTriangleSubdivisionRuleAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCornerIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCornerSharpnessesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCreaseIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCreaseLengthsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCreaseSharpnessesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFaceCount(*args, **kwargs):
        ...
    @staticmethod
    def GetFaceVaryingLinearInterpolationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFaceVertexCountsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFaceVertexIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHoleIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetInterpolateBoundaryAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSubdivisionSchemeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTriangleSubdivisionRuleAttr(*args, **kwargs):
        ...
    @staticmethod
    def ValidateTopology(*args, **kwargs):
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
class ModelAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def ComputeExtentsHint(*args, **kwargs):
        ...
    @staticmethod
    def ComputeModelDrawMode(*args, **kwargs):
        ...
    @staticmethod
    def CreateConstraintTarget(*args, **kwargs):
        ...
    @staticmethod
    def CreateModelApplyDrawModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateModelCardGeometryAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateModelCardTextureXNegAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateModelCardTextureXPosAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateModelCardTextureYNegAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateModelCardTextureYPosAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateModelCardTextureZNegAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateModelCardTextureZPosAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateModelDrawModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateModelDrawModeColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetConstraintTarget(*args, **kwargs):
        ...
    @staticmethod
    def GetConstraintTargets(*args, **kwargs):
        ...
    @staticmethod
    def GetExtentsHint(*args, **kwargs):
        ...
    @staticmethod
    def GetExtentsHintAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetModelApplyDrawModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetModelCardGeometryAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetModelCardTextureXNegAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetModelCardTextureXPosAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetModelCardTextureYNegAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetModelCardTextureYPosAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetModelCardTextureZNegAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetModelCardTextureZPosAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetModelDrawModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetModelDrawModeColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def SetExtentsHint(*args, **kwargs):
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
class MotionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def ComputeMotionBlurScale(*args, **kwargs):
        ...
    @staticmethod
    def ComputeNonlinearSampleCount(*args, **kwargs):
        ...
    @staticmethod
    def ComputeVelocityScale(*args, **kwargs):
        ...
    @staticmethod
    def CreateMotionBlurScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNonlinearSampleCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVelocityScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetMotionBlurScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNonlinearSampleCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetVelocityScaleAttr(*args, **kwargs):
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
class NurbsCurves(Curves):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateKnotsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOrderAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePointWeightsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRangesAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetKnotsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOrderAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPointWeightsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRangesAttr(*args, **kwargs):
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
class NurbsPatch(PointBased):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreatePointWeightsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTrimCurveCountsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTrimCurveKnotsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTrimCurveOrdersAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTrimCurvePointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTrimCurveRangesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTrimCurveVertexCountsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUFormAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUKnotsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUOrderAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateURangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUVertexCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVFormAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVKnotsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVOrderAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVRangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVVertexCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetPointWeightsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTrimCurveCountsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTrimCurveKnotsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTrimCurveOrdersAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTrimCurvePointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTrimCurveRangesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTrimCurveVertexCountsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUFormAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUKnotsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUOrderAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetURangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUVertexCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVFormAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVKnotsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVOrderAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVRangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVVertexCountAttr(*args, **kwargs):
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
class Plane(Gprim):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDoubleSidedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDoubleSidedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetWidthAttr(*args, **kwargs):
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
class PointBased(Gprim):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ComputeExtent(*args, **kwargs):
        ...
    @staticmethod
    def ComputePointsAtTime(*args, **kwargs):
        ...
    @staticmethod
    def ComputePointsAtTimes(*args, **kwargs):
        ...
    @staticmethod
    def CreateAccelerationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNormalsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVelocitiesAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAccelerationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalsInterpolation(*args, **kwargs):
        ...
    @staticmethod
    def GetPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetVelocitiesAttr(*args, **kwargs):
        ...
    @staticmethod
    def SetNormalsInterpolation(*args, **kwargs):
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
class PointInstancer(Boundable):
    class MaskApplication(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'PointInstancer'
        allValues: typing.ClassVar[tuple]  # value = (UsdGeom.PointInstancer.ApplyMask, UsdGeom.PointInstancer.IgnoreMask)
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
    class ProtoXformInclusion(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'PointInstancer'
        allValues: typing.ClassVar[tuple]  # value = (UsdGeom.PointInstancer.IncludeProtoXform, UsdGeom.PointInstancer.ExcludeProtoXform)
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
    ApplyMask: typing.ClassVar[MaskApplication]  # value = UsdGeom.PointInstancer.ApplyMask
    ExcludeProtoXform: typing.ClassVar[ProtoXformInclusion]  # value = UsdGeom.PointInstancer.ExcludeProtoXform
    IgnoreMask: typing.ClassVar[MaskApplication]  # value = UsdGeom.PointInstancer.IgnoreMask
    IncludeProtoXform: typing.ClassVar[ProtoXformInclusion]  # value = UsdGeom.PointInstancer.IncludeProtoXform
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ActivateAllIds(*args, **kwargs):
        ...
    @staticmethod
    def ActivateId(*args, **kwargs):
        ...
    @staticmethod
    def ActivateIds(*args, **kwargs):
        ...
    @staticmethod
    def ComputeExtentAtTime(*args, **kwargs):
        ...
    @staticmethod
    def ComputeExtentAtTimes(*args, **kwargs):
        ...
    @staticmethod
    def ComputeInstanceTransformsAtTime(*args, **kwargs):
        ...
    @staticmethod
    def ComputeInstanceTransformsAtTimes(*args, **kwargs):
        ...
    @staticmethod
    def ComputeMaskAtTime(*args, **kwargs):
        ...
    @staticmethod
    def CreateAccelerationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateAngularVelocitiesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateIdsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateInvisibleIdsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOrientationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOrientationsfAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePositionsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateProtoIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePrototypesRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateScalesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVelocitiesAttr(*args, **kwargs):
        ...
    @staticmethod
    def DeactivateId(*args, **kwargs):
        ...
    @staticmethod
    def DeactivateIds(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAccelerationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetAngularVelocitiesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetIdsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetInstanceCount(*args, **kwargs):
        ...
    @staticmethod
    def GetInvisibleIdsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOrientationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOrientationsfAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPositionsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetProtoIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPrototypesRel(*args, **kwargs):
        ...
    @staticmethod
    def GetScalesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetVelocitiesAttr(*args, **kwargs):
        ...
    @staticmethod
    def InvisId(*args, **kwargs):
        ...
    @staticmethod
    def InvisIds(*args, **kwargs):
        ...
    @staticmethod
    def VisAllIds(*args, **kwargs):
        ...
    @staticmethod
    def VisId(*args, **kwargs):
        ...
    @staticmethod
    def VisIds(*args, **kwargs):
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
class Points(PointBased):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ComputeExtent(*args, **kwargs):
        ...
    @staticmethod
    def CreateIdsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWidthsAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetIdsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPointCount(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetWidthsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWidthsInterpolation(*args, **kwargs):
        ...
    @staticmethod
    def SetWidthsInterpolation(*args, **kwargs):
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
class Primvar(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def BlockIndices(*args, **kwargs):
        ...
    @staticmethod
    def ComputeFlattened(*args, **kwargs):
        ...
    @staticmethod
    def CreateIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetBaseName(*args, **kwargs):
        ...
    @staticmethod
    def GetDeclarationInfo(*args, **kwargs):
        ...
    @staticmethod
    def GetElementSize(*args, **kwargs):
        ...
    @staticmethod
    def GetIndices(*args, **kwargs):
        ...
    @staticmethod
    def GetIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetInterpolation(*args, **kwargs):
        ...
    @staticmethod
    def GetName(*args, **kwargs):
        ...
    @staticmethod
    def GetNamespace(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimvarName(*args, **kwargs):
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
    def GetUnauthoredValuesIndex(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredElementSize(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredInterpolation(*args, **kwargs):
        ...
    @staticmethod
    def HasAuthoredValue(*args, **kwargs):
        ...
    @staticmethod
    def HasValue(*args, **kwargs):
        ...
    @staticmethod
    def IsDefined(*args, **kwargs):
        ...
    @staticmethod
    def IsIdTarget(*args, **kwargs):
        ...
    @staticmethod
    def IsIndexed(*args, **kwargs):
        ...
    @staticmethod
    def IsPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def IsValidInterpolation(*args, **kwargs):
        ...
    @staticmethod
    def IsValidPrimvarName(*args, **kwargs):
        ...
    @staticmethod
    def NameContainsNamespaces(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def SetElementSize(*args, **kwargs):
        ...
    @staticmethod
    def SetIdTarget(*args, **kwargs):
        ...
    @staticmethod
    def SetIndices(*args, **kwargs):
        ...
    @staticmethod
    def SetInterpolation(*args, **kwargs):
        ...
    @staticmethod
    def SetUnauthoredValuesIndex(*args, **kwargs):
        ...
    @staticmethod
    def SplitName(*args, **kwargs):
        ...
    @staticmethod
    def StripPrimvarsName(*args, **kwargs):
        ...
    @staticmethod
    def ValueMightBeTimeVarying(*args, **kwargs):
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
class PrimvarsAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def BlockPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def CanContainPropertyName(*args, **kwargs):
        ...
    @staticmethod
    def CreateIndexedPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def CreateNonIndexedPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def CreatePrimvar(*args, **kwargs):
        ...
    @staticmethod
    def FindIncrementallyInheritablePrimvars(*args, **kwargs):
        ...
    @staticmethod
    def FindInheritablePrimvars(*args, **kwargs):
        ...
    @staticmethod
    def FindPrimvarWithInheritance(*args, **kwargs):
        ...
    @staticmethod
    def FindPrimvarsWithInheritance(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAuthoredPrimvars(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimvars(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimvarsWithAuthoredValues(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimvarsWithValues(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def HasPossiblyInheritedPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def HasPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def RemovePrimvar(*args, **kwargs):
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
class Scope(Imageable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Define(*args, **kwargs):
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
class Sphere(Gprim):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetExtentAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
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
class Subset(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateElementTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFamilyNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGeomSubset(*args, **kwargs):
        ...
    @staticmethod
    def CreateIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUniqueGeomSubset(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAllGeomSubsetFamilyNames(*args, **kwargs):
        ...
    @staticmethod
    def GetAllGeomSubsets(*args, **kwargs):
        ...
    @staticmethod
    def GetElementTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFamilyNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFamilyType(*args, **kwargs):
        ...
    @staticmethod
    def GetGeomSubsets(*args, **kwargs):
        ...
    @staticmethod
    def GetIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetUnassignedIndices(*args, **kwargs):
        ...
    @staticmethod
    def SetFamilyType(*args, **kwargs):
        ...
    @staticmethod
    def ValidateFamily(*args, **kwargs):
        ...
    @staticmethod
    def ValidateSubsets(*args, **kwargs):
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
class TetMesh(PointBased):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ComputeSurfaceFaces(*args, **kwargs):
        ...
    @staticmethod
    def CreateSurfaceFaceVertexIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTetVertexIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def FindInvertedElements(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSurfaceFaceVertexIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTetVertexIndicesAttr(*args, **kwargs):
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
class Tokens(Boost.Python.instance):
    BasisCurves: typing.ClassVar[str] = 'BasisCurves'
    Boundable: typing.ClassVar[str] = 'Boundable'
    Camera: typing.ClassVar[str] = 'Camera'
    Capsule: typing.ClassVar[str] = 'Capsule'
    Capsule_1: typing.ClassVar[str] = 'Capsule_1'
    Cone: typing.ClassVar[str] = 'Cone'
    Cube: typing.ClassVar[str] = 'Cube'
    Curves: typing.ClassVar[str] = 'Curves'
    Cylinder: typing.ClassVar[str] = 'Cylinder'
    Cylinder_1: typing.ClassVar[str] = 'Cylinder_1'
    GeomModelAPI: typing.ClassVar[str] = 'GeomModelAPI'
    GeomSubset: typing.ClassVar[str] = 'GeomSubset'
    Gprim: typing.ClassVar[str] = 'Gprim'
    HermiteCurves: typing.ClassVar[str] = 'HermiteCurves'
    Imageable: typing.ClassVar[str] = 'Imageable'
    Mesh: typing.ClassVar[str] = 'Mesh'
    MotionAPI: typing.ClassVar[str] = 'MotionAPI'
    NurbsCurves: typing.ClassVar[str] = 'NurbsCurves'
    NurbsPatch: typing.ClassVar[str] = 'NurbsPatch'
    Plane: typing.ClassVar[str] = 'Plane'
    PointBased: typing.ClassVar[str] = 'PointBased'
    PointInstancer: typing.ClassVar[str] = 'PointInstancer'
    Points: typing.ClassVar[str] = 'Points'
    PrimvarsAPI: typing.ClassVar[str] = 'PrimvarsAPI'
    Scope: typing.ClassVar[str] = 'Scope'
    Sphere: typing.ClassVar[str] = 'Sphere'
    TetMesh: typing.ClassVar[str] = 'TetMesh'
    VisibilityAPI: typing.ClassVar[str] = 'VisibilityAPI'
    Xform: typing.ClassVar[str] = 'Xform'
    XformCommonAPI: typing.ClassVar[str] = 'XformCommonAPI'
    Xformable: typing.ClassVar[str] = 'Xformable'
    accelerations: typing.ClassVar[str] = 'accelerations'
    all: typing.ClassVar[str] = 'all'
    angularVelocities: typing.ClassVar[str] = 'angularVelocities'
    axis: typing.ClassVar[str] = 'axis'
    basis: typing.ClassVar[str] = 'basis'
    bezier: typing.ClassVar[str] = 'bezier'
    bilinear: typing.ClassVar[str] = 'bilinear'
    boundaries: typing.ClassVar[str] = 'boundaries'
    bounds: typing.ClassVar[str] = 'bounds'
    box: typing.ClassVar[str] = 'box'
    bspline: typing.ClassVar[str] = 'bspline'
    cards: typing.ClassVar[str] = 'cards'
    catmullClark: typing.ClassVar[str] = 'catmullClark'
    catmullRom: typing.ClassVar[str] = 'catmullRom'
    clippingPlanes: typing.ClassVar[str] = 'clippingPlanes'
    clippingRange: typing.ClassVar[str] = 'clippingRange'
    closed: typing.ClassVar[str] = 'closed'
    constant: typing.ClassVar[str] = 'constant'
    cornerIndices: typing.ClassVar[str] = 'cornerIndices'
    cornerSharpnesses: typing.ClassVar[str] = 'cornerSharpnesses'
    cornersOnly: typing.ClassVar[str] = 'cornersOnly'
    cornersPlus1: typing.ClassVar[str] = 'cornersPlus1'
    cornersPlus2: typing.ClassVar[str] = 'cornersPlus2'
    creaseIndices: typing.ClassVar[str] = 'creaseIndices'
    creaseLengths: typing.ClassVar[str] = 'creaseLengths'
    creaseSharpnesses: typing.ClassVar[str] = 'creaseSharpnesses'
    cross: typing.ClassVar[str] = 'cross'
    cubic: typing.ClassVar[str] = 'cubic'
    curveVertexCounts: typing.ClassVar[str] = 'curveVertexCounts'
    default_: typing.ClassVar[str] = 'default'
    doubleSided: typing.ClassVar[str] = 'doubleSided'
    edge: typing.ClassVar[str] = 'edge'
    edgeAndCorner: typing.ClassVar[str] = 'edgeAndCorner'
    edgeOnly: typing.ClassVar[str] = 'edgeOnly'
    elementSize: typing.ClassVar[str] = 'elementSize'
    elementType: typing.ClassVar[str] = 'elementType'
    exposure: typing.ClassVar[str] = 'exposure'
    extent: typing.ClassVar[str] = 'extent'
    extentsHint: typing.ClassVar[str] = 'extentsHint'
    fStop: typing.ClassVar[str] = 'fStop'
    face: typing.ClassVar[str] = 'face'
    faceVarying: typing.ClassVar[str] = 'faceVarying'
    faceVaryingLinearInterpolation: typing.ClassVar[str] = 'faceVaryingLinearInterpolation'
    faceVertexCounts: typing.ClassVar[str] = 'faceVertexCounts'
    faceVertexIndices: typing.ClassVar[str] = 'faceVertexIndices'
    familyName: typing.ClassVar[str] = 'familyName'
    focalLength: typing.ClassVar[str] = 'focalLength'
    focusDistance: typing.ClassVar[str] = 'focusDistance'
    fromTexture: typing.ClassVar[str] = 'fromTexture'
    guide: typing.ClassVar[str] = 'guide'
    guideVisibility: typing.ClassVar[str] = 'guideVisibility'
    height: typing.ClassVar[str] = 'height'
    hermite: typing.ClassVar[str] = 'hermite'
    holeIndices: typing.ClassVar[str] = 'holeIndices'
    horizontalAperture: typing.ClassVar[str] = 'horizontalAperture'
    horizontalApertureOffset: typing.ClassVar[str] = 'horizontalApertureOffset'
    ids: typing.ClassVar[str] = 'ids'
    inactiveIds: typing.ClassVar[str] = 'inactiveIds'
    indices: typing.ClassVar[str] = 'indices'
    inherited: typing.ClassVar[str] = 'inherited'
    interpolateBoundary: typing.ClassVar[str] = 'interpolateBoundary'
    interpolation: typing.ClassVar[str] = 'interpolation'
    invisible: typing.ClassVar[str] = 'invisible'
    invisibleIds: typing.ClassVar[str] = 'invisibleIds'
    knots: typing.ClassVar[str] = 'knots'
    left: typing.ClassVar[str] = 'left'
    leftHanded: typing.ClassVar[str] = 'leftHanded'
    length: typing.ClassVar[str] = 'length'
    linear: typing.ClassVar[str] = 'linear'
    loop: typing.ClassVar[str] = 'loop'
    metersPerUnit: typing.ClassVar[str] = 'metersPerUnit'
    modelApplyDrawMode: typing.ClassVar[str] = 'model:applyDrawMode'
    modelCardGeometry: typing.ClassVar[str] = 'model:cardGeometry'
    modelCardTextureXNeg: typing.ClassVar[str] = 'model:cardTextureXNeg'
    modelCardTextureXPos: typing.ClassVar[str] = 'model:cardTextureXPos'
    modelCardTextureYNeg: typing.ClassVar[str] = 'model:cardTextureYNeg'
    modelCardTextureYPos: typing.ClassVar[str] = 'model:cardTextureYPos'
    modelCardTextureZNeg: typing.ClassVar[str] = 'model:cardTextureZNeg'
    modelCardTextureZPos: typing.ClassVar[str] = 'model:cardTextureZPos'
    modelDrawMode: typing.ClassVar[str] = 'model:drawMode'
    modelDrawModeColor: typing.ClassVar[str] = 'model:drawModeColor'
    mono: typing.ClassVar[str] = 'mono'
    motionBlurScale: typing.ClassVar[str] = 'motion:blurScale'
    motionNonlinearSampleCount: typing.ClassVar[str] = 'motion:nonlinearSampleCount'
    motionVelocityScale: typing.ClassVar[str] = 'motion:velocityScale'
    nonOverlapping: typing.ClassVar[str] = 'nonOverlapping'
    none: typing.ClassVar[str] = 'none'
    nonperiodic: typing.ClassVar[str] = 'nonperiodic'
    normals: typing.ClassVar[str] = 'normals'
    open: typing.ClassVar[str] = 'open'
    order: typing.ClassVar[str] = 'order'
    orientation: typing.ClassVar[str] = 'orientation'
    orientations: typing.ClassVar[str] = 'orientations'
    orientationsf: typing.ClassVar[str] = 'orientationsf'
    origin: typing.ClassVar[str] = 'origin'
    orthographic: typing.ClassVar[str] = 'orthographic'
    partition: typing.ClassVar[str] = 'partition'
    periodic: typing.ClassVar[str] = 'periodic'
    perspective: typing.ClassVar[str] = 'perspective'
    pinned: typing.ClassVar[str] = 'pinned'
    pivot: typing.ClassVar[str] = 'pivot'
    point: typing.ClassVar[str] = 'point'
    pointWeights: typing.ClassVar[str] = 'pointWeights'
    points: typing.ClassVar[str] = 'points'
    positions: typing.ClassVar[str] = 'positions'
    power: typing.ClassVar[str] = 'power'
    primvarsDisplayColor: typing.ClassVar[str] = 'primvars:displayColor'
    primvarsDisplayOpacity: typing.ClassVar[str] = 'primvars:displayOpacity'
    projection: typing.ClassVar[str] = 'projection'
    protoIndices: typing.ClassVar[str] = 'protoIndices'
    prototypes: typing.ClassVar[str] = 'prototypes'
    proxy: typing.ClassVar[str] = 'proxy'
    proxyPrim: typing.ClassVar[str] = 'proxyPrim'
    proxyVisibility: typing.ClassVar[str] = 'proxyVisibility'
    purpose: typing.ClassVar[str] = 'purpose'
    radius: typing.ClassVar[str] = 'radius'
    radiusBottom: typing.ClassVar[str] = 'radiusBottom'
    radiusTop: typing.ClassVar[str] = 'radiusTop'
    ranges: typing.ClassVar[str] = 'ranges'
    render: typing.ClassVar[str] = 'render'
    renderVisibility: typing.ClassVar[str] = 'renderVisibility'
    right: typing.ClassVar[str] = 'right'
    rightHanded: typing.ClassVar[str] = 'rightHanded'
    scales: typing.ClassVar[str] = 'scales'
    shutterClose: typing.ClassVar[str] = 'shutter:close'
    shutterOpen: typing.ClassVar[str] = 'shutter:open'
    size: typing.ClassVar[str] = 'size'
    smooth: typing.ClassVar[str] = 'smooth'
    stereoRole: typing.ClassVar[str] = 'stereoRole'
    subdivisionScheme: typing.ClassVar[str] = 'subdivisionScheme'
    surfaceFaceVertexIndices: typing.ClassVar[str] = 'surfaceFaceVertexIndices'
    tangents: typing.ClassVar[str] = 'tangents'
    tetVertexIndices: typing.ClassVar[str] = 'tetVertexIndices'
    tetrahedron: typing.ClassVar[str] = 'tetrahedron'
    triangleSubdivisionRule: typing.ClassVar[str] = 'triangleSubdivisionRule'
    trimCurveCounts: typing.ClassVar[str] = 'trimCurve:counts'
    trimCurveKnots: typing.ClassVar[str] = 'trimCurve:knots'
    trimCurveOrders: typing.ClassVar[str] = 'trimCurve:orders'
    trimCurvePoints: typing.ClassVar[str] = 'trimCurve:points'
    trimCurveRanges: typing.ClassVar[str] = 'trimCurve:ranges'
    trimCurveVertexCounts: typing.ClassVar[str] = 'trimCurve:vertexCounts'
    type: typing.ClassVar[str] = 'type'
    uForm: typing.ClassVar[str] = 'uForm'
    uKnots: typing.ClassVar[str] = 'uKnots'
    uOrder: typing.ClassVar[str] = 'uOrder'
    uRange: typing.ClassVar[str] = 'uRange'
    uVertexCount: typing.ClassVar[str] = 'uVertexCount'
    unauthoredValuesIndex: typing.ClassVar[str] = 'unauthoredValuesIndex'
    uniform: typing.ClassVar[str] = 'uniform'
    unrestricted: typing.ClassVar[str] = 'unrestricted'
    upAxis: typing.ClassVar[str] = 'upAxis'
    vForm: typing.ClassVar[str] = 'vForm'
    vKnots: typing.ClassVar[str] = 'vKnots'
    vOrder: typing.ClassVar[str] = 'vOrder'
    vRange: typing.ClassVar[str] = 'vRange'
    vVertexCount: typing.ClassVar[str] = 'vVertexCount'
    varying: typing.ClassVar[str] = 'varying'
    velocities: typing.ClassVar[str] = 'velocities'
    vertex: typing.ClassVar[str] = 'vertex'
    verticalAperture: typing.ClassVar[str] = 'verticalAperture'
    verticalApertureOffset: typing.ClassVar[str] = 'verticalApertureOffset'
    visibility: typing.ClassVar[str] = 'visibility'
    visible: typing.ClassVar[str] = 'visible'
    width: typing.ClassVar[str] = 'width'
    widths: typing.ClassVar[str] = 'widths'
    wrap: typing.ClassVar[str] = 'wrap'
    x: typing.ClassVar[str] = 'X'
    xformOpOrder: typing.ClassVar[str] = 'xformOpOrder'
    y: typing.ClassVar[str] = 'Y'
    z: typing.ClassVar[str] = 'Z'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class VisibilityAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateGuideVisibilityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateProxyVisibilityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRenderVisibilityAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetGuideVisibilityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetProxyVisibilityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPurposeVisibilityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRenderVisibilityAttr(*args, **kwargs):
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
class Xform(Xformable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Define(*args, **kwargs):
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
class XformCache(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ComputeRelativeTransform(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalToWorldTransform(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalTransformation(*args, **kwargs):
        ...
    @staticmethod
    def GetParentToWorldTransform(*args, **kwargs):
        ...
    @staticmethod
    def GetTime(*args, **kwargs):
        ...
    @staticmethod
    def SetTime(*args, **kwargs):
        ...
    @staticmethod
    def Swap(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class XformCommonAPI(pxr.Usd.APISchemaBase):
    class OpFlags(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'XformCommonAPI'
        allValues: typing.ClassVar[tuple]  # value = (UsdGeom.XformCommonAPI.OpTranslate, UsdGeom.XformCommonAPI.OpRotate, UsdGeom.XformCommonAPI.OpScale, UsdGeom.XformCommonAPI.OpPivot)
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
    class RotationOrder(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'XformCommonAPI'
        allValues: typing.ClassVar[tuple]  # value = (UsdGeom.XformCommonAPI.RotationOrderXYZ, UsdGeom.XformCommonAPI.RotationOrderXZY, UsdGeom.XformCommonAPI.RotationOrderYXZ, UsdGeom.XformCommonAPI.RotationOrderYZX, UsdGeom.XformCommonAPI.RotationOrderZXY, UsdGeom.XformCommonAPI.RotationOrderZYX)
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
    OpPivot: typing.ClassVar[OpFlags]  # value = UsdGeom.XformCommonAPI.OpPivot
    OpRotate: typing.ClassVar[OpFlags]  # value = UsdGeom.XformCommonAPI.OpRotate
    OpScale: typing.ClassVar[OpFlags]  # value = UsdGeom.XformCommonAPI.OpScale
    OpTranslate: typing.ClassVar[OpFlags]  # value = UsdGeom.XformCommonAPI.OpTranslate
    RotationOrderXYZ: typing.ClassVar[RotationOrder]  # value = UsdGeom.XformCommonAPI.RotationOrderXYZ
    RotationOrderXZY: typing.ClassVar[RotationOrder]  # value = UsdGeom.XformCommonAPI.RotationOrderXZY
    RotationOrderYXZ: typing.ClassVar[RotationOrder]  # value = UsdGeom.XformCommonAPI.RotationOrderYXZ
    RotationOrderYZX: typing.ClassVar[RotationOrder]  # value = UsdGeom.XformCommonAPI.RotationOrderYZX
    RotationOrderZXY: typing.ClassVar[RotationOrder]  # value = UsdGeom.XformCommonAPI.RotationOrderZXY
    RotationOrderZYX: typing.ClassVar[RotationOrder]  # value = UsdGeom.XformCommonAPI.RotationOrderZYX
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def CanConvertOpTypeToRotationOrder(*args, **kwargs):
        ...
    @staticmethod
    def ConvertOpTypeToRotationOrder(*args, **kwargs):
        ...
    @staticmethod
    def ConvertRotationOrderToOpType(*args, **kwargs):
        ...
    @staticmethod
    def CreateXformOps(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetResetXformStack(*args, **kwargs):
        ...
    @staticmethod
    def GetRotationTransform(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetXformVectors(*args, **kwargs):
        ...
    @staticmethod
    def GetXformVectorsByAccumulation(*args, **kwargs):
        ...
    @staticmethod
    def SetPivot(*args, **kwargs):
        ...
    @staticmethod
    def SetResetXformStack(*args, **kwargs):
        ...
    @staticmethod
    def SetRotate(*args, **kwargs):
        ...
    @staticmethod
    def SetScale(*args, **kwargs):
        ...
    @staticmethod
    def SetTranslate(*args, **kwargs):
        ...
    @staticmethod
    def SetXformVectors(*args, **kwargs):
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
class XformOp(Boost.Python.instance):
    class Precision(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'XformOp'
        allValues: typing.ClassVar[tuple]  # value = (UsdGeom.XformOp.PrecisionDouble, UsdGeom.XformOp.PrecisionFloat, UsdGeom.XformOp.PrecisionHalf)
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
    class Type(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'XformOp'
        allValues: typing.ClassVar[tuple]  # value = (UsdGeom.XformOp.TypeInvalid, UsdGeom.XformOp.TypeTranslate, UsdGeom.XformOp.TypeScale, UsdGeom.XformOp.TypeRotateX, UsdGeom.XformOp.TypeRotateY, UsdGeom.XformOp.TypeRotateZ, UsdGeom.XformOp.TypeRotateXYZ, UsdGeom.XformOp.TypeRotateXZY, UsdGeom.XformOp.TypeRotateYXZ, UsdGeom.XformOp.TypeRotateYZX, UsdGeom.XformOp.TypeRotateZXY, UsdGeom.XformOp.TypeRotateZYX, UsdGeom.XformOp.TypeOrient, UsdGeom.XformOp.TypeTransform)
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
    PrecisionDouble: typing.ClassVar[Precision]  # value = UsdGeom.XformOp.PrecisionDouble
    PrecisionFloat: typing.ClassVar[Precision]  # value = UsdGeom.XformOp.PrecisionFloat
    PrecisionHalf: typing.ClassVar[Precision]  # value = UsdGeom.XformOp.PrecisionHalf
    TypeInvalid: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeInvalid
    TypeOrient: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeOrient
    TypeRotateX: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeRotateX
    TypeRotateXYZ: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeRotateXYZ
    TypeRotateXZY: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeRotateXZY
    TypeRotateY: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeRotateY
    TypeRotateYXZ: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeRotateYXZ
    TypeRotateYZX: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeRotateYZX
    TypeRotateZ: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeRotateZ
    TypeRotateZXY: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeRotateZXY
    TypeRotateZYX: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeRotateZYX
    TypeScale: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeScale
    TypeTransform: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeTransform
    TypeTranslate: typing.ClassVar[Type]  # value = UsdGeom.XformOp.TypeTranslate
    __instance_size__: typing.ClassVar[int] = 160
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetBaseName(*args, **kwargs):
        ...
    @staticmethod
    def GetName(*args, **kwargs):
        ...
    @staticmethod
    def GetNamespace(*args, **kwargs):
        ...
    @staticmethod
    def GetNumTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetOpName(*args, **kwargs):
        ...
    @staticmethod
    def GetOpTransform(*args, **kwargs):
        ...
    @staticmethod
    def GetOpType(*args, **kwargs):
        ...
    @staticmethod
    def GetOpTypeEnum(*args, **kwargs):
        ...
    @staticmethod
    def GetOpTypeToken(*args, **kwargs):
        ...
    @staticmethod
    def GetPrecision(*args, **kwargs):
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
    def IsDefined(*args, **kwargs):
        ...
    @staticmethod
    def IsInverseOp(*args, **kwargs):
        ...
    @staticmethod
    def MightBeTimeVarying(*args, **kwargs):
        ...
    @staticmethod
    def Set(*args, **kwargs):
        ...
    @staticmethod
    def SplitName(*args, **kwargs):
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
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class XformOpTypes(Boost.Python.instance):
    orient: typing.ClassVar[str] = 'orient'
    resetXformStack: typing.ClassVar[str] = '!resetXformStack!'
    rotateX: typing.ClassVar[str] = 'rotateX'
    rotateXYZ: typing.ClassVar[str] = 'rotateXYZ'
    rotateXZY: typing.ClassVar[str] = 'rotateXZY'
    rotateY: typing.ClassVar[str] = 'rotateY'
    rotateYXZ: typing.ClassVar[str] = 'rotateYXZ'
    rotateYZX: typing.ClassVar[str] = 'rotateYZX'
    rotateZ: typing.ClassVar[str] = 'rotateZ'
    rotateZXY: typing.ClassVar[str] = 'rotateZXY'
    rotateZYX: typing.ClassVar[str] = 'rotateZYX'
    scale: typing.ClassVar[str] = 'scale'
    transform: typing.ClassVar[str] = 'transform'
    translate: typing.ClassVar[str] = 'translate'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Xformable(Imageable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def AddOrientOp(*args, **kwargs):
        ...
    @staticmethod
    def AddRotateXOp(*args, **kwargs):
        ...
    @staticmethod
    def AddRotateXYZOp(*args, **kwargs):
        ...
    @staticmethod
    def AddRotateXZYOp(*args, **kwargs):
        ...
    @staticmethod
    def AddRotateYOp(*args, **kwargs):
        ...
    @staticmethod
    def AddRotateYXZOp(*args, **kwargs):
        ...
    @staticmethod
    def AddRotateYZXOp(*args, **kwargs):
        ...
    @staticmethod
    def AddRotateZOp(*args, **kwargs):
        ...
    @staticmethod
    def AddRotateZXYOp(*args, **kwargs):
        ...
    @staticmethod
    def AddRotateZYXOp(*args, **kwargs):
        ...
    @staticmethod
    def AddScaleOp(*args, **kwargs):
        ...
    @staticmethod
    def AddTransformOp(*args, **kwargs):
        ...
    @staticmethod
    def AddTranslateOp(*args, **kwargs):
        ...
    @staticmethod
    def AddXformOp(*args, **kwargs):
        ...
    @staticmethod
    def ClearXformOpOrder(*args, **kwargs):
        ...
    @staticmethod
    def CreateXformOpOrderAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalTransformation(*args, **kwargs):
        """
        
        
        Compute the fully-combined, local-to-parent transformation for this prim.
        If a client does not need to manipulate the individual ops themselves, and requires only the combined transform on this prim, this method will take care of all the data marshalling and linear algebra needed to combine the ops into a 4x4 affine transformation matrix, in double-precision, regardless of the precision of the op inputs.
        The python version of this function only returns the computed  local-to-parent transformation. Clients must independently call  GetResetXformStack() to be able to construct the local-to-world transformation.
        
        Compute the fully-combined, local-to-parent transformation for this prim as efficiently as possible, using pre-fetched list of ordered xform ops supplied by the client.
        The python version of this function only returns the computed  local-to-parent transformation. Clients must independently call  GetResetXformStack() to be able to construct the local-to-world transformation.
        """
    @staticmethod
    def GetOrderedXformOps(*args, **kwargs):
        """
        
        
        Return the ordered list of transform operations to be applied to this prim, in least-to-most-local order.  This is determined by the intersection of authored op-attributes and the explicit ordering of those attributes encoded in the "xformOpOrder" attribute on this prim.
        
        Any entries in "xformOpOrder" that do not correspond to valid attributes on the xformable prim are skipped and a warning is issued.
        
        A UsdGeomTransformable that has not had any ops added via AddXformOp() will return an empty vector.
        
        
        
        The python version of this function only returns the ordered list of xformOps. Clients must independently call GetResetXformStack() if they need the info.
        """
    @staticmethod
    def GetOrientOp(*args, **kwargs):
        ...
    @staticmethod
    def GetResetXformStack(*args, **kwargs):
        ...
    @staticmethod
    def GetRotateXOp(*args, **kwargs):
        ...
    @staticmethod
    def GetRotateXYZOp(*args, **kwargs):
        ...
    @staticmethod
    def GetRotateXZYOp(*args, **kwargs):
        ...
    @staticmethod
    def GetRotateYOp(*args, **kwargs):
        ...
    @staticmethod
    def GetRotateYXZOp(*args, **kwargs):
        ...
    @staticmethod
    def GetRotateYZXOp(*args, **kwargs):
        ...
    @staticmethod
    def GetRotateZOp(*args, **kwargs):
        ...
    @staticmethod
    def GetRotateZXYOp(*args, **kwargs):
        ...
    @staticmethod
    def GetRotateZYXOp(*args, **kwargs):
        ...
    @staticmethod
    def GetScaleOp(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetTimeSamplesInInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetTransformOp(*args, **kwargs):
        ...
    @staticmethod
    def GetTranslateOp(*args, **kwargs):
        ...
    @staticmethod
    def GetXformOp(*args, **kwargs):
        ...
    @staticmethod
    def GetXformOpOrderAttr(*args, **kwargs):
        ...
    @staticmethod
    def IsTransformationAffectedByAttrNamed(*args, **kwargs):
        ...
    @staticmethod
    def MakeMatrixXform(*args, **kwargs):
        ...
    @staticmethod
    def SetResetXformStack(*args, **kwargs):
        ...
    @staticmethod
    def SetXformOpOrder(*args, **kwargs):
        ...
    @staticmethod
    def TransformMightBeTimeVarying(*args, **kwargs):
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
__MFB_FULL_PACKAGE_NAME: str = 'usdGeom'
