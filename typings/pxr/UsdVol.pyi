from __future__ import annotations
import pxr.UsdGeom
import typing
__all__ = ['Field3DAsset', 'FieldAsset', 'FieldBase', 'OpenVDBAsset', 'Tokens', 'Volume']
class Field3DAsset(FieldAsset):
    """
    
    Field3D field primitive. The FieldAsset filePath attribute must
    specify a file in the Field3D format on disk.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdVolTokens. So to set an attribute to the value"rightHanded", use
    UsdVolTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateFieldDataTypeAttr(*args, **kwargs):
        """
        
        CreateFieldDataTypeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetFieldDataTypeAttr() , and also Create vs Get Property Methods
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
    def CreateFieldPurposeAttr(*args, **kwargs):
        """
        
        CreateFieldPurposeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetFieldPurposeAttr() , and also Create vs Get Property Methods
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
        
        **classmethod** Define(stage, path) -> Field3DAsset
        
        
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
        
        **classmethod** Get(stage, path) -> Field3DAsset
        
        
        Return a UsdVolField3DAsset holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdVolField3DAsset(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetFieldDataTypeAttr(*args, **kwargs):
        """
        
        GetFieldDataTypeAttr() -> Attribute
        
        
        Token which is used to indicate the data type of an individual field.
        
        
        Authors use this to tell consumers more about the field without
        opening the file on disk. The list of allowed tokens reflects the
        available choices for Field3d volumes.
        
        Declaration
        
        ``token fieldDataType``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Allowed Values
        
        half, float, double, half3, float3, double3
        
        
        
        """
    @staticmethod
    def GetFieldPurposeAttr(*args, **kwargs):
        """
        
        GetFieldPurposeAttr() -> Attribute
        
        
        Optional token which can be used to indicate the purpose or grouping
        of an individual field.
        
        
        Clients which consume Field3D files should treat this as the Field3D
        field *name*.
        
        Declaration
        
        ``token fieldPurpose``
        
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
        
        
        Construct a UsdVolField3DAsset on UsdPrim ``prim`` .
        
        
        Equivalent to UsdVolField3DAsset::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdVolField3DAsset on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdVolField3DAsset (schemaObj.GetPrim()), as
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
class FieldAsset(FieldBase):
    """
    
    Base class for field primitives defined by an external file.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdVolTokens. So to set an attribute to the value"rightHanded", use
    UsdVolTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateFieldDataTypeAttr(*args, **kwargs):
        """
        
        CreateFieldDataTypeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetFieldDataTypeAttr() , and also Create vs Get Property Methods
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
    def CreateFieldIndexAttr(*args, **kwargs):
        """
        
        CreateFieldIndexAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetFieldIndexAttr() , and also Create vs Get Property Methods for
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
    def CreateFieldNameAttr(*args, **kwargs):
        """
        
        CreateFieldNameAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetFieldNameAttr() , and also Create vs Get Property Methods for
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
    def CreateFilePathAttr(*args, **kwargs):
        """
        
        CreateFilePathAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetFilePathAttr() , and also Create vs Get Property Methods for
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
    def CreateVectorDataRoleHintAttr(*args, **kwargs):
        """
        
        CreateVectorDataRoleHintAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetVectorDataRoleHintAttr() , and also Create vs Get Property
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
        
        **classmethod** Get(stage, path) -> FieldAsset
        
        
        Return a UsdVolFieldAsset holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdVolFieldAsset(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetFieldDataTypeAttr(*args, **kwargs):
        """
        
        GetFieldDataTypeAttr() -> Attribute
        
        
        Token which is used to indicate the data type of an individual field.
        
        
        Authors use this to tell consumers more about the field without
        opening the file on disk. The list of allowed tokens is specified with
        the specific asset type. A missing value is considered an error.
        
        Declaration
        
        ``token fieldDataType``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        
        
        """
    @staticmethod
    def GetFieldIndexAttr(*args, **kwargs):
        """
        
        GetFieldIndexAttr() -> Attribute
        
        
        A file can contain multiple fields with the same name.
        
        
        This optional attribute is an index used to disambiguate between these
        multiple fields with the same name.
        
        Declaration
        
        ``int fieldIndex``
        
        C++ Type
        
        int
        
        Usd Type
        
        SdfValueTypeNames->Int
        
        
        
        """
    @staticmethod
    def GetFieldNameAttr(*args, **kwargs):
        """
        
        GetFieldNameAttr() -> Attribute
        
        
        Name of an individual field within the file specified by the filePath
        attribute.
        
        
        
        Declaration
        
        ``token fieldName``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        
        
        """
    @staticmethod
    def GetFilePathAttr(*args, **kwargs):
        """
        
        GetFilePathAttr() -> Attribute
        
        
        An asset path attribute that points to a file on disk.
        
        
        For each supported file format, a separate FieldAsset subclass is
        required.
        
        This attribute's value can be animated over time, as most volume asset
        formats represent just a single timeSample of a volume. However, it
        does not, at this time, support any pattern substitutions like"$F".
        
        Declaration
        
        ``asset filePath``
        
        C++ Type
        
        SdfAssetPath
        
        Usd Type
        
        SdfValueTypeNames->Asset
        
        
        
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
    def GetVectorDataRoleHintAttr(*args, **kwargs):
        """
        
        GetVectorDataRoleHintAttr() -> Attribute
        
        
        Optional token which is used to indicate the role of a vector valued
        field.
        
        
        This can drive the data type in which fields are made available in a
        renderer or whether the vector values are to be transformed.
        
        Declaration
        
        ``token vectorDataRoleHint ="None"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Allowed Values
        
        None, Point, Normal, Vector, Color
        
        
        
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
        
        
        Construct a UsdVolFieldAsset on UsdPrim ``prim`` .
        
        
        Equivalent to UsdVolFieldAsset::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdVolFieldAsset on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdVolFieldAsset (schemaObj.GetPrim()), as it
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
class FieldBase(pxr.UsdGeom.Xformable):
    """
    
    Base class for field primitives.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> FieldBase
        
        
        Return a UsdVolFieldBase holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdVolFieldBase(stage->GetPrimAtPath(path));
        
        
        
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
        
        
        Construct a UsdVolFieldBase on UsdPrim ``prim`` .
        
        
        Equivalent to UsdVolFieldBase::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdVolFieldBase on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdVolFieldBase (schemaObj.GetPrim()), as it
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
class OpenVDBAsset(FieldAsset):
    """
    
    OpenVDB field primitive. The FieldAsset filePath attribute must
    specify a file in the OpenVDB format on disk.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdVolTokens. So to set an attribute to the value"rightHanded", use
    UsdVolTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateFieldClassAttr(*args, **kwargs):
        """
        
        CreateFieldClassAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetFieldClassAttr() , and also Create vs Get Property Methods for
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
    def CreateFieldDataTypeAttr(*args, **kwargs):
        """
        
        CreateFieldDataTypeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetFieldDataTypeAttr() , and also Create vs Get Property Methods
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
        
        **classmethod** Define(stage, path) -> OpenVDBAsset
        
        
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
        
        **classmethod** Get(stage, path) -> OpenVDBAsset
        
        
        Return a UsdVolOpenVDBAsset holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdVolOpenVDBAsset(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetFieldClassAttr(*args, **kwargs):
        """
        
        GetFieldClassAttr() -> Attribute
        
        
        Optional token which can be used to indicate the class of an
        individual grid.
        
        
        This is a mapping to openvdb::GridClass where the values are
        GRID_LEVEL_SET, GRID_FOG_VOLUME, GRID_STAGGERED, and GRID_UNKNOWN.
        
        Declaration
        
        ``token fieldClass``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Allowed Values
        
        levelSet, fogVolume, staggered, unknown
        
        
        
        """
    @staticmethod
    def GetFieldDataTypeAttr(*args, **kwargs):
        """
        
        GetFieldDataTypeAttr() -> Attribute
        
        
        Token which is used to indicate the data type of an individual field.
        
        
        Authors use this to tell consumers more about the field without
        opening the file on disk. The list of allowed tokens reflects the
        available choices for OpenVDB volumes.
        
        Declaration
        
        ``token fieldDataType``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Allowed Values
        
        half, float, double, int, uint, int64, half2, float2, double2, int2,
        half3, float3, double3, int3, matrix3d, matrix4d, quatd, bool, mask,
        string
        
        
        
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
        
        
        Construct a UsdVolOpenVDBAsset on UsdPrim ``prim`` .
        
        
        Equivalent to UsdVolOpenVDBAsset::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdVolOpenVDBAsset on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdVolOpenVDBAsset (schemaObj.GetPrim()), as
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
class Tokens(Boost.Python.instance):
    bool_: typing.ClassVar[str] = 'bool'
    color: typing.ClassVar[str] = 'Color'
    double2: typing.ClassVar[str] = 'double2'
    double3: typing.ClassVar[str] = 'double3'
    double_: typing.ClassVar[str] = 'double'
    field: typing.ClassVar[str] = 'field'
    fieldClass: typing.ClassVar[str] = 'fieldClass'
    fieldDataType: typing.ClassVar[str] = 'fieldDataType'
    fieldIndex: typing.ClassVar[str] = 'fieldIndex'
    fieldName: typing.ClassVar[str] = 'fieldName'
    fieldPurpose: typing.ClassVar[str] = 'fieldPurpose'
    filePath: typing.ClassVar[str] = 'filePath'
    float2: typing.ClassVar[str] = 'float2'
    float3: typing.ClassVar[str] = 'float3'
    float_: typing.ClassVar[str] = 'float'
    fogVolume: typing.ClassVar[str] = 'fogVolume'
    half: typing.ClassVar[str] = 'half'
    half2: typing.ClassVar[str] = 'half2'
    half3: typing.ClassVar[str] = 'half3'
    int2: typing.ClassVar[str] = 'int2'
    int3: typing.ClassVar[str] = 'int3'
    int64: typing.ClassVar[str] = 'int64'
    int_: typing.ClassVar[str] = 'int'
    levelSet: typing.ClassVar[str] = 'levelSet'
    mask: typing.ClassVar[str] = 'mask'
    matrix3d: typing.ClassVar[str] = 'matrix3d'
    matrix4d: typing.ClassVar[str] = 'matrix4d'
    none_: typing.ClassVar[str] = 'None'
    normal: typing.ClassVar[str] = 'Normal'
    point: typing.ClassVar[str] = 'Point'
    quatd: typing.ClassVar[str] = 'quatd'
    staggered: typing.ClassVar[str] = 'staggered'
    string: typing.ClassVar[str] = 'string'
    uint: typing.ClassVar[str] = 'uint'
    unknown: typing.ClassVar[str] = 'unknown'
    vector: typing.ClassVar[str] = 'Vector'
    vectorDataRoleHint: typing.ClassVar[str] = 'vectorDataRoleHint'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Volume(pxr.UsdGeom.Gprim):
    """
    
    A renderable volume primitive. A volume is made up of any number of
    FieldBase primitives bound together in this volume. Each FieldBase
    primitive is specified as a relationship with a namespace prefix
    of"field".
    
    The relationship name is used by the renderer to associate individual
    fields with the named input parameters on the volume shader. Using
    this indirect approach to connecting fields to shader parameters
    (rather than using the field prim's name) allows a single field to be
    reused for different shader inputs, or to be used as different shader
    parameters when rendering different Volumes. This means that the name
    of the field prim is not relevant to its contribution to the volume
    prims which refer to it. Nor does the field prim's location in the
    scene graph have any relevance, and Volumes may refer to fields
    anywhere in the scene graph. **However**, unless Field prims need to
    be shared by multiple Volumes, a Volume's Field prims should be
    located under the Volume in namespace, for enhanced organization.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def BlockFieldRelationship(*args, **kwargs):
        """
        
        BlockFieldRelationship(name) -> bool
        
        
        Blocks an existing field relationship on this volume, ensuring it will
        not be enumerated by GetFieldPaths() .
        
        
        Returns true if the relationship existed, false if it did not. In
        other words the return value indicates whether the volume prim was
        changed.
        
        The name lookup automatically applies the field relationship
        namespacing, if it isn't specified in the name token.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def CreateFieldRelationship(*args, **kwargs):
        """
        
        CreateFieldRelationship(name, fieldPath) -> bool
        
        
        Creates a relationship on this volume that targets the specified
        field.
        
        
        If an existing relationship exists with the same name, it is replaced
        (since only one target is allowed for each named relationship).
        
        Returns ``true`` if the relationship was successfully created and set
        \\- it is legal to call this method for a field relationship that
        already"exists", i.e. already posesses scene description, as this is
        the only method we provide for setting a field relatioonship's value,
        to help enforce that field relationships can have only a single (or
        no) target.
        
        fieldPath
        
        \\- can be a prim path, or the path of another relationship, to effect
        Relationship Forwarding The name lookup automatically applies the
        field relationship namespacing, if it isn't specified in the name
        token.
        
        
        Parameters
        ----------
        name : str
        
        fieldPath : Path
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Volume
        
        
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
        
        **classmethod** Get(stage, path) -> Volume
        
        
        Return a UsdVolVolume holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdVolVolume(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetFieldPath(*args, **kwargs):
        """
        
        GetFieldPath(name) -> Path
        
        
        Checks if there is an existing field relationship with a given name,
        and if so, returns the path to the Field prim it targets, or else the
        empty path.
        
        
        The name lookup automatically applies the field relationship
        namespacing, if it isn't specified in the name token.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetFieldPaths(*args, **kwargs):
        """
        
        GetFieldPaths() -> FieldMap
        
        
        Return a map of field relationship names to the fields themselves,
        represented as prim paths.
        
        
        This map provides all the information that should be needed to tie
        fields to shader parameters and render this volume.
        
        The field relationship names that server as the map keys will have the
        field namespace stripped from them.
        
        
        
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
    def HasFieldRelationship(*args, **kwargs):
        """
        
        HasFieldRelationship(name) -> bool
        
        
        Checks if there is an existing field relationship with a given name.
        
        
        This query will return ``true`` even for a field relationship that has
        been blocked and therefore will not contribute to the map returned by
        GetFieldRelationships()
        
        The name lookup automatically applies the field relationship
        namespacing, if it isn't specified in the name token.
        
        
        Parameters
        ----------
        name : str
        
        
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
        
        
        Construct a UsdVolVolume on UsdPrim ``prim`` .
        
        
        Equivalent to UsdVolVolume::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* ``prim`` , but will not immediately throw an error for an
        invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdVolVolume on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdVolVolume (schemaObj.GetPrim()), as it
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
__MFB_FULL_PACKAGE_NAME: str = 'usdVol'
