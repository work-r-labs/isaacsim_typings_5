from __future__ import annotations
import pxr.Sdf
import pxr.Tf
import typing
__all__ = ['APISchemaBase', 'AssetInfoKeys', 'Attribute', 'AttributeQuery', 'BlockStageCachePopulation', 'BlockStageCaches', 'ClipsAPI', 'CollectionAPI', 'CompositionArc', 'CrateInfo', 'EditContext', 'EditTarget', 'Inherits', 'InterpolationType', 'InterpolationTypeHeld', 'InterpolationTypeLinear', 'ListPosition', 'ListPositionBackOfAppendList', 'ListPositionBackOfPrependList', 'ListPositionFrontOfAppendList', 'ListPositionFrontOfPrependList', 'LoadPolicy', 'LoadWithDescendants', 'LoadWithoutDescendants', 'ModelAPI', 'Notice', 'Object', 'Payloads', 'Prim', 'PrimAllPrimsPredicate', 'PrimCompositionQuery', 'PrimDefaultPredicate', 'PrimDefinition', 'PrimHasDefiningSpecifier', 'PrimIsAbstract', 'PrimIsActive', 'PrimIsDefined', 'PrimIsGroup', 'PrimIsInstance', 'PrimIsLoaded', 'PrimIsModel', 'PrimRange', 'PrimTypeInfo', 'Property', 'References', 'Relationship', 'ResolveInfo', 'ResolveInfoSource', 'ResolveInfoSourceDefault', 'ResolveInfoSourceFallback', 'ResolveInfoSourceNone', 'ResolveInfoSourceTimeSamples', 'ResolveInfoSourceValueClips', 'ResolveTarget', 'SchemaBase', 'SchemaKind', 'SchemaRegistry', 'Specializes', 'Stage', 'StageCache', 'StageCacheContext', 'StageCacheContextBlockType', 'StageLoadRules', 'StagePopulationMask', 'TimeCode', 'Tokens', 'Typed', 'UsdCollectionMembershipQuery', 'UsdFileFormat', 'VariantSet', 'VariantSets', 'ZipFile', 'ZipFileWriter']
class APISchemaBase(SchemaBase):
    """
    
    The base class for all *API* schemas.
    
    An API schema provides an interface to a prim's qualities, but does
    not specify a typeName for the underlying prim. The prim's qualities
    include its inheritance structure, attributes, relationships etc.
    Since it cannot provide a typeName, an API schema is considered to be
    non-concrete.
    
    To auto-generate an API schema using usdGenSchema, simply leave the
    typeName empty and make it inherit from"/APISchemaBase"or from another
    API schema. See UsdModelAPI, UsdClipsAPI and UsdCollectionAPI for
    examples.
    
    API schemas are classified into applied and non-applied API schemas.
    The author of an API schema has to decide on the type of API schema at
    the time of its creation by setting customData['apiSchemaType'] in the
    schema definition (i.e. in the associated primSpec inside the
    schema.usda file). UsdAPISchemaBase implements methods that are used
    to record the application of an API schema on a USD prim.
    
    If an API schema only provides an interface to set certain core bits
    of metadata (like UsdModelAPI, which sets model kind and UsdClipsAPI,
    which sets clips-related metadata) OR if the API schema can apply to
    any type of prim or only to a known fixed set of prim types OR if
    there is no use of recording the application of the API schema, in
    such cases, it would be better to make it a non-applied API schema.
    Examples of non-applied API schemas include UsdModelAPI, UsdClipsAPI,
    UsdShadeConnectableAPI and UsdGeomPrimvarsAPI.
    
    If there is a need to discover (or record) whether a prim contains or
    subscribes to a given API schema, it would be advantageous to make the
    API schema be"applied". In general, API schemas that add one or more
    properties to a prim should be tagged as applied API schemas. A public
    Apply() method is generated for applied API schemas by usdGenSchema.
    An applied API schema must be applied to a prim via a call to the
    generated Apply() method, for the schema object to evaluate to true
    when converted to a bool using the explicit bool conversion operator.
    Examples of applied API schemas include UsdCollectionAPI,
    UsdGeomModelAPI and UsdGeomMotionAPI
    
    
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
    """
    
    Scenegraph object for authoring and retrieving numeric, string, and
    array valued data, sampled over time.
    
    The allowed value types for UsdAttribute are dictated by the Sdf
    ("Scene Description Foundations") core's data model, which we
    summarize in Basic Datatypes for Scene Description Provided by Sdf.
    
    Attribute Defining Qualities
    ============================
    
    In addition to its value type, an Attribute has two other defining
    qualities:
    
       - **Variability** Expresses whether an attribute is intended to
         have time samples ( GetVariability() == ``SdfVariabilityVarying`` ),
         or only a default ( GetVariability() == ``SdfVariabilityUniform`` ).
         For more on reasoning about time samples, see Value & Time-Sample
         Accessors.
    
       - **Custom** Determines whether an attribute belongs to a schema (
         IsCustom() == ``false`` ), or is a user-defined, custom attribute.
         schema attributes will always be defined on a prim of the schema type,
         ans may possess fallback values from the schema, whereas custom
         attributes must always first be authored in order to be defined. Note
         that *custom* is actually an aspect of UsdProperty, as UsdRelationship
         can also be custom or provided by a schema.
    
    Attribute Creation and Existence
    ================================
    
    One can always create an attribute generically via
    UsdPrim::CreateAttribute() , which ensures that an attribute"is
    defined"in the current UsdEditTarget. In order to author any metadata
    or a default or timesample for an attribute, *it must first be
    defined*. It is sufficient that the attribute be defined in any one of
    the layers participating in the stage's current composition; for
    *builtin* attributes (those belonging to the owning prim's defining
    schema, i.e. the most specific subclass of UsdTypedSchema for which
    prim.IsA<schema>() will evaluate to true) there need be no authored
    scene description, because a definition is provided by the prim's
    schema definition.
    
    **Creating** an attribute does not imply that the attribute has a
    value. More broadly, in the following code:
    
    .. code-block:: text
    
      if (UsdAttribute attr = prim.GetAttribute(TfToken("myAttr"))){
         \\.\\.\\.
      }
    
    The UsdAttribute passes the bool test, because it is defined; however,
    inside the clause, we have no guarantee that attr has a value.
    
    Attribute Value Interpolation
    =============================
    
    UsdAttribute supports two interpolation behaviors when retrieving
    attribute values at times where no value is explicitly authored. The
    desired behavior may be specified via UsdStage::SetInterpolationType.
    That behavior will be used for all calls to UsdAttribute::Get.
    
    The supported interpolation types are:
    
       - **Held** Attribute values are held constant between authored
         values. An attribute's value will be equal to the nearest preceding
         authored value. If there is no preceding authored value, the value
         will be equal to the nearest subsequent value.
    
       - **Linear** Attribute values are linearly interpolated between
         authored values.
         Linear interpolation is only supported for certain data types. See
         USD_LINEAR_INTERPOLATION_TYPES for the list of these types. Types that
         do not support linear interpolation will use held interpolation
         instead.
    
    Linear interpolation is done element-by-element for array, vector, and
    matrix data types. If linear interpolation is requested for two array
    values with different sizes, held interpolation will be used instead.
    
    Attribute Value Blocking
    ========================
    
    While prims can effectively be removed from a scene by deactivating
    them, properties cannot. However, it is possible to **block an
    attribute's value**, thus making the attribute behave as if it has a
    definition (and possibly metadata), but no authored value.
    
    One blocks an attribute using UsdAttribute::Block() , which will block
    the attribute in the stage's current UsdEditTarget, by authoring an
    SdfValueBlock in the attribute's *default*, and only values authored
    in weaker layers than the editTarget will be blocked. If the value
    block is the strongest authored opinion for the attribute, the
    HasAuthoredValue() method will return *false*, and the HasValue() and
    Get() methods will only return *true* if the attribute possesses a
    fallback value from the prim's schema."Unblocking"a blocked attribute
    is as simple as setting a *default* or timeSample value for the
    attribute in the same or stronger layer.
    
    The semantics of Value Clips necessitate the ability to selectively
    block an attribute's value for only some intervals in its authored
    range of samples. One can block an attribute's value at time *t* by
    calling ``attr.Set(SdfValueBlock, t)`` When an attribute is
    thusly"partially blocked", UsdAttribute::Get() will succeed only for
    those time intervals whose left/earlier bracketing timeSample is
    **not** SdfValueBlock.
    
    Due to this time-varying potential of value blocking, it may be the
    case that an attribute's HasAuthoredValue() and HasValue() methods
    both return *true* (because they do not and cannot consider time-
    varying blocks), but Get() may yet return *false* over some intervals.
    
    Attributes of type SdfAssetPath and UsdAttribute::Get()
    =======================================================
    
    If an attribute's value type is SdfAssetPath or SdfAssetPathArray,
    Get() performs extra work to compute the resolved asset paths, using
    the layer that has the strongest value opinion as the anchor
    for"relative"asset paths. Both the unresolved and resolved results are
    available through SdfAssetPath::GetAssetPath() and
    SdfAssetPath::GetResolvedPath() , respectively.
    
    Clients that call Get() on many asset-path-valued attributes may wish
    to employ an ArResolverScopedCache to improve asset path resolution
    performance.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def AddConnection(*args, **kwargs):
        """
        
        AddConnection(source, position) -> bool
        
        
        Adds ``source`` to the list of connections, in the position specified
        by ``position`` .
        
        
        Issue an error if ``source`` identifies a prototype prim or an object
        descendant to a prototype prim. It is not valid to author connections
        to these objects.
        
        What data this actually authors depends on what data is currently
        authored in the authoring layer, with respect to list-editing
        semantics, which we will document soon
        
        
        Parameters
        ----------
        source : Path
        
        position : ListPosition
        
        
        """
    @staticmethod
    def Block(*args, **kwargs):
        """
        
        Block() -> None
        
        
        Remove all time samples on an attribute and author a *block*
        ``default`` value.
        
        
        This causes the attribute to resolve as if there were no authored
        value opinions in weaker layers.
        
        See Attribute Value Blocking for more information, including
        information on time-varying blocking.
        
        
        
        """
    @staticmethod
    def Clear(*args, **kwargs):
        """
        
        Clear() -> bool
        
        
        Clears the authored default value and all time samples for this
        attribute at the current EditTarget and returns true on success.
        
        
        Calling clear when either no value is authored or no spec is present,
        is a silent no-op returning true.
        
        This method does not affect any other data authored on this attribute.
        
        
        
        """
    @staticmethod
    def ClearAtTime(*args, **kwargs):
        """
        
        ClearAtTime(time) -> bool
        
        
        Clear the authored value for this attribute at the given *time*, at
        the current EditTarget and return true on success.
        
        
        UsdTimeCode::Default() can be used to clear the default value.
        
        Calling clear when either no value is authored or no spec is present,
        is a silent no-op returning true.
        
        
        Parameters
        ----------
        time : TimeCode
        
        
        """
    @staticmethod
    def ClearColorSpace(*args, **kwargs):
        """
        
        ClearColorSpace() -> bool
        
        
        Clears authored color-space value on the attribute.
        
        
        
        SetColorSpace()
        
        
        
        """
    @staticmethod
    def ClearConnections(*args, **kwargs):
        """
        
        ClearConnections() -> bool
        
        
        Remove all opinions about the connections list from the current edit
        target.
        
        
        
        """
    @staticmethod
    def ClearDefault(*args, **kwargs):
        """
        
        ClearDefault() -> bool
        
        
        Shorthand for ClearAtTime(UsdTimeCode::Default()).
        
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        Get(value, time) -> bool
        
        
        Perform value resolution to fetch the value of this attribute at the
        requested UsdTimeCode ``time`` , which defaults to *default*.
        
        
        If no value is authored at ``time`` but values are authored at other
        times, this function will return an interpolated value based on the
        stage's interpolation type. See Attribute Value Interpolation.
        
        This templated accessor is designed for high performance data-
        streaming applications, allowing one to fetch data into the same
        container repeatedly, avoiding memory allocations when possible
        (VtArray containers will be resized as necessary to conform to the
        size of data being read).
        
        This template is only instantiated for the valid scene description
        value types and their corresponding VtArray containers. See Basic
        Datatypes for Scene Description Provided by Sdf for the complete list
        of types.
        
        Values are retrieved without regard to this attribute's variability.
        For example, a uniform attribute may retrieve time sample values if
        any are authored. However, the USD_VALIDATE_VARIABILITY TF_DEBUG code
        will cause debug information to be output if values that are
        inconsistent with this attribute's variability are retrieved. See
        UsdAttribute::GetVariability for more details.
        
        true if there was a value to be read, it was of the type T requested,
        and we read it successfully - false otherwise. For more details, see
        TimeSamples, Defaults, and Value Resolution, and also Attributes of
        type SdfAssetPath and UsdAttribute::Get() for information on how to
        retrieve resolved asset paths from SdfAssetPath-valued attributes.
        
        
        Parameters
        ----------
        value : T
        
        time : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        Get(value, time) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Type-erased access, often not as efficient as typed access.
        
        
        Parameters
        ----------
        value : VtValue
        
        time : TimeCode
        
        
        """
    @staticmethod
    def GetBracketingTimeSamples(*args, **kwargs):
        """
        
        GetBracketingTimeSamples(desiredTime, lower, upper, hasTimeSamples) -> bool
        
        
        Populate *lower* and *upper* with the next greater and lesser value
        relative to the *desiredTime*.
        
        
        Return false if no value exists or an error occurs, true if either a
        default value or timeSamples exist.
        
        Use standard resolution semantics: if a stronger default value is
        authored over weaker time samples, the default value hides the
        underlying timeSamples.
        
        1) If a sample exists at the *desiredTime*, set both upper and lower
        to *desiredTime*.
        
        2) If samples exist surrounding, but not equal to the *desiredTime*,
        set lower and upper to the bracketing samples nearest to the
        *desiredTime*.
        
        3) If the *desiredTime* is outside of the range of authored samples,
        clamp upper and lower to the nearest time sample.
        
        4) If no samples exist, do not modify upper and lower and set
        *hasTimeSamples* to false.
        
        In cases (1), (2) and (3), set *hasTimeSamples* to true.
        
        All four cases above are considered to be successful, thus the return
        value will be true and no error message will be emitted.
        
        
        Parameters
        ----------
        desiredTime : float
        
        lower : float
        
        upper : float
        
        hasTimeSamples : bool
        
        
        """
    @staticmethod
    def GetColorSpace(*args, **kwargs):
        """
        
        GetColorSpace() -> str
        
        
        Gets the color space in which the attribute is authored.
        
        
        
        SetColorSpace() UsdStage Color Configuration API
        
        
        
        """
    @staticmethod
    def GetConnections(*args, **kwargs):
        """
        
        GetConnections(sources) -> bool
        
        
        Compose this attribute's connections and fill ``sources`` with the
        result.
        
        
        All preexisting elements in ``sources`` are lost.
        
        Returns true if any connection path opinions have been authored and no
        composition errors were encountered, returns false otherwise. Note
        that authored opinions may include opinions that clear the connections
        and a return value of true does not necessarily indicate that
        ``sources`` will contain any connection paths.
        
        See Relationship Targets and Attribute Connections for details on
        behavior when targets point to objects beneath instance prims.
        
        The result is not cached, and thus recomputed on each query.
        
        
        Parameters
        ----------
        sources : list[Path]
        
        
        """
    @staticmethod
    def GetNumTimeSamples(*args, **kwargs):
        """
        
        GetNumTimeSamples() -> int
        
        
        Returns the number of time samples that have been authored.
        
        
        This method uses the standard resolution semantics, so if a stronger
        default value is authored over weaker time samples, the default value
        will hide the underlying timesamples.
        
        This function will query all value clips that may contribute time
        samples for this attribute, opening them if needed. This may be
        expensive, especially if many clips are involved.
        
        
        
        """
    @staticmethod
    def GetResolveInfo(*args, **kwargs):
        """
        
        GetResolveInfo(time) -> ResolveInfo
        
        
        Perform value resolution to determine the source of the resolved value
        of this attribute at the requested UsdTimeCode ``time`` .
        
        
        Parameters
        ----------
        time : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        GetResolveInfo() -> ResolveInfo
        
        
        Perform value resolution to determine the source of the resolved value
        of this attribute at any non-default time.
        
        
        Often (i.e. unless the attribute is affected by Value Clips) the
        source of the resolved value does not vary over time. See
        UsdAttributeQuery as an example that takes advantage of this quality
        of value resolution.
        
        
        
        """
    @staticmethod
    def GetRoleName(*args, **kwargs):
        """
        
        GetRoleName() -> str
        
        
        Return the roleName for this attribute's typeName.
        
        
        
        """
    @staticmethod
    def GetTimeSamples(*args, **kwargs):
        """
        
        GetTimeSamples(times) -> bool
        
        
        Populates a vector with authored sample times.
        
        
        Returns false only on error.
        
        This method uses the standard resolution semantics, so if a stronger
        default value is authored over weaker time samples, the default value
        will hide the underlying timesamples.
        
        This function will query all value clips that may contribute time
        samples for this attribute, opening them if needed. This may be
        expensive, especially if many clips are involved. times
        
        \\- on return, will contain the *sorted*, ascending timeSample
        ordinates. Any data in ``times`` will be lost, as this method clears
        ``times`` .
        
        UsdAttribute::GetTimeSamplesInInterval
        
        
        Parameters
        ----------
        times : list[float]
        
        
        """
    @staticmethod
    def GetTimeSamplesInInterval(*args, **kwargs):
        """
        
        GetTimeSamplesInInterval(interval, times) -> bool
        
        
        Populates a vector with authored sample times in ``interval`` .
        
        
        Returns false only on an error.
        
        This function will only query the value clips that may contribute time
        samples for this attribute in the given interval, opening them if
        necessary. interval
        
        \\- the GfInterval on which to gather time samples. times
        
        \\- on return, will contain the *sorted*, ascending timeSample
        ordinates. Any data in ``times`` will be lost, as this method clears
        ``times`` .
        
        UsdAttribute::GetTimeSamples
        
        
        Parameters
        ----------
        interval : Interval
        
        times : list[float]
        
        
        """
    @staticmethod
    def GetTypeName(*args, **kwargs):
        """
        
        GetTypeName() -> ValueTypeName
        
        
        Return the"scene description"value type name for this attribute.
        
        
        
        """
    @staticmethod
    def GetUnionedTimeSamples(*args, **kwargs):
        """
        
        **classmethod** GetUnionedTimeSamples(attrs, times) -> bool
        
        
        Populates the given vector, ``times`` with the union of all the
        authored sample times on all of the given attributes, ``attrs`` .
        
        
        
        This function will query all value clips that may contribute time
        samples for the attributes in ``attrs`` , opening them if needed. This
        may be expensive, especially if many clips are involved. The
        accumulated sample times will be in sorted (increasing) order and will
        not contain any duplicates.
        
        This clears any existing values in the ``times`` vector before
        accumulating sample times of the given attributes.
        
        false if any of the attributes in ``attr`` are invalid or if there's
        an error when fetching time-samples for any of the attributes.
        
        UsdAttribute::GetTimeSamples
        
        UsdAttribute::GetUnionedTimeSamplesInInterval
        
        
        Parameters
        ----------
        attrs : list[Attribute]
        
        times : list[float]
        
        
        """
    @staticmethod
    def GetUnionedTimeSamplesInInterval(*args, **kwargs):
        """
        
        **classmethod** GetUnionedTimeSamplesInInterval(attrs, interval, times) -> bool
        
        
        Populates the given vector, ``times`` with the union of all the
        authored sample times in the GfInterval, ``interval`` on all of the
        given attributes, ``attrs`` .
        
        
        
        This function will only query the value clips that may contribute time
        samples for the attributes in ``attrs`` , in the given ``interval`` ,
        opening them if necessary. The accumulated sample times will be in
        sorted (increasing) order and will not contain any duplicates.
        
        This clears any existing values in the ``times`` vector before
        accumulating sample times of the given attributes.
        
        false if any of the attributes in ``attr`` are invalid or if there's
        an error fetching time-samples for any of the attributes.
        
        UsdAttribute::GetTimeSamplesInInterval
        
        UsdAttribute::GetUnionedTimeSamples
        
        
        Parameters
        ----------
        attrs : list[Attribute]
        
        interval : Interval
        
        times : list[float]
        
        
        """
    @staticmethod
    def GetVariability(*args, **kwargs):
        """
        
        GetVariability() -> Variability
        
        
        An attribute's variability expresses whether it is intended to have
        time-samples ( ``SdfVariabilityVarying`` ), or only a single default
        value ( ``SdfVariabilityUniform`` ).
        
        
        Variability is required meta-data of all attributes, and its fallback
        value is SdfVariabilityVarying.
        
        
        
        """
    @staticmethod
    def HasAuthoredConnections(*args, **kwargs):
        """
        
        HasAuthoredConnections() -> bool
        
        
        Return true if this attribute has any authored opinions regarding
        connections.
        
        
        Note that this includes opinions that remove connections, so a true
        return does not necessarily indicate that this attribute has
        connections.
        
        
        
        """
    @staticmethod
    def HasAuthoredValue(*args, **kwargs):
        """
        
        HasAuthoredValue() -> bool
        
        
        Return true if this attribute has either an authored default value or
        authored time samples.
        
        
        If the attribute has been blocked, then return ``false``
        
        
        
        """
    @staticmethod
    def HasAuthoredValueOpinion(*args, **kwargs):
        """
        
        HasAuthoredValueOpinion() -> bool
        
        
        Deprecated
        
        This method is deprecated because it returns ``true`` even when an
        attribute is blocked. Please use HasAuthoredValue() instead. If you
        truly need to know whether the attribute has **any** authored value
        opinions, *including blocks*, you can make the following query:
        ``attr.GetResolveInfo(). HasAuthoredValueOpinion()``
        
        Return true if this attribute has either an authored default value or
        authored time samples.
        
        
        
        """
    @staticmethod
    def HasColorSpace(*args, **kwargs):
        """
        
        HasColorSpace() -> bool
        
        
        Returns whether color-space is authored on the attribute.
        
        
        
        GetColorSpace()
        
        
        
        """
    @staticmethod
    def HasFallbackValue(*args, **kwargs):
        """
        
        HasFallbackValue() -> bool
        
        
        Return true if this attribute has a fallback value provided by a
        registered schema.
        
        
        
        """
    @staticmethod
    def HasValue(*args, **kwargs):
        """
        
        HasValue() -> bool
        
        
        Return true if this attribute has an authored default value, authored
        time samples or a fallback value provided by a registered schema.
        
        
        If the attribute has been blocked, then return ``true`` if and only if
        it has a fallback value.
        
        
        
        """
    @staticmethod
    def RemoveConnection(*args, **kwargs):
        """
        
        RemoveConnection(source) -> bool
        
        
        Removes ``target`` from the list of targets.
        
        
        Issue an error if ``source`` identifies a prototype prim or an object
        descendant to a prototype prim. It is not valid to author connections
        to these objects.
        
        
        Parameters
        ----------
        source : Path
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(value, time) -> bool
        
        
        Set the value of this attribute in the current UsdEditTarget to
        ``value`` at UsdTimeCode ``time`` , which defaults to *default*.
        
        
        Values are authored without regard to this attribute's variability.
        For example, time sample values may be authored on a uniform
        attribute. However, the USD_VALIDATE_VARIABILITY TF_DEBUG code will
        cause debug information to be output if values that are inconsistent
        with this attribute's variability are authored. See
        UsdAttribute::GetVariability for more details.
        
        false and generate an error if type ``T`` does not match this
        attribute's defined scene description type **exactly**, or if there is
        no existing definition for the attribute.
        
        
        Parameters
        ----------
        value : T
        
        time : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        Set(value, time) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        As a convenience, we allow the setting of string value typed
        attributes via a C string value.
        
        
        Parameters
        ----------
        value : str
        
        time : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        Set(value, time) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        value : VtValue
        
        time : TimeCode
        
        
        """
    @staticmethod
    def SetColorSpace(*args, **kwargs):
        """
        
        SetColorSpace(colorSpace) -> None
        
        
        Sets the color space of the attribute to ``colorSpace`` .
        
        
        
        GetColorSpace() UsdStage Color Configuration API
        
        
        Parameters
        ----------
        colorSpace : str
        
        
        """
    @staticmethod
    def SetConnections(*args, **kwargs):
        """
        
        SetConnections(sources) -> bool
        
        
        Make the authoring layer's opinion of the connection list explicit,
        and set exactly to ``sources`` .
        
        
        Issue an error if ``source`` identifies a prototype prim or an object
        descendant to a prototype prim. It is not valid to author connections
        to these objects.
        
        If any path in ``sources`` is invalid, issue an error and return
        false.
        
        
        Parameters
        ----------
        sources : list[Path]
        
        
        """
    @staticmethod
    def SetTypeName(*args, **kwargs):
        """
        
        SetTypeName(typeName) -> bool
        
        
        Set the value for typeName at the current EditTarget, return true on
        success, false if the value can not be written.
        
        
        **Note** that this value should not be changed as it is typically
        either automatically authored or provided by a property definition.
        This method is provided primarily for fixing invalid scene
        description.
        
        
        Parameters
        ----------
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def SetVariability(*args, **kwargs):
        """
        
        SetVariability(variability) -> bool
        
        
        Set the value for variability at the current EditTarget, return true
        on success, false if the value can not be written.
        
        
        **Note** that this value should not be changed as it is typically
        either automatically authored or provided by a property definition.
        This method is provided primarily for fixing invalid scene
        description.
        
        
        Parameters
        ----------
        variability : Variability
        
        
        """
    @staticmethod
    def ValueMightBeTimeVarying(*args, **kwargs):
        """
        
        ValueMightBeTimeVarying() -> bool
        
        
        Return true if it is possible, but not certain, that this attribute's
        value changes over time, false otherwise.
        
        
        If this function returns false, it is certain that this attribute's
        value remains constant over time.
        
        This function is equivalent to checking if GetNumTimeSamples() >1, but
        may be more efficient since it does not actually need to get a full
        count of all time samples.
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct an invalid attribute.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim, proxyPrimPath, attrName)
        
        
        Parameters
        ----------
        prim : Usd_PrimData
        
        proxyPrimPath : Path
        
        attrName : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__(objType, prim, proxyPrimPath, propName)
        
        
        Parameters
        ----------
        objType : UsdObjType
        
        prim : Usd_PrimData
        
        proxyPrimPath : Path
        
        propName : str
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class AttributeQuery(Boost.Python.instance):
    """
    
    Object for efficiently making repeated queries for attribute values.
    
    Retrieving an attribute's value at a particular time requires
    determining the source of strongest opinion for that value. Often
    (i.e. unless the attribute is affected by Value Clips) this source
    does not vary over time. UsdAttributeQuery uses this fact to speed up
    repeated value queries by caching the source information for an
    attribute. It is safe to use a UsdAttributeQuery for any attribute -
    if the attribute *is* affected by Value Clips, the performance gain
    will just be less.
    
    Resolve targets
    ===============
    
    An attribute query can also be constructed for an attribute along with
    a UsdResolveTarget. A resolve target allows value resolution to
    consider only a subrange of the prim stack instead of the entirety of
    it. All of the methods of an attribute query created with a resolve
    target will perform value resolution within that resolve target. This
    can be useful for finding the value of an attribute resolved up to a
    particular layer or for determining if a value authored on layer would
    be overridden by a stronger opinion.
    
    Thread safety
    =============
    
    This object provides the basic thread-safety guarantee. Multiple
    threads may call the value accessor functions simultaneously.
    
    Invalidation
    ============
    
    This object does not listen for change notification. If a consumer is
    holding on to a UsdAttributeQuery, it is their responsibility to
    dispose of it in response to a resync change to the associated
    attribute. Failing to do so may result in incorrect values or crashes
    due to dereferencing invalid objects.
    
    """
    @staticmethod
    def CreateQueries(*args, **kwargs):
        """
        
        **classmethod** CreateQueries(prim, attrNames) -> list[AttributeQuery]
        
        
        Construct new queries for the attributes named in ``attrNames`` under
        the prim ``prim`` .
        
        
        The objects in the returned vector will line up 1-to-1 with
        ``attrNames`` .
        
        
        Parameters
        ----------
        prim : Prim
        
        attrNames : list[str]
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        Get(value, time) -> bool
        
        
        Perform value resolution to fetch the value of the attribute
        associated with this query at the requested UsdTimeCode ``time`` .
        
        
        
        UsdAttribute::Get
        
        
        Parameters
        ----------
        value : T
        
        time : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        Get(value, time) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Type-erased access, often not as efficient as typed access.
        
        
        Parameters
        ----------
        value : VtValue
        
        time : TimeCode
        
        
        """
    @staticmethod
    def GetAttribute(*args, **kwargs):
        """
        
        GetAttribute() -> Attribute
        
        
        Return the attribute associated with this query.
        
        
        
        """
    @staticmethod
    def GetBracketingTimeSamples(*args, **kwargs):
        """
        
        GetBracketingTimeSamples(desiredTime, lower, upper, hasTimeSamples) -> bool
        
        
        Populate *lower* and *upper* with the next greater and lesser value
        relative to the *desiredTime*.
        
        
        
        UsdAttribute::GetBracketingTimeSamples
        
        
        Parameters
        ----------
        desiredTime : float
        
        lower : float
        
        upper : float
        
        hasTimeSamples : bool
        
        
        """
    @staticmethod
    def GetNumTimeSamples(*args, **kwargs):
        """
        
        GetNumTimeSamples() -> int
        
        
        Returns the number of time samples that have been authored.
        
        
        
        UsdAttribute::GetNumTimeSamples
        
        
        
        """
    @staticmethod
    def GetTimeSamples(*args, **kwargs):
        """
        
        GetTimeSamples(times) -> bool
        
        
        Populates a vector with authored sample times.
        
        
        Returns false only on error.  Behaves identically to
        UsdAttribute::GetTimeSamples()
        
        UsdAttributeQuery::GetTimeSamplesInInterval
        
        
        Parameters
        ----------
        times : list[float]
        
        
        """
    @staticmethod
    def GetTimeSamplesInInterval(*args, **kwargs):
        """
        
        GetTimeSamplesInInterval(interval, times) -> bool
        
        
        Populates a vector with authored sample times in ``interval`` .
        
        
        Returns false only on an error.
        
        Behaves identically to UsdAttribute::GetTimeSamplesInInterval()
        
        
        Parameters
        ----------
        interval : Interval
        
        times : list[float]
        
        
        """
    @staticmethod
    def GetUnionedTimeSamples(*args, **kwargs):
        """
        
        **classmethod** GetUnionedTimeSamples(attrQueries, times) -> bool
        
        
        Populates the given vector, ``times`` with the union of all the
        authored sample times on all of the given attribute-query objects,
        ``attrQueries`` .
        
        
        Behaves identically to UsdAttribute::GetUnionedTimeSamples()
        
        false if one or more attribute-queries in ``attrQueries`` are invalid
        or if there's an error fetching time-samples for any of the attribute-
        query objects.
        
        UsdAttribute::GetUnionedTimeSamples
        
        UsdAttributeQuery::GetUnionedTimeSamplesInInterval
        
        
        Parameters
        ----------
        attrQueries : list[AttributeQuery]
        
        times : list[float]
        
        
        """
    @staticmethod
    def GetUnionedTimeSamplesInInterval(*args, **kwargs):
        """
        
        **classmethod** GetUnionedTimeSamplesInInterval(attrQueries, interval, times) -> bool
        
        
        Populates the given vector, ``times`` with the union of all the
        authored sample times in the GfInterval, ``interval`` on all of the
        given attribute-query objects, ``attrQueries`` .
        
        
        Behaves identically to UsdAttribute::GetUnionedTimeSamplesInInterval()
        
        false if one or more attribute-queries in ``attrQueries`` are invalid
        or if there's an error fetching time-samples for any of the attribute-
        query objects.
        
        UsdAttribute::GetUnionedTimeSamplesInInterval
        
        
        Parameters
        ----------
        attrQueries : list[AttributeQuery]
        
        interval : Interval
        
        times : list[float]
        
        
        """
    @staticmethod
    def HasAuthoredValue(*args, **kwargs):
        """
        
        HasAuthoredValue() -> bool
        
        
        Return true if this attribute has either an authored default value or
        authored time samples.
        
        
        If the attribute has been blocked, then return ``false``
        
        UsdAttribute::HasAuthoredValue()
        
        
        
        """
    @staticmethod
    def HasAuthoredValueOpinion(*args, **kwargs):
        """
        
        HasAuthoredValueOpinion() -> bool
        
        
        Deprecated
        
        This method is deprecated because it returns ``true`` even when an
        attribute is blocked. Please use HasAuthoredValue() instead. If you
        truly need to know whether the attribute has **any** authored value
        opinions, *including blocks*, you can make the following query:
        ``query.GetAttribute().GetResolveInfo(). HasAuthoredValueOpinion()``
        
        Return true if this attribute has either an authored default value or
        authored time samples.
        
        
        
        """
    @staticmethod
    def HasFallbackValue(*args, **kwargs):
        """
        
        HasFallbackValue() -> bool
        
        
        Return true if the attribute associated with this query has a fallback
        value provided by a registered schema.
        
        
        
        UsdAttribute::HasFallbackValue
        
        
        
        """
    @staticmethod
    def HasValue(*args, **kwargs):
        """
        
        HasValue() -> bool
        
        
        Return true if the attribute associated with this query has an
        authored default value, authored time samples or a fallback value
        provided by a registered schema.
        
        
        
        UsdAttribute::HasValue
        
        
        
        """
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        IsValid() -> bool
        
        
        Return true if this query is valid (i.e.
        
        
        it is associated with a valid attribute), false otherwise.
        
        
        
        """
    @staticmethod
    def ValueMightBeTimeVarying(*args, **kwargs):
        """
        
        ValueMightBeTimeVarying() -> bool
        
        
        Return true if it is possible, but not certain, that this attribute's
        value changes over time, false otherwise.
        
        
        
        UsdAttribute::ValueMightBeTimeVarying
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct an invalid query object.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Copy constructor.
        
        
        Parameters
        ----------
        other : AttributeQuery
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Move constructor.
        
        
        Parameters
        ----------
        other : AttributeQuery
        
        
        
        ----------------------------------------------------------------------
        
        __init__(attr)
        
        
        Construct a new query for the attribute ``attr`` .
        
        
        Parameters
        ----------
        attr : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim, attrName)
        
        
        Construct a new query for the attribute named ``attrName`` under the
        prim ``prim`` .
        
        
        Parameters
        ----------
        prim : Prim
        
        attrName : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__(attr, resolveTarget)
        
        
        Construct a new query for the attribute ``attr`` with the given
        resolve target ``resolveTarget`` .
        
        
        Note that a UsdResolveTarget is associated with a particular prim so
        only resolve targets for the attribute's owning prim are allowed.
        
        
        Parameters
        ----------
        attr : Attribute
        
        resolveTarget : ResolveTarget
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ClipsAPI(APISchemaBase):
    """
    
    UsdClipsAPI is an API schema that provides an interface to a prim's
    clip metadata. Clips are a"value resolution"feature that allows one to
    specify a sequence of usd files (clips) to be consulted, over time, as
    a source of varying overrides for the prims at and beneath this prim
    in namespace.
    
    SetClipAssetPaths() establishes the set of clips that can be
    consulted. SetClipActive() specifies the ordering of clip application
    over time (clips can be repeated), while SetClipTimes() specifies
    time-mapping from stage-time to clip-time for the clip active at a
    given stage-time, which allows for time-dilation and repetition of
    clips. Finally, SetClipPrimPath() determines the path within each clip
    that will map to this prim, i.e. the location within the clip at which
    we will look for opinions for this prim.
    
    The clip asset paths, times and active metadata can also be specified
    through template clip metadata. This can be desirable when your set of
    assets is very large, as the template metadata is much more concise.
    SetClipTemplateAssetPath() establishes the asset identifier pattern of
    the set of clips to be consulted. SetClipTemplateStride() ,
    SetClipTemplateEndTime() , and SetClipTemplateStartTime() specify the
    range in which USD will search, based on the template. From the set of
    resolved asset paths, times and active will be derived internally.
    
    A prim may have multiple"clip sets"  named sets of clips that each
    have their own values for the metadata described above. For example, a
    prim might have a clip set named"Clips_1"that specifies some group of
    clip asset paths, and another clip set named"Clips_2"that uses an
    entirely different set of clip asset paths. These clip sets are
    composed across composition arcs, so clip sets for a prim may be
    defined in multiple sublayers or references, for example. Individual
    metadata for a given clip set may be sparsely overridden.
    
    Important facts about clips:
    
       - Within the layerstack in which clips are established, the
         opinions within the clips will be *weaker* than any local opinions in
         the layerstack, but em stronger than varying opinions coming across
         references and variants.
    
       - We will never look for metadata or default opinions in clips
         when performing value resolution on the owning stage, since these
         quantities must be time-invariant.
         This leads to the common structure in which we reference a model
         asset on a prim, and then author clips at the same site: the asset
         reference will provide the topology and unvarying data for the model,
         while the clips will provide the time-sampled animation.
    
    For further information, see Sequencable, Re-timable Animated"Value
    Clips"
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ComputeClipAssetPaths(*args, **kwargs):
        """
        
        ComputeClipAssetPaths(clipSet) -> VtArray[AssetPath]
        
        
        Computes and resolves the list of clip asset paths used by the clip
        set named ``clipSet`` .
        
        
        This is the same list of paths that would be used during value
        resolution.
        
        If the clip set is defined using template clip metadata, this function
        will compute the asset paths based on the template parameters.
        Otherwise this function will use the authored clipAssetPaths.
        
        
        Parameters
        ----------
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        ComputeClipAssetPaths() -> VtArray[AssetPath]
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        """
    @staticmethod
    def GenerateClipManifest(*args, **kwargs):
        """
        
        GenerateClipManifest(clipSet, writeBlocksForClipsWithMissingValues) -> Layer
        
        
        Create a clip manifest containing entries for all attributes in the
        value clips for clip set ``clipSet`` .
        
        
        This returns an anonymous layer that can be exported and reused (
        
        SetClipManifestAssetPath). If ``writeBlocksForClipsWithMissingValues``
        is ``true`` , the generated manifest will have value blocks authored
        for each attribute at the activation times of clips that do not
        contain time samples for that attribute. This accelerates searches
        done when the interpolation of missing clip values is enabled. See
        GetInterpolateMissingClipValues and Interpolating Missing Values in
        Clip Set for more details.
        
        Returns an invalid SdfLayerRefPtr on failure.
        
        
        Parameters
        ----------
        clipSet : str
        
        writeBlocksForClipsWithMissingValues : bool
        
        
        
        ----------------------------------------------------------------------
        
        GenerateClipManifest(writeBlocksForClipsWithMissingValues) -> Layer
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        writeBlocksForClipsWithMissingValues : bool
        
        
        """
    @staticmethod
    def GenerateClipManifestFromLayers(*args, **kwargs):
        """
        
        **classmethod** GenerateClipManifestFromLayers(clipLayers, clipPrimPath) -> Layer
        
        
        Create a clip manifest containing entries for all attributes in the
        given ``clipLayers`` that belong to the prim at ``clipPrimPath`` and
        all descendants.
        
        
        This returns an anonymous layer that can be exported and reused (
        
        SetClipManifestAssetPath). Returns an invalid SdfLayerRefPtr on
        failure.
        
        
        Parameters
        ----------
        clipLayers : list[Layer]
        
        clipPrimPath : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> ClipsAPI
        
        
        Return a UsdClipsAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdClipsAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetClipActive(*args, **kwargs):
        """
        
        GetClipActive(activeClips, clipSet) -> bool
        
        
        List of pairs (time, clip index) indicating the time on the stage at
        which the clip in the clip set named ``clipSet`` specified by the clip
        index is active.
        
        
        For instance, a value of [(0.0, 0), (20.0, 1)] indicates that clip 0
        is active at time 0 and clip 1 is active at time 20.
        
        
        Parameters
        ----------
        activeClips : Vec2dArray
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        GetClipActive(activeClips) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        activeClips : Vec2dArray
        
        
        """
    @staticmethod
    def GetClipAssetPaths(*args, **kwargs):
        """
        
        GetClipAssetPaths(assetPaths, clipSet) -> bool
        
        
        List of asset paths to the clips in the clip set named ``clipSet`` .
        
        
        This list is unordered, but elements in this list are referred to by
        index in other clip-related fields.
        
        
        Parameters
        ----------
        assetPaths : VtArray[AssetPath]
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        GetClipAssetPaths(assetPaths) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        assetPaths : VtArray[AssetPath]
        
        
        """
    @staticmethod
    def GetClipManifestAssetPath(*args, **kwargs):
        """
        
        GetClipManifestAssetPath(manifestAssetPath, clipSet) -> bool
        
        
        Asset path for the clip manifest for the clip set named ``clipSet`` .
        
        
        The clip manifest indicates which attributes have time samples
        authored in the clips specified on this prim. During value resolution,
        clips will only be examined if the attribute exists and is declared as
        varying in the manifest. See Clip Manifest for more details.
        
        For instance, if this prim's path is</Prim_1>, the clip prim path
        is</Prim>, and we want values for the attribute</Prim_1.size>, we will
        only look within this prim's clips if the attribute</Prim.size>exists
        and is varying in the manifest.
        
        
        Parameters
        ----------
        manifestAssetPath : AssetPath
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        GetClipManifestAssetPath(manifestAssetPath) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        manifestAssetPath : AssetPath
        
        
        """
    @staticmethod
    def GetClipPrimPath(*args, **kwargs):
        """
        
        GetClipPrimPath(primPath, clipSet) -> bool
        
        
        Path to the prim in the clips in the clip set named ``clipSet`` from
        which time samples will be read.
        
        
        This prim's path will be substituted with this value to determine the
        final path in the clip from which to read data. For instance, if this
        prims'path is'/Prim_1', the clip prim path is'/Prim', and we want to
        get values for the attribute'/Prim_1.size'. The clip prim path will be
        substituted in, yielding'/Prim.size', and each clip will be examined
        for values at that path.
        
        
        Parameters
        ----------
        primPath : str
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        GetClipPrimPath(primPath) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        primPath : str
        
        
        """
    @staticmethod
    def GetClipSets(*args, **kwargs):
        """
        
        GetClipSets(clipSets) -> bool
        
        
        ListOp that may be used to affect how opinions from clip sets are
        applied during value resolution.
        
        
        By default, clip sets in a layer stack are examined in lexicographical
        order by name for attribute values during value resolution. The clip
        sets listOp can be used to reorder the clip sets in a layer stack or
        remove them entirely from consideration during value resolution
        without modifying the clips dictionary.
        
        This is *not* the list of clip sets that are authored on this prim. To
        retrieve that information, use GetClips to examine the clips
        dictionary directly.
        
        This function returns the clip sets listOp from the current edit
        target.
        
        
        Parameters
        ----------
        clipSets : StringListOp
        
        
        """
    @staticmethod
    def GetClipTemplateActiveOffset(*args, **kwargs):
        """
        
        GetClipTemplateActiveOffset(clipTemplateActiveOffset, clipSet) -> bool
        
        
        A double representing the offset value used by USD when determining
        the active period for each clip.
        
        
        
        
        Parameters
        ----------
        clipTemplateActiveOffset : float
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        GetClipTemplateActiveOffset(clipTemplateActiveOffset) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTemplateActiveOffset : float
        
        
        """
    @staticmethod
    def GetClipTemplateAssetPath(*args, **kwargs):
        """
        
        GetClipTemplateAssetPath(clipTemplateAssetPath, clipSet) -> bool
        
        
        A template string representing a set of assets to be used as clips for
        the clip set named ``clipSet`` .
        
        
        This string can be of two forms:
        
        integer frames: path/basename.###.usd
        
        subinteger frames: path/basename.##.##.usd.
        
        For the integer portion of the specification, USD will take a
        particular time, determined by the template start time, stride, and
        end time, and pad it with zeros up to the number of hashes provided so
        long as the number of hashes is greater than the digits required to
        specify the integer value.
        
        For instance:
        
        time = 12, template asset path = foo.##.usd =>foo.12.usd time = 12,
        template asset path = foo.###.usd =>foo.012.usd time = 333, template
        asset path = foo.#.usd =>foo.333.usd
        
        In the case of subinteger portion of a specifications, USD requires
        the specification to be exact.
        
        For instance:
        
        time = 1.15, template asset path = foo.#.###.usd =>foo.1.150.usd time
        = 1.145, template asset path = foo.#.##.usd =>foo.1.15.usd time = 1.1,
        template asset path = foo.#.##.usd =>foo.1.10.usd
        
        Note that USD requires that hash groups be adjacent in the string, and
        that there only be one or two such groups.
        
        
        Parameters
        ----------
        clipTemplateAssetPath : str
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        GetClipTemplateAssetPath(clipTemplateAssetPath) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTemplateAssetPath : str
        
        
        """
    @staticmethod
    def GetClipTemplateEndTime(*args, **kwargs):
        """
        
        GetClipTemplateEndTime(clipTemplateEndTime, clipSet) -> bool
        
        
        A double which indicates the end of the range USD will use to to
        search for asset paths for the clip set named ``clipSet`` .
        
        
        This value is inclusive in that range.
        
        GetClipTemplateAssetPath.
        
        
        Parameters
        ----------
        clipTemplateEndTime : float
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        GetClipTemplateEndTime(clipTemplateEndTime) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTemplateEndTime : float
        
        
        """
    @staticmethod
    def GetClipTemplateStartTime(*args, **kwargs):
        """
        
        GetClipTemplateStartTime(clipTemplateStartTime, clipSet) -> bool
        
        
        A double which indicates the start of the range USD will use to search
        for asset paths for the clip set named ``clipSet`` .
        
        
        This value is inclusive in that range.
        
        GetClipTemplateAssetPath.
        
        
        Parameters
        ----------
        clipTemplateStartTime : float
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        GetClipTemplateStartTime(clipTemplateStartTime) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTemplateStartTime : float
        
        
        """
    @staticmethod
    def GetClipTemplateStride(*args, **kwargs):
        """
        
        GetClipTemplateStride(clipTemplateStride, clipSet) -> bool
        
        
        A double representing the increment value USD will use when searching
        for asset paths for the clip set named ``clipSet`` .
        
        
        
        GetClipTemplateAssetPath.
        
        
        Parameters
        ----------
        clipTemplateStride : float
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        GetClipTemplateStride(clipTemplateStride) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTemplateStride : float
        
        
        """
    @staticmethod
    def GetClipTimes(*args, **kwargs):
        """
        
        GetClipTimes(clipTimes, clipSet) -> bool
        
        
        List of pairs (stage time, clip time) indicating the time in the
        active clip in the clip set named ``clipSet`` that should be consulted
        for values at the corresponding stage time.
        
        
        During value resolution, this list will be sorted by stage time; times
        will then be linearly interpolated between consecutive entries. For
        instance, for clip times [(0.0, 0.0), (10.0, 20.0)], at stage time 0,
        values from the active clip at time 0 will be used, at stage time 5,
        values from the active clip at time 10, and at stage time 10, clip
        values at time 20.
        
        
        Parameters
        ----------
        clipTimes : Vec2dArray
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        GetClipTimes(clipTimes) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTimes : Vec2dArray
        
        
        """
    @staticmethod
    def GetClips(*args, **kwargs):
        """
        
        GetClips(clips) -> bool
        
        
        Dictionary that contains the definition of the clip sets on this prim.
        
        
        Each entry in this dictionary defines a clip set: the entry's key is
        the name of the clip set and the entry's value is a dictionary
        containing the metadata that specifies the clips in the set.
        
        See UsdClipsAPIInfoKeys for the keys used for each clip set's
        dictionary, or use the other API to set or get values for a given clip
        set.
        
        
        Parameters
        ----------
        clips : VtDictionary
        
        
        """
    @staticmethod
    def GetInterpolateMissingClipValues(*args, **kwargs):
        """
        
        GetInterpolateMissingClipValues(interpolate, clipSet) -> bool
        
        
        Parameters
        ----------
        interpolate : bool
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        GetInterpolateMissingClipValues(interpolate) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        Parameters
        ----------
        interpolate : bool
        
        
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
    def SetClipActive(*args, **kwargs):
        """
        
        SetClipActive(activeClips, clipSet) -> bool
        
        
        Set the active clip metadata for the clip set named ``clipSet`` .
        
        
        
        GetClipActive()
        
        
        Parameters
        ----------
        activeClips : Vec2dArray
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        SetClipActive(activeClips) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        activeClips : Vec2dArray
        
        
        """
    @staticmethod
    def SetClipAssetPaths(*args, **kwargs):
        """
        
        SetClipAssetPaths(assetPaths, clipSet) -> bool
        
        
        Set the clip asset paths for the clip set named ``clipSet`` .
        
        
        
        GetClipAssetPaths()
        
        
        Parameters
        ----------
        assetPaths : VtArray[AssetPath]
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        SetClipAssetPaths(assetPaths) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        assetPaths : VtArray[AssetPath]
        
        
        """
    @staticmethod
    def SetClipManifestAssetPath(*args, **kwargs):
        """
        
        SetClipManifestAssetPath(manifestAssetPath, clipSet) -> bool
        
        
        Set the clip manifest asset path for this prim.
        
        
        
        GetClipManifestAssetPath()
        
        
        Parameters
        ----------
        manifestAssetPath : AssetPath
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        SetClipManifestAssetPath(manifestAssetPath) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        manifestAssetPath : AssetPath
        
        
        """
    @staticmethod
    def SetClipPrimPath(*args, **kwargs):
        """
        
        SetClipPrimPath(primPath, clipSet) -> bool
        
        
        Set the clip prim path for the clip set named ``clipSet`` .
        
        
        
        GetClipPrimPath()
        
        
        Parameters
        ----------
        primPath : str
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        SetClipPrimPath(primPath) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        primPath : str
        
        
        """
    @staticmethod
    def SetClipSets(*args, **kwargs):
        """
        
        SetClipSets(clipSets) -> bool
        
        
        Set the clip sets list op for this prim.
        
        
        
        GetClipSets
        
        
        Parameters
        ----------
        clipSets : StringListOp
        
        
        """
    @staticmethod
    def SetClipTemplateActiveOffset(*args, **kwargs):
        """
        
        SetClipTemplateActiveOffset(clipTemplateActiveOffset, clipSet) -> bool
        
        
        Set the clip template offset for the clip set named ``clipSet`` .
        
        
        
        GetClipTemplateActiveOffset
        
        
        Parameters
        ----------
        clipTemplateActiveOffset : float
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        SetClipTemplateActiveOffset(clipTemplateActiveOffset) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTemplateActiveOffset : float
        
        
        """
    @staticmethod
    def SetClipTemplateAssetPath(*args, **kwargs):
        """
        
        SetClipTemplateAssetPath(clipTemplateAssetPath, clipSet) -> bool
        
        
        Set the clip template asset path for the clip set named ``clipSet`` .
        
        
        
        GetClipTemplateAssetPath
        
        
        Parameters
        ----------
        clipTemplateAssetPath : str
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        SetClipTemplateAssetPath(clipTemplateAssetPath) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTemplateAssetPath : str
        
        
        """
    @staticmethod
    def SetClipTemplateEndTime(*args, **kwargs):
        """
        
        SetClipTemplateEndTime(clipTemplateEndTime, clipSet) -> bool
        
        
        Set the template end time for the clipset named ``clipSet`` .
        
        
        
        GetClipTemplateEndTime()
        
        
        Parameters
        ----------
        clipTemplateEndTime : float
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        SetClipTemplateEndTime(clipTemplateEndTime) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTemplateEndTime : float
        
        
        """
    @staticmethod
    def SetClipTemplateStartTime(*args, **kwargs):
        """
        
        SetClipTemplateStartTime(clipTemplateStartTime, clipSet) -> bool
        
        
        Set the template start time for the clip set named ``clipSet`` .
        
        
        
        GetClipTemplateStartTime
        
        
        Parameters
        ----------
        clipTemplateStartTime : float
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        SetClipTemplateStartTime(clipTemplateStartTime) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTemplateStartTime : float
        
        
        """
    @staticmethod
    def SetClipTemplateStride(*args, **kwargs):
        """
        
        SetClipTemplateStride(clipTemplateStride, clipSet) -> bool
        
        
        Set the template stride for the clip set named ``clipSet`` .
        
        
        
        GetClipTemplateStride()
        
        
        Parameters
        ----------
        clipTemplateStride : float
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        SetClipTemplateStride(clipTemplateStride) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTemplateStride : float
        
        
        """
    @staticmethod
    def SetClipTimes(*args, **kwargs):
        """
        
        SetClipTimes(clipTimes, clipSet) -> bool
        
        
        Set the clip times metadata for this prim.
        
        
        
        GetClipTimes()
        
        
        Parameters
        ----------
        clipTimes : Vec2dArray
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        SetClipTimes(clipTimes) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        
        UsdClipsAPISetNames
        
        
        Parameters
        ----------
        clipTimes : Vec2dArray
        
        
        """
    @staticmethod
    def SetClips(*args, **kwargs):
        """
        
        SetClips(clips) -> bool
        
        
        Set the clips dictionary for this prim.
        
        
        
        GetClips
        
        
        Parameters
        ----------
        clips : VtDictionary
        
        
        """
    @staticmethod
    def SetInterpolateMissingClipValues(*args, **kwargs):
        """
        
        SetInterpolateMissingClipValues(interpolate, clipSet) -> bool
        
        
        Set whether missing clip values are interpolated from surrounding
        clips.
        
        
        Parameters
        ----------
        interpolate : bool
        
        clipSet : str
        
        
        
        ----------------------------------------------------------------------
        
        SetInterpolateMissingClipValues(interpolate) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        
        
        Parameters
        ----------
        interpolate : bool
        
        
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
        
        
        Construct a UsdClipsAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdClipsAPI::Get (prim.GetStage(), prim.GetPath()) for a
        *valid* ``prim`` , but will not immediately throw an error for an
        invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdClipsAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdClipsAPI (schemaObj.GetPrim()), as it
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
class CollectionAPI(APISchemaBase):
    """
    
    This is a general purpose API schema, used to describe a collection of
    heterogeneous objects within the scene."Objects"here may be prims or
    properties belonging to prims or other collections. It's an add-on
    schema that can be applied many times to a prim with different
    collection names.
    
    A collection allows an enumeration of a set of paths to include and a
    set of paths to exclude. Whether the descendants of an included path
    are members of a collection are decided by its expansion rule (see
    below). If the collection excludes paths that are not descendents of
    included paths, the collection implicitly includes the root path</>.
    If such a collection also includes paths that are not descendants of
    the excluded paths, it is considered invalid, since the intention is
    ambiguous.
    
    All the properties authored by the schema are namespaced
    under"collection:". The given name of the collection provides
    additional namespacing for the various per-collection properties,
    which include the following:
    
       - **uniform token collection: *collectionName* :expansionRule** -
         specified how the paths that are included in the collection must be
         expanded to determine its members. Possible values include:
    
       - **explicitOnly** - only paths in the includes rel targets and not
         in the excludes rel targets belong to the collection.
    
       - **expandPrims** - all the prims at or below the includes rel-
         targets (and not under the excludes rel-targets) belong to the
         collection. Any property paths included in the collection would, of
         course, also be honored. This is the default behavior as it satisfies
         most use cases.
    
       - **expandPrimsAndProperties** - like expandPrims, but also
         includes all properties on all matched prims. We're still not quite
         sure what the use cases are for this, but you can use it to capture a
         whole lot of UsdObjects very concisely.
    
       - **bool collection: *collectionName* :includeRoot** - boolean
         attribute indicating whether the pseudo-root path</>should be counted
         as one of the included target paths. The fallback is false. This
         separate attribute is required because relationships cannot directly
         target the root.
    
       - **rel collection: *collectionName* :includes** - specifies a list
         of targets that are included in the collection. This can target prims
         or properties directly. A collection can insert the rules of another
         collection by making its *includes* relationship target the
         **collection:{collectionName}** property on the owning prim of the
         collection to be included. Such a property may not (and typically does
         not) exist on the UsdStage, but it is the path that is used to refer
         to the collection. It is important to note that including another
         collection does not guarantee the contents of that collection will be
         in the final collection; instead, the rules are merged. This means,
         for example, an exclude entry may exclude a portion of the included
         collection. When a collection includes one or more collections, the
         order in which targets are added to the includes relationship may
         become significant, if there are conflicting opinions about the same
         path. Targets that are added later are considered to be stronger than
         earlier targets for the same path.
    
       - **rel collection: *collectionName* :excludes** - specifies a list
         of targets that are excluded below the **included** paths in this
         collection. This can target prims or properties directly, but **cannot
         target another collection**. This is to keep the membership
         determining logic simple, efficient and easier to reason about.
         Finally, it is invalid for a collection to exclude paths that are not
         included in it. The presence of such"orphaned"excluded paths will not
         affect the set of paths included in the collection, but may affect the
         performance of querying membership of a path in the collection (see
         UsdCollectionAPI::MembershipQuery::IsPathIncluded) or of enumerating
         the objects belonging to the collection (see
         UsdCollectionAPI::GetIncludedObjects).
    
    **Implicit inclusion**
    
    In some scenarios it is useful to express a collection that includes
    everything except certain paths. To support this, a collection that
    has an exclude that is not a descendent of any include will include
    the root path</>.
    
    **Creating collections in C++**
    
    .. code-block:: text
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdTokens. So to set an attribute to the value"rightHanded", use
    UsdTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim, name) -> CollectionAPI
        
        
        Applies this **multiple-apply** API schema to the given ``prim`` along
        with the given instance name, ``name`` .
        
        
        This information is stored by adding"CollectionAPI:<i>name</i>"to the
        token-valued, listOp metadata *apiSchemas* on the prim. For example,
        if ``name`` is'instance1', the token'CollectionAPI:instance1'is added
        to'apiSchemas'.
        
        A valid UsdCollectionAPI object is returned upon success. An invalid
        (or empty) UsdCollectionAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        
        """
    @staticmethod
    def BlockCollection(*args, **kwargs):
        """
        
        BlockCollection() -> bool
        
        
        Blocks the targets of the includes and excludes relationships of the
        collection, making it<\\* *empty* if"includeRoot"is false (or unset)
        or.
        
        
        
           - *include everything* if"includeRoot"is true. (assuming there are
             no opinions in stronger edit targets).
        
        
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, name, whyNot) -> bool
        
        
        Returns true if this **multiple-apply** API schema can be applied,
        with the given instance name, ``name`` , to the given ``prim`` .
        
        
        If this schema can not be a applied the prim, this returns false and,
        if provided, populates ``whyNot`` with the reason it can not be
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
        
        name : str
        
        whyNot : str
        
        
        """
    @staticmethod
    def CanContainPropertyName(*args, **kwargs):
        """
        
        **classmethod** CanContainPropertyName(name) -> bool
        
        
        Test whether a given ``name`` contains the"collection:"prefix.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def ComputeIncludedObjects(*args, **kwargs):
        """
        
        **classmethod** ComputeIncludedObjects(query, stage, pred) -> set[Object]
        
        
        Returns all the usd objects that satisfy the predicate, ``pred`` in
        the collection represented by the UsdCollectionMembershipQuery object,
        ``query`` .
        
        
        The results depends on the load state of the UsdStage, ``stage`` .
        
        
        Parameters
        ----------
        query : UsdCollectionMembershipQuery
        
        stage : UsdStageWeak
        
        pred : _PrimFlagsPredicate
        
        
        """
    @staticmethod
    def ComputeIncludedPaths(*args, **kwargs):
        """
        
        **classmethod** ComputeIncludedPaths(query, stage, pred) -> SdfPathSet
        
        
        Returns all the paths that satisfy the predicate, ``pred`` in the
        collection represented by the UsdCollectionMembershipQuery object,
        ``query`` .
        
        
        The result depends on the load state of the UsdStage, ``stage`` .
        
        
        Parameters
        ----------
        query : UsdCollectionMembershipQuery
        
        stage : UsdStageWeak
        
        pred : _PrimFlagsPredicate
        
        
        """
    @staticmethod
    def ComputeMembershipQuery(*args, **kwargs):
        """
        
        ComputeMembershipQuery() -> UsdCollectionMembershipQuery
        
        
        Computes and returns a UsdCollectionMembershipQuery object which can
        be used to query inclusion or exclusion of paths in the collection.
        
        
        
        
        ----------------------------------------------------------------------
        
        ComputeMembershipQuery(query) -> None
        
        
        Populates the UsdCollectionMembershipQuery object with data from this
        collection, so it can be used to query inclusion or exclusion of
        paths.
        
        
        Parameters
        ----------
        query : UsdCollectionMembershipQuery
        
        
        """
    @staticmethod
    def CreateExcludesRel(*args, **kwargs):
        """
        
        CreateExcludesRel() -> Relationship
        
        
        See GetExcludesRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateExpansionRuleAttr(*args, **kwargs):
        """
        
        CreateExpansionRuleAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetExpansionRuleAttr() , and also Create vs Get Property Methods
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
    def CreateIncludeRootAttr(*args, **kwargs):
        """
        
        CreateIncludeRootAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetIncludeRootAttr() , and also Create vs Get Property Methods for
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
    def CreateIncludesRel(*args, **kwargs):
        """
        
        CreateIncludesRel() -> Relationship
        
        
        See GetIncludesRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def ExcludePath(*args, **kwargs):
        """
        
        ExcludePath(pathToExclude) -> bool
        
        
        Excludes or removes the given path, ``pathToExclude`` from the
        collection.
        
        
        If the collection is empty, the collection becomes one that includes
        all paths except the givne path. Otherwise, this does nothing if the
        path is not included in the collection.
        
        This does not modify the expansion-rule of the collection. Hence, if
        the expansionRule is *expandPrims* or *expandPrimsAndProperties*, then
        the descendants of ``pathToExclude`` will also be excluded from the
        collection, unless explicitly included.
        
        UsdCollectionAPI::IncludePath()
        
        
        Parameters
        ----------
        pathToExclude : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> CollectionAPI
        
        
        Return a UsdCollectionAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        ``path`` must be of the format<path>.collection:name.
        
        This is shorthand for the following:
        
        .. code-block:: text
        
          TfToken name = SdfPath::StripNamespace(path.GetToken());
          UsdCollectionAPI(
              stage->GetPrimAtPath(path.GetPrimPath()), name);
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        
        ----------------------------------------------------------------------
        
        Get(prim, name) -> CollectionAPI
        
        
        Return a UsdCollectionAPI with name ``name`` holding the prim ``prim``
        .
        
        
        Shorthand for UsdCollectionAPI(prim, name);
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        
        """
    @staticmethod
    def GetAll(*args, **kwargs):
        """
        
        **classmethod** GetAll(prim) -> list[CollectionAPI]
        
        
        Return a vector of all named instances of UsdCollectionAPI on the
        given ``prim`` .
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def GetAllCollections(*args, **kwargs):
        """
        
        **classmethod** GetAllCollections(prim) -> list[CollectionAPI]
        
        
        Returns all the named collections on the given USD prim.
        
        
        Deprecated
        
        Use GetAll(prim) instead.
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def GetCollection(*args, **kwargs):
        """
        
        **classmethod** GetCollection(stage, collectionPath) -> CollectionAPI
        
        
        Returns the collection represented by the given collection path,
        ``collectionPath`` on the given USD stage.
        
        
        Parameters
        ----------
        stage : Stage
        
        collectionPath : Path
        
        
        
        ----------------------------------------------------------------------
        
        GetCollection(prim, name) -> CollectionAPI
        
        
        Returns the schema object representing a collection named ``name`` on
        the given ``prim`` .
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        
        """
    @staticmethod
    def GetCollectionPath(*args, **kwargs):
        """
        
        GetCollectionPath() -> Path
        
        
        Returns the canonical path that represents this collection.
        
        
        This points to a property named"collection:{collectionName}"on the
        prim defining the collection (which won't really exist as a property
        on the UsdStage, but will be used to refer to the collection). This is
        the path to be used to"include"this collection in another collection.
        
        
        
        """
    @staticmethod
    def GetExcludesRel(*args, **kwargs):
        """
        
        GetExcludesRel() -> Relationship
        
        
        Specifies a list of targets that are excluded below the included paths
        in this collection.
        
        
        This can target prims or properties directly, but cannot target
        another collection. This is to keep the membership determining logic
        simple, efficient and easier to reason about. Finally, it is invalid
        for a collection to exclude paths that are not included in it. The
        presence of such"orphaned"excluded paths will not affect the set of
        paths included in the collection, but may affect the performance of
        querying membership of a path in the collection (see
        UsdCollectionAPI::MembershipQuery::IsPathIncluded) or of enumerating
        the objects belonging to the collection (see
        UsdCollectionAPI::GetIncludedObjects).
        
        
        
        """
    @staticmethod
    def GetExpansionRuleAttr(*args, **kwargs):
        """
        
        GetExpansionRuleAttr() -> Attribute
        
        
        Specifies how the paths that are included in the collection must be
        expanded to determine its members.
        
        
        
        Declaration
        
        ``uniform token expansionRule ="expandPrims"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        explicitOnly, expandPrims, expandPrimsAndProperties
        
        
        
        """
    @staticmethod
    def GetIncludeRootAttr(*args, **kwargs):
        """
        
        GetIncludeRootAttr() -> Attribute
        
        
        Boolean attribute indicating whether the pseudo-root path</>should be
        counted as one of the included target paths.
        
        
        The fallback is false. This separate attribute is required because
        relationships cannot directly target the root.
        
        Declaration
        
        ``uniform bool includeRoot``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetIncludesRel(*args, **kwargs):
        """
        
        GetIncludesRel() -> Relationship
        
        
        Specifies a list of targets that are included in the collection.
        
        
        This can target prims or properties directly. A collection can insert
        the rules of another collection by making its *includes* relationship
        target the **collection:{collectionName}** property on the owning prim
        of the collection to be included
        
        
        
        """
    @staticmethod
    def GetName(*args, **kwargs):
        """
        
        GetName() -> str
        
        
        Returns the name of this multiple-apply schema instance.
        
        
        
        """
    @staticmethod
    def GetNamedCollectionPath(*args, **kwargs):
        """
        
        **classmethod** GetNamedCollectionPath(prim, collectionName) -> Path
        
        
        Returns the canonical path to the collection named, ``name`` on the
        given prim, ``prim`` .
        
        
        
        GetCollectionPath()
        
        
        Parameters
        ----------
        prim : Prim
        
        collectionName : str
        
        
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
        
        
        
        ----------------------------------------------------------------------
        
        GetSchemaAttributeNames(includeInherited, instanceName) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes for a given instance name.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved. The names returned will have the
        proper namespace prefix.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        instanceName : str
        
        
        """
    @staticmethod
    def HasNoIncludedPaths(*args, **kwargs):
        """
        
        HasNoIncludedPaths() -> bool
        
        
        Returns true if the collection has nothing included in it.
        
        
        This requires both that the includes relationship have no target
        paths, and that the includeRoot attribute be false. Note that there
        may be cases where the collection has no objects included in it even
        when HasNoIncludedPaths() returns false. For example, if the included
        objects are unloaded or if the included objects are also excluded.
        
        
        
        """
    @staticmethod
    def IncludePath(*args, **kwargs):
        """
        
        IncludePath(pathToInclude) -> bool
        
        
        Includes or adds the given path, ``pathToInclude`` in the collection.
        
        
        This does nothing if the path is already included in the collection.
        
        This does not modify the expansion-rule of the collection. Hence, if
        the expansionRule is *expandPrims* or *expandPrimsAndProperties*, then
        the descendants of ``pathToInclude`` will be also included in the
        collection unless explicitly excluded.
        
        UsdCollectionAPI::ExcludePath()
        
        
        Parameters
        ----------
        pathToInclude : Path
        
        
        """
    @staticmethod
    def IsCollectionAPIPath(*args, **kwargs):
        """
        
        **classmethod** IsCollectionAPIPath(path, name) -> bool
        
        
        Checks if the given path ``path`` is of an API schema of type
        CollectionAPI.
        
        
        If so, it stores the instance name of the schema in ``name`` and
        returns true. Otherwise, it returns false.
        
        
        Parameters
        ----------
        path : Path
        
        name : str
        
        
        """
    @staticmethod
    def IsSchemaPropertyBaseName(*args, **kwargs):
        """
        
        **classmethod** IsSchemaPropertyBaseName(baseName) -> bool
        
        
        Checks if the given name ``baseName`` is the base name of a property
        of CollectionAPI.
        
        
        Parameters
        ----------
        baseName : str
        
        
        """
    @staticmethod
    def ResetCollection(*args, **kwargs):
        """
        
        ResetCollection() -> bool
        
        
        Resets the collection by clearing both the includes and excludes
        targets of the collection in the current UsdEditTarget.
        
        
        
        This does not modify the"includeRoot"attribute which is used to
        include or exclude everything (i.e. the pseudoRoot) in the USD stage.
        
        
        
        """
    @staticmethod
    def Validate(*args, **kwargs):
        """
        
        Validate(reason) -> bool
        
        
        Validates the collection by checking the following rules:
        
        
        
           - a collection's expansionRule should be one
             of"explicitOnly","expandPrims"or"expandPrimsAndProperties".
        
           - a collection should not have have a circular dependency on
             another collection.
        
           - a collection should not have both includes and excludes among its
             top-level rules
        
        
        
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
        
        __init__(prim, name)
        
        
        Construct a UsdCollectionAPI on UsdPrim ``prim`` with name ``name`` .
        
        
        Equivalent to UsdCollectionAPI::Get ( prim.GetStage(),
        prim.GetPath().AppendProperty("collection:name"));
        
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj, name)
        
        
        Construct a UsdCollectionAPI on the prim held by ``schemaObj`` with
        name ``name`` .
        
        
        Should be preferred over UsdCollectionAPI (schemaObj.GetPrim(), name),
        as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        name : str
        
        
        """
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
    """
    
    A class for introspecting the underlying qualities of
    .usdc'crate'files, for diagnostic purposes.
    
    """
    class Section(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 40
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
        __instance_size__: typing.ClassVar[int] = 64
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
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def GetFileVersion(*args, **kwargs):
        """
        
        GetFileVersion() -> str
        
        
        Return the file version.
        
        
        
        """
    @staticmethod
    def GetSections(*args, **kwargs):
        """
        
        GetSections() -> list[Section]
        
        
        Return the named file sections, their location and sizes in the file.
        
        
        
        """
    @staticmethod
    def GetSoftwareVersion(*args, **kwargs):
        """
        
        GetSoftwareVersion() -> str
        
        
        Return the software version.
        
        
        
        """
    @staticmethod
    def GetSummaryStats(*args, **kwargs):
        """
        
        GetSummaryStats() -> SummaryStats
        
        
        Return summary statistics structure for this file.
        
        
        
        """
    @staticmethod
    def Open(*args, **kwargs):
        """
        
        **classmethod** Open(fileName) -> CrateInfo
        
        
        Attempt to open and read ``fileName`` .
        
        
        Parameters
        ----------
        fileName : str
        
        
        """
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
    """
    
    A utility class to temporarily modify a stage's current EditTarget
    during an execution scope.
    
    This is an"RAII"-like object meant to be used as an automatic local
    variable. Upon construction, it sets a given stage's EditTarget, and
    upon destruction it restores the stage's EditTarget to what it was
    previously.
    
    Example usage, temporarily overriding a stage's EditTarget to direct
    an edit to the stage's session layer. When the *ctx* object expires,
    it restores the stage's EditTarget to whatever it was previously.
    
    .. code-block:: text
    
      void SetVisState(const UsdPrim  & prim, bool vis) {
          UsdEditContext ctx(prim.GetStage(),
                             prim.GetStage()->GetSessionLayer());
          prim.GetAttribute("visible").Set(vis);
      }
    
    **Threading Note**
    
    When one thread is mutating a *UsdStage*, it is unsafe for any other
    thread to either query or mutate it. Using this class with a stage in
    such a way that it modifies the stage's EditTarget constitutes a
    mutation.
    
    """
    __instance_size__: typing.ClassVar[int] = 120
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : EditContext
        
        
        
        ----------------------------------------------------------------------
        
        __init__(stage)
        
        
        Construct without modifying *stage's* current EditTarget.
        
        
        Save *stage's* current EditTarget to restore on destruction.
        
        
        Parameters
        ----------
        stage : Stage
        
        
        
        ----------------------------------------------------------------------
        
        __init__(stage, editTarget)
        
        
        Construct and save *stage's* current EditTarget to restore on
        destruction, then invoke stage->SetEditTarget(editTarget).
        
        
        If *editTarget* is invalid, a coding error will be issued by the
        *stage*, and its EditTarget will not be modified.
        
        
        Parameters
        ----------
        stage : Stage
        
        editTarget : EditTarget
        
        
        
        ----------------------------------------------------------------------
        
        __init__(stageTarget)
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This ctor is handy to construct an edit context from the return value
        of another function (Cannot return a UsdEditContext since it needs to
        be noncopyable).
        
        
        If *editTarget* is invalid, a coding error will be issued by the
        *stage*, and its EditTarget will not be modified.
        
        
        Parameters
        ----------
        stageTarget : tuple[Stage, EditTarget]
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class EditTarget(Boost.Python.instance):
    """
    
    Defines a mapping from scene graph paths to Sdf spec paths in a
    SdfLayer where edits should be directed, or up to where to perform
    partial composition.
    
    A UsdEditTarget can represent an arbitrary point in a composition
    graph for the purposes of placing edits and resolving values. This
    enables editing and resolving across references, classes, variants,
    and payloads.
    
    In the simplest case, an EditTarget represents a single layer in a
    stage's local LayerStack. In this case, the mapping that transforms
    scene graph paths to spec paths in the layer is the identity function.
    That is, the UsdAttribute path'/World/Foo.avar'would map to the
    SdfPropertySpec path'/World/Foo.avar'.
    
    For a more complex example, suppose'/World/Foo'in'Shot.usda'is a
    reference to'/Model'in'Model.usda'. One can construct a UsdEditTarget
    that maps scene graph paths from the'Shot.usda'stage across the
    reference to the appropriate paths in the'Model.usda'layer. For
    example, the UsdAttribute '/World/Foo.avar'would map to the
    SdfPropertySpec '/Model.avar'. Paths in the stage composed
    at'Shot.usda'that weren't prefixed by'/World/Foo'would not have a
    valid mapping to'Model.usda'.
    
    EditTargets may also work for any other kind of arc or series of arcs.
    This allows for editing across variants, classes, and payloads, or in
    a variant on the far side of a reference, for example.
    
    In addition to mapping scene paths to spec paths for editing,
    EditTargets may also be used to identify points in the composition
    graph for partial composition. Though it doesn't currently exist, a
    UsdCompose API that takes UsdEditTarget arguments may someday be
    provided.
    
    For convenience and deployment ease, SdfLayerHandles will implicitly
    convert to UsdEditTargets. A UsdEditTarget constructed in this way
    means direct opinions in a layer in a stage's local LayerStack.
    
    """
    __instance_size__: typing.ClassVar[int] = 88
    @staticmethod
    def ComposeOver(*args, **kwargs):
        """
        
        ComposeOver(weaker) -> EditTarget
        
        
        Return a new EditTarget composed over *weaker*.
        
        
        This is typically used to make an EditTarget"explicit". For example,
        an edit target with a layer but with no mapping and no LayerStack
        identifier indicates a layer in the local LayerStack of a composed
        scene. However, an EditTarget with the same layer but an explicit
        identity mapping and the LayerStack identifier of the composed scene
        may be desired. This can be obtained by composing a partial (e.g.
        layer only) EditTarget over an explicit EditTarget with layer, mapping
        and layer stack identifier.
        
        
        Parameters
        ----------
        weaker : EditTarget
        
        
        """
    @staticmethod
    def ForLocalDirectVariant(*args, **kwargs):
        """
        
        **classmethod** ForLocalDirectVariant(layer, varSelPath) -> EditTarget
        
        
        Convenience constructor for editing a direct variant in a local
        LayerStack.
        
        
        The ``varSelPath`` must be a prim variant selection path (see
        SdfPath::IsPrimVariantSelectionPath() ).
        
        
        Parameters
        ----------
        layer : Layer
        
        varSelPath : Path
        
        
        """
    @staticmethod
    def GetLayer(*args, **kwargs):
        """
        
        GetLayer() -> Layer
        
        
        Return the layer this EditTarget contains.
        
        
        
        
        ----------------------------------------------------------------------
        
        GetLayer() -> Layer
        
        
        
        """
    @staticmethod
    def GetMapFunction(*args, **kwargs):
        """
        
        GetMapFunction() -> MapFunction
        
        
        Returns the PcpMapFunction representing the map from source specs
        (including any variant selections) to the stage.
        
        
        
        """
    @staticmethod
    def GetPrimSpecForScenePath(*args, **kwargs):
        """
        
        GetPrimSpecForScenePath(scenePath) -> PrimSpec
        
        
        Convenience function for getting the PrimSpec in the edit target's
        layer for *scenePath*.
        
        
        This is equivalent to
        target.GetLayer()->GetPrimAtPath(target.MapToSpecPath(scenePath)) if
        target has a valid layer. If this target IsNull or there is no valid
        mapping from *scenePath* to a SdfPrimSpec path in the layer, return
        null.
        
        
        Parameters
        ----------
        scenePath : Path
        
        
        """
    @staticmethod
    def GetPropertySpecForScenePath(*args, **kwargs):
        """
        
        GetPropertySpecForScenePath(scenePath) -> PropertySpec
        
        
        Parameters
        ----------
        scenePath : Path
        
        
        """
    @staticmethod
    def GetSpecForScenePath(*args, **kwargs):
        """
        
        GetSpecForScenePath(scenePath) -> Spec
        
        
        Parameters
        ----------
        scenePath : Path
        
        
        """
    @staticmethod
    def IsNull(*args, **kwargs):
        """
        
        IsNull() -> bool
        
        
        Return true if this EditTarget is null.
        
        
        Null EditTargets map paths unchanged, and have no layer or LayerStack
        identifier.
        
        
        
        """
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        IsValid() -> bool
        
        
        Return true if this EditTarget is valid, false otherwise.
        
        
        Edit targets are considered valid when they have a layer.
        
        
        
        """
    @staticmethod
    def MapToSpecPath(*args, **kwargs):
        """
        
        MapToSpecPath(scenePath) -> Path
        
        
        Map the provided *scenePath* into a SdfSpec path for the EditTarget's
        layer, according to the EditTarget's mapping.
        
        
        Null edit targets and EditTargets for which *IsLocalLayer* are true
        return scenePath unchanged.
        
        
        Parameters
        ----------
        scenePath : Path
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct a null EditTarget.
        
        
        A null EditTarget will return paths unchanged when asked to map paths.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(layer, offset)
        
        
        Constructor.
        
        
        Allow implicit conversion from SdfLayerHandle. EditTargets constructed
        in this way specify layers in the scene's local LayerStack. This lets
        clients pass layers directly in this common case without explicitly
        having to construct a *UsdEditTarget* instance. To automatically
        supply the appropriate layer offset for the given layer, see
        UsdStage::GetEditTargetForLayer().
        
        
        Parameters
        ----------
        layer : Layer
        
        offset : LayerOffset
        
        
        
        ----------------------------------------------------------------------
        
        __init__(layer, offset)
        
        
        Convenience implicit conversion from SdfLayerRefPtr.
        
        
        See above constructor for more information.
        
        
        Parameters
        ----------
        layer : Layer
        
        offset : LayerOffset
        
        
        
        ----------------------------------------------------------------------
        
        __init__(layer, node)
        
        
        Construct an EditTarget with *layer* and *node*.
        
        
        The mapping will be used to map paths from the scene into the
        *layer's* namespace given the *PcpNodeRef* *node's* mapping.
        
        
        Parameters
        ----------
        layer : Layer
        
        node : NodeRef
        
        
        
        ----------------------------------------------------------------------
        
        __init__(layer, node)
        
        
        Convenience constructor taking SdfLayerRefPtr.
        
        
        See above constructor for more information.
        
        
        Parameters
        ----------
        layer : Layer
        
        node : NodeRef
        
        
        
        ----------------------------------------------------------------------
        
        __init__(layer, mapping)
        
        
        Parameters
        ----------
        layer : Layer
        
        mapping : MapFunction
        
        
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Inherits(Boost.Python.instance):
    """
    
    A proxy class for applying listOp edits to the inherit paths list for
    a prim.
    
    All paths passed to the UsdInherits API are expected to be in the
    namespace of the owning prim's stage. Subroot prim inherit paths will
    be translated from this namespace to the namespace of the current edit
    target, if necessary. If a path cannot be translated, a coding error
    will be issued and no changes will be made. Root prim inherit paths
    will not be translated.
    
    """
    @staticmethod
    def AddInherit(*args, **kwargs):
        """
        
        AddInherit(primPath, position) -> bool
        
        
        Adds a path to the inheritPaths listOp at the current EditTarget, in
        the position specified by ``position`` .
        
        
        Parameters
        ----------
        primPath : Path
        
        position : ListPosition
        
        
        """
    @staticmethod
    def ClearInherits(*args, **kwargs):
        """
        
        ClearInherits() -> bool
        
        
        Removes the authored inheritPaths listOp edits at the current edit
        target.
        
        
        
        """
    @staticmethod
    def GetAllDirectInherits(*args, **kwargs):
        """
        
        GetAllDirectInherits() -> list[Path]
        
        
        Return all the paths in this prim's stage's local layer stack that
        would compose into this prim via direct inherits (excluding prim specs
        that would be composed into this prim due to inherits authored on
        ancestral prims) in strong-to-weak order.
        
        
        Note that there currently may not be any scene description at these
        paths on the stage. This returns all the potential places that such
        opinions could appear.
        
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        Return the prim this object is bound to.
        
        
        
        
        ----------------------------------------------------------------------
        
        GetPrim() -> Prim
        
        
        
        """
    @staticmethod
    def RemoveInherit(*args, **kwargs):
        """
        
        RemoveInherit(primPath) -> bool
        
        
        Removes the specified path from the inheritPaths listOp at the current
        EditTarget.
        
        
        Parameters
        ----------
        primPath : Path
        
        
        """
    @staticmethod
    def SetInherits(*args, **kwargs):
        """
        
        SetInherits(items) -> bool
        
        
        Explicitly set the inherited paths, potentially blocking weaker
        opinions that add or remove items, returning true on success, false if
        the edit could not be performed.
        
        
        Parameters
        ----------
        items : list[Path]
        
        
        """
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
    """
    
    UsdModelAPI is an API schema that provides an interface to a prim's
    model qualities, if it does, in fact, represent the root prim of a
    model.
    
    The first and foremost model quality is its *kind*, i.e. the metadata
    that establishes it as a model (See KindRegistry). UsdModelAPI
    provides various methods for setting and querying the prim's kind, as
    well as queries (also available on UsdPrim) for asking what category
    of model the prim is. See Kind and Model-ness.
    
    UsdModelAPI also provides access to a prim's assetInfo data. While any
    prim *can* host assetInfo, it is common that published (referenced)
    assets are packaged as models, therefore it is convenient to provide
    access to the one from the other.
    
    """
    class KindValidation(pxr.Tf.Tf_PyEnumWrapper):
        """
        
        Option for validating queries to a prim's kind metadata.
        
        IsKind()
        
        """
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
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> ModelAPI
        
        
        Return a UsdModelAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdModelAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetAssetIdentifier(*args, **kwargs):
        """
        
        GetAssetIdentifier(identifier) -> bool
        
        
        Returns the model's asset identifier as authored in the composed
        assetInfo dictionary.
        
        
        The asset identifier can be used to resolve the model's root layer via
        the asset resolver plugin.
        
        
        Parameters
        ----------
        identifier : AssetPath
        
        
        """
    @staticmethod
    def GetAssetInfo(*args, **kwargs):
        """
        
        GetAssetInfo(info) -> bool
        
        
        Returns the model's composed assetInfo dictionary.
        
        
        The asset info dictionary is used to annotate models with various data
        related to asset management. For example, asset name, identifier,
        version etc.
        
        The elements of this dictionary are composed element-wise, and are
        nestable.
        
        
        Parameters
        ----------
        info : VtDictionary
        
        
        """
    @staticmethod
    def GetAssetName(*args, **kwargs):
        """
        
        GetAssetName(assetName) -> bool
        
        
        Returns the model's asset name from the composed assetInfo dictionary.
        
        
        The asset name is the name of the asset, as would be used in a
        database query.
        
        
        Parameters
        ----------
        assetName : str
        
        
        """
    @staticmethod
    def GetAssetVersion(*args, **kwargs):
        """
        
        GetAssetVersion(version) -> bool
        
        
        Returns the model's resolved asset version.
        
        
        
        If you publish assets with an embedded version, then you may receive
        that version string. You may, however, cause your authoring tools to
        record the resolved version *at the time at which a reference to the
        asset was added to an aggregate*, at the referencing site. In such a
        pipeline, this API will always return that stronger opinion, even if
        the asset is republished with a newer version, and even though that
        newer version may be the one that is resolved when the UsdStage is
        opened.
        
        
        Parameters
        ----------
        version : str
        
        
        """
    @staticmethod
    def GetKind(*args, **kwargs):
        """
        
        GetKind(kind) -> bool
        
        
        Retrieve the authored ``kind`` for this prim.
        
        
        To test whether the returned ``kind`` matches a particular
        known"clientKind":
        
        .. code-block:: text
        
          TfToken kind;
          
          bool isClientKind = UsdModelAPI(prim).GetKind(&kind) and
                              KindRegistry::IsA(kind, clientKind);
        
        true if there was an authored kind that was successfully read,
        otherwise false.
        
        The Kind module for further details on how to use Kind for
        classification, and how to extend the taxonomy.
        
        
        Parameters
        ----------
        kind : str
        
        
        """
    @staticmethod
    def GetPayloadAssetDependencies(*args, **kwargs):
        """
        
        GetPayloadAssetDependencies(assetDeps) -> bool
        
        
        Returns the list of asset dependencies referenced inside the payload
        of the model.
        
        
        This typically contains identifiers of external assets that are
        referenced inside the model's payload. When the model is created, this
        list is compiled and set at the root of the model. This enables
        efficient dependency analysis without the need to include the model's
        payload.
        
        
        Parameters
        ----------
        assetDeps : VtArray[AssetPath]
        
        
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
    def IsGroup(*args, **kwargs):
        """
        
        IsGroup() -> bool
        
        
        Return true if this prim represents a model group, based on its kind
        metadata.
        
        
        
        """
    @staticmethod
    def IsKind(*args, **kwargs):
        """
        
        IsKind(baseKind, validation) -> bool
        
        
        Return true if the prim's kind metadata is or inherits from
        ``baseKind`` as defined by the Kind Registry.
        
        
        If ``validation`` is KindValidationModelHierarchy (the default), then
        this also ensures that if baseKind is a model, the prim conforms to
        the rules of model hierarchy, as defined by IsModel. If set to
        KindValidationNone, no additional validation is done.
        
        IsModel and IsGroup are preferrable to IsKind("model") as they are
        optimized for fast traversal.
        
        If a prim's model hierarchy is not valid, it is possible that that
        prim.IsModel() and prim.IsKind("model",
        Usd.ModelAPI.KindValidationNone) return different answers. (As a
        corallary, this is also true for for prim.IsGroup())
        
        
        Parameters
        ----------
        baseKind : str
        
        validation : KindValidation
        
        
        """
    @staticmethod
    def IsModel(*args, **kwargs):
        """
        
        IsModel() -> bool
        
        
        Return true if this prim represents a model, based on its kind
        metadata.
        
        
        
        """
    @staticmethod
    def SetAssetIdentifier(*args, **kwargs):
        """
        
        SetAssetIdentifier(identifier) -> None
        
        
        Sets the model's asset identifier to the given asset path,
        ``identifier`` .
        
        
        
        GetAssetIdentifier()
        
        
        Parameters
        ----------
        identifier : AssetPath
        
        
        """
    @staticmethod
    def SetAssetInfo(*args, **kwargs):
        """
        
        SetAssetInfo(info) -> None
        
        
        Sets the model's assetInfo dictionary to ``info`` in the current edit
        target.
        
        
        Parameters
        ----------
        info : VtDictionary
        
        
        """
    @staticmethod
    def SetAssetName(*args, **kwargs):
        """
        
        SetAssetName(assetName) -> None
        
        
        Sets the model's asset name to ``assetName`` .
        
        
        
        GetAssetName()
        
        
        Parameters
        ----------
        assetName : str
        
        
        """
    @staticmethod
    def SetAssetVersion(*args, **kwargs):
        """
        
        SetAssetVersion(version) -> None
        
        
        Sets the model's asset version string.
        
        
        
        GetAssetVersion()
        
        
        Parameters
        ----------
        version : str
        
        
        """
    @staticmethod
    def SetKind(*args, **kwargs):
        """
        
        SetKind(kind) -> bool
        
        
        Author a ``kind`` for this prim, at the current UsdEditTarget.
        
        
        
        true if ``kind`` was successully authored, otherwise false.
        
        
        Parameters
        ----------
        kind : str
        
        
        """
    @staticmethod
    def SetPayloadAssetDependencies(*args, **kwargs):
        """
        
        SetPayloadAssetDependencies(assetDeps) -> None
        
        
        Sets the list of external asset dependencies referenced inside the
        payload of a model.
        
        
        
        GetPayloadAssetDependencies()
        
        
        Parameters
        ----------
        assetDeps : VtArray[AssetPath]
        
        
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
        
        
        Construct a UsdModelAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdModelAPI::Get (prim.GetStage(), prim.GetPath()) for a
        *valid* ``prim`` , but will not immediately throw an error for an
        invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdModelAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdModelAPI (schemaObj.GetPrim()), as it
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
class Notice(Boost.Python.instance):
    """
    
    Container class for Usd notices
    
    """
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
        def GetFastUpdates(*args, **kwargs):
            ...
        @staticmethod
        def GetResyncedPaths(*args, **kwargs):
            ...
        @staticmethod
        def HasChangedFields(*args, **kwargs):
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
    """
    
    Base class for Usd scenegraph objects, providing common API.
    
    The commonality between the three types of scenegraph objects in Usd (
    UsdPrim, UsdAttribute, UsdRelationship) is that they can all have
    metadata. Other objects in the API ( UsdReferences, UsdVariantSets,
    etc.) simply *are* kinds of metadata.
    
    UsdObject 's API primarily provides schema for interacting with the
    metadata common to all the scenegraph objects, as well as generic
    access to metadata.
    
    section Usd_UsdObject_Lifetime Lifetime Management and Object Validity
    
    Every derived class of UsdObject supports explicit detection of object
    validity through an *explicit-bool* operator, so client code should
    always be able use objects safely, even across edits to the owning
    UsdStage. UsdObject classes also perform some level of validity
    checking upon every use, in order to facilitate debugging of unsafe
    code, although we reserve the right to activate that behavior only in
    debug builds, if it becomes compelling to do so for performance
    reasons. This per-use checking will cause a fatal error upon failing
    the inline validity check, with an error message describing the
    namespace location of the dereferenced object on its owning UsdStage.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ClearAssetInfo(*args, **kwargs):
        """
        
        ClearAssetInfo() -> None
        
        
        Clear the authored opinion for this object's assetInfo dictionary at
        the current EditTarget.
        
        
        Do nothing if there is no such authored opinion.
        
        
        
        """
    @staticmethod
    def ClearAssetInfoByKey(*args, **kwargs):
        """
        
        ClearAssetInfoByKey(keyPath) -> None
        
        
        Clear the authored opinion identified by ``keyPath`` in this object's
        assetInfo dictionary at the current EditTarget.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries. Do nothing if there is no such authored opinion.
        
        
        Parameters
        ----------
        keyPath : str
        
        
        """
    @staticmethod
    def ClearCustomData(*args, **kwargs):
        """
        
        ClearCustomData() -> None
        
        
        Clear the authored opinion for this object's customData dictionary at
        the current EditTarget.
        
        
        Do nothing if there is no such authored opinion.
        
        
        
        """
    @staticmethod
    def ClearCustomDataByKey(*args, **kwargs):
        """
        
        ClearCustomDataByKey(keyPath) -> None
        
        
        Clear the authored opinion identified by ``keyPath`` in this object's
        customData dictionary at the current EditTarget.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries. Do nothing if there is no such authored opinion.
        
        
        Parameters
        ----------
        keyPath : str
        
        
        """
    @staticmethod
    def ClearDocumentation(*args, **kwargs):
        """
        
        ClearDocumentation() -> bool
        
        
        Clears this object's documentation (metadata) in the current
        EditTarget (only).
        
        
        Returns true on success.
        
        
        
        """
    @staticmethod
    def ClearHidden(*args, **kwargs):
        """
        
        ClearHidden() -> bool
        
        
        Clears the opinion for"Hidden"at the current EditTarget.
        
        
        
        """
    @staticmethod
    def ClearMetadata(*args, **kwargs):
        """
        
        ClearMetadata(key) -> bool
        
        
        Clears the authored *key's* value at the current EditTarget, returning
        false on error.
        
        
        If no value is present, this method is a no-op and returns true. It is
        considered an error to call ClearMetadata when no spec is present for
        this UsdObject, i.e. if the object has no presence in the current
        UsdEditTarget.
        
        General Metadata in USD
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def ClearMetadataByDictKey(*args, **kwargs):
        """
        
        ClearMetadataByDictKey(key, keyPath) -> bool
        
        
        Clear any authored value identified by ``key`` and ``keyPath`` at the
        current EditTarget.
        
        
        The ``keyPath`` is a':'-separated path identifying a path in
        subdictionaries stored in the metadata field at ``key`` . Return true
        if the value is cleared successfully, false otherwise.
        
        Dictionary-valued Metadata
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        
        """
    @staticmethod
    def GetAllAuthoredMetadata(*args, **kwargs):
        """
        
        GetAllAuthoredMetadata() -> UsdMetadataValueMap
        
        
        Resolve and return all user-authored metadata on this object, sorted
        lexicographically.
        
        
        
        This method does not return field keys for composition arcs, such as
        references, inherits, payloads, sublayers, variants, or primChildren,
        nor does it return the default value or timeSamples.
        
        
        
        """
    @staticmethod
    def GetAllMetadata(*args, **kwargs):
        """
        
        GetAllMetadata() -> UsdMetadataValueMap
        
        
        Resolve and return all metadata (including both authored and fallback
        values) on this object, sorted lexicographically.
        
        
        
        This method does not return field keys for composition arcs, such as
        references, inherits, payloads, sublayers, variants, or primChildren,
        nor does it return the default value or timeSamples.
        
        
        
        """
    @staticmethod
    def GetAssetInfo(*args, **kwargs):
        """
        
        GetAssetInfo() -> VtDictionary
        
        
        Return this object's composed assetInfo dictionary.
        
        
        The asset info dictionary is used to annotate objects representing the
        root-prims of assets (generally organized as models) with various data
        related to asset management. For example, asset name, root layer
        identifier, asset version etc.
        
        The elements of this dictionary are composed element-wise, and are
        nestable.
        
        There is no means to query an assetInfo field's valuetype other than
        fetching the value and interrogating it.
        
        GetAssetInfoByKey()
        
        
        
        """
    @staticmethod
    def GetAssetInfoByKey(*args, **kwargs):
        """
        
        GetAssetInfoByKey(keyPath) -> VtValue
        
        
        Return the element identified by ``keyPath`` in this object's composed
        assetInfo dictionary.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries. This is in general more efficient than composing the
        entire assetInfo dictionary than pulling out one sub-element.
        
        
        Parameters
        ----------
        keyPath : str
        
        
        """
    @staticmethod
    def GetCustomData(*args, **kwargs):
        """
        
        GetCustomData() -> VtDictionary
        
        
        Return this object's composed customData dictionary.
        
        
        CustomData is"custom metadata", a place for applications and users to
        put uniform data that is entirely dynamic and subject to no schema
        known to Usd. Unlike metadata like'hidden','displayName'etc, which
        must be declared in code or a data file that is considered part of
        one's Usd distribution (e.g. a plugInfo.json file) to be used,
        customData keys and the datatypes of their corresponding values are ad
        hoc. No validation will ever be performed that values for the same key
        in different layers are of the same type - strongest simply wins.
        
        Dictionaries like customData are composed element-wise, and are
        nestable.
        
        There is no means to query a customData field's valuetype other than
        fetching the value and interrogating it.
        
        GetCustomDataByKey()
        
        
        
        """
    @staticmethod
    def GetCustomDataByKey(*args, **kwargs):
        """
        
        GetCustomDataByKey(keyPath) -> VtValue
        
        
        Return the element identified by ``keyPath`` in this object's composed
        customData dictionary.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries. This is in general more efficient than composing the
        entire customData dictionary and then pulling out one sub-element.
        
        
        Parameters
        ----------
        keyPath : str
        
        
        """
    @staticmethod
    def GetDescription(*args, **kwargs):
        """
        
        GetDescription() -> str
        
        
        Return a string that provides a brief summary description of the
        object.
        
        
        This method, along with IsValid() /bool_operator, is always safe to
        call on a possibly-expired object, and the description will specify
        whether the object is valid or expired, along with a few other bits of
        data.
        
        
        
        """
    @staticmethod
    def GetDocumentation(*args, **kwargs):
        """
        
        GetDocumentation() -> str
        
        
        Return this object's documentation (metadata).
        
        
        This returns the empty string if no documentation has been set.
        
        SetDocumentation()
        
        
        
        """
    @staticmethod
    def GetMetadata(*args, **kwargs):
        """
        
        GetMetadata(key, value) -> bool
        
        
        Resolve the requested metadatum named ``key`` into ``value`` ,
        returning true on success.
        
        
        
        false if ``key`` was not resolvable, or if ``value's`` type ``T``
        differed from that of the resolved metadatum.
        
        For any composition-related metadata, as enumerated in
        GetAllMetadata() , this method will return only the strongest opinion
        found, not applying the composition rules used by Pcp to process the
        data. For more processed/composed views of composition data, please
        refer to the specific interface classes, such as UsdReferences,
        UsdInherits, UsdVariantSets, etc.
        
        General Metadata in USD
        
        
        Parameters
        ----------
        key : str
        
        value : T
        
        
        
        ----------------------------------------------------------------------
        
        GetMetadata(key, value) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        Type-erased access.
        
        
        Parameters
        ----------
        key : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def GetMetadataByDictKey(*args, **kwargs):
        """
        
        GetMetadataByDictKey(key, keyPath, value) -> bool
        
        
        Resolve the requested dictionary sub-element ``keyPath`` of
        dictionary-valued metadatum named ``key`` into ``value`` , returning
        true on success.
        
        
        If you know you neeed just a small number of elements from a
        dictionary, accessing them element-wise using this method can be much
        less expensive than fetching the entire dictionary with
        GetMetadata(key).
        
        false if ``key`` was not resolvable, or if ``value's`` type ``T``
        differed from that of the resolved metadatum. The ``keyPath`` is
        a':'-separated path addressing an element in subdictionaries.
        
        Dictionary-valued Metadata
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        value : T
        
        
        
        ----------------------------------------------------------------------
        
        GetMetadataByDictKey(key, keyPath, value) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def GetName(*args, **kwargs):
        """
        
        GetName() -> str
        
        
        Return the full name of this object, i.e.
        
        
        the last component of its SdfPath in namespace.
        
        This is equivalent to, but generally cheaper than, GetPath()
        .GetNameToken()
        
        
        
        """
    @staticmethod
    def GetNamespaceDelimiter(*args, **kwargs):
        """
        
        **classmethod** GetNamespaceDelimiter() -> char
        
        
        
        """
    @staticmethod
    def GetPath(*args, **kwargs):
        """
        
        GetPath() -> Path
        
        
        Return the complete scene path to this object on its UsdStage, which
        may (UsdPrim) or may not (all other subclasses) return a cached
        result.
        
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        Return this object if it is a prim, otherwise return this object's
        nearest owning prim.
        
        
        
        """
    @staticmethod
    def GetPrimPath(*args, **kwargs):
        """
        
        GetPrimPath() -> Path
        
        
        Return this object's path if this object is a prim, otherwise this
        object's nearest owning prim's path.
        
        
        Equivalent to GetPrim() . GetPath() .
        
        
        
        """
    @staticmethod
    def GetStage(*args, **kwargs):
        """
        
        GetStage() -> UsdStageWeak
        
        
        Return the stage that owns the object, and to whose state and lifetime
        this object's validity is tied.
        
        
        
        """
    @staticmethod
    def HasAssetInfo(*args, **kwargs):
        """
        
        HasAssetInfo() -> bool
        
        
        Return true if there are any authored or fallback opinions for this
        object's assetInfo dictionary, false otherwise.
        
        
        
        """
    @staticmethod
    def HasAssetInfoKey(*args, **kwargs):
        """
        
        HasAssetInfoKey(keyPath) -> bool
        
        
        Return true if there are any authored or fallback opinions for the
        element identified by ``keyPath`` in this object's assetInfo
        dictionary, false otherwise.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries.
        
        
        Parameters
        ----------
        keyPath : str
        
        
        """
    @staticmethod
    def HasAuthoredAssetInfo(*args, **kwargs):
        """
        
        HasAuthoredAssetInfo() -> bool
        
        
        Return true if there are any authored opinions (excluding fallback)
        for this object's assetInfo dictionary, false otherwise.
        
        
        
        """
    @staticmethod
    def HasAuthoredAssetInfoKey(*args, **kwargs):
        """
        
        HasAuthoredAssetInfoKey(keyPath) -> bool
        
        
        Return true if there are any authored opinions (excluding fallback)
        for the element identified by ``keyPath`` in this object's assetInfo
        dictionary, false otherwise.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries.
        
        
        Parameters
        ----------
        keyPath : str
        
        
        """
    @staticmethod
    def HasAuthoredCustomData(*args, **kwargs):
        """
        
        HasAuthoredCustomData() -> bool
        
        
        Return true if there are any authored opinions (excluding fallback)
        for this object's customData dictionary, false otherwise.
        
        
        
        """
    @staticmethod
    def HasAuthoredCustomDataKey(*args, **kwargs):
        """
        
        HasAuthoredCustomDataKey(keyPath) -> bool
        
        
        Return true if there are any authored opinions (excluding fallback)
        for the element identified by ``keyPath`` in this object's customData
        dictionary, false otherwise.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries.
        
        
        Parameters
        ----------
        keyPath : str
        
        
        """
    @staticmethod
    def HasAuthoredDocumentation(*args, **kwargs):
        """
        
        HasAuthoredDocumentation() -> bool
        
        
        Returns true if documentation was explicitly authored and
        GetMetadata() will return a meaningful value for documentation.
        
        
        
        
        
        """
    @staticmethod
    def HasAuthoredHidden(*args, **kwargs):
        """
        
        HasAuthoredHidden() -> bool
        
        
        Returns true if hidden was explicitly authored and GetMetadata() will
        return a meaningful value for Hidden.
        
        
        Note that IsHidden returns a fallback value (false) when hidden is not
        authored.
        
        
        
        """
    @staticmethod
    def HasAuthoredMetadata(*args, **kwargs):
        """
        
        HasAuthoredMetadata(key) -> bool
        
        
        Returns true if the *key* has an authored value, false if no value was
        authored or the only value available is a prim's metadata fallback.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def HasAuthoredMetadataDictKey(*args, **kwargs):
        """
        
        HasAuthoredMetadataDictKey(key, keyPath) -> bool
        
        
        Return true if there exists any authored opinion (excluding fallbacks)
        for ``key`` and ``keyPath`` .
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at ``key`` .
        
        Dictionary-valued Metadata
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        
        """
    @staticmethod
    def HasCustomData(*args, **kwargs):
        """
        
        HasCustomData() -> bool
        
        
        Return true if there are any authored or fallback opinions for this
        object's customData dictionary, false otherwise.
        
        
        
        """
    @staticmethod
    def HasCustomDataKey(*args, **kwargs):
        """
        
        HasCustomDataKey(keyPath) -> bool
        
        
        Return true if there are any authored or fallback opinions for the
        element identified by ``keyPath`` in this object's customData
        dictionary, false otherwise.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries.
        
        
        Parameters
        ----------
        keyPath : str
        
        
        """
    @staticmethod
    def HasMetadata(*args, **kwargs):
        """
        
        HasMetadata(key) -> bool
        
        
        Returns true if the *key* has a meaningful value, that is, if
        GetMetadata() will provide a value, either because it was authored or
        because a prim's metadata fallback will be provided.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def HasMetadataDictKey(*args, **kwargs):
        """
        
        HasMetadataDictKey(key, keyPath) -> bool
        
        
        Return true if there exists any authored or fallback opinion for
        ``key`` and ``keyPath`` .
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at ``key`` .
        
        Dictionary-valued Metadata
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        
        """
    @staticmethod
    def IsHidden(*args, **kwargs):
        """
        
        IsHidden() -> bool
        
        
        Gets the value of the'hidden'metadata field, false if not authored.
        
        
        When an object is marked as hidden, it is an indicator to clients who
        generically display objects (such as GUI widgets) that this object
        should not be included, unless explicitly asked for. Although this is
        just a hint and thus up to each application to interpret, we use it
        primarily as a way of simplifying hierarchy displays, by hiding *only*
        the representation of the object itself, *not* its subtree,
        instead"pulling up"everything below it one level in the hierarchical
        nesting.
        
        Note again that this is a hint for UI only - it should not be
        interpreted by any renderer as making a prim invisible to drawing.
        
        
        
        """
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        IsValid() -> bool
        
        
        Return true if this is a valid object, false otherwise.
        
        
        
        """
    @staticmethod
    def SetAssetInfo(*args, **kwargs):
        """
        
        SetAssetInfo(customData) -> None
        
        
        Author this object's assetInfo dictionary to ``assetInfo`` at the
        current EditTarget.
        
        
        Parameters
        ----------
        customData : VtDictionary
        
        
        """
    @staticmethod
    def SetAssetInfoByKey(*args, **kwargs):
        """
        
        SetAssetInfoByKey(keyPath, value) -> None
        
        
        Author the element identified by ``keyPath`` in this object's
        assetInfo dictionary at the current EditTarget.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries.
        
        
        Parameters
        ----------
        keyPath : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def SetCustomData(*args, **kwargs):
        """
        
        SetCustomData(customData) -> None
        
        
        Author this object's customData dictionary to ``customData`` at the
        current EditTarget.
        
        
        Parameters
        ----------
        customData : VtDictionary
        
        
        """
    @staticmethod
    def SetCustomDataByKey(*args, **kwargs):
        """
        
        SetCustomDataByKey(keyPath, value) -> None
        
        
        Author the element identified by ``keyPath`` in this object's
        customData dictionary at the current EditTarget.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries.
        
        
        Parameters
        ----------
        keyPath : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def SetDocumentation(*args, **kwargs):
        """
        
        SetDocumentation(doc) -> bool
        
        
        Sets this object's documentation (metadata). Returns true on success.
        
        
        Parameters
        ----------
        doc : str
        
        
        """
    @staticmethod
    def SetHidden(*args, **kwargs):
        """
        
        SetHidden(hidden) -> bool
        
        
        Sets the value of the'hidden'metadata field.
        
        
        See IsHidden() for details.
        
        
        Parameters
        ----------
        hidden : bool
        
        
        """
    @staticmethod
    def SetMetadata(*args, **kwargs):
        """
        
        SetMetadata(key, value) -> bool
        
        
        Set metadatum ``key's`` value to ``value`` .
        
        
        
        false if ``value's`` type does not match the schema type for ``key`` .
        
        General Metadata in USD
        
        
        Parameters
        ----------
        key : str
        
        value : T
        
        
        
        ----------------------------------------------------------------------
        
        SetMetadata(key, value) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        key : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def SetMetadataByDictKey(*args, **kwargs):
        """
        
        SetMetadataByDictKey(key, keyPath, value) -> bool
        
        
        Author ``value`` to the field identified by ``key`` and ``keyPath`` at
        the current EditTarget.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at ``key`` . Return true
        if the value is authored successfully, false otherwise.
        
        Dictionary-valued Metadata
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        value : T
        
        
        
        ----------------------------------------------------------------------
        
        SetMetadataByDictKey(key, keyPath, value) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        value : VtValue
        
        
        """
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
        """
        
        __init__()
        
        
        Default constructor produces an invalid object.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : _Null[Derived]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim, proxyPrimPath)
        
        
        Parameters
        ----------
        prim : Usd_PrimData
        
        proxyPrimPath : Path
        
        
        
        ----------------------------------------------------------------------
        
        __init__(objType, prim, proxyPrimPath, propName)
        
        
        Parameters
        ----------
        objType : UsdObjType
        
        prim : Usd_PrimData
        
        proxyPrimPath : Path
        
        propName : str
        
        
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Payloads(Boost.Python.instance):
    """
    
    UsdPayloads provides an interface to authoring and introspecting
    payloads. Payloads behave the same as Usd references except that
    payloads can be optionally loaded.
    
    """
    @staticmethod
    def AddInternalPayload(*args, **kwargs):
        """
        
        AddInternalPayload(primPath, layerOffset, position) -> bool
        
        
        Add an internal payload to the specified prim.
        
        
        
        Internal Payloads
        
        
        Parameters
        ----------
        primPath : Path
        
        layerOffset : LayerOffset
        
        position : ListPosition
        
        
        """
    @staticmethod
    def AddPayload(*args, **kwargs):
        """
        
        AddPayload(payload, position) -> bool
        
        
        Adds a payload to the payload listOp at the current EditTarget, in the
        position specified by ``position`` .
        
        
        
        Why adding references may fail for explanation of expectations on
        ``payload`` and what return values and errors to expect, and ListOps
        and List Editing for details on list editing and composition of
        listOps.
        
        
        Parameters
        ----------
        payload : Payload
        
        position : ListPosition
        
        
        
        ----------------------------------------------------------------------
        
        AddPayload(identifier, primPath, layerOffset, position) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        identifier : str
        
        primPath : Path
        
        layerOffset : LayerOffset
        
        position : ListPosition
        
        
        
        ----------------------------------------------------------------------
        
        AddPayload(identifier, layerOffset, position) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        
        Payloads Without Prim Paths
        
        
        Parameters
        ----------
        identifier : str
        
        layerOffset : LayerOffset
        
        position : ListPosition
        
        
        """
    @staticmethod
    def ClearPayloads(*args, **kwargs):
        """
        
        ClearPayloads() -> bool
        
        
        Removes the authored payload listOp edits at the current EditTarget.
        
        
        The same caveats for Remove() apply to Clear(). In fact, Clear() may
        actually increase the number of composed payloads, if the listOp being
        cleared contained the"remove"operator.
        
        ListOps and List Editing
        
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        Return the prim this object is bound to.
        
        
        
        
        ----------------------------------------------------------------------
        
        GetPrim() -> Prim
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        
        """
    @staticmethod
    def RemovePayload(*args, **kwargs):
        """
        
        RemovePayload(ref) -> bool
        
        
        Removes the specified payload from the payloads listOp at the current
        EditTarget.
        
        
        This does not necessarily eliminate the payload completely, as it may
        be added or set in another layer in the same LayerStack as the current
        EditTarget.
        
        ListOps and List Editing
        
        
        Parameters
        ----------
        ref : Payload
        
        
        """
    @staticmethod
    def SetPayloads(*args, **kwargs):
        """
        
        SetPayloads(items) -> bool
        
        
        Explicitly set the payloads, potentially blocking weaker opinions that
        add or remove items.
        
        
        
        Why adding payloads may fail for explanation of expectations on
        ``items`` and what return values and errors to expect, and ListOps and
        List Editing for details on list editing and composition of listOps.
        
        
        Parameters
        ----------
        items : list[Payload]
        
        
        """
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
    """
    
    UsdPrim is the sole persistent scenegraph object on a UsdStage, and is
    the embodiment of a"Prim"as described in the *Universal Scene
    Description Composition Compendium*
    
    A UsdPrim is the principal container of other types of scene
    description. It provides API for accessing and creating all of the
    contained kinds of scene description, which include:
    
       - UsdVariantSets - all VariantSets on the prim ( GetVariantSets() ,
         GetVariantSet() )
    
       - UsdReferences - all references on the prim ( GetReferences() )
    
       - UsdInherits - all inherits on the prim ( GetInherits() )
    
       - UsdSpecializes - all specializes on the prim ( GetSpecializes() )
         As well as access to the API objects for properties contained within
         the prim - UsdPrim as well as all of the following classes are
         subclasses of UsdObject :
    
       - UsdProperty - generic access to all attributes and relationships.
         A UsdProperty can be queried and cast to a UsdAttribute or
         UsdRelationship using UsdObject::Is<>() and UsdObject::As<>() . (
         GetPropertyNames() , GetProperties() , GetPropertiesInNamespace() ,
         GetPropertyOrder() , SetPropertyOrder() )
    
       - UsdAttribute - access to default and timesampled attribute
         values, as well as value resolution information, and attribute-
         specific metadata ( CreateAttribute() , GetAttribute() ,
         GetAttributes() , HasAttribute() )
    
       - UsdRelationship - access to authoring and resolving relationships
         to other prims and properties ( CreateRelationship() ,
         GetRelationship() , GetRelationships() , HasRelationship() )
         UsdPrim also provides access to iteration through its prim children,
         optionally making use of the prim predicates facility ( GetChildren()
         , GetAllChildren() , GetFilteredChildren() ).
    
    Management
    ==========
    
    Clients acquire UsdPrim objects, which act like weak/guarded pointers
    to persistent objects owned and managed by their originating UsdStage.
    We provide the following guarantees for a UsdPrim acquired via
    UsdStage::GetPrimAtPath() or UsdStage::OverridePrim() or
    UsdStage::DefinePrim() :
    
       - As long as no further mutations to the structure of the UsdStage
         are made, the UsdPrim will still be valid. Loading and Unloading are
         considered structural mutations.
    
       - When the UsdStage 's structure *is* mutated, the thread
         performing the mutation will receive a UsdNotice::ObjectsChanged
         notice after the stage has been reconfigured, which provides details
         as to what prims may have been created or destroyed, and what prims
         may simply have changed in some structural way.
         Prim access in"reader"threads should be limited to GetPrimAtPath() ,
         which will never cause a mutation to the Stage or its layers.
    
    Please refer to UsdNotice for a listing of the events that could cause
    UsdNotice::ObjectsChanged to be emitted.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def AddAppliedSchema(*args, **kwargs):
        """
        
        AddAppliedSchema(appliedSchemaName) -> bool
        
        
        Adds the applied API schema name token ``appliedSchemaName`` to the
        *apiSchemas* metadata for this prim at the current edit target.
        
        
        For multiple-apply schemas the name token should include the instance
        name for the applied schema, for example'CollectionAPI:plasticStuff'.
        
        The name will only be added if the list operation at the edit target
        does not already have this applied schema in its explicit, prepended,
        or appended lists and is always added to the end of either the
        prepended or explicit items.
        
        Returns true upon success or if the API schema is already applied in
        the current edit target.
        
        An error is issued and false returned for any of the following
        conditions:
        
           - this prim is not a valid prim for editing
        
           - this prim is valid, but cannot be reached or overridden in the
             current edit target
        
           - the schema name cannot be added to the apiSchemas listOp metadata
             Unlike ApplyAPI this method does not require that the name token
             refer to a valid API schema type. ApplyAPI is the preferred method for
             applying valid API schemas.
        
        
        Parameters
        ----------
        appliedSchemaName : str
        
        
        """
    @staticmethod
    def ApplyAPI(*args, **kwargs):
        """
        
        ApplyAPI() -> bool
        
        
        Applies a **single-apply** API schema with the given C++
        type'SchemaType'to this prim in the current edit target.
        
        
        This information is stored by adding the API schema's name token to
        the token-valued, listOp metadata *apiSchemas* on this prim.
        
        Returns true upon success or if the API schema is already applied in
        the current edit target.
        
        An error is issued and false returned for any of the following
        conditions:
        
           - this prim is not a valid prim for editing
        
           - this prim is valid, but cannot be reached or overridden in the
             current edit target
        
           - the schema name cannot be added to the apiSchemas listOp metadata
        
        
        
        
        
        ----------------------------------------------------------------------
        
        ApplyAPI(schemaType) -> bool
        
        
        Non-templated overload of the templated ApplyAPI above.
        
        
        This function behaves exactly like the templated ApplyAPI  except for
        the runtime schemaType validation which happens at compile time in the
        templated version. This method is provided for python clients. Use of
        the templated ApplyAPI is preferred.
        
        
        Parameters
        ----------
        schemaType : Type
        
        
        
        ----------------------------------------------------------------------
        
        ApplyAPI(instanceName) -> bool
        
        
        Applies a **multiple-apply** API schema with the given C++
        type'SchemaType'and instance name ``instanceName`` to this prim in the
        current edit target.
        
        
        This information is stored in the token-valued, listOp metadata
        *apiSchemas* on this prim. For example, if SchemaType is'
        UsdCollectionAPI 'and ``instanceName`` is'plasticStuff', the
        name'CollectionAPI:plasticStuff'is added to the'apiSchemas'listOp
        metadata.
        
        Returns true upon success or if the API schema is already applied with
        this ``instanceName`` in the current edit target.
        
        An error is issued and false returned for any of the following
        conditions:
        
           - ``instanceName`` is empty
        
           - this prim is not a valid prim for editing
        
           - this prim is valid, but cannot be reached or overridden in the
             current edit target
        
           - the schema name cannot be added to the apiSchemas listOp metadata
        
        
        
        Parameters
        ----------
        instanceName : str
        
        
        
        ----------------------------------------------------------------------
        
        ApplyAPI(schemaType, instanceName) -> bool
        
        
        Non-templated overload of the templated ApplyAPI above.
        
        
        This function behaves exactly like the templated ApplyAPI  except for
        the runtime schemaType validation which happens at compile time in the
        templated version. This method is provided for python clients. Use of
        the templated ApplyAPI is preferred.
        
        
        Parameters
        ----------
        schemaType : Type
        
        instanceName : str
        
        
        """
    @staticmethod
    def CanApplyAPI(*args, **kwargs):
        """
        
        CanApplyAPI(whyNot) -> bool
        
        
        }@
        
        
        Returns whether a **single-apply** API schema with the given C++
        type'SchemaType'can be applied to this prim. If the return value is
        false, and ``whyNot`` is provided, the reason the schema cannot be
        applied is written to whyNot.
        
        Whether the schema can be applied is determined by the schema type
        definition which may specify that the API schema can only be applied
        to certain prim types.
        
        The return value of this function only indicates whether it would be
        valid to apply this schema to the prim. It has no bearing on whether
        calling ApplyAPI will be successful or not.
        
        
        Parameters
        ----------
        whyNot : str
        
        
        
        ----------------------------------------------------------------------
        
        CanApplyAPI(schemaType, whyNot) -> bool
        
        
        Non-templated overload of the templated CanApplyAPI above.
        
        
        This function behaves exactly like the templated CanApplyAPI  except
        for the runtime schemaType validation which happens at compile time in
        the templated version. This method is provided for python clients. Use
        of the templated CanApplyAPI is preferred.
        
        
        Parameters
        ----------
        schemaType : Type
        
        whyNot : str
        
        
        
        ----------------------------------------------------------------------
        
        CanApplyAPI(instanceName, whyNot) -> bool
        
        
        Returns whether a **multiple-apply** API schema with the given C++
        type'SchemaType'can be applied to this prim with the given
        ``instanceName`` .
        
        
        If the return value is false, and ``whyNot`` is provided, the reason
        the schema cannot be applied is written to whyNot.
        
        Whether the schema can be applied is determined by the schema type
        definition which may specify that the API schema can only be applied
        to certain prim types. It also determines whether the instance name is
        a valid instance name for the multiple apply schema.
        
        The return value of this function only indicates whether it would be
        valid to apply this schema to the prim. It has no bearing on whether
        calling ApplyAPI will be successful or not.
        
        
        Parameters
        ----------
        instanceName : str
        
        whyNot : str
        
        
        
        ----------------------------------------------------------------------
        
        CanApplyAPI(schemaType, instanceName, whyNot) -> bool
        
        
        Non-templated overload of the templated CanApplyAPI above.
        
        
        This function behaves exactly like the templated CanApplyAPI  except
        for the runtime schemaType validation which happens at compile time in
        the templated version. This method is provided for python clients. Use
        of the templated CanApplyAPI is preferred.
        
        
        Parameters
        ----------
        schemaType : Type
        
        instanceName : str
        
        whyNot : str
        
        
        """
    @staticmethod
    def ClearActive(*args, **kwargs):
        """
        
        ClearActive() -> bool
        
        
        Remove the authored'active'opinion at the current EditTarget.
        
        
        Do nothing if there is no authored opinion.
        
        See How"active"Affects Prims on a UsdStage for the effects of
        activating or deactivating a prim.
        
        
        
        """
    @staticmethod
    def ClearChildrenReorder(*args, **kwargs):
        """
        
        ClearChildrenReorder() -> None
        
        
        Remove the opinion for the metadata used to reorder children of this
        prim at the current EditTarget.
        
        
        
        """
    @staticmethod
    def ClearInstanceable(*args, **kwargs):
        """
        
        ClearInstanceable() -> bool
        
        
        Remove the authored'instanceable'opinion at the current EditTarget.
        
        
        Do nothing if there is no authored opinion.
        
        
        
        """
    @staticmethod
    def ClearPayload(*args, **kwargs):
        """
        
        ClearPayload() -> bool
        
        
        Deprecated
        
        Clears the payload at the current EditTarget for this prim. Return
        false if the payload could not be cleared.
        
        
        
        """
    @staticmethod
    def ClearPropertyOrder(*args, **kwargs):
        """
        
        ClearPropertyOrder() -> None
        
        
        Remove the opinion for propertyOrder metadata on this prim at the
        current EditTarget.
        
        
        
        """
    @staticmethod
    def ClearTypeName(*args, **kwargs):
        """
        
        ClearTypeName() -> bool
        
        
        Clear the opinion for this Prim's typeName at the current edit target.
        
        
        
        """
    @staticmethod
    def ComputeExpandedPrimIndex(*args, **kwargs):
        """
        
        ComputeExpandedPrimIndex() -> PrimIndex
        
        
        Compute the prim index containing all sites that could contribute
        opinions to this prim.
        
        
        This function is similar to UsdPrim::GetPrimIndex. However, the
        returned prim index includes all sites that could possibly contribute
        opinions to this prim, not just the sites that currently do so. This
        is useful in certain situations; for example, this could be used to
        generate a list of sites where clients could make edits to affect this
        prim, or for debugging purposes.
        
        This function may be relatively slow, since it will recompute the prim
        index on every call. Clients should prefer UsdPrim::GetPrimIndex
        unless the additional site information is truly needed.
        
        
        
        """
    @staticmethod
    def CreateAttribute(*args, **kwargs):
        """
        
        CreateAttribute(name, typeName, custom, variability) -> Attribute
        
        
        Author scene description for the attribute named *attrName* at the
        current EditTarget if none already exists.
        
        
        Return a valid attribute if scene description was successfully
        authored or if it already existed, return invalid attribute otherwise.
        Note that the supplied *typeName* and *custom* arguments are only used
        in one specific case. See below for details.
        
        Suggested use:
        
        .. code-block:: text
        
          if (UsdAttribute myAttr = prim.CreateAttribute(\\.\\.\\.)) {
             // success. 
          }
        
        To call this, GetPrim() must return a valid prim.
        
           - If a spec for this attribute already exists at the current edit
             target, do nothing.
        
           - If a spec for *attrName* of a different spec type (e.g. a
             relationship) exists at the current EditTarget, issue an error.
        
           - If *name* refers to a builtin attribute according to the prim's
             definition, author an attribute spec with required metadata from the
             definition.
        
           - If *name* refers to a builtin relationship, issue an error.
        
           - If there exists an absolute strongest authored attribute spec for
             *attrName*, author an attribute spec at the current EditTarget by
             copying required metadata from that strongest spec.
        
           - If there exists an absolute strongest authored relationship spec
             for *attrName*, issue an error.
        
           - Otherwise author an attribute spec at the current EditTarget
             using the provided *typeName* and *custom* for the required metadata
             fields. Note that these supplied arguments are only ever used in this
             particular circumstance, in all other cases they are ignored.
        
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        custom : bool
        
        variability : Variability
        
        
        
        ----------------------------------------------------------------------
        
        CreateAttribute(name, typeName, variability) -> Attribute
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Create a custom attribute with ``name`` , ``typeName`` and
        ``variability`` .
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        variability : Variability
        
        
        
        ----------------------------------------------------------------------
        
        CreateAttribute(nameElts, typeName, custom, variability) -> Attribute
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This overload of CreateAttribute() accepts a vector of name components
        used to construct a *namespaced* property name.
        
        
        For details, see Names, Namespace Ordering, and Property Namespaces
        
        
        Parameters
        ----------
        nameElts : list[str]
        
        typeName : ValueTypeName
        
        custom : bool
        
        variability : Variability
        
        
        
        ----------------------------------------------------------------------
        
        CreateAttribute(nameElts, typeName, variability) -> Attribute
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Create a custom attribute with ``nameElts`` , ``typeName`` , and
        ``variability`` .
        
        
        Parameters
        ----------
        nameElts : list[str]
        
        typeName : ValueTypeName
        
        variability : Variability
        
        
        """
    @staticmethod
    def CreateRelationship(*args, **kwargs):
        """
        
        CreateRelationship(relName, custom) -> Relationship
        
        
        Author scene description for the relationship named *relName* at the
        current EditTarget if none already exists.
        
        
        Return a valid relationship if scene description was successfully
        authored or if it already existed, return an invalid relationship
        otherwise.
        
        Suggested use:
        
        .. code-block:: text
        
          if (UsdRelationship myRel = prim.CreateRelationship(\\.\\.\\.)) {
             // success. 
          }
        
        To call this, GetPrim() must return a valid prim.
        
           - If a spec for this relationship already exists at the current
             edit target, do nothing.
        
           - If a spec for *relName* of a different spec type (e.g. an
             attribute) exists at the current EditTarget, issue an error.
        
           - If *name* refers to a builtin relationship according to the
             prim's definition, author a relationship spec with required metadata
             from the definition.
        
           - If *name* refers to a builtin attribute, issue an error.
        
           - If there exists an absolute strongest authored relationship spec
             for *relName*, author a relationship spec at the current EditTarget by
             copying required metadata from that strongest spec.
        
           - If there exists an absolute strongest authored attribute spec for
             *relName*, issue an error.
        
           - Otherwise author a uniform relationship spec at the current
             EditTarget, honoring ``custom`` .
        
        
        
        Parameters
        ----------
        relName : str
        
        custom : bool
        
        
        
        ----------------------------------------------------------------------
        
        CreateRelationship(nameElts, custom) -> Relationship
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This overload of CreateRelationship() accepts a vector of name
        components used to construct a *namespaced* property name.
        
        
        For details, see Names, Namespace Ordering, and Property Namespaces
        
        
        Parameters
        ----------
        nameElts : list[str]
        
        custom : bool
        
        
        """
    @staticmethod
    def FindAllAttributeConnectionPaths(*args, **kwargs):
        """
        
        FindAllAttributeConnectionPaths(pred, recurseOnSources) -> list[Path]
        
        
        Search the prim subtree rooted at this prim for attributes for which
        ``predicate`` returns true, collect their connection source paths and
        return them in an arbitrary order.
        
        
        If ``recurseOnSources`` is true, act as if this function was invoked
        on the connected prims and owning prims of connected properties also
        and return the union.
        
        
        Parameters
        ----------
        pred : function[bool( Attribute )]
        
        recurseOnSources : bool
        
        
        """
    @staticmethod
    def FindAllRelationshipTargetPaths(*args, **kwargs):
        """
        
        FindAllRelationshipTargetPaths(pred, recurseOnTargets) -> list[Path]
        
        
        Search the prim subtree rooted at this prim for relationships for
        which ``predicate`` returns true, collect their target paths and
        return them in an arbitrary order.
        
        
        If ``recurseOnTargets`` is true, act as if this function was invoked
        on the targeted prims and owning prims of targeted properties also
        (but not of forwarding relationships) and return the union.
        
        
        Parameters
        ----------
        pred : function[bool( Relationship )]
        
        recurseOnTargets : bool
        
        
        """
    @staticmethod
    def GetAllChildren(*args, **kwargs):
        """
        
        GetAllChildren() -> SiblingRange
        
        
        Return all this prim's children as an iterable range.
        
        
        
        """
    @staticmethod
    def GetAllChildrenNames(*args, **kwargs):
        """
        
        GetAllChildrenNames() -> list[str]
        
        
        Return the names of the child prims in the order they appear when
        iterating over GetAllChildren.
        
        
        
        
        
        """
    @staticmethod
    def GetAppliedSchemas(*args, **kwargs):
        """
        
        GetAppliedSchemas() -> list[str]
        
        
        Return a vector containing the names of API schemas which have been
        applied to this prim.
        
        
        This includes both the authored API schemas applied using the Apply()
        method on the particular schema class as well as any built-in API
        schemas that are automatically included through the prim type's prim
        definition. To get only the authored API schemas use GetPrimTypeInfo
        instead.
        
        
        
        """
    @staticmethod
    def GetAttribute(*args, **kwargs):
        """
        
        GetAttribute(attrName) -> Attribute
        
        
        Return a UsdAttribute with the name *attrName*.
        
        
        The attribute returned may or may not **actually** exist so it must be
        checked for validity. Suggested use:
        
        .. code-block:: text
        
          if (UsdAttribute myAttr = prim.GetAttribute("myAttr")) {
             // myAttr is safe to use. 
             // Edits to the owning stage requires subsequent validation.
          } else {
             // myAttr was not defined/authored
          }
        
        
        
        Parameters
        ----------
        attrName : str
        
        
        """
    @staticmethod
    def GetAttributeAtPath(*args, **kwargs):
        """
        
        GetAttributeAtPath(path) -> Attribute
        
        
        Returns the attribute at ``path`` on the same stage as this prim.
        
        
        If path is relative, it will be anchored to the path of this prim.
        
        There is no guarantee that this method returns an attribute on this
        prim. This is only guaranteed if path is a purely relative property
        path.
        
        GetAttribute(const TfToken&) const
        
        UsdStage::GetAttributeAtPath(const SdfPath&) const
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetAttributes(*args, **kwargs):
        """
        
        GetAttributes() -> list[Attribute]
        
        
        Like GetProperties() , but exclude all relationships from the result.
        
        
        
        """
    @staticmethod
    def GetAuthoredAttributes(*args, **kwargs):
        """
        
        GetAuthoredAttributes() -> list[Attribute]
        
        
        Like GetAttributes() , but exclude attributes without authored scene
        description from the result.
        
        
        See UsdProperty::IsAuthored() .
        
        
        
        """
    @staticmethod
    def GetAuthoredProperties(*args, **kwargs):
        """
        
        GetAuthoredProperties(predicate) -> list[Property]
        
        
        Return this prim's properties (attributes and relationships) that have
        authored scene description, ordered by name according to the strongest
        propertyOrder statement in scene description if one exists, otherwise
        ordered according to TfDictionaryLessThan.
        
        
        If a valid ``predicate`` is passed in, then only authored properties
        whose names pass the predicate are included in the result. This is
        useful if the client is interested only in a subset of authored
        properties on the prim. For example, only the ones in a given
        namespace or only the ones needed to compute a value.
        
        GetProperties()
        
        UsdProperty::IsAuthored()
        
        
        Parameters
        ----------
        predicate : PropertyPredicateFunc
        
        
        """
    @staticmethod
    def GetAuthoredPropertiesInNamespace(*args, **kwargs):
        """
        
        GetAuthoredPropertiesInNamespace(namespaces) -> list[Property]
        
        
        Like GetPropertiesInNamespace() , but exclude properties that do not
        have authored scene description from the result.
        
        
        See UsdProperty::IsAuthored() .
        
        For details of namespaced properties, see Names, Namespace Ordering,
        and Property Namespaces
        
        
        Parameters
        ----------
        namespaces : list[str]
        
        
        
        ----------------------------------------------------------------------
        
        GetAuthoredPropertiesInNamespace(namespaces) -> list[Property]
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        ``namespaces`` must be an already-concatenated ordered set of
        namespaces, and may or may not terminate with the namespace-separator
        character.
        
        
        If ``namespaces`` is empty, this method is equivalent to
        GetAuthoredProperties() .
        
        
        Parameters
        ----------
        namespaces : str
        
        
        """
    @staticmethod
    def GetAuthoredPropertyNames(*args, **kwargs):
        """
        
        GetAuthoredPropertyNames(predicate) -> list[str]
        
        
        Return this prim's property names (attributes and relationships) that
        have authored scene description, ordered according to the strongest
        propertyOrder statement in scene description if one exists, otherwise
        ordered according to TfDictionaryLessThan.
        
        
        If a valid ``predicate`` is passed in, then only the authored
        properties whose names pass the predicate are included in the result.
        This is useful if the client is interested only in a subset of
        authored properties on the prim. For example, only the ones in a given
        namespace or only the ones needed to compute a value.
        
        GetPropertyNames()
        
        UsdProperty::IsAuthored()
        
        
        Parameters
        ----------
        predicate : PropertyPredicateFunc
        
        
        """
    @staticmethod
    def GetAuthoredRelationships(*args, **kwargs):
        """
        
        GetAuthoredRelationships() -> list[Relationship]
        
        
        Like GetRelationships() , but exclude relationships without authored
        scene description from the result.
        
        
        See UsdProperty::IsAuthored() .
        
        
        
        """
    @staticmethod
    def GetChild(*args, **kwargs):
        """
        
        GetChild(name) -> Prim
        
        
        Return this prim's direct child named ``name`` if it has one,
        otherwise return an invalid UsdPrim.
        
        
        Equivalent to:
        
        .. code-block:: text
        
          prim.GetStage()->GetPrimAtPath(prim.GetPath().AppendChild(name))
        
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetChildren(*args, **kwargs):
        """
        
        GetChildren() -> SiblingRange
        
        
        Return this prim's active, loaded, defined, non-abstract children as
        an iterable range.
        
        
        Equivalent to:
        
        .. code-block:: text
        
          GetFilteredChildren(UsdPrimDefaultPredicate)
        
        See Prim predicate flags and UsdPrimDefaultPredicate for more
        information.
        
        
        
        """
    @staticmethod
    def GetChildrenNames(*args, **kwargs):
        """
        
        GetChildrenNames() -> list[str]
        
        
        Return the names of the child prims in the order they appear when
        iterating over GetChildren.
        
        
        
        
        
        """
    @staticmethod
    def GetChildrenReorder(*args, **kwargs):
        """
        
        GetChildrenReorder() -> list[str]
        
        
        Return the strongest opinion for the metadata used to reorder children
        of this prim.
        
        
        Due to how reordering of prim children is composed, this value cannot
        be relied on to get the actual order of the prim's children. Use
        GetChidrenNames, GetAllChildrenNames, GetFilteredChildrenNames to get
        the true child order if needed.
        
        
        
        """
    @staticmethod
    def GetFilteredChildren(*args, **kwargs):
        """
        
        GetFilteredChildren(predicate) -> SiblingRange
        
        
        Return a subset of all of this prim's children filtered by
        ``predicate`` as an iterable range.
        
        
        The ``predicate`` is generated by combining a series of prim flag
        terms with either&&or || and !.
        
        Example usage:
        
        .. code-block:: text
        
          // Get all active model children.
          GetFilteredChildren(UsdPrimIsActive && UsdPrimIsModel);
          
          // Get all model children that pass the default predicate.
          GetFilteredChildren(UsdPrimDefaultPredicate && UsdPrimIsModel);
        
        If this prim is an instance, no children will be returned unless
        UsdTraverseInstanceProxies is used to allow instance proxies to be
        returned, or if this prim is itself an instance proxy.
        
        See Prim predicate flags and UsdPrimDefaultPredicate for more
        information.
        
        
        Parameters
        ----------
        predicate : _PrimFlagsPredicate
        
        
        """
    @staticmethod
    def GetFilteredChildrenNames(*args, **kwargs):
        """
        
        GetFilteredChildrenNames(predicate) -> list[str]
        
        
        Return the names of the child prims in the order they appear when
        iterating over GetFilteredChildren( ``predicate`` ).
        
        
        
        
        Parameters
        ----------
        predicate : _PrimFlagsPredicate
        
        
        """
    @staticmethod
    def GetFilteredNextSibling(*args, **kwargs):
        """
        
        GetFilteredNextSibling(predicate) -> Prim
        
        
        Return this prim's next sibling that matches ``predicate`` if it has
        one, otherwise return the invalid UsdPrim.
        
        
        See Prim predicate flags and UsdPrimDefaultPredicate for more
        information.
        
        
        Parameters
        ----------
        predicate : _PrimFlagsPredicate
        
        
        """
    @staticmethod
    def GetInherits(*args, **kwargs):
        """
        
        GetInherits() -> Inherits
        
        
        Return a UsdInherits object that allows one to add, remove, or mutate
        inherits *at the currently set UsdEditTarget*.
        
        
        While the UsdInherits object has no methods for *listing* the
        currently authored inherits on a prim, one can use a
        UsdPrimCompositionQuery to query the inherits arcs that are composed
        by this prim.
        
        UsdPrimCompositionQuery::GetDirectInherits
        
        
        
        """
    @staticmethod
    def GetInstances(*args, **kwargs):
        """
        
        GetInstances() -> list[Prim]
        
        
        If this prim is a prototype prim, returns all prims that are instances
        of this prototype.
        
        
        Otherwise, returns an empty vector.
        
        Note that this function will return prims in prototypes for instances
        that are nested beneath other instances.
        
        
        
        """
    @staticmethod
    def GetNextSibling(*args, **kwargs):
        """
        
        GetNextSibling() -> Prim
        
        
        Return this prim's next active, loaded, defined, non-abstract sibling
        if it has one, otherwise return an invalid UsdPrim.
        
        
        Equivalent to:
        
        .. code-block:: text
        
          GetFilteredNextSibling(UsdPrimDefaultPredicate)
        
        See Prim predicate flags and UsdPrimDefaultPredicate for more
        information.
        
        
        
        """
    @staticmethod
    def GetObjectAtPath(*args, **kwargs):
        """
        
        GetObjectAtPath(path) -> Object
        
        
        Returns the object at ``path`` on the same stage as this prim.
        
        
        If path is is relative, it will be anchored to the path of this prim.
        
        UsdStage::GetObjectAtPath(const SdfPath&) const
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetParent(*args, **kwargs):
        """
        
        GetParent() -> Prim
        
        
        Return this prim's parent prim.
        
        
        Return an invalid UsdPrim if this is a root prim.
        
        
        
        """
    @staticmethod
    def GetPayloads(*args, **kwargs):
        """
        
        GetPayloads() -> Payloads
        
        
        Return a UsdPayloads object that allows one to add, remove, or mutate
        payloads *at the currently set UsdEditTarget*.
        
        
        While the UsdPayloads object has no methods for *listing* the
        currently authored payloads on a prim, one can use a
        UsdPrimCompositionQuery to query the payload arcs that are composed by
        this prim.
        
        
        
        """
    @staticmethod
    def GetPrimAtPath(*args, **kwargs):
        """
        
        GetPrimAtPath(path) -> Prim
        
        
        Returns the prim at ``path`` on the same stage as this prim.
        
        
        If path is is relative, it will be anchored to the path of this prim.
        
        UsdStage::GetPrimAtPath(const SdfPath&) const
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetPrimDefinition(*args, **kwargs):
        """
        
        GetPrimDefinition() -> PrimDefinition
        
        
        Return this prim's definition based on the prim's type if the type is
        a registered prim type.
        
        
        Returns an empty prim definition if it is not.
        
        
        
        """
    @staticmethod
    def GetPrimInPrototype(*args, **kwargs):
        """
        
        GetPrimInPrototype() -> Prim
        
        
        If this prim is an instance proxy, return the UsdPrim for the
        corresponding prim in the instance's prototype.
        
        
        Otherwise, return an invalid UsdPrim.
        
        
        
        """
    @staticmethod
    def GetPrimIndex(*args, **kwargs):
        """
        
        GetPrimIndex() -> PrimIndex
        
        
        Return the cached prim index containing all sites that can contribute
        opinions to this prim.
        
        
        The prim index can be used to examine the composition arcs and scene
        description sites that can contribute to this prim's property and
        metadata values.
        
        The prim index returned by this function is optimized and may not
        include sites that do not contribute opinions to this prim. Use
        UsdPrim::ComputeExpandedPrimIndex to compute a prim index that
        includes all possible sites that could contribute opinions.
        
        This prim index will be empty for prototype prims. This ensures that
        these prims do not provide any attribute or metadata values. For all
        other prims in prototypes, this is the prim index that was chosen to
        be shared with all other instances. In either case, the prim index's
        path will not be the same as the prim's path.
        
        Prim indexes may be invalidated by changes to the UsdStage and cannot
        detect if they are expired. Clients should avoid keeping copies of the
        prim index across such changes, which include scene description
        changes or changes to load state.
        
        
        
        """
    @staticmethod
    def GetPrimStack(*args, **kwargs):
        """
        
        GetPrimStack() -> list[PrimSpec]
        
        
        Return all the authored SdfPrimSpecs that may contain opinions for
        this prim in order from strong to weak.
        
        
        This does not include all the places where contributing prim specs
        could potentially be created; rather, it includes only those prim
        specs that already exist. To discover all the places that prim specs
        could be authored that would contribute opinions, see"Composition
        Structure"
        
        Use this method for debugging and diagnostic purposes. It is **not**
        advisable to retain a PrimStack for expedited metadata value
        resolution, since not all metadata resolves with
        simple"strongestopinion wins"semantics.
        
        
        
        """
    @staticmethod
    def GetPrimStackWithLayerOffsets(*args, **kwargs):
        """
        
        GetPrimStackWithLayerOffsets() -> list[tuple[PrimSpec, LayerOffset]]
        
        
        Return all the authored SdfPrimSpecs that may contain opinions for
        this prim in order from strong to weak paired with the cumulative
        layer offset from the stage's root layer to the layer containing the
        prim spec.
        
        
        This behaves exactly the same as UsdPrim::GetPrimStack with the
        addition of providing the cumulative layer offset of each spec's
        layer.
        
        Use this method for debugging and diagnostic purposes. It is **not**
        advisable to retain a PrimStack for expedited metadata value
        resolution, since not all metadata resolves with
        simple"strongestopinion wins"semantics.
        
        
        
        """
    @staticmethod
    def GetPrimTypeInfo(*args, **kwargs):
        """
        
        GetPrimTypeInfo() -> PrimTypeInfo
        
        
        Return the prim's full type info composed from its type name, applied
        API schemas, and any fallback types defined on the stage for
        unrecognized prim type names.
        
        
        The returned type structure contains the"true"schema type used to
        create this prim's prim definition and answer the IsA query. This
        value is cached and efficient to query. The cached values are
        guaranteed to exist for (at least) as long as the prim's stage is
        open.
        
        GetTypeName
        
        GetAppliedSchemas
        
        Fallback Prim Types
        
        
        
        """
    @staticmethod
    def GetProperties(*args, **kwargs):
        """
        
        GetProperties(predicate) -> list[Property]
        
        
        Return all of this prim's properties (attributes and relationships),
        including all builtin properties, ordered by name according to the
        strongest propertyOrder statement in scene description if one exists,
        otherwise ordered according to TfDictionaryLessThan.
        
        
        If a valid ``predicate`` is passed in, then only properties whose
        names  pass the predicate are included in the result. This is useful
        if the client is interested only in a subset of properties on the
        prim. For example, only the ones in a given namespace or only the ones
        needed to compute a value.
        
        To obtain only either attributes or relationships, use either
        GetAttributes() or GetRelationships() .
        
        To determine whether a property is either an attribute or a
        relationship, use the UsdObject::As() and UsdObject::Is() methods in
        C++:
        
        .. code-block:: text
        
          // Use As<>() to obtain a subclass instance.
          if (UsdAttribute attr = property.As<UsdAttribute>()) {
              // use attribute 'attr'.
          else if (UsdRelationship rel = property.As<UsdRelationship>()) {
              // use relationship 'rel'.
          }
          
          // Use Is<>() to discriminate only.
          if (property.Is<UsdAttribute>()) {
              // property is an attribute.
          }
        
        In Python, use the standard isinstance() function:
        
        .. code-block:: text
        
          if isinstance(property, Usd.Attribute):
              # property is a Usd.Attribute.
          elif isinstance(property, Usd.Relationship):
              # property is a Usd.Relationship.
        
        GetAuthoredProperties()
        
        UsdProperty::IsAuthored()
        
        
        Parameters
        ----------
        predicate : PropertyPredicateFunc
        
        
        """
    @staticmethod
    def GetPropertiesInNamespace(*args, **kwargs):
        """
        
        GetPropertiesInNamespace(namespaces) -> list[Property]
        
        
        Return this prim's properties that are inside the given property
        namespace ordered according to the strongest propertyOrder statement
        in scene description if one exists, otherwise ordered according to
        TfDictionaryLessThan.
        
        
        A ``namespaces`` argument whose elements are ["ri","attribute"] will
        return all the properties under the namespace"ri:attribute",
        i.e."ri:attribute:\\*". An empty ``namespaces`` argument is equivalent
        to GetProperties() .
        
        For details of namespaced properties, see Names, Namespace Ordering,
        and Property Namespaces
        
        
        Parameters
        ----------
        namespaces : list[str]
        
        
        
        ----------------------------------------------------------------------
        
        GetPropertiesInNamespace(namespaces) -> list[Property]
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        ``namespaces`` must be an already-concatenated ordered set of
        namespaces, and may or may not terminate with the namespace-separator
        character.
        
        
        If ``namespaces`` is empty, this method is equivalent to
        GetProperties() .
        
        
        Parameters
        ----------
        namespaces : str
        
        
        """
    @staticmethod
    def GetProperty(*args, **kwargs):
        """
        
        GetProperty(propName) -> Property
        
        
        Return a UsdProperty with the name *propName*.
        
        
        The property returned may or may not **actually** exist so it must be
        checked for validity. Suggested use:
        
        .. code-block:: text
        
          if (UsdProperty myProp = prim.GetProperty("myProp")) {
             // myProp is safe to use. 
             // Edits to the owning stage requires subsequent validation.
          } else {
             // myProp was not defined/authored
          }
        
        
        
        Parameters
        ----------
        propName : str
        
        
        """
    @staticmethod
    def GetPropertyAtPath(*args, **kwargs):
        """
        
        GetPropertyAtPath(path) -> Property
        
        
        Returns the property at ``path`` on the same stage as this prim.
        
        
        If path is relative, it will be anchored to the path of this prim.
        
        There is no guarantee that this method returns a property on this
        prim. This is only guaranteed if path is a purely relative property
        path.
        
        GetProperty(const TfToken&) const
        
        UsdStage::GetPropertyAtPath(const SdfPath&) const
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetPropertyNames(*args, **kwargs):
        """
        
        GetPropertyNames(predicate) -> list[str]
        
        
        Return all of this prim's property names (attributes and
        relationships), including all builtin properties.
        
        
        If a valid ``predicate`` is passed in, then only properties whose
        names pass the predicate are included in the result. This is useful if
        the client is interested only in a subset of properties on the prim.
        For example, only the ones in a given namespace or only the ones
        needed to compute a value.
        
        GetAuthoredPropertyNames()
        
        UsdProperty::IsAuthored()
        
        
        Parameters
        ----------
        predicate : PropertyPredicateFunc
        
        
        """
    @staticmethod
    def GetPropertyOrder(*args, **kwargs):
        """
        
        GetPropertyOrder() -> list[str]
        
        
        Return the strongest propertyOrder metadata value authored on this
        prim.
        
        
        
        """
    @staticmethod
    def GetPrototype(*args, **kwargs):
        """
        
        GetPrototype() -> Prim
        
        
        If this prim is an instance, return the UsdPrim for the corresponding
        prototype.
        
        
        Otherwise, return an invalid UsdPrim.
        
        
        
        """
    @staticmethod
    def GetReferences(*args, **kwargs):
        """
        
        GetReferences() -> References
        
        
        Return a UsdReferences object that allows one to add, remove, or
        mutate references *at the currently set UsdEditTarget*.
        
        
        While the UsdReferences object has no methods for *listing* the
        currently authored references on a prim, one can use a
        UsdPrimCompositionQuery to query the reference arcs that are composed
        by this prim.
        
        UsdPrimCompositionQuery::GetDirectReferences
        
        
        
        """
    @staticmethod
    def GetRelationship(*args, **kwargs):
        """
        
        GetRelationship(relName) -> Relationship
        
        
        Return a UsdRelationship with the name *relName*.
        
        
        The relationship returned may or may not **actually** exist so it must
        be checked for validity. Suggested use:
        
        .. code-block:: text
        
          if (UsdRelationship myRel = prim.GetRelationship("myRel")) {
             // myRel is safe to use.
             // Edits to the owning stage requires subsequent validation.
          } else {
             // myRel was not defined/authored
          }
        
        
        
        Parameters
        ----------
        relName : str
        
        
        """
    @staticmethod
    def GetRelationshipAtPath(*args, **kwargs):
        """
        
        GetRelationshipAtPath(path) -> Relationship
        
        
        Returns the relationship at ``path`` on the same stage as this prim.
        
        
        If path is relative, it will be anchored to the path of this prim.
        
        There is no guarantee that this method returns a relationship on this
        prim. This is only guaranteed if path is a purely relative property
        path.
        
        GetRelationship(const TfToken&) const
        
        UsdStage::GetRelationshipAtPath(const SdfPath&) const
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetRelationships(*args, **kwargs):
        """
        
        GetRelationships() -> list[Relationship]
        
        
        Like GetProperties() , but exclude all attributes from the result.
        
        
        
        """
    @staticmethod
    def GetSpecializes(*args, **kwargs):
        """
        
        GetSpecializes() -> Specializes
        
        
        Return a UsdSpecializes object that allows one to add, remove, or
        mutate specializes *at the currently set UsdEditTarget*.
        
        
        While the UsdSpecializes object has no methods for *listing* the
        currently authored specializes on a prim, one can use a
        UsdPrimCompositionQuery to query the specializes arcs that are
        composed by this prim.
        
        
        
        """
    @staticmethod
    def GetSpecifier(*args, **kwargs):
        """
        
        GetSpecifier() -> Specifier
        
        
        Return this prim's composed specifier.
        
        
        
        """
    @staticmethod
    def GetTypeName(*args, **kwargs):
        """
        
        GetTypeName() -> str
        
        
        Return this prim's composed type name.
        
        
        This value is cached and is efficient to query. Note that this is just
        the composed type name as authored and may not represent the full type
        of the prim and its prim definition. If you need to reason about the
        actual type of the prim, use GetPrimTypeInfo instead as it accounts
        for recognized schemas, applied API schemas, fallback types, etc.
        
        
        
        """
    @staticmethod
    def GetVariantSet(*args, **kwargs):
        """
        
        GetVariantSet(variantSetName) -> VariantSet
        
        
        Retrieve a specifically named VariantSet for editing or constructing a
        UsdEditTarget.
        
        
        This is a shortcut for
        
        .. code-block:: text
        
          prim.GetVariantSets().GetVariantSet(variantSetName)
        
        
        
        Parameters
        ----------
        variantSetName : str
        
        
        """
    @staticmethod
    def GetVariantSets(*args, **kwargs):
        """
        
        GetVariantSets() -> VariantSets
        
        
        Return a UsdVariantSets object representing all the VariantSets
        present on this prim.
        
        
        The returned object also provides the API for adding new VariantSets
        to the prim.
        
        
        
        """
    @staticmethod
    def HasAPI(*args, **kwargs):
        """
        
        HasAPI() -> enable_if[T.schemaKind != SchemaKind.MultipleApplyAPI, bool].type
        
        
        **Using HasAPI in C++**
        
        
        
        .. code-block:: text
        
          UsdPrim prim = stage->OverridePrim("/path/to/prim");
          MyDomainBozAPI = MyDomainBozAPI::Apply(prim);
          assert(prim.HasAPI<MyDomainBozAPI>());
          
          UsdCollectionAPI collAPI = UsdCollectionAPI::Apply(prim, 
                  /\\*instanceName\\*/ TfToken("geom"))
          assert(prim.HasAPI<UsdCollectionAPI>()
          assert(prim.HasAPI<UsdCollectionAPI>(/\\*instanceName\\*/ TfToken("geom")))
        
        The python version of this method takes as an argument the TfType of
        the API schema class. Similar validation of the schema type is
        performed in python at run-time and a coding error is issued if the
        given type is not a valid applied API schema.
        
        **Using HasAPI in Python**
        
        .. code-block:: text
        
          prim = stage.OverridePrim("/path/to/prim")
          bozAPI = MyDomain.BozAPI.Apply(prim)
          assert prim.HasAPI(MyDomain.BozAPI)
          
          collAPI = Usd.CollectionAPI.Apply(prim, "geom")
          assert(prim.HasAPI(Usd.CollectionAPI))
          assert(prim.HasAPI(Usd.CollectionAPI, instanceName="geom"))
        
         Return true if the UsdPrim has had a single API schema represented by
        the C++ class type **T** applied to it through the Apply() method
        provided on the API schema class.
        
        
        
        
        ----------------------------------------------------------------------
        
        HasAPI(instanceName) -> enable_if[T.schemaKind== SchemaKind.MultipleApplyAPI, bool].type
        
        
        Return true if the UsdPrim has had a multiple-apply API schema
        represented by the C++ class type **T** applied to it through the
        Apply() method provided on the API schema class.
        
        
        ``instanceName`` , if non-empty is used to determine if a particular
        instance of a multiple-apply API schema (eg. UsdCollectionAPI) has
        been applied to the prim, otherwise this returns true if any instance
        of the multiple-apply API has been applied.
        
        
        Parameters
        ----------
        instanceName : str
        
        
        
        ----------------------------------------------------------------------
        
        HasAPI(schemaType, instanceName) -> bool
        
        
        Return true if a prim has an API schema with TfType ``schemaType`` .
        
        
        ``instanceName`` , if non-empty is used to determine if a particular
        instance of a multiple-apply API schema (eg. UsdCollectionAPI) has
        been applied to the prim. A coding error is issued if a non-empty
        ``instanceName`` is passed in and **T** represents a single-apply API
        schema.
        
        This function behaves exactly like the templated HasAPI functions
        except for the runtime schemaType validation which happens at compile
        time in the templated versions. This method is provided for python
        clients. Use of the templated HasAPI functions are preferred.
        
        
        Parameters
        ----------
        schemaType : Type
        
        instanceName : str
        
        
        """
    @staticmethod
    def HasAttribute(*args, **kwargs):
        """
        
        HasAttribute(attrName) -> bool
        
        
        Return true if this prim has an attribute named ``attrName`` , false
        otherwise.
        
        
        Parameters
        ----------
        attrName : str
        
        
        """
    @staticmethod
    def HasAuthoredActive(*args, **kwargs):
        """
        
        HasAuthoredActive() -> bool
        
        
        Return true if this prim has an authored opinion for'active', false
        otherwise.
        
        
        See How"active"Affects Prims on a UsdStage for what it means for a
        prim to be active.
        
        
        
        """
    @staticmethod
    def HasAuthoredInherits(*args, **kwargs):
        """
        
        HasAuthoredInherits() -> bool
        
        
        Return true if this prim has any authored inherits.
        
        
        
        """
    @staticmethod
    def HasAuthoredInstanceable(*args, **kwargs):
        """
        
        HasAuthoredInstanceable() -> bool
        
        
        Return true if this prim has an authored opinion for'instanceable',
        false otherwise.
        
        
        
        """
    @staticmethod
    def HasAuthoredPayloads(*args, **kwargs):
        """
        
        HasAuthoredPayloads() -> bool
        
        
        Return true if this prim has any authored payloads.
        
        
        
        """
    @staticmethod
    def HasAuthoredReferences(*args, **kwargs):
        """
        
        HasAuthoredReferences() -> bool
        
        
        Return true if this prim has any authored references.
        
        
        
        """
    @staticmethod
    def HasAuthoredSpecializes(*args, **kwargs):
        """
        
        HasAuthoredSpecializes() -> bool
        
        
        Returns true if this prim has any authored specializes.
        
        
        
        """
    @staticmethod
    def HasAuthoredTypeName(*args, **kwargs):
        """
        
        HasAuthoredTypeName() -> bool
        
        
        Return true if a typeName has been authored.
        
        
        
        """
    @staticmethod
    def HasDefiningSpecifier(*args, **kwargs):
        """
        
        HasDefiningSpecifier() -> bool
        
        
        Return true if this prim has a specifier of type SdfSpecifierDef or
        SdfSpecifierClass.
        
        
        
        SdfIsDefiningSpecifier
        
        
        
        """
    @staticmethod
    def HasPayload(*args, **kwargs):
        """
        
        HasPayload() -> bool
        
        
        Deprecated
        
        Return true if a payload is present on this prim.
        
        Payloads: Impact of Using and Not Using
        
        
        
        """
    @staticmethod
    def HasProperty(*args, **kwargs):
        """
        
        HasProperty(propName) -> bool
        
        
        Return true if this prim has an property named ``propName`` , false
        otherwise.
        
        
        Parameters
        ----------
        propName : str
        
        
        """
    @staticmethod
    def HasRelationship(*args, **kwargs):
        """
        
        HasRelationship(relName) -> bool
        
        
        Return true if this prim has a relationship named ``relName`` , false
        otherwise.
        
        
        Parameters
        ----------
        relName : str
        
        
        """
    @staticmethod
    def HasVariantSets(*args, **kwargs):
        """
        
        HasVariantSets() -> bool
        
        
        Return true if this prim has any authored VariantSets.
        
        
        
        this connotes only the *existence* of one of more VariantSets, *not*
        that such VariantSets necessarily contain any variants or variant
        opinions.
        
        
        
        """
    @staticmethod
    def IsA(*args, **kwargs):
        """
        
        IsA() -> bool
        
        
        Return true if the prim's schema type, is or inherits schema type T.
        
        
        
        GetPrimTypeInfo
        
        UsdPrimTypeInfo::GetSchemaType
        
        Fallback Prim Types
        
        
        
        
        ----------------------------------------------------------------------
        
        IsA(schemaType) -> bool
        
        
        Return true if the prim's schema type is or inherits ``schemaType`` .
        
        
        
        GetPrimTypeInfo
        
        UsdPrimTypeInfo::GetSchemaType
        
        Fallback Prim Types
        
        
        Parameters
        ----------
        schemaType : Type
        
        
        """
    @staticmethod
    def IsAbstract(*args, **kwargs):
        """
        
        IsAbstract() -> bool
        
        
        Return true if this prim or any of its ancestors is a class.
        
        
        
        """
    @staticmethod
    def IsActive(*args, **kwargs):
        """
        
        IsActive() -> bool
        
        
        Return true if this prim is active, meaning neither it nor any of its
        ancestors have active=false.
        
        
        Return false otherwise.
        
        See How"active"Affects Prims on a UsdStage for what it means for a
        prim to be active.
        
        
        
        """
    @staticmethod
    def IsDefined(*args, **kwargs):
        """
        
        IsDefined() -> bool
        
        
        Return true if this prim and all its ancestors have defining
        specifiers, false otherwise.
        
        
        
        SdfIsDefiningSpecifier.
        
        
        
        """
    @staticmethod
    def IsGroup(*args, **kwargs):
        """
        
        IsGroup() -> bool
        
        
        Return true if this prim is a model group based on its kind metadata,
        false otherwise.
        
        
        If this prim is a group, it is also necessarily a model.
        
        
        
        """
    @staticmethod
    def IsInPrototype(*args, **kwargs):
        """
        
        IsInPrototype() -> bool
        
        
        Return true if this prim is a prototype prim or a descendant of a
        prototype prim, false otherwise.
        
        
        
        IsPrototype
        
        
        
        """
    @staticmethod
    def IsInstance(*args, **kwargs):
        """
        
        IsInstance() -> bool
        
        
        Return true if this prim is an instance of a prototype, false
        otherwise.
        
        
        If this prim is an instance, calling GetPrototype() will return the
        UsdPrim for the corresponding prototype prim.
        
        
        
        """
    @staticmethod
    def IsInstanceProxy(*args, **kwargs):
        """
        
        IsInstanceProxy() -> bool
        
        
        Return true if this prim is an instance proxy, false otherwise.
        
        
        An instance proxy prim represents a descendent of an instance prim.
        
        
        
        """
    @staticmethod
    def IsInstanceable(*args, **kwargs):
        """
        
        IsInstanceable() -> bool
        
        
        Return true if this prim has been marked as instanceable.
        
        
        Note that this is not the same as IsInstance() . A prim may return
        true for IsInstanceable() and false for IsInstance() if this prim is
        not active or if it is marked as instanceable but contains no
        instanceable data.
        
        
        
        """
    @staticmethod
    def IsLoaded(*args, **kwargs):
        """
        
        IsLoaded() -> bool
        
        
        Return true if this prim is active, and *either* it is loadable and it
        is loaded, *or* its nearest loadable ancestor is loaded, *or* it has
        no loadable ancestor; false otherwise.
        
        
        
        """
    @staticmethod
    def IsModel(*args, **kwargs):
        """
        
        IsModel() -> bool
        
        
        Return true if this prim is a model based on its kind metadata, false
        otherwise.
        
        
        
        """
    @staticmethod
    def IsPathInPrototype(*args, **kwargs):
        """
        
        **classmethod** IsPathInPrototype(path) -> bool
        
        
        Return true if the given ``path`` identifies a prototype prim or a
        prim or property descendant of a prototype prim, false otherwise.
        
        
        
        IsPrototypePath
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def IsPrototype(*args, **kwargs):
        """
        
        IsPrototype() -> bool
        
        
        Return true if this prim is an instancing prototype prim, false
        otherwise.
        
        
        
        IsInPrototype
        
        
        
        """
    @staticmethod
    def IsPrototypePath(*args, **kwargs):
        """
        
        **classmethod** IsPrototypePath(path) -> bool
        
        
        Return true if the given ``path`` identifies a prototype prim, false
        otherwise.
        
        
        This function will return false for prim and property paths that are
        descendants of a prototype prim path.
        
        IsPathInPrototype
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def IsPseudoRoot(*args, **kwargs):
        """
        
        IsPseudoRoot() -> bool
        
        
        Returns true if the prim is the pseudo root.
        
        
        
        Equivalent to
        
        .. code-block:: text
        
          prim.GetPath() == SdfPath::AbsoluteRootPath()
        
        
        
        
        """
    @staticmethod
    def Load(*args, **kwargs):
        """
        
        Load(policy) -> None
        
        
        Load this prim, all its ancestors, and by default all its descendants.
        
        
        If ``loadPolicy`` is UsdLoadWithoutDescendants, then load only this
        prim and its ancestors.
        
        See UsdStage::Load for additional details.
        
        
        Parameters
        ----------
        policy : LoadPolicy
        
        
        """
    @staticmethod
    def MakeResolveTargetStrongerThanEditTarget(*args, **kwargs):
        """
        
        MakeResolveTargetStrongerThanEditTarget(editTarget) -> ResolveTarget
        
        
        Creates and returns a resolve target that, when passed to a
        UsdAttributeQuery for one of this prim's attributes, causes value
        resolution to only consider specs that are stronger than the spec that
        would be authored for this prim when using the given ``editTarget`` .
        
        
        If the edit target would not affect any specs that could contribute to
        this prim, a null resolve target is returned.
        
        
        Parameters
        ----------
        editTarget : EditTarget
        
        
        """
    @staticmethod
    def MakeResolveTargetUpToEditTarget(*args, **kwargs):
        """
        
        MakeResolveTargetUpToEditTarget(editTarget) -> ResolveTarget
        
        
        Creates and returns a resolve target that, when passed to a
        UsdAttributeQuery for one of this prim's attributes, causes value
        resolution to only consider weaker specs up to and including the spec
        that would be authored for this prim when using the given
        ``editTarget`` .
        
        
        If the edit target would not affect any specs that could contribute to
        this prim, a null resolve target is returned.
        
        
        Parameters
        ----------
        editTarget : EditTarget
        
        
        """
    @staticmethod
    def RemoveAPI(*args, **kwargs):
        """
        
        RemoveAPI() -> bool
        
        
        Removes a **single-apply** API schema with the given C++
        type'SchemaType'from this prim in the current edit target.
        
        
        This is done by removing the API schema's name token from the token-
        valued, listOp metadata *apiSchemas* on this prim as well as authoring
        an explicit deletion of schema name from the listOp.
        
        Returns true upon success or if the API schema is already deleted in
        the current edit target.
        
        An error is issued and false returned for any of the following
        conditions:
        
           - this prim is not a valid prim for editing
        
           - this prim is valid, but cannot be reached or overridden in the
             current edit target
        
           - the schema name cannot be deleted in the apiSchemas listOp
             metadata
        
        
        
        
        
        ----------------------------------------------------------------------
        
        RemoveAPI(schemaType) -> bool
        
        
        Non-templated overload of the templated RemoveAPI above.
        
        
        This function behaves exactly like the templated RemoveAPI  except for
        the runtime schemaType validation which happens at compile time in the
        templated version. This method is provided for python clients. Use of
        the templated RemoveAPI is preferred.
        
        
        Parameters
        ----------
        schemaType : Type
        
        
        
        ----------------------------------------------------------------------
        
        RemoveAPI(instanceName) -> bool
        
        
        Removes a **multiple-apply** API schema with the given C++
        type'SchemaType'and instance name ``instanceName`` from this prim in
        the current edit target.
        
        
        This is done by removing the instanced schema name token from the
        token-valued, listOp metadata *apiSchemas* on this prim as well as
        authoring an explicit deletion of the name from the listOp. For
        example, if SchemaType is' UsdCollectionAPI 'and ``instanceName``
        is'plasticStuff', the name'CollectionAPI:plasticStuff'is deleted from
        the'apiSchemas'listOp metadata.
        
        Returns true upon success or if the API schema with this
        ``instanceName`` is already deleted in the current edit target.
        
        An error is issued and false returned for any of the following
        conditions:
        
           - ``instanceName`` is empty
        
           - this prim is not a valid prim for editing
        
           - this prim is valid, but cannot be reached or overridden in the
             current edit target
        
           - the schema name cannot be deleted in the apiSchemas listOp
             metadata
        
        
        
        Parameters
        ----------
        instanceName : str
        
        
        
        ----------------------------------------------------------------------
        
        RemoveAPI(schemaType, instanceName) -> bool
        
        
        Non-templated overload of the templated RemoveAPI above.
        
        
        This function behaves exactly like the templated RemoveAPI  except for
        the runtime schemaType validation which happens at compile time in the
        templated version. This method is provided for python clients. Use of
        the templated RemoveAPI is preferred.
        
        
        Parameters
        ----------
        schemaType : Type
        
        instanceName : str
        
        
        """
    @staticmethod
    def RemoveAppliedSchema(*args, **kwargs):
        """
        
        RemoveAppliedSchema(appliedSchemaName) -> bool
        
        
        Removes the applied API schema name token ``appliedSchemaName`` from
        the *apiSchemas* metadata for this prim at the current edit target.
        
        
        For multiple-apply schemas the name token should include the instance
        name for the applied schema, for example'CollectionAPI:plasticStuff'
        
        For an explicit list operation, this removes the applied schema name
        from the explicit items list if it was present. For a non-explicit
        list operation, this will remove any occurrence of the applied schema
        name from the prepended and appended item as well as adding it to the
        deleted items list.
        
        Returns true upon success or if the API schema is already deleted in
        the current edit target.
        
        An error is issued and false returned for any of the following
        conditions:
        
           - this prim is not a valid prim for editing
        
           - this prim is valid, but cannot be reached or overridden in the
             current edit target
        
           - the schema name cannot be deleted in the apiSchemas listOp
             metadata
             Unlike RemoveAPI this method does not require that the name token
             refer to a valid API schema type. RemoveAPI is the preferred method
             for removing valid API schemas.
        
        
        Parameters
        ----------
        appliedSchemaName : str
        
        
        """
    @staticmethod
    def RemoveProperty(*args, **kwargs):
        """
        
        RemoveProperty(propName) -> bool
        
        
        Remove all scene description for the property with the given
        ``propName`` *in the current UsdEditTarget*.
        
        
        Return true if the property is removed, false otherwise.
        
        Because this method can only remove opinions about the property from
        the current EditTarget, you may generally find it more useful to use
        UsdAttribute::Block() , which will ensure that all values from the
        EditTarget and weaker layers for the property will be ignored.
        
        
        Parameters
        ----------
        propName : str
        
        
        """
    @staticmethod
    def SetActive(*args, **kwargs):
        """
        
        SetActive(active) -> bool
        
        
        Author'active'metadata for this prim at the current EditTarget.
        
        
        See How"active"Affects Prims on a UsdStage for the effects of
        activating or deactivating a prim.
        
        
        Parameters
        ----------
        active : bool
        
        
        """
    @staticmethod
    def SetChildrenReorder(*args, **kwargs):
        """
        
        SetChildrenReorder(order) -> None
        
        
        Author an opinion for the metadata used to reorder children of this
        prim at the current EditTarget.
        
        
        Parameters
        ----------
        order : list[str]
        
        
        """
    @staticmethod
    def SetInstanceable(*args, **kwargs):
        """
        
        SetInstanceable(instanceable) -> bool
        
        
        Author'instanceable'metadata for this prim at the current EditTarget.
        
        
        Parameters
        ----------
        instanceable : bool
        
        
        """
    @staticmethod
    def SetPayload(*args, **kwargs):
        """
        
        SetPayload(payload) -> bool
        
        
        Deprecated
        
        Author payload metadata for this prim at the current edit target.
        Return true on success, false if the value could not be set.
        
        Payloads: Impact of Using and Not Using
        
        
        Parameters
        ----------
        payload : Payload
        
        
        
        ----------------------------------------------------------------------
        
        SetPayload(assetPath, primPath) -> bool
        
        
        Deprecated
        
        Shorthand for SetPayload(SdfPayload(assetPath, primPath)).
        
        
        Parameters
        ----------
        assetPath : str
        
        primPath : Path
        
        
        
        ----------------------------------------------------------------------
        
        SetPayload(layer, primPath) -> bool
        
        
        Deprecated
        
        Shorthand for SetPayload( SdfPayload (layer->GetIdentifier(),
        primPath)).
        
        
        Parameters
        ----------
        layer : Layer
        
        primPath : Path
        
        
        """
    @staticmethod
    def SetPropertyOrder(*args, **kwargs):
        """
        
        SetPropertyOrder(order) -> None
        
        
        Author an opinion for propertyOrder metadata on this prim at the
        current EditTarget.
        
        
        Parameters
        ----------
        order : list[str]
        
        
        """
    @staticmethod
    def SetSpecifier(*args, **kwargs):
        """
        
        SetSpecifier(specifier) -> bool
        
        
        Author an opinion for this Prim's specifier at the current edit
        target.
        
        
        Parameters
        ----------
        specifier : Specifier
        
        
        """
    @staticmethod
    def SetTypeName(*args, **kwargs):
        """
        
        SetTypeName(typeName) -> bool
        
        
        Author this Prim's typeName at the current EditTarget.
        
        
        Parameters
        ----------
        typeName : str
        
        
        """
    @staticmethod
    def Unload(*args, **kwargs):
        """
        
        Unload() -> None
        
        
        Unloads this prim and all its descendants.
        
        
        See UsdStage::Unload for additional details.
        
        
        
        """
    @staticmethod
    def _GetSourcePrimIndex(*args, **kwargs):
        """
        
        _GetSourcePrimIndex() -> PrimIndex
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct an invalid prim.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(primData, proxyPrimPath)
        
        
        Parameters
        ----------
        primData : Usd_PrimData
        
        proxyPrimPath : Path
        
        
        
        ----------------------------------------------------------------------
        
        __init__(objType, prim, proxyPrimPath, propName)
        
        
        Parameters
        ----------
        objType : UsdObjType
        
        prim : Usd_PrimData
        
        proxyPrimPath : Path
        
        propName : str
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class PrimCompositionQuery(Boost.Python.instance):
    """
    
    Object for making optionally filtered composition queries about a
    prim. It creates a list of strength ordering
    UsdPrimCompositionQueryArc that can be filtered by a combination of
    criteria and returned.
    
    Invalidation
    ============
    
    This object does not listen for change notification. If a consumer is
    holding on to a UsdPrimCompositionQuery, it is their responsibility to
    dispose of it in response to a resync change to the associated prim.
    Failing to do so may result in incorrect values or crashes due to
    dereferencing invalid objects.
    
    """
    class ArcIntroducedFilter(Boost.Python.enum):
        """
        
        Choices for filtering composition arcs based on where the arc is
        introduced.
        
        
        
        """
        All: typing.ClassVar[ArcIntroducedFilter]  # value = pxr.Usd.ArcIntroducedFilter.All
        IntroducedInRootLayerPrimSpec: typing.ClassVar[ArcIntroducedFilter]  # value = pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerPrimSpec
        IntroducedInRootLayerStack: typing.ClassVar[ArcIntroducedFilter]  # value = pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerStack
        __slots__: typing.ClassVar[tuple] = tuple()
        names: typing.ClassVar[dict]  # value = {'All': pxr.Usd.ArcIntroducedFilter.All, 'IntroducedInRootLayerStack': pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerStack, 'IntroducedInRootLayerPrimSpec': pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerPrimSpec}
        values: typing.ClassVar[dict]  # value = {0: pxr.Usd.ArcIntroducedFilter.All, 1: pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerStack, 2: pxr.Usd.ArcIntroducedFilter.IntroducedInRootLayerPrimSpec}
    class ArcTypeFilter(Boost.Python.enum):
        """
        
        Choices for filtering composition arcs based on arc type.
        
        """
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
        """
        
        Choices for filtering composition arcs on dependency type.
        
        
        This can be direct (arc introduced at the prim's level in namespace)
        or ancestral (arc introduced by a namespace parent of the prim).
        
        """
        All: typing.ClassVar[DependencyTypeFilter]  # value = pxr.Usd.DependencyTypeFilter.All
        Ancestral: typing.ClassVar[DependencyTypeFilter]  # value = pxr.Usd.DependencyTypeFilter.Ancestral
        Direct: typing.ClassVar[DependencyTypeFilter]  # value = pxr.Usd.DependencyTypeFilter.Direct
        __slots__: typing.ClassVar[tuple] = tuple()
        names: typing.ClassVar[dict]  # value = {'All': pxr.Usd.DependencyTypeFilter.All, 'Direct': pxr.Usd.DependencyTypeFilter.Direct, 'Ancestral': pxr.Usd.DependencyTypeFilter.Ancestral}
        values: typing.ClassVar[dict]  # value = {0: pxr.Usd.DependencyTypeFilter.All, 1: pxr.Usd.DependencyTypeFilter.Direct, 2: pxr.Usd.DependencyTypeFilter.Ancestral}
    class Filter(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 32
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
        """
        
        Choices for filtering composition arcs on whether the node contributes
        specs to the prim.
        
        """
        All: typing.ClassVar[HasSpecsFilter]  # value = pxr.Usd.HasSpecsFilter.All
        HasNoSpecs: typing.ClassVar[HasSpecsFilter]  # value = pxr.Usd.HasSpecsFilter.HasNoSpecs
        HasSpecs: typing.ClassVar[HasSpecsFilter]  # value = pxr.Usd.HasSpecsFilter.HasSpecs
        __slots__: typing.ClassVar[tuple] = tuple()
        names: typing.ClassVar[dict]  # value = {'All': pxr.Usd.HasSpecsFilter.All, 'HasSpecs': pxr.Usd.HasSpecsFilter.HasSpecs, 'HasNoSpecs': pxr.Usd.HasSpecsFilter.HasNoSpecs}
        values: typing.ClassVar[dict]  # value = {0: pxr.Usd.HasSpecsFilter.All, 1: pxr.Usd.HasSpecsFilter.HasSpecs, 2: pxr.Usd.HasSpecsFilter.HasNoSpecs}
    @staticmethod
    def GetCompositionArcs(*args, **kwargs):
        """
        
        GetCompositionArcs() -> list[UsdPrimCompositionQueryArc]
        
        
        Return a list of composition arcs for this query's prim using the
        current query filter.
        
        
        The composition arcs are always returned in order from strongest to
        weakest regardless of the filter.
        
        
        
        """
    @staticmethod
    def GetDirectInherits(*args, **kwargs):
        """
        
        **classmethod** GetDirectInherits(prim) -> PrimCompositionQuery
        
        
        Returns a prim composition query for the given ``prim`` with a preset
        filter that only returns inherit arcs that are not ancestral.
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def GetDirectReferences(*args, **kwargs):
        """
        
        **classmethod** GetDirectReferences(prim) -> PrimCompositionQuery
        
        
        Returns a prim composition query for the given ``prim`` with a preset
        filter that only returns reference arcs that are not ancestral.
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def GetDirectRootLayerArcs(*args, **kwargs):
        """
        
        **classmethod** GetDirectRootLayerArcs(prim) -> PrimCompositionQuery
        
        
        Returns a prim composition query for the given ``prim`` with a preset
        filter that only returns direct arcs that were introduced by opinions
        defined in a layer in the root layer stack.
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim, filter)
        
        
        Create a prim composition query for the ``with`` the given option
        ``filter`` .
        
        
        Parameters
        ----------
        prim : Prim
        
        filter : Filter
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def filter(*args, **kwargs):
        """
        type : Filter
        
        
        Return a copy of the current filter parameters.
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Change the filter for this query.
        """
    @filter.setter
    def filter(*args, **kwargs):
        ...
class PrimDefinition(Boost.Python.instance):
    """
    
    Class representing the builtin definition of a prim given the schemas
    registered in the schema registry.
    
    
    It provides access to the the builtin properties and metadata of a
    prim whose type is defined by this definition.
    
    Instances of this class can only be created by the UsdSchemaRegistry.
    
    """
    @staticmethod
    def FlattenTo(*args, **kwargs):
        """
        
        FlattenTo(layer, path, newSpecSpecifier) -> bool
        
        
        Copies the contents of this prim definition to a prim spec on the
        given ``layer`` at the given ``path`` .
        
        
        This includes the entire property spec for each of this definition's
        built-in properties as well as all of this definition's prim metadata.
        
        If the prim definition represents a concrete prim type, the type name
        of the prim spec is set to the the type name of this prim definition.
        Otherwise the type name is set to empty. The'apiSchemas'metadata on
        the prim spec will always be explicitly set to the combined list of
        all API schemas applied to this prim definition, i.e. the list
        returned by UsdPrimDefinition::GetAppliedAPISchemas. Note that if this
        prim definition is an API schema prim definition (see
        UsdSchemaRegistry::FindAppliedAPIPrimDefinition) then'apiSchemas'will
        be empty as this prim definition does not"have"an applied API because
        instead it"is"an applied API.
        
        If there is no prim spec at the given ``path`` , a new prim spec is
        created at that path with the specifier ``newSpecSpecifier`` . Any
        necessary ancestor specs will be created as well but they will always
        be created as overs. If a spec does exist at ``path`` , then all of
        its properties and schema allowed metadata are cleared before it is
        populated from the prim definition.
        
        
        Parameters
        ----------
        layer : Layer
        
        path : Path
        
        newSpecSpecifier : Specifier
        
        
        
        ----------------------------------------------------------------------
        
        FlattenTo(parent, name, newSpecSpecifier) -> Prim
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Copies the contents of this prim definition to a prim spec at the
        current edit target for a prim with the given ``name`` under the prim
        ``parent`` .
        
        
        Parameters
        ----------
        parent : Prim
        
        name : str
        
        newSpecSpecifier : Specifier
        
        
        
        ----------------------------------------------------------------------
        
        FlattenTo(prim, newSpecSpecifier) -> Prim
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Copies the contents of this prim definition to a prim spec at the
        current edit target for the given ``prim`` .
        
        
        Parameters
        ----------
        prim : Prim
        
        newSpecSpecifier : Specifier
        
        
        """
    @staticmethod
    def GetAppliedAPISchemas(*args, **kwargs):
        """
        
        GetAppliedAPISchemas() -> list[str]
        
        
        Return the list of names of the API schemas that have been applied to
        this prim definition in order.
        
        
        
        """
    @staticmethod
    def GetAttributeFallbackValue(*args, **kwargs):
        """
        
        GetAttributeFallbackValue(attrName, value) -> bool
        
        
        Retrieves the fallback value for the attribute named ``attrName`` and
        stores it in ``value`` if possible.
        
        
        Returns true if the attribute exists in this prim definition and it
        has a fallback value defined. Returns false otherwise.
        
        
        Parameters
        ----------
        attrName : str
        
        value : T
        
        
        """
    @staticmethod
    def GetDocumentation(*args, **kwargs):
        """
        
        GetDocumentation() -> str
        
        
        Returns the documentation metadata defined by the prim definition for
        the prim itself.
        
        
        
        """
    @staticmethod
    def GetMetadata(*args, **kwargs):
        """
        
        GetMetadata(key, value) -> bool
        
        
        Retrieves the fallback value for the metadata field named ``key`` ,
        that is defined by this prim definition for the prim itself and stores
        it in ``value`` if possible.
        
        
        Returns true if a fallback value is defined for the given metadata
        ``key`` . Returns false otherwise.
        
        
        Parameters
        ----------
        key : str
        
        value : T
        
        
        """
    @staticmethod
    def GetMetadataByDictKey(*args, **kwargs):
        """
        
        GetMetadataByDictKey(key, keyPath, value) -> bool
        
        
        Retrieves the value at ``keyPath`` from the fallback dictionary value
        for the dictionary metadata field named ``key`` , that is defined by
        this prim definition for the prim itself, and stores it in ``value``
        if possible.
        
        
        Returns true if a fallback dictionary value is defined for the given
        metadata ``key`` and it contains a value at ``keyPath`` . Returns
        false otherwise.
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        value : T
        
        
        """
    @staticmethod
    def GetPropertyDocumentation(*args, **kwargs):
        """
        
        GetPropertyDocumentation(propName) -> str
        
        
        Returns the documentation metadata defined by the prim definition for
        the property named ``propName`` if it exists.
        
        
        Parameters
        ----------
        propName : str
        
        
        """
    @staticmethod
    def GetPropertyMetadata(*args, **kwargs):
        """
        
        GetPropertyMetadata(propName, key, value) -> bool
        
        
        Retrieves the fallback value for the metadata field named ``key`` ,
        that is defined by this prim definition for the property named
        ``propName`` , and stores it in ``value`` if possible.
        
        
        Returns true if a fallback value is defined for the given metadata
        ``key`` for the named property. Returns false otherwise.
        
        
        Parameters
        ----------
        propName : str
        
        key : str
        
        value : T
        
        
        """
    @staticmethod
    def GetPropertyMetadataByDictKey(*args, **kwargs):
        """
        
        GetPropertyMetadataByDictKey(propName, key, keyPath, value) -> bool
        
        
        Retrieves the value at ``keyPath`` from the fallback dictionary value
        for the dictionary metadata field named ``key`` , that is defined by
        this prim definition for the property named ``propName`` , and stores
        it in ``value`` if possible.
        
        
        Returns true if a fallback dictionary value is defined for the given
        metadata ``key`` for the named property and it contains a value at
        ``keyPath`` . Returns false otherwise.
        
        
        Parameters
        ----------
        propName : str
        
        key : str
        
        keyPath : str
        
        value : T
        
        
        """
    @staticmethod
    def GetPropertyNames(*args, **kwargs):
        """
        
        GetPropertyNames() -> list[str]
        
        
        Return the list of names of builtin properties for this prim
        definition.
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeSpec(*args, **kwargs):
        """
        
        GetSchemaAttributeSpec(attrName) -> AttributeSpec
        
        
        This is a convenience method.
        
        
        It is shorthand for TfDynamic_cast<SdfAttributeSpecHandle>(
        GetSchemaPropertySpec(primType, attrName));
        
        
        Parameters
        ----------
        attrName : str
        
        
        """
    @staticmethod
    def GetSchemaPropertySpec(*args, **kwargs):
        """
        
        GetSchemaPropertySpec(propName) -> PropertySpec
        
        
        Return the property spec that defines the fallback for the property
        named *propName* on prims of this prim definition's type.
        
        
        Return null if there is no such property spec.
        
        
        Parameters
        ----------
        propName : str
        
        
        """
    @staticmethod
    def GetSchemaRelationshipSpec(*args, **kwargs):
        """
        
        GetSchemaRelationshipSpec(relName) -> RelationshipSpec
        
        
        This is a convenience method.
        
        
        It is shorthand for TfDynamic_cast<SdfRelationshipSpecHandle>(
        GetSchemaPropertySpec(primType, relName));
        
        
        Parameters
        ----------
        relName : str
        
        
        """
    @staticmethod
    def ListMetadataFields(*args, **kwargs):
        """
        
        ListMetadataFields() -> list[str]
        
        
        Returns the list of names of metadata fields that are defined by this
        prim definition for the prim itself.
        
        
        
        """
    @staticmethod
    def ListPropertyMetadataFields(*args, **kwargs):
        """
        
        ListPropertyMetadataFields(propName) -> list[str]
        
        
        Returns the list of names of metadata fields that are defined by this
        prim definition for property ``propName`` if a property named
        ``propName`` exists.
        
        
        Parameters
        ----------
        propName : str
        
        
        """
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
    """
    
    An forward-iterable range that traverses a subtree of prims rooted at
    a given prim in depth-first order.
    
    In addition to depth-first order, UsdPrimRange provides the optional
    ability to traverse in depth-first pre- and post-order wher prims
    appear twice in the range; first before all descendants and then again
    immediately after all descendants. This is useful for maintaining
    state associated with subtrees, in a stack-like fashion. See
    UsdPrimRange::iterator::IsPostVisit() to detect when an iterator is
    visiting a prim for the second time.
    
    There are several constructors providing different levels of
    configurability; ultimately, one can provide a prim predicate for a
    custom iteration, just as one would use UsdPrim::GetFilteredChildren()
    in a custom recursion.
    
    Why would one want to use a UsdPrimRange rather than just iterating
    over the results of UsdPrim::GetFilteredDescendants() ? Primarily, if
    one of the following applies:
    
       - You need to perform pre-and-post-order processing
    
       - You may want to prune sub-trees from processing (see
         UsdPrimRange::iterator::PruneChildren() )
    
       - You want to treat the root prim itself uniformly with its
         descendents (GetFilteredDescendants() will not return the root prim
         itself, while UsdPrimRange will - see UsdPrimRange::Stage for an
         exception).
         **Using UsdPrimRange in C++**
    
    UsdPrimRange provides standard container-like semantics. For example:
    
    .. code-block:: text
    
      // simple range-for iteration
      for (UsdPrim prim: UsdPrimRange(rootPrim)) {
          ProcessPrim(prim);
      }
      
      // using stl algorithms
      std::vector<UsdPrim> meshes;
      auto range = stage->Traverse();
      std::copy_if(range.begin(), range.end(), std::back_inserter(meshes),
                   [](UsdPrim const &) { return prim.IsA<UsdGeomMesh>(); });
      
      // iterator-based iterating, with subtree pruning
      UsdPrimRange range(rootPrim);
      for (auto iter = range.begin(); iter != range.end(); ++iter) {
          if (UsdModelAPI(\\*iter).GetKind() == KindTokens->component) {
              iter.PruneChildren();
          }
          else {
              nonComponents.push_back(\\*iter);
          }
      }
    
    **Using Usd.PrimRange in python**
    
    The python wrapping for PrimRange is python-iterable, so it can used
    directly as the object of a"for x in\\.\\.\\."clause; however in that
    usage one loses access to PrimRange methods such as PruneChildren()
    and IsPostVisit(). Simply create the iterator outside the loop to
    overcome this limitation. Finally, in python, prim predicates must be
    combined with bit-wise operators rather than logical operators because
    the latter are not overridable.
    
    .. code-block:: text
    
      # simple iteration
      for prim in Usd.PrimRange(rootPrim):
          ProcessPrim(prim)
      
      # filtered range using iterator to invoke iterator methods
      it = iter(Usd.PrimRange.Stage(stage, Usd.PrimIsLoaded  &  ~Usd.PrimIsAbstract))
      for prim in it:
          if Usd.ModelAPI(prim).GetKind() == Kind.Tokens.component:
              it.PruneChildren()
          else:
              nonComponents.append(prim)
    
    Finally, since iterators in python are not directly dereferencable, we
    provide the *python* *only* methods GetCurrentPrim() and IsValid(),
    documented in the python help system.
    
    """
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
        """
        
        **classmethod** AllPrims(start) -> PrimRange
        
        
        Construct a PrimRange that traverses the subtree rooted at ``start``
        in depth-first order, visiting all prims (including deactivated,
        undefined, and abstract prims).
        
        
        Parameters
        ----------
        start : Prim
        
        
        """
    @staticmethod
    def AllPrimsPreAndPostVisit(*args, **kwargs):
        """
        
        **classmethod** AllPrimsPreAndPostVisit(start) -> PrimRange
        
        
        Construct a PrimRange that traverses the subtree rooted at ``start``
        in depth-first order, visiting all prims (including deactivated,
        undefined, and abstract prims) with pre- and post-order visitation.
        
        
        Pre- and post-order visitation means that each prim appears twice in
        the range; not only prior to all its descendants as with an ordinary
        traversal but also immediately following its descendants. This lets
        client code maintain state for subtrees. See
        UsdPrimRange::iterator::IsPostVisit() .
        
        
        Parameters
        ----------
        start : Prim
        
        
        """
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        
        true if the iterator is not yet exhausted
        """
    @staticmethod
    def PreAndPostVisit(*args, **kwargs):
        """
        
        **classmethod** PreAndPostVisit(start) -> PrimRange
        
        
        Create a PrimRange that traverses the subtree rooted at ``start`` in
        depth-first order, visiting prims that pass the default predicate (as
        defined by UsdPrimDefaultPredicate) with pre- and post-order
        visitation.
        
        
        Pre- and post-order visitation means that each prim appears twice in
        the range; not only prior to all its descendants as with an ordinary
        traversal but also immediately following its descendants. This lets
        client code maintain state for subtrees. See
        UsdPrimRange::iterator::IsPostVisit() .
        
        
        Parameters
        ----------
        start : Prim
        
        
        
        ----------------------------------------------------------------------
        
        PreAndPostVisit(start, predicate) -> PrimRange
        
        
        Create a PrimRange that traverses the subtree rooted at ``start`` in
        depth-first order, visiting prims that pass ``predicate`` with pre-
        and post-order visitation.
        
        
        Pre- and post-order visitation means that each prim appears twice in
        the range; not only prior to all its descendants as with an ordinary
        traversal but also immediately following its descendants. This lets
        client code maintain state for subtrees. See
        UsdPrimRange::iterator::IsPostVisit() .
        
        
        Parameters
        ----------
        start : Prim
        
        predicate : _PrimFlagsPredicate
        
        
        """
    @staticmethod
    def Stage(*args, **kwargs):
        """
        
        **classmethod** Stage(stage, predicate) -> PrimRange
        
        
        Create a PrimRange that traverses all the prims on ``stage`` , and
        visits those that pass the default predicate (as defined by
        UsdPrimDefaultPredicate).
        
        
        Parameters
        ----------
        stage : Stage
        
        predicate : _PrimFlagsPredicate
        
        
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
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(start)
        
        
        Construct a PrimRange that traverses the subtree rooted at ``start``
        in depth-first order, visiting prims that pass the default predicate
        (as defined by UsdPrimDefaultPredicate).
        
        
        Parameters
        ----------
        start : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(start, predicate)
        
        
        Construct a PrimRange that traverses the subtree rooted at ``start``
        in depth-first order, visiting prims that pass ``predicate`` .
        
        
        Parameters
        ----------
        start : Prim
        
        predicate : _PrimFlagsPredicate
        
        
        
        ----------------------------------------------------------------------
        
        __init__(begin, end, proxyPrimPath, predicate)
        
        
        Parameters
        ----------
        begin : Usd_PrimData
        
        end : Usd_PrimData
        
        proxyPrimPath : Path
        
        predicate : _PrimFlagsPredicate
        
        
        """
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
    """
    
    Class that holds the full type information for a prim.
    
    
    It holds the type name, applied API schema names, and possibly a
    mapped schema type name which represent a unique full type. The info
    this holds is used to cache and provide the"real"schema type for the
    prim's type name regardless of whether it is a recognized prim type or
    not. The optional"mapped schema type name"is used to obtain a valid
    schema type for an unrecognized prim type name if the stage provides a
    fallback type for the unrecognized type. This class also provides
    access to the prim definition that defines all the built-in properties
    and metadata of a prim of this type.
    
    """
    @staticmethod
    def GetAppliedAPISchemas(*args, **kwargs):
        """
        
        GetAppliedAPISchemas() -> list[str]
        
        
        Returns the list of applied API schemas, directly authored on the
        prim, that impart additional properties on its prim definition.
        
        
        This does NOT include the applied API schemas that may be defined in
        the conrete prim type's prim definition\\.\\.
        
        
        
        """
    @staticmethod
    def GetEmptyPrimType(*args, **kwargs):
        """
        
        **classmethod** GetEmptyPrimType() -> PrimTypeInfo
        
        
        Returns the empty prim type info.
        
        
        
        """
    @staticmethod
    def GetPrimDefinition(*args, **kwargs):
        """
        
        GetPrimDefinition() -> PrimDefinition
        
        
        Returns the prim definition associated with this prim type's schema
        type and applied API schemas.
        
        
        
        """
    @staticmethod
    def GetSchemaType(*args, **kwargs):
        """
        
        GetSchemaType() -> Type
        
        
        Returns the TfType of the actual concrete schema that prims of this
        type will use to create their prim definition.
        
        
        Typically, this will be the type registered in the schema registry for
        the concrete prim type returned by GetTypeName. But if the stage
        provided this type info with a fallback type because the prim type
        name is not a recognized schema, this will return the provided
        fallback schema type instead.
        
        Fallback Prim Types
        
        
        
        """
    @staticmethod
    def GetSchemaTypeName(*args, **kwargs):
        """
        
        GetSchemaTypeName() -> str
        
        
        Returns the type name associated with the schema type returned from
        GetSchemaType.
        
        
        This will always be equivalent to calling
        UsdSchemaRegistry::GetConcreteSchemaTypeName on the type returned by
        GetSchemaType and will typically be the same as GetTypeName as long as
        the prim type name is a recognized prim type.
        
        Fallback Prim Types
        
        
        
        """
    @staticmethod
    def GetTypeName(*args, **kwargs):
        """
        
        GetTypeName() -> str
        
        
        Returns the concrete prim type name.
        
        
        
        """
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
    """
    
    Base class for UsdAttribute and UsdRelationship scenegraph objects.
    
    UsdProperty has a bool conversion operator that validates that the
    property IsDefined() and thus valid for querying and authoring values
    and metadata. This is a fairly expensive query that we do **not**
    cache, so if client code retains UsdProperty objects it should manage
    its object validity closely for performance. An ideal pattern is to
    listen for UsdNotice::StageContentsChanged notifications, and
    revalidate/refetch retained UsdObjects only then and otherwise use
    them without validity checking.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ClearDisplayGroup(*args, **kwargs):
        """
        
        ClearDisplayGroup() -> bool
        
        
        Clears this property's display group (metadata) in the current
        EditTarget (only).
        
        
        Returns true on success.
        
        
        
        """
    @staticmethod
    def ClearDisplayName(*args, **kwargs):
        """
        
        ClearDisplayName() -> bool
        
        
        Clears this property's display name (metadata) in the current
        EditTarget (only).
        
        
        Returns true on success.
        
        
        
        """
    @staticmethod
    def FlattenTo(*args, **kwargs):
        """
        
        FlattenTo(parent) -> Property
        
        
        Flattens this property to a property spec with the same name beneath
        the given ``parent`` prim in the edit target of its owning stage.
        
        
        The ``parent`` prim may belong to a different stage than this
        property's owning stage.
        
        Flattening authors all authored resolved values and metadata for this
        property into the destination property spec. If this property is a
        builtin property, fallback values and metadata will also be authored
        if the destination property has a different fallback value or no
        fallback value, or if the destination property has an authored value
        that overrides its fallback.
        
        Attribute connections and relationship targets that target an object
        beneath this property's owning prim will be remapped to target objects
        beneath the destination ``parent`` prim.
        
        If the destination spec already exists, it will be overwritten.
        
        UsdStage::Flatten
        
        
        Parameters
        ----------
        parent : Prim
        
        
        
        ----------------------------------------------------------------------
        
        FlattenTo(parent, propName) -> Property
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Flattens this property to a property spec with the given ``propName``
        beneath the given ``parent`` prim in the edit target of its owning
        stage.
        
        
        The ``parent`` prim may belong to a different stage than this
        property's owning stage.
        
        
        Parameters
        ----------
        parent : Prim
        
        propName : str
        
        
        
        ----------------------------------------------------------------------
        
        FlattenTo(property) -> Property
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Flattens this property to a property spec for the given ``property``
        in the edit target of its owning prim's stage.
        
        
        The ``property`` owning prim may belong to a different stage than this
        property's owning stage.
        
        
        Parameters
        ----------
        property : Property
        
        
        """
    @staticmethod
    def GetBaseName(*args, **kwargs):
        """
        
        GetBaseName() -> str
        
        
        Return this property's name with all namespace prefixes removed, i.e.
        
        
        the last component of the return value of GetName()
        
        This is generally the property's"client name"; property namespaces are
        often used to group related properties together. The namespace
        prefixes the property name but many consumers will care only about un-
        namespaced name, i.e. its BaseName. For more information, see Names,
        Namespace Ordering, and Property Namespaces
        
        
        
        """
    @staticmethod
    def GetDisplayGroup(*args, **kwargs):
        """
        
        GetDisplayGroup() -> str
        
        
        Return this property's display group (metadata).
        
        
        This returns the empty token if no display group has been set.
        
        SetDisplayGroup()
        
        
        
        """
    @staticmethod
    def GetDisplayName(*args, **kwargs):
        """
        
        GetDisplayName() -> str
        
        
        Return this property's display name (metadata).
        
        
        This returns the empty string if no display name has been set.
        
        SetDisplayName()
        
        
        
        """
    @staticmethod
    def GetNamespace(*args, **kwargs):
        """
        
        GetNamespace() -> str
        
        
        Return this property's complete namespace prefix.
        
        
        Return the empty token if this property has no namespaces.
        
        This is the complement of GetBaseName() , although it does *not*
        contain a trailing namespace delimiter
        
        
        
        """
    @staticmethod
    def GetNestedDisplayGroups(*args, **kwargs):
        """
        
        GetNestedDisplayGroups() -> list[str]
        
        
        Return this property's displayGroup as a sequence of groups to be
        nested, or an empty vector if displayGroup is empty or not authored.
        
        
        
        """
    @staticmethod
    def GetPropertyStack(*args, **kwargs):
        """
        
        GetPropertyStack(time) -> list[PropertySpec]
        
        
        Returns a strength-ordered list of property specs that provide
        opinions for this property.
        
        
        If ``time`` is UsdTimeCode::Default() , *or* this property is a
        UsdRelationship (which are never affected by clips), we will not
        consider value clips for opinions. For any other ``time`` , for a
        UsdAttribute, clips whose samples may contribute an opinion will be
        included. These specs are ordered from strongest to weakest opinion,
        although if ``time`` requires interpolation between two adjacent
        clips, both clips will appear, sequentially.
        
        The results returned by this method are meant for debugging and
        diagnostic purposes. It is **not** advisable to retain a PropertyStack
        for the purposes of expedited value resolution for properties, since
        the makeup of an attribute's PropertyStack may itself be time-varying.
        To expedite repeated value resolution of attributes, you should
        instead retain a ``UsdAttributeQuery`` .
        
        UsdClipsAPI
        
        
        Parameters
        ----------
        time : TimeCode
        
        
        """
    @staticmethod
    def GetPropertyStackWithLayerOffsets(*args, **kwargs):
        """
        
        GetPropertyStackWithLayerOffsets(time) -> list[tuple[PropertySpec, LayerOffset]]
        
        
        Returns a strength-ordered list of property specs that provide
        opinions for this property paired with the cumulative layer offset
        from the stage's root layer to the layer containing the property spec.
        
        
        This behaves exactly the same as UsdProperty::GetPropertyStack with
        the addition of providing the cumulative layer offset of each spec's
        layer.
        
        The results returned by this method are meant for debugging and
        diagnostic purposes. It is **not** advisable to retain a PropertyStack
        for the purposes of expedited value resolution for properties, since
        the makeup of an attribute's PropertyStack may itself be time-varying.
        To expedite repeated value resolution of attributes, you should
        instead retain a ``UsdAttributeQuery`` .
        
        
        Parameters
        ----------
        time : TimeCode
        
        
        """
    @staticmethod
    def HasAuthoredDisplayGroup(*args, **kwargs):
        """
        
        HasAuthoredDisplayGroup() -> bool
        
        
        Returns true if displayGroup was explicitly authored and GetMetadata()
        will return a meaningful value for displayGroup.
        
        
        
        
        
        """
    @staticmethod
    def HasAuthoredDisplayName(*args, **kwargs):
        """
        
        HasAuthoredDisplayName() -> bool
        
        
        Returns true if displayName was explicitly authored and GetMetadata()
        will return a meaningful value for displayName.
        
        
        
        
        
        """
    @staticmethod
    def IsAuthored(*args, **kwargs):
        """
        
        IsAuthored() -> bool
        
        
        Return true if there are any authored opinions for this property in
        any layer that contributes to this stage, false otherwise.
        
        
        
        """
    @staticmethod
    def IsAuthoredAt(*args, **kwargs):
        """
        
        IsAuthoredAt(editTarget) -> bool
        
        
        Return true if there is an SdfPropertySpec authored for this property
        at the given *editTarget*, otherwise return false.
        
        
        Note that this method does not do partial composition. It does not
        consider whether authored scene description exists at *editTarget* or
        weaker, only **exactly at** the given *editTarget*.
        
        
        Parameters
        ----------
        editTarget : EditTarget
        
        
        """
    @staticmethod
    def IsCustom(*args, **kwargs):
        """
        
        IsCustom() -> bool
        
        
        Return true if this is a custom property (i.e., not part of a prim
        schema).
        
        
        The'custom'modifier in USD serves the same function as
        Alembic's'userProperties', which is to say as a categorization for ad
        hoc client data not formalized into any schema, and therefore not
        carrying an expectation of specific processing by consuming
        applications.
        
        
        
        """
    @staticmethod
    def IsDefined(*args, **kwargs):
        """
        
        IsDefined() -> bool
        
        
        Return true if this is a builtin property or if the strongest authored
        SdfPropertySpec for this property's path matches this property's
        dynamic type.
        
        
        That is, SdfRelationshipSpec in case this is a UsdRelationship, and
        SdfAttributeSpec in case this is a UsdAttribute. Return ``false`` if
        this property's prim has expired.
        
        For attributes, a ``true`` return does not imply that this attribute
        possesses a value, only that has been declared, is of a certain type
        and variability, and that it is safe to use to query and author values
        and metadata.
        
        
        
        """
    @staticmethod
    def SetCustom(*args, **kwargs):
        """
        
        SetCustom(isCustom) -> bool
        
        
        Set the value for custom at the current EditTarget, return true on
        success, false if the value can not be written.
        
        
        **Note** that this value should not be changed as it is typically
        either automatically authored or provided by a property definition.
        This method is provided primarily for fixing invalid scene
        description.
        
        
        Parameters
        ----------
        isCustom : bool
        
        
        """
    @staticmethod
    def SetDisplayGroup(*args, **kwargs):
        """
        
        SetDisplayGroup(displayGroup) -> bool
        
        
        Sets this property's display group (metadata).
        
        
        Returns true on success.
        
        DisplayGroup provides UI hinting for grouping related properties
        together for display. We define a convention for specifying nesting of
        groups by recognizing the property namespace separator in displayGroup
        as denoting group-nesting.
        
        SetNestedDisplayGroups()
        
        
        Parameters
        ----------
        displayGroup : str
        
        
        """
    @staticmethod
    def SetDisplayName(*args, **kwargs):
        """
        
        SetDisplayName(name) -> bool
        
        
        Sets this property's display name (metadata).
        
        
        Returns true on success.
        
        DisplayName is meant to be a descriptive label, not necessarily an
        alternate identifier; therefore there is no restriction on which
        characters can appear in it.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def SetNestedDisplayGroups(*args, **kwargs):
        """
        
        SetNestedDisplayGroups(nestedGroups) -> bool
        
        
        Sets this property's display group (metadata) to the nested sequence.
        
        
        Returns true on success.
        
        A displayGroup set with this method can still be retrieved with
        GetDisplayGroup() , with the namespace separator embedded in the
        result. If ``nestedGroups`` is empty, we author an empty string for
        displayGroup.
        
        SetDisplayGroup()
        
        
        Parameters
        ----------
        nestedGroups : list[str]
        
        
        """
    @staticmethod
    def SplitName(*args, **kwargs):
        """
        
        SplitName() -> list[str]
        
        
        Return this property's name elements including namespaces and its base
        name as the final element.
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : _Null[Derived]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(objType, prim, proxyPrimPath, propName)
        
        
        Parameters
        ----------
        objType : UsdObjType
        
        prim : Usd_PrimData
        
        proxyPrimPath : Path
        
        propName : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__()
        
        
        Construct an invalid property.
        
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class References(Boost.Python.instance):
    """
    
    UsdReferences provides an interface to authoring and introspecting
    references in Usd.
    
    References are the primary operator for"encapsulated aggregation"of
    scene description. *aggregation* means that references let us build up
    rich scenes by composing scene description recorded in a (most often)
    different layer. A scene can reference the same layer many times at
    different locations in a scene's namespace. Referenced scene
    description can be overridden in the referencing (or stronger) layers,
    allowing each instance of the reference to be directly
    customized/overridden. *Encapsulated* means that regardless of how
    much scene description is in the referenced layer, only the scene
    description under and composed from (via other composition arcs in the
    referenced layer) the targeted prim will be composed into the
    aggregate scene. Multiple references to the same layer will result in
    the layer being opened and retained in memory only once, although each
    referencing prim will compose unique prim indices for the tree rooted
    at the referenced prim.
    
    Important Qualities and Effective Use of References
    ===================================================
    
       - Any prim can host zero, one or multiple references
    
       - References are list editable; that is, they compose differently
         than ordinary properties and metadata. In any given LayerStack, each
         authored reference operation at the same SdfPath location in each
         layer (i.e. on the same prim) will compose into an aggregate result by
         adding to, removing from, or replacing"weaker"references.
    
       - References can target the same LayerStack in which they are
         authored, as long as doing so does not introduce a cycle in the
         composition graph. See Expressing"internal"references to the
         containing LayerStack
    
       - The ``identifier`` component of a reference in the provided API
         can be a resolvable asset-path to some external layer, empty, in which
         case the reference targets the root layer of the LayerStack containing
         the referencing layer, or the identifier of an existing anonymous, in-
         memory-only SdfLayer. Care should be exercised in the latter case:
         calling Export() on an anonymous layer to serialize it to a file will
         not attempt to replace any references to anonymous layers with
         references to file-backed layers.
    
       - Opinions brought in by reference on an ancestor prim are weaker
         than opinions brought in by references on a descendant prim.
    
    References may omit the target prim path if the referenced layer has
    the'defaultPrim'metadata set. In this case, the reference targets
    the'defaultPrim'in the referenced layer. A layer's defaultPrim can be
    authored and accessed on a UsdStage whose root layer is the layer in
    question: see UsdStage::GetDefaultPrim() and
    UsdStage::SetDefaultPrim() . One can also author defaultPrim directly
    on an SdfLayer - see SdfLayer::GetDefaultPrim() ,
    SdfLayer::SetDefaultPrim() .
    
    References may omit the identifier specifying the referenced layer.
    This creates an"internal"reference. During composition, the referenced
    layer will be resolved to the root layer of the LayerStack containing
    the layer where the reference was authored. See AddInternalReference()
    .
    
    References may target any prim in a layer. In the simplest and most
    common case, a root prim in a layer will be referenced. However,
    referencing sub-root prims can be useful in a variety of other cases;
    for example, a user might organize prims into a meaningful hierarchy
    in a layer for display purposes, then use sub-root references to
    reference a selection from that hierarchy into a scene.
    
    Sub-root references have subtle behaviors with respect to opinions and
    composition arcs authored on ancestors of the referenced prim. Users
    should carefully consider this when deciding whether to use sub-root
    references. These issues can be avoided by not authoring any
    properties or metadata on ancestors of prims that are meant to be
    referenced.
    
    Consider the following example:
    
    .. code-block:: text
    
      \\* shot.usda                                 | \\* asset.usda
                                                  |
      #usda 1.0                                   | #usda 1.0
                                                  |
      over "Class"                                | class "Class"
      {                                           | {
          over "B"                                | }
          {                                       |
              over "Model"                        | def "A" (
              {                                   |    inherits = </Class>
                  int a = 3                       | )
              }                                   | {
          }                                       |     token purpose = "render"
      }                                           |
                                                  |     def "B" (
      over "A"                                    |        variantSets = "type"
      {                                           |        variants = {
          over "B" (                              |             string type = "a"
              # variant selection won't be used   |        }
              variants = {                        |     )
                  string type = "b"               |     {
              }                                   |         variantSet "type" = {
          )                                       |             "a" {
          {                                       |                 def "Model"
          }                                       |                 {
      }                                           |                     int a = 1
                                                  |                 }
      def "ReferencedModel" (                     |             }
          references = @./asset.usda@</A/B/Model> |             "b" {
      )                                           |                 def "Model"
      {                                           |                 {
      }                                           |                     int a = 2
                                                  |                 }
                                                  |             }
                                                  |         }
                                                  |     }
                                                  | }
    
       - Property and metadata opinions on the ancestors of the referenced
         prim *are not* present in the composed stage and will never contribute
         to any computations. In this example, the opinion for the attribute
         /A.purpose in asset.usda will never be visible in the UsdStage for
         shot.usda.
    
       - Property and metadata opinions due to ancestral composition arcs
         *are* present in the composed stage. In this example, the attribute
         /Class/B/Model.a in shot.usda will be present in the UsdStage for
         shot.usda, even though the inherit arc is authored on an ancestor of
         the referenced prim.
    
       - A consequence of these rules is that users might not be able to
         override ancestral variant selections that affect the referenced prim.
         In this example, the Model prim being referenced comes from the
         variant selection {type=a} on prim /A/B in asset.usda. The {type=b}
         variant cannot be selected in shot.usda, even if prims with the same
         hierarchy happen to exist there. There are various workarounds for
         this; in this example, the {type=b} variant selection could be
         authored on /Class/B/Model in shot.usda instead because of the inherit
         arc that was established on prim /A.
    
    AddReference() and SetReferences() can each fail for a number of
    reasons. If one of the specified prim targets for one of the
    references is not a prim, we will generate an error, fail to author
    any scene description, and return ``false`` . If anything goes wrong
    in attempting to write the reference, we also return false, and the
    reference will also remain unauthored. Otherwise, if the reference was
    successfully authored, we will return ``true`` . **A successful
    reference authoring operation may still generate composition errors!**
    Just because the reference you specified was syntactically correct and
    therefore successfully authored, does not imply it was meaningful. If
    you wish to ensure that the reference you are about to author will be
    meaningfully consumable by your stage, you are strongly encouraged to
    **ensure it will resolve to an actual file by using
    UsdStage::ResolveIdentifierToEditTarget() before authoring the
    reference.**
    
    When adding an internal reference, the given prim path is expected to
    be in the namespace of the owning prim's stage. Sub-root prim paths
    will be translated from this namespace to the namespace of the current
    edit target, if necessary. If a path cannot be translated, a coding
    error will be issued and no changes will be made. Non-sub-root paths
    will not be translated.
    
    Immediately upon successful authoring of the reference (before
    returning from AddReference() , RemoveReference() , ClearReferences()
    , or SetReferences() ), the UsdStage on which the reference was
    authored will recompose the subtree rooted at the prim hosting the
    reference. If the provided identifier does not resolve to a layer that
    is already opened or that can be opened in the usd format, *or* if the
    provided primPath is not an actual prim in that layer, the stage's
    recomposition will fail, and pass on composition errors to the client.
    
    """
    @staticmethod
    def AddInternalReference(*args, **kwargs):
        """
        
        AddInternalReference(primPath, layerOffset, position) -> bool
        
        
        Add an internal reference to the specified prim.
        
        
        
        Internal References
        
        
        Parameters
        ----------
        primPath : Path
        
        layerOffset : LayerOffset
        
        position : ListPosition
        
        
        """
    @staticmethod
    def AddReference(*args, **kwargs):
        """
        
        AddReference(ref, position) -> bool
        
        
        Adds a reference to the reference listOp at the current EditTarget, in
        the position specified by ``position`` .
        
        
        
        Why adding references may fail for explanation of expectations on
        ``ref`` and what return values and errors to expect, and ListOps and
        List Editing for details on list editing and composition of listOps.
        
        
        Parameters
        ----------
        ref : Reference
        
        position : ListPosition
        
        
        
        ----------------------------------------------------------------------
        
        AddReference(identifier, primPath, layerOffset, position) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        identifier : str
        
        primPath : Path
        
        layerOffset : LayerOffset
        
        position : ListPosition
        
        
        
        ----------------------------------------------------------------------
        
        AddReference(identifier, layerOffset, position) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        
        References Without Prim Paths
        
        
        Parameters
        ----------
        identifier : str
        
        layerOffset : LayerOffset
        
        position : ListPosition
        
        
        """
    @staticmethod
    def ClearReferences(*args, **kwargs):
        """
        
        ClearReferences() -> bool
        
        
        Removes the authored reference listOp edits at the current EditTarget.
        
        
        The same caveats for Remove() apply to Clear(). In fact, Clear() may
        actually increase the number of composed references, if the listOp
        being cleared contained the"remove"operator.
        
        ListOps and List Editing
        
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        Return the prim this object is bound to.
        
        
        
        
        ----------------------------------------------------------------------
        
        GetPrim() -> Prim
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        
        """
    @staticmethod
    def RemoveReference(*args, **kwargs):
        """
        
        RemoveReference(ref) -> bool
        
        
        Removes the specified reference from the references listOp at the
        current EditTarget.
        
        
        This does not necessarily eliminate the reference completely, as it
        may be added or set in another layer in the same LayerStack as the
        current EditTarget.
        
        ListOps and List Editing
        
        
        Parameters
        ----------
        ref : Reference
        
        
        """
    @staticmethod
    def SetReferences(*args, **kwargs):
        """
        
        SetReferences(items) -> bool
        
        
        Explicitly set the references, potentially blocking weaker opinions
        that add or remove items.
        
        
        
        Why adding references may fail for explanation of expectations on
        ``ref`` and what return values and errors to expect, and ListOps and
        List Editing for details on list editing and composition of listOps.
        
        
        Parameters
        ----------
        items : list[Reference]
        
        
        """
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
    """
    
    A UsdRelationship creates dependencies between scenegraph objects by
    allowing a prim to *target* other prims, attributes, or relationships.
    
    Relationship Characteristics
    ============================
    
    A UsdRelationship is a pointer to other objects, which are named by
    their scenegraph paths. When authoring relationships, the *target*
    parameters should be scenegraph paths in the composed namespace of the
    UsdStage into which you are authoring. If your edits are targeted to a
    different layer, across various composition arcs (because you
    specified a non-default UsdEditTarget), the target's path will be
    automatically translated into the proper namespace.
    
    A single UsdRelationship can target multiple other objects, which can
    be of UsdPrim, UsdAttribute, or UsdRelationship type. UsdRelationship
    participates in"list editing", which means that stronger layers in a
    composed scene can add, remove, or reorder targets authored on the
    relationship in weaker layers *without* stomping the weaker opinions,
    although stomping behavior is still possible, via SetTargets() .
    
    An authored relationship creates a dependency of the targeting prim on
    the targeted prim(s). We consider these dependencies to
    be"loaddependencies", which means that when we load the targeting
    prim's"load group", we will also load the targeted prims'load groups,
    to ensure that all the data required to render the model containing
    the targeting prim is composed and available.
    
    Like UsdAttribute, UsdRelationship objects are meant to be ephemeral,
    live on the stack, and be cheap to refetch from their owning UsdPrim.
    
    Unlike UsdAttribute s, which can either be uniform over all time or
    vary in value over time, UsdRelationship is **always uniform**.
    
    Relationship Restrictions
    =========================
    
    When authoring relationship targets in a stage's local LayerStack, all
    target paths are legal (Note we may restrict this prior to launch to
    only allowing targeting of already-extant scenegraph objects).
    However, a relationship target that is legal in a local LayerStack may
    become unreachable when the stage's root layer is *referenced* into an
    aggregate, and will cause an error when attempting to load/compose the
    aggregate.
    
    This can happen because references encapsulate just the tree whose
    root is targeted in the reference - no other scene description in the
    referenced layer will be composed into the aggregate. So if some
    descendant prim of the referenced root targets a relationship to
    another tree in the same layer, that relationship would dangle, and
    the client will error in GetTargets() or GetForwardedTargets() .
    
    Authoring targets to objects within prototypes is not allowed, since
    prototype prims do not have a stable identity across runs. Consumers
    must author targets to the object within an instance instead.
    
    Relationships authored in a descendent prim of a referenced prim may
    not target the referenced prim itself or any of its immediate child
    properties if the referencing prim is instanceable. Allowing this
    would break the ability for this relationship to be instanced and
    shared by multiple instances  it would force consumers of
    relationships within prototypes to resolve targets in the context of
    each of that prototype's instances.
    
    Relationship Forwarding
    =======================
    
    Because a relationship can target another relationship, we can and do
    provide the ability to resolve chained or *forwarded* relationships.
    This can be useful in several situations, including:
    
       - Combining relationships with VariantSets to create
         demultiplexers. A prim can host a relationship that serves as
         a"binding post"for other prims to target. The prim also hosts
         a"bindingVariant" UsdVariantSet whose variants each modulate the
         target of the binding-post relationship. We can now change the
         *forwarded* target of all prims targeting the binding-post by simply
         switching the bindingVariant VariantSet. We will work through this
         example in the USD reference manual.
    
       - Defining a relationship as part of a model's interface (so that
         it can be targeted in model hierarchy with no models loaded), which,
         inside the model's payload, forwards to prims useful to a client, the
         set of which may vary depending on the model's configured VariantSets.
    
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def AddTarget(*args, **kwargs):
        """
        
        AddTarget(target, position) -> bool
        
        
        Adds ``target`` to the list of targets, in the position specified by
        ``position`` .
        
        
        Passing paths to prototype prims or any other objects in prototypes
        will cause an error to be issued. It is not valid to author targets to
        these objects.
        
        What data this actually authors depends on what data is currently
        authored in the authoring layer, with respect to list-editing
        semantics, which we will document soon
        
        
        Parameters
        ----------
        target : Path
        
        position : ListPosition
        
        
        """
    @staticmethod
    def ClearTargets(*args, **kwargs):
        """
        
        ClearTargets(removeSpec) -> bool
        
        
        Remove all opinions about the target list from the current edit
        target.
        
        
        Only remove the spec if ``removeSpec`` is true (leave the spec to
        preserve meta-data we may have intentionally authored on the
        relationship)
        
        
        Parameters
        ----------
        removeSpec : bool
        
        
        """
    @staticmethod
    def GetForwardedTargets(*args, **kwargs):
        """
        
        GetForwardedTargets(targets) -> bool
        
        
        Compose this relationship's *ultimate* targets, taking into
        account"relationship forwarding", and fill ``targets`` with the
        result.
        
        
        All preexisting elements in ``targets`` are lost. This method never
        inserts relationship paths in ``targets`` .
        
        Returns true if any of the visited relationships that are not"purely
        forwarding"has an authored opinion for its target paths and no
        composition errors were encountered while computing any targets.
        Purely forwarding, in this context, means the relationship has at
        least one target but all of its targets are paths to other
        relationships. Note that authored opinions may include opinions that
        clear the targets and a return value of true does not necessarily
        indicate that ``targets`` will not be empty.
        
        Returns false otherwise. When composition errors occur, this function
        continues to collect successfully composed targets, but returns false
        to indicate to the caller that errors occurred.
        
        When a forwarded target cannot be determined, e.g. due to a
        composition error, no value is returned for that target; the
        alternative would be to return the relationship path at which the
        forwarded targets could not be composed, however this would require
        all callers of GetForwardedTargets() to account for unexpected
        relationship paths being returned with the expected target results.
        For example, a particular caller may expect only prim paths in the
        target vector, but when composition errors occur, relationships would
        be included, potentially triggering additional down stream errors.
        
        See Relationship Forwarding for details on the semantics.
        
        The result is not cached, so will be recomputed on every query.
        
        
        Parameters
        ----------
        targets : list[Path]
        
        
        """
    @staticmethod
    def GetTargets(*args, **kwargs):
        """
        
        GetTargets(targets) -> bool
        
        
        Compose this relationship's targets and fill ``targets`` with the
        result.
        
        
        All preexisting elements in ``targets`` are lost.
        
        Returns true if any target path opinions have been authored and no
        composition errors were encountered, returns false otherwise. Note
        that authored opinions may include opinions that clear the targets and
        a return value of true does not necessarily indicate that ``targets``
        will contain any target paths.
        
        See Relationship Targets and Attribute Connections for details on
        behavior when targets point to objects beneath instance prims.
        
        The result is not cached, so will be recomputed on every query.
        
        
        Parameters
        ----------
        targets : list[Path]
        
        
        """
    @staticmethod
    def HasAuthoredTargets(*args, **kwargs):
        """
        
        HasAuthoredTargets() -> bool
        
        
        Returns true if any target path opinions have been authored.
        
        
        Note that this may include opinions that clear targets and may not
        indicate that target paths will exist for this relationship.
        
        
        
        """
    @staticmethod
    def RemoveTarget(*args, **kwargs):
        """
        
        RemoveTarget(target) -> bool
        
        
        Removes ``target`` from the list of targets.
        
        
        Passing paths to prototype prims or any other objects in prototypes
        will cause an error to be issued. It is not valid to author targets to
        these objects.
        
        
        Parameters
        ----------
        target : Path
        
        
        """
    @staticmethod
    def SetTargets(*args, **kwargs):
        """
        
        SetTargets(targets) -> bool
        
        
        Make the authoring layer's opinion of the targets list explicit, and
        set exactly to ``targets`` .
        
        
        Passing paths to prototype prims or any other objects in prototypes
        will cause an error to be issued. It is not valid to author targets to
        these objects.
        
        If any target in ``targets`` is invalid, no targets will be authored
        and this function will return false.
        
        
        Parameters
        ----------
        targets : list[Path]
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct an invalid relationship.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim, proxyPrimPath, relName)
        
        
        Parameters
        ----------
        prim : Usd_PrimData
        
        proxyPrimPath : Path
        
        relName : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__(objType, prim, proxyPrimPath, propName)
        
        
        Parameters
        ----------
        objType : UsdObjType
        
        prim : Usd_PrimData
        
        proxyPrimPath : Path
        
        propName : str
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class ResolveInfo(Boost.Python.instance):
    """
    
    Container for information about the source of an attribute's value,
    i.e. the'resolved'location of the attribute.
    
    For more details, see TimeSamples, Defaults, and Value Resolution.
    
    """
    __instance_size__: typing.ClassVar[int] = 96
    @staticmethod
    def GetNode(*args, **kwargs):
        """
        
        GetNode() -> NodeRef
        
        
        Return the node within the containing PcpPrimIndex that provided the
        resolved value opinion.
        
        
        
        """
    @staticmethod
    def GetSource(*args, **kwargs):
        """
        
        GetSource() -> ResolveInfoSource
        
        
        Return the source of the associated attribute's value.
        
        
        
        """
    @staticmethod
    def ValueIsBlocked(*args, **kwargs):
        """
        
        ValueIsBlocked() -> bool
        
        
        Return true if this UsdResolveInfo represents an attribute whose value
        is blocked.
        
        
        
        UsdAttribute::Block()
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        """
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
    """
    
    Defines a subrange of nodes and layers within a prim's prim index to
    consider when performing value resolution for the prim's attributes. A
    resolve target can then be passed to UsdAttributeQuery during its
    construction to have all of the queries made by the UsdAttributeQuery
    use the resolve target's subrange for their value resolution.
    
    Resolve targets can be created via methods on
    UsdPrimCompositionQueryArc to to limit value resolution to a subrange
    of the prim's composed specs that are no stronger that arc, or a
    subrange of specs that is strictly stronger than that arc (optionally
    providing a particular layer within the arc's layer stack to further
    limit the range of specs).
    
    Alternatively, resolve targets can also be created via methods on
    UsdPrim that can limit value resolution to either up to or stronger
    than the spec that would be edited when setting a value for the prim
    using the given UsdEditTarget.
    
    Unlike UsdEditTarget, a UsdResolveTarget is only relevant to the prim
    it is created for and can only be used in a UsdAttributeQuery for
    attributes on this prim.
    
    Invalidation
    ============
    
    This object does not listen for change notification. If a consumer is
    holding on to a UsdResolveTarget, it is their responsibility to
    dispose of it in response to a resync change to the associated prim.
    Failing to do so may result in incorrect values or crashes due to
    dereferencing invalid objects.
    
    """
    __instance_size__: typing.ClassVar[int] = 112
    @staticmethod
    def GetPrimIndex(*args, **kwargs):
        """
        
        GetPrimIndex() -> PrimIndex
        
        
        Get the prim index of the resolve target.
        
        
        
        """
    @staticmethod
    def GetStartLayer(*args, **kwargs):
        """
        
        GetStartLayer() -> Layer
        
        
        Returns the layer in the layer stack of the start node that value
        resolution with this resolve target will start at.
        
        
        
        """
    @staticmethod
    def GetStartNode(*args, **kwargs):
        """
        
        GetStartNode() -> NodeRef
        
        
        Returns the node that value resolution with this resolve target will
        start at.
        
        
        
        """
    @staticmethod
    def GetStopLayer(*args, **kwargs):
        """
        
        GetStopLayer() -> Layer
        
        
        Returns the layer in the layer stack of the stop node that value
        resolution with this resolve target will stop at.
        
        
        
        """
    @staticmethod
    def GetStopNode(*args, **kwargs):
        """
        
        GetStopNode() -> NodeRef
        
        
        Returns the node that value resolution with this resolve target will
        stop at when the"stop at"layer is reached.
        
        
        
        """
    @staticmethod
    def IsNull(*args, **kwargs):
        """
        
        IsNull() -> bool
        
        
        Returns true if this is a null resolve target.
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(index, node, layer)
        
        
        Parameters
        ----------
        index : PrimIndex
        
        node : NodeRef
        
        layer : Layer
        
        
        
        ----------------------------------------------------------------------
        
        __init__(index, node, layer, stopNode, stopLayer)
        
        
        Parameters
        ----------
        index : PrimIndex
        
        node : NodeRef
        
        layer : Layer
        
        stopNode : NodeRef
        
        stopLayer : Layer
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class SchemaBase(Boost.Python.instance):
    """
    
    The base class for all schema types in Usd.
    
    Schema objects hold a UsdPrim internally and provide a layer of
    specific named API atop the underlying scene graph.
    
    Schema objects are polymorphic but they are intended to be created as
    automatic local variables, so they may be passed and returned by-
    value. This leaves them subject to slicing. This means that if one
    passes a ``SpecificSchema`` instance to a function that takes a
    UsdSchemaBase *by-value*, all the polymorphic behavior specific to
    ``SpecificSchema`` is lost.
    
    To avoid slicing, it is encouraged that functions taking schema object
    arguments take them by ``const&`` if const access is sufficient,
    otherwise by non-const pointer.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def GetPath(*args, **kwargs):
        """
        
        GetPath() -> Path
        
        
        Shorthand for GetPrim() -> GetPath() .
        
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        Return this schema object's held prim.
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetSchemaClassPrimDefinition(*args, **kwargs):
        """
        
        GetSchemaClassPrimDefinition() -> PrimDefinition
        
        
        Return the prim definition associated with this schema instance if one
        exists, otherwise return null.
        
        
        This does not use the held prim's type. To get the held prim
        instance's definition, use UsdPrim::GetPrimDefinition() .
        
        UsdPrim::GetPrimDefinition()
        
        
        
        """
    @staticmethod
    def GetSchemaKind(*args, **kwargs):
        """
        
        GetSchemaKind() -> SchemaKind
        
        
        Returns the kind of schema this class is.
        
        
        
        """
    @staticmethod
    def IsAPISchema(*args, **kwargs):
        """
        
        IsAPISchema() -> bool
        
        
        Returns whether this is an API schema or not.
        
        
        
        """
    @staticmethod
    def IsAppliedAPISchema(*args, **kwargs):
        """
        
        IsAppliedAPISchema() -> bool
        
        
        Returns whether this is an applied API schema or not.
        
        
        If this returns true this class will have an Apply() method
        
        
        
        """
    @staticmethod
    def IsConcrete(*args, **kwargs):
        """
        
        IsConcrete() -> bool
        
        
        Returns whether or not this class corresponds to a concrete
        instantiable prim type in scene description.
        
        
        If this is true, GetStaticPrimDefinition() will return a valid prim
        definition with a non-empty typeName.
        
        
        
        """
    @staticmethod
    def IsMultipleApplyAPISchema(*args, **kwargs):
        """
        
        IsMultipleApplyAPISchema() -> bool
        
        
        Returns whether this is an applied API schema or not.
        
        
        If this returns true the constructor, Get and Apply methods of this
        class will take in the name of the API schema instance.
        
        
        
        """
    @staticmethod
    def IsTyped(*args, **kwargs):
        """
        
        IsTyped() -> bool
        
        
        Returns whether or not this class inherits from UsdTyped.
        
        
        Types which inherit from UsdTyped can impart a typename on a UsdPrim.
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __getattribute__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct and store ``prim`` as the held prim.
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(otherSchema)
        
        
        Construct and store for the same prim held by ``otherSchema`` .
        
        
        Parameters
        ----------
        otherSchema : SchemaBase
        
        
        """
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
    """
    
    Singleton registry that provides access to schema type information and
    the prim definitions for registered Usd"IsA"and applied API schema
    types. It also contains the data from the generated schemas that is
    used by prim definitions to provide properties and fallbacks.
    
    The data contained herein comes from the generatedSchema.usda file
    (generated when a schema.usda file is processed by *usdGenSchema*) of
    each schema-defining module. The registry expects each schema type to
    be represented as a single prim spec with its inheritance flattened,
    i.e. the prim spec contains a union of all its local and class
    inherited property specs and metadata fields.
    
    It is used by the Usd core, via UsdPrimDefinition, to determine how to
    create scene description for unauthored"built-in"properties of schema
    classes, to enumerate all properties for a given schema class, and
    finally to provide fallback values for unauthored built-in properties.
    
    """
    @staticmethod
    def BuildComposedPrimDefinition(*args, **kwargs):
        """
        
        BuildComposedPrimDefinition(primType, appliedAPISchemas) -> PrimDefinition
        
        
        Composes and returns a new UsdPrimDefinition from the given
        ``primType`` and list of ``appliedSchemas`` .
        
        
        This prim definition will contain a union of properties from the
        registered prim definitions of each of the provided types.
        
        
        Parameters
        ----------
        primType : str
        
        appliedAPISchemas : list[str]
        
        
        """
    @staticmethod
    def FindAppliedAPIPrimDefinition(*args, **kwargs):
        """
        
        FindAppliedAPIPrimDefinition(typeName) -> PrimDefinition
        
        
        Finds the prim definition for the given ``typeName`` token if
        ``typeName`` is a registered applied API schema type.
        
        
        Returns null if it is not.
        
        
        Parameters
        ----------
        typeName : str
        
        
        """
    @staticmethod
    def FindConcretePrimDefinition(*args, **kwargs):
        """
        
        FindConcretePrimDefinition(typeName) -> PrimDefinition
        
        
        Finds the prim definition for the given ``typeName`` token if
        ``typeName`` is a registered concrete typed schema type.
        
        
        Returns null if it is not.
        
        
        Parameters
        ----------
        typeName : str
        
        
        """
    @staticmethod
    def GetAPISchemaCanOnlyApplyToTypeNames(*args, **kwargs):
        """
        
        **classmethod** GetAPISchemaCanOnlyApplyToTypeNames(apiSchemaName, instanceName) -> list[str]
        
        
        Returns a list of prim type names that the given ``apiSchemaName`` can
        only be applied to.
        
        
        A non-empty list indicates that the API schema can only be applied to
        prim that are or derive from prim type names in the list. If the list
        is empty, the API schema can be applied to prims of any type.
        
        If a non-empty ``instanceName`` is provided, this will first look for
        a list of"can only apply to"names specific to that instance of the API
        schema and return that if found. If a list is not found for the
        specific instance, it will fall back to looking for a"can only apply
        to"list for just the schema name itself.
        
        
        Parameters
        ----------
        apiSchemaName : str
        
        instanceName : str
        
        
        """
    @staticmethod
    def GetAPISchemaTypeName(*args, **kwargs):
        """
        
        **classmethod** GetAPISchemaTypeName(schemaType) -> str
        
        
        Return the type name in the USD schema for API schema types only from
        the given registered ``schemaType`` .
        
        
        Parameters
        ----------
        schemaType : Type
        
        
        """
    @staticmethod
    def GetAPITypeFromSchemaTypeName(*args, **kwargs):
        """
        
        **classmethod** GetAPITypeFromSchemaTypeName(typeName) -> Type
        
        
        Return the TfType of the schema corresponding to the given API schema
        type name ``typeName`` .
        
        
        This the inverse of GetAPISchemaTypeNAme.
        
        
        Parameters
        ----------
        typeName : str
        
        
        """
    @staticmethod
    def GetAutoApplyAPISchemas(*args, **kwargs):
        """
        
        **classmethod** GetAutoApplyAPISchemas() -> map[str, list[str]]
        
        
        Returns a map of the names of all registered auto apply API schemas to
        the list of type names each is registered to be auto applied to.
        
        
        The list of type names to apply to will directly match what is
        specified in the plugin metadata for each schema type. While auto
        apply schemas do account for the existence and validity of the type
        names and expand to include derived types of the listed types, the
        type lists returned by this function do not.
        
        
        
        """
    @staticmethod
    def GetConcreteSchemaTypeName(*args, **kwargs):
        """
        
        **classmethod** GetConcreteSchemaTypeName(schemaType) -> str
        
        
        Return the type name in the USD schema for concrete prim types only
        from the given registered ``schemaType`` .
        
        
        Parameters
        ----------
        schemaType : Type
        
        
        """
    @staticmethod
    def GetConcreteTypeFromSchemaTypeName(*args, **kwargs):
        """
        
        **classmethod** GetConcreteTypeFromSchemaTypeName(typeName) -> Type
        
        
        Return the TfType of the schema corresponding to the given concrete
        prim type name ``typeName`` .
        
        
        This the inverse of GetConcreteSchemaTypeName.
        
        
        Parameters
        ----------
        typeName : str
        
        
        """
    @staticmethod
    def GetEmptyPrimDefinition(*args, **kwargs):
        """
        
        GetEmptyPrimDefinition() -> PrimDefinition
        
        
        Returns the empty prim definition.
        
        
        
        """
    @staticmethod
    def GetFallbackPrimTypes(*args, **kwargs):
        """
        
        GetFallbackPrimTypes() -> VtDictionary
        
        
        Returns a dictionary mapping concrete schema prim type names to a
        VtTokenArray of fallback prim type names if fallback types are defined
        for the schema type in its registered schema.
        
        
        The standard use case for this to provide schema defined metadata that
        can be saved with a stage to inform an older version of USD - that may
        not have some schema types - as to which types it can used instead
        when encountering a prim of one these types.
        
        UsdStage::WriteFallbackPrimTypes
        
        Fallback Prim Types
        
        
        
        """
    @staticmethod
    def GetMultipleApplyNameTemplateBaseName(*args, **kwargs):
        """
        
        **classmethod** GetMultipleApplyNameTemplateBaseName(nameTemplate) -> str
        
        
        Returns the base name for the multiple apply schema name template
        ``nameTemplate`` .
        
        
        The base name is the substring of the given name template that comes
        after the instance name placeholder and the subsequent namespace
        delimiter. If the given property name does not contain the instance
        name placeholder, it is not a name template and the name template is
        returned as is.
        
        
        Parameters
        ----------
        nameTemplate : str
        
        
        """
    @staticmethod
    def GetSchemaKind(*args, **kwargs):
        """
        
        **classmethod** GetSchemaKind(schemaType) -> SchemaKind
        
        
        Returns the kind of the schema the given ``schemaType`` represents.
        
        
        This returns UsdSchemaKind::Invalid if ``schemaType`` is not a valid
        schema type or if the kind cannot be determined from type's plugin
        information.
        
        
        Parameters
        ----------
        schemaType : Type
        
        
        
        ----------------------------------------------------------------------
        
        GetSchemaKind(typeName) -> SchemaKind
        
        
        Returns the kind of the schema the given ``typeName`` represents.
        
        
        This returns UsdSchemaKind::Invalid if ``typeName`` is not a valid
        schema type name or if the kind cannot be determined from type's
        plugin information.
        
        
        Parameters
        ----------
        typeName : str
        
        
        """
    @staticmethod
    def GetSchemaTypeName(*args, **kwargs):
        """
        
        **classmethod** GetSchemaTypeName(schemaType) -> str
        
        
        Return the type name in the USD schema for prims or API schemas of the
        given registered ``schemaType`` .
        
        
        Parameters
        ----------
        schemaType : Type
        
        
        
        ----------------------------------------------------------------------
        
        GetSchemaTypeName() -> str
        
        
        Return the type name in the USD schema for prims or API schemas of the
        given registered ``SchemaType`` .
        
        
        
        """
    @staticmethod
    def GetTypeFromName(*args, **kwargs):
        """
        
        **classmethod** GetTypeFromName(typeName) -> Type
        
        
        Finds the TfType of a schema with ``typeName`` .
        
        
        This is primarily for when you have been provided Schema typeName
        (perhaps from a User Interface or Script) and need to identify if a
        prim's type inherits/is that typeName. If the type name IS known, then
        using the schema class is preferred.
        
        .. code-block:: text
        
          # This code attempts to match all prims on a stage to a given
          # user specified type, making the traditional schema based idioms not
          # applicable.
          data = parser.parse_args()
          tfType = UsdSchemaRegistry.GetTypeFromName(data.type)
          matchedPrims = [p for p in stage.Traverse() if p.IsA(tfType)] 
        
        It's worth noting that GetTypeFromName("Sphere") ==
        GetTypeFromName("UsdGeomSphere"), as this function resolves both the
        Schema's C++ class name and any registered aliases from a modules
        plugInfo.json file. However, GetTypeFromName("Boundable") !=
        GetTypeFromName("UsdGeomBoundable") because type aliases don't get
        registered for abstract schema types.
        
        
        Parameters
        ----------
        typeName : str
        
        
        """
    @staticmethod
    def GetTypeFromSchemaTypeName(*args, **kwargs):
        """
        
        **classmethod** GetTypeFromSchemaTypeName(typeName) -> Type
        
        
        Return the TfType of the schema corresponding to the given prim or API
        schema name ``typeName`` .
        
        
        This the inverse of GetSchemaTypeName.
        
        
        Parameters
        ----------
        typeName : str
        
        
        """
    @staticmethod
    def GetTypeNameAndInstance(*args, **kwargs):
        """
        
        **classmethod** GetTypeNameAndInstance(apiSchemaName) -> tuple[str, str]
        
        
        Returns the schema type name and the instance name parsed from the
        given ``apiSchemaName`` .
        
        
        ``apiSchemaName`` is the name of an applied schema as it appears in
        the list of applied schemas on a prim. For single-apply API schemas
        the name will just be the schema type name. For multiple-apply schemas
        the name should include the schema type name and the applied instance
        name separated by a namespace delimiter, for
        example'CollectionAPI:plasticStuff'.
        
        This function returns the separated schema type name and instance name
        component tokens if possible, otherwise it returns the
        ``apiSchemaName`` as the type name and an empty instance name.
        
        Note that no validation is done on the returned tokens. Clients are
        advised to use GetTypeFromSchemaTypeName() to validate the typeName
        token.
        
        UsdPrim::AddAppliedSchema(const TfToken&) const
        
        UsdPrim::GetAppliedSchemas() const
        
        
        Parameters
        ----------
        apiSchemaName : str
        
        
        """
    @staticmethod
    def IsAbstract(*args, **kwargs):
        """
        
        **classmethod** IsAbstract(primType) -> bool
        
        
        Returns true if the prim type ``primType`` is an abstract schema type
        and, unlike a concrete type, is not instantiable in scene description.
        
        
        Parameters
        ----------
        primType : Type
        
        
        
        ----------------------------------------------------------------------
        
        IsAbstract(primType) -> bool
        
        
        Returns true if the prim type ``primType`` is an abstract schema type
        and, unlike a concrete type, is not instantiable in scene description.
        
        
        Parameters
        ----------
        primType : str
        
        
        """
    @staticmethod
    def IsAllowedAPISchemaInstanceName(*args, **kwargs):
        """
        
        **classmethod** IsAllowedAPISchemaInstanceName(apiSchemaName, instanceName) -> bool
        
        
        Returns true if the given ``instanceName`` is an allowed instance name
        for the multiple apply API schema named ``apiSchemaName`` .
        
        
        Any instance name that matches the name of a property provided by the
        API schema is disallowed and will return false. If the schema type has
        plugin metadata that specifies allowed instance names, then only those
        specified names are allowed for the schema type. If the instance name
        is empty or the API is not a multiple apply schema, this will return
        false.
        
        
        Parameters
        ----------
        apiSchemaName : str
        
        instanceName : str
        
        
        """
    @staticmethod
    def IsAppliedAPISchema(*args, **kwargs):
        """
        
        **classmethod** IsAppliedAPISchema(apiSchemaType) -> bool
        
        
        Returns true if ``apiSchemaType`` is an applied API schema type.
        
        
        Parameters
        ----------
        apiSchemaType : Type
        
        
        
        ----------------------------------------------------------------------
        
        IsAppliedAPISchema(apiSchemaType) -> bool
        
        
        Returns true if ``apiSchemaType`` is an applied API schema type.
        
        
        Parameters
        ----------
        apiSchemaType : str
        
        
        """
    @staticmethod
    def IsConcrete(*args, **kwargs):
        """
        
        **classmethod** IsConcrete(primType) -> bool
        
        
        Returns true if the prim type ``primType`` is instantiable in scene
        description.
        
        
        Parameters
        ----------
        primType : Type
        
        
        
        ----------------------------------------------------------------------
        
        IsConcrete(primType) -> bool
        
        
        Returns true if the prim type ``primType`` is instantiable in scene
        description.
        
        
        Parameters
        ----------
        primType : str
        
        
        """
    @staticmethod
    def IsDisallowedField(*args, **kwargs):
        """
        
        **classmethod** IsDisallowedField(fieldName) -> bool
        
        
        Returns true if the field ``fieldName`` cannot have fallback values
        specified in schemas.
        
        
        Fields are generally disallowed because their fallback values aren't
        used. For instance, fallback values for composition arcs aren't used
        during composition, so allowing them to be set in schemas would be
        misleading.
        
        
        Parameters
        ----------
        fieldName : str
        
        
        """
    @staticmethod
    def IsMultipleApplyAPISchema(*args, **kwargs):
        """
        
        **classmethod** IsMultipleApplyAPISchema(apiSchemaType) -> bool
        
        
        Returns true if ``apiSchemaType`` is a multiple-apply API schema type.
        
        
        Parameters
        ----------
        apiSchemaType : Type
        
        
        
        ----------------------------------------------------------------------
        
        IsMultipleApplyAPISchema(apiSchemaType) -> bool
        
        
        Returns true if ``apiSchemaType`` is a multiple-apply API schema type.
        
        
        Parameters
        ----------
        apiSchemaType : str
        
        
        """
    @staticmethod
    def IsMultipleApplyNameTemplate(*args, **kwargs):
        """
        
        **classmethod** IsMultipleApplyNameTemplate(nameTemplate) -> bool
        
        
        Returns true if ``nameTemplate`` is a multiple apply schema name
        template.
        
        
        The given ``nameTemplate`` is a name template if and only if it
        contains the instance name place holder"__INSTANCE_NAME__"as an exact
        match as one of the tokenized components of the name tokenized by the
        namespace delimiter.
        
        
        Parameters
        ----------
        nameTemplate : str
        
        
        """
    @staticmethod
    def IsTyped(*args, **kwargs):
        """
        
        **classmethod** IsTyped(primType) -> bool
        
        
        Returns true if the prim type ``primType`` inherits from UsdTyped.
        
        
        Parameters
        ----------
        primType : Type
        
        
        """
    @staticmethod
    def MakeMultipleApplyNameInstance(*args, **kwargs):
        """
        
        **classmethod** MakeMultipleApplyNameInstance(nameTemplate, instanceName) -> str
        
        
        Returns an instance of a multiple apply schema name from the given
        ``nameTemplate`` for the given ``instanceName`` .
        
        
        The returned name is created by replacing the instance name
        placeholder"__INSTANCE_NAME__"in the name template with the given
        instance name. If the instance name placeholder is not found in
        ``nameTemplate`` , then the name template is not multiple apply name
        template and is returned as is.
        
        Note that the instance name placeholder must be found as an exact full
        word match with one of the tokenized components of the name template,
        when tokenized by the namespace delimiter, in order for it to be
        treated as a placeholder and substituted with the instance name.
        
        
        Parameters
        ----------
        nameTemplate : str
        
        instanceName : str
        
        
        """
    @staticmethod
    def MakeMultipleApplyNameTemplate(*args, **kwargs):
        """
        
        **classmethod** MakeMultipleApplyNameTemplate(namespacePrefix, baseName) -> str
        
        
        Creates a name template that can represent a property or API schema
        that belongs to a multiple apply schema and will therefore have
        multiple instances with different names.
        
        
        The name template is created by joining the ``namespacePrefix`` , the
        instance name placeholder"__INSTANCE_NAME__", and the ``baseName``
        using the namespace delimiter. Therefore the returned name template
        will be of one of the following forms depending on whether either of
        the inputs is empty:
        
           - namespacePrefix: **INSTANCE_NAME** :baseName
        
           - namespacePrefix: **INSTANCE_NAME**
        
           - **INSTANCE_NAME** :baseName
        
           - **INSTANCE_NAME**
        
        Name templates can be passed to MakeMultipleApplyNameInstance along
        with an instance name to create the name for a particular instance.
        
        
        Parameters
        ----------
        namespacePrefix : str
        
        baseName : str
        
        
        """
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
        
        __init__()
        
        
        
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
    """
    
    A proxy class for applying listOp edits to the specializes list for a
    prim.
    
    All paths passed to the UsdSpecializes API are expected to be in the
    namespace of the owning prim's stage. Subroot prim specializes paths
    will be translated from this namespace to the namespace of the current
    edit target, if necessary. If a path cannot be translated, a coding
    error will be issued and no changes will be made. Root prim
    specializes paths will not be translated.
    
    """
    @staticmethod
    def AddSpecialize(*args, **kwargs):
        """
        
        AddSpecialize(primPath, position) -> bool
        
        
        Adds a path to the specializes listOp at the current EditTarget, in
        the position specified by ``position`` .
        
        
        Parameters
        ----------
        primPath : Path
        
        position : ListPosition
        
        
        """
    @staticmethod
    def ClearSpecializes(*args, **kwargs):
        """
        
        ClearSpecializes() -> bool
        
        
        Removes the authored specializes listOp edits at the current edit
        target.
        
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        Return the prim this object is bound to.
        
        
        
        
        ----------------------------------------------------------------------
        
        GetPrim() -> Prim
        
        
        
        """
    @staticmethod
    def RemoveSpecialize(*args, **kwargs):
        """
        
        RemoveSpecialize(primPath) -> bool
        
        
        Removes the specified path from the specializes listOp at the current
        EditTarget.
        
        
        Parameters
        ----------
        primPath : Path
        
        
        """
    @staticmethod
    def SetSpecializes(*args, **kwargs):
        """
        
        SetSpecializes(items) -> bool
        
        
        Explicitly set specializes paths, potentially blocking weaker opinions
        that add or remove items, returning true on success, false if the edit
        could not be performed.
        
        
        Parameters
        ----------
        items : list[Path]
        
        
        """
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
    """
    
    The outermost container for scene description, which owns and presents
    composed prims as a scenegraph, following the composition recipe
    recursively described in its associated"root layer".
    
    USD derives its persistent-storage scalability by combining and
    reusing simple compositions into richer aggregates using referencing
    and layering with sparse overrides. Ultimately, every composition
    (i.e."scene") is identifiable by its root layer, i.e. the ``.usd``
    file, and a scene is instantiated in an application on a UsdStage that
    presents a composed view of the scene's root layer. Each simple
    composition referenced into a larger composition could be presented on
    its own UsdStage, at the same (or not) time that it is participating
    in the larger composition on its own UsdStage; all of the underlying
    layers will be shared by the two stages, while each maintains its own
    scenegraph of composed prims.
    
    A UsdStage has sole ownership over the UsdPrim 's with which it is
    populated, and retains *shared* ownership (with other stages and
    direct clients of SdfLayer 's, via the Sdf_LayerRegistry that
    underlies all SdfLayer creation methods) of layers. It provides
    roughly five categories of API that address different aspects of scene
    management:
    
       - Stage lifetime management methods for constructing and initially
         populating a UsdStage from an existing layer file, or one that will be
         created as a result, in memory or on the filesystem.
    
       - Load/unload working set management methods that allow you to
         specify which payloads should be included and excluded from the
         stage's composition.
    
       - Variant management methods to manage policy for which variant to
         use when composing prims that provide a named variant set, but do not
         specify a selection.
    
       - Prim access, creation, and mutation methods that allow you to
         find, create, or remove a prim identified by a path on the stage. This
         group also provides methods for efficiently traversing the prims on
         the stage.
    
       - Layers and EditTargets methods provide access to the layers in
         the stage's *root LayerStack* (i.e. the root layer and all of its
         recursive sublayers), and the ability to set a UsdEditTarget into
         which all subsequent mutations to objects associated with the stage
         (e.g. prims, properties, etc) will go.
    
       - Serialization methods for"flattening"a composition (to varying
         degrees), and exporting a completely flattened view of the stage to a
         string or file. These methods can be very useful for targeted asset
         optimization and debugging, though care should be exercized with large
         scenes, as flattening defeats some of the benefits of referenced scene
         description, and may produce very large results, especially in file
         formats that do not support data de-duplication, like the usda ASCII
         format!
    
    Stage Session Layers
    ====================
    
    Each UsdStage can possess an optional"session layer". The purpose of a
    session layer is to hold ephemeral edits that modify a UsdStage 's
    contents or behavior in a way that is useful to the client, but should
    not be considered as permanent mutations to be recorded upon export. A
    very common use of session layers is to make variant selections, to
    pick a specific LOD or shading variation, for example. The session
    layer is also frequently used to perform interactive vising/invsning
    of geometry and assets in the scene. A session layer, if present,
    contributes to a UsdStage 's identity, for purposes of stage-caching,
    etc.
    
    """
    class InitialLoadSet(pxr.Tf.Tf_PyEnumWrapper):
        """
        
        Specifies the initial set of prims to load when opening a UsdStage.
        
        """
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
        """
        
        ClearDefaultPrim() -> None
        
        
        Clear the default prim layer metadata in this stage's root layer.
        
        
        This is shorthand for:
        
        .. code-block:: text
        
          stage->GetRootLayer()->ClearDefaultPrim();
        
         Note that this function always authors to the stage's root layer. To
        author to a different layer, use the SdfLayer::SetDefaultPrim() API.
        
        
        
        """
    @staticmethod
    def ClearMetadata(*args, **kwargs):
        """
        
        ClearMetadata(key) -> bool
        
        
        Clear the value of stage metadatum ``key`` , if the stage's current
        UsdEditTarget is the root or session layer.
        
        
        If the current EditTarget is any other layer, raise a coding error.
        
        true if authoring was successful, false otherwise. Generates a coding
        error if ``key`` is not allowed as layer metadata.
        
        General Metadata in USD
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def ClearMetadataByDictKey(*args, **kwargs):
        """
        
        ClearMetadataByDictKey(key, keyPath) -> bool
        
        
        Clear any authored value identified by ``key`` and ``keyPath`` at the
        current EditTarget.
        
        
        The ``keyPath`` is a':'-separated path identifying a path in
        subdictionaries stored in the metadata field at ``key`` . If
        ``keyPath`` is empty, no action is taken.
        
        true if the value is cleared successfully, false otherwise. Generates
        a coding error if ``key`` is not allowed as layer metadata.
        
        Dictionary-valued Metadata
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        
        """
    @staticmethod
    def CreateClassPrim(*args, **kwargs):
        """
        
        CreateClassPrim(rootPrimPath) -> Prim
        
        
        Author an *SdfPrimSpec* with *specifier* == *SdfSpecifierClass* for
        the class at root prim path ``path`` at the current EditTarget.
        
        
        The current EditTarget must have UsdEditTarget::IsLocalLayer() ==
        true.
        
        The given *path* must be an absolute, root prim path that does not
        contain any variant selections.
        
        If a defined ( UsdPrim::IsDefined() ) non-class prim already exists at
        ``path`` , issue an error and return an invalid UsdPrim.
        
        If it is impossible to author the necessary PrimSpec, issue an error
        and return an invalid *UsdPrim*.
        
        
        Parameters
        ----------
        rootPrimPath : Path
        
        
        """
    @staticmethod
    def CreateInMemory(*args, **kwargs):
        """
        
        **classmethod** CreateInMemory(load) -> Stage
        
        
        Creates a new stage only in memory, analogous to creating an anonymous
        SdfLayer.
        
        
        If ``pathResolverContext`` is provided it will be bound when creating
        the root layer at ``identifier`` and whenever asset path resolution is
        done for this stage, regardless of what other context may be bound at
        that time. Otherwise Usd will create the root layer with no context
        bound, then create a context for all future asset path resolution for
        the stage by calling ArResolver::CreateDefaultContext.
        
        The initial set of prims to load on the stage can be specified using
        the ``load`` parameter.
        
        UsdStage::InitialLoadSet. Invoking an overload that does not take a
        ``sessionLayer`` argument will create a stage with an anonymous in-
        memory session layer. To create a stage without a session layer, pass
        TfNullPtr (or None in python) as the ``sessionLayer`` argument.
        
        
        Parameters
        ----------
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        CreateInMemory(identifier, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        identifier : str
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        CreateInMemory(identifier, pathResolverContext, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        identifier : str
        
        pathResolverContext : ResolverContext
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        CreateInMemory(identifier, sessionLayer, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        identifier : str
        
        sessionLayer : Layer
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        CreateInMemory(identifier, sessionLayer, pathResolverContext, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        identifier : str
        
        sessionLayer : Layer
        
        pathResolverContext : ResolverContext
        
        load : InitialLoadSet
        
        
        """
    @staticmethod
    def CreateNew(*args, **kwargs):
        """
        
        **classmethod** CreateNew(identifier, load) -> Stage
        
        
        Create a new stage with root layer ``identifier`` , destroying
        potentially existing files with that identifier; it is considered an
        error if an existing, open layer is present with this identifier.
        
        
        
        SdfLayer::CreateNew() Invoking an overload that does not take a
        ``sessionLayer`` argument will create a stage with an anonymous in-
        memory session layer. To create a stage without a session layer, pass
        TfNullPtr (or None in python) as the ``sessionLayer`` argument. The
        initial set of prims to load on the stage can be specified using the
        ``load`` parameter.
        
        UsdStage::InitialLoadSet. If ``pathResolverContext`` is provided it
        will be bound when creating the root layer at ``identifier`` and
        whenever asset path resolution is done for this stage, regardless of
        what other context may be bound at that time. Otherwise Usd will
        create the root layer with no context bound, then create a context for
        all future asset path resolution for the stage by calling
        ArResolver::CreateDefaultContextForAsset with the root layer's
        repository path if the layer has one, otherwise its resolved path.
        
        
        Parameters
        ----------
        identifier : str
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        CreateNew(identifier, sessionLayer, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        identifier : str
        
        sessionLayer : Layer
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        CreateNew(identifier, sessionLayer, pathResolverContext, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        identifier : str
        
        sessionLayer : Layer
        
        pathResolverContext : ResolverContext
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        CreateNew(identifier, pathResolverContext, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        identifier : str
        
        pathResolverContext : ResolverContext
        
        load : InitialLoadSet
        
        
        """
    @staticmethod
    def DefinePrim(*args, **kwargs):
        """
        
        DefinePrim(path, typeName) -> Prim
        
        
        Attempt to ensure a *UsdPrim* at ``path`` is defined (according to
        UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim at ``path`` is already defined on this stage and
        ``typeName`` is empty or equal to the existing prim's typeName, return
        that prim. Otherwise author an *SdfPrimSpec* with *specifier* ==
        *SdfSpecifierDef* and ``typeName`` for the prim at ``path`` at the
        current EditTarget. Author *SdfPrimSpec* s with ``specifier`` ==
        *SdfSpecifierDef* and empty typeName at the current EditTarget for any
        nonexistent, or existing but not *Defined* ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace or one of the ancestors of ``path`` is inactive on the
        UsdStage), issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not match the supplied ``typeName`` , in case a stronger typeName
        opinion overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        path : Path
        
        typeName : str
        
        
        """
    @staticmethod
    def ExpandPopulationMask(*args, **kwargs):
        """
        
        ExpandPopulationMask(relPred, attrPred) -> None
        
        
        Expand this stage's population mask to include the targets of all
        relationships that pass ``relPred`` and connections to all attributes
        that pass ``attrPred`` recursively.
        
        
        If ``relPred`` is null, include all relationship targets; if
        ``attrPred`` is null, include all connections.
        
        This function can be used, for example, to expand a population mask
        for a given prim to include bound materials, if those bound materials
        are expressed as relationships or attribute connections.
        
        See also UsdPrim::FindAllRelationshipTargetPaths() and
        UsdPrim::FindAllAttributeConnectionPaths() .
        
        
        Parameters
        ----------
        relPred : function[bool( Relationship )]
        
        attrPred : function[bool( Attribute )]
        
        
        """
    @staticmethod
    def Export(*args, **kwargs):
        """
        
        Export(filename, addSourceFileComment, args) -> bool
        
        
        Writes out the composite scene as a single flattened layer into
        *filename*.
        
        
        If addSourceFileComment is true, a comment in the output layer will
        mention the input layer it was generated from.
        
        See UsdStage::Flatten for details of the flattening transformation.
        
        
        Parameters
        ----------
        filename : str
        
        addSourceFileComment : bool
        
        args : Layer.FileFormatArguments
        
        
        """
    @staticmethod
    def ExportToString(*args, **kwargs):
        """
        
        ExportToString(result, addSourceFileComment) -> bool
        
        
        Writes the composite scene as a flattened Usd text representation into
        the given *string*.
        
        
        If addSourceFileComment is true, a comment in the output layer will
        mention the input layer it was generated from.
        
        See UsdStage::Flatten for details of the flattening transformation.
        
        
        Parameters
        ----------
        result : str
        
        addSourceFileComment : bool
        
        
        """
    @staticmethod
    def FindLoadable(*args, **kwargs):
        """
        
        FindLoadable(rootPath) -> SdfPathSet
        
        
        Returns an SdfPathSet of all paths that can be loaded.
        
        
        Note that this method does not return paths to inactive prims as they
        cannot be loaded.
        
        The set returned includes loaded and unloaded paths. To determine the
        set of unloaded paths, one can diff this set with the current load
        set, for example:
        
        .. code-block:: text
        
          SdfPathSet loaded = stage->GetLoadSet(),
                     all = stage->FindLoadable(),
                     result;
          std::set_difference(loaded.begin(), loaded.end(),
                              all.begin(), all.end(),
                              std::inserter(result, result.end()));
        
        See Working Set Management for more information.
        
        
        Parameters
        ----------
        rootPath : Path
        
        
        """
    @staticmethod
    def Flatten(*args, **kwargs):
        """
        
        Flatten(addSourceFileComment) -> Layer
        
        
        Returns a single, anonymous, merged layer for this composite scene.
        
        
        Specifically, this function removes **most** composition metadata and
        authors the resolved values for each object directly into the
        flattened layer.
        
        All VariantSets are removed and only the currently selected variants
        will be present in the resulting layer.
        
        Class prims will still exist, however all inherits arcs will have been
        removed and the inherited data will be copied onto each child object.
        Composition arcs authored on the class itself will be flattened into
        the class.
        
        Flatten preserves scenegraph instancing by creating independent roots
        for each prototype currently composed on this stage, and adding a
        single internal reference arc on each instance prim to its
        corresponding prototype.
        
        Time samples across sublayer offsets will will have the time offset
        and scale applied to each time index.
        
        Finally, any deactivated prims will be pruned from the result.
        
        
        Parameters
        ----------
        addSourceFileComment : bool
        
        
        """
    @staticmethod
    def GetAttributeAtPath(*args, **kwargs):
        """
        
        GetAttributeAtPath(path) -> Attribute
        
        
        Return the UsdAttribute at ``path`` , or an invalid UsdAttribute if
        none exists.
        
        
        This is equivalent to
        
        .. code-block:: text
        
          stage.GetObjectAtPath(path).As<UsdAttribute>();
        
        GetObjectAtPath(const SdfPath&) const
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetColorConfigFallbacks(*args, **kwargs):
        """
        
        **classmethod** GetColorConfigFallbacks(colorConfiguration, colorManagementSystem) -> None
        
        
        Returns the global fallback values
        of'colorConfiguration'and'colorManagementSystem'.
        
        
        These are set in the plugInfo.json file of a plugin, but can be
        overridden by calling the static method SetColorConfigFallbacks() .
        
        The python wrapping of this method returns a tuple containing
        (colorConfiguration, colorManagementSystem).
        
        SetColorConfigFallbacks, Color Configuration API
        
        
        Parameters
        ----------
        colorConfiguration : AssetPath
        
        colorManagementSystem : str
        
        
        """
    @staticmethod
    def GetColorConfiguration(*args, **kwargs):
        """
        
        GetColorConfiguration() -> AssetPath
        
        
        Returns the default color configuration used to interpret the per-
        attribute color-spaces in the composed USD stage.
        
        
        Color Configuration API
        
        
        
        """
    @staticmethod
    def GetColorManagementSystem(*args, **kwargs):
        """
        
        GetColorManagementSystem() -> str
        
        
        Sets the name of the color management system to be used for loading
        and interpreting the color configuration file.
        
        
        Color Configuration API
        
        
        
        """
    @staticmethod
    def GetDefaultPrim(*args, **kwargs):
        """
        
        GetDefaultPrim() -> Prim
        
        
        Return the root UsdPrim on this stage whose name is the root layer's
        defaultPrim metadata's value.
        
        
        Return an invalid prim if there is no such prim or if the root layer's
        defaultPrim metadata is unset or is not a valid prim name. Note that
        this function only examines this stage's rootLayer. It does not
        consider sublayers of the rootLayer. See also
        SdfLayer::GetDefaultPrim() .
        
        
        
        """
    @staticmethod
    def GetEditTarget(*args, **kwargs):
        """
        
        GetEditTarget() -> EditTarget
        
        
        Return the stage's EditTarget.
        
        
        
        """
    @staticmethod
    def GetEditTargetForLocalLayer(*args, **kwargs):
        """
        
        GetEditTargetForLocalLayer(i) -> EditTarget
        
        
        Return a UsdEditTarget for editing the layer at index *i* in the layer
        stack.
        
        
        This edit target will incorporate any layer time offset that applies
        to the sublayer.
        
        
        Parameters
        ----------
        i : int
        
        
        
        ----------------------------------------------------------------------
        
        GetEditTargetForLocalLayer(layer) -> EditTarget
        
        
        Return a UsdEditTarget for editing the given local *layer*.
        
        
        If the given layer appears more than once in the layer stack, the time
        offset to the first occurrence will be used.
        
        
        Parameters
        ----------
        layer : Layer
        
        
        """
    @staticmethod
    def GetEndTimeCode(*args, **kwargs):
        """
        
        GetEndTimeCode() -> float
        
        
        Returns the stage's end timeCode.
        
        
        If the stage has an associated session layer with an end timeCode
        opinion, this value is returned. Otherwise, the end timeCode opinion
        from the root layer is returned.
        
        
        
        """
    @staticmethod
    def GetFramesPerSecond(*args, **kwargs):
        """
        
        GetFramesPerSecond() -> float
        
        
        Returns the stage's framesPerSecond value.
        
        
        This makes an advisory statement about how the contained data can be
        most usefully consumed and presented. It's primarily an indication of
        the expected playback rate for the data, but a timeline editing tool
        might also want to use this to decide how to scale and label its
        timeline.
        
        The default value of framesPerSecond is 24.
        
        
        
        """
    @staticmethod
    def GetGlobalVariantFallbacks(*args, **kwargs):
        """
        
        **classmethod** GetGlobalVariantFallbacks() -> PcpVariantFallbackMap
        
        
        Get the global variant fallback preferences used in new UsdStages.
        
        
        
        """
    @staticmethod
    def GetInterpolationType(*args, **kwargs):
        """
        
        GetInterpolationType() -> InterpolationType
        
        
        Returns the interpolation type used during value resolution for all
        attributes on this stage.
        
        
        
        """
    @staticmethod
    def GetLayerStack(*args, **kwargs):
        """
        
        GetLayerStack(includeSessionLayers) -> list[Layer]
        
        
        Return this stage's local layers in strong-to-weak order.
        
        
        If *includeSessionLayers* is true, return the linearized strong-to-
        weak sublayers rooted at the stage's session layer followed by the
        linearized strong-to-weak sublayers rooted at this stage's root layer.
        If *includeSessionLayers* is false, omit the sublayers rooted at this
        stage's session layer.
        
        
        Parameters
        ----------
        includeSessionLayers : bool
        
        
        """
    @staticmethod
    def GetLoadRules(*args, **kwargs):
        """
        
        GetLoadRules() -> StageLoadRules
        
        
        Return the stage's current UsdStageLoadRules governing payload
        inclusion.
        
        
        See Working Set Management for more information.
        
        
        
        """
    @staticmethod
    def GetLoadSet(*args, **kwargs):
        """
        
        GetLoadSet() -> SdfPathSet
        
        
        Returns a set of all loaded paths.
        
        
        The paths returned are both those that have been explicitly loaded and
        those that were loaded as a result of dependencies, ancestors or
        descendants of explicitly loaded paths.
        
        This method does not return paths to inactive prims.
        
        See Working Set Management for more information.
        
        
        
        """
    @staticmethod
    def GetMetadata(*args, **kwargs):
        """
        
        GetMetadata(key, value) -> bool
        
        
        Return in ``value`` an authored or fallback value (if one was defined
        for the given metadatum) for Stage metadatum ``key`` .
        
        
        Order of resolution is session layer, followed by root layer, else
        fallback to the SdfSchema.
        
        true if we successfully retrieved a value of the requested type; false
        if ``key`` is not allowed as layer metadata or no value was found.
        Generates a coding error if we retrieved a stored value of a type
        other than the requested type
        
        General Metadata in USD
        
        
        Parameters
        ----------
        key : str
        
        value : T
        
        
        
        ----------------------------------------------------------------------
        
        GetMetadata(key, value) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        key : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def GetMetadataByDictKey(*args, **kwargs):
        """
        
        GetMetadataByDictKey(key, keyPath, value) -> bool
        
        
        Resolve the requested dictionary sub-element ``keyPath`` of
        dictionary-valued metadatum named ``key`` , returning the resolved
        value.
        
        
        If you know you need just a small number of elements from a
        dictionary, accessing them element-wise using this method can be much
        less expensive than fetching the entire dictionary with
        GetMetadata(key).
        
        true if we successfully retrieved a value of the requested type; false
        if ``key`` is not allowed as layer metadata or no value was found.
        Generates a coding error if we retrieved a stored value of a type
        other than the requested type The ``keyPath`` is a':'-separated path
        addressing an element in subdictionaries. If ``keyPath`` is empty,
        returns an empty VtValue.
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        value : T
        
        
        
        ----------------------------------------------------------------------
        
        GetMetadataByDictKey(key, keyPath, value) -> bool
        
        
        overload
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def GetMutedLayers(*args, **kwargs):
        """
        
        GetMutedLayers() -> list[str]
        
        
        Returns a vector of all layers that have been muted on this stage.
        
        
        
        """
    @staticmethod
    def GetObjectAtPath(*args, **kwargs):
        """
        
        GetObjectAtPath(path) -> Object
        
        
        Return the UsdObject at ``path`` , or an invalid UsdObject if none
        exists.
        
        
        If ``path`` indicates a prim beneath an instance, returns an instance
        proxy prim if a prim exists at the corresponding path in that
        instance's prototype. If ``path`` indicates a property beneath a child
        of an instance, returns a property whose parent prim is an instance
        proxy prim.
        
        Example:
        
        .. code-block:: text
        
          if (UsdObject obj = stage->GetObjectAtPath(path)) {
              if (UsdPrim prim = obj.As<UsdPrim>()) {
                  // Do things with prim
              }
              else if (UsdProperty prop = obj.As<UsdProperty>()) {
                  // Do things with property. We can also cast to
                  // UsdRelationship or UsdAttribute using this same pattern.
              }
          }
          else {
              // No object at specified path
          }
        
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetPathResolverContext(*args, **kwargs):
        """
        
        GetPathResolverContext() -> ResolverContext
        
        
        Return the path resolver context for all path resolution during
        composition of this stage.
        
        
        Useful for external clients that want to resolve paths with the same
        context as this stage, or create new stages with the same context.
        
        
        
        """
    @staticmethod
    def GetPopulationMask(*args, **kwargs):
        """
        
        GetPopulationMask() -> StagePopulationMask
        
        
        Return this stage's population mask.
        
        
        
        """
    @staticmethod
    def GetPrimAtPath(*args, **kwargs):
        """
        
        GetPrimAtPath(path) -> Prim
        
        
        Return the UsdPrim at ``path`` , or an invalid UsdPrim if none exists.
        
        
        If ``path`` indicates a prim beneath an instance, returns an instance
        proxy prim if a prim exists at the corresponding path in that
        instance's prototype.
        
        Unlike OverridePrim() and DefinePrim() , this method will never author
        scene description, and therefore is safe to use as a"reader"in the Usd
        multi-threading model.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetPropertyAtPath(*args, **kwargs):
        """
        
        GetPropertyAtPath(path) -> Property
        
        
        Return the UsdProperty at ``path`` , or an invalid UsdProperty if none
        exists.
        
        
        This is equivalent to
        
        .. code-block:: text
        
          stage.GetObjectAtPath(path).As<UsdProperty>();
        
        GetObjectAtPath(const SdfPath&) const
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetPrototypes(*args, **kwargs):
        """
        
        GetPrototypes() -> list[Prim]
        
        
        Returns all native instancing prototype prims.
        
        
        
        """
    @staticmethod
    def GetPseudoRoot(*args, **kwargs):
        """
        
        GetPseudoRoot() -> Prim
        
        
        Return the stage's"pseudo-root"prim, whose name is defined by Usd.
        
        
        The stage's named root prims are namespace children of this prim,
        which exists to make the namespace hierarchy a tree instead of a
        forest. This simplifies algorithms that want to traverse all prims.
        
        A UsdStage always has a pseudo-root prim, unless there was an error
        opening or creating the stage, in which case this method returns an
        invalid UsdPrim.
        
        
        
        """
    @staticmethod
    def GetRelationshipAtPath(*args, **kwargs):
        """
        
        GetRelationshipAtPath(path) -> Relationship
        
        
        Return the UsdAttribute at ``path`` , or an invalid UsdAttribute if
        none exists.
        
        
        This is equivalent to
        
        .. code-block:: text
        
          stage.GetObjectAtPath(path).As<UsdRelationship>();
        
        GetObjectAtPath(const SdfPath&) const
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetRootLayer(*args, **kwargs):
        """
        
        GetRootLayer() -> Layer
        
        
        Return this stage's root layer.
        
        
        
        """
    @staticmethod
    def GetSessionLayer(*args, **kwargs):
        """
        
        GetSessionLayer() -> Layer
        
        
        Return this stage's root session layer.
        
        
        
        """
    @staticmethod
    def GetStartTimeCode(*args, **kwargs):
        """
        
        GetStartTimeCode() -> float
        
        
        Returns the stage's start timeCode.
        
        
        If the stage has an associated session layer with a start timeCode
        opinion, this value is returned. Otherwise, the start timeCode opinion
        from the root layer is returned.
        
        
        
        """
    @staticmethod
    def GetTimeCodesPerSecond(*args, **kwargs):
        """
        
        GetTimeCodesPerSecond() -> float
        
        
        Returns the stage's timeCodesPerSecond value.
        
        
        The timeCodesPerSecond value scales the time ordinate for the samples
        contained in the stage to seconds. If timeCodesPerSecond is 24, then a
        sample at time ordinate 24 should be viewed exactly one second after
        the sample at time ordinate 0.
        
        Like SdfLayer::GetTimeCodesPerSecond, this accessor uses a dynamic
        fallback to framesPerSecond. The order of precedence is:
        
           - timeCodesPerSecond from session layer
        
           - timeCodesPerSecond from root layer
        
           - framesPerSecond from session layer
        
           - framesPerSecond from root layer
        
           - fallback value of 24
        
        
        
        
        """
    @staticmethod
    def GetUsedLayers(*args, **kwargs):
        """
        
        GetUsedLayers(includeClipLayers) -> list[Layer]
        
        
        Return a vector of all of the layers *currently* consumed by this
        stage, as determined by the composition arcs that were traversed to
        compose and populate the stage.
        
        
        The list of consumed layers will change with the stage's load-set and
        variant selections, so the return value should be considered only a
        snapshot. The return value will include the stage's session layer, if
        it has one. If *includeClipLayers* is true, we will also include all
        of the layers that this stage has had to open so far to perform value
        resolution of attributes affected by Value Clips
        
        
        Parameters
        ----------
        includeClipLayers : bool
        
        
        """
    @staticmethod
    def HasAuthoredMetadata(*args, **kwargs):
        """
        
        HasAuthoredMetadata(key) -> bool
        
        
        Returns ``true`` if the *key* has an authored value, ``false`` if no
        value was authored or the only value available is the SdfSchema 's
        metadata fallback.
        
        
        
        If a value for a metadatum *not* legal to author on layers is present
        in the root or session layer (which could happen through hand-editing
        or use of certain low-level API's), this method will still return
        ``false`` .
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def HasAuthoredMetadataDictKey(*args, **kwargs):
        """
        
        HasAuthoredMetadataDictKey(key, keyPath) -> bool
        
        
        Return true if there exists any authored opinion (excluding fallbacks)
        for ``key`` and ``keyPath`` .
        
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at ``key`` . If
        ``keyPath`` is empty, returns ``false`` .
        
        Dictionary-valued Metadata
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        
        """
    @staticmethod
    def HasAuthoredTimeCodeRange(*args, **kwargs):
        """
        
        HasAuthoredTimeCodeRange() -> bool
        
        
        Returns true if the stage has both start and end timeCodes authored in
        the session layer or the root layer of the stage.
        
        
        
        """
    @staticmethod
    def HasDefaultPrim(*args, **kwargs):
        """
        
        HasDefaultPrim() -> bool
        
        
        Return true if this stage's root layer has an authored opinion for the
        default prim layer metadata.
        
        
        This is shorthand for:
        
        .. code-block:: text
        
          stage->GetRootLayer()->HasDefaultPrim();
        
         Note that this function only consults the stage's root layer. To
        consult a different layer, use the SdfLayer::HasDefaultPrim() API.
        
        
        
        """
    @staticmethod
    def HasLocalLayer(*args, **kwargs):
        """
        
        HasLocalLayer(layer) -> bool
        
        
        Return true if *layer* is one of the layers in this stage's local,
        root layerStack.
        
        
        Parameters
        ----------
        layer : Layer
        
        
        """
    @staticmethod
    def HasMetadata(*args, **kwargs):
        """
        
        HasMetadata(key) -> bool
        
        
        Returns true if the *key* has a meaningful value, that is, if
        GetMetadata() will provide a value, either because it was authored or
        because the Stage metadata was defined with a meaningful fallback
        value.
        
        
        Returns false if ``key`` is not allowed as layer metadata.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def HasMetadataDictKey(*args, **kwargs):
        """
        
        HasMetadataDictKey(key, keyPath) -> bool
        
        
        Return true if there exists any authored or fallback opinion for
        ``key`` and ``keyPath`` .
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at ``key`` . If
        ``keyPath`` is empty, returns ``false`` .
        
        Returns false if ``key`` is not allowed as layer metadata.
        
        Dictionary-valued Metadata
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        
        """
    @staticmethod
    def IsLayerMuted(*args, **kwargs):
        """
        
        IsLayerMuted(layerIdentifier) -> bool
        
        
        Returns true if the layer specified by ``layerIdentifier`` is muted in
        this cache, false otherwise.
        
        
        See documentation on MuteLayer for details on how ``layerIdentifier``
        is compared to the layers that have been muted.
        
        
        Parameters
        ----------
        layerIdentifier : str
        
        
        """
    @staticmethod
    def IsSupportedFile(*args, **kwargs):
        """
        
        **classmethod** IsSupportedFile(filePath) -> bool
        
        
        Indicates whether the specified file is supported by UsdStage.
        
        
        This function is a cheap way to determine whether a file might be
        open-able with UsdStage::Open. It is purely based on the given
        ``filePath`` and does not open the file or perform analysis on the
        contents. As such, UsdStage::Open may still fail even if this function
        returns true.
        
        
        Parameters
        ----------
        filePath : str
        
        
        """
    @staticmethod
    def Load(*args, **kwargs):
        """
        
        Load(path, policy) -> Prim
        
        
        Modify this stage's load rules to load the prim at ``path`` , its
        ancestors, and all of its descendants if ``policy`` is
        UsdLoadWithDescendants.
        
        
        If ``policy`` is UsdLoadWithoutDescendants, then payloads on
        descendant prims are not loaded.
        
        See Working Set Management for more information.
        
        
        Parameters
        ----------
        path : Path
        
        policy : LoadPolicy
        
        
        """
    @staticmethod
    def LoadAndUnload(*args, **kwargs):
        """
        
        LoadAndUnload(loadSet, unloadSet, policy) -> None
        
        
        Unload and load the given path sets.
        
        
        The effect is as if the unload set were processed first followed by
        the load set.
        
        This is equivalent to calling UsdStage::Unload for each item in the
        unloadSet followed by UsdStage::Load for each item in the loadSet,
        however this method is more efficient as all operations are committed
        in a single batch. The ``policy`` argument is described in the
        documentation for Load() .
        
        See Working Set Management for more information.
        
        
        Parameters
        ----------
        loadSet : SdfPathSet
        
        unloadSet : SdfPathSet
        
        policy : LoadPolicy
        
        
        """
    @staticmethod
    def MuteAndUnmuteLayers(*args, **kwargs):
        """
        
        MuteAndUnmuteLayers(muteLayers, unmuteLayers) -> None
        
        
        Mute and unmute the layers identified in ``muteLayers`` and
        ``unmuteLayers`` .
        
        
        
        This is equivalent to calling UsdStage::UnmuteLayer for each layer in
        ``unmuteLayers`` followed by UsdStage::MuteLayer for each layer in
        ``muteLayers`` , however this method is more efficient as all
        operations are committed in a single batch.
        
        
        Parameters
        ----------
        muteLayers : list[str]
        
        unmuteLayers : list[str]
        
        
        """
    @staticmethod
    def MuteLayer(*args, **kwargs):
        """
        
        MuteLayer(layerIdentifier) -> None
        
        
        Mute the layer identified by ``layerIdentifier`` .
        
        
        Muted layers are ignored by the stage; they do not participate in
        value resolution or composition and do not appear in any LayerStack.
        If the root layer of a reference or payload LayerStack is muted, the
        behavior is as if the muted layer did not exist, which means a
        composition error will be generated.
        
        A canonical identifier for each layer in ``layersToMute`` will be
        computed using ArResolver::CreateIdentifier using the stage's root
        layer as the anchoring asset. Any layer encountered during composition
        with the same identifier will be considered muted and ignored.
        
        Note that muting a layer will cause this stage to release all
        references to that layer. If no other client is holding on to
        references to that layer, it will be unloaded. In this case, if there
        are unsaved edits to the muted layer, those edits are lost.  Since
        anonymous layers are not serialized, muting an anonymous layer will
        cause that layer and its contents to be lost in this case.
        
        Muting a layer that has not been used by this stage is not an error.
        If that layer is encountered later, muting will take effect and that
        layer will be ignored.
        
        The root layer of this stage may not be muted; attempting to do so
        will generate a coding error.
        
        
        Parameters
        ----------
        layerIdentifier : str
        
        
        """
    @staticmethod
    def Open(*args, **kwargs):
        """
        
        **classmethod** Open(filePath, load) -> Stage
        
        
        Attempt to find a matching existing stage in a cache if
        UsdStageCacheContext objects exist on the stack.
        
        
        Failing that, create a new stage and recursively compose prims defined
        within and referenced by the layer at ``filePath`` , which must
        already exist.
        
        The initial set of prims to load on the stage can be specified using
        the ``load`` parameter.
        
        UsdStage::InitialLoadSet. If ``pathResolverContext`` is provided it
        will be bound when opening the root layer at ``filePath`` and whenever
        asset path resolution is done for this stage, regardless of what other
        context may be bound at that time. Otherwise Usd will open the root
        layer with no context bound, then create a context for all future
        asset path resolution for the stage by calling
        ArResolver::CreateDefaultContextForAsset with the layer's repository
        path if the layer has one, otherwise its resolved path.
        
        
        Parameters
        ----------
        filePath : str
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        Open(filePath, pathResolverContext, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        filePath : str
        
        pathResolverContext : ResolverContext
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        Open(rootLayer, load) -> Stage
        
        
        Open a stage rooted at ``rootLayer`` .
        
        
        Attempt to find a stage that matches the passed arguments in a
        UsdStageCache if UsdStageCacheContext objects exist on the calling
        stack. If a matching stage is found, return that stage. Otherwise,
        create a new stage rooted at ``rootLayer`` .
        
        Invoking an overload that does not take a ``sessionLayer`` argument
        will create a stage with an anonymous in-memory session layer. To
        create a stage without a session layer, pass TfNullPtr (or None in
        python) as the ``sessionLayer`` argument.
        
        The initial set of prims to load on the stage can be specified using
        the ``load`` parameter.
        
        UsdStage::InitialLoadSet. If ``pathResolverContext`` is provided it
        will be bound when whenever asset path resolution is done for this
        stage, regardless of what other context may be bound at that time.
        Otherwise Usd will create a context for all future asset path
        resolution for the stage by calling
        ArResolver::CreateDefaultContextForAsset with the layer's repository
        path if the layer has one, otherwise its resolved path.
        
        When searching for a matching stage in bound UsdStageCache s, only the
        provided arguments matter for cache lookup. For example, if only a
        root layer (or a root layer file path) is provided, the first stage
        found in any cache that has that root layer is returned. So, for
        example if you require that the stage have no session layer, you must
        explicitly specify TfNullPtr (or None in python) for the sessionLayer
        argument.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        Open(rootLayer, sessionLayer, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        sessionLayer : Layer
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        Open(rootLayer, pathResolverContext, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        pathResolverContext : ResolverContext
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        Open(rootLayer, sessionLayer, pathResolverContext, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        sessionLayer : Layer
        
        pathResolverContext : ResolverContext
        
        load : InitialLoadSet
        
        
        """
    @staticmethod
    def OpenMasked(*args, **kwargs):
        """
        
        **classmethod** OpenMasked(filePath, mask, load) -> Stage
        
        
        Create a new stage and recursively compose prims defined within and
        referenced by the layer at ``filePath`` which must already exist,
        subject to ``mask`` .
        
        
        These OpenMasked() methods do not automatically consult or populate
        UsdStageCache s.
        
        The initial set of prims to load on the stage can be specified using
        the ``load`` parameter.
        
        UsdStage::InitialLoadSet. If ``pathResolverContext`` is provided it
        will be bound when opening the root layer at ``filePath`` and whenever
        asset path resolution is done for this stage, regardless of what other
        context may be bound at that time. Otherwise Usd will open the root
        layer with no context bound, then create a context for all future
        asset path resolution for the stage by calling
        ArResolver::CreateDefaultContextForAsset with the layer's repository
        path if the layer has one, otherwise its resolved path.
        
        
        Parameters
        ----------
        filePath : str
        
        mask : StagePopulationMask
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        OpenMasked(filePath, pathResolverContext, mask, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        filePath : str
        
        pathResolverContext : ResolverContext
        
        mask : StagePopulationMask
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        OpenMasked(rootLayer, mask, load) -> Stage
        
        
        Open a stage rooted at ``rootLayer`` and with limited population
        subject to ``mask`` .
        
        
        These OpenMasked() methods do not automatically consult or populate
        UsdStageCache s.
        
        Invoking an overload that does not take a ``sessionLayer`` argument
        will create a stage with an anonymous in-memory session layer. To
        create a stage without a session layer, pass TfNullPtr (or None in
        python) as the ``sessionLayer`` argument.
        
        The initial set of prims to load on the stage can be specified using
        the ``load`` parameter.
        
        UsdStage::InitialLoadSet. If ``pathResolverContext`` is provided it
        will be bound when whenever asset path resolution is done for this
        stage, regardless of what other context may be bound at that time.
        Otherwise Usd will create a context for all future asset path
        resolution for the stage by calling
        ArResolver::CreateDefaultContextForAsset with the layer's repository
        path if the layer has one, otherwise its resolved path.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        mask : StagePopulationMask
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        OpenMasked(rootLayer, sessionLayer, mask, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        sessionLayer : Layer
        
        mask : StagePopulationMask
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        OpenMasked(rootLayer, pathResolverContext, mask, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        pathResolverContext : ResolverContext
        
        mask : StagePopulationMask
        
        load : InitialLoadSet
        
        
        
        ----------------------------------------------------------------------
        
        OpenMasked(rootLayer, sessionLayer, pathResolverContext, mask, load) -> Stage
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        sessionLayer : Layer
        
        pathResolverContext : ResolverContext
        
        mask : StagePopulationMask
        
        load : InitialLoadSet
        
        
        """
    @staticmethod
    def OverridePrim(*args, **kwargs):
        """
        
        OverridePrim(path) -> Prim
        
        
        Attempt to ensure a *UsdPrim* at ``path`` exists on this stage.
        
        
        If a prim already exists at ``path`` , return it. Otherwise author
        *SdfPrimSpecs* with *specifier* == *SdfSpecifierOver* and empty
        *typeName* at the current EditTarget to create this prim and any
        nonexistent ancestors, then return it.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        If an ancestor of ``path`` identifies an *inactive* prim, author scene
        description as described above but return an invalid prim, since the
        resulting prim is descendant to an inactive prim.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def Reload(*args, **kwargs):
        """
        
        Reload() -> None
        
        
        Calls SdfLayer::Reload on all layers contributing to this stage,
        except session layers and sublayers of session layers.
        
        
        This includes non-session sublayers, references and payloads. Note
        that reloading anonymous layers clears their content, so invoking
        Reload() on a stage constructed via CreateInMemory() will clear its
        root layer.
        
        This method is considered a mutation, which has potentially global
        effect! Unlike the various Load() methods whose actions affect only
        **this stage**, Reload() may cause layers to change their contents,
        and because layers are global resources shared by potentially many
        Stages, calling Reload() on one stage may result in a mutation to any
        number of stages. In general, unless you are highly confident your
        stage is the only consumer of its layers, you should only call
        Reload() when you are assured no other threads may be reading from any
        Stages.
        
        
        
        """
    @staticmethod
    def RemovePrim(*args, **kwargs):
        """
        
        RemovePrim(path) -> bool
        
        
        Remove all scene description for the given ``path`` and its subtree
        *in the current UsdEditTarget*.
        
        
        This method does not do what you might initially think! Calling this
        function will not necessarily cause the UsdPrim at ``path`` on this
        stage to disappear. Completely eradicating a prim from a composition
        can be an involved process, involving edits to many contributing
        layers, some of which (in many circumstances) will not be editable by
        a client. This method is a surgical instrument that *can* be used
        iteratively to effect complete removal of a prim and its subtree from
        namespace, assuming the proper permissions are acquired, but more
        commonly it is used to perform layer-level operations; e.g.: ensuring
        that a given layer (as expressed by a UsdEditTarget) provides no
        opinions for a prim and its subtree.
        
        Generally, if your eye is attracted to this method, you probably want
        to instead use UsdPrim::SetActive(false), which will provide the
        composed effect of removing the prim and its subtree from the
        composition, without actually removing any scene description, which as
        a bonus, means that the effect is reversible at a later time!
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def ResolveIdentifierToEditTarget(*args, **kwargs):
        """
        
        ResolveIdentifierToEditTarget(identifier) -> str
        
        
        Resolve the given identifier using this stage's ArResolverContext and
        the layer of its GetEditTarget() as an anchor for relative references
        (e.g.
        
        
        @./siblingFile.usd@).
        
        a non-empty string containing either the same identifier that was
        passed in (if the identifier refers to an already-opened layer or
        an"anonymous", in-memory layer), or a resolved layer filepath. If the
        identifier was not resolvable, return the empty string.
        
        
        Parameters
        ----------
        identifier : str
        
        
        """
    @staticmethod
    def Save(*args, **kwargs):
        """
        
        Save() -> None
        
        
        Calls SdfLayer::Save on all dirty layers contributing to this stage
        except session layers and sublayers of session layers.
        
        
        This function will emit a warning and skip each dirty anonymous layer
        it encounters, since anonymous layers cannot be saved with
        SdfLayer::Save. These layers must be manually exported by calling
        SdfLayer::Export.
        
        
        
        """
    @staticmethod
    def SaveSessionLayers(*args, **kwargs):
        """
        
        SaveSessionLayers() -> None
        
        
        Calls SdfLayer::Save on all dirty session layers and sublayers of
        session layers contributing to this stage.
        
        
        This function will emit a warning and skip each dirty anonymous layer
        it encounters, since anonymous layers cannot be saved with
        SdfLayer::Save. These layers must be manually exported by calling
        SdfLayer::Export.
        
        
        
        """
    @staticmethod
    def SetColorConfigFallbacks(*args, **kwargs):
        """
        
        **classmethod** SetColorConfigFallbacks(colorConfiguration, colorManagementSystem) -> None
        
        
        Sets the global fallback values of color configuration metadata which
        includes the'colorConfiguration'asset path and the name of the color
        management system.
        
        
        This overrides any fallback values authored in plugInfo files.
        
        If the specified value of ``colorConfiguration`` or
        ``colorManagementSystem`` is empty, then the corresponding fallback
        value isn't set. In other words, for this call to have an effect, at
        least one value must be non-empty. Additionally, these can't be reset
        to empty values.
        
        GetColorConfigFallbacks() Color Configuration API
        
        
        Parameters
        ----------
        colorConfiguration : AssetPath
        
        colorManagementSystem : str
        
        
        """
    @staticmethod
    def SetColorConfiguration(*args, **kwargs):
        """
        
        SetColorConfiguration(colorConfig) -> None
        
        
        Sets the default color configuration to be used to interpret the per-
        attribute color-spaces in the composed USD stage.
        
        
        This is specified as asset path which can be resolved to the color
        spec file.
        
        Color Configuration API
        
        
        Parameters
        ----------
        colorConfig : AssetPath
        
        
        """
    @staticmethod
    def SetColorManagementSystem(*args, **kwargs):
        """
        
        SetColorManagementSystem(cms) -> None
        
        
        Sets the name of the color management system used to interpret the
        color configuration file pointed at by the colorConfiguration
        metadata.
        
        
        Color Configuration API
        
        
        Parameters
        ----------
        cms : str
        
        
        """
    @staticmethod
    def SetDefaultPrim(*args, **kwargs):
        """
        
        SetDefaultPrim(prim) -> None
        
        
        Set the default prim layer metadata in this stage's root layer.
        
        
        This is shorthand for:
        
        .. code-block:: text
        
          stage->GetRootLayer()->SetDefaultPrim(prim.GetName());
        
         Note that this function always authors to the stage's root layer. To
        author to a different layer, use the SdfLayer::SetDefaultPrim() API.
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def SetEditTarget(*args, **kwargs):
        """
        
        SetEditTarget(editTarget) -> None
        
        
        Set the stage's EditTarget.
        
        
        If *editTarget.IsLocalLayer()*, check to see if it's a layer in this
        stage's local LayerStack. If not, issue an error and do nothing. If
        *editTarget* is invalid, issue an error and do nothing. If
        *editTarget* differs from the stage's current EditTarget, set the
        EditTarget and send UsdNotice::StageChangedEditTarget. Otherwise do
        nothing.
        
        
        Parameters
        ----------
        editTarget : EditTarget
        
        
        """
    @staticmethod
    def SetEndTimeCode(*args, **kwargs):
        """
        
        SetEndTimeCode(arg1) -> None
        
        
        Sets the stage's end timeCode.
        
        
        The end timeCode is set in the current EditTarget, if it is the root
        layer of the stage or the session layer associated with the stage. If
        the current EditTarget is neither, a warning is issued and the end
        timeCode is not set.
        
        
        Parameters
        ----------
        arg1 : float
        
        
        """
    @staticmethod
    def SetFramesPerSecond(*args, **kwargs):
        """
        
        SetFramesPerSecond(framesPerSecond) -> None
        
        
        Sets the stage's framesPerSecond value.
        
        
        The framesPerSecond value is set in the current EditTarget, if it is
        the root layer of the stage or the session layer associated with the
        stage. If the current EditTarget is neither, a warning is issued and
        no value is set.
        
        GetFramesPerSecond()
        
        
        Parameters
        ----------
        framesPerSecond : float
        
        
        """
    @staticmethod
    def SetGlobalVariantFallbacks(*args, **kwargs):
        """
        
        **classmethod** SetGlobalVariantFallbacks(fallbacks) -> None
        
        
        Set the global variant fallback preferences used in new UsdStages.
        
        
        This overrides any fallbacks configured in plugin metadata, and only
        affects stages created after this call.
        
        This does not affect existing UsdStages.
        
        
        Parameters
        ----------
        fallbacks : PcpVariantFallbackMap
        
        
        """
    @staticmethod
    def SetInterpolationType(*args, **kwargs):
        """
        
        SetInterpolationType(interpolationType) -> None
        
        
        Sets the interpolation type used during value resolution for all
        attributes on this stage.
        
        
        Changing this will cause a UsdNotice::StageContentsChanged notice to
        be sent, as values at times where no samples are authored may have
        changed.
        
        
        Parameters
        ----------
        interpolationType : InterpolationType
        
        
        """
    @staticmethod
    def SetLoadRules(*args, **kwargs):
        """
        
        SetLoadRules(rules) -> None
        
        
        Set the UsdStageLoadRules to govern payload inclusion on this stage.
        
        
        This rebuilds the stage's entire prim hierarchy to follow ``rules`` .
        
        Note that subsequent calls to Load() , Unload() , LoadAndUnload() will
        modify this stages load rules as described in the documentation for
        those member functions.
        
        See Working Set Management for more information.
        
        
        Parameters
        ----------
        rules : StageLoadRules
        
        
        """
    @staticmethod
    def SetMetadata(*args, **kwargs):
        """
        
        SetMetadata(key, value) -> bool
        
        
        Set the value of Stage metadatum ``key`` to ``value`` , if the stage's
        current UsdEditTarget is the root or session layer.
        
        
        If the current EditTarget is any other layer, raise a coding error.
        
        true if authoring was successful, false otherwise. Generates a coding
        error if ``key`` is not allowed as layer metadata.
        
        General Metadata in USD
        
        
        Parameters
        ----------
        key : str
        
        value : T
        
        
        
        ----------------------------------------------------------------------
        
        SetMetadata(key, value) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        key : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def SetMetadataByDictKey(*args, **kwargs):
        """
        
        SetMetadataByDictKey(key, keyPath, value) -> bool
        
        
        Author ``value`` to the field identified by ``key`` and ``keyPath`` at
        the current EditTarget.
        
        
        The ``keyPath`` is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at ``key`` . If
        ``keyPath`` is empty, no action is taken.
        
        true if the value is authored successfully, false otherwise. Generates
        a coding error if ``key`` is not allowed as layer metadata.
        
        Dictionary-valued Metadata
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        value : T
        
        
        
        ----------------------------------------------------------------------
        
        SetMetadataByDictKey(key, keyPath, value) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        key : str
        
        keyPath : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def SetPopulationMask(*args, **kwargs):
        """
        
        SetPopulationMask(mask) -> None
        
        
        Set this stage's population mask and recompose the stage.
        
        
        Parameters
        ----------
        mask : StagePopulationMask
        
        
        """
    @staticmethod
    def SetStartTimeCode(*args, **kwargs):
        """
        
        SetStartTimeCode(arg1) -> None
        
        
        Sets the stage's start timeCode.
        
        
        The start timeCode is set in the current EditTarget, if it is the root
        layer of the stage or the session layer associated with the stage. If
        the current EditTarget is neither, a warning is issued and the start
        timeCode is not set.
        
        
        Parameters
        ----------
        arg1 : float
        
        
        """
    @staticmethod
    def SetTimeCodesPerSecond(*args, **kwargs):
        """
        
        SetTimeCodesPerSecond(timeCodesPerSecond) -> None
        
        
        Sets the stage's timeCodesPerSecond value.
        
        
        The timeCodesPerSecond value is set in the current EditTarget, if it
        is the root layer of the stage or the session layer associated with
        the stage. If the current EditTarget is neither, a warning is issued
        and no value is set.
        
        GetTimeCodesPerSecond()
        
        
        Parameters
        ----------
        timeCodesPerSecond : float
        
        
        """
    @staticmethod
    def Traverse(*args, **kwargs):
        """
        
        Traverse() -> PrimRange
        
        
        Traverse the active, loaded, defined, non-abstract prims on this stage
        depth-first.
        
        
        Traverse() returns a UsdPrimRange, which allows low-latency traversal,
        with the ability to prune subtrees from traversal. It is python
        iterable, so in its simplest form, one can do:
        
        .. code-block:: text
        
          for prim in stage.Traverse():
              print prim.GetPath()
        
        If either a pre-and-post-order traversal or a traversal rooted at a
        particular prim is desired, construct a UsdPrimRange directly.
        
        This is equivalent to UsdPrimRange::Stage() .
        
        
        
        
        ----------------------------------------------------------------------
        
        Traverse(predicate) -> PrimRange
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Traverse the prims on this stage subject to ``predicate`` .
        
        
        This is equivalent to UsdPrimRange::Stage() .
        
        
        Parameters
        ----------
        predicate : _PrimFlagsPredicate
        
        
        """
    @staticmethod
    def TraverseAll(*args, **kwargs):
        """
        
        TraverseAll() -> PrimRange
        
        
        Traverse all the prims on this stage depth-first.
        
        
        
        Traverse()
        
        UsdPrimRange::Stage()
        
        
        
        """
    @staticmethod
    def Unload(*args, **kwargs):
        """
        
        Unload(path) -> None
        
        
        Modify this stage's load rules to unload the prim and its descendants
        specified by ``path`` .
        
        
        See Working Set Management for more information.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def UnmuteLayer(*args, **kwargs):
        """
        
        UnmuteLayer(layerIdentifier) -> None
        
        
        Unmute the layer identified by ``layerIdentifier`` if it had
        previously been muted.
        
        
        Parameters
        ----------
        layerIdentifier : str
        
        
        """
    @staticmethod
    def WriteFallbackPrimTypes(*args, **kwargs):
        """
        
        WriteFallbackPrimTypes() -> None
        
        
        Writes the fallback prim types defined in the schema registry to the
        stage as dictionary valued fallback prim type metadata.
        
        
        If the stage already has fallback prim type metadata, the fallback
        types from the schema registry will be added to the existing metadata,
        only for types that are already present in the dictionary, i.e. this
        won't overwrite existing fallback entries.
        
        The current edit target determines whether the metadata is written to
        the root layer or the session layer. If the edit target specifies
        another layer besides these, this will produce an error.
        
        This function can be used at any point before calling Save or Export
        on a stage to record the fallback types for the current schemas. This
        allows another version of Usd to open this stage and treat prim types
        it doesn't recognize as a type it does recognize defined for it in
        this metadata.
        
        Fallback Prim Types UsdSchemaRegistry::GetFallbackPrimTypes
        
        
        
        """
    @staticmethod
    def _GetPcpCache(*args, **kwargs):
        """
        
        _GetPcpCache() -> Cache
        
        
        
        
        ----------------------------------------------------------------------
        
        _GetPcpCache() -> Cache
        
        
        
        """
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
    """
    
    A strongly concurrency safe collection of UsdStageRefPtr s, enabling
    sharing across multiple clients and threads. See UsdStageCacheContext
    for typical use cases finding UsdStage s in a cache and publishing
    UsdStage s to a cache.
    
    UsdStageCache is strongly thread safe: all operations other than
    construction and destruction may be performed concurrently.
    
    Clients typically populate and fetch UsdStage s in caches by binding a
    UsdStageCacheContext object to a cache, then using the
    UsdStage::Open() API. See UsdStageCacheContext for more details.
    Clients may also populate and fetch directly via
    UsdStageCache::Insert() , UsdStageCache::Find() ,
    UsdStageCache::FindOneMatching() , and
    UsdStageCache::FindAllMatching() API.
    
    Caches provide a mechanism that associates a lightweight key,
    UsdStageCache::Id, with a cached stage. A UsdStageCache::Id can be
    converted to and from long int and string. This can be useful for
    communicating within a third party application that cannot transmit
    arbitrary C++ objects. See UsdStageCache::GetId() .
    
    Clients may iterate all cache elements using
    UsdStageCache::GetAllStages() and remove elements with
    UsdStageCache::Erase() , UsdStageCache::EraseAll() , and
    UsdStageCache::Clear() .
    
    Note that this class is a regular type: it can be copied and assigned
    at will. It is not a singleton. Also, since it holds a collection of
    UsdStageRefPtr objects, copying it does not create new UsdStage
    instances, it merely copies the RefPtrs.
    
    Enabling the USD_STAGE_CACHE TF_DEBUG code will issue debug output for
    UsdStageCache Find/Insert/Erase/Clear operations. Also see
    UsdStageCache::SetDebugName() and UsdStageCache::GetDebugName() .
    
    """
    class Id(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 24
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
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def Clear(*args, **kwargs):
        """
        
        Clear() -> None
        
        
        Remove all entries from this cache, leaving it empty and equivalent to
        a default-constructed cache.
        
        
        Since the cache contains UsdStageRefPtr, erasing a stage from the
        cache will only destroy the stage if no other UsdStageRefPtrs exist
        referring to it.
        
        
        
        """
    @staticmethod
    def Contains(*args, **kwargs):
        """
        
        Contains(stage) -> bool
        
        
        Return true if ``stage`` is present in this cache, false otherwise.
        
        
        Parameters
        ----------
        stage : Stage
        
        
        
        ----------------------------------------------------------------------
        
        Contains(id) -> bool
        
        
        Return true if ``id`` is present in this cache, false otherwise.
        
        
        Parameters
        ----------
        id : Id
        
        
        """
    @staticmethod
    def Erase(*args, **kwargs):
        """
        
        Erase(id) -> bool
        
        
        Erase the stage identified by ``id`` from this cache and return true.
        
        
        If ``id`` is invalid or there is no associated stage in this cache, do
        nothing and return false. Since the cache contains UsdStageRefPtr,
        erasing a stage from the cache will only destroy the stage if no other
        UsdStageRefPtrs exist referring to it.
        
        
        Parameters
        ----------
        id : Id
        
        
        
        ----------------------------------------------------------------------
        
        Erase(stage) -> bool
        
        
        Erase ``stage`` from this cache and return true.
        
        
        If ``stage`` is not present in this cache, do nothing and return
        false. Since the cache contains UsdStageRefPtr, erasing a stage from
        the cache will only destroy the stage if no other UsdStageRefPtrs
        exist referring to it.
        
        
        Parameters
        ----------
        stage : Stage
        
        
        """
    @staticmethod
    def EraseAll(*args, **kwargs):
        """
        
        EraseAll(rootLayer) -> int
        
        
        Erase all stages present in the cache with ``rootLayer`` and return
        the number erased.
        
        
        Since the cache contains UsdStageRefPtr, erasing a stage from the
        cache will only destroy the stage if no other UsdStageRefPtrs exist
        referring to it.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        
        
        ----------------------------------------------------------------------
        
        EraseAll(rootLayer, sessionLayer) -> int
        
        
        Erase all stages present in the cache with ``rootLayer`` and
        ``sessionLayer`` and return the number erased.
        
        
        Since the cache contains UsdStageRefPtr, erasing a stage from the
        cache will only destroy the stage if no other UsdStageRefPtrs exist
        referring to it.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        sessionLayer : Layer
        
        
        
        ----------------------------------------------------------------------
        
        EraseAll(rootLayer, sessionLayer, pathResolverContext) -> int
        
        
        Erase all stages present in the cache with ``rootLayer`` ,
        ``sessionLayer`` , and ``pathResolverContext`` and return the number
        erased.
        
        
        Since the cache contains UsdStageRefPtr, erasing a stage from the
        cache will only destroy the stage if no other UsdStageRefPtrs exist
        referring to it.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        sessionLayer : Layer
        
        pathResolverContext : ResolverContext
        
        
        """
    @staticmethod
    def Find(*args, **kwargs):
        """
        
        Find(id) -> Stage
        
        
        Find the stage in this cache corresponding to ``id`` in this cache.
        
        
        If ``id`` is not valid (see Id::IsValid() ) or if this cache does not
        have a stage corresponding to ``id`` , return null.
        
        
        Parameters
        ----------
        id : Id
        
        
        """
    @staticmethod
    def FindAllMatching(*args, **kwargs):
        """
        
        FindAllMatching(rootLayer) -> list[Stage]
        
        
        Find all stages in this cache with ``rootLayer`` .
        
        
        If there is no matching stage in this cache, return an empty vector.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        
        
        ----------------------------------------------------------------------
        
        FindAllMatching(rootLayer, sessionLayer) -> list[Stage]
        
        
        Find all stages in this cache with ``rootLayer`` and ``sessionLayer``
        .
        
        
        If there is no matching stage in this cache, return an empty vector.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        sessionLayer : Layer
        
        
        
        ----------------------------------------------------------------------
        
        FindAllMatching(rootLayer, pathResolverContext) -> list[Stage]
        
        
        Find all stages in this cache with ``rootLayer`` and
        ``pathResolverContext`` .
        
        
        If there is no matching stage in this cache, return an empty vector.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        pathResolverContext : ResolverContext
        
        
        
        ----------------------------------------------------------------------
        
        FindAllMatching(rootLayer, sessionLayer, pathResolverContext) -> list[Stage]
        
        
        Find all stages in this cache with ``rootLayer`` , ``sessionLayer`` ,
        and ``pathResolverContext`` .
        
        
        If there is no matching stage in this cache, return an empty vector.
        If there is more than one matching stage in this cache, return an
        arbitrary matching one.
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        sessionLayer : Layer
        
        pathResolverContext : ResolverContext
        
        
        """
    @staticmethod
    def FindOneMatching(*args, **kwargs):
        """
        
        FindOneMatching(rootLayer) -> Stage
        
        
        Find a stage in this cache with ``rootLayer`` .
        
        
        If there is no matching stage in this cache, return null. If there is
        more than one matching stage in this cache, return an arbitrary
        matching one. See also FindAllMatching() .
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        
        
        ----------------------------------------------------------------------
        
        FindOneMatching(rootLayer, sessionLayer) -> Stage
        
        
        Find a stage in this cache with ``rootLayer`` and ``sessionLayer`` .
        
        
        If there is no matching stage in this cache, return null. If there is
        more than one matching stage in this cache, return an arbitrary
        matching one. See also FindAllMatching() .
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        sessionLayer : Layer
        
        
        
        ----------------------------------------------------------------------
        
        FindOneMatching(rootLayer, pathResolverContext) -> Stage
        
        
        Find a stage in this cache with ``rootLayer`` and
        ``pathResolverContext`` .
        
        
        If there is no matching stage in this cache, return null. If there is
        more than one matching stage in this cache, return an arbitrary
        matching one.
        
        FindAllMatching()
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        pathResolverContext : ResolverContext
        
        
        
        ----------------------------------------------------------------------
        
        FindOneMatching(rootLayer, sessionLayer, pathResolverContext) -> Stage
        
        
        Find a stage in this cache with ``rootLayer`` , ``sessionLayer`` , and
        ``pathResolverContext`` .
        
        
        If there is no matching stage in this cache, return null. If there is
        more than one matching stage in this cache, return an arbitrary
        matching one.
        
        FindAllMatching()
        
        
        Parameters
        ----------
        rootLayer : Layer
        
        sessionLayer : Layer
        
        pathResolverContext : ResolverContext
        
        
        """
    @staticmethod
    def GetAllStages(*args, **kwargs):
        """
        
        GetAllStages() -> list[Stage]
        
        
        Return a vector containing the stages present in this cache.
        
        
        
        """
    @staticmethod
    def GetDebugName(*args, **kwargs):
        """
        
        GetDebugName() -> str
        
        
        Retrieve this cache's debug name, set with SetDebugName() .
        
        
        If no debug name has been assigned, return the empty string.
        
        
        
        """
    @staticmethod
    def GetId(*args, **kwargs):
        """
        
        GetId(stage) -> Id
        
        
        Return the Id associated with ``stage`` in this cache.
        
        
        If ``stage`` is not present in this cache, return an invalid Id.
        
        
        Parameters
        ----------
        stage : Stage
        
        
        """
    @staticmethod
    def Insert(*args, **kwargs):
        """
        
        Insert(stage) -> Id
        
        
        Insert ``stage`` into this cache and return its associated Id.
        
        
        If the given ``stage`` is already present in this cache, simply return
        its associated Id.
        
        
        Parameters
        ----------
        stage : Stage
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Return true if this cache holds no stages, false otherwise.
        
        
        
        """
    @staticmethod
    def SetDebugName(*args, **kwargs):
        """
        
        SetDebugName(debugName) -> None
        
        
        Assign a debug name to this cache.
        
        
        This will be emitted in debug output messages when the
        USD_STAGE_CACHES debug flag is enabled. If set to the empty string,
        the cache's address will be used instead.
        
        
        Parameters
        ----------
        debugName : str
        
        
        """
    @staticmethod
    def Size(*args, **kwargs):
        """
        
        Size() -> int
        
        
        Return the number of stages present in this cache.
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Default construct an empty cache.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(other)
        
        
        Construct a new cache as a copy of ``other`` .
        
        
        Parameters
        ----------
        other : StageCache
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        """
        
        swap(other) -> None
        
        
        Swap the contents of this cache with ``other`` .
        
        
        Parameters
        ----------
        other : StageCache
        
        
        """
class StageCacheContext(Boost.Python.instance):
    """
    
    A context object that lets the UsdStage::Open() API read from or read
    from and write to a UsdStageCache instance during a scope of
    execution.
    
    Code examples illustrate typical use:
    
    .. code-block:: text
    
      {
          // A stage cache to work with.
          UsdStageCache stageCache;
      
          // Bind this cache.  UsdStage::Open() will attempt to find a matching
          // stage in the cache.  If none is found, it will open a new stage and
          // insert it into the cache.
          UsdStageCacheContext context(stageCache);
      
          // Since the cache is currently empty, this Open call will not find an
          // existing stage in the cache, but will insert the newly opened stage
          // in it.
          auto stage = UsdStage::Open(<args>);
      
          assert(stageCache.Contains(stage));
          
          // A subsequent Open() call with the same arguments will retrieve the
          // stage from cache.
          auto stage2 = UsdStage::Open(<args>);
          assert(stage2 == stage);
      }
    
    The UsdStage::Open() API examines caches in UsdStageCacheContexts that
    exist on the stack in the current thread in order starting with the
    most recently created (deepest in the stack) to the least recently
    created.
    
    The UsdUseButDoNotPopulateCache() function makes a cache available for
    UsdStage::Open() to find stages in, but newly opened stages will not
    be published to it. This can be useful if you want to make use of a
    cache but cannot or do not wish to mutate that cache.
    
    Passing UsdBlockStageCaches disables cache use entirely (as if no
    UsdStageCacheContexts exist on the stack), while
    UsdBlockStageCachePopulation disables writing to all bound caches (as
    if they were all established with UsdUseButDoNotPopulateCache()).
    
    Threading note: Different threads have different call stacks, so
    UsdStageCacheContext objects that exist in one thread's stack do not
    influence calls to UsdStage::Open() from a different thread.
    
    """
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(cache)
        
        
        Bind a cache for calls to UsdStage::Open() to read from and write to.
        
        
        Parameters
        ----------
        cache : StageCache
        
        
        
        ----------------------------------------------------------------------
        
        __init__(holder)
        
        
        Bind a cache for calls to UsdStage::Open() to read from.
        
        
        
        UsdUseButDoNotPopulateCache()
        
        
        Parameters
        ----------
        holder : _NonPopulatingStageCacheWrapper
        
        
        
        ----------------------------------------------------------------------
        
        __init__(blockType)
        
        
        Disable cache use completely (with UsdBlockStageCaches) or only for
        writing (with UsdBlockStageCacheWrites).
        
        
        Parameters
        ----------
        blockType : StageCacheContextBlockType
        
        
        """
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
    """
    
    This class represents rules that govern payload inclusion on
    UsdStages.
    
    Rules are represented as pairs of SdfPath and a Rule enum value, one
    of AllRule, OnlyRule, and NoneRule. To understand how rules apply to
    particular paths, see UsdStageLoadRules::GetEffectiveRuleForPath() .
    
    Convenience methods for manipulating rules by
    typical'Load'and'Unload'operations are provided in
    UsdStageLoadRules::LoadWithoutDescendants() ,
    UsdStageLoadRules::LoadWithDescendants() , UsdStageLoadRules::Unload()
    .
    
    For finer-grained rule crafting, see AddRule() .
    
    Remove redundant rules that do not change the effective load state
    with UsdStageLoadRules::Minimize() .
    
    """
    class Rule(pxr.Tf.Tf_PyEnumWrapper):
        """
        
        These values are paired with paths to govern payload inclusion on
        UsdStages.
        
        """
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
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def AddRule(*args, **kwargs):
        """
        
        AddRule(path, rule) -> None
        
        
        Add a literal rule. If there's already a rule for ``path`` , replace
        it.
        
        
        Parameters
        ----------
        path : Path
        
        rule : Rule
        
        
        """
    @staticmethod
    def GetEffectiveRuleForPath(*args, **kwargs):
        """
        
        GetEffectiveRuleForPath(path) -> Rule
        
        
        Return the"effective"rule for the given ``path`` .
        
        
        For example, if the closest ancestral rule of ``path`` is an
        ``AllRule`` , return ``AllRule`` . If the closest ancestral rule of
        ``path`` is for ``path`` itself and it is an ``OnlyRule`` , return
        ``OnlyRule`` . Otherwise if there is a closest descendant rule to
        ``path`` this is an ``OnlyRule`` or an ``AllRule`` , return
        ``OnlyRule`` . Otherwise return ``NoneRule`` .
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetRules(*args, **kwargs):
        """
        
        GetRules() -> list[tuple[Path, Rule]]
        
        
        Return all the rules as a vector.
        
        
        
        """
    @staticmethod
    def IsLoaded(*args, **kwargs):
        """
        
        IsLoaded(path) -> bool
        
        
        Return true if the given ``path`` is considered loaded by these rules,
        or false if it is considered unloaded.
        
        
        This is equivalent to GetEffectiveRuleForPath(path) != NoneRule.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def IsLoadedWithAllDescendants(*args, **kwargs):
        """
        
        IsLoadedWithAllDescendants(path) -> bool
        
        
        Return true if the given ``path`` and all descendants are considered
        loaded by these rules; false otherwise.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def IsLoadedWithNoDescendants(*args, **kwargs):
        """
        
        IsLoadedWithNoDescendants(path) -> bool
        
        
        Return true if the given ``path`` and is considered loaded, but none
        of its descendants are considered loaded by these rules; false
        otherwise.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def LoadAll(*args, **kwargs):
        """
        
        **classmethod** LoadAll() -> StageLoadRules
        
        
        Return rules that load all payloads.
        
        
        This is equivalent to default-constructed UsdStageLoadRules.
        
        
        
        """
    @staticmethod
    def LoadAndUnload(*args, **kwargs):
        """
        
        LoadAndUnload(loadSet, unloadSet, policy) -> None
        
        
        Add rules as if Unload() was called for each element of ``unloadSet``
        followed by calls to either LoadWithDescendants() (if ``policy`` is
        UsdLoadPolicy::LoadWithDescendants) or LoadWithoutDescendants() (if
        ``policy`` is UsdLoadPolicy::LoadWithoutDescendants) for each element
        of ``loadSet`` .
        
        
        Parameters
        ----------
        loadSet : SdfPathSet
        
        unloadSet : SdfPathSet
        
        policy : LoadPolicy
        
        
        """
    @staticmethod
    def LoadNone(*args, **kwargs):
        """
        
        **classmethod** LoadNone() -> StageLoadRules
        
        
        Return rules that load no payloads.
        
        
        
        """
    @staticmethod
    def LoadWithDescendants(*args, **kwargs):
        """
        
        LoadWithDescendants(path) -> None
        
        
        Add a rule indicating that ``path`` , all its ancestors, and all its
        descendants shall be loaded.
        
        
        Any previous rules created by calling LoadWithoutDescendants() or
        Unload() on this path or descendant paths are replaced by this rule.
        For example, calling LoadWithoutDescendants('/World/sets/kitchen')
        followed by LoadWithDescendants('/World/sets') will effectively remove
        the rule created in the first call. See AddRule() for more direct
        manipulation.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def LoadWithoutDescendants(*args, **kwargs):
        """
        
        LoadWithoutDescendants(path) -> None
        
        
        Add a rule indicating that ``path`` and all its ancestors but none of
        its descendants shall be loaded.
        
        
        Any previous rules created by calling LoadWithDescendants() or
        Unload() on this path or descendant paths are replaced or restricted
        by this rule. For example, calling LoadWithDescendants('/World/sets')
        followed by LoadWithoutDescendants('/World/sets/kitchen') will cause
        everything under'/World/sets'to load except for those things
        under'/World/sets/kitchen'. See AddRule() for more direct
        manipulation.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def Minimize(*args, **kwargs):
        """
        
        Minimize() -> None
        
        
        Remove any redundant rules to make the set of rules as small as
        possible without changing behavior.
        
        
        
        """
    @staticmethod
    def SetRules(*args, **kwargs):
        """
        
        SetRules(rules) -> None
        
        
        Set literal rules, must be sorted by SdfPath::operator< .
        
        
        Parameters
        ----------
        rules : list[tuple[Path, Rule]]
        
        
        
        ----------------------------------------------------------------------
        
        SetRules(rules) -> None
        
        
        Set literal rules, must be sorted by SdfPath::operator< .
        
        
        Parameters
        ----------
        rules : list[tuple[Path, Rule]]
        
        
        """
    @staticmethod
    def Unload(*args, **kwargs):
        """
        
        Unload(path) -> None
        
        
        Add a rule indicating that ``path`` and all its descendants shall be
        unloaded.
        
        
        Any previous rules created by calling LoadWithDescendants() or
        LoadWithoutDescendants() on this path or descendant paths are replaced
        or restricted by this rule. For example, calling
        LoadWithDescendants('/World/sets') followed by
        Unload('/World/sets/kitchen') will cause everything
        under'/World/sets'to load, except for'/World/sets/kitchen'and
        everything under it.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct rules that load all payloads.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : StageLoadRules
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : StageLoadRules
        
        
        """
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
        """
        
        swap(other) -> None
        
        
        Swap the contents of these rules with ``other`` .
        
        
        Parameters
        ----------
        other : StageLoadRules
        
        
        """
class StagePopulationMask(Boost.Python.instance):
    """
    
    This class represents a mask that may be applied to a UsdStage to
    limit the set of UsdPrim s it populates. This is useful in cases where
    clients have a large scene but only wish to view or query a single or
    a handful of objects. For example, suppose we have a city block with
    buildings, cars, crowds of people, and a couple of main characters.
    Some tasks might only require looking at a single main character and
    perhaps a few props. We can create a population mask with the paths to
    the character and props of interest and open a UsdStage with that
    mask. Usd will avoid populating the other objects in the scene, saving
    time and memory. See UsdStage::OpenMasked() for more.
    
    A mask is defined by a set of SdfPath s with the following qualities:
    they are absolute prim paths (or the absolute root path), and no path
    in the set is an ancestor path of any other path in the set other than
    itself. For example, the set of paths ['/a/b','/a/c','/x/y'] is a
    valid mask, but the set of paths ['/a/b','/a/b/c','/x/y'] is
    redundant, since'/a/b'is an ancestor of'/a/b/c'. The path'/a/b/c'may
    be removed. The GetUnion() and Add() methods ensure that no redundant
    paths are added.
    
    Default-constructed UsdStagePopulationMask s are considered empty (
    IsEmpty() ) and include no paths. A population mask containing
    SdfPath::AbsoluteRootPath() includes all paths.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Add(*args, **kwargs):
        """
        
        Add(other) -> StagePopulationMask
        
        
        Assign this mask to be its union with ``other`` and return a reference
        to this mask.
        
        
        Parameters
        ----------
        other : StagePopulationMask
        
        
        
        ----------------------------------------------------------------------
        
        Add(path) -> StagePopulationMask
        
        
        Assign this mask to be its union with ``path`` and return a reference
        to this mask.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def All(*args, **kwargs):
        """
        
        **classmethod** All() -> StagePopulationMask
        
        
        Return a mask that includes all paths.
        
        
        This is the mask that contains the absolute root path.
        
        
        
        """
    @staticmethod
    def GetIncludedChildNames(*args, **kwargs):
        """
        
        GetIncludedChildNames(path, childNames) -> bool
        
        
        Return true if this mask includes any child prims beneath ``path`` ,
        false otherwise.
        
        
        If only specific child prims beneath ``path`` are included, the names
        of those children will be returned in ``childNames`` . If all child
        prims beneath ``path`` are included, ``childNames`` will be empty.
        
        
        Parameters
        ----------
        path : Path
        
        childNames : list[str]
        
        
        """
    @staticmethod
    def GetIntersection(*args, **kwargs):
        """
        
        GetIntersection(other) -> StagePopulationMask
        
        
        Return a mask that is the intersection of this and ``other`` .
        
        
        Parameters
        ----------
        other : StagePopulationMask
        
        
        """
    @staticmethod
    def GetPaths(*args, **kwargs):
        """
        
        GetPaths() -> list[Path]
        
        
        Return the set of paths that define this mask.
        
        
        
        """
    @staticmethod
    def GetUnion(*args, **kwargs):
        """
        
        GetUnion(other) -> StagePopulationMask
        
        
        Return a mask that is the union of this and ``other`` .
        
        
        Parameters
        ----------
        other : StagePopulationMask
        
        
        
        ----------------------------------------------------------------------
        
        GetUnion(path) -> StagePopulationMask
        
        
        Return a mask that is the union of this and a mask containing the
        single ``path`` .
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def Includes(*args, **kwargs):
        """
        
        Includes(other) -> bool
        
        
        Return true if this mask is a superset of ``other`` .
        
        
        That is, if this mask includes at least every path that ``other``
        includes.
        
        
        Parameters
        ----------
        other : StagePopulationMask
        
        
        
        ----------------------------------------------------------------------
        
        Includes(path) -> bool
        
        
        Return true if this mask includes ``path`` .
        
        
        This is true if ``path`` is one of the paths in this mask, or if it is
        either a descendant or an ancestor of one of the paths in this mask.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def IncludesSubtree(*args, **kwargs):
        """
        
        IncludesSubtree(path) -> bool
        
        
        Return true if this mask includes ``path`` and all paths descendant to
        ``path`` .
        
        
        For example, consider a mask containing the path'/a/b'. Then the
        following holds:
        
        .. code-block:: text
        
          mask.Includes('/a') -> true
          mask.Includes('/a/b') -> true
          mask.IncludesSubtree('/a') -> false
          mask.IncludesSubtree('/a/b') -> true
        
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def Intersection(*args, **kwargs):
        """
        
        **classmethod** Intersection(l, r) -> StagePopulationMask
        
        
        Return a mask that is the intersection of ``l`` and ``r`` .
        
        
        Parameters
        ----------
        l : StagePopulationMask
        
        r : StagePopulationMask
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Return true if this mask contains no paths.
        
        
        Empty masks include no paths.
        
        
        
        """
    @staticmethod
    def Union(*args, **kwargs):
        """
        
        **classmethod** Union(l, r) -> StagePopulationMask
        
        
        Return a mask that is the union of ``l`` and ``r`` .
        
        
        Parameters
        ----------
        l : StagePopulationMask
        
        r : StagePopulationMask
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct an empty mask that includes no paths.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : StagePopulationMask
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : StagePopulationMask
        
        
        
        ----------------------------------------------------------------------
        
        __init__(f, l)
        
        
        Construct a mask from the range of paths [f, l).
        
        
        All paths in the range must be absolute prim paths or the absolute
        root path. (See SdfPath::IsAbsolutePath,
        SdfPath::IsAbsoluteRootOrPrimPath).
        
        
        Parameters
        ----------
        f : Iter
        
        l : Iter
        
        
        
        ----------------------------------------------------------------------
        
        __init__(paths)
        
        
        Construct a mask from ``paths`` .
        
        
        All paths must be absolute prim paths or the absolute root path. (See
        SdfPath::IsAbsolutePath, SdfPath::IsAbsoluteRootOrPrimPath).
        
        
        Parameters
        ----------
        paths : list[Path]
        
        
        
        ----------------------------------------------------------------------
        
        __init__(paths)
        
        
        Construct a mask from ``paths`` .
        
        
        All paths must be absolute prim paths or the absolute root path. (See
        SdfPath::IsAbsolutePath, SdfPath::IsAbsoluteRootOrPrimPath).
        
        
        Parameters
        ----------
        paths : list[Path]
        
        
        """
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
    """
    
    Represent a time value, which may be either numeric, holding a double
    value, or a sentinel value UsdTimeCode::Default() .
    
    A UsdTimeCode does *not* represent an SMPTE timecode, although we may,
    in future, support conversion functions between the two. Instead,
    UsdTimeCode is an abstraction that acknowledges that in the principal
    domains of use for USD, there are many different ways of encoding
    time, and USD must be able to capture and translate between all of
    them for interchange, retaining as much intent of the authoring
    application as possible.
    
    A UsdTimeCode is therefore a unitless, generic time measurement that
    serves as the ordinate for time-sampled data in USD files. A client of
    USD relies on the UsdStage (which in turn consults metadata authored
    in its root layer) to define the mapping of TimeCodes to units like
    seconds and frames.
    
    UsdStage::GetStartTimeCode()
    
    UsdStage::GetEndTimeCode()
    
    UsdStage::GetTimeCodesPerSecond()
    
    UsdStage::GetFramesPerSecond() As described in TimeSamples, Defaults,
    and Value Resolution, USD optionally provides an
    unvarying,'default'value for every attribute. UsdTimeCode embodies a
    time value that can either be a floating-point sample time, or the
    default.
    
    All UsdAttribute and derived API that requires a time parameter
    defaults to UsdTimeCode::Default() if the parameter is left
    unspecified, and auto-constructs from a floating-point argument.
    
    UsdTimeCode::EarliestTime() is provided to aid clients who wish to
    retrieve the first authored timesample for any attribute.
    
    """
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
    __instance_size__: typing.ClassVar[int] = 24
    @staticmethod
    def Default(*args, **kwargs):
        """
        
        **classmethod** Default() -> TimeCode
        
        
        Produce a UsdTimeCode representing the sentinel value for'default'.
        
        
        
        In inequality comparisons, Default() is considered less than any
        numeric TimeCode, including EarliestTime() , indicative of the fact
        that in UsdAttribute value resolution, the sample at Default() (if
        any) is always weaker than any numeric timeSample in the same layer.
        For more information, see TimeSamples, Defaults, and Value Resolution
        
        
        
        """
    @staticmethod
    def EarliestTime(*args, **kwargs):
        """
        
        **classmethod** EarliestTime() -> TimeCode
        
        
        Produce a UsdTimeCode representing the lowest/earliest possible
        timeCode.
        
        
        Thus, for any given timeSample *s*, its time ordinate *t* will obey:
        t>= UsdTimeCode::EarliestTime()
        
        This is useful for clients that wish to retrieve the first authored
        timeSample for an attribute, as they can use
        UsdTimeCode::EarliestTime() as the *time* argument to
        UsdAttribute::Get() and UsdAttribute::GetBracketingTimeSamples()
        
        
        
        """
    @staticmethod
    def GetValue(*args, **kwargs):
        """
        
        GetValue() -> float
        
        
        Return the numeric value for this time.
        
        
        If this time *IsDefault()*, return a quiet NaN value.
        
        
        
        """
    @staticmethod
    def IsDefault(*args, **kwargs):
        """
        
        IsDefault() -> bool
        
        
        Return true if this time represents the'default'sentinel value, false
        otherwise.
        
        
        This is equivalent to !IsNumeric().
        
        
        
        """
    @staticmethod
    def IsEarliestTime(*args, **kwargs):
        """
        
        IsEarliestTime() -> bool
        
        
        Return true if this time represents the lowest/earliest possible
        timeCode, false otherwise.
        
        
        
        """
    @staticmethod
    def IsNumeric(*args, **kwargs):
        """
        
        IsNumeric() -> bool
        
        
        Return true if this time represents a numeric value, false otherwise.
        
        
        This is equivalent to !IsDefault().
        
        
        
        """
    @staticmethod
    def SafeStep(*args, **kwargs):
        """
        
        **classmethod** SafeStep(maxValue, maxCompression) -> float
        
        
        Produce a safe step value such that for any numeric UsdTimeCode t in
        [-maxValue, maxValue], t +/- (step / maxCompression) != t with a
        safety factor of 2.
        
        
        This is shorthand for std::numeric_limits<double>::epsilon() \\*
        maxValue \\* maxCompression \\* 2.0. Such a step value is recommended
        for simulating jump discontinuities in time samples. For example,
        author value x at time t, and value y at time t + SafeStep() . This
        ensures that as the sample times are shifted and scaled, t and t +
        SafeStep() remain distinct so long as they adhere to the ``maxValue``
        and ``maxCompression`` limits.
        
        
        Parameters
        ----------
        maxValue : float
        
        maxCompression : float
        
        
        """
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
        """
        
        __init__(t)
        
        
        Construct with optional time value. Impilicitly convert from double.
        
        
        Parameters
        ----------
        t : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(timeCode)
        
        
        Construct and implicitly cast from SdfTimeCode.
        
        
        Parameters
        ----------
        timeCode : TimeCode
        
        
        """
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
    apiSchemas: typing.ClassVar[str] = 'apiSchemas'
    clipSets: typing.ClassVar[str] = 'clipSets'
    clips: typing.ClassVar[str] = 'clips'
    collection: typing.ClassVar[str] = 'collection'
    collection_MultipleApplyTemplate_Excludes: typing.ClassVar[str] = 'collection:__INSTANCE_NAME__:excludes'
    collection_MultipleApplyTemplate_ExpansionRule: typing.ClassVar[str] = 'collection:__INSTANCE_NAME__:expansionRule'
    collection_MultipleApplyTemplate_IncludeRoot: typing.ClassVar[str] = 'collection:__INSTANCE_NAME__:includeRoot'
    collection_MultipleApplyTemplate_Includes: typing.ClassVar[str] = 'collection:__INSTANCE_NAME__:includes'
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
    """
    
    The base class for all *typed* schemas (those that can impart a
    typeName to a UsdPrim), and therefore the base class for all
    instantiable and"IsA"schemas.
    
    UsdTyped implements a typeName-based query for its override of
    UsdSchemaBase::_IsCompatible() . It provides no other behavior.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
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
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdTyped on UsdPrim ``prim`` .
        
        
        Equivalent to UsdTyped::Get (prim.GetStage(), prim.GetPath()) for a
        *valid* ``prim`` , but will not immediately throw an error for an
        invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdTyped on the prim wrapped by ``schemaObj`` .
        
        
        Should be preferred over UsdTyped (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class UsdCollectionMembershipQuery(Boost.Python.instance):
    """
    
    Represents a flattened view of a collection. For more information
    about collections, please see UsdCollectionAPI as a way to encode and
    retrieve a collection from scene description. A
    UsdCollectionMembershipQuery object can be used to answer queries
    about membership of paths in the collection efficiently.
    
    """
    __instance_size__: typing.ClassVar[int] = 128
    @staticmethod
    def GetAsPathExpansionRuleMap(*args, **kwargs):
        """
        
        GetAsPathExpansionRuleMap() -> PathExpansionRuleMap
        
        
        Returns a raw map of the paths included or excluded in the collection
        along with the expansion rules for the included paths.
        
        
        
        """
    @staticmethod
    def GetIncludedCollections(*args, **kwargs):
        """
        
        GetIncludedCollections() -> SdfPathSet
        
        
        Returns a set of paths for all collections that were included in the
        collection from which this UsdCollectionMembershipQuery object was
        computed.
        
        
        This set is recursive, so collections that were included by other
        collections will be part of this set. The collection from which this
        UsdCollectionMembershipQuery object was computed is *not* part of this
        set.
        
        
        
        """
    @staticmethod
    def HasExcludes(*args, **kwargs):
        """
        
        HasExcludes() -> bool
        
        
        Returns true if the collection excludes one or more paths below an
        included path.
        
        
        
        """
    @staticmethod
    def IsPathIncluded(*args, **kwargs):
        """
        
        IsPathIncluded(path, expansionRule) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Returns whether the given path is included in the collection from
        which this UsdCollectionMembershipQuery object was computed.
        
        
        This is the API that clients should use for determining if a given
        object is a member of the collection. To enumerate all the members of
        a collection, use UsdComputeIncludedObjectsFromCollection or
        UsdComputeIncludedPathsFromCollection.
        
        If ``expansionRule`` is not nullptr, it is set to the expansion- rule
        value that caused the path to be included in or excluded from the
        collection. If ``path`` is not included in the collection,
        ``expansionRule`` is set to UsdTokens->exclude.
        
        It is useful to specify this parameter and use this overload of
        IsPathIncluded() , when you're interested in traversing a subtree and
        want to know whether the root of the subtree is included in a
        collection. For evaluating membership of descendants of the root,
        please use the other overload of IsPathIncluded() , that takes both a
        path and the parent expansionRule.
        
        The python version of this method only returns the boolean result. It
        does not return ``expansionRule`` .
        
        
        Parameters
        ----------
        path : Path
        
        expansionRule : str
        
        
        
        ----------------------------------------------------------------------
        
        IsPathIncluded(path, parentExpansionRule, expansionRule) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Returns whether the given path, ``path`` is included in the collection
        from which this UsdCollectionMembershipQuery object was computed,
        given the parent-path's inherited expansion rule,
        ``parentExpansionRule`` .
        
        
        If ``expansionRule`` is not nullptr, it is set to the expansion- rule
        value that caused the path to be included in or excluded from the
        collection. If ``path`` is not included in the collection,
        ``expansionRule`` is set to UsdTokens->exclude.
        
        The python version of this method only returns the boolean result. It
        does not return ``expansionRule`` .
        
        
        Parameters
        ----------
        path : Path
        
        parentExpansionRule : str
        
        expansionRule : str
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Default Constructor, creates an empty UsdCollectionMembershipQuery
        object.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(pathExpansionRuleMap, includedCollections)
        
        
        Constructor that takes a path expansion rule map.
        
        
        The map is scanned for'excludes'when the UsdCollectionMembershipQuery
        object is constructed.
        
        
        Parameters
        ----------
        pathExpansionRuleMap : PathExpansionRuleMap
        
        includedCollections : SdfPathSet
        
        
        
        ----------------------------------------------------------------------
        
        __init__(pathExpansionRuleMap, includedCollections)
        
        
        Constructor that takes a path expansion rule map as an rvalue
        reference.
        
        
        Parameters
        ----------
        pathExpansionRuleMap : PathExpansionRuleMap
        
        includedCollections : SdfPathSet
        
        
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class UsdFileFormat(pxr.Sdf.FileFormat):
    """
    
    File format for USD files.
    
    When creating a file through the SdfLayer::CreateNew() interface, the
    meaningful SdfFileFormat::FileFormatArguments are as follows:
    
       - UsdUsdFileFormatTokens->FormatArg, which must be a supported
         format's'Id'. The possible values are UsdUsdaFileFormatTokens->Id or
         UsdUsdcFileFormatTokens->Id.
         If no UsdUsdFileFormatTokens->FormatArg is supplied, the default is
         UsdUsdcFileFormatTokens->Id.
    
    """
    @staticmethod
    def GetUnderlyingFormatForLayer(*args, **kwargs):
        """
        
        **classmethod** GetUnderlyingFormatForLayer(layer) -> str
        
        
        Returns the value of the"format"argument to be used in the
        FileFormatArguments when exporting or saving the given layer.
        
        
        Returns an empty token if the given layer does not have this file
        format.
        
        
        Parameters
        ----------
        layer : Layer
        
        
        """
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
    """
    
    A UsdVariantSet represents a single VariantSet in USD (e.g.
    modelingVariant or shadingVariant), which can have multiple variations
    that express different sets of opinions about the scene description
    rooted at the prim that defines the VariantSet.
    
    (More detailed description of variants to follow)
    
    """
    @staticmethod
    def AddVariant(*args, **kwargs):
        """
        
        AddVariant(variantName, position) -> bool
        
        
        Author a variant spec for *variantName* in this VariantSet at the
        stage's current EditTarget, in the position specified by ``position``
        .
        
        
        Return true if the spec was successfully authored, false otherwise.
        
        This will create the VariantSet itself, if necessary, so as long as
        UsdPrim "prim"is valid, the following should always work:
        
        .. code-block:: text
        
          UsdVariantSet vs = prim.GetVariantSet("myVariantSet");
          vs.AddVariant("myFirstVariation");
          vs.SetVariantSelection("myFirstVariation");
          {
              UsdEditContext ctx(vs.GetVariantEditContext());
              // Now all of our subsequent edits will go "inside" the 
              // 'myFirstVariation' variant of 'myVariantSet'
          }
        
        
        
        Parameters
        ----------
        variantName : str
        
        position : ListPosition
        
        
        """
    @staticmethod
    def BlockVariantSelection(*args, **kwargs):
        """
        
        BlockVariantSelection() -> bool
        
        
        Block any weaker selections for this VariantSet by authoring an empty
        string at the stage's current EditTarget.
        
        
        Return true on success, false otherwise.
        
        
        
        """
    @staticmethod
    def ClearVariantSelection(*args, **kwargs):
        """
        
        ClearVariantSelection() -> bool
        
        
        Clear any selection for this VariantSet from the current EditTarget.
        
        
        Return true on success, false otherwise.
        
        
        
        """
    @staticmethod
    def GetName(*args, **kwargs):
        """
        
        GetName() -> str
        
        
        Return this VariantSet's name.
        
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        Return this VariantSet's held prim.
        
        
        
        """
    @staticmethod
    def GetVariantEditContext(*args, **kwargs):
        """
        
        GetVariantEditContext(layer) -> tuple[Stage, EditTarget]
        
        
        Helper function for configuring a UsdStage 's EditTarget to author
        into the currently selected variant.
        
        
        Returns configuration for a UsdEditContext
        
        To begin editing into VariantSet *varSet's* currently selected
        variant:
        
        In C++, we would use the following pattern:
        
        .. code-block:: text
        
          {
              UsdEditContext ctxt(varSet.GetVariantEditContext());
          
              // All Usd mutation of the UsdStage on which varSet sits will
              // now go "inside" the currently selected variant of varSet
          }
        
        In python, the pattern is:
        
        .. code-block:: text
        
          with varSet.GetVariantEditContext():
              # Now sending mutations to current variant
        
        See GetVariantEditTarget() for discussion of ``layer`` parameter
        
        
        Parameters
        ----------
        layer : Layer
        
        
        """
    @staticmethod
    def GetVariantEditTarget(*args, **kwargs):
        """
        
        GetVariantEditTarget(layer) -> EditTarget
        
        
        Return a *UsdEditTarget* that edits the currently selected variant in
        this VariantSet in *layer*.
        
        
        If there is no currently selected variant in this VariantSet, return
        an invalid EditTarget.
        
        If *layer* is unspecified, then we will use the layer of our prim's
        stage's current UsdEditTarget.
        
        Currently, we require *layer* to be in the stage's local LayerStack
        (see UsdStage::HasLocalLayer() ), and will issue an error and return
        an invalid EditTarget if *layer* is not. We may relax this restriction
        in the future, if need arises, but it introduces several complications
        in specification and behavior.
        
        
        Parameters
        ----------
        layer : Layer
        
        
        """
    @staticmethod
    def GetVariantNames(*args, **kwargs):
        """
        
        GetVariantNames() -> list[str]
        
        
        Return the composed variant names for this VariantSet, ordered
        lexicographically.
        
        
        
        """
    @staticmethod
    def GetVariantSelection(*args, **kwargs):
        """
        
        GetVariantSelection() -> str
        
        
        Return the variant selection for this VariantSet.
        
        
        If there is no selection, return the empty string.
        
        
        
        """
    @staticmethod
    def HasAuthoredVariant(*args, **kwargs):
        """
        
        HasAuthoredVariant(variantName) -> bool
        
        
        Returns true if this VariantSet already possesses a variant.
        
        
        Parameters
        ----------
        variantName : str
        
        
        """
    @staticmethod
    def HasAuthoredVariantSelection(*args, **kwargs):
        """
        
        HasAuthoredVariantSelection(value) -> bool
        
        
        Returns true if there is a selection authored for this VariantSet in
        any layer.
        
        
        If requested, the variant selection (if any) will be returned in
        ``value`` .
        
        
        Parameters
        ----------
        value : str
        
        
        """
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        IsValid() -> bool
        
        
        Is this UsdVariantSet object usable? If not, calling any of its other
        methods is likely to crash.
        
        
        
        """
    @staticmethod
    def SetVariantSelection(*args, **kwargs):
        """
        
        SetVariantSelection(variantName) -> bool
        
        
        Author a variant selection for this VariantSet, setting it to
        *variantName* in the stage's current EditTarget.
        
        
        If ``variantName`` is empty, clear the variant selection (see
        ClearVariantSelection). Call BlockVariantSelection to explicitly set
        an empty variant selection.
        
        Return true if the selection was successfully authored or cleared,
        false otherwise.
        
        
        Parameters
        ----------
        variantName : str
        
        
        """
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
    """
    
    UsdVariantSets represents the collection of VariantSets that are
    present on a UsdPrim.
    
    A UsdVariantSets object, retrieved from a prim via
    UsdPrim::GetVariantSets() , provides the API for interrogating and
    modifying the composed list of VariantSets active defined on the prim,
    and also the facility for authoring a VariantSet *selection* for any
    of those VariantSets.
    
    """
    @staticmethod
    def AddVariantSet(*args, **kwargs):
        """
        
        AddVariantSet(variantSetName, position) -> VariantSet
        
        
        Find an existing, or create a new VariantSet on the originating
        UsdPrim, named ``variantSetName`` .
        
        
        This step is not always necessary, because if this UsdVariantSets
        object is valid, then
        
        .. code-block:: text
        
          varSetsObj.GetVariantSet(variantSetName).AddVariant(variantName);
        
         will always succeed, creating the VariantSet first, if necessary.
        This method exists for situations in which you want to create a
        VariantSet without necessarily populating it with variants.
        
        
        Parameters
        ----------
        variantSetName : str
        
        position : ListPosition
        
        
        """
    @staticmethod
    def GetAllVariantSelections(*args, **kwargs):
        """
        
        GetAllVariantSelections() -> SdfVariantSelectionMap
        
        
        Returns the composed map of all variant selections authored on the the
        originating UsdPrim, regardless of whether a corresponding variant set
        exists.
        
        
        
        """
    @staticmethod
    def GetNames(*args, **kwargs):
        """
        
        GetNames(names) -> bool
        
        
        Compute the list of all VariantSets authored on the originating
        UsdPrim.
        
        
        Always return true. Clear the contents of ``names`` and store the
        result there.
        
        
        Parameters
        ----------
        names : list[str]
        
        
        
        ----------------------------------------------------------------------
        
        GetNames() -> list[str]
        
        
        Return a list of all VariantSets authored on the originating UsdPrim.
        
        
        
        """
    @staticmethod
    def GetVariantSelection(*args, **kwargs):
        """
        
        GetVariantSelection(variantSetName) -> str
        
        
        Return the composed variant selection for the VariantSet named
        *variantSetName*.
        
        
        If there is no selection, (or ``variantSetName`` does not exist)
        return the empty string.
        
        
        Parameters
        ----------
        variantSetName : str
        
        
        """
    @staticmethod
    def GetVariantSet(*args, **kwargs):
        """
        
        GetVariantSet(variantSetName) -> VariantSet
        
        
        Return a UsdVariantSet object for ``variantSetName`` .
        
        
        This always succeeds, although the returned VariantSet will be invalid
        if the originating prim is invalid
        
        
        Parameters
        ----------
        variantSetName : str
        
        
        """
    @staticmethod
    def HasVariantSet(*args, **kwargs):
        """
        
        HasVariantSet(variantSetName) -> bool
        
        
        Returns true if a VariantSet named ``variantSetName`` exists on the
        originating prim.
        
        
        Parameters
        ----------
        variantSetName : str
        
        
        """
    @staticmethod
    def SetSelection(*args, **kwargs):
        """
        
        SetSelection(variantSetName, variantName) -> bool
        
        
        Parameters
        ----------
        variantSetName : str
        
        variantName : str
        
        
        """
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
    """
    
    Class for reading a zip file. This class is primarily intended to
    support the .usdz file format. It is not a general-purpose zip reader,
    as it does not implement the full zip file specification. In
    particular:
    
       - This class does not natively support decompressing data from a
         zip archive. Clients may access the data exactly as stored in the file
         and perform their own decompression if desired.
    
       - This class does not rely on the central directory in order to
         read the contents of the file. This allows it to operate on partial
         zip archives. However, this also means it may handle certain zip files
         incorrectly. For example, if a file was deleted from a zip archive by
         just removing its central directory header, that file will still be
         found by this class.
    
    
    """
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
        """
        
        DumpContents() -> None
        
        
        Print out listing of contents of this zip archive to stdout.
        
        
        For diagnostic purposes only.
        
        
        
        """
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
        """
        
        **classmethod** Open(filePath) -> ZipFile
        
        
        Opens the zip archive at ``filePath`` .
        
        
        Returns invalid object on error.
        
        
        Parameters
        ----------
        filePath : str
        
        
        
        ----------------------------------------------------------------------
        
        Open(asset) -> ZipFile
        
        
        Opens the zip archive ``asset`` .
        
        
        Returns invalid object on error.
        
        
        Parameters
        ----------
        asset : ArAsset
        
        
        """
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
    """
    
    Class for writing a zip file. This class is primarily intended to
    support the .usdz file format. It is not a general-purpose zip writer,
    as it does not implement the full zip file specification. However, all
    files written by this class should be valid zip files and readable by
    external zip modules and utilities.
    
    """
    @staticmethod
    def AddFile(*args, **kwargs):
        """
        
        AddFile(filePath, filePathInArchive) -> str
        
        
        Adds the file at ``filePath`` to the zip archive with no compression
        applied.
        
        
        If ``filePathInArchive`` is non-empty, the file will be added at that
        path in the archive. Otherwise, it will be added at ``filePath`` .
        
        Returns the file path used to identify the file in the zip archive on
        success. This path conforms to the zip file specification and may not
        be the same as ``filePath`` or ``filePathInArchive`` . Returns an
        empty string on failure.
        
        
        Parameters
        ----------
        filePath : str
        
        filePathInArchive : str
        
        
        """
    @staticmethod
    def CreateNew(*args, **kwargs):
        """
        
        **classmethod** CreateNew(filePath) -> ZipFileWriter
        
        
        Create a new file writer with ``filePath`` as the destination file
        path where the zip archive will be written.
        
        
        The zip file will not be written to ``filePath`` until the writer is
        destroyed or Save() is called.
        
        Returns an invalid object on error.
        
        
        Parameters
        ----------
        filePath : str
        
        
        """
    @staticmethod
    def Discard(*args, **kwargs):
        """
        
        Discard() -> None
        
        
        Discards the zip archive so that it is not saved to the destination
        file path.
        
        
        Once discarded, the file writer is invalid and may not be reused.
        
        
        
        """
    @staticmethod
    def Save(*args, **kwargs):
        """
        
        Save() -> bool
        
        
        Finalizes the zip archive and saves it to the destination file path.
        
        
        Once saved, the file writer is invalid and may not be reused. Returns
        true on success, false otherwise.
        
        
        
        """
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
