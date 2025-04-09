from __future__ import annotations
import pxr.Usd
import typing
__all__ = ['GenerativeProceduralAPI', 'Tokens']
class GenerativeProceduralAPI(pxr.Usd.APISchemaBase):
    """
    
    This API extends and configures the core UsdProcGenerativeProcedural
    schema defined within usdProc for use with hydra generative
    procedurals as defined within hdGp.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdHydraTokens. So to set an attribute to the value"rightHanded",
    use UsdHydraTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> GenerativeProceduralAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"HydraGenerativeProceduralAPI"to
        the token-valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdHydraGenerativeProceduralAPI object is returned upon
        success. An invalid (or empty) UsdHydraGenerativeProceduralAPI object
        is returned upon failure. See UsdPrim::ApplyAPI() for conditions
        resulting in failure.
        
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
    def CreateProceduralSystemAttr(*args, **kwargs):
        """
        
        CreateProceduralSystemAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetProceduralSystemAttr() , and also Create vs Get Property
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
    def CreateProceduralTypeAttr(*args, **kwargs):
        """
        
        CreateProceduralTypeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetProceduralTypeAttr() , and also Create vs Get Property Methods
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
        
        **classmethod** Get(stage, path) -> GenerativeProceduralAPI
        
        
        Return a UsdHydraGenerativeProceduralAPI holding the prim adhering to
        this schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdHydraGenerativeProceduralAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetProceduralSystemAttr(*args, **kwargs):
        """
        
        GetProceduralSystemAttr() -> Attribute
        
        
        This value should correspond to a configured instance of
        HdGpGenerativeProceduralResolvingSceneIndex which will evaluate the
        procedural.
        
        
        The default value of"hydraGenerativeProcedural"matches the equivalent
        default of HdGpGenerativeProceduralResolvingSceneIndex. Multiple
        instances of the scene index can be used to determine where within a
        scene index chain a given procedural will be evaluated.
        
        Declaration
        
        ``token proceduralSystem ="hydraGenerativeProcedural"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        
        
        """
    @staticmethod
    def GetProceduralTypeAttr(*args, **kwargs):
        """
        
        GetProceduralTypeAttr() -> Attribute
        
        
        The registered name of a HdGpGenerativeProceduralPlugin to be
        executed.
        
        
        
        Declaration
        
        ``token primvars:hdGp:proceduralType``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        
        
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
        
        
        Construct a UsdHydraGenerativeProceduralAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdHydraGenerativeProceduralAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdHydraGenerativeProceduralAPI on the prim held by
        ``schemaObj`` .
        
        
        Should be preferred over UsdHydraGenerativeProceduralAPI
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
class Tokens(Boost.Python.instance):
    HwPrimvar_1: typing.ClassVar[str] = 'HwPrimvar_1'
    HwPtexTexture_1: typing.ClassVar[str] = 'HwPtexTexture_1'
    HwUvTexture_1: typing.ClassVar[str] = 'HwUvTexture_1'
    black: typing.ClassVar[str] = 'black'
    clamp: typing.ClassVar[str] = 'clamp'
    displayLookBxdf: typing.ClassVar[str] = 'displayLook:bxdf'
    faceIndex: typing.ClassVar[str] = 'faceIndex'
    faceOffset: typing.ClassVar[str] = 'faceOffset'
    frame: typing.ClassVar[str] = 'frame'
    hydraGenerativeProcedural: typing.ClassVar[str] = 'hydraGenerativeProcedural'
    infoFilename: typing.ClassVar[str] = 'inputs:file'
    infoVarname: typing.ClassVar[str] = 'inputs:varname'
    linear: typing.ClassVar[str] = 'linear'
    linearMipmapLinear: typing.ClassVar[str] = 'linearMipmapLinear'
    linearMipmapNearest: typing.ClassVar[str] = 'linearMipmapNearest'
    magFilter: typing.ClassVar[str] = 'magFilter'
    minFilter: typing.ClassVar[str] = 'minFilter'
    mirror: typing.ClassVar[str] = 'mirror'
    nearest: typing.ClassVar[str] = 'nearest'
    nearestMipmapLinear: typing.ClassVar[str] = 'nearestMipmapLinear'
    nearestMipmapNearest: typing.ClassVar[str] = 'nearestMipmapNearest'
    primvarsHdGpProceduralType: typing.ClassVar[str] = 'primvars:hdGp:proceduralType'
    proceduralSystem: typing.ClassVar[str] = 'proceduralSystem'
    repeat: typing.ClassVar[str] = 'repeat'
    textureMemory: typing.ClassVar[str] = 'textureMemory'
    useMetadata: typing.ClassVar[str] = 'useMetadata'
    uv: typing.ClassVar[str] = 'uv'
    wrapS: typing.ClassVar[str] = 'wrapS'
    wrapT: typing.ClassVar[str] = 'wrapT'
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
__MFB_FULL_PACKAGE_NAME: str = 'usdHydra'
