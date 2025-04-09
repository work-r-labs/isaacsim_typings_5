from __future__ import annotations
import pxr.UsdGeom
import typing
__all__ = ['GenerativeProcedural', 'Tokens']
class GenerativeProcedural(pxr.UsdGeom.Boundable):
    """
    
    Represents an abstract generative procedural prim which delivers its
    input parameters via properties (including relationships) within
    the"primvars:"namespace.
    
    It does not itself have any awareness or participation in the
    execution of the procedural but rather serves as a means of delivering
    a procedural's definition and input parameters.
    
    The value of its"proceduralSystem"property (either authored or
    provided by API schema fallback) indicates to which system the
    procedural definition is meaningful.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdProcTokens. So to set an attribute to the value"rightHanded",
    use UsdProcTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
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
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> GenerativeProcedural
        
        
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
        
        **classmethod** Get(stage, path) -> GenerativeProcedural
        
        
        Return a UsdProcGenerativeProcedural holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdProcGenerativeProcedural(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetProceduralSystemAttr(*args, **kwargs):
        """
        
        GetProceduralSystemAttr() -> Attribute
        
        
        The name or convention of the system responsible for evaluating the
        procedural.
        
        
        NOTE: A fallback value for this is typically set via an API schema.
        
        Declaration
        
        ``token proceduralSystem``
        
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
        
        
        Construct a UsdProcGenerativeProcedural on UsdPrim ``prim`` .
        
        
        Equivalent to UsdProcGenerativeProcedural::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdProcGenerativeProcedural on the prim held by
        ``schemaObj`` .
        
        
        Should be preferred over UsdProcGenerativeProcedural
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
    proceduralSystem: typing.ClassVar[str] = 'proceduralSystem'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'usdProc'
