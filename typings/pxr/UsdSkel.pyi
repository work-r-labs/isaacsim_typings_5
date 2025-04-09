from __future__ import annotations
import pxr.Usd
import pxr.UsdGeom
import typing
__all__ = ['AnimMapper', 'AnimQuery', 'Animation', 'Binding', 'BindingAPI', 'BlendShape', 'BlendShapeQuery', 'Cache', 'InbetweenShape', 'PackedJointAnimation', 'Root', 'Skeleton', 'SkeletonQuery', 'SkinningQuery', 'Tokens', 'Topology']
class AnimMapper(Boost.Python.instance):
    """
    """
    @staticmethod
    def IsIdentity(*args, **kwargs):
        """
        
        IsIdentity() -> bool
        
        
        Returns true if this is an identity map.
        
        
        The source and target orders of an identity map are identical.
        
        
        
        """
    @staticmethod
    def IsNull(*args, **kwargs):
        """
        
        IsNull() -> bool
        
        
        Returns true if this is a null mapping.
        
        
        No source elements of a null map are mapped to the target.
        
        
        
        """
    @staticmethod
    def IsSparse(*args, **kwargs):
        """
        
        IsSparse() -> bool
        
        
        Returns true if this is a sparse mapping.
        
        
        A sparse mapping means that not all target values will be overridden
        by source values, when mapped with Remap().
        
        
        
        """
    @staticmethod
    def Remap(*args, **kwargs):
        """
        
        Remap(source, target, elementSize, defaultValue) -> bool
        
        
        Typed remapping of data in an arbitrary, stl-like container.
        
        
        The ``source`` array provides a run of ``elementSize`` for each path
        in the \\em sourceOrder. These elements are remapped and copied over
        the ``target`` array. Prior to remapping, the ``target`` array is
        resized to the size of the \\em targetOrder (as given at mapper
        construction time) multiplied by the ``elementSize`` . New element
        created in the array are initialized to ``defaultValue`` , if
        provided.
        
        
        Parameters
        ----------
        source : Container
        
        target : Container
        
        elementSize : int
        
        defaultValue : Container.value_type
        
        
        
        ----------------------------------------------------------------------
        
        Remap(source, target, elementSize, defaultValue) -> bool
        
        
        Type-erased remapping of data from ``source`` into ``target`` .
        
        
        The ``source`` array provides a run of ``elementSize`` elements for
        each path in the \\em sourceOrder. These elements are remapped and
        copied over the ``target`` array. Prior to remapping, the ``target``
        array is resized to the size of the \\em targetOrder (as given at
        mapper construction time) multiplied by the ``elementSize`` . New
        elements created in the array are initialized to ``defaultValue`` , if
        provided. Remapping is supported for registered Sdf array value types
        only.
        
        
        Parameters
        ----------
        source : VtValue
        
        target : VtValue
        
        elementSize : int
        
        defaultValue : VtValue
        
        
        """
    @staticmethod
    def RemapTransforms(*args, **kwargs):
        """
        
        RemapTransforms(source, target, elementSize) -> bool
        
        
        Convenience method for the common task of remapping transform arrays.
        
        
        This performs the same operation as Remap(), but sets the matrix
        identity as the default value.
        
        
        Parameters
        ----------
        source : VtArray[Matrix4]
        
        target : VtArray[Matrix4]
        
        elementSize : int
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct a null mapper.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(size)
        
        
        Construct an identity mapper for remapping a range of ``size`` elems.
        
        
        An identity mapper is used to indicate that no remapping is required.
        
        
        Parameters
        ----------
        size : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(sourceOrder, targetOrder)
        
        
        Construct a mapper for mapping data from ``sourceOrder`` to
        ``targetOrder`` .
        
        
        Parameters
        ----------
        sourceOrder : TokenArray
        
        targetOrder : TokenArray
        
        
        
        ----------------------------------------------------------------------
        
        __init__(sourceOrder, sourceOrderSize, targetOrder, targetOrderSize)
        
        
        Construct a mapper for mapping data from ``sourceOrder`` to
        ``targetOrder`` , each being arrays of size ``sourceOrderSize``  and
        ``targetOrderSize`` , respectively.
        
        
        Parameters
        ----------
        sourceOrder : str
        
        sourceOrderSize : int
        
        targetOrder : str
        
        targetOrderSize : int
        
        
        """
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class AnimQuery(Boost.Python.instance):
    """
    
    Class providing efficient queries of primitives that provide skel
    animation.
    
    """
    @staticmethod
    def BlendShapeWeightsMightBeTimeVarying(*args, **kwargs):
        """
        
        BlendShapeWeightsMightBeTimeVarying() -> bool
        
        
        Return true if it possible, but not certain, that the blend shape
        weights computed through this animation query change over time, false
        otherwise.
        
        
        
        UsdAttribute::ValueMightBeTimeVayring
        
        
        
        """
    @staticmethod
    def ComputeBlendShapeWeights(*args, **kwargs):
        """
        
        ComputeBlendShapeWeights(weights, time) -> bool
        
        
        Parameters
        ----------
        weights : FloatArray
        
        time : TimeCode
        
        
        """
    @staticmethod
    def ComputeJointLocalTransformComponents(*args, **kwargs):
        """
        
        ComputeJointLocalTransformComponents(translations, rotations, scales, time) -> bool
        
        
        Compute translation,rotation,scale components of the joint transforms
        in joint-local space.
        
        
        This is provided to facilitate direct streaming of animation data in a
        form that can efficiently be processed for animation blending.
        
        
        Parameters
        ----------
        translations : Vec3fArray
        
        rotations : QuatfArray
        
        scales : Vec3hArray
        
        time : TimeCode
        
        
        """
    @staticmethod
    def ComputeJointLocalTransforms(*args, **kwargs):
        """
        
        ComputeJointLocalTransforms(xforms, time) -> bool
        
        
        Compute joint transforms in joint-local space.
        
        
        Transforms are returned in the order specified by the joint ordering
        of the animation primitive itself.
        
        
        Parameters
        ----------
        xforms : VtArray[Matrix4]
        
        time : TimeCode
        
        
        """
    @staticmethod
    def GetBlendShapeOrder(*args, **kwargs):
        """
        
        GetBlendShapeOrder() -> TokenArray
        
        
        Returns an array of tokens describing the ordering of blend shape
        channels in the animation.
        
        
        
        """
    @staticmethod
    def GetBlendShapeWeightTimeSamples(*args, **kwargs):
        """
        
        GetBlendShapeWeightTimeSamples(attrs) -> bool
        
        
        Get the time samples at which values contributing to blend shape
        weights have been set.
        
        
        
        UsdAttribute::GetTimeSamples
        
        
        Parameters
        ----------
        attrs : list[float]
        
        
        """
    @staticmethod
    def GetBlendShapeWeightTimeSamplesInInterval(*args, **kwargs):
        """
        
        GetBlendShapeWeightTimeSamplesInInterval(interval, times) -> bool
        
        
        Get the time samples at which values contributing to blend shape
        weights are set, over ``interval`` .
        
        
        
        UsdAttribute::GetTimeSamplesInInterval
        
        
        Parameters
        ----------
        interval : Interval
        
        times : list[float]
        
        
        """
    @staticmethod
    def GetJointOrder(*args, **kwargs):
        """
        
        GetJointOrder() -> TokenArray
        
        
        Returns an array of tokens describing the ordering of joints in the
        animation.
        
        
        
        UsdSkelSkeleton::GetJointOrder
        
        
        
        """
    @staticmethod
    def GetJointTransformTimeSamples(*args, **kwargs):
        """
        
        GetJointTransformTimeSamples(times) -> bool
        
        
        Get the time samples at which values contributing to joint transforms
        are set.
        
        
        This only computes the time samples for sampling transforms in joint-
        local space, and does not include time samples affecting the root
        transformation.
        
        UsdAttribute::GetTimeSamples
        
        
        Parameters
        ----------
        times : list[float]
        
        
        """
    @staticmethod
    def GetJointTransformTimeSamplesInInterval(*args, **kwargs):
        """
        
        GetJointTransformTimeSamplesInInterval(interval, times) -> bool
        
        
        Get the time samples at which values contributing to joint transforms
        are set, over ``interval`` .
        
        
        This only computes the time samples for sampling transforms in joint-
        local space, and does not include time samples affecting the root
        transformation.
        
        UsdAttribute::GetTimeSamplesInInterval
        
        
        Parameters
        ----------
        interval : Interval
        
        times : list[float]
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        Return the primitive this anim query reads from.
        
        
        
        """
    @staticmethod
    def JointTransformsMightBeTimeVarying(*args, **kwargs):
        """
        
        JointTransformsMightBeTimeVarying() -> bool
        
        
        Return true if it possible, but not certain, that joint transforms
        computed through this animation query change over time, false
        otherwise.
        
        
        
        UsdAttribute::ValueMightBeTimeVayring
        
        
        
        """
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
    """
    
    Describes a skel animation, where joint animation is stored in a
    vectorized form.
    
    See the extended Skel Animation documentation for more information.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateBlendShapeWeightsAttr(*args, **kwargs):
        """
        
        CreateBlendShapeWeightsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetBlendShapeWeightsAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateBlendShapesAttr(*args, **kwargs):
        """
        
        CreateBlendShapesAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetBlendShapesAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateJointsAttr(*args, **kwargs):
        """
        
        CreateJointsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetJointsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateRotationsAttr(*args, **kwargs):
        """
        
        CreateRotationsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetRotationsAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateScalesAttr(*args, **kwargs):
        """
        
        CreateScalesAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetScalesAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateTranslationsAttr(*args, **kwargs):
        """
        
        CreateTranslationsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetTranslationsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Animation
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> Animation
        
        
        Return a UsdSkelAnimation holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdSkelAnimation(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetBlendShapeWeightsAttr(*args, **kwargs):
        """
        
        GetBlendShapeWeightsAttr() -> Attribute
        
        
        Array of weight values for each blend shape.
        
        
        Each weight value is associated with the corresponding blend shape
        identified within the *blendShapes* token array, and therefore must
        have the same length as \\*blendShapes.
        
        Declaration
        
        ``float[] blendShapeWeights``
        
        C++ Type
        
        VtArray<float>
        
        Usd Type
        
        SdfValueTypeNames->FloatArray
        
        
        
        """
    @staticmethod
    def GetBlendShapesAttr(*args, **kwargs):
        """
        
        GetBlendShapesAttr() -> Attribute
        
        
        Array of tokens identifying which blend shapes this animation's data
        applies to.
        
        
        The tokens for blendShapes correspond to the tokens set in the
        *skel:blendShapes* binding property of the UsdSkelBindingAPI.
        
        Declaration
        
        ``uniform token[] blendShapes``
        
        C++ Type
        
        VtArray<TfToken>
        
        Usd Type
        
        SdfValueTypeNames->TokenArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetJointsAttr(*args, **kwargs):
        """
        
        GetJointsAttr() -> Attribute
        
        
        Array of tokens identifying which joints this animation's data applies
        to.
        
        
        The tokens for joints correspond to the tokens of Skeleton primitives.
        The order of the joints as listed here may vary from the order of
        joints on the Skeleton itself.
        
        Declaration
        
        ``uniform token[] joints``
        
        C++ Type
        
        VtArray<TfToken>
        
        Usd Type
        
        SdfValueTypeNames->TokenArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetRotationsAttr(*args, **kwargs):
        """
        
        GetRotationsAttr() -> Attribute
        
        
        Joint-local unit quaternion rotations of all affected joints, in
        32-bit precision.
        
        
        Array length should match the size of the *joints* attribute.
        
        Declaration
        
        ``quatf[] rotations``
        
        C++ Type
        
        VtArray<GfQuatf>
        
        Usd Type
        
        SdfValueTypeNames->QuatfArray
        
        
        
        """
    @staticmethod
    def GetScalesAttr(*args, **kwargs):
        """
        
        GetScalesAttr() -> Attribute
        
        
        Joint-local scales of all affected joints, in 16 bit precision.
        
        
        Array length should match the size of the *joints* attribute.
        
        Declaration
        
        ``half3[] scales``
        
        C++ Type
        
        VtArray<GfVec3h>
        
        Usd Type
        
        SdfValueTypeNames->Half3Array
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetTransforms(*args, **kwargs):
        """
        
        GetTransforms(xforms, time) -> bool
        
        
        Convenience method for querying resolved transforms at ``time`` .
        
        
        Note that it is more efficient to query transforms through
        UsdSkelAnimQuery or UsdSkelSkeletonQuery.
        
        
        Parameters
        ----------
        xforms : Matrix4dArray
        
        time : TimeCode
        
        
        """
    @staticmethod
    def GetTranslationsAttr(*args, **kwargs):
        """
        
        GetTranslationsAttr() -> Attribute
        
        
        Joint-local translations of all affected joints.
        
        
        Array length should match the size of the *joints* attribute.
        
        Declaration
        
        ``float3[] translations``
        
        C++ Type
        
        VtArray<GfVec3f>
        
        Usd Type
        
        SdfValueTypeNames->Float3Array
        
        
        
        """
    @staticmethod
    def SetTransforms(*args, **kwargs):
        """
        
        SetTransforms(xforms, time) -> bool
        
        
        Convenience method for setting an array of transforms.
        
        
        The given transforms must be *orthogonal*.
        
        
        Parameters
        ----------
        xforms : Matrix4dArray
        
        time : TimeCode
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdSkelAnimation on UsdPrim ``prim`` .
        
        
        Equivalent to UsdSkelAnimation::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdSkelAnimation on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdSkelAnimation (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Binding(Boost.Python.instance):
    """
    
    Helper object that describes the binding of a skeleton to a set of
    skinnable objects. The set of skinnable objects is given as
    UsdSkelSkinningQuery prims, which can be used both to identify the
    skinned prim as well compute skinning properties of the prim.
    
    """
    __instance_size__: typing.ClassVar[int] = 80
    @staticmethod
    def GetSkeleton(*args, **kwargs):
        """
        
        GetSkeleton() -> Skeleton
        
        
        Returns the bound skeleton.
        
        
        
        """
    @staticmethod
    def GetSkinningTargets(*args, **kwargs):
        """
        
        GetSkinningTargets() -> VtArray[SkinningQuery]
        
        
        Returns the set skinning targets.
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(skel, skinningQueries)
        
        
        Parameters
        ----------
        skel : Skeleton
        
        skinningQueries : VtArray[SkinningQuery]
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class BindingAPI(pxr.Usd.APISchemaBase):
    """
    
    Provides API for authoring and extracting all the skinning-related
    data that lives in the"geometry hierarchy"of prims and models that
    want to be skeletally deformed.
    
    See the extended UsdSkelBindingAPI schema documentation for more about
    bindings and how they apply in a scene graph.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> BindingAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"SkelBindingAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdSkelBindingAPI object is returned upon success. An invalid
        (or empty) UsdSkelBindingAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, whyNot) -> bool
        
        
        Returns true if this **single-apply** API schema can be applied to the
        given ``prim`` .
        
        
        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        whyNot : str
        
        
        """
    @staticmethod
    def CreateAnimationSourceRel(*args, **kwargs):
        """
        
        CreateAnimationSourceRel() -> Relationship
        
        
        See GetAnimationSourceRel() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateBlendShapeTargetsRel(*args, **kwargs):
        """
        
        CreateBlendShapeTargetsRel() -> Relationship
        
        
        See GetBlendShapeTargetsRel() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateBlendShapesAttr(*args, **kwargs):
        """
        
        CreateBlendShapesAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetBlendShapesAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateGeomBindTransformAttr(*args, **kwargs):
        """
        
        CreateGeomBindTransformAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetGeomBindTransformAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateJointIndicesAttr(*args, **kwargs):
        """
        
        CreateJointIndicesAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetJointIndicesAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateJointIndicesPrimvar(*args, **kwargs):
        """
        
        CreateJointIndicesPrimvar(constant, elementSize) -> Primvar
        
        
        Convenience function to create the jointIndices primvar, optionally
        specifying elementSize.
        
        
        If ``constant`` is true, the resulting primvar is configured
        with'constant'interpolation, and describes a rigid deformation.
        Otherwise, the primvar is configured with'vertex'interpolation, and
        describes joint influences that vary per point.
        
        CreateJointIndicesAttr() , GetJointIndicesPrimvar()
        
        
        Parameters
        ----------
        constant : bool
        
        elementSize : int
        
        
        """
    @staticmethod
    def CreateJointWeightsAttr(*args, **kwargs):
        """
        
        CreateJointWeightsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetJointWeightsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateJointWeightsPrimvar(*args, **kwargs):
        """
        
        CreateJointWeightsPrimvar(constant, elementSize) -> Primvar
        
        
        Convenience function to create the jointWeights primvar, optionally
        specifying elementSize.
        
        
        If ``constant`` is true, the resulting primvar is configured
        with'constant'interpolation, and describes a rigid deformation.
        Otherwise, the primvar is configured with'vertex'interpolation, and
        describes joint influences that vary per point.
        
        CreateJointWeightsAttr() , GetJointWeightsPrimvar()
        
        
        Parameters
        ----------
        constant : bool
        
        elementSize : int
        
        
        """
    @staticmethod
    def CreateJointsAttr(*args, **kwargs):
        """
        
        CreateJointsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetJointsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateSkeletonRel(*args, **kwargs):
        """
        
        CreateSkeletonRel() -> Relationship
        
        
        See GetSkeletonRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateSkinningBlendWeightPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def CreateSkinningBlendWeightsAttr(*args, **kwargs):
        """
        
        CreateSkinningBlendWeightsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetSkinningBlendWeightsAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateSkinningMethodAttr(*args, **kwargs):
        """
        
        CreateSkinningMethodAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetSkinningMethodAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> BindingAPI
        
        
        Return a UsdSkelBindingAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdSkelBindingAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetAnimationSource(*args, **kwargs):
        """
        
        GetAnimationSource(prim) -> bool
        
        
        Convenience method to query the animation source bound on this prim.
        
        
        Returns true if an animation source binding is defined, and sets
        ``prim`` to the target prim. The resulting primitive may still be
        invalid, if the prim has been explicitly *unbound*.
        
        This does not resolved inherited animation source bindings.
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def GetAnimationSourceRel(*args, **kwargs):
        """
        
        GetAnimationSourceRel() -> Relationship
        
        
        Animation source to be bound to Skeleton primitives at or beneath the
        location at which this property is defined.
        
        
        
        """
    @staticmethod
    def GetBlendShapeTargetsRel(*args, **kwargs):
        """
        
        GetBlendShapeTargetsRel() -> Relationship
        
        
        Ordered list of all target blend shapes.
        
        
        This property is not inherited hierarchically, and is expected to be
        authored directly on the skinnable primitive to which the the blend
        shapes apply.
        
        
        
        """
    @staticmethod
    def GetBlendShapesAttr(*args, **kwargs):
        """
        
        GetBlendShapesAttr() -> Attribute
        
        
        An array of tokens defining the order onto which blend shape weights
        from an animation source map onto the *skel:blendShapeTargets* rel of
        a binding site.
        
        
        If authored, the number of elements must be equal to the number of
        targets in the *blendShapeTargets* rel. This property is not inherited
        hierarchically, and is expected to be authored directly on the
        skinnable primitive to which the blend shapes apply.
        
        Declaration
        
        ``uniform token[] skel:blendShapes``
        
        C++ Type
        
        VtArray<TfToken>
        
        Usd Type
        
        SdfValueTypeNames->TokenArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetGeomBindTransformAttr(*args, **kwargs):
        """
        
        GetGeomBindTransformAttr() -> Attribute
        
        
        Encodes the bind-time world space transforms of the prim.
        
        
        If the transform is identical for a group of gprims that share a
        common ancestor, the transform may be authored on the ancestor,
        to"inherit"down to all the leaf gprims. If this transform is unset, an
        identity transform is used instead.
        
        Declaration
        
        ``matrix4d primvars:skel:geomBindTransform``
        
        C++ Type
        
        GfMatrix4d
        
        Usd Type
        
        SdfValueTypeNames->Matrix4d
        
        
        
        """
    @staticmethod
    def GetInheritedAnimationSource(*args, **kwargs):
        """
        
        GetInheritedAnimationSource() -> Prim
        
        
        Returns the animation source bound at this prim, or one of its
        ancestors.
        
        
        
        """
    @staticmethod
    def GetInheritedSkeleton(*args, **kwargs):
        """
        
        GetInheritedSkeleton() -> Skeleton
        
        
        Returns the skeleton bound at this prim, or one of its ancestors.
        
        
        
        """
    @staticmethod
    def GetJointIndicesAttr(*args, **kwargs):
        """
        
        GetJointIndicesAttr() -> Attribute
        
        
        Indices into the *joints* attribute of the closest (in namespace)
        bound Skeleton that affect each point of a PointBased gprim.
        
        
        The primvar can have either *constant* or *vertex* interpolation. This
        primvar's *elementSize* will determine how many joint influences apply
        to each point. Indices must point be valid. Null influences should be
        defined by setting values in jointWeights to zero. See UsdGeomPrimvar
        for more information on interpolation and elementSize.
        
        Declaration
        
        ``int[] primvars:skel:jointIndices``
        
        C++ Type
        
        VtArray<int>
        
        Usd Type
        
        SdfValueTypeNames->IntArray
        
        
        
        """
    @staticmethod
    def GetJointIndicesPrimvar(*args, **kwargs):
        """
        
        GetJointIndicesPrimvar() -> Primvar
        
        
        Convenience function to get the jointIndices attribute as a primvar.
        
        
        
        GetJointIndicesAttr, GetInheritedJointWeightsPrimvar
        
        
        
        """
    @staticmethod
    def GetJointWeightsAttr(*args, **kwargs):
        """
        
        GetJointWeightsAttr() -> Attribute
        
        
        Weights for the joints that affect each point of a PointBased gprim.
        
        
        The primvar can have either *constant* or *vertex* interpolation. This
        primvar's *elementSize* will determine how many joints influences
        apply to each point. The length, interpolation, and elementSize of
        *jointWeights* must match that of *jointIndices*. See UsdGeomPrimvar
        for more information on interpolation and elementSize.
        
        Declaration
        
        ``float[] primvars:skel:jointWeights``
        
        C++ Type
        
        VtArray<float>
        
        Usd Type
        
        SdfValueTypeNames->FloatArray
        
        
        
        """
    @staticmethod
    def GetJointWeightsPrimvar(*args, **kwargs):
        """
        
        GetJointWeightsPrimvar() -> Primvar
        
        
        Convenience function to get the jointWeights attribute as a primvar.
        
        
        
        GetJointWeightsAttr, GetInheritedJointWeightsPrimvar
        
        
        
        """
    @staticmethod
    def GetJointsAttr(*args, **kwargs):
        """
        
        GetJointsAttr() -> Attribute
        
        
        An (optional) array of tokens defining the list of joints to which
        jointIndices apply.
        
        
        If not defined, jointIndices applies to the ordered list of joints
        defined in the bound Skeleton's *joints* attribute. If undefined on a
        primitive, the primitive inherits the value of the nearest ancestor
        prim, if any.
        
        Declaration
        
        ``uniform token[] skel:joints``
        
        C++ Type
        
        VtArray<TfToken>
        
        Usd Type
        
        SdfValueTypeNames->TokenArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetSkeleton(*args, **kwargs):
        """
        
        GetSkeleton(skel) -> bool
        
        
        Convenience method to query the Skeleton bound on this prim.
        
        
        Returns true if a Skeleton binding is defined, and sets ``skel`` to
        the target skel. The resulting Skeleton may still be invalid, if the
        Skeleton has been explicitly *unbound*.
        
        This does not resolved inherited skeleton bindings.
        
        
        Parameters
        ----------
        skel : Skeleton
        
        
        """
    @staticmethod
    def GetSkeletonRel(*args, **kwargs):
        """
        
        GetSkeletonRel() -> Relationship
        
        
        Skeleton to be bound to this prim and its descendents that possess a
        mapping and weighting to the joints of the identified Skeleton.
        
        
        
        """
    @staticmethod
    def GetSkinningBlendWeightPrimvar(*args, **kwargs):
        ...
    @staticmethod
    def GetSkinningBlendWeightsAttr(*args, **kwargs):
        """
        
        GetSkinningBlendWeightsAttr() -> Attribute
        
        
        Weights for weighted blend skinning method.
        
        
        The primvar can have either *constant* or *vertex* interpolation.
        Constant interpolation means every vertex share the same single blend
        weight. Vertex interpolation means every vertex has their own blend
        weight. The element size should match the vertices count in this case.
        
        C++ Type: VtArray<float>  Usd Type: SdfValueTypeNames->FloatArray
        Variability: SdfVariabilityUniform  Fallback Value: No Fallback
        
        
        
        """
    @staticmethod
    def GetSkinningMethodAttr(*args, **kwargs):
        """
        
        GetSkinningMethodAttr() -> Attribute
        
        
        Different calculation method for skinning.
        
        
        LBS, DQ, and blendWeight
        
        C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
        SdfVariabilityUniform  Fallback Value: ClassicLinear  Allowed Values :
        [ClassicLinear, DualQuaternion, WeightedBlend]
        
        
        
        """
    @staticmethod
    def SetRigidJointInfluence(*args, **kwargs):
        """
        
        SetRigidJointInfluence(jointIndex, weight) -> bool
        
        
        Convenience method for defining joints influences that make a
        primitive rigidly deformed by a single joint.
        
        
        Parameters
        ----------
        jointIndex : int
        
        weight : float
        
        
        """
    @staticmethod
    def ValidateJointIndices(*args, **kwargs):
        """
        
        **classmethod** ValidateJointIndices(indices, numJoints, reason) -> bool
        
        
        Validate an array of joint indices.
        
        
        This ensures that all indices are the in the range [0, numJoints).
        Returns true if the indices are valid, or false otherwise. If invalid
        and ``reason`` is non-null, an error message describing the first
        validation error will be set.
        
        
        Parameters
        ----------
        indices : TfSpan[int]
        
        numJoints : int
        
        reason : str
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdSkelBindingAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdSkelBindingAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdSkelBindingAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdSkelBindingAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class BlendShape(pxr.Usd.Typed):
    """
    
    Describes a target blend shape, possibly containing inbetween shapes.
    
    See the extended Blend Shape Schema documentation for information.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateInbetween(*args, **kwargs):
        """
        
        CreateInbetween(name) -> InbetweenShape
        
        
        Author scene description to create an attribute on this prim that will
        be recognized as an Inbetween (i.e.
        
        
        will present as a valid UsdSkelInbetweenShape).
        
        The name of the created attribute or may or may not be the specified
        ``attrName`` , due to the possible need to apply property namespacing.
        Creation may fail and return an invalid Inbetwen if ``attrName``
        contains a reserved keyword.
        
        an invalid UsdSkelInbetweenShape if we failed to create a valid
        attribute, a valid UsdSkelInbetweenShape otherwise. It is not an error
        to create over an existing, compatible attribute.
        
        UsdSkelInbetweenShape::IsInbetween()
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def CreateNormalOffsetsAttr(*args, **kwargs):
        """
        
        CreateNormalOffsetsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetNormalOffsetsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateOffsetsAttr(*args, **kwargs):
        """
        
        CreateOffsetsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetOffsetsAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreatePointIndicesAttr(*args, **kwargs):
        """
        
        CreatePointIndicesAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetPointIndicesAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> BlendShape
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> BlendShape
        
        
        Return a UsdSkelBlendShape holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdSkelBlendShape(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetAuthoredInbetweens(*args, **kwargs):
        """
        
        GetAuthoredInbetweens() -> list[InbetweenShape]
        
        
        Like GetInbetweens() , but exclude inbetwens that have no authored
        scene / description.
        
        
        
        """
    @staticmethod
    def GetInbetween(*args, **kwargs):
        """
        
        GetInbetween(name) -> InbetweenShape
        
        
        Return the Inbetween corresponding to the attribute named ``name`` ,
        which will be valid if an Inbetween attribute definition already
        exists.
        
        
        Name lookup will account for Inbetween namespacing, which means that
        this method will succeed in some cases where ``UsdSkelInbetweenShape
        (prim->GetAttribute(name))`` will not, unless ``name`` has the proper
        namespace prefix.
        
        HasInbetween()
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetInbetweens(*args, **kwargs):
        """
        
        GetInbetweens() -> list[InbetweenShape]
        
        
        Return valid UsdSkelInbetweenShape objects for all defined Inbetweens
        on this prim.
        
        
        
        """
    @staticmethod
    def GetNormalOffsetsAttr(*args, **kwargs):
        """
        
        GetNormalOffsetsAttr() -> Attribute
        
        
        **Required property**.
        
        
        Normal offsets which, when added to the base pose, provides the
        normals of the target shape.
        
        Declaration
        
        ``uniform vector3f[] normalOffsets``
        
        C++ Type
        
        VtArray<GfVec3f>
        
        Usd Type
        
        SdfValueTypeNames->Vector3fArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetOffsetsAttr(*args, **kwargs):
        """
        
        GetOffsetsAttr() -> Attribute
        
        
        **Required property**.
        
        
        Position offsets which, when added to the base pose, provides the
        target shape.
        
        Declaration
        
        ``uniform vector3f[] offsets``
        
        C++ Type
        
        VtArray<GfVec3f>
        
        Usd Type
        
        SdfValueTypeNames->Vector3fArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetPointIndicesAttr(*args, **kwargs):
        """
        
        GetPointIndicesAttr() -> Attribute
        
        
        **Optional property**.
        
        
        Indices into the original mesh that correspond to the values in
        *offsets* and of any inbetween shapes. If authored, the number of
        elements must be equal to the number of elements in the *offsets*
        array.
        
        Declaration
        
        ``uniform int[] pointIndices``
        
        C++ Type
        
        VtArray<int>
        
        Usd Type
        
        SdfValueTypeNames->IntArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def HasInbetween(*args, **kwargs):
        """
        
        HasInbetween(name) -> bool
        
        
        Return true if there is a defined Inbetween named ``name`` on this
        prim.
        
        
        Name lookup will account for Inbetween namespacing.
        
        GetInbetween()
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def ValidatePointIndices(*args, **kwargs):
        """
        
        **classmethod** ValidatePointIndices(indices, numPoints, reason) -> bool
        
        
        Validates a set of point indices for a given point count.
        
        
        This ensures that all point indices are in the range [0, numPoints).
        Returns true if the indices are valid, or false otherwise. If invalid
        and ``reason`` is non-null, an error message describing the first
        validation error will be set.
        
        
        Parameters
        ----------
        indices : TfSpan[int]
        
        numPoints : int
        
        reason : str
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdSkelBlendShape on UsdPrim ``prim`` .
        
        
        Equivalent to UsdSkelBlendShape::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdSkelBlendShape on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdSkelBlendShape (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class BlendShapeQuery(Boost.Python.instance):
    """
    
    Helper class used to resolve blend shape weights, including
    inbetweens.
    
    """
    __instance_size__: typing.ClassVar[int] = 120
    @staticmethod
    def ComputeBlendShapePointIndices(*args, **kwargs):
        """
        
        ComputeBlendShapePointIndices() -> list[IntArray]
        
        
        Compute an array holding the point indices of all shapes.
        
        
        This is indexed by the *blendShapeIndices* returned by
        ComputeSubShapes(). Since the *pointIndices* property of blend shapes
        is optional, some of the arrays may be empty.
        
        
        
        """
    @staticmethod
    def ComputeDeformedPoints(*args, **kwargs):
        """
        
        ComputeDeformedPoints(subShapeWeights, blendShapeIndices, subShapeIndices, blendShapePointIndices, subShapePointOffsets, points) -> bool
        
        
        Deform ``points`` using the resolved sub-shapes given by
        ``subShapeWeights`` , ``blendShapeIndices`` and ``subShapeIndices`` .
        
        
        The ``blendShapePointIndices`` and ``blendShapePointOffsets`` arrays
        both provide the pre-computed point offsets and indices of each sub-
        shape, as computed by ComputeBlendShapePointIndices() and
        ComputeSubShapePointOffsets() .
        
        
        Parameters
        ----------
        subShapeWeights : TfSpan[float]
        
        blendShapeIndices : TfSpan[unsigned]
        
        subShapeIndices : TfSpan[unsigned]
        
        blendShapePointIndices : list[IntArray]
        
        subShapePointOffsets : list[Vec3fArray]
        
        points : TfSpan[Vec3f]
        
        
        """
    @staticmethod
    def ComputeSubShapePointOffsets(*args, **kwargs):
        """
        
        ComputeSubShapePointOffsets() -> list[Vec3fArray]
        
        
        Compute an array holding the point offsets of all sub-shapes.
        
        
        This includes offsets of both primary shapes  those stored directly on
        a BlendShape primitive  as well as those of inbetween shapes. This is
        indexed by the *subShapeIndices* returned by ComputeSubShapeWeights()
        .
        
        
        
        """
    @staticmethod
    def ComputeSubShapeWeights(*args, **kwargs):
        """
        
        ComputeSubShapeWeights(weights, subShapeWeights, blendShapeIndices, subShapeIndices) -> bool
        
        
        Compute the resolved weights for all sub-shapes bound to this prim.
        
        
        The ``weights`` values are initial weight values, ordered according to
        the *skel:blendShapeTargets* relationship of the prim this query is
        associated with. If there are any inbetween shapes, a new set of
        weights is computed, providing weighting of the relevant inbetweens.
        
        All computed arrays shared the same size. Elements of the same index
        identify which sub-shape of which blend shape a given weight value is
        mapped to.
        
        
        Parameters
        ----------
        weights : TfSpan[float]
        
        subShapeWeights : FloatArray
        
        blendShapeIndices : UIntArray
        
        subShapeIndices : UIntArray
        
        
        """
    @staticmethod
    def GetBlendShape(*args, **kwargs):
        """
        
        GetBlendShape(blendShapeIndex) -> BlendShape
        
        
        Returns the blend shape corresponding to ``blendShapeIndex`` .
        
        
        Parameters
        ----------
        blendShapeIndex : int
        
        
        """
    @staticmethod
    def GetBlendShapeIndex(*args, **kwargs):
        """
        
        GetBlendShapeIndex(subShapeIndex) -> int
        
        
        Returns the blend shape index corresponding to the ``i'th`` sub-shape.
        
        
        Parameters
        ----------
        subShapeIndex : int
        
        
        """
    @staticmethod
    def GetInbetween(*args, **kwargs):
        """
        
        GetInbetween(subShapeIndex) -> InbetweenShape
        
        
        Returns the inbetween shape corresponding to sub-shape ``i`` , if any.
        
        
        Parameters
        ----------
        subShapeIndex : int
        
        
        """
    @staticmethod
    def GetNumBlendShapes(*args, **kwargs):
        """
        
        GetNumBlendShapes() -> int
        
        
        
        """
    @staticmethod
    def GetNumSubShapes(*args, **kwargs):
        """
        
        GetNumSubShapes() -> int
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(binding)
        
        
        Parameters
        ----------
        binding : BindingAPI
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
class Cache(Boost.Python.instance):
    """
    
    Thread-safe cache for accessing query objects for evaluating skeletal
    data.
    
    
    This provides caching of major structural components, such as skeletal
    topology. In a streaming context, this cache is intended to persist.
    
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def Clear(*args, **kwargs):
        """
        
        Clear() -> None
        
        
        
        """
    @staticmethod
    def ComputeSkelBinding(*args, **kwargs):
        """
        
        ComputeSkelBinding(skelRoot, skel, binding, predicate) -> bool
        
        
        Compute the bindings corresponding to a single skeleton, bound beneath
        ``skelRoot`` , as discovered through a traversal using ``predicate`` .
        
        
        Skinnable prims are only discoverable by this method if Populate() has
        already been called for ``skelRoot`` , with an equivalent predicate.
        
        
        Parameters
        ----------
        skelRoot : Root
        
        skel : Skeleton
        
        binding : Binding
        
        predicate : _PrimFlagsPredicate
        
        
        """
    @staticmethod
    def ComputeSkelBindings(*args, **kwargs):
        """
        
        ComputeSkelBindings(skelRoot, bindings, predicate) -> bool
        
        
        Compute the set of skeleton bindings beneath ``skelRoot`` , as
        discovered through a traversal using ``predicate`` .
        
        
        Skinnable prims are only discoverable by this method if Populate() has
        already been called for ``skelRoot`` , with an equivalent predicate.
        
        
        Parameters
        ----------
        skelRoot : Root
        
        bindings : list[Binding]
        
        predicate : _PrimFlagsPredicate
        
        
        """
    @staticmethod
    def GetAnimQuery(*args, **kwargs):
        """
        
        GetAnimQuery(anim) -> AnimQuery
        
        
        Get an anim query corresponding to ``anim`` .
        
        
        This does not require Populate() to be called on the cache.
        
        
        Parameters
        ----------
        anim : Animation
        
        
        
        ----------------------------------------------------------------------
        
        GetAnimQuery(prim) -> AnimQuery
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Deprecated
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def GetSkelQuery(*args, **kwargs):
        """
        
        GetSkelQuery(skel) -> SkeletonQuery
        
        
        Get a skel query for computing properties of ``skel`` .
        
        
        This does not require Populate() to be called on the cache.
        
        
        Parameters
        ----------
        skel : Skeleton
        
        
        """
    @staticmethod
    def GetSkinningQuery(*args, **kwargs):
        """
        
        GetSkinningQuery(prim) -> SkinningQuery
        
        
        Get a skinning query at ``prim`` .
        
        
        Skinning queries are defined at any skinnable prims (I.e., boundable
        prims with fully defined joint influences).
        
        The caller must first Populate() the cache with the skel root
        containing ``prim`` , with a predicate that will visit ``prim`` , in
        order for a skinning query to be discoverable.
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def Populate(*args, **kwargs):
        """
        
        Populate(root, predicate) -> bool
        
        
        Populate the cache for the skeletal data beneath prim ``root`` , as
        traversed using ``predicate`` .
        
        
        Population resolves inherited skel bindings set using the
        UsdSkelBindingAPI, making resolved bindings available through
        GetSkinningQuery() , ComputeSkelBdining() and ComputeSkelBindings() .
        
        
        Parameters
        ----------
        root : Root
        
        predicate : _PrimFlagsPredicate
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class InbetweenShape(Boost.Python.instance):
    """
    
    Schema wrapper for UsdAttribute for authoring and introspecting
    attributes that serve as inbetween shapes of a UsdSkelBlendShape.
    
    Inbetween shapes allow an explicit shape to be specified when the
    blendshape to which it's bound is evaluated at a certain weight. For
    example, rather than performing piecewise linear interpolation between
    a primary shape and the rest shape at weight 0.5, an inbetween shape
    could be defined at the weight. For weight values greater than 0.5, a
    shape would then be resolved by linearly interpolating between the
    inbetween shape and the primary shape, while for weight values less
    than or equal to 0.5, the shape is resolved by linearly interpolating
    between the inbetween shape and the primary shape.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateNormalOffsetsAttr(*args, **kwargs):
        """
        
        CreateNormalOffsetsAttr(defaultValue) -> Attribute
        
        
        Returns the existing normal offsets attribute if the shape has normal
        offsets, or creates a new one.
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        
        """
    @staticmethod
    def GetAttr(*args, **kwargs):
        """
        
        GetAttr() -> Attribute
        
        
        Explicit UsdAttribute extractor.
        
        
        
        """
    @staticmethod
    def GetNormalOffsets(*args, **kwargs):
        """
        
        GetNormalOffsets(offsets) -> bool
        
        
        Get the normal offsets authored for this shape.
        
        
        Normal offsets are optional, and may be left unspecified.
        
        
        Parameters
        ----------
        offsets : Vec3fArray
        
        
        """
    @staticmethod
    def GetNormalOffsetsAttr(*args, **kwargs):
        """
        
        GetNormalOffsetsAttr() -> Attribute
        
        
        Returns a valid normal offsets attribute if the shape has normal
        offsets.
        
        
        Returns an invalid attribute otherwise.
        
        
        
        """
    @staticmethod
    def GetOffsets(*args, **kwargs):
        """
        
        GetOffsets(offsets) -> bool
        
        
        Get the point offsets corresponding to this shape.
        
        
        Parameters
        ----------
        offsets : Vec3fArray
        
        
        """
    @staticmethod
    def GetWeight(*args, **kwargs):
        """
        
        GetWeight(weight) -> bool
        
        
        Return the location at which the shape is applied.
        
        
        Parameters
        ----------
        weight : float
        
        
        """
    @staticmethod
    def HasAuthoredWeight(*args, **kwargs):
        """
        
        HasAuthoredWeight() -> bool
        
        
        Has a weight value been explicitly authored on this shape?
        
        
        
        GetWeight()
        
        
        
        """
    @staticmethod
    def IsDefined(*args, **kwargs):
        """
        
        IsDefined() -> bool
        
        
        Return true if the wrapped UsdAttribute::IsDefined() , and in addition
        the attribute is identified as an Inbetween.
        
        
        
        """
    @staticmethod
    def IsInbetween(*args, **kwargs):
        """
        
        **classmethod** IsInbetween(attr) -> bool
        
        
        Test whether a given UsdAttribute represents a valid Inbetween, which
        implies that creating a UsdSkelInbetweenShape from the attribute will
        succeed.
        
        
        Succes implies that ``attr.IsDefined()`` is true.
        
        
        Parameters
        ----------
        attr : Attribute
        
        
        """
    @staticmethod
    def SetNormalOffsets(*args, **kwargs):
        """
        
        SetNormalOffsets(offsets) -> bool
        
        
        Set the normal offsets authored for this shape.
        
        
        Parameters
        ----------
        offsets : Vec3fArray
        
        
        """
    @staticmethod
    def SetOffsets(*args, **kwargs):
        """
        
        SetOffsets(offsets) -> bool
        
        
        Set the point offsets corresponding to this shape.
        
        
        Parameters
        ----------
        offsets : Vec3fArray
        
        
        """
    @staticmethod
    def SetWeight(*args, **kwargs):
        """
        
        SetWeight(weight) -> bool
        
        
        Set the location at which the shape is applied.
        
        
        Parameters
        ----------
        weight : float
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Default constructor returns an invalid inbetween shape.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(attr)
        
        
        Speculative constructor that will produce a valid
        UsdSkelInbetweenShape when ``attr`` already represents an attribute
        that is an Inbetween, and produces an *invalid* Inbetween otherwise
        (i.e.
        
        
        operator bool() will return false).
        
        Calling ``UsdSkelInbetweenShape::IsInbetween(attr)`` will return the
        same truth value as this constructor, but if you plan to subsequently
        use the Inbetween anyways, just use this constructor.
        
        
        Parameters
        ----------
        attr : Attribute
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class PackedJointAnimation(Animation):
    """
    
    Deprecated. Please use SkelAnimation instead.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> PackedJointAnimation
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> PackedJointAnimation
        
        
        Return a UsdSkelPackedJointAnimation holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdSkelPackedJointAnimation(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdSkelPackedJointAnimation on UsdPrim ``prim`` .
        
        
        Equivalent to UsdSkelPackedJointAnimation::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdSkelPackedJointAnimation on the prim held by
        ``schemaObj`` .
        
        
        Should be preferred over UsdSkelPackedJointAnimation
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Root(pxr.UsdGeom.Boundable):
    """
    
    Boundable prim type used to identify a scope beneath which skeletally-
    posed primitives are defined.
    
    A SkelRoot must be defined at or above a skinned primitive for any
    skinning behaviors in UsdSkel.
    
    See the extended Skel Root Schema documentation for more information.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Root
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Find(*args, **kwargs):
        """
        
        **classmethod** Find(prim) -> Root
        
        
        Returns the skel root at or above ``prim`` , or an invalid schema
        object  if no ancestor prim is defined as a skel root.
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> Root
        
        
        Return a UsdSkelRoot holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdSkelRoot(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdSkelRoot on UsdPrim ``prim`` .
        
        
        Equivalent to UsdSkelRoot::Get (prim.GetStage(), prim.GetPath()) for a
        *valid* ``prim`` , but will not immediately throw an error for an
        invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdSkelRoot on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdSkelRoot (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Skeleton(pxr.UsdGeom.Boundable):
    """
    
    Describes a skeleton.
    
    See the extended Skeleton Schema documentation for more information.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateBindTransformsAttr(*args, **kwargs):
        """
        
        CreateBindTransformsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetBindTransformsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateJointNamesAttr(*args, **kwargs):
        """
        
        CreateJointNamesAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetJointNamesAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateJointsAttr(*args, **kwargs):
        """
        
        CreateJointsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetJointsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateRestTransformsAttr(*args, **kwargs):
        """
        
        CreateRestTransformsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetRestTransformsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Skeleton
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> Skeleton
        
        
        Return a UsdSkelSkeleton holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdSkelSkeleton(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetBindTransformsAttr(*args, **kwargs):
        """
        
        GetBindTransformsAttr() -> Attribute
        
        
        Specifies the bind-pose transforms of each joint in **world space**,
        in the ordering imposed by *joints*.
        
        
        
        Declaration
        
        ``uniform matrix4d[] bindTransforms``
        
        C++ Type
        
        VtArray<GfMatrix4d>
        
        Usd Type
        
        SdfValueTypeNames->Matrix4dArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetJointNamesAttr(*args, **kwargs):
        """
        
        GetJointNamesAttr() -> Attribute
        
        
        If authored, provides a unique name per joint.
        
        
        This may be optionally set to provide better names when translating to
        DCC apps that require unique joint names.
        
        Declaration
        
        ``uniform token[] jointNames``
        
        C++ Type
        
        VtArray<TfToken>
        
        Usd Type
        
        SdfValueTypeNames->TokenArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetJointsAttr(*args, **kwargs):
        """
        
        GetJointsAttr() -> Attribute
        
        
        An array of path tokens identifying the set of joints that make up the
        skeleton, and their order.
        
        
        Each token in the array must be valid when parsed as an SdfPath. The
        parent-child relationships of the corresponding paths determine the
        parent-child relationships of each joint. It is not required that the
        name at the end of each path be unique, but rather only that the paths
        themselves be unique.
        
        Declaration
        
        ``uniform token[] joints``
        
        C++ Type
        
        VtArray<TfToken>
        
        Usd Type
        
        SdfValueTypeNames->TokenArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetRestTransformsAttr(*args, **kwargs):
        """
        
        GetRestTransformsAttr() -> Attribute
        
        
        Specifies the rest-pose transforms of each joint in **local space**,
        in the ordering imposed by *joints*.
        
        
        This provides fallback values for joint transforms when a Skeleton
        either has no bound animation source, or when that animation source
        only contains animation for a subset of a Skeleton's joints.
        
        Declaration
        
        ``uniform matrix4d[] restTransforms``
        
        C++ Type
        
        VtArray<GfMatrix4d>
        
        Usd Type
        
        SdfValueTypeNames->Matrix4dArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdSkelSkeleton on UsdPrim ``prim`` .
        
        
        Equivalent to UsdSkelSkeleton::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdSkelSkeleton on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdSkelSkeleton (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class SkeletonQuery(Boost.Python.instance):
    """
    
    Primary interface to reading *bound* skeleton data. This is used to
    query properties such as resolved transforms and animation bindings,
    as bound through the UsdSkelBindingAPI.
    
    A UsdSkelSkeletonQuery can not be constructed directly, and instead
    must be constructed through a UsdSkelCache instance. This is done as
    follows:
    
    .. code-block:: text
    
      // Global cache, intended to persist.
      UsdSkelCache skelCache;
      // Populate the cache for a skel root.
      skelCache.Populate(UsdSkelRoot(skelRootPrim));
      
      if (UsdSkelSkeletonQuery skelQuery = skelCache.GetSkelQuery(skelPrim)) {
          \\.\\.\\.
      }
    
    
    """
    @staticmethod
    def ComputeJointLocalTransforms(*args, **kwargs):
        """
        
        ComputeJointLocalTransforms(xforms, time, atRest) -> bool
        
        
        Compute joint transforms in joint-local space, at ``time`` .
        
        
        This returns transforms in joint order of the skeleton. If ``atRest``
        is false and an animation source is bound, local transforms defined by
        the animation are mapped into the skeleton's joint order. Any
        transforms not defined by the animation source use the transforms from
        the rest pose as a fallback value. If valid transforms cannot be
        computed for the animation source, the ``xforms`` are instead set to
        the rest transforms.
        
        
        Parameters
        ----------
        xforms : VtArray[Matrix4]
        
        time : TimeCode
        
        atRest : bool
        
        
        """
    @staticmethod
    def ComputeJointRestRelativeTransforms(*args, **kwargs):
        """
        
        ComputeJointRestRelativeTransforms(xforms, time) -> bool
        
        
        Compute joint transforms which, when concatenated against the rest
        pose, produce joint transforms in joint-local space.
        
        
        More specifically, this computes *restRelativeTransform* in:
        
        .. code-block:: text
        
          restRelativeTransform \\* restTransform = jointLocalTransform
        
        
        
        Parameters
        ----------
        xforms : VtArray[Matrix4]
        
        time : TimeCode
        
        
        """
    @staticmethod
    def ComputeJointSkelTransforms(*args, **kwargs):
        """
        
        ComputeJointSkelTransforms(xforms, time, atRest) -> bool
        
        
        Compute joint transforms in skeleton space, at ``time`` .
        
        
        This concatenates joint transforms as computed from
        ComputeJointLocalTransforms() . If ``atRest`` is true, any bound
        animation source is ignored, and transforms are computed from the rest
        pose. The skeleton-space transforms of the rest pose are cached
        internally.
        
        
        Parameters
        ----------
        xforms : VtArray[Matrix4]
        
        time : TimeCode
        
        atRest : bool
        
        
        """
    @staticmethod
    def ComputeJointWorldTransforms(*args, **kwargs):
        """
        
        ComputeJointWorldTransforms(xforms, xfCache, atRest) -> bool
        
        
        Compute joint transforms in world space, at whatever time is
        configured on ``xfCache`` .
        
        
        This is equivalent to computing skel-space joint transforms with
        CmoputeJointSkelTransforms(), and then concatenating all transforms by
        the local-to-world transform of the Skeleton prim. If ``atRest`` is
        true, any bound animation source is ignored, and transforms are
        computed from the rest pose.
        
        
        Parameters
        ----------
        xforms : VtArray[Matrix4]
        
        xfCache : XformCache
        
        atRest : bool
        
        
        """
    @staticmethod
    def ComputeSkinningTransforms(*args, **kwargs):
        """
        
        ComputeSkinningTransforms(xforms, time) -> bool
        
        
        Compute transforms representing the change in transformation of a
        joint from its rest pose, in skeleton space.
        
        
        I.e.,
        
        .. code-block:: text
        
          inverse(bindTransform)\\*jointTransform
        
        These are the transforms usually required for skinning.
        
        
        Parameters
        ----------
        xforms : VtArray[Matrix4]
        
        time : TimeCode
        
        
        """
    @staticmethod
    def GetAnimQuery(*args, **kwargs):
        """
        
        GetAnimQuery() -> AnimQuery
        
        
        Returns the animation query that provides animation for the bound
        skeleton instance, if any.
        
        
        
        """
    @staticmethod
    def GetJointOrder(*args, **kwargs):
        """
        
        GetJointOrder() -> TokenArray
        
        
        Returns an array of joint paths, given as tokens, describing the order
        and parent-child relationships of joints in the skeleton.
        
        
        
        UsdSkelSkeleton::GetJointOrder
        
        
        
        """
    @staticmethod
    def GetJointWorldBindTransforms(*args, **kwargs):
        """
        
        GetJointWorldBindTransforms(xforms) -> bool
        
        
        Returns the world space joint transforms at bind time.
        
        
        Parameters
        ----------
        xforms : VtArray[Matrix4]
        
        
        """
    @staticmethod
    def GetMapper(*args, **kwargs):
        """
        
        GetMapper() -> AnimMapper
        
        
        Returns a mapper for remapping from the bound animation, if any, to
        the Skeleton.
        
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        Returns the underlying Skeleton primitive corresponding to the bound
        skeleton instance, if any.
        
        
        
        """
    @staticmethod
    def GetSkeleton(*args, **kwargs):
        """
        
        GetSkeleton() -> Skeleton
        
        
        Returns the bound skeleton instance, if any.
        
        
        
        """
    @staticmethod
    def GetTopology(*args, **kwargs):
        """
        
        GetTopology() -> Topology
        
        
        Returns the topology of the bound skeleton instance, if any.
        
        
        
        """
    @staticmethod
    def HasBindPose(*args, **kwargs):
        """
        
        HasBindPose() -> bool
        
        
        Returns ``true`` if the size of the array returned by
        skeleton::GetBindTransformsAttr() matches the number of joints in the
        skeleton.
        
        
        
        """
    @staticmethod
    def HasRestPose(*args, **kwargs):
        """
        
        HasRestPose() -> bool
        
        
        Returns ``true`` if the size of the array returned by
        skeleton::GetRestTransformsAttr() matches the number of joints in the
        skeleton.
        
        
        
        """
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
class SkinningQuery(Boost.Python.instance):
    """
    
    Object used for querying resolved bindings for skinning.
    
    """
    __instance_size__: typing.ClassVar[int] = 464
    @staticmethod
    def ComputeExtentsPadding(*args, **kwargs):
        """
        
        ComputeExtentsPadding(skelRestXforms, boundable) -> float
        
        
        Helper for computing an *approximate* padding for use in extents
        computations.
        
        
        The padding is computed as the difference between the pivots of the
        ``skelRestXforms``  *skeleton space* joint transforms at rest  and the
        extents of the skinned primitive. This is intended to provide a
        suitable, constant metric for padding joint extents as computed by
        UsdSkelComputeJointsExtent.
        
        
        Parameters
        ----------
        skelRestXforms : VtArray[Matrix4]
        
        boundable : Boundable
        
        
        """
    @staticmethod
    def ComputeJointInfluences(*args, **kwargs):
        """
        
        ComputeJointInfluences(indices, weights, time) -> bool
        
        
        Convenience method for computing joint influences.
        
        
        In addition to querying influences, this will also perform validation
        of the basic form of the weight data  although the array contents is
        not validated.
        
        
        Parameters
        ----------
        indices : IntArray
        
        weights : FloatArray
        
        time : TimeCode
        
        
        """
    @staticmethod
    def ComputeSkinnedPoints(*args, **kwargs):
        """
        
        ComputeSkinnedPoints(xforms, points, time) -> bool
        
        
        Compute skinned points using linear blend skinning.
        
        
        Both ``xforms`` and ``points`` are given in *skeleton space*, using
        the joint order of the bound skeleton. Joint influences and the
        (optional) binding transform are computed at time ``time`` (which will
        typically be unvarying).
        
        UsdSkelSkeletonQuery::ComputeSkinningTransforms
        
        
        Parameters
        ----------
        xforms : VtArray[Matrix4]
        
        points : Vec3fArray
        
        time : TimeCode
        
        
        """
    @staticmethod
    def ComputeSkinnedTransform(*args, **kwargs):
        """
        
        ComputeSkinnedTransform(xforms, xform, time) -> bool
        
        
        Compute a skinning transform using linear blend skinning.
        
        
        The ``xforms`` are given in *skeleton space*, using the joint order of
        the bound skeleton. Joint influences and the (optional) binding
        transform are computed at time ``time`` (which will typically be
        unvarying). If this skinning query holds non-constant joint
        influences, no transform will be computed, and the function will
        return false.
        
        UsdSkelSkeletonQuery::ComputeSkinningTransforms
        
        
        Parameters
        ----------
        xforms : VtArray[Matrix4]
        
        xform : Matrix4
        
        time : TimeCode
        
        
        """
    @staticmethod
    def ComputeVaryingJointInfluences(*args, **kwargs):
        """
        
        ComputeVaryingJointInfluences(numPoints, indices, weights, time) -> bool
        
        
        Convenience method for computing joint influence, where constant
        influences are expanded to hold values per point.
        
        
        In addition to querying influences, this will also perform validation
        of the basic form of the weight data  although the array contents is
        not validated.
        
        
        Parameters
        ----------
        numPoints : int
        
        indices : IntArray
        
        weights : FloatArray
        
        time : TimeCode
        
        
        """
    @staticmethod
    def GetBlendShapeMapper(*args, **kwargs):
        """
        
        GetBlendShapeMapper() -> AnimMapper
        
        
        Return the mapper for remapping blend shapes from the order of the
        bound SkelAnimation to the local blend shape order of this prim.
        
        
        Returns a null reference if the underlying prim has no blend shapes.
        The mapper maps data from the order given by the *blendShapes* order
        on the SkelAnimation to the order given by the *skel:blendShapes*
        property, as set through the UsdSkelBindingAPI.
        
        
        
        """
    @staticmethod
    def GetBlendShapeOrder(*args, **kwargs):
        """
        
        GetBlendShapeOrder(blendShapes) -> bool
        
        
        Get the blend shapes for this skinning site, if any.
        
        
        Parameters
        ----------
        blendShapes : TokenArray
        
        
        """
    @staticmethod
    def GetBlendShapeTargetsRel(*args, **kwargs):
        """
        
        GetBlendShapeTargetsRel() -> Relationship
        
        
        
        """
    @staticmethod
    def GetBlendShapesAttr(*args, **kwargs):
        """
        
        GetBlendShapesAttr() -> Attribute
        
        
        
        """
    @staticmethod
    def GetGeomBindTransform(*args, **kwargs):
        """
        
        GetGeomBindTransform(time) -> Matrix4d
        
        
        Parameters
        ----------
        time : TimeCode
        
        
        """
    @staticmethod
    def GetGeomBindTransformAttr(*args, **kwargs):
        """
        
        GetGeomBindTransformAttr() -> Attribute
        
        
        
        """
    @staticmethod
    def GetInterpolation(*args, **kwargs):
        """
        
        GetInterpolation() -> str
        
        
        
        """
    @staticmethod
    def GetJointIndicesPrimvar(*args, **kwargs):
        """
        
        GetJointIndicesPrimvar() -> Primvar
        
        
        
        """
    @staticmethod
    def GetJointMapper(*args, **kwargs):
        """
        
        GetJointMapper() -> AnimMapper
        
        
        Return a mapper for remapping from the joint order of the skeleton to
        the local joint order of this prim, if any.
        
        
        Returns a null pointer if the prim has no custom joint orer. The
        mapper maps data from the order given by the *joints* order on the
        Skeleton to the order given by the *skel:joints* property, as
        optionally set through the UsdSkelBindingAPI.
        
        
        
        """
    @staticmethod
    def GetJointOrder(*args, **kwargs):
        """
        
        GetJointOrder(jointOrder) -> bool
        
        
        Get the custom joint order for this skinning site, if any.
        
        
        Parameters
        ----------
        jointOrder : TokenArray
        
        
        """
    @staticmethod
    def GetJointWeightsPrimvar(*args, **kwargs):
        """
        
        GetJointWeightsPrimvar() -> Primvar
        
        
        
        """
    @staticmethod
    def GetMapper(*args, **kwargs):
        """
        
        GetMapper() -> AnimMapper
        
        
        Deprecated
        
        Use GetJointMapper.
        
        
        
        """
    @staticmethod
    def GetNumInfluencesPerComponent(*args, **kwargs):
        """
        
        GetNumInfluencesPerComponent() -> int
        
        
        Returns the number of influences encoded for each component.
        
        
        If the prim defines rigid joint influences, then this returns the
        number of influences that map to every point. Otherwise, this provides
        the number of influences per point.
        
        IsRigidlyDeformed
        
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        
        """
    @staticmethod
    def GetSkinningBlendWeightsPrimvar(*args, **kwargs):
        """
        
        GetSkinningBlendWeightsPrimvar() -> Primvar
        
        
        
        """
    @staticmethod
    def GetSkinningMethodAttr(*args, **kwargs):
        """
        
        GetSkinningMethodAttr() -> Attribute
        
        
        
        """
    @staticmethod
    def GetTimeSamples(*args, **kwargs):
        """
        
        GetTimeSamples(times) -> bool
        
        
        Populate ``times`` with the union of time samples for all properties
        that affect skinning, independent of joint transforms and any other
        prim-specific properties (such as points).
        
        
        
        UsdAttribute::GetTimeSamples
        
        
        Parameters
        ----------
        times : list[float]
        
        
        """
    @staticmethod
    def GetTimeSamplesInInterval(*args, **kwargs):
        """
        
        GetTimeSamplesInInterval(interval, times) -> bool
        
        
        Populate ``times`` with the union of time samples within ``interval``
        , for all properties that affect skinning, independent of joint
        transforms and any other prim-specific properties (such as points).
        
        
        
        UsdAttribute::GetTimeSamplesInInterval
        
        
        Parameters
        ----------
        interval : Interval
        
        times : list[float]
        
        
        """
    @staticmethod
    def HasBlendShapes(*args, **kwargs):
        """
        
        HasBlendShapes() -> bool
        
        
        Returns true if there are blend shapes associated with this prim.
        
        
        
        """
    @staticmethod
    def HasJointInfluences(*args, **kwargs):
        """
        
        HasJointInfluences() -> bool
        
        
        Returns true if joint influence data is associated with this prim.
        
        
        
        """
    @staticmethod
    def IsRigidlyDeformed(*args, **kwargs):
        """
        
        IsRigidlyDeformed() -> bool
        
        
        Returns true if the held prim has the same joint influences across all
        points, or false otherwise.
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim, skelJointOrder, blendShapeOrder, jointIndices, jointWeights, geomBindTransform, skinningMethod, skinningBlendWeights, joints, blendShapes, blendShapeTargets)
        
        
        Construct a new skining query for the resolved properties set through
        the UsdSkelBindingAPI, as inherited on ``prim`` .
        
        
        The resulting query will be marked valid only if the inherited
        properties provide proper valid joint influences.
        
        
        Parameters
        ----------
        prim : Prim
        
        skelJointOrder : TokenArray
        
        blendShapeOrder : TokenArray
        
        jointIndices : Attribute
        
        jointWeights : Attribute
        
        geomBindTransform : Attribute
        
        skinningMethod : Attribute
        
        skinningBlendWeights : Attribute
        
        joints : Attribute
        
        blendShapes : Attribute
        
        blendShapeTargets : Relationship
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
class Tokens(Boost.Python.instance):
    bindTransforms: typing.ClassVar[str] = 'bindTransforms'
    blendShapeWeights: typing.ClassVar[str] = 'blendShapeWeights'
    blendShapes: typing.ClassVar[str] = 'blendShapes'
    classicLinear: typing.ClassVar[str] = 'ClassicLinear'
    dualQuaternion: typing.ClassVar[str] = 'DualQuaternion'
    jointNames: typing.ClassVar[str] = 'jointNames'
    joints: typing.ClassVar[str] = 'joints'
    normalOffsets: typing.ClassVar[str] = 'normalOffsets'
    offsets: typing.ClassVar[str] = 'offsets'
    pointIndices: typing.ClassVar[str] = 'pointIndices'
    primvarsSkelGeomBindTransform: typing.ClassVar[str] = 'primvars:skel:geomBindTransform'
    primvarsSkelJointIndices: typing.ClassVar[str] = 'primvars:skel:jointIndices'
    primvarsSkelJointWeights: typing.ClassVar[str] = 'primvars:skel:jointWeights'
    primvarsSkelSkinningBlendWeights: typing.ClassVar[str] = 'primvars:skel:skinningBlendWeights'
    restTransforms: typing.ClassVar[str] = 'restTransforms'
    rotations: typing.ClassVar[str] = 'rotations'
    scales: typing.ClassVar[str] = 'scales'
    skelAnimationSource: typing.ClassVar[str] = 'skel:animationSource'
    skelBlendShapeTargets: typing.ClassVar[str] = 'skel:blendShapeTargets'
    skelBlendShapes: typing.ClassVar[str] = 'skel:blendShapes'
    skelJoints: typing.ClassVar[str] = 'skel:joints'
    skelSkeleton: typing.ClassVar[str] = 'skel:skeleton'
    skelSkinningMethod: typing.ClassVar[str] = 'skel:skinningMethod'
    translations: typing.ClassVar[str] = 'translations'
    weight: typing.ClassVar[str] = 'weight'
    weightedBlend: typing.ClassVar[str] = 'WeightedBlend'
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
    """
    
    Object holding information describing skeleton topology. This provides
    the hierarchical information needed to reason about joint
    relationships in a manner suitable to computations.
    
    """
    @staticmethod
    def GetNumJoints(*args, **kwargs):
        """
        
        GetNumJoints() -> int
        
        
        
        """
    @staticmethod
    def GetParent(*args, **kwargs):
        """
        
        GetParent(index) -> int
        
        
        Returns the parent joint of the ``index'th`` joint, Returns -1 for
        joints with no parent (roots).
        
        
        Parameters
        ----------
        index : int
        
        
        """
    @staticmethod
    def GetParentIndices(*args, **kwargs):
        """
        
        GetParentIndices() -> IntArray
        
        
        
        """
    @staticmethod
    def IsRoot(*args, **kwargs):
        """
        
        IsRoot(index) -> bool
        
        
        Returns true if the ``index'th`` joint is a root joint.
        
        
        Parameters
        ----------
        index : int
        
        
        """
    @staticmethod
    def Validate(*args, **kwargs):
        """
        
        Validate(reason) -> bool
        
        
        Validate the topology.
        
        
        If validation is unsuccessful, a reason why will be written to
        ``reason`` , if provided.
        
        
        Parameters
        ----------
        reason : str
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct an empty topology.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(paths)
        
        
        Construct a skel topology from ``paths`` , an array holding ordered
        joint paths as tokens.
        
        
        Internally, each token must be converted to an SdfPath. If SdfPath
        objects are already accessible, it is more efficient to use the
        construct taking an SdfPath array.
        
        
        Parameters
        ----------
        paths : TfSpan[str]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(paths)
        
        
        Construct a skel topology from ``paths`` , an array of joint paths.
        
        
        Parameters
        ----------
        paths : TfSpan[Path]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(parentIndices)
        
        
        Construct a skel topology from an array of parent indices.
        
        
        For each joint, this provides the parent index of that joint, or -1 if
        none.
        
        
        Parameters
        ----------
        parentIndices : IntArray
        
        
        """
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class _CanApplyResult(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
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
