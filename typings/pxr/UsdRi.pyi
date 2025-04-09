from __future__ import annotations
import pxr.Usd
import typing
__all__ = ['MaterialAPI', 'SplineAPI', 'StatementsAPI', 'TextureAPI', 'Tokens']
class MaterialAPI(pxr.Usd.APISchemaBase):
    """
    
    Deprecated
    
    Materials should use UsdShadeMaterial instead. This schema will be
    removed in a future release.
    
    This API provides outputs that connect a material prim to prman
    shaders and RIS objects.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdRiTokens. So to set an attribute to the value"rightHanded", use
    UsdRiTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> MaterialAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"RiMaterialAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdRiMaterialAPI object is returned upon success. An invalid
        (or empty) UsdRiMaterialAPI object is returned upon failure. See
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
    def ComputeInterfaceInputConsumersMap(*args, **kwargs):
        """
        
        ComputeInterfaceInputConsumersMap(computeTransitiveConsumers) -> NodeGraph.InterfaceInputConsumersMap
        
        
        Walks the namespace subtree below the material and computes a map
        containing the list of all inputs on the material and the associated
        vector of consumers of their values.
        
        
        The consumers can be inputs on shaders within the material or on node-
        graphs under it.
        
        
        Parameters
        ----------
        computeTransitiveConsumers : bool
        
        
        """
    @staticmethod
    def CreateDisplacementAttr(*args, **kwargs):
        """
        
        CreateDisplacementAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDisplacementAttr() , and also Create vs Get Property Methods
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
    def CreateSurfaceAttr(*args, **kwargs):
        """
        
        CreateSurfaceAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetSurfaceAttr() , and also Create vs Get Property Methods for
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
    def CreateVolumeAttr(*args, **kwargs):
        """
        
        CreateVolumeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetVolumeAttr() , and also Create vs Get Property Methods for when
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
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> MaterialAPI
        
        
        Return a UsdRiMaterialAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdRiMaterialAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetDisplacement(*args, **kwargs):
        """
        
        GetDisplacement(ignoreBaseMaterial) -> Shader
        
        
        Returns a valid shader object if the"displacement"output on the
        material is connected to one.
        
        
        If ``ignoreBaseMaterial`` is true and if the"displacement"shader
        source is specified in the base-material of this material, then this
        returns an invalid shader object.
        
        
        Parameters
        ----------
        ignoreBaseMaterial : bool
        
        
        """
    @staticmethod
    def GetDisplacementAttr(*args, **kwargs):
        """
        
        GetDisplacementAttr() -> Attribute
        
        
        
        Declaration
        
        ``token outputs:ri:displacement``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        
        
        """
    @staticmethod
    def GetDisplacementOutput(*args, **kwargs):
        """
        
        GetDisplacementOutput() -> Output
        
        
        Returns the"displacement"output associated with the material.
        
        
        
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
    def GetSurface(*args, **kwargs):
        """
        
        GetSurface(ignoreBaseMaterial) -> Shader
        
        
        Returns a valid shader object if the"surface"output on the material is
        connected to one.
        
        
        If ``ignoreBaseMaterial`` is true and if the"surface"shader source is
        specified in the base-material of this material, then this returns an
        invalid shader object.
        
        
        Parameters
        ----------
        ignoreBaseMaterial : bool
        
        
        """
    @staticmethod
    def GetSurfaceAttr(*args, **kwargs):
        """
        
        GetSurfaceAttr() -> Attribute
        
        
        
        Declaration
        
        ``token outputs:ri:surface``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        
        
        """
    @staticmethod
    def GetSurfaceOutput(*args, **kwargs):
        """
        
        GetSurfaceOutput() -> Output
        
        
        Returns the"surface"output associated with the material.
        
        
        
        """
    @staticmethod
    def GetVolume(*args, **kwargs):
        """
        
        GetVolume(ignoreBaseMaterial) -> Shader
        
        
        Returns a valid shader object if the"volume"output on the material is
        connected to one.
        
        
        If ``ignoreBaseMaterial`` is true and if the"volume"shader source is
        specified in the base-material of this material, then this returns an
        invalid shader object.
        
        
        Parameters
        ----------
        ignoreBaseMaterial : bool
        
        
        """
    @staticmethod
    def GetVolumeAttr(*args, **kwargs):
        """
        
        GetVolumeAttr() -> Attribute
        
        
        
        Declaration
        
        ``token outputs:ri:volume``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        
        
        """
    @staticmethod
    def GetVolumeOutput(*args, **kwargs):
        """
        
        GetVolumeOutput() -> Output
        
        
        Returns the"volume"output associated with the material.
        
        
        
        """
    @staticmethod
    def SetDisplacementSource(*args, **kwargs):
        """
        
        SetDisplacementSource(displacementPath) -> bool
        
        
        Parameters
        ----------
        displacementPath : Path
        
        
        """
    @staticmethod
    def SetSurfaceSource(*args, **kwargs):
        """
        
        SetSurfaceSource(surfacePath) -> bool
        
        
        Parameters
        ----------
        surfacePath : Path
        
        
        """
    @staticmethod
    def SetVolumeSource(*args, **kwargs):
        """
        
        SetVolumeSource(volumePath) -> bool
        
        
        Parameters
        ----------
        volumePath : Path
        
        
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
        
        
        Construct a UsdRiMaterialAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdRiMaterialAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdRiMaterialAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdRiMaterialAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        
        ----------------------------------------------------------------------
        
        __init__(material)
        
        
        A constructor for creating a MaterialAPI object from a material prim.
        
        
        Parameters
        ----------
        material : Material
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class SplineAPI(pxr.Usd.APISchemaBase):
    """
    
    Deprecated
    
    This API schema will be removed in a future release.
    
    RiSplineAPI is a general purpose API schema used to describe a named
    spline stored as a set of attributes on a prim.
    
    It is an add-on schema that can be applied many times to a prim with
    different spline names. All the attributes authored by the schema are
    namespaced under"$NAME:spline:", with the name of the spline providing
    a namespace for the attributes.
    
    The spline describes a 2D piecewise cubic curve with a position and
    value for each knot. This is chosen to give straightforward artistic
    control over the shape. The supported basis types are:
    
       - linear (UsdRiTokens->linear)
    
       - bspline (UsdRiTokens->bspline)
    
       - Catmull-Rom (UsdRiTokens->catmullRom)
    
    
    """
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> SplineAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"RiSplineAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.
        
        A valid UsdRiSplineAPI object is returned upon success. An invalid (or
        empty) UsdRiSplineAPI object is returned upon failure. See
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
    def CreateInterpolationAttr(*args, **kwargs):
        """
        
        CreateInterpolationAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetInterpolationAttr() , and also Create vs Get Property Methods
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
    def CreatePositionsAttr(*args, **kwargs):
        """
        
        CreatePositionsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetPositionsAttr() , and also Create vs Get Property Methods for
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
    def CreateValuesAttr(*args, **kwargs):
        """
        
        CreateValuesAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetValuesAttr() , and also Create vs Get Property Methods for when
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
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> SplineAPI
        
        
        Return a UsdRiSplineAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdRiSplineAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetInterpolationAttr(*args, **kwargs):
        """
        
        GetInterpolationAttr() -> Attribute
        
        
        Interpolation method for the spline.
        
        
        C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
        SdfVariabilityUniform  Fallback Value: linear  Allowed Values :
        [linear, constant, bspline, catmullRom]
        
        
        
        """
    @staticmethod
    def GetPositionsAttr(*args, **kwargs):
        """
        
        GetPositionsAttr() -> Attribute
        
        
        Positions of the knots.
        
        
        C++ Type: VtArray<float>  Usd Type: SdfValueTypeNames->FloatArray
        Variability: SdfVariabilityUniform  Fallback Value: No Fallback
        
        
        
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
    def GetValuesAttr(*args, **kwargs):
        """
        
        GetValuesAttr() -> Attribute
        
        
        Values of the knots.
        
        
        C++ Type: See GetValuesTypeName()  Usd Type: See GetValuesTypeName()
        Variability: SdfVariabilityUniform  Fallback Value: No Fallback
        
        
        
        """
    @staticmethod
    def GetValuesTypeName(*args, **kwargs):
        """
        
        GetValuesTypeName() -> ValueTypeName
        
        
        Returns the intended typename of the values attribute of the spline.
        
        
        
        """
    @staticmethod
    def Validate(*args, **kwargs):
        """
        
        Validate(reason) -> bool
        
        
        Validates the attribute values belonging to the spline.
        
        
        Returns true if the spline has all valid attribute values. Returns
        false and populates the ``reason`` output argument if the spline has
        invalid attribute values.
        
        Here's the list of validations performed by this method:
        
           - the SplineAPI must be fully initialized
        
           - interpolation attribute must exist and use an allowed value
        
           - the positions array must be a float array
        
           - the positions array must be sorted by increasing value
        
           - the values array must use the correct value type
        
           - the positions and values array must have the same size
        
        
        
        Parameters
        ----------
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
        
        
        Construct a UsdRiSplineAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdRiSplineAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdRiSplineAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdRiSplineAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim, splineName, valuesTypeName, doesDuplicateBSplineEndpoints)
        
        
        Construct a UsdRiSplineAPI with the given ``splineName`` on the
        UsdPrim ``prim`` .
        
        
        Parameters
        ----------
        prim : Prim
        
        splineName : str
        
        valuesTypeName : ValueTypeName
        
        doesDuplicateBSplineEndpoints : bool
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj, splineName, valuesTypeName, doesDuplicateBSplineEndpoints)
        
        
        Construct a UsdRiSplineAPI with the given ``splineName`` on the prim
        held by ``schemaObj`` .
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        splineName : str
        
        valuesTypeName : ValueTypeName
        
        doesDuplicateBSplineEndpoints : bool
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class StatementsAPI(pxr.Usd.APISchemaBase):
    """
    
    Container namespace schema for all renderman statements.
    
    The longer term goal is for clients to go directly to primvar or
    render-attribute API's, instead of using UsdRi StatementsAPI for
    inherited attributes. Anticpating this, StatementsAPI can smooth the
    way via a few environment variables:
    
       - USDRI_STATEMENTS_READ_OLD_ENCODING: Causes StatementsAPI to read
         old-style attributes instead of primvars in the"ri:"namespace.
    
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> StatementsAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"StatementsAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdRiStatementsAPI object is returned upon success. An invalid
        (or empty) UsdRiStatementsAPI object is returned upon failure. See
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
    def CreateRiAttribute(*args, **kwargs):
        """
        
        CreateRiAttribute(name, riType, nameSpace) -> Attribute
        
        
        Create a rib attribute on the prim to which this schema is attached.
        
        
        A rib attribute consists of an attribute *"nameSpace"* and an
        attribute *"name"*. For example, the namespace"cull"may define
        attributes"backfacing"and"hidden", and user-defined attributes belong
        to the namespace"user".
        
        This method makes no attempt to validate that the given ``nameSpace``
        and *name* are actually meaningful to prman or any other renderer.
        
        riType
        
        should be a known RenderMan type definition, which can be array-
        valued. For instance, both"color"and"float[3]"are valid values for
        ``riType`` .
        
        
        Parameters
        ----------
        name : str
        
        riType : str
        
        nameSpace : str
        
        
        
        ----------------------------------------------------------------------
        
        CreateRiAttribute(name, tfType, nameSpace) -> Attribute
        
        
        Creates an attribute of the given ``tfType`` .
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        name : str
        
        tfType : Type
        
        nameSpace : str
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> StatementsAPI
        
        
        Return a UsdRiStatementsAPI holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdRiStatementsAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetCoordinateSystem(*args, **kwargs):
        """
        
        GetCoordinateSystem() -> str
        
        
        Returns the value in the"ri:coordinateSystem"attribute if it exists.
        
        
        
        """
    @staticmethod
    def GetModelCoordinateSystems(*args, **kwargs):
        """
        
        GetModelCoordinateSystems(targets) -> bool
        
        
        Populates the output ``targets`` with the authored
        ri:modelCoordinateSystems, if any.
        
        
        Returns true if the query was successful.
        
        
        Parameters
        ----------
        targets : list[Path]
        
        
        """
    @staticmethod
    def GetModelScopedCoordinateSystems(*args, **kwargs):
        """
        
        GetModelScopedCoordinateSystems(targets) -> bool
        
        
        Populates the output ``targets`` with the authored
        ri:modelScopedCoordinateSystems, if any.
        
        
        Returns true if the query was successful.
        
        
        Parameters
        ----------
        targets : list[Path]
        
        
        """
    @staticmethod
    def GetRiAttribute(*args, **kwargs):
        """
        
        GetRiAttribute(name, nameSpace) -> Attribute
        
        
        Return a UsdAttribute representing the Ri attribute with the name
        *name*, in the namespace *nameSpace*.
        
        
        The attribute returned may or may not **actually** exist so it must be
        checked for validity.
        
        
        Parameters
        ----------
        name : str
        
        nameSpace : str
        
        
        """
    @staticmethod
    def GetRiAttributeName(*args, **kwargs):
        """
        
        **classmethod** GetRiAttributeName(prop) -> str
        
        
        Return the base, most-specific name of the rib attribute.
        
        
        For example, the *name* of the rib
        attribute"cull:backfacing"is"backfacing"
        
        
        Parameters
        ----------
        prop : Property
        
        
        """
    @staticmethod
    def GetRiAttributeNameSpace(*args, **kwargs):
        """
        
        **classmethod** GetRiAttributeNameSpace(prop) -> str
        
        
        Return the containing namespace of the rib attribute (e.g."user").
        
        
        Parameters
        ----------
        prop : Property
        
        
        """
    @staticmethod
    def GetRiAttributes(*args, **kwargs):
        """
        
        GetRiAttributes(nameSpace) -> list[Property]
        
        
        Return all rib attributes on this prim, or under a specific namespace
        (e.g."user").
        
        
        As noted above, rib attributes can be either UsdAttribute or
        UsdRelationship, and like all UsdProperties, need not have a defined
        value.
        
        
        Parameters
        ----------
        nameSpace : str
        
        
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
    def GetScopedCoordinateSystem(*args, **kwargs):
        """
        
        GetScopedCoordinateSystem() -> str
        
        
        Returns the value in the"ri:scopedCoordinateSystem"attribute if it
        exists.
        
        
        
        """
    @staticmethod
    def HasCoordinateSystem(*args, **kwargs):
        """
        
        HasCoordinateSystem() -> bool
        
        
        Returns true if the underlying prim has a ri:coordinateSystem opinion.
        
        
        
        """
    @staticmethod
    def HasScopedCoordinateSystem(*args, **kwargs):
        """
        
        HasScopedCoordinateSystem() -> bool
        
        
        Returns true if the underlying prim has a ri:scopedCoordinateSystem
        opinion.
        
        
        
        """
    @staticmethod
    def IsRiAttribute(*args, **kwargs):
        """
        
        **classmethod** IsRiAttribute(prop) -> bool
        
        
        Return true if the property is in the"ri:attributes"namespace.
        
        
        Parameters
        ----------
        prop : Property
        
        
        """
    @staticmethod
    def MakeRiAttributePropertyName(*args, **kwargs):
        """
        
        **classmethod** MakeRiAttributePropertyName(attrName) -> str
        
        
        Returns the given ``attrName`` prefixed with the full Ri attribute
        namespace, creating a name suitable for an RiAttribute UsdProperty.
        
        
        This handles conversion of common separator characters used in other
        packages, such as periods and underscores.
        
        Will return empty string if attrName is not a valid property
        identifier; otherwise, will return a valid property name that
        identifies the property as an RiAttribute, according to the following
        rules:
        
           - If ``attrName`` is already a properly constructed RiAttribute
             property name, return it unchanged.
        
           - If ``attrName`` contains two or more tokens separated by a
             *colon*, consider the first to be the namespace, and the rest the
             name, joined by underscores
        
           - If ``attrName`` contains two or more tokens separated by a
             *period*, consider the first to be the namespace, and the rest the
             name, joined by underscores
        
           - If ``attrName`` contains two or more tokens separated by an,
             *underscore* consider the first to be the namespace, and the rest the
             name, joined by underscores
        
           - else, assume ``attrName`` is the name, and"user"is the namespace
        
        
        
        Parameters
        ----------
        attrName : str
        
        
        """
    @staticmethod
    def SetCoordinateSystem(*args, **kwargs):
        """
        
        SetCoordinateSystem(coordSysName) -> None
        
        
        Sets the"ri:coordinateSystem"attribute to the given string value,
        creating the attribute if needed.
        
        
        That identifies this prim as providing a coordinate system, which can
        be retrieved via UsdGeomXformable::GetTransformAttr(). Also adds the
        owning prim to the ri:modelCoordinateSystems relationship targets on
        its parent leaf model prim, if it exists. If this prim is not under a
        leaf model, no relationship targets will be authored.
        
        
        Parameters
        ----------
        coordSysName : str
        
        
        """
    @staticmethod
    def SetScopedCoordinateSystem(*args, **kwargs):
        """
        
        SetScopedCoordinateSystem(coordSysName) -> None
        
        
        Sets the"ri:scopedCoordinateSystem"attribute to the given string
        value, creating the attribute if needed.
        
        
        That identifies this prim as providing a coordinate system, which can
        be retrieved via UsdGeomXformable::GetTransformAttr(). Such coordinate
        systems are local to the RI attribute stack state, but does get
        updated properly for instances when defined inside an object master.
        Also adds the owning prim to the ri:modelScopedCoordinateSystems
        relationship targets on its parent leaf model prim, if it exists. If
        this prim is not under a leaf model, no relationship targets will be
        authored.
        
        
        Parameters
        ----------
        coordSysName : str
        
        
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
        
        
        Construct a UsdRiStatementsAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdRiStatementsAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdRiStatementsAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdRiStatementsAPI (schemaObj.GetPrim()), as
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
class TextureAPI(pxr.Usd.APISchemaBase):
    """
    
    Deprecated
    
    This API schema will be removed in a future release.
    
    RiTextureAPI is an API schema that provides an interface to add
    Renderman-specific attributes to adjust textures.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> TextureAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"RiTextureAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.
        
        A valid UsdRiTextureAPI object is returned upon success. An invalid
        (or empty) UsdRiTextureAPI object is returned upon failure. See
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
    def CreateRiTextureGammaAttr(*args, **kwargs):
        """
        
        CreateRiTextureGammaAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetRiTextureGammaAttr() , and also Create vs Get Property Methods
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
    def CreateRiTextureSaturationAttr(*args, **kwargs):
        """
        
        CreateRiTextureSaturationAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetRiTextureSaturationAttr() , and also Create vs Get Property
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
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> TextureAPI
        
        
        Return a UsdRiTextureAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdRiTextureAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetRiTextureGammaAttr(*args, **kwargs):
        """
        
        GetRiTextureGammaAttr() -> Attribute
        
        
        Gamma-correct the texture.
        
        
        
        Declaration
        
        ``float ri:texture:gamma``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetRiTextureSaturationAttr(*args, **kwargs):
        """
        
        GetRiTextureSaturationAttr() -> Attribute
        
        
        Adjust the texture's saturation.
        
        
        
        Declaration
        
        ``float ri:texture:saturation``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
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
        
        
        Construct a UsdRiTextureAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdRiTextureAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdRiTextureAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdRiTextureAPI (schemaObj.GetPrim()), as it
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
class Tokens(Boost.Python.instance):
    bspline: typing.ClassVar[str] = 'bspline'
    catmullRom: typing.ClassVar[str] = 'catmull-rom'
    constant: typing.ClassVar[str] = 'constant'
    interpolation: typing.ClassVar[str] = 'interpolation'
    linear: typing.ClassVar[str] = 'linear'
    outputsRiDisplacement: typing.ClassVar[str] = 'outputs:ri:displacement'
    outputsRiSurface: typing.ClassVar[str] = 'outputs:ri:surface'
    outputsRiVolume: typing.ClassVar[str] = 'outputs:ri:volume'
    positions: typing.ClassVar[str] = 'positions'
    renderContext: typing.ClassVar[str] = 'ri'
    riTextureGamma: typing.ClassVar[str] = 'ri:texture:gamma'
    riTextureSaturation: typing.ClassVar[str] = 'ri:texture:saturation'
    spline: typing.ClassVar[str] = 'spline'
    values: typing.ClassVar[str] = 'values'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
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
__MFB_FULL_PACKAGE_NAME: str = 'usdRi'
