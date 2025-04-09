"""
Python bindings for libSdr
"""
from __future__ import annotations
import pxr.Ndr
import typing
__all__ = ['NodeContext', 'NodeMetadata', 'NodeRole', 'PropertyMetadata', 'PropertyRole', 'PropertyTypes', 'Registry', 'ShaderNode', 'ShaderNodeList', 'ShaderProperty']
class NodeContext(Boost.Python.instance):
    Displacement: typing.ClassVar[str] = 'displacement'
    Light: typing.ClassVar[str] = 'light'
    LightFilter: typing.ClassVar[str] = 'lightFilter'
    Pattern: typing.ClassVar[str] = 'pattern'
    PixelFilter: typing.ClassVar[str] = 'pixelFilter'
    SampleFilter: typing.ClassVar[str] = 'sampleFilter'
    Surface: typing.ClassVar[str] = 'surface'
    Volume: typing.ClassVar[str] = 'volume'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class NodeMetadata(Boost.Python.instance):
    Category: typing.ClassVar[str] = 'category'
    Departments: typing.ClassVar[str] = 'departments'
    Help: typing.ClassVar[str] = 'help'
    ImplementationName: typing.ClassVar[str] = '__SDR__implementationName'
    Label: typing.ClassVar[str] = 'label'
    Pages: typing.ClassVar[str] = 'pages'
    Primvars: typing.ClassVar[str] = 'primvars'
    Role: typing.ClassVar[str] = 'role'
    SdrDefinitionNameFallbackPrefix: typing.ClassVar[str] = 'sdrDefinitionNameFallbackPrefix'
    SdrUsdEncodingVersion: typing.ClassVar[str] = 'sdrUsdEncodingVersion'
    Target: typing.ClassVar[str] = '__SDR__target'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class NodeRole(Boost.Python.instance):
    Field: typing.ClassVar[str] = 'field'
    Math: typing.ClassVar[str] = 'math'
    Primvar: typing.ClassVar[str] = 'primvar'
    Texture: typing.ClassVar[str] = 'texture'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class PropertyMetadata(Boost.Python.instance):
    Colorspace: typing.ClassVar[str] = '__SDR__colorspace'
    Connectable: typing.ClassVar[str] = 'connectable'
    DefaultInput: typing.ClassVar[str] = '__SDR__defaultinput'
    Help: typing.ClassVar[str] = 'help'
    Hints: typing.ClassVar[str] = 'hints'
    ImplementationName: typing.ClassVar[str] = '__SDR__implementationName'
    IsAssetIdentifier: typing.ClassVar[str] = '__SDR__isAssetIdentifier'
    IsDynamicArray: typing.ClassVar[str] = 'isDynamicArray'
    Label: typing.ClassVar[str] = 'label'
    Options: typing.ClassVar[str] = 'options'
    Page: typing.ClassVar[str] = 'page'
    RenderType: typing.ClassVar[str] = 'renderType'
    Role: typing.ClassVar[str] = 'role'
    SdrUsdDefinitionType: typing.ClassVar[str] = 'sdrUsdDefinitionType'
    Target: typing.ClassVar[str] = '__SDR__target'
    ValidConnectionTypes: typing.ClassVar[str] = 'validConnectionTypes'
    VstructConditionalExpr: typing.ClassVar[str] = 'vstructConditionalExpr'
    VstructMemberName: typing.ClassVar[str] = 'vstructMemberName'
    VstructMemberOf: typing.ClassVar[str] = 'vstructMemberOf'
    Widget: typing.ClassVar[str] = 'widget'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class PropertyRole(Boost.Python.instance):
    None: typing.ClassVar[str] = 'none'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class PropertyTypes(Boost.Python.instance):
    Color: typing.ClassVar[str] = 'color'
    Color4: typing.ClassVar[str] = 'color4'
    Float: typing.ClassVar[str] = 'float'
    Int: typing.ClassVar[str] = 'int'
    Matrix: typing.ClassVar[str] = 'matrix'
    Normal: typing.ClassVar[str] = 'normal'
    Point: typing.ClassVar[str] = 'point'
    String: typing.ClassVar[str] = 'string'
    Struct: typing.ClassVar[str] = 'struct'
    Terminal: typing.ClassVar[str] = 'terminal'
    Unknown: typing.ClassVar[str] = 'unknown'
    Vector: typing.ClassVar[str] = 'vector'
    Vstruct: typing.ClassVar[str] = 'vstruct'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Registry(pxr.Ndr.Registry):
    """
    
    The shading-specialized version of ``NdrRegistry`` .
    
    """
    @staticmethod
    def GetShaderNodeByIdentifier(*args, **kwargs):
        """
        
        GetShaderNodeByIdentifier(identifier, typePriority) -> ShaderNode
        
        
        Exactly like ``NdrRegistry::GetNodeByIdentifier()`` , but returns a
        ``SdrShaderNode`` pointer instead of a ``NdrNode`` pointer.
        
        
        Parameters
        ----------
        identifier : NdrIdentifier
        
        typePriority : NdrTokenVec
        
        
        """
    @staticmethod
    def GetShaderNodeByIdentifierAndType(*args, **kwargs):
        """
        
        GetShaderNodeByIdentifierAndType(identifier, nodeType) -> ShaderNode
        
        
        Exactly like ``NdrRegistry::GetNodeByIdentifierAndType()`` , but
        returns a ``SdrShaderNode`` pointer instead of a ``NdrNode`` pointer.
        
        
        Parameters
        ----------
        identifier : NdrIdentifier
        
        nodeType : str
        
        
        """
    @staticmethod
    def GetShaderNodeByName(*args, **kwargs):
        """
        
        GetShaderNodeByName(name, typePriority, filter) -> ShaderNode
        
        
        Exactly like ``NdrRegistry::GetNodeByName()`` , but returns a
        ``SdrShaderNode`` pointer instead of a ``NdrNode`` pointer.
        
        
        Parameters
        ----------
        name : str
        
        typePriority : NdrTokenVec
        
        filter : VersionFilter
        
        
        """
    @staticmethod
    def GetShaderNodeByNameAndType(*args, **kwargs):
        """
        
        GetShaderNodeByNameAndType(name, nodeType, filter) -> ShaderNode
        
        
        Exactly like ``NdrRegistry::GetNodeByNameAndType()`` , but returns a
        ``SdrShaderNode`` pointer instead of a ``NdrNode`` pointer.
        
        
        Parameters
        ----------
        name : str
        
        nodeType : str
        
        filter : VersionFilter
        
        
        """
    @staticmethod
    def GetShaderNodeFromAsset(*args, **kwargs):
        """
        
        GetShaderNodeFromAsset(shaderAsset, metadata, subIdentifier, sourceType) -> ShaderNode
        
        
        Wrapper method for NdrRegistry::GetNodeFromAsset() .
        
        
        Returns a valid SdrShaderNode pointer upon success.
        
        
        Parameters
        ----------
        shaderAsset : AssetPath
        
        metadata : NdrTokenMap
        
        subIdentifier : str
        
        sourceType : str
        
        
        """
    @staticmethod
    def GetShaderNodeFromSourceCode(*args, **kwargs):
        """
        
        GetShaderNodeFromSourceCode(sourceCode, sourceType, metadata) -> ShaderNode
        
        
        Wrapper method for NdrRegistry::GetNodeFromSourceCode() .
        
        
        Returns a valid SdrShaderNode pointer upon success.
        
        
        Parameters
        ----------
        sourceCode : str
        
        sourceType : str
        
        metadata : NdrTokenMap
        
        
        """
    @staticmethod
    def GetShaderNodesByFamily(*args, **kwargs):
        """
        
        GetShaderNodesByFamily(family, filter) -> SdrShaderNodePtrVec
        
        
        Exactly like ``NdrRegistry::GetNodesByFamily()`` , but returns a
        vector of ``SdrShaderNode`` pointers instead of a vector of
        ``NdrNode`` pointers.
        
        
        Parameters
        ----------
        family : str
        
        filter : VersionFilter
        
        
        """
    @staticmethod
    def GetShaderNodesByIdentifier(*args, **kwargs):
        """
        
        GetShaderNodesByIdentifier(identifier) -> SdrShaderNodePtrVec
        
        
        Exactly like ``NdrRegistry::GetNodesByIdentifier()`` , but returns a
        vector of ``SdrShaderNode`` pointers instead of a vector of
        ``NdrNode`` pointers.
        
        
        Parameters
        ----------
        identifier : NdrIdentifier
        
        
        """
    @staticmethod
    def GetShaderNodesByName(*args, **kwargs):
        """
        
        GetShaderNodesByName(name, filter) -> SdrShaderNodePtrVec
        
        
        Exactly like ``NdrRegistry::GetNodesByName()`` , but returns a vector
        of ``SdrShaderNode`` pointers instead of a vector of ``NdrNode``
        pointers.
        
        
        Parameters
        ----------
        name : str
        
        filter : VersionFilter
        
        
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
class ShaderNode(pxr.Ndr.Node):
    """
    
    A specialized version of ``NdrNode`` which holds shading information.
    
    """
    @staticmethod
    def GetAdditionalPrimvarProperties(*args, **kwargs):
        """
        
        GetAdditionalPrimvarProperties() -> NdrTokenVec
        
        
        The list of string input properties whose values provide the names of
        additional primvars consumed by this node.
        
        
        For example, this may return a token named ``varname`` . This
        indicates that the client should query the value of a (presumed to be
        string-valued) input attribute named varname from its scene
        description to determine the name of a primvar the node will consume.
        See ``GetPrimvars()`` for additional information.
        
        
        
        """
    @staticmethod
    def GetAllVstructNames(*args, **kwargs):
        """
        
        GetAllVstructNames() -> NdrTokenVec
        
        
        Gets all vstructs that are present in the shader.
        
        
        
        """
    @staticmethod
    def GetAssetIdentifierInputNames(*args, **kwargs):
        """
        
        GetAssetIdentifierInputNames() -> NdrTokenVec
        
        
        Returns the list of all inputs that are tagged as asset identifier
        inputs.
        
        
        
        """
    @staticmethod
    def GetCategory(*args, **kwargs):
        """
        
        GetCategory() -> str
        
        
        The category assigned to this node, if any.
        
        
        Distinct from the family returned from ``GetFamily()`` .
        
        
        
        """
    @staticmethod
    def GetDefaultInput(*args, **kwargs):
        """
        
        GetDefaultInput() -> ShaderProperty
        
        
        Returns the first shader input that is tagged as the default input.
        
        
        A default input and its value can be used to acquire a fallback value
        for a node when the node is considered'disabled'or otherwise incapable
        of producing an output value.
        
        
        
        """
    @staticmethod
    def GetDepartments(*args, **kwargs):
        """
        
        GetDepartments() -> NdrTokenVec
        
        
        The departments this node is associated with, if any.
        
        
        
        """
    @staticmethod
    def GetHelp(*args, **kwargs):
        """
        
        GetHelp() -> str
        
        
        The help message assigned to this node, if any.
        
        
        
        """
    @staticmethod
    def GetImplementationName(*args, **kwargs):
        """
        
        GetImplementationName() -> str
        
        
        Returns the implementation name of this node.
        
        
        The name of the node is how to refer to the node in shader networks.
        The label is how to present this node to users. The implementation
        name is the name of the function (or something) this node represents
        in the implementation. Any client using the implementation **must**
        call this method to get the correct name; using ``getName()`` is not
        correct.
        
        
        
        """
    @staticmethod
    def GetLabel(*args, **kwargs):
        """
        
        GetLabel() -> str
        
        
        The label assigned to this node, if any.
        
        
        Distinct from the name returned from ``GetName()`` . In the context of
        a UI, the label value might be used as the display name for the node
        instead of the name.
        
        
        
        """
    @staticmethod
    def GetPages(*args, **kwargs):
        """
        
        GetPages() -> NdrTokenVec
        
        
        Gets the pages on which the node's properties reside (an aggregate of
        the unique ``SdrShaderProperty::GetPage()`` values for all of the
        node's properties).
        
        
        Nodes themselves do not reside on pages. In an example scenario,
        properties might be divided into two pages,'Simple'and'Advanced'.
        
        
        
        """
    @staticmethod
    def GetPrimvars(*args, **kwargs):
        """
        
        GetPrimvars() -> NdrTokenVec
        
        
        The list of primvars this node knows it requires / uses.
        
        
        For example, a shader node may require the'normals'primvar to function
        correctly. Additional, user specified primvars may have been authored
        on the node. These can be queried via
        ``GetAdditionalPrimvarProperties()`` . Together, ``GetPrimvars()`` and
        ``GetAdditionalPrimvarProperties()`` , provide the complete list of
        primvar requirements for the node.
        
        
        
        """
    @staticmethod
    def GetPropertyNamesForPage(*args, **kwargs):
        """
        
        GetPropertyNamesForPage(pageName) -> NdrTokenVec
        
        
        Gets the names of the properties on a certain page (one that was
        returned by ``GetPages()`` ).
        
        
        To get properties that are not assigned to a page, an empty string can
        be used for ``pageName`` .
        
        
        Parameters
        ----------
        pageName : str
        
        
        """
    @staticmethod
    def GetRole(*args, **kwargs):
        """
        
        GetRole() -> str
        
        
        Returns the role of this node.
        
        
        This is used to annotate the role that the shader node plays inside a
        shader network. We can tag certain shaders to indicate their role
        within a shading network. We currently tag primvar reading nodes,
        texture reading nodes and nodes that access volume fields (like
        extinction or scattering). This is done to identify resources used by
        a shading network.
        
        
        
        """
    @staticmethod
    def GetShaderInput(*args, **kwargs):
        """
        
        GetShaderInput(inputName) -> ShaderProperty
        
        
        Get a shader input property by name.
        
        
        ``nullptr`` is returned if an input with the given name does not
        exist.
        
        
        Parameters
        ----------
        inputName : str
        
        
        """
    @staticmethod
    def GetShaderOutput(*args, **kwargs):
        """
        
        GetShaderOutput(outputName) -> ShaderProperty
        
        
        Get a shader output property by name.
        
        
        ``nullptr`` is returned if an output with the given name does not
        exist.
        
        
        Parameters
        ----------
        outputName : str
        
        
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
class ShaderNodeList(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class ShaderProperty(pxr.Ndr.Property):
    """
    
    A specialized version of ``NdrProperty`` which holds shading
    information.
    
    """
    @staticmethod
    def GetDefaultValueAsSdfType(*args, **kwargs):
        """
        
        GetDefaultValueAsSdfType() -> VtValue
        
        
        Accessor for default value corresponding to the SdfValueTypeName
        returned by GetTypeAsSdfType.
        
        
        Note that this is different than GetDefaultValue which returns the
        default value associated with the SdrPropertyType and may differ from
        the SdfValueTypeName, example when sdrUsdDefinitionType metadata is
        specified for a sdr property.
        
        GetTypeAsSdfType
        
        
        
        """
    @staticmethod
    def GetHelp(*args, **kwargs):
        """
        
        GetHelp() -> str
        
        
        The help message assigned to this property, if any.
        
        
        
        """
    @staticmethod
    def GetHints(*args, **kwargs):
        """
        
        GetHints() -> NdrTokenMap
        
        
        Any UI"hints"that are associated with this property.
        
        
        "Hints"are simple key/value pairs.
        
        
        
        """
    @staticmethod
    def GetImplementationName(*args, **kwargs):
        """
        
        GetImplementationName() -> str
        
        
        Returns the implementation name of this property.
        
        
        The name of the property is how to refer to the property in shader
        networks. The label is how to present this property to users. The
        implementation name is the name of the parameter this property
        represents in the implementation. Any client using the implementation
        **must** call this method to get the correct name; using ``getName()``
        is not correct.
        
        
        
        """
    @staticmethod
    def GetLabel(*args, **kwargs):
        """
        
        GetLabel() -> str
        
        
        The label assigned to this property, if any.
        
        
        Distinct from the name returned from ``GetName()`` . In the context of
        a UI, the label value might be used as the display name for the
        property instead of the name.
        
        
        
        """
    @staticmethod
    def GetOptions(*args, **kwargs):
        """
        
        GetOptions() -> NdrOptionVec
        
        
        If the property has a set of valid values that are pre-determined,
        this will return the valid option names and corresponding string
        values (if the option was specified with a value).
        
        
        
        """
    @staticmethod
    def GetPage(*args, **kwargs):
        """
        
        GetPage() -> str
        
        
        The page (group), eg"Advanced", this property appears on, if any.
        
        
        Note that the page for a shader property can be nested, delimited
        by":", representing the hierarchy of sub-pages a property is defined
        in.
        
        
        
        """
    @staticmethod
    def GetVStructConditionalExpr(*args, **kwargs):
        """
        
        GetVStructConditionalExpr() -> str
        
        
        If this field is part of a vstruct, this is the conditional
        expression.
        
        
        
        """
    @staticmethod
    def GetVStructMemberName(*args, **kwargs):
        """
        
        GetVStructMemberName() -> str
        
        
        If this field is part of a vstruct, this is its name in the struct.
        
        
        
        """
    @staticmethod
    def GetVStructMemberOf(*args, **kwargs):
        """
        
        GetVStructMemberOf() -> str
        
        
        If this field is part of a vstruct, this is the name of the struct.
        
        
        
        """
    @staticmethod
    def GetValidConnectionTypes(*args, **kwargs):
        """
        
        GetValidConnectionTypes() -> NdrTokenVec
        
        
        Gets the list of valid connection types for this property.
        
        
        This value comes from shader metadata, and may not be specified. The
        value from ``NdrProperty::GetType()`` can be used as a fallback, or
        you can use the connectability test in ``CanConnectTo()`` .
        
        
        
        """
    @staticmethod
    def GetWidget(*args, **kwargs):
        """
        
        GetWidget() -> str
        
        
        The widget"hint"that indicates the widget that can best display the
        type of data contained in this property, if any.
        
        
        Examples of this value could include"number","slider", etc.
        
        
        
        """
    @staticmethod
    def IsAssetIdentifier(*args, **kwargs):
        """
        
        IsAssetIdentifier() -> bool
        
        
        Determines if the value held by this property is an asset identifier
        (eg, a file path); the logic for this is left up to the parser.
        
        
        Note: The type returned from ``GetTypeAsSdfType()`` will be ``Asset``
        if this method returns ``true`` (even though its true underlying data
        type is string).
        
        
        
        """
    @staticmethod
    def IsDefaultInput(*args, **kwargs):
        """
        
        IsDefaultInput() -> bool
        
        
        Determines if the value held by this property is the default input for
        this node.
        
        
        
        """
    @staticmethod
    def IsVStruct(*args, **kwargs):
        """
        
        IsVStruct() -> bool
        
        
        Returns true if the field is the head of a vstruct.
        
        
        
        """
    @staticmethod
    def IsVStructMember(*args, **kwargs):
        """
        
        IsVStructMember() -> bool
        
        
        Returns true if this field is part of a vstruct.
        
        
        
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
__MFB_FULL_PACKAGE_NAME: str = 'sdr'
