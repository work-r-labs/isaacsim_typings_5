from __future__ import annotations
import pxr.Usd
import typing
__all__ = ['DenoisePass', 'Pass', 'Product', 'Settings', 'SettingsBase', 'Tokens', 'Var']
class DenoisePass(pxr.Usd.Typed):
    """
    
    A RenderDenoisePass generates renders via a denoising process. This
    may be the same renderer that a pipeline uses for UsdRender, or may be
    a separate one. Notably, a RenderDenoisePass requires another Pass to
    be present for it to operate. The denoising process itself is not
    generative, and requires images inputs to operate.
    
    As denoising integration varies so widely across pipelines, all
    implementation details are left to pipeline-specific prims that
    inherit from RenderDenoisePass.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> DenoisePass
        
        
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
        
        **classmethod** Get(stage, path) -> DenoisePass
        
        
        Return a UsdRenderDenoisePass holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdRenderDenoisePass(stage->GetPrimAtPath(path));
        
        
        
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
        
        
        Construct a UsdRenderDenoisePass on UsdPrim ``prim`` .
        
        
        Equivalent to UsdRenderDenoisePass::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdRenderDenoisePass on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdRenderDenoisePass (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        
        
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
class Pass(pxr.Usd.Typed):
    """
    
    A RenderPass prim encapsulates the necessary information to generate
    multipass renders. It houses properties for generating dependencies
    and the necessary commands to run to generate renders, as well as
    visibility controls for the scene. While RenderSettings describes the
    information needed to generate images from a single invocation of a
    renderer, RenderPass describes the additional information needed to
    generate a time varying set of images.
    
    There are two consumers of RenderPass prims - a runtime executable
    that generates images from usdRender prims, and pipeline specific code
    that translates between usdRender prims and the pipeline's resource
    scheduling software. We'll refer to the latter as'job submission
    code'.
    
    The name of the prim is used as the pass's name.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdRenderTokens. So to set an attribute to the value"rightHanded",
    use UsdRenderTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateCommandAttr(*args, **kwargs):
        """
        
        CreateCommandAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetCommandAttr() , and also Create vs Get Property Methods for
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
    def CreateDenoiseEnableAttr(*args, **kwargs):
        """
        
        CreateDenoiseEnableAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDenoiseEnableAttr() , and also Create vs Get Property Methods
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
    def CreateDenoisePassRel(*args, **kwargs):
        """
        
        CreateDenoisePassRel() -> Relationship
        
        
        See GetDenoisePassRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateFileNameAttr(*args, **kwargs):
        """
        
        CreateFileNameAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetFileNameAttr() , and also Create vs Get Property Methods for
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
    def CreateInputPassesRel(*args, **kwargs):
        """
        
        CreateInputPassesRel() -> Relationship
        
        
        See GetInputPassesRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreatePassTypeAttr(*args, **kwargs):
        """
        
        CreatePassTypeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetPassTypeAttr() , and also Create vs Get Property Methods for
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
    def CreateRenderSourceRel(*args, **kwargs):
        """
        
        CreateRenderSourceRel() -> Relationship
        
        
        See GetRenderSourceRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Pass
        
        
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
        
        **classmethod** Get(stage, path) -> Pass
        
        
        Return a UsdRenderPass holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdRenderPass(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetCommandAttr(*args, **kwargs):
        """
        
        GetCommandAttr() -> Attribute
        
        
        The command to run in order to generate renders for this pass.
        
        
        The job submission code can use this to properly send tasks to the job
        scheduling software that will generate products.
        
        The command can contain variables that will be substituted
        appropriately during submission, as seen in the example below with
        {fileName}.
        
        For example: command[0] ="prman"command[1] ="-progress"command[2]
        ="-pixelvariance"command[3] ="-0.15"command[4] ="{fileName}"# the
        fileName property will be substituted
        
        Declaration
        
        ``uniform string[] command``
        
        C++ Type
        
        VtArray<std::string>
        
        Usd Type
        
        SdfValueTypeNames->StringArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetDenoiseEnableAttr(*args, **kwargs):
        """
        
        GetDenoiseEnableAttr() -> Attribute
        
        
        When True, this Pass pass should be denoised.
        
        
        
        Declaration
        
        ``uniform bool denoise:enable = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetDenoisePassRel(*args, **kwargs):
        """
        
        GetDenoisePassRel() -> Relationship
        
        
        The The UsdRenderDenoisePass prim from which to source denoise
        settings.
        
        
        
        """
    @staticmethod
    def GetFileNameAttr(*args, **kwargs):
        """
        
        GetFileNameAttr() -> Attribute
        
        
        The asset that contains the rendering prims or other information
        needed to render this pass.
        
        
        
        Declaration
        
        ``uniform asset fileName``
        
        C++ Type
        
        SdfAssetPath
        
        Usd Type
        
        SdfValueTypeNames->Asset
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetInputPassesRel(*args, **kwargs):
        """
        
        GetInputPassesRel() -> Relationship
        
        
        The set of other Passes that this Pass depends on in order to be
        constructed properly.
        
        
        For example, a Pass A may generate a texture, which is then used as an
        input to Pass B.
        
        By default, usdRender makes some assumptions about the relationship
        between this prim and the prims listed in inputPasses. Namely, when
        per-frame tasks are generated from these pass prims, usdRender will
        assume a one-to-one relationship between tasks that share their frame
        number. Consider a pass named'composite'whose *inputPasses* targets a
        Pass prim named'beauty`.  By default, each frame for'composite'will
        depend on the same frame from'beauty': beauty.1 ->composite.1 beauty.2
        \\->composite.2 etc
        
        The consumer of this RenderPass graph of inputs will need to resolve
        the transitive dependencies.
        
        
        
        """
    @staticmethod
    def GetPassTypeAttr(*args, **kwargs):
        """
        
        GetPassTypeAttr() -> Attribute
        
        
        A string used to categorize differently structured or executed types
        of passes within a customized pipeline.
        
        
        For example, when multiple DCC's (e.g. Houdini, Katana, Nuke) each
        compute and contribute different Products to a final result, it may be
        clearest and most flexible to create a separate RenderPass for each.
        
        Declaration
        
        ``uniform token passType``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetRenderSourceRel(*args, **kwargs):
        """
        
        GetRenderSourceRel() -> Relationship
        
        
        The source prim to render from.
        
        
        If *fileName* is not present, the source is assumed to be a
        RenderSettings prim present in the current Usd stage. If fileName is
        present, the source should be found in the file there. This
        relationship might target a string attribute on this or another prim
        that identifies the appropriate object in the external container.
        
        For example, for a Usd-backed pass, this would point to a
        RenderSettings prim. Houdini passes would point to a Rop. Nuke passes
        would point to a write node.
        
        
        
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
        
        
        Construct a UsdRenderPass on UsdPrim ``prim`` .
        
        
        Equivalent to UsdRenderPass::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* ``prim`` , but will not immediately throw an error for an
        invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdRenderPass on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdRenderPass (schemaObj.GetPrim()), as it
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
class Product(SettingsBase):
    """
    
    A UsdRenderProduct describes an image or other file-like artifact
    produced by a render. A RenderProduct combines one or more RenderVars
    into a file or interactive buffer. It also provides all the controls
    established in UsdRenderSettingsBase as optional overrides to whatever
    the owning UsdRenderSettings prim dictates.
    
    Specific renderers may support additional settings, such as a way to
    configure compression settings, filetype metadata, and so forth. Such
    settings can be encoded using renderer-specific API schemas applied to
    the product prim.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdRenderTokens. So to set an attribute to the value"rightHanded",
    use UsdRenderTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateOrderedVarsRel(*args, **kwargs):
        """
        
        CreateOrderedVarsRel() -> Relationship
        
        
        See GetOrderedVarsRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateProductNameAttr(*args, **kwargs):
        """
        
        CreateProductNameAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetProductNameAttr() , and also Create vs Get Property Methods for
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
    def CreateProductTypeAttr(*args, **kwargs):
        """
        
        CreateProductTypeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetProductTypeAttr() , and also Create vs Get Property Methods for
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
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Product
        
        
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
        
        **classmethod** Get(stage, path) -> Product
        
        
        Return a UsdRenderProduct holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdRenderProduct(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetOrderedVarsRel(*args, **kwargs):
        """
        
        GetOrderedVarsRel() -> Relationship
        
        
        Specifies the RenderVars that should be consumed and combined into the
        final product.
        
        
        If ordering is relevant to the output driver, then the ordering of
        targets in this relationship provides the order to use.
        
        
        
        """
    @staticmethod
    def GetProductNameAttr(*args, **kwargs):
        """
        
        GetProductNameAttr() -> Attribute
        
        
        Specifies the name that the output/display driver should give the
        product.
        
        
        This is provided as-authored to the driver, whose responsibility it is
        to situate the product on a filesystem or other storage, in the
        desired location.
        
        Declaration
        
        ``token productName =""``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        
        
        """
    @staticmethod
    def GetProductTypeAttr(*args, **kwargs):
        """
        
        GetProductTypeAttr() -> Attribute
        
        
        The type of output to produce.
        
        
        The default,"raster", indicates a 2D image.
        
        In the future, UsdRender may define additional product types.
        
        Declaration
        
        ``uniform token productType ="raster"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
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
        
        
        Construct a UsdRenderProduct on UsdPrim ``prim`` .
        
        
        Equivalent to UsdRenderProduct::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdRenderProduct on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdRenderProduct (schemaObj.GetPrim()), as it
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
class Settings(SettingsBase):
    """
    
    A UsdRenderSettings prim specifies global settings for a render
    process, including an enumeration of the RenderProducts that should
    result, and the UsdGeomImageable purposes that should be rendered. How
    settings affect rendering
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdRenderTokens. So to set an attribute to the value"rightHanded",
    use UsdRenderTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateIncludedPurposesAttr(*args, **kwargs):
        """
        
        CreateIncludedPurposesAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetIncludedPurposesAttr() , and also Create vs Get Property
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
    def CreateMaterialBindingPurposesAttr(*args, **kwargs):
        """
        
        CreateMaterialBindingPurposesAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetMaterialBindingPurposesAttr() , and also Create vs Get Property
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
    def CreateProductsRel(*args, **kwargs):
        """
        
        CreateProductsRel() -> Relationship
        
        
        See GetProductsRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateRenderingColorSpaceAttr(*args, **kwargs):
        """
        
        CreateRenderingColorSpaceAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetRenderingColorSpaceAttr() , and also Create vs Get Property
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
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Settings
        
        
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
        
        **classmethod** Get(stage, path) -> Settings
        
        
        Return a UsdRenderSettings holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdRenderSettings(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetIncludedPurposesAttr(*args, **kwargs):
        """
        
        GetIncludedPurposesAttr() -> Attribute
        
        
        The list of UsdGeomImageable *purpose* values that should be included
        in the render.
        
        
        Note this cannot be specified per-RenderProduct because it is a
        statement of which geometry is present.
        
        Declaration
        
        ``uniform token[] includedPurposes = ["default","render"]``
        
        C++ Type
        
        VtArray<TfToken>
        
        Usd Type
        
        SdfValueTypeNames->TokenArray
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetMaterialBindingPurposesAttr(*args, **kwargs):
        """
        
        GetMaterialBindingPurposesAttr() -> Attribute
        
        
        Ordered list of material purposes to consider when resolving material
        bindings in the scene.
        
        
        The empty string indicates the"allPurpose"binding.
        
        Declaration
        
        ``uniform token[] materialBindingPurposes = ["full",""]``
        
        C++ Type
        
        VtArray<TfToken>
        
        Usd Type
        
        SdfValueTypeNames->TokenArray
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        full, preview,""
        
        
        
        """
    @staticmethod
    def GetProductsRel(*args, **kwargs):
        """
        
        GetProductsRel() -> Relationship
        
        
        The set of RenderProducts the render should produce.
        
        
        This relationship should target UsdRenderProduct prims. If no
        *products* are specified, an application should produce an rgb image
        according to the RenderSettings configuration, to a default display or
        image name.
        
        
        
        """
    @staticmethod
    def GetRenderingColorSpaceAttr(*args, **kwargs):
        """
        
        GetRenderingColorSpaceAttr() -> Attribute
        
        
        Describes a renderer's working (linear) colorSpace where all the
        renderer/shader math is expected to happen.
        
        
        When no renderingColorSpace is provided, renderer should use its own
        default.
        
        Declaration
        
        ``uniform token renderingColorSpace``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
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
    def GetStageRenderSettings(*args, **kwargs):
        """
        
        **classmethod** GetStageRenderSettings(stage) -> Settings
        
        
        Fetch and return ``stage`` 's render settings, as indicated by root
        layer metadata.
        
        
        If unauthored, or the metadata does not refer to a valid
        UsdRenderSettings prim, this will return an invalid UsdRenderSettings
        prim.
        
        
        Parameters
        ----------
        stage : UsdStageWeak
        
        
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
        
        
        Construct a UsdRenderSettings on UsdPrim ``prim`` .
        
        
        Equivalent to UsdRenderSettings::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdRenderSettings on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdRenderSettings (schemaObj.GetPrim()), as
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
class SettingsBase(pxr.Usd.Typed):
    """
    
    Abstract base class that defines render settings that can be specified
    on either a RenderSettings prim or a RenderProduct prim.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdRenderTokens. So to set an attribute to the value"rightHanded",
    use UsdRenderTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateAspectRatioConformPolicyAttr(*args, **kwargs):
        """
        
        CreateAspectRatioConformPolicyAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetAspectRatioConformPolicyAttr() , and also Create vs Get
        Property Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateCameraRel(*args, **kwargs):
        """
        
        CreateCameraRel() -> Relationship
        
        
        See GetCameraRel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateDataWindowNDCAttr(*args, **kwargs):
        """
        
        CreateDataWindowNDCAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDataWindowNDCAttr() , and also Create vs Get Property Methods
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
    def CreateDisableMotionBlurAttr(*args, **kwargs):
        """
        
        CreateDisableMotionBlurAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDisableMotionBlurAttr() , and also Create vs Get Property
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
    def CreateInstantaneousShutterAttr(*args, **kwargs):
        """
        
        CreateInstantaneousShutterAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetInstantaneousShutterAttr() , and also Create vs Get Property
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
    def CreatePixelAspectRatioAttr(*args, **kwargs):
        """
        
        CreatePixelAspectRatioAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetPixelAspectRatioAttr() , and also Create vs Get Property
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
    def CreateResolutionAttr(*args, **kwargs):
        """
        
        CreateResolutionAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetResolutionAttr() , and also Create vs Get Property Methods for
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
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> SettingsBase
        
        
        Return a UsdRenderSettingsBase holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdRenderSettingsBase(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetAspectRatioConformPolicyAttr(*args, **kwargs):
        """
        
        GetAspectRatioConformPolicyAttr() -> Attribute
        
        
        Indicates the policy to use to resolve an aspect ratio mismatch
        between the camera aperture and image settings.
        
        
        This policy allows a standard render setting to do something
        reasonable given varying camera inputs.
        
        The camera aperture aspect ratio is determined by the aperture
        atributes on the UsdGeomCamera.
        
        The image aspect ratio is determined by the resolution and
        pixelAspectRatio attributes in the render settings.
        
           - "expandAperture": if necessary, expand the aperture to fit the
             image, exposing additional scene content
        
           - "cropAperture": if necessary, crop the aperture to fit the image,
             cropping scene content
        
           - "adjustApertureWidth": if necessary, adjust aperture width to
             make its aspect ratio match the image
        
           - "adjustApertureHeight": if necessary, adjust aperture height to
             make its aspect ratio match the image
        
           - "adjustPixelAspectRatio": compute pixelAspectRatio to make the
             image exactly cover the aperture; disregards existing attribute value
             of pixelAspectRatio
        
        Declaration
        
        ``uniform token aspectRatioConformPolicy ="expandAperture"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        expandAperture, cropAperture, adjustApertureWidth,
        adjustApertureHeight, adjustPixelAspectRatio
        
        
        
        """
    @staticmethod
    def GetCameraRel(*args, **kwargs):
        """
        
        GetCameraRel() -> Relationship
        
        
        The *camera* relationship specifies the primary camera to use in a
        render.
        
        
        It must target a UsdGeomCamera.
        
        
        
        """
    @staticmethod
    def GetDataWindowNDCAttr(*args, **kwargs):
        """
        
        GetDataWindowNDCAttr() -> Attribute
        
        
        dataWindowNDC specifies the axis-aligned rectangular region in the
        adjusted aperture window within which the renderer should produce
        data.
        
        
        It is specified as (xmin, ymin, xmax, ymax) in normalized device
        coordinates, where the range 0 to 1 corresponds to the aperture. (0,0)
        corresponds to the bottom-left corner and (1,1) corresponds to the
        upper-right corner.
        
        Specifying a window outside the unit square will produce overscan
        data. Specifying a window that does not cover the unit square will
        produce a cropped render.
        
        A pixel is included in the rendered result if the pixel center is
        contained by the data window. This is consistent with standard rules
        used by polygon rasterization engines. UsdRenderRasterization
        
        The data window is expressed in NDC so that cropping and overscan may
        be resolution independent. In interactive workflows, incremental
        cropping and resolution adjustment may be intermixed to isolate and
        examine parts of the scene. In compositing workflows, overscan may be
        used to support image post-processing kernels, and reduced-resolution
        proxy renders may be used for faster iteration.
        
        The dataWindow:ndc coordinate system references the aperture after any
        adjustments required by aspectRatioConformPolicy.
        
        Declaration
        
        ``uniform float4 dataWindowNDC = (0, 0, 1, 1)``
        
        C++ Type
        
        GfVec4f
        
        Usd Type
        
        SdfValueTypeNames->Float4
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetDisableMotionBlurAttr(*args, **kwargs):
        """
        
        GetDisableMotionBlurAttr() -> Attribute
        
        
        Disable all motion blur by setting the shutter interval of the
        targeted camera to [0,0] - that is, take only one sample, namely at
        the current time code.
        
        
        
        Declaration
        
        ``uniform bool disableMotionBlur = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetInstantaneousShutterAttr(*args, **kwargs):
        """
        
        GetInstantaneousShutterAttr() -> Attribute
        
        
        Deprecated - use disableMotionBlur instead.
        
        
        Override the targeted *camera* 's *shutterClose* to be equal to the
        value of its *shutterOpen*, to produce a zero-width shutter interval.
        This gives us a convenient way to disable motion blur.
        
        Declaration
        
        ``uniform bool instantaneousShutter = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetPixelAspectRatioAttr(*args, **kwargs):
        """
        
        GetPixelAspectRatioAttr() -> Attribute
        
        
        The aspect ratio (width/height) of image pixels.
        
        
        The default ratio 1.0 indicates square pixels.
        
        Declaration
        
        ``uniform float pixelAspectRatio = 1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetResolutionAttr(*args, **kwargs):
        """
        
        GetResolutionAttr() -> Attribute
        
        
        The image pixel resolution, corresponding to the camera's screen
        window.
        
        
        
        Declaration
        
        ``uniform int2 resolution = (2048, 1080)``
        
        C++ Type
        
        GfVec2i
        
        Usd Type
        
        SdfValueTypeNames->Int2
        
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
        
        
        Construct a UsdRenderSettingsBase on UsdPrim ``prim`` .
        
        
        Equivalent to UsdRenderSettingsBase::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdRenderSettingsBase on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdRenderSettingsBase (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        
        
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
    adjustApertureHeight: typing.ClassVar[str] = 'adjustApertureHeight'
    adjustApertureWidth: typing.ClassVar[str] = 'adjustApertureWidth'
    adjustPixelAspectRatio: typing.ClassVar[str] = 'adjustPixelAspectRatio'
    aspectRatioConformPolicy: typing.ClassVar[str] = 'aspectRatioConformPolicy'
    camera: typing.ClassVar[str] = 'camera'
    color3f: typing.ClassVar[str] = 'color3f'
    command: typing.ClassVar[str] = 'command'
    cropAperture: typing.ClassVar[str] = 'cropAperture'
    dataType: typing.ClassVar[str] = 'dataType'
    dataWindowNDC: typing.ClassVar[str] = 'dataWindowNDC'
    denoiseEnable: typing.ClassVar[str] = 'denoise:enable'
    denoisePass: typing.ClassVar[str] = 'denoise:pass'
    disableMotionBlur: typing.ClassVar[str] = 'disableMotionBlur'
    expandAperture: typing.ClassVar[str] = 'expandAperture'
    fileName: typing.ClassVar[str] = 'fileName'
    full: typing.ClassVar[str] = 'full'
    includedPurposes: typing.ClassVar[str] = 'includedPurposes'
    inputPasses: typing.ClassVar[str] = 'inputPasses'
    instantaneousShutter: typing.ClassVar[str] = 'instantaneousShutter'
    intrinsic: typing.ClassVar[str] = 'intrinsic'
    lpe: typing.ClassVar[str] = 'lpe'
    materialBindingPurposes: typing.ClassVar[str] = 'materialBindingPurposes'
    orderedVars: typing.ClassVar[str] = 'orderedVars'
    passType: typing.ClassVar[str] = 'passType'
    pixelAspectRatio: typing.ClassVar[str] = 'pixelAspectRatio'
    preview: typing.ClassVar[str] = 'preview'
    primvar: typing.ClassVar[str] = 'primvar'
    productName: typing.ClassVar[str] = 'productName'
    productType: typing.ClassVar[str] = 'productType'
    products: typing.ClassVar[str] = 'products'
    raster: typing.ClassVar[str] = 'raster'
    raw: typing.ClassVar[str] = 'raw'
    renderSettingsPrimPath: typing.ClassVar[str] = 'renderSettingsPrimPath'
    renderSource: typing.ClassVar[str] = 'renderSource'
    renderingColorSpace: typing.ClassVar[str] = 'renderingColorSpace'
    resolution: typing.ClassVar[str] = 'resolution'
    sourceName: typing.ClassVar[str] = 'sourceName'
    sourceType: typing.ClassVar[str] = 'sourceType'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Var(pxr.Usd.Typed):
    """
    
    A UsdRenderVar describes a custom data variable for a render to
    produce. The prim describes the source of the data, which can be a
    shader output or an LPE (Light Path Expression), and also allows
    encoding of (generally renderer-specific) parameters that configure
    the renderer for computing the variable.
    
    The name of the RenderVar prim drives the name of the data variable
    that the renderer will produce.
    
    In the future, UsdRender may standardize RenderVar representation for
    well-known variables under the sourceType ``intrinsic`` , such as *r*,
    *g*, *b*, *a*, *z*, or *id*. For any described attribute *Fallback*
    *Value* or *Allowed* *Values* below that are text/tokens, the actual
    token is published and defined in UsdRenderTokens. So to set an
    attribute to the value"rightHanded", use UsdRenderTokens->rightHanded
    as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateDataTypeAttr(*args, **kwargs):
        """
        
        CreateDataTypeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDataTypeAttr() , and also Create vs Get Property Methods for
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
    def CreateSourceNameAttr(*args, **kwargs):
        """
        
        CreateSourceNameAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetSourceNameAttr() , and also Create vs Get Property Methods for
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
    def CreateSourceTypeAttr(*args, **kwargs):
        """
        
        CreateSourceTypeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetSourceTypeAttr() , and also Create vs Get Property Methods for
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
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Var
        
        
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
        
        **classmethod** Get(stage, path) -> Var
        
        
        Return a UsdRenderVar holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdRenderVar(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetDataTypeAttr(*args, **kwargs):
        """
        
        GetDataTypeAttr() -> Attribute
        
        
        The type of this channel, as a USD attribute type.
        
        
        
        Declaration
        
        ``uniform token dataType ="color3f"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
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
    def GetSourceNameAttr(*args, **kwargs):
        """
        
        GetSourceNameAttr() -> Attribute
        
        
        The renderer should look for an output of this name as the computed
        value for the RenderVar.
        
        
        
        Declaration
        
        ``uniform string sourceName =""``
        
        C++ Type
        
        std::string
        
        Usd Type
        
        SdfValueTypeNames->String
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetSourceTypeAttr(*args, **kwargs):
        """
        
        GetSourceTypeAttr() -> Attribute
        
        
        Indicates the type of the source.
        
        
        
           - "raw": The name should be passed directly to the renderer. This
             is the default behavior.
        
           - "primvar": This source represents the name of a primvar. Some
             renderers may use this to ensure that the primvar is provided; other
             renderers may require that a suitable material network be provided, in
             which case this is simply an advisory setting.
        
           - "lpe": Specifies a Light Path Expression in the OSL Light Path
             Expressions language as the source for this RenderVar. Some renderers
             may use extensions to that syntax, which will necessarily be non-
             portable.
        
           - "intrinsic": This setting is currently unimplemented, but
             represents a future namespace for UsdRender to provide portable
             baseline RenderVars, such as camera depth, that may have varying
             implementations for each renderer.
        
        Declaration
        
        ``uniform token sourceType ="raw"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        raw, primvar, lpe, intrinsic
        
        
        
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
        
        
        Construct a UsdRenderVar on UsdPrim ``prim`` .
        
        
        Equivalent to UsdRenderVar::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* ``prim`` , but will not immediately throw an error for an
        invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdRenderVar on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdRenderVar (schemaObj.GetPrim()), as it
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
__MFB_FULL_PACKAGE_NAME: str = 'usdRender'
