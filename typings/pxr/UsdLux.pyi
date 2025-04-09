from __future__ import annotations
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
import typing
__all__ = ['BoundableLightBase', 'CylinderLight', 'DiskLight', 'DistantLight', 'DomeLight', 'GeometryLight', 'LightAPI', 'LightFilter', 'LightListAPI', 'ListAPI', 'MeshLightAPI', 'NonboundableLightBase', 'PluginLight', 'PluginLightFilter', 'PortalLight', 'RectLight', 'ShadowAPI', 'ShapingAPI', 'SphereLight', 'Tokens', 'VolumeLightAPI']
class BoundableLightBase(pxr.UsdGeom.Boundable):
    """
    
    Base class for intrinsic lights that are boundable.
    
    The primary purpose of this class is to provide a direct API to the
    functions provided by LightAPI for concrete derived light types.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateColorAttr(*args, **kwargs):
        """
        
        CreateColorAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateColorAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateColorTemperatureAttr(*args, **kwargs):
        """
        
        CreateColorTemperatureAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateColorTemperatureAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateDiffuseAttr(*args, **kwargs):
        """
        
        CreateDiffuseAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateDiffuseAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateEnableColorTemperatureAttr(*args, **kwargs):
        """
        
        CreateEnableColorTemperatureAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateEnableColorTemperatureAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateExposureAttr(*args, **kwargs):
        """
        
        CreateExposureAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateExposureAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateFiltersRel(*args, **kwargs):
        """
        
        CreateFiltersRel() -> Relationship
        
        
        See UsdLuxLightAPI::CreateFiltersRel() .
        
        
        
        """
    @staticmethod
    def CreateIntensityAttr(*args, **kwargs):
        """
        
        CreateIntensityAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateIntensityAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateNormalizeAttr(*args, **kwargs):
        """
        
        CreateNormalizeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateNormalizeAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateSpecularAttr(*args, **kwargs):
        """
        
        CreateSpecularAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateSpecularAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> BoundableLightBase
        
        
        Return a UsdLuxBoundableLightBase holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxBoundableLightBase(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetColorAttr(*args, **kwargs):
        """
        
        GetColorAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetColorAttr() .
        
        
        
        """
    @staticmethod
    def GetColorTemperatureAttr(*args, **kwargs):
        """
        
        GetColorTemperatureAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetColorTemperatureAttr() .
        
        
        
        """
    @staticmethod
    def GetDiffuseAttr(*args, **kwargs):
        """
        
        GetDiffuseAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetDiffuseAttr() .
        
        
        
        """
    @staticmethod
    def GetEnableColorTemperatureAttr(*args, **kwargs):
        """
        
        GetEnableColorTemperatureAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetEnableColorTemperatureAttr() .
        
        
        
        """
    @staticmethod
    def GetExposureAttr(*args, **kwargs):
        """
        
        GetExposureAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetExposureAttr() .
        
        
        
        """
    @staticmethod
    def GetFiltersRel(*args, **kwargs):
        """
        
        GetFiltersRel() -> Relationship
        
        
        See UsdLuxLightAPI::GetFiltersRel() .
        
        
        
        """
    @staticmethod
    def GetIntensityAttr(*args, **kwargs):
        """
        
        GetIntensityAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetIntensityAttr() .
        
        
        
        """
    @staticmethod
    def GetNormalizeAttr(*args, **kwargs):
        """
        
        GetNormalizeAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetNormalizeAttr() .
        
        
        
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
    def GetSpecularAttr(*args, **kwargs):
        """
        
        GetSpecularAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetSpecularAttr() .
        
        
        
        """
    @staticmethod
    def LightAPI(*args, **kwargs):
        """
        
        LightAPI() -> LightAPI
        
        
        Contructs and returns a UsdLuxLightAPI object for this light.
        
        
        
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
        
        
        Construct a UsdLuxBoundableLightBase on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxBoundableLightBase::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxBoundableLightBase on the prim held by ``schemaObj``
        .
        
        
        Should be preferred over UsdLuxBoundableLightBase
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
class CylinderLight(BoundableLightBase):
    """
    
    Light emitted outward from a cylinder. The cylinder is centered at the
    origin and has its major axis on the X axis. The cylinder does not
    emit light from the flat end-caps.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateLengthAttr(*args, **kwargs):
        """
        
        CreateLengthAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetLengthAttr() , and also Create vs Get Property Methods for when
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
    def CreateRadiusAttr(*args, **kwargs):
        """
        
        CreateRadiusAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetRadiusAttr() , and also Create vs Get Property Methods for when
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
    def CreateTreatAsLineAttr(*args, **kwargs):
        """
        
        CreateTreatAsLineAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetTreatAsLineAttr() , and also Create vs Get Property Methods for
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
        
        **classmethod** Define(stage, path) -> CylinderLight
        
        
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
        
        **classmethod** Get(stage, path) -> CylinderLight
        
        
        Return a UsdLuxCylinderLight holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxCylinderLight(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetLengthAttr(*args, **kwargs):
        """
        
        GetLengthAttr() -> Attribute
        
        
        Width of the rectangle, in the local X axis.
        
        
        
        Declaration
        
        ``float inputs:length = 1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
        """
        
        GetRadiusAttr() -> Attribute
        
        
        Radius of the cylinder.
        
        
        
        Declaration
        
        ``float inputs:radius = 0.5``
        
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
    def GetTreatAsLineAttr(*args, **kwargs):
        """
        
        GetTreatAsLineAttr() -> Attribute
        
        
        A hint that this light can be treated as a'line'light (effectively, a
        zero-radius cylinder) by renderers that benefit from non-area
        lighting.
        
        
        Renderers that only support area lights can disregard this.
        
        Declaration
        
        ``bool treatAsLine = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
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
        
        
        Construct a UsdLuxCylinderLight on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxCylinderLight::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxCylinderLight on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxCylinderLight (schemaObj.GetPrim()), as
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
class DiskLight(BoundableLightBase):
    """
    
    Light emitted from one side of a circular disk. The disk is centered
    in the XY plane and emits light along the -Z axis.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateRadiusAttr(*args, **kwargs):
        """
        
        CreateRadiusAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetRadiusAttr() , and also Create vs Get Property Methods for when
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
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> DiskLight
        
        
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
        
        **classmethod** Get(stage, path) -> DiskLight
        
        
        Return a UsdLuxDiskLight holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxDiskLight(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
        """
        
        GetRadiusAttr() -> Attribute
        
        
        Radius of the disk.
        
        
        
        Declaration
        
        ``float inputs:radius = 0.5``
        
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
        
        
        Construct a UsdLuxDiskLight on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxDiskLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxDiskLight on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxDiskLight (schemaObj.GetPrim()), as it
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
class DistantLight(NonboundableLightBase):
    """
    
    Light emitted from a distant source along the -Z axis. Also known as a
    directional light.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateAngleAttr(*args, **kwargs):
        """
        
        CreateAngleAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetAngleAttr() , and also Create vs Get Property Methods for when
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
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> DistantLight
        
        
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
        
        **classmethod** Get(stage, path) -> DistantLight
        
        
        Return a UsdLuxDistantLight holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxDistantLight(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetAngleAttr(*args, **kwargs):
        """
        
        GetAngleAttr() -> Attribute
        
        
        Angular size of the light in degrees.
        
        
        As an example, the Sun is approximately 0.53 degrees as seen from
        Earth. Higher values broaden the light and therefore soften shadow
        edges.
        
        Declaration
        
        ``float inputs:angle = 0.53``
        
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
        
        
        Construct a UsdLuxDistantLight on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxDistantLight::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxDistantLight on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxDistantLight (schemaObj.GetPrim()), as
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
class DomeLight(NonboundableLightBase):
    """
    
    Light emitted inward from a distant external environment, such as a
    sky or IBL light probe. The orientation of a dome light with a latlong
    texture is expected to match the OpenEXR specification for latlong
    environment maps. From the OpenEXR documentation:
    
    Latitude-Longitude Map:
    
    The environment is projected onto the image using polar coordinates
    (latitude and longitude). A pixel's x coordinate corresponds to its
    longitude, and the y coordinate corresponds to its latitude. Pixel
    (dataWindow.min.x, dataWindow.min.y) has latitude +pi/2 and longitude
    +pi; pixel (dataWindow.max.x, dataWindow.max.y) has latitude -pi/2 and
    longitude -pi.
    
    In 3D space, latitudes -pi/2 and +pi/2 correspond to the negative and
    positive y direction. Latitude 0, longitude 0 points into positive z
    direction; and latitude 0, longitude pi/2 points into positive x
    direction.
    
    The size of the data window should be 2\\*N by N pixels (width by
    height),
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdLuxTokens. So to set an attribute to the value"rightHanded", use
    UsdLuxTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateGuideRadiusAttr(*args, **kwargs):
        """
        
        CreateGuideRadiusAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetGuideRadiusAttr() , and also Create vs Get Property Methods for
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
    def CreatePortalsRel(*args, **kwargs):
        """
        
        CreatePortalsRel() -> Relationship
        
        
        See GetPortalsRel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateTextureFileAttr(*args, **kwargs):
        """
        
        CreateTextureFileAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetTextureFileAttr() , and also Create vs Get Property Methods for
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
    def CreateTextureFormatAttr(*args, **kwargs):
        """
        
        CreateTextureFormatAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetTextureFormatAttr() , and also Create vs Get Property Methods
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
        
        **classmethod** Define(stage, path) -> DomeLight
        
        
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
        
        **classmethod** Get(stage, path) -> DomeLight
        
        
        Return a UsdLuxDomeLight holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxDomeLight(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetGuideRadiusAttr(*args, **kwargs):
        """
        
        GetGuideRadiusAttr() -> Attribute
        
        
        The radius of guide geometry to use to visualize the dome light.
        
        
        The default is 1 km for scenes whose metersPerUnit is the USD default
        of 0.01 (i.e., 1 world unit is 1 cm).
        
        Declaration
        
        ``float guideRadius = 100000``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetPortalsRel(*args, **kwargs):
        """
        
        GetPortalsRel() -> Relationship
        
        
        Optional portals to guide light sampling.
        
        
        
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
    def GetTextureFileAttr(*args, **kwargs):
        """
        
        GetTextureFileAttr() -> Attribute
        
        
        A color texture to use on the dome, such as an HDR (high dynamic
        range) texture intended for IBL (image based lighting).
        
        
        
        Declaration
        
        ``asset inputs:texture:file``
        
        C++ Type
        
        SdfAssetPath
        
        Usd Type
        
        SdfValueTypeNames->Asset
        
        
        
        """
    @staticmethod
    def GetTextureFormatAttr(*args, **kwargs):
        """
        
        GetTextureFormatAttr() -> Attribute
        
        
        Specifies the parameterization of the color map file.
        
        
        Valid values are:
        
           - automatic: Tries to determine the layout from the file itself.
             For example, Renderman texture files embed an explicit
             parameterization.
        
           - latlong: Latitude as X, longitude as Y.
        
           - mirroredBall: An image of the environment reflected in a sphere,
             using an implicitly orthogonal projection.
        
           - angular: Similar to mirroredBall but the radial dimension is
             mapped linearly to the angle, providing better sampling at the edges.
        
           - cubeMapVerticalCross: A cube map with faces laid out as a
             vertical cross.
        
        Declaration
        
        ``token inputs:texture:format ="automatic"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Allowed Values
        
        automatic, latlong, mirroredBall, angular, cubeMapVerticalCross
        
        
        
        """
    @staticmethod
    def OrientToStageUpAxis(*args, **kwargs):
        """
        
        OrientToStageUpAxis() -> None
        
        
        Adds a transformation op, if neeeded, to orient the dome to align with
        the stage's up axis.
        
        
        Uses UsdLuxTokens->orientToStageUpAxis as the op suffix. If an op with
        this suffix already exists, this method assumes it is already applying
        the proper correction and does nothing further. If no op is required
        to match the stage's up axis, no op will be created.
        
        UsdGeomXformOp
        
        UsdGeomGetStageUpAxis
        
        
        
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
        
        
        Construct a UsdLuxDomeLight on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxDomeLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxDomeLight on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxDomeLight (schemaObj.GetPrim()), as it
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
class GeometryLight(NonboundableLightBase):
    """
    
    Deprecated
    
    Light emitted outward from a geometric prim (UsdGeomGprim), which is
    typically a mesh.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateGeometryRel(*args, **kwargs):
        """
        
        CreateGeometryRel() -> Relationship
        
        
        See GetGeometryRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> GeometryLight
        
        
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
        
        **classmethod** Get(stage, path) -> GeometryLight
        
        
        Return a UsdLuxGeometryLight holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxGeometryLight(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetGeometryRel(*args, **kwargs):
        """
        
        GetGeometryRel() -> Relationship
        
        
        Relationship to the geometry to use as the light source.
        
        
        
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
        
        
        Construct a UsdLuxGeometryLight on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxGeometryLight::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxGeometryLight on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxGeometryLight (schemaObj.GetPrim()), as
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
class LightAPI(pxr.Usd.APISchemaBase):
    """
    
    API schema that imparts the quality of being a light onto a prim.
    
    A light is any prim that has this schema applied to it. This is true
    regardless of whether LightAPI is included as a built-in API of the
    prim type (e.g. RectLight or DistantLight) or is applied directly to a
    Gprim that should be treated as a light.
    
    **Linking**
    
    Lights can be linked to geometry. Linking controls which geometry a
    light illuminates, and which geometry casts shadows from the light.
    
    Linking is specified as collections (UsdCollectionAPI) which can be
    accessed via GetLightLinkCollection() and GetShadowLinkCollection().
    Note that these collections have their includeRoot set to true, so
    that lights will illuminate and cast shadows from all objects by
    default. To illuminate only a specific set of objects, there are two
    options. One option is to modify the collection paths to explicitly
    exclude everything else, assuming it is known; the other option is to
    set includeRoot to false and explicitly include the desired objects.
    These are complementary approaches that may each be preferable
    depending on the scenario and how to best express the intent of the
    light setup.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdLuxTokens. So to set an attribute to the value"rightHanded", use
    UsdLuxTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> LightAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"LightAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.
        
        A valid UsdLuxLightAPI object is returned upon success. An invalid (or
        empty) UsdLuxLightAPI object is returned upon failure. See
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
    def ConnectableAPI(*args, **kwargs):
        """
        
        ConnectableAPI() -> ConnectableAPI
        
        
        Contructs and returns a UsdShadeConnectableAPI object with this light.
        
        
        Note that most tasks can be accomplished without explicitly
        constructing a UsdShadeConnectable API, since connection-related API
        such as UsdShadeConnectableAPI::ConnectToSource() are static methods,
        and UsdLuxLightAPI will auto-convert to a UsdShadeConnectableAPI when
        passed to functions that want to act generically on a connectable
        UsdShadeConnectableAPI object.
        
        
        
        """
    @staticmethod
    def CreateColorAttr(*args, **kwargs):
        """
        
        CreateColorAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetColorAttr() , and also Create vs Get Property Methods for when
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
    def CreateColorTemperatureAttr(*args, **kwargs):
        """
        
        CreateColorTemperatureAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetColorTemperatureAttr() , and also Create vs Get Property
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
    def CreateDiffuseAttr(*args, **kwargs):
        """
        
        CreateDiffuseAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDiffuseAttr() , and also Create vs Get Property Methods for
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
    def CreateEnableColorTemperatureAttr(*args, **kwargs):
        """
        
        CreateEnableColorTemperatureAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetEnableColorTemperatureAttr() , and also Create vs Get Property
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
    def CreateExposureAttr(*args, **kwargs):
        """
        
        CreateExposureAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetExposureAttr() , and also Create vs Get Property Methods for
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
    def CreateFiltersRel(*args, **kwargs):
        """
        
        CreateFiltersRel() -> Relationship
        
        
        See GetFiltersRel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateInput(*args, **kwargs):
        """
        
        CreateInput(name, typeName) -> Input
        
        
        Create an input which can either have a value or can be connected.
        
        
        The attribute representing the input is created in
        the"inputs:"namespace. Inputs on lights are connectable.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def CreateIntensityAttr(*args, **kwargs):
        """
        
        CreateIntensityAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetIntensityAttr() , and also Create vs Get Property Methods for
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
    def CreateMaterialSyncModeAttr(*args, **kwargs):
        """
        
        CreateMaterialSyncModeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetMaterialSyncModeAttr() , and also Create vs Get Property
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
    def CreateNormalizeAttr(*args, **kwargs):
        """
        
        CreateNormalizeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetNormalizeAttr() , and also Create vs Get Property Methods for
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
    def CreateOutput(*args, **kwargs):
        """
        
        CreateOutput(name, typeName) -> Output
        
        
        Create an output which can either have a value or can be connected.
        
        
        The attribute representing the output is created in
        the"outputs:"namespace. Outputs on a light cannot be connected, as
        their value is assumed to be computed externally.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def CreateShaderIdAttr(*args, **kwargs):
        """
        
        CreateShaderIdAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShaderIdAttr() , and also Create vs Get Property Methods for
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
    def CreateShaderIdAttrForRenderContext(*args, **kwargs):
        """
        
        CreateShaderIdAttrForRenderContext(renderContext, defaultValue, writeSparsely) -> Attribute
        
        
        Creates the shader ID attribute for the given ``renderContext`` .
        
        
        See GetShaderIdAttrForRenderContext() , and also Create vs Get
        Property Methods for when to use Get vs Create. If specified, author
        ``defaultValue`` as the attribute's default, sparsely (when it makes
        sense to do so) if ``writeSparsely`` is ``true`` - the default for
        ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        renderContext : str
        
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateSpecularAttr(*args, **kwargs):
        """
        
        CreateSpecularAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetSpecularAttr() , and also Create vs Get Property Methods for
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
        
        **classmethod** Get(stage, path) -> LightAPI
        
        
        Return a UsdLuxLightAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxLightAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetColorAttr(*args, **kwargs):
        """
        
        GetColorAttr() -> Attribute
        
        
        The color of emitted light, in energy-linear terms.
        
        
        
        Declaration
        
        ``color3f inputs:color = (1, 1, 1)``
        
        C++ Type
        
        GfVec3f
        
        Usd Type
        
        SdfValueTypeNames->Color3f
        
        
        
        """
    @staticmethod
    def GetColorTemperatureAttr(*args, **kwargs):
        """
        
        GetColorTemperatureAttr() -> Attribute
        
        
        Color temperature, in degrees Kelvin, representing the white point.
        
        
        The default is a common white point, D65. Lower values are warmer and
        higher values are cooler. The valid range is from 1000 to 10000. Only
        takes effect when enableColorTemperature is set to true. When active,
        the computed result multiplies against the color attribute. See
        UsdLuxBlackbodyTemperatureAsRgb() .
        
        Declaration
        
        ``float inputs:colorTemperature = 6500``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetDiffuseAttr(*args, **kwargs):
        """
        
        GetDiffuseAttr() -> Attribute
        
        
        A multiplier for the effect of this light on the diffuse response of
        materials.
        
        
        This is a non-physical control.
        
        Declaration
        
        ``float inputs:diffuse = 1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetEnableColorTemperatureAttr(*args, **kwargs):
        """
        
        GetEnableColorTemperatureAttr() -> Attribute
        
        
        Enables using colorTemperature.
        
        
        
        Declaration
        
        ``bool inputs:enableColorTemperature = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
        """
    @staticmethod
    def GetExposureAttr(*args, **kwargs):
        """
        
        GetExposureAttr() -> Attribute
        
        
        Scales the power of the light exponentially as a power of 2 (similar
        to an F-stop control over exposure).
        
        
        The result is multiplied against the intensity.
        
        Declaration
        
        ``float inputs:exposure = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetFiltersRel(*args, **kwargs):
        """
        
        GetFiltersRel() -> Relationship
        
        
        Relationship to the light filters that apply to this light.
        
        
        
        """
    @staticmethod
    def GetInput(*args, **kwargs):
        """
        
        GetInput(name) -> Input
        
        
        Return the requested input if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetInputs(*args, **kwargs):
        """
        
        GetInputs(onlyAuthored) -> list[Input]
        
        
        Inputs are represented by attributes in the"inputs:"namespace.
        
        
        If ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
        """
    @staticmethod
    def GetIntensityAttr(*args, **kwargs):
        """
        
        GetIntensityAttr() -> Attribute
        
        
        Scales the power of the light linearly.
        
        
        
        Declaration
        
        ``float inputs:intensity = 1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetLightLinkCollectionAPI(*args, **kwargs):
        """
        
        GetLightLinkCollectionAPI() -> CollectionAPI
        
        
        Return the UsdCollectionAPI interface used for examining and modifying
        the light-linking of this light.
        
        
        Light-linking controls which geometry this light illuminates.
        
        
        
        """
    @staticmethod
    def GetMaterialSyncModeAttr(*args, **kwargs):
        """
        
        GetMaterialSyncModeAttr() -> Attribute
        
        
        For a LightAPI applied to geometry that has a bound Material, which is
        entirely or partly emissive, this specifies the relationship of the
        Material response to the lighting response.
        
        
        Valid values are:
        
           - materialGlowTintsLight: All primary and secondary rays see the
             emissive/glow response as dictated by the bound Material while the
             base color seen by light rays (which is then modulated by all of the
             other LightAPI controls) is the multiplication of the color feeding
             the emission/glow input of the Material (i.e. its surface or volume
             shader) with the scalar or pattern input to *inputs:color*. This
             allows the light's color to tint the geometry's glow color while
             preserving access to intensity and other light controls as ways to
             further modulate the illumination.
        
           - independent: All primary and secondary rays see the emissive/glow
             response as dictated by the bound Material, while the base color seen
             by light rays is determined solely by *inputs:color*. Note that for
             partially emissive geometry (in which some parts are reflective rather
             than emissive), a suitable pattern must be connected to the light's
             color input, or else the light will radiate uniformly from the
             geometry.
        
           - noMaterialResponse: The geometry behaves as if there is no
             Material bound at all, i.e. there is no diffuse, specular, or
             transmissive response. The base color of light rays is entirely
             controlled by the *inputs:color*. This is the standard mode
             for"canonical"lights in UsdLux and indicates to renderers that a
             Material will either never be bound or can always be ignored.
        
        Declaration
        
        ``uniform token light:materialSyncMode ="noMaterialResponse"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        materialGlowTintsLight, independent, noMaterialResponse
        
        
        
        """
    @staticmethod
    def GetNormalizeAttr(*args, **kwargs):
        """
        
        GetNormalizeAttr() -> Attribute
        
        
        Normalizes power by the surface area of the light.
        
        
        This makes it easier to independently adjust the power and shape of
        the light, by causing the power to not vary with the area or angular
        size of the light.
        
        Declaration
        
        ``bool inputs:normalize = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
        """
    @staticmethod
    def GetOutput(*args, **kwargs):
        """
        
        GetOutput(name) -> Output
        
        
        Return the requested output if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetOutputs(*args, **kwargs):
        """
        
        GetOutputs(onlyAuthored) -> list[Output]
        
        
        Outputs are represented by attributes in the"outputs:"namespace.
        
        
        If ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
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
    def GetShaderId(*args, **kwargs):
        """
        
        GetShaderId(renderContexts) -> str
        
        
        Return the light's shader ID for the given list of available
        ``renderContexts`` .
        
        
        The shader ID returned by this function is the identifier to use when
        looking up the shader definition for this light in the shader
        registry.
        
        The render contexts are expected to be listed in priority order, so
        for each render context provided, this will try to find the shader ID
        attribute specific to that render context (see
        GetShaderIdAttrForRenderContext() ) and will return the value of the
        first one found that has a non-empty value. If no shader ID value can
        be found for any of the given render contexts or ``renderContexts`` is
        empty, then this will return the value of the default shader ID
        attribute (see GetShaderIdAttr() ).
        
        
        Parameters
        ----------
        renderContexts : list[str]
        
        
        """
    @staticmethod
    def GetShaderIdAttr(*args, **kwargs):
        """
        
        GetShaderIdAttr() -> Attribute
        
        
        Default ID for the light's shader.
        
        
        This defines the shader ID for this light when a render context
        specific shader ID is not available.
        
        The default shaderId for the intrinsic UsdLux lights (RectLight,
        DistantLight, etc.) are set to default to the light's type name. For
        each intrinsic UsdLux light, we will always register an SdrShaderNode
        in the SdrRegistry, with the identifier matching the type name and the
        source type"USD", that corresponds to the light's inputs.
        
        GetShaderId
        
        GetShaderIdAttrForRenderContext
        
        SdrRegistry::GetShaderNodeByIdentifier
        
        SdrRegistry::GetShaderNodeByIdentifierAndType
        
        Declaration
        
        ``uniform token light:shaderId =""``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetShaderIdAttrForRenderContext(*args, **kwargs):
        """
        
        GetShaderIdAttrForRenderContext(renderContext) -> Attribute
        
        
        Returns the shader ID attribute for the given ``renderContext`` .
        
        
        If ``renderContext`` is non-empty, this will try to return an
        attribute named *light:shaderId* with the namespace prefix
        ``renderContext`` . For example, if the passed in render context
        is"ri"then the attribute returned by this function would have the
        following signature:
        
        Declaration
        
        ``token ri:light:shaderId``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        If the render context is empty, this will return the default shader ID
        attribute as returned by GetShaderIdAttr() .
        
        
        Parameters
        ----------
        renderContext : str
        
        
        """
    @staticmethod
    def GetShadowLinkCollectionAPI(*args, **kwargs):
        """
        
        GetShadowLinkCollectionAPI() -> CollectionAPI
        
        
        Return the UsdCollectionAPI interface used for examining and modifying
        the shadow-linking of this light.
        
        
        Shadow-linking controls which geometry casts shadows from this light.
        
        
        
        """
    @staticmethod
    def GetSpecularAttr(*args, **kwargs):
        """
        
        GetSpecularAttr() -> Attribute
        
        
        A multiplier for the effect of this light on the specular response of
        materials.
        
        
        This is a non-physical control.
        
        Declaration
        
        ``float inputs:specular = 1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
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
        
        __init__(connectable)
        
        
        Constructor that takes a ConnectableAPI object.
        
        
        Allow implicit conversion of a UsdShadeConnectableAPI to
        UsdLuxLightAPI
        
        
        Parameters
        ----------
        connectable : ConnectableAPI
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim)
        
        
        Construct a UsdLuxLightAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxLightAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxLightAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxLightAPI (schemaObj.GetPrim()), as it
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
class LightFilter(pxr.UsdGeom.Xformable):
    """
    
    A light filter modifies the effect of a light. Lights refer to filters
    via relationships so that filters may be shared.
    
    **Linking**
    
    Filters can be linked to geometry. Linking controls which geometry a
    light-filter affects, when considering the light filters attached to a
    light illuminating the geometry.
    
    Linking is specified as a collection (UsdCollectionAPI) which can be
    accessed via GetFilterLinkCollection().
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdLuxTokens. So to set an attribute to the value"rightHanded", use
    UsdLuxTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def ConnectableAPI(*args, **kwargs):
        """
        
        ConnectableAPI() -> ConnectableAPI
        
        
        Contructs and returns a UsdShadeConnectableAPI object with this light
        filter.
        
        
        Note that most tasks can be accomplished without explicitly
        constructing a UsdShadeConnectable API, since connection-related API
        such as UsdShadeConnectableAPI::ConnectToSource() are static methods,
        and UsdLuxLightFilter will auto-convert to a UsdShadeConnectableAPI
        when passed to functions that want to act generically on a connectable
        UsdShadeConnectableAPI object.
        
        
        
        """
    @staticmethod
    def CreateInput(*args, **kwargs):
        """
        
        CreateInput(name, typeName) -> Input
        
        
        Create an input which can either have a value or can be connected.
        
        
        The attribute representing the input is created in
        the"inputs:"namespace. Inputs on light filters are connectable.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def CreateOutput(*args, **kwargs):
        """
        
        CreateOutput(name, typeName) -> Output
        
        
        Create an output which can either have a value or can be connected.
        
        
        The attribute representing the output is created in
        the"outputs:"namespace. Outputs on a light filter cannot be connected,
        as their value is assumed to be computed externally.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def CreateShaderIdAttr(*args, **kwargs):
        """
        
        CreateShaderIdAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShaderIdAttr() , and also Create vs Get Property Methods for
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
    def CreateShaderIdAttrForRenderContext(*args, **kwargs):
        """
        
        CreateShaderIdAttrForRenderContext(renderContext, defaultValue, writeSparsely) -> Attribute
        
        
        Creates the shader ID attribute for the given ``renderContext`` .
        
        
        See GetShaderIdAttrForRenderContext() , and also Create vs Get
        Property Methods for when to use Get vs Create. If specified, author
        ``defaultValue`` as the attribute's default, sparsely (when it makes
        sense to do so) if ``writeSparsely`` is ``true`` - the default for
        ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        renderContext : str
        
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> LightFilter
        
        
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
        
        **classmethod** Get(stage, path) -> LightFilter
        
        
        Return a UsdLuxLightFilter holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxLightFilter(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetFilterLinkCollectionAPI(*args, **kwargs):
        """
        
        GetFilterLinkCollectionAPI() -> CollectionAPI
        
        
        Return the UsdCollectionAPI interface used for examining and modifying
        the filter-linking of this light filter.
        
        
        Linking controls which geometry this light filter affects.
        
        
        
        """
    @staticmethod
    def GetInput(*args, **kwargs):
        """
        
        GetInput(name) -> Input
        
        
        Return the requested input if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetInputs(*args, **kwargs):
        """
        
        GetInputs(onlyAuthored) -> list[Input]
        
        
        Inputs are represented by attributes in the"inputs:"namespace.
        
        
        If ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
        """
    @staticmethod
    def GetOutput(*args, **kwargs):
        """
        
        GetOutput(name) -> Output
        
        
        Return the requested output if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetOutputs(*args, **kwargs):
        """
        
        GetOutputs(onlyAuthored) -> list[Output]
        
        
        Outputs are represented by attributes in the"outputs:"namespace.
        
        
        If ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
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
    def GetShaderId(*args, **kwargs):
        """
        
        GetShaderId(renderContexts) -> str
        
        
        Return the light filter's shader ID for the given list of available
        ``renderContexts`` .
        
        
        The shader ID returned by this function is the identifier to use when
        looking up the shader definition for this light filter in the shader
        registry.
        
        The render contexts are expected to be listed in priority order, so
        for each render context provided, this will try to find the shader ID
        attribute specific to that render context (see
        GetShaderIdAttrForRenderContext() ) and will return the value of the
        first one found that has a non-empty value. If no shader ID value can
        be found for any of the given render contexts or ``renderContexts`` is
        empty, then this will return the value of the default shader ID
        attribute (see GetShaderIdAttr() ).
        
        
        Parameters
        ----------
        renderContexts : list[str]
        
        
        """
    @staticmethod
    def GetShaderIdAttr(*args, **kwargs):
        """
        
        GetShaderIdAttr() -> Attribute
        
        
        Default ID for the light filter's shader.
        
        
        This defines the shader ID for this light filter when a render context
        specific shader ID is not available.
        
        GetShaderId
        
        GetShaderIdAttrForRenderContext
        
        SdrRegistry::GetShaderNodeByIdentifier
        
        SdrRegistry::GetShaderNodeByIdentifierAndType
        
        Declaration
        
        ``uniform token lightFilter:shaderId =""``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetShaderIdAttrForRenderContext(*args, **kwargs):
        """
        
        GetShaderIdAttrForRenderContext(renderContext) -> Attribute
        
        
        Returns the shader ID attribute for the given ``renderContext`` .
        
        
        If ``renderContext`` is non-empty, this will try to return an
        attribute named *lightFilter:shaderId* with the namespace prefix
        ``renderContext`` . For example, if the passed in render context
        is"ri"then the attribute returned by this function would have the
        following signature:
        
        Declaration
        
        ``token ri:lightFilter:shaderId``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        If the render context is empty, this will return the default shader ID
        attribute as returned by GetShaderIdAttr() .
        
        
        Parameters
        ----------
        renderContext : str
        
        
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
        
        __init__(connectable)
        
        
        Constructor that takes a ConnectableAPI object.
        
        
        Allow implicit conversion of UsdShadeConnectableAPI to
        UsdLuxLightFilter.
        
        
        Parameters
        ----------
        connectable : ConnectableAPI
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim)
        
        
        Construct a UsdLuxLightFilter on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxLightFilter::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxLightFilter on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxLightFilter (schemaObj.GetPrim()), as
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
class LightListAPI(pxr.Usd.APISchemaBase):
    """
    
    API schema to support discovery and publishing of lights in a scene.
    
    Discovering Lights via Traversal
    ================================
    
    To motivate this API, consider what is required to discover all lights
    in a scene. We must load all payloads and traverse all prims:
    
    .. code-block:: text
    
      01  // Load everything on the stage so we can find all lights,
      02  // including those inside payloads
      03  stage->Load();
      04  
      05  // Traverse all prims, checking if they have an applied UsdLuxLightAPI
      06  // (Note: ignoring instancing and a few other things for simplicity)
      07  SdfPathVector lights;
      08  for (UsdPrim prim: stage->Traverse()) {
      09      if (prim.HasAPI<UsdLuxLightAPI>()) {
      10          lights.push_back(i->GetPath());
      11      }
      12  }
    
    This traversal  suitably elaborated to handle certain details  is the
    first and simplest thing UsdLuxLightListAPI provides.
    UsdLuxLightListAPI::ComputeLightList() performs this traversal and
    returns all lights in the scene:
    
    .. code-block:: text
    
      01  UsdLuxLightListAPI listAPI(stage->GetPseudoRoot());
      02  SdfPathVector lights = listAPI.ComputeLightList();
    
    Publishing a Cached Light List
    ==============================
    
    Consider a USD client that needs to quickly discover lights but wants
    to defer loading payloads and traversing the entire scene where
    possible, and is willing to do up-front computation and caching to
    achieve that.
    
    UsdLuxLightListAPI provides a way to cache the computed light list, by
    publishing the list of lights onto prims in the model hierarchy.
    Consider a big set that contains lights:
    
    .. code-block:: text
    
      01  def Xform "BigSetWithLights" (
      02      kind = "assembly"
      03      payload = @BigSetWithLights.usd@   // Heavy payload
      04  ) {
      05      // Pre-computed, cached list of lights inside payload
      06      rel lightList = [
      07          <./Lights/light_1>,
      08          <./Lights/light_2>,
      09          \\.\\.\\.
      10      ]
      11      token lightList:cacheBehavior = "consumeAndContinue";
      12  }
    
    The lightList relationship encodes a set of lights, and the
    lightList:cacheBehavior property provides fine-grained control over
    how to use that cache. (See details below.)
    
    The cache can be created by first invoking
    ComputeLightList(ComputeModeIgnoreCache) to pre-compute the list and
    then storing the result with UsdLuxLightListAPI::StoreLightList() .
    
    To enable efficient retrieval of the cache, it should be stored on a
    model hierarchy prim. Furthermore, note that while you can use a
    UsdLuxLightListAPI bound to the pseudo-root prim to query the lights
    (as in the example above) because it will perform a traversal over
    descendants, you cannot store the cache back to the pseduo-root prim.
    
    To consult the cached list, we invoke
    ComputeLightList(ComputeModeConsultModelHierarchyCache):
    
    .. code-block:: text
    
      01  // Find and load all lights, using lightList cache where available
      02  UsdLuxLightListAPI list(stage->GetPseudoRoot());
      03  SdfPathSet lights = list.ComputeLightList(
      04      UsdLuxLightListAPI::ComputeModeConsultModelHierarchyCache);
      05  stage.LoadAndUnload(lights, SdfPathSet());
    
    In this mode, ComputeLightList() will traverse the model hierarchy,
    accumulating cached light lists.
    
    Controlling Cache Behavior
    ==========================
    
    The lightList:cacheBehavior property gives additional fine-grained
    control over cache behavior:
    
       - The fallback value,"ignore", indicates that the lightList should
         be disregarded. This provides a way to invalidate cache entries. Note
         that unless"ignore"is specified, a lightList with an empty list of
         targets is considered a cache indicating that no lights are present.
    
       - The value"consumeAndContinue"indicates that the cache should be
         consulted to contribute lights to the scene, and that recursion should
         continue down the model hierarchy in case additional lights are added
         as descedants. This is the default value established when
         StoreLightList() is invoked. This behavior allows the lights within a
         large model, such as the BigSetWithLights example above, to be
         published outside the payload, while also allowing referencing and
         layering to add additional lights over that set.
    
       - The value"consumeAndHalt"provides a way to terminate recursive
         traversal of the scene for light discovery. The cache will be
         consulted but no descendant prims will be examined.
    
    Instancing
    ==========
    
    Where instances are present, UsdLuxLightListAPI::ComputeLightList()
    will return the instance-unique paths to any lights discovered within
    those instances. Lights within a UsdGeomPointInstancer will not be
    returned, however, since they cannot be referred to solely via paths.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdLuxTokens. So to set an attribute to the value"rightHanded", use
    UsdLuxTokens->rightHanded as the value.
    
    """
    class ComputeMode(pxr.Tf.Tf_PyEnumWrapper):
        """
        
        Runtime control over whether to consult stored lightList caches.
        
        """
        _baseName: typing.ClassVar[str] = 'LightListAPI'
        allValues: typing.ClassVar[tuple]  # value = (UsdLux.LightListAPI.ComputeModeConsultModelHierarchyCache, UsdLux.LightListAPI.ComputeModeIgnoreCache)
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
    ComputeModeConsultModelHierarchyCache: typing.ClassVar[ComputeMode]  # value = UsdLux.LightListAPI.ComputeModeConsultModelHierarchyCache
    ComputeModeIgnoreCache: typing.ClassVar[ComputeMode]  # value = UsdLux.LightListAPI.ComputeModeIgnoreCache
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> LightListAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"LightListAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.
        
        A valid UsdLuxLightListAPI object is returned upon success. An invalid
        (or empty) UsdLuxLightListAPI object is returned upon failure. See
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
    def ComputeLightList(*args, **kwargs):
        """
        
        ComputeLightList(mode) -> SdfPathSet
        
        
        Computes and returns the list of lights and light filters in the
        stage, optionally consulting a cached result.
        
        
        In ComputeModeIgnoreCache mode, caching is ignored, and this does a
        prim traversal looking for prims that have a UsdLuxLightAPI or are of
        type UsdLuxLightFilter.
        
        In ComputeModeConsultModelHierarchyCache, this does a traversal only
        of the model hierarchy. In this traversal, any lights that live as
        model hierarchy prims are accumulated, as well as any paths stored in
        lightList caches. The lightList:cacheBehavior attribute gives further
        control over the cache behavior; see the class overview for details.
        
        When instances are present, ComputeLightList(ComputeModeIgnoreCache)
        will return the instance-uniqiue paths to any lights discovered within
        those instances. Lights within a UsdGeomPointInstancer will not be
        returned, however, since they cannot be referred to solely via paths.
        
        
        Parameters
        ----------
        mode : ComputeMode
        
        
        """
    @staticmethod
    def CreateLightListCacheBehaviorAttr(*args, **kwargs):
        """
        
        CreateLightListCacheBehaviorAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetLightListCacheBehaviorAttr() , and also Create vs Get Property
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
    def CreateLightListRel(*args, **kwargs):
        """
        
        CreateLightListRel() -> Relationship
        
        
        See GetLightListRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> LightListAPI
        
        
        Return a UsdLuxLightListAPI holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxLightListAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetLightListCacheBehaviorAttr(*args, **kwargs):
        """
        
        GetLightListCacheBehaviorAttr() -> Attribute
        
        
        Controls how the lightList should be interpreted.
        
        
        Valid values are:
        
           - consumeAndHalt: The lightList should be consulted, and if it
             exists, treated as a final authoritative statement of any lights that
             exist at or below this prim, halting recursive discovery of lights.
        
           - consumeAndContinue: The lightList should be consulted, but
             recursive traversal over nameChildren should continue in case
             additional lights are added by descendants.
        
           - ignore: The lightList should be entirely ignored. This provides a
             simple way to temporarily invalidate an existing cache. This is the
             fallback behavior.
        
        Declaration
        
        ``token lightList:cacheBehavior``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Allowed Values
        
        consumeAndHalt, consumeAndContinue, ignore
        
        
        
        """
    @staticmethod
    def GetLightListRel(*args, **kwargs):
        """
        
        GetLightListRel() -> Relationship
        
        
        Relationship to lights in the scene.
        
        
        
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
    def InvalidateLightList(*args, **kwargs):
        """
        
        InvalidateLightList() -> None
        
        
        Mark any stored lightlist as invalid, by setting the
        lightList:cacheBehavior attribute to ignore.
        
        
        
        """
    @staticmethod
    def StoreLightList(*args, **kwargs):
        """
        
        StoreLightList(arg1) -> None
        
        
        Store the given paths as the lightlist for this prim.
        
        
        Paths that do not have this prim's path as a prefix will be silently
        ignored. This will set the listList:cacheBehavior
        to"consumeAndContinue".
        
        
        Parameters
        ----------
        arg1 : SdfPathSet
        
        
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
        
        
        Construct a UsdLuxLightListAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxLightListAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxLightListAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxLightListAPI (schemaObj.GetPrim()), as
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
class ListAPI(pxr.Usd.APISchemaBase):
    """
    
    Deprecated
    
    Use LightListAPI instead
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdLuxTokens. So to set an attribute to the value"rightHanded", use
    UsdLuxTokens->rightHanded as the value.
    
    """
    class ComputeMode(pxr.Tf.Tf_PyEnumWrapper):
        """
        
        Runtime control over whether to consult stored lightList caches.
        
        """
        _baseName: typing.ClassVar[str] = 'ListAPI'
        allValues: typing.ClassVar[tuple]  # value = (UsdLux.ListAPI.ComputeModeConsultModelHierarchyCache, UsdLux.ListAPI.ComputeModeIgnoreCache)
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
    ComputeModeConsultModelHierarchyCache: typing.ClassVar[ComputeMode]  # value = UsdLux.ListAPI.ComputeModeConsultModelHierarchyCache
    ComputeModeIgnoreCache: typing.ClassVar[ComputeMode]  # value = UsdLux.ListAPI.ComputeModeIgnoreCache
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> ListAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"ListAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.
        
        A valid UsdLuxListAPI object is returned upon success. An invalid (or
        empty) UsdLuxListAPI object is returned upon failure. See
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
    def ComputeLightList(*args, **kwargs):
        """
        
        ComputeLightList(mode) -> SdfPathSet
        
        
        Computes and returns the list of lights and light filters in the
        stage, optionally consulting a cached result.
        
        
        In ComputeModeIgnoreCache mode, caching is ignored, and this does a
        prim traversal looking for prims that have a UsdLuxLightAPI or are of
        type UsdLuxLightFilter.
        
        In ComputeModeConsultModelHierarchyCache, this does a traversal only
        of the model hierarchy. In this traversal, any lights that live as
        model hierarchy prims are accumulated, as well as any paths stored in
        lightList caches. The lightList:cacheBehavior attribute gives further
        control over the cache behavior; see the class overview for details.
        
        When instances are present, ComputeLightList(ComputeModeIgnoreCache)
        will return the instance-uniqiue paths to any lights discovered within
        those instances. Lights within a UsdGeomPointInstancer will not be
        returned, however, since they cannot be referred to solely via paths.
        
        
        Parameters
        ----------
        mode : ComputeMode
        
        
        """
    @staticmethod
    def CreateLightListCacheBehaviorAttr(*args, **kwargs):
        """
        
        CreateLightListCacheBehaviorAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetLightListCacheBehaviorAttr() , and also Create vs Get Property
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
    def CreateLightListRel(*args, **kwargs):
        """
        
        CreateLightListRel() -> Relationship
        
        
        See GetLightListRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> ListAPI
        
        
        Return a UsdLuxListAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxListAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetLightListCacheBehaviorAttr(*args, **kwargs):
        """
        
        GetLightListCacheBehaviorAttr() -> Attribute
        
        
        Controls how the lightList should be interpreted.
        
        
        Valid values are:
        
           - consumeAndHalt: The lightList should be consulted, and if it
             exists, treated as a final authoritative statement of any lights that
             exist at or below this prim, halting recursive discovery of lights.
        
           - consumeAndContinue: The lightList should be consulted, but
             recursive traversal over nameChildren should continue in case
             additional lights are added by descendants.
        
           - ignore: The lightList should be entirely ignored. This provides a
             simple way to temporarily invalidate an existing cache. This is the
             fallback behavior.
        
        Declaration
        
        ``token lightList:cacheBehavior``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Allowed Values
        
        consumeAndHalt, consumeAndContinue, ignore
        
        
        
        """
    @staticmethod
    def GetLightListRel(*args, **kwargs):
        """
        
        GetLightListRel() -> Relationship
        
        
        Relationship to lights in the scene.
        
        
        
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
    def InvalidateLightList(*args, **kwargs):
        """
        
        InvalidateLightList() -> None
        
        
        Mark any stored lightlist as invalid, by setting the
        lightList:cacheBehavior attribute to ignore.
        
        
        
        """
    @staticmethod
    def StoreLightList(*args, **kwargs):
        """
        
        StoreLightList(arg1) -> None
        
        
        Store the given paths as the lightlist for this prim.
        
        
        Paths that do not have this prim's path as a prefix will be silently
        ignored. This will set the listList:cacheBehavior
        to"consumeAndContinue".
        
        
        Parameters
        ----------
        arg1 : SdfPathSet
        
        
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
        
        
        Construct a UsdLuxListAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxListAPI::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* ``prim`` , but will not immediately throw an error for an
        invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxListAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxListAPI (schemaObj.GetPrim()), as it
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
class MeshLightAPI(pxr.Usd.APISchemaBase):
    """
    
    This is the preferred API schema to apply to Mesh type prims when
    adding light behaviors to a mesh. At its base, this API schema has the
    built-in behavior of applying LightAPI to the mesh and overriding the
    default materialSyncMode to allow the emission/glow of the bound
    material to affect the color of the light. But, it additionally serves
    as a hook for plugins to attach additional properties to"mesh
    lights"through the creation of API schemas which are authored to auto-
    apply to MeshLightAPI.
    
    Auto applied API schemas
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> MeshLightAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"MeshLightAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.
        
        A valid UsdLuxMeshLightAPI object is returned upon success. An invalid
        (or empty) UsdLuxMeshLightAPI object is returned upon failure. See
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
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> MeshLightAPI
        
        
        Return a UsdLuxMeshLightAPI holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxMeshLightAPI(stage->GetPrimAtPath(path));
        
        
        
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
        
        
        Construct a UsdLuxMeshLightAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxMeshLightAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxMeshLightAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxMeshLightAPI (schemaObj.GetPrim()), as
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
class NonboundableLightBase(pxr.UsdGeom.Xformable):
    """
    
    Base class for intrinsic lights that are not boundable.
    
    The primary purpose of this class is to provide a direct API to the
    functions provided by LightAPI for concrete derived light types.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateColorAttr(*args, **kwargs):
        """
        
        CreateColorAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateColorAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateColorTemperatureAttr(*args, **kwargs):
        """
        
        CreateColorTemperatureAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateColorTemperatureAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateDiffuseAttr(*args, **kwargs):
        """
        
        CreateDiffuseAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateDiffuseAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateEnableColorTemperatureAttr(*args, **kwargs):
        """
        
        CreateEnableColorTemperatureAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateEnableColorTemperatureAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateExposureAttr(*args, **kwargs):
        """
        
        CreateExposureAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateExposureAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateFiltersRel(*args, **kwargs):
        """
        
        CreateFiltersRel() -> Relationship
        
        
        See UsdLuxLightAPI::CreateFiltersRel() .
        
        
        
        """
    @staticmethod
    def CreateIntensityAttr(*args, **kwargs):
        """
        
        CreateIntensityAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateIntensityAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateNormalizeAttr(*args, **kwargs):
        """
        
        CreateNormalizeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateNormalizeAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateSpecularAttr(*args, **kwargs):
        """
        
        CreateSpecularAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See UsdLuxLightAPI::CreateSpecularAttr() .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> NonboundableLightBase
        
        
        Return a UsdLuxNonboundableLightBase holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxNonboundableLightBase(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetColorAttr(*args, **kwargs):
        """
        
        GetColorAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetColorAttr() .
        
        
        
        """
    @staticmethod
    def GetColorTemperatureAttr(*args, **kwargs):
        """
        
        GetColorTemperatureAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetColorTemperatureAttr() .
        
        
        
        """
    @staticmethod
    def GetDiffuseAttr(*args, **kwargs):
        """
        
        GetDiffuseAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetDiffuseAttr() .
        
        
        
        """
    @staticmethod
    def GetEnableColorTemperatureAttr(*args, **kwargs):
        """
        
        GetEnableColorTemperatureAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetEnableColorTemperatureAttr() .
        
        
        
        """
    @staticmethod
    def GetExposureAttr(*args, **kwargs):
        """
        
        GetExposureAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetExposureAttr() .
        
        
        
        """
    @staticmethod
    def GetFiltersRel(*args, **kwargs):
        """
        
        GetFiltersRel() -> Relationship
        
        
        See UsdLuxLightAPI::GetFiltersRel() .
        
        
        
        """
    @staticmethod
    def GetIntensityAttr(*args, **kwargs):
        """
        
        GetIntensityAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetIntensityAttr() .
        
        
        
        """
    @staticmethod
    def GetNormalizeAttr(*args, **kwargs):
        """
        
        GetNormalizeAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetNormalizeAttr() .
        
        
        
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
    def GetSpecularAttr(*args, **kwargs):
        """
        
        GetSpecularAttr() -> Attribute
        
        
        See UsdLuxLightAPI::GetSpecularAttr() .
        
        
        
        """
    @staticmethod
    def LightAPI(*args, **kwargs):
        """
        
        LightAPI() -> LightAPI
        
        
        Contructs and returns a UsdLuxLightAPI object for this light.
        
        
        
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
        
        
        Construct a UsdLuxNonboundableLightBase on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxNonboundableLightBase::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxNonboundableLightBase on the prim held by
        ``schemaObj`` .
        
        
        Should be preferred over UsdLuxNonboundableLightBase
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
class PluginLight(pxr.UsdGeom.Xformable):
    """
    
    Light that provides properties that allow it to identify an external
    SdrShadingNode definition, through UsdShadeNodeDefAPI, that can be
    provided to render delegates without the need to provide a schema
    definition for the light's type.
    
    Plugin Lights and Light Filters
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> PluginLight
        
        
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
        
        **classmethod** Get(stage, path) -> PluginLight
        
        
        Return a UsdLuxPluginLight holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxPluginLight(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetNodeDefAPI(*args, **kwargs):
        """
        
        GetNodeDefAPI() -> NodeDefAPI
        
        
        Convenience method for accessing the UsdShadeNodeDefAPI functionality
        for this prim.
        
        
        One can also construct a UsdShadeNodeDefAPI directly from a UsdPrim.
        
        
        
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
        
        
        Construct a UsdLuxPluginLight on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxPluginLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxPluginLight on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxPluginLight (schemaObj.GetPrim()), as
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
class PluginLightFilter(LightFilter):
    """
    
    Light filter that provides properties that allow it to identify an
    external SdrShadingNode definition, through UsdShadeNodeDefAPI, that
    can be provided to render delegates without the need to provide a
    schema definition for the light filter's type.
    
    Plugin Lights and Light Filters
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> PluginLightFilter
        
        
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
        
        **classmethod** Get(stage, path) -> PluginLightFilter
        
        
        Return a UsdLuxPluginLightFilter holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxPluginLightFilter(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetNodeDefAPI(*args, **kwargs):
        """
        
        GetNodeDefAPI() -> NodeDefAPI
        
        
        Convenience method for accessing the UsdShadeNodeDefAPI functionality
        for this prim.
        
        
        One can also construct a UsdShadeNodeDefAPI directly from a UsdPrim.
        
        
        
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
        
        
        Construct a UsdLuxPluginLightFilter on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxPluginLightFilter::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxPluginLightFilter on the prim held by ``schemaObj``
        .
        
        
        Should be preferred over UsdLuxPluginLightFilter
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
class PortalLight(BoundableLightBase):
    """
    
    A rectangular portal in the local XY plane that guides sampling of a
    dome light. Transmits light in the -Z direction. The rectangle is 1
    unit in length.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> PortalLight
        
        
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
        
        **classmethod** Get(stage, path) -> PortalLight
        
        
        Return a UsdLuxPortalLight holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxPortalLight(stage->GetPrimAtPath(path));
        
        
        
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
        
        
        Construct a UsdLuxPortalLight on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxPortalLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxPortalLight on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxPortalLight (schemaObj.GetPrim()), as
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
class RectLight(BoundableLightBase):
    """
    
    Light emitted from one side of a rectangle. The rectangle is centered
    in the XY plane and emits light along the -Z axis. The rectangle is 1
    unit in length in the X and Y axis. In the default position, a texture
    file's min coordinates should be at (+X, +Y) and max coordinates at
    (-X, -Y).
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateHeightAttr(*args, **kwargs):
        """
        
        CreateHeightAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetHeightAttr() , and also Create vs Get Property Methods for when
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
    def CreateTextureFileAttr(*args, **kwargs):
        """
        
        CreateTextureFileAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetTextureFileAttr() , and also Create vs Get Property Methods for
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
    def CreateWidthAttr(*args, **kwargs):
        """
        
        CreateWidthAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetWidthAttr() , and also Create vs Get Property Methods for when
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
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> RectLight
        
        
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
        
        **classmethod** Get(stage, path) -> RectLight
        
        
        Return a UsdLuxRectLight holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxRectLight(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetHeightAttr(*args, **kwargs):
        """
        
        GetHeightAttr() -> Attribute
        
        
        Height of the rectangle, in the local Y axis.
        
        
        
        Declaration
        
        ``float inputs:height = 1``
        
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
    def GetTextureFileAttr(*args, **kwargs):
        """
        
        GetTextureFileAttr() -> Attribute
        
        
        A color texture to use on the rectangle.
        
        
        
        Declaration
        
        ``asset inputs:texture:file``
        
        C++ Type
        
        SdfAssetPath
        
        Usd Type
        
        SdfValueTypeNames->Asset
        
        
        
        """
    @staticmethod
    def GetWidthAttr(*args, **kwargs):
        """
        
        GetWidthAttr() -> Attribute
        
        
        Width of the rectangle, in the local X axis.
        
        
        
        Declaration
        
        ``float inputs:width = 1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
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
        
        
        Construct a UsdLuxRectLight on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxRectLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxRectLight on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxRectLight (schemaObj.GetPrim()), as it
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
class ShadowAPI(pxr.Usd.APISchemaBase):
    """
    
    Controls to refine a light's shadow behavior. These are non-physical
    controls that are valuable for visual lighting work.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> ShadowAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"ShadowAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.
        
        A valid UsdLuxShadowAPI object is returned upon success. An invalid
        (or empty) UsdLuxShadowAPI object is returned upon failure. See
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
    def ConnectableAPI(*args, **kwargs):
        """
        
        ConnectableAPI() -> ConnectableAPI
        
        
        Contructs and returns a UsdShadeConnectableAPI object with this shadow
        API prim.
        
        
        Note that a valid UsdLuxShadowAPI will only return a valid
        UsdShadeConnectableAPI if the its prim's Typed schema type is actually
        connectable.
        
        
        
        """
    @staticmethod
    def CreateInput(*args, **kwargs):
        """
        
        CreateInput(name, typeName) -> Input
        
        
        Create an input which can either have a value or can be connected.
        
        
        The attribute representing the input is created in
        the"inputs:"namespace. Inputs on shadow API are connectable.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def CreateOutput(*args, **kwargs):
        """
        
        CreateOutput(name, typeName) -> Output
        
        
        Create an output which can either have a value or can be connected.
        
        
        The attribute representing the output is created in
        the"outputs:"namespace. Outputs on a shadow API cannot be connected,
        as their value is assumed to be computed externally.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def CreateShadowColorAttr(*args, **kwargs):
        """
        
        CreateShadowColorAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShadowColorAttr() , and also Create vs Get Property Methods for
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
    def CreateShadowDistanceAttr(*args, **kwargs):
        """
        
        CreateShadowDistanceAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShadowDistanceAttr() , and also Create vs Get Property Methods
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
    def CreateShadowEnableAttr(*args, **kwargs):
        """
        
        CreateShadowEnableAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShadowEnableAttr() , and also Create vs Get Property Methods
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
    def CreateShadowFalloffAttr(*args, **kwargs):
        """
        
        CreateShadowFalloffAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShadowFalloffAttr() , and also Create vs Get Property Methods
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
    def CreateShadowFalloffGammaAttr(*args, **kwargs):
        """
        
        CreateShadowFalloffGammaAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShadowFalloffGammaAttr() , and also Create vs Get Property
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
        
        **classmethod** Get(stage, path) -> ShadowAPI
        
        
        Return a UsdLuxShadowAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxShadowAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetInput(*args, **kwargs):
        """
        
        GetInput(name) -> Input
        
        
        Return the requested input if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetInputs(*args, **kwargs):
        """
        
        GetInputs(onlyAuthored) -> list[Input]
        
        
        Inputs are represented by attributes in the"inputs:"namespace.
        
        
        If ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
        """
    @staticmethod
    def GetOutput(*args, **kwargs):
        """
        
        GetOutput(name) -> Output
        
        
        Return the requested output if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetOutputs(*args, **kwargs):
        """
        
        GetOutputs(onlyAuthored) -> list[Output]
        
        
        Outputs are represented by attributes in the"outputs:"namespace.
        
        
        If ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
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
    def GetShadowColorAttr(*args, **kwargs):
        """
        
        GetShadowColorAttr() -> Attribute
        
        
        The color of shadows cast by the light.
        
        
        This is a non-physical control. The default is to cast black shadows.
        
        Declaration
        
        ``color3f inputs:shadow:color = (0, 0, 0)``
        
        C++ Type
        
        GfVec3f
        
        Usd Type
        
        SdfValueTypeNames->Color3f
        
        
        
        """
    @staticmethod
    def GetShadowDistanceAttr(*args, **kwargs):
        """
        
        GetShadowDistanceAttr() -> Attribute
        
        
        The maximum distance shadows are cast.
        
        
        The default value (-1) indicates no limit.
        
        Declaration
        
        ``float inputs:shadow:distance = -1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetShadowEnableAttr(*args, **kwargs):
        """
        
        GetShadowEnableAttr() -> Attribute
        
        
        Enables shadows to be cast by this light.
        
        
        
        Declaration
        
        ``bool inputs:shadow:enable = 1``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
        """
    @staticmethod
    def GetShadowFalloffAttr(*args, **kwargs):
        """
        
        GetShadowFalloffAttr() -> Attribute
        
        
        The near distance at which shadow falloff begins.
        
        
        The default value (-1) indicates no falloff.
        
        Declaration
        
        ``float inputs:shadow:falloff = -1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetShadowFalloffGammaAttr(*args, **kwargs):
        """
        
        GetShadowFalloffGammaAttr() -> Attribute
        
        
        A gamma (i.e., exponential) control over shadow strength with linear
        distance within the falloff zone.
        
        
        This requires the use of shadowDistance and shadowFalloff.
        
        Declaration
        
        ``float inputs:shadow:falloffGamma = 1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
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
        
        __init__(connectable)
        
        
        Constructor that takes a ConnectableAPI object.
        
        
        Allow implicit conversion of UsdShadeConnectableAPI to
        UsdLuxShadowAPI.
        
        
        Parameters
        ----------
        connectable : ConnectableAPI
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim)
        
        
        Construct a UsdLuxShadowAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxShadowAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxShadowAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxShadowAPI (schemaObj.GetPrim()), as it
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
class ShapingAPI(pxr.Usd.APISchemaBase):
    """
    
    Controls for shaping a light's emission.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> ShapingAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"ShapingAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.
        
        A valid UsdLuxShapingAPI object is returned upon success. An invalid
        (or empty) UsdLuxShapingAPI object is returned upon failure. See
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
    def ConnectableAPI(*args, **kwargs):
        """
        
        ConnectableAPI() -> ConnectableAPI
        
        
        Contructs and returns a UsdShadeConnectableAPI object with this
        shaping API prim.
        
        
        Note that a valid UsdLuxShapingAPI will only return a valid
        UsdShadeConnectableAPI if the its prim's Typed schema type is actually
        connectable.
        
        
        
        """
    @staticmethod
    def CreateInput(*args, **kwargs):
        """
        
        CreateInput(name, typeName) -> Input
        
        
        Create an input which can either have a value or can be connected.
        
        
        The attribute representing the input is created in
        the"inputs:"namespace. Inputs on shaping API are connectable.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def CreateOutput(*args, **kwargs):
        """
        
        CreateOutput(name, typeName) -> Output
        
        
        Create an output which can either have a value or can be connected.
        
        
        The attribute representing the output is created in
        the"outputs:"namespace. Outputs on a shaping API cannot be connected,
        as their value is assumed to be computed externally.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def CreateShapingConeAngleAttr(*args, **kwargs):
        """
        
        CreateShapingConeAngleAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShapingConeAngleAttr() , and also Create vs Get Property
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
    def CreateShapingConeSoftnessAttr(*args, **kwargs):
        """
        
        CreateShapingConeSoftnessAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShapingConeSoftnessAttr() , and also Create vs Get Property
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
    def CreateShapingFocusAttr(*args, **kwargs):
        """
        
        CreateShapingFocusAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShapingFocusAttr() , and also Create vs Get Property Methods
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
    def CreateShapingFocusTintAttr(*args, **kwargs):
        """
        
        CreateShapingFocusTintAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShapingFocusTintAttr() , and also Create vs Get Property
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
    def CreateShapingIesAngleScaleAttr(*args, **kwargs):
        """
        
        CreateShapingIesAngleScaleAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShapingIesAngleScaleAttr() , and also Create vs Get Property
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
    def CreateShapingIesFileAttr(*args, **kwargs):
        """
        
        CreateShapingIesFileAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShapingIesFileAttr() , and also Create vs Get Property Methods
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
    def CreateShapingIesNormalizeAttr(*args, **kwargs):
        """
        
        CreateShapingIesNormalizeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetShapingIesNormalizeAttr() , and also Create vs Get Property
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
        
        **classmethod** Get(stage, path) -> ShapingAPI
        
        
        Return a UsdLuxShapingAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxShapingAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetInput(*args, **kwargs):
        """
        
        GetInput(name) -> Input
        
        
        Return the requested input if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetInputs(*args, **kwargs):
        """
        
        GetInputs(onlyAuthored) -> list[Input]
        
        
        Inputs are represented by attributes in the"inputs:"namespace.
        
        
        If ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
        """
    @staticmethod
    def GetOutput(*args, **kwargs):
        """
        
        GetOutput(name) -> Output
        
        
        Return the requested output if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetOutputs(*args, **kwargs):
        """
        
        GetOutputs(onlyAuthored) -> list[Output]
        
        
        Outputs are represented by attributes in the"outputs:"namespace.
        
        
        If ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
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
    def GetShapingConeAngleAttr(*args, **kwargs):
        """
        
        GetShapingConeAngleAttr() -> Attribute
        
        
        Angular limit off the primary axis to restrict the light spread.
        
        
        
        Declaration
        
        ``float inputs:shaping:cone:angle = 90``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetShapingConeSoftnessAttr(*args, **kwargs):
        """
        
        GetShapingConeSoftnessAttr() -> Attribute
        
        
        Controls the cutoff softness for cone angle.
        
        
        TODO: clarify semantics
        
        Declaration
        
        ``float inputs:shaping:cone:softness = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetShapingFocusAttr(*args, **kwargs):
        """
        
        GetShapingFocusAttr() -> Attribute
        
        
        A control to shape the spread of light.
        
        
        Higher focus values pull light towards the center and narrow the
        spread. Implemented as an off-axis cosine power exponent. TODO:
        clarify semantics
        
        Declaration
        
        ``float inputs:shaping:focus = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetShapingFocusTintAttr(*args, **kwargs):
        """
        
        GetShapingFocusTintAttr() -> Attribute
        
        
        Off-axis color tint.
        
        
        This tints the emission in the falloff region. The default tint is
        black. TODO: clarify semantics
        
        Declaration
        
        ``color3f inputs:shaping:focusTint = (0, 0, 0)``
        
        C++ Type
        
        GfVec3f
        
        Usd Type
        
        SdfValueTypeNames->Color3f
        
        
        
        """
    @staticmethod
    def GetShapingIesAngleScaleAttr(*args, **kwargs):
        """
        
        GetShapingIesAngleScaleAttr() -> Attribute
        
        
        Rescales the angular distribution of the IES profile.
        
        
        TODO: clarify semantics
        
        Declaration
        
        ``float inputs:shaping:ies:angleScale = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetShapingIesFileAttr(*args, **kwargs):
        """
        
        GetShapingIesFileAttr() -> Attribute
        
        
        An IES (Illumination Engineering Society) light profile describing the
        angular distribution of light.
        
        
        
        Declaration
        
        ``asset inputs:shaping:ies:file``
        
        C++ Type
        
        SdfAssetPath
        
        Usd Type
        
        SdfValueTypeNames->Asset
        
        
        
        """
    @staticmethod
    def GetShapingIesNormalizeAttr(*args, **kwargs):
        """
        
        GetShapingIesNormalizeAttr() -> Attribute
        
        
        Normalizes the IES profile so that it affects the shaping of the light
        while preserving the overall energy output.
        
        
        
        Declaration
        
        ``bool inputs:shaping:ies:normalize = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
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
        
        __init__(connectable)
        
        
        Constructor that takes a ConnectableAPI object.
        
        
        Allow implicit conversion of UsdShadeConnectableAPI to
        UsdLuxShapingAPI.
        
        
        Parameters
        ----------
        connectable : ConnectableAPI
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim)
        
        
        Construct a UsdLuxShapingAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxShapingAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxShapingAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxShapingAPI (schemaObj.GetPrim()), as it
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
class SphereLight(BoundableLightBase):
    """
    
    Light emitted outward from a sphere.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateRadiusAttr(*args, **kwargs):
        """
        
        CreateRadiusAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetRadiusAttr() , and also Create vs Get Property Methods for when
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
    def CreateTreatAsPointAttr(*args, **kwargs):
        """
        
        CreateTreatAsPointAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetTreatAsPointAttr() , and also Create vs Get Property Methods
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
        
        **classmethod** Define(stage, path) -> SphereLight
        
        
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
        
        **classmethod** Get(stage, path) -> SphereLight
        
        
        Return a UsdLuxSphereLight holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxSphereLight(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
        """
        
        GetRadiusAttr() -> Attribute
        
        
        Radius of the sphere.
        
        
        
        Declaration
        
        ``float inputs:radius = 0.5``
        
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
    def GetTreatAsPointAttr(*args, **kwargs):
        """
        
        GetTreatAsPointAttr() -> Attribute
        
        
        A hint that this light can be treated as a'point'light (effectively, a
        zero-radius sphere) by renderers that benefit from non-area lighting.
        
        
        Renderers that only support area lights can disregard this.
        
        Declaration
        
        ``bool treatAsPoint = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
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
        
        
        Construct a UsdLuxSphereLight on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxSphereLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxSphereLight on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxSphereLight (schemaObj.GetPrim()), as
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
    angular: typing.ClassVar[str] = 'angular'
    automatic: typing.ClassVar[str] = 'automatic'
    collectionFilterLinkIncludeRoot: typing.ClassVar[str] = 'collection:filterLink:includeRoot'
    collectionLightLinkIncludeRoot: typing.ClassVar[str] = 'collection:lightLink:includeRoot'
    collectionShadowLinkIncludeRoot: typing.ClassVar[str] = 'collection:shadowLink:includeRoot'
    consumeAndContinue: typing.ClassVar[str] = 'consumeAndContinue'
    consumeAndHalt: typing.ClassVar[str] = 'consumeAndHalt'
    cubeMapVerticalCross: typing.ClassVar[str] = 'cubeMapVerticalCross'
    cylinderLight: typing.ClassVar[str] = 'CylinderLight'
    diskLight: typing.ClassVar[str] = 'DiskLight'
    distantLight: typing.ClassVar[str] = 'DistantLight'
    domeLight: typing.ClassVar[str] = 'DomeLight'
    extent: typing.ClassVar[str] = 'extent'
    filterLink: typing.ClassVar[str] = 'filterLink'
    geometry: typing.ClassVar[str] = 'geometry'
    geometryLight: typing.ClassVar[str] = 'GeometryLight'
    guideRadius: typing.ClassVar[str] = 'guideRadius'
    ignore: typing.ClassVar[str] = 'ignore'
    independent: typing.ClassVar[str] = 'independent'
    inputsAngle: typing.ClassVar[str] = 'inputs:angle'
    inputsColor: typing.ClassVar[str] = 'inputs:color'
    inputsColorTemperature: typing.ClassVar[str] = 'inputs:colorTemperature'
    inputsDiffuse: typing.ClassVar[str] = 'inputs:diffuse'
    inputsEnableColorTemperature: typing.ClassVar[str] = 'inputs:enableColorTemperature'
    inputsExposure: typing.ClassVar[str] = 'inputs:exposure'
    inputsHeight: typing.ClassVar[str] = 'inputs:height'
    inputsIntensity: typing.ClassVar[str] = 'inputs:intensity'
    inputsLength: typing.ClassVar[str] = 'inputs:length'
    inputsNormalize: typing.ClassVar[str] = 'inputs:normalize'
    inputsRadius: typing.ClassVar[str] = 'inputs:radius'
    inputsShadowColor: typing.ClassVar[str] = 'inputs:shadow:color'
    inputsShadowDistance: typing.ClassVar[str] = 'inputs:shadow:distance'
    inputsShadowEnable: typing.ClassVar[str] = 'inputs:shadow:enable'
    inputsShadowFalloff: typing.ClassVar[str] = 'inputs:shadow:falloff'
    inputsShadowFalloffGamma: typing.ClassVar[str] = 'inputs:shadow:falloffGamma'
    inputsShapingConeAngle: typing.ClassVar[str] = 'inputs:shaping:cone:angle'
    inputsShapingConeSoftness: typing.ClassVar[str] = 'inputs:shaping:cone:softness'
    inputsShapingFocus: typing.ClassVar[str] = 'inputs:shaping:focus'
    inputsShapingFocusTint: typing.ClassVar[str] = 'inputs:shaping:focusTint'
    inputsShapingIesAngleScale: typing.ClassVar[str] = 'inputs:shaping:ies:angleScale'
    inputsShapingIesFile: typing.ClassVar[str] = 'inputs:shaping:ies:file'
    inputsShapingIesNormalize: typing.ClassVar[str] = 'inputs:shaping:ies:normalize'
    inputsSpecular: typing.ClassVar[str] = 'inputs:specular'
    inputsTextureFile: typing.ClassVar[str] = 'inputs:texture:file'
    inputsTextureFormat: typing.ClassVar[str] = 'inputs:texture:format'
    inputsWidth: typing.ClassVar[str] = 'inputs:width'
    latlong: typing.ClassVar[str] = 'latlong'
    lightFilterShaderId: typing.ClassVar[str] = 'lightFilter:shaderId'
    lightFilters: typing.ClassVar[str] = 'light:filters'
    lightLink: typing.ClassVar[str] = 'lightLink'
    lightList: typing.ClassVar[str] = 'lightList'
    lightListCacheBehavior: typing.ClassVar[str] = 'lightList:cacheBehavior'
    lightMaterialSyncMode: typing.ClassVar[str] = 'light:materialSyncMode'
    lightShaderId: typing.ClassVar[str] = 'light:shaderId'
    materialGlowTintsLight: typing.ClassVar[str] = 'materialGlowTintsLight'
    meshLight: typing.ClassVar[str] = 'MeshLight'
    mirroredBall: typing.ClassVar[str] = 'mirroredBall'
    noMaterialResponse: typing.ClassVar[str] = 'noMaterialResponse'
    orientToStageUpAxis: typing.ClassVar[str] = 'orientToStageUpAxis'
    portalLight: typing.ClassVar[str] = 'PortalLight'
    portals: typing.ClassVar[str] = 'portals'
    rectLight: typing.ClassVar[str] = 'RectLight'
    shadowLink: typing.ClassVar[str] = 'shadowLink'
    sphereLight: typing.ClassVar[str] = 'SphereLight'
    treatAsLine: typing.ClassVar[str] = 'treatAsLine'
    treatAsPoint: typing.ClassVar[str] = 'treatAsPoint'
    volumeLight: typing.ClassVar[str] = 'VolumeLight'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class VolumeLightAPI(pxr.Usd.APISchemaBase):
    """
    
    This is the preferred API schema to apply to Volume type prims when
    adding light behaviors to a volume. At its base, this API schema has
    the built-in behavior of applying LightAPI to the volume and
    overriding the default materialSyncMode to allow the emission/glow of
    the bound material to affect the color of the light. But, it
    additionally serves as a hook for plugins to attach additional
    properties to"volume lights"through the creation of API schemas which
    are authored to auto-apply to VolumeLightAPI.
    
    Auto applied API schemas
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> VolumeLightAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"VolumeLightAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdLuxVolumeLightAPI object is returned upon success. An
        invalid (or empty) UsdLuxVolumeLightAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.
        
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
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> VolumeLightAPI
        
        
        Return a UsdLuxVolumeLightAPI holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdLuxVolumeLightAPI(stage->GetPrimAtPath(path));
        
        
        
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
        
        
        Construct a UsdLuxVolumeLightAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdLuxVolumeLightAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdLuxVolumeLightAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdLuxVolumeLightAPI (schemaObj.GetPrim()),
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
__MFB_FULL_PACKAGE_NAME: str = 'usdLux'
