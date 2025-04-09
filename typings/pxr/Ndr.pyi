"""
Python bindings for libNdr
"""
from __future__ import annotations
import pxr.Tf
import typing
__all__ = ['DiscoveryPlugin', 'DiscoveryPluginContext', 'DiscoveryPluginList', 'DiscoveryUri', 'Node', 'NodeDiscoveryResult', 'NodeList', 'Property', 'Registry', 'Version', 'VersionFilter', 'VersionFilterAllVersions', 'VersionFilterDefaultOnly']
class DiscoveryPlugin(Boost.Python.instance):
    """
    
    Interface for discovery plugins.
    
    Discovery plugins, like the name implies, find nodes. Where the plugin
    searches is up to the plugin that implements this interface. Examples
    of discovery plugins could include plugins that look for nodes on the
    filesystem, another that finds nodes in a cloud service, and another
    that searches a local database. Multiple discovery plugins that search
    the filesystem in specific locations/ways could also be created. All
    discovery plugins are executed as soon as the registry is
    instantiated.
    
    These plugins simply report back to the registry what nodes they found
    in a generic way. The registry doesn't know much about the innards of
    the nodes yet, just that the nodes exist. Understanding the nodes is
    the responsibility of another set of plugins defined by the
    ``NdrParserPlugin`` interface.
    
    Discovery plugins report back to the registry via
    ``NdrNodeDiscoveryResult`` s. These are small, lightweight classes
    that contain the information for a single node that was found during
    discovery. The discovery result only includes node information that
    can be gleaned pre-parse, so the data is fairly limited; to see
    exactly what's included, and what is expected to be populated, see the
    documentation for ``NdrNodeDiscoveryResult`` .
    
    How to Create a Discovery Plugin
    ================================
    
    There are three steps to creating a discovery plugin:
    
       - Implement the discovery plugin interface, ``NdrDiscoveryPlugin``
    
       - Register your new plugin with the registry. The registration
         macro must be called in your plugin's implementation file:
    
    .. code-block:: text
    
      NDR_REGISTER_DISCOVERY_PLUGIN(YOUR_DISCOVERY_PLUGIN_CLASS_NAME)
    
     This macro is available in discoveryPlugin.h.
    
       - In the same folder as your plugin, create a ``plugInfo.json``
         file. This file must be formatted like so, substituting
         ``YOUR_LIBRARY_NAME`` , ``YOUR_CLASS_NAME`` , and
         ``YOUR_DISPLAY_NAME`` :
    
    .. code-block:: text
    
      {
          "Plugins": [{
              "Type": "module",
              "Name": "YOUR_LIBRARY_NAME",
              "Root": "@PLUG_INFO_ROOT@",
              "LibraryPath": "@PLUG_INFO_LIBRARY_PATH@",
              "ResourcePath": "@PLUG_INFO_RESOURCE_PATH@",
              "Info": {
                  "Types": {
                      "YOUR_CLASS_NAME" : {
                          "bases": ["NdrDiscoveryPlugin"],
                          "displayName": "YOUR_DISPLAY_NAME"
                      }
                  }
              }
          }]
      }
    
    The NDR ships with one discovery plugin, the
    ``_NdrFilesystemDiscoveryPlugin`` . Take a look at NDR's plugInfo.json
    file for example values for ``YOUR_LIBRARY_NAME`` ,
    ``YOUR_CLASS_NAME`` , and ``YOUR_DISPLAY_NAME`` . If multiple
    discovery plugins exist in the same folder, you can continue adding
    additional plugins under the ``Types`` key in the JSON. More detailed
    information about the plugInfo.json format can be found in the
    documentation for the ``plug`` module (in pxr/base).
    
    
    """
    @staticmethod
    def DiscoverNodes(*args, **kwargs):
        """
        
        DiscoverNodes(arg1) -> NdrNodeDiscoveryResultVec
        
        
        Finds and returns all nodes that the implementing plugin should be
        aware of.
        
        
        Parameters
        ----------
        arg1 : Context
        
        
        """
    @staticmethod
    def GetSearchURIs(*args, **kwargs):
        """
        
        GetSearchURIs() -> NdrStringVec
        
        
        Gets the URIs that this plugin is searching for nodes in.
        
        
        
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
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
class DiscoveryPluginContext(Boost.Python.instance):
    """
    
    A context for discovery.
    
    
    Discovery plugins can use this to get a limited set of non-local
    information without direct coupling between plugins.
    
    """
    @staticmethod
    def GetSourceType(*args, **kwargs):
        """
        
        GetSourceType(discoveryType) -> str
        
        
        Returns the source type associated with the discovery type.
        
        
        This may return an empty token if there is no such association.
        
        
        Parameters
        ----------
        discoveryType : str
        
        
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
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
class DiscoveryPluginList(Boost.Python.instance):
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
class DiscoveryUri(Boost.Python.instance):
    """
    
    Struct for holding a URI and its resolved URI for a file discovered by
    NdrFsHelpersDiscoverFiles.
    
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def resolvedUri(*args, **kwargs):
        ...
    @resolvedUri.setter
    def resolvedUri(*args, **kwargs):
        ...
    @property
    def uri(*args, **kwargs):
        ...
    @uri.setter
    def uri(*args, **kwargs):
        ...
class Node(Boost.Python.instance):
    """
    
    Represents an abstract node. Describes information like the name of
    the node, what its inputs and outputs are, and any associated
    metadata.
    
    In almost all cases, this class will not be used directly. More
    specialized nodes can be created that derive from ``NdrNode`` ; those
    specialized nodes can add their own domain-specific data and methods.
    
    """
    @staticmethod
    def GetContext(*args, **kwargs):
        """
        
        GetContext() -> str
        
        
        Gets the context of the node.
        
        
        The context is the context that the node declares itself as having
        (or, if a particular node does not declare a context, it will be
        assigned a default context by the parser).
        
        As a concrete example from the ``Sdr`` module, a shader with a
        specific source type may perform different duties vs. another shader
        with the same source type. For example, one shader with a source type
        of ``SdrArgsParser::SourceType`` may declare itself as having a
        context of'pattern', while another shader of the same source type may
        say it is used for lighting, and thus has a context of'light'.
        
        
        
        """
    @staticmethod
    def GetFamily(*args, **kwargs):
        """
        
        GetFamily() -> str
        
        
        Gets the name of the family that the node belongs to.
        
        
        An empty token will be returned if the node does not belong to a
        family.
        
        
        
        """
    @staticmethod
    def GetIdentifier(*args, **kwargs):
        """
        
        GetIdentifier() -> NdrIdentifier
        
        
        Return the identifier of the node.
        
        
        
        """
    @staticmethod
    def GetInfoString(*args, **kwargs):
        """
        
        GetInfoString() -> str
        
        
        Gets a string with basic information about this node.
        
        
        Helpful for things like adding this node to a log.
        
        
        
        """
    @staticmethod
    def GetInput(*args, **kwargs):
        """
        
        GetInput(inputName) -> Property
        
        
        Get an input property by name.
        
        
        ``nullptr`` is returned if an input with the given name does not
        exist.
        
        
        Parameters
        ----------
        inputName : str
        
        
        """
    @staticmethod
    def GetInputNames(*args, **kwargs):
        """
        
        GetInputNames() -> NdrTokenVec
        
        
        Get an ordered list of all the input names on this node.
        
        
        
        """
    @staticmethod
    def GetMetadata(*args, **kwargs):
        """
        
        GetMetadata() -> NdrTokenMap
        
        
        All metadata that came from the parse process.
        
        
        Specialized nodes may isolate values in the metadata (with possible
        manipulations and/or additional parsing) and expose those values in
        their API.
        
        
        
        """
    @staticmethod
    def GetName(*args, **kwargs):
        """
        
        GetName() -> str
        
        
        Gets the name of the node.
        
        
        
        """
    @staticmethod
    def GetOutput(*args, **kwargs):
        """
        
        GetOutput(outputName) -> Property
        
        
        Get an output property by name.
        
        
        ``nullptr`` is returned if an output with the given name does not
        exist.
        
        
        Parameters
        ----------
        outputName : str
        
        
        """
    @staticmethod
    def GetOutputNames(*args, **kwargs):
        """
        
        GetOutputNames() -> NdrTokenVec
        
        
        Get an ordered list of all the output names on this node.
        
        
        
        """
    @staticmethod
    def GetResolvedDefinitionURI(*args, **kwargs):
        """
        
        GetResolvedDefinitionURI() -> str
        
        
        Gets the URI to the resource that provided this node's definition.
        
        
        Could be a path to a file, or some other resource identifier. This URI
        should be fully resolved.
        
        NdrNode::GetResolvedImplementationURI()
        
        
        
        """
    @staticmethod
    def GetResolvedImplementationURI(*args, **kwargs):
        """
        
        GetResolvedImplementationURI() -> str
        
        
        Gets the URI to the resource that provides this node's implementation.
        
        
        Could be a path to a file, or some other resource identifier. This URI
        should be fully resolved.
        
        NdrNode::GetResolvedDefinitionURI()
        
        
        
        """
    @staticmethod
    def GetSourceCode(*args, **kwargs):
        """
        
        GetSourceCode() -> str
        
        
        Returns the source code for this node.
        
        
        This will be empty for most nodes. It will be non-empty only for the
        nodes that are constructed using NdrRegistry::GetNodeFromSourceCode()
        , in which case, the source code has not been parsed (or even
        compiled) yet.
        
        An unparsed node with non-empty source-code but no properties is
        considered to be invalid. Once the node is parsed and the relevant
        properties and metadata are extracted from the source code, the node
        becomes valid.
        
        NdrNode::IsValid
        
        
        
        """
    @staticmethod
    def GetSourceType(*args, **kwargs):
        """
        
        GetSourceType() -> str
        
        
        Gets the type of source that this node originated from.
        
        
        Note that this is distinct from ``GetContext()`` , which is the type
        that the node declares itself as having.
        
        As a concrete example from the ``Sdr`` module, several shader parsers
        exist and operate on different types of shaders. In this scenario,
        each distinct type of shader (OSL, Args, etc) is considered a
        different *source*, even though they are all shaders. In addition, the
        shaders under each source type may declare themselves as having a
        specific context (shaders can serve different roles). See
        ``GetContext()`` for more information on this.
        
        
        
        """
    @staticmethod
    def GetVersion(*args, **kwargs):
        """
        
        GetVersion() -> Version
        
        
        Return the version of the node.
        
        
        
        """
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        IsValid() -> bool
        
        
        Whether or not this node is valid.
        
        
        A node that is valid indicates that the parser plugin was able to
        successfully parse the contents of this node.
        
        Note that if a node is not valid, some data like its name, URI, source
        code etc. could still be available (data that was obtained during the
        discovery process). However, other data that must be gathered from the
        parsing process will NOT be available (eg, inputs and outputs).
        
        
        
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
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class NodeDiscoveryResult(Boost.Python.instance):
    """
    
    Represents the raw data of a node, and some other bits of metadata,
    that were determined via a ``NdrDiscoveryPlugin`` .
    
    """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(identifier, version, name, family, discoveryType, sourceType, uri, resolvedUri, sourceCode, metadata, blindData, subIdentifier)
        
        
        Constructor.
        
        
        Parameters
        ----------
        identifier : NdrIdentifier
        
        version : Version
        
        name : str
        
        family : str
        
        discoveryType : str
        
        sourceType : str
        
        uri : str
        
        resolvedUri : str
        
        sourceCode : str
        
        metadata : NdrTokenMap
        
        blindData : str
        
        subIdentifier : str
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def blindData(*args, **kwargs):
        ...
    @property
    def discoveryType(*args, **kwargs):
        ...
    @property
    def family(*args, **kwargs):
        ...
    @property
    def identifier(*args, **kwargs):
        ...
    @property
    def metadata(*args, **kwargs):
        ...
    @property
    def name(*args, **kwargs):
        ...
    @property
    def resolvedUri(*args, **kwargs):
        ...
    @property
    def sourceCode(*args, **kwargs):
        ...
    @property
    def sourceType(*args, **kwargs):
        ...
    @property
    def subIdentifier(*args, **kwargs):
        ...
    @property
    def uri(*args, **kwargs):
        ...
    @property
    def version(*args, **kwargs):
        ...
class NodeList(Boost.Python.instance):
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
class Property(Boost.Python.instance):
    """
    
    Represents a property (input or output) that is part of a ``NdrNode``
    instance.
    
    A property must have a name and type, but may also specify a host of
    additional metadata. Instances can also be queried to determine if
    another ``NdrProperty`` instance can be connected to it.
    
    In almost all cases, this class will not be used directly. More
    specialized properties can be created that derive from ``NdrProperty``
    ; those specialized properties can add their own domain-specific data
    and methods.
    
    """
    @staticmethod
    def CanConnectTo(*args, **kwargs):
        """
        
        CanConnectTo(other) -> bool
        
        
        Determines if this property can be connected to the specified
        property.
        
        
        Parameters
        ----------
        other : Property
        
        
        """
    @staticmethod
    def GetArraySize(*args, **kwargs):
        """
        
        GetArraySize() -> int
        
        
        Gets this property's array size.
        
        
        If this property is a fixed-size array type, the array size is
        returned. In the case of a dynamically-sized array, this method
        returns the array size that the parser reports, and should not be
        relied upon to be accurate. A parser may report -1 for the array size,
        for example, to indicate a dynamically-sized array. For types that are
        not a fixed-size array or dynamic array, this returns 0.
        
        
        
        """
    @staticmethod
    def GetDefaultValue(*args, **kwargs):
        """
        
        GetDefaultValue() -> VtValue
        
        
        Gets this property's default value associated with the type of the
        property.
        
        
        
        GetType()
        
        
        
        """
    @staticmethod
    def GetInfoString(*args, **kwargs):
        """
        
        GetInfoString() -> str
        
        
        Gets a string with basic information about this property.
        
        
        Helpful for things like adding this property to a log.
        
        
        
        """
    @staticmethod
    def GetMetadata(*args, **kwargs):
        """
        
        GetMetadata() -> NdrTokenMap
        
        
        All of the metadata that came from the parse process.
        
        
        
        """
    @staticmethod
    def GetName(*args, **kwargs):
        """
        
        GetName() -> str
        
        
        Gets the name of the property.
        
        
        
        """
    @staticmethod
    def GetType(*args, **kwargs):
        """
        
        GetType() -> str
        
        
        Gets the type of the property.
        
        
        
        """
    @staticmethod
    def GetTypeAsSdfType(*args, **kwargs):
        """
        
        GetTypeAsSdfType() -> NdrSdfTypeIndicator
        
        
        Converts the property's type from ``GetType()`` into a
        ``SdfValueTypeName`` .
        
        
        Two scenarios can result: an exact mapping from property type to Sdf
        type, and an inexact mapping. In the first scenario, the first element
        in the pair will be the cleanly-mapped Sdf type, and the second
        element, a TfToken, will be empty. In the second scenario, the Sdf
        type will be set to ``Token`` to indicate an unclean mapping, and the
        second element will be set to the original type returned by
        ``GetType()`` .
        
        GetDefaultValueAsSdfType
        
        
        
        """
    @staticmethod
    def IsArray(*args, **kwargs):
        """
        
        IsArray() -> bool
        
        
        Whether this property's type is an array type.
        
        
        
        """
    @staticmethod
    def IsConnectable(*args, **kwargs):
        """
        
        IsConnectable() -> bool
        
        
        Whether this property can be connected to other properties.
        
        
        If this returns ``true`` , connectability to a specific property can
        be tested via ``CanConnectTo()`` .
        
        
        
        """
    @staticmethod
    def IsDynamicArray(*args, **kwargs):
        """
        
        IsDynamicArray() -> bool
        
        
        Whether this property's array type is dynamically-sized.
        
        
        
        """
    @staticmethod
    def IsOutput(*args, **kwargs):
        """
        
        IsOutput() -> bool
        
        
        Whether this property is an output.
        
        
        
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
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Registry(Boost.Python.instance):
    """
    
    The registry provides access to node information."Discovery
    Plugins"are responsible for finding the nodes that should be included
    in the registry.
    
    Discovery plugins are found through the plugin system. If additional
    discovery plugins need to be specified, a client can pass them to
    ``SetExtraDiscoveryPlugins()`` .
    
    When the registry is first told about the discovery plugins, the
    plugins will be asked to discover nodes. These plugins will generate
    ``NdrNodeDiscoveryResult`` instances, which only contain basic
    metadata. Once the client asks for information that would require the
    node's contents to be parsed (eg, what its inputs and outputs are),
    the registry will begin the parsing process on an as-needed basis. See
    ``NdrNodeDiscoveryResult`` for the information that can be retrieved
    without triggering a parse.
    
    Some methods in this module may allow for a"family"to be provided. A
    family is simply a generic grouping which is optional.
    
    """
    @staticmethod
    def GetAllNodeSourceTypes(*args, **kwargs):
        """
        
        GetAllNodeSourceTypes() -> NdrTokenVec
        
        
        Get a sorted list of all node source types that may be present on the
        nodes in the registry.
        
        
        Source types originate from the discovery process, but there is no
        guarantee that the discovered source types will also have a registered
        parser plugin. The actual supported source types here depend on the
        parsers that are available. Also note that some parser plugins may not
        advertise a source type.
        
        See the documentation for ``NdrParserPlugin`` and
        ``NdrNode::GetSourceType()`` for more information.
        
        
        
        """
    @staticmethod
    def GetNodeByIdentifier(*args, **kwargs):
        """
        
        GetNodeByIdentifier(identifier, sourceTypePriority) -> Node
        
        
        Get the node with the specified ``identifier`` , and an optional
        ``sourceTypePriority`` list specifying the set of node SOURCE types
        (see ``NdrNode::GetSourceType()`` ) that should be searched.
        
        
        If no sourceTypePriority is specified, the first encountered node with
        the specified identifier will be returned (first is arbitrary) if
        found.
        
        If a sourceTypePriority list is specified, then this will iterate
        through each source type and try to find a node matching by
        identifier. This is equivalent to calling
        NdrRegistry::GetNodeByIdentifierAndType for each source type until a
        node is found.
        
        Nodes of the same identifier but different source type can exist in
        the registry. If a node'Foo'with source types'abc'and'xyz'exist in the
        registry, and you want to make sure the'abc'version is fetched before
        the'xyz'version, the priority list would be specified as
        ['abc','xyz']. If the'abc'version did not exist in the registry, then
        the'xyz'version would be returned.
        
        Returns ``nullptr`` if a node matching the arguments can't be found.
        
        
        Parameters
        ----------
        identifier : NdrIdentifier
        
        sourceTypePriority : NdrTokenVec
        
        
        """
    @staticmethod
    def GetNodeByIdentifierAndType(*args, **kwargs):
        """
        
        GetNodeByIdentifierAndType(identifier, sourceType) -> Node
        
        
        Get the node with the specified ``identifier`` and ``sourceType`` .
        
        
        If there is no matching node for the sourceType, nullptr is returned.
        
        
        Parameters
        ----------
        identifier : NdrIdentifier
        
        sourceType : str
        
        
        """
    @staticmethod
    def GetNodeByName(*args, **kwargs):
        """
        
        GetNodeByName(name, sourceTypePriority, filter) -> Node
        
        
        Get the node with the specified name.
        
        
        An optional priority list specifies the set of node SOURCE types (
        
        NdrNode::GetSourceType() ) that should be searched and in what order.
        Optionally, a filter can be specified to consider just the default
        versions of nodes matching ``name`` (the default) or all versions of
        the nodes.
        
        GetNodeByIdentifier() .
        
        
        Parameters
        ----------
        name : str
        
        sourceTypePriority : NdrTokenVec
        
        filter : VersionFilter
        
        
        """
    @staticmethod
    def GetNodeByNameAndType(*args, **kwargs):
        """
        
        GetNodeByNameAndType(name, sourceType, filter) -> Node
        
        
        A convenience wrapper around ``GetNodeByName()`` .
        
        
        Instead of providing a priority list, an exact type is specified, and
        ``nullptr`` is returned if a node with the exact identifier and type
        does not exist.
        
        Optionally, a filter can be specified to consider just the default
        versions of nodes matching ``name`` (the default) or all versions of
        the nodes.
        
        
        Parameters
        ----------
        name : str
        
        sourceType : str
        
        filter : VersionFilter
        
        
        """
    @staticmethod
    def GetNodeFromAsset(*args, **kwargs):
        """
        
        GetNodeFromAsset(asset, metadata, subIdentifier, sourceType) -> Node
        
        
        Parses the given ``asset`` , constructs a NdrNode from it and adds it
        to the registry.
        
        
        Nodes created from an asset using this API can be looked up by the
        unique identifier and sourceType of the returned node, or by URI,
        which will be set to the unresolved asset path value.
        
        ``metadata`` contains additional metadata needed for parsing and
        compiling the source code in the file pointed to by ``asset``
        correctly. This metadata supplements the metadata available in the
        asset and overrides it in cases where there are key collisions.
        
        ``subidentifier`` is optional, and it would be used to indicate a
        particular definition in the asset file if the asset contains multiple
        node definitions.
        
        ``sourceType`` is optional, and it is only needed to indicate a
        particular type if the asset file is capable of representing a node
        definition of multiple source types.
        
        Returns a valid node if the asset is parsed successfully using one of
        the registered parser plugins.
        
        
        Parameters
        ----------
        asset : AssetPath
        
        metadata : NdrTokenMap
        
        subIdentifier : str
        
        sourceType : str
        
        
        """
    @staticmethod
    def GetNodeFromSourceCode(*args, **kwargs):
        """
        
        GetNodeFromSourceCode(sourceCode, sourceType, metadata) -> Node
        
        
        Parses the given ``sourceCode`` string, constructs a NdrNode from it
        and adds it to the registry.
        
        
        The parser to be used is determined by the specified ``sourceType`` .
        
        Nodes created from source code using this API can be looked up by the
        unique identifier and sourceType of the returned node.
        
        ``metadata`` contains additional metadata needed for parsing and
        compiling the source code correctly. This metadata supplements the
        metadata available in ``sourceCode`` and overrides it cases where
        there are key collisions.
        
        Returns a valid node if the given source code is parsed successfully
        using the parser plugins that is registered for the specified
        ``sourceType`` .
        
        
        Parameters
        ----------
        sourceCode : str
        
        sourceType : str
        
        metadata : NdrTokenMap
        
        
        """
    @staticmethod
    def GetNodeIdentifiers(*args, **kwargs):
        """
        
        GetNodeIdentifiers(family, filter) -> NdrIdentifierVec
        
        
        Get the identifiers of all the nodes that the registry is aware of.
        
        
        This will not run the parsing plugins on the nodes that have been
        discovered, so this method is relatively quick. Optionally,
        a"family"name can be specified to only get the identifiers of nodes
        that belong to that family and a filter can be specified to get just
        the default version (the default) or all versions of the node.
        
        
        Parameters
        ----------
        family : str
        
        filter : VersionFilter
        
        
        """
    @staticmethod
    def GetNodeNames(*args, **kwargs):
        """
        
        GetNodeNames(family) -> NdrStringVec
        
        
        Get the names of all the nodes that the registry is aware of.
        
        
        This will not run the parsing plugins on the nodes that have been
        discovered, so this method is relatively quick. Optionally,
        a"family"name can be specified to only get the names of nodes that
        belong to that family.
        
        
        Parameters
        ----------
        family : str
        
        
        """
    @staticmethod
    def GetNodesByFamily(*args, **kwargs):
        """
        
        GetNodesByFamily(family, filter) -> NdrNodeConstPtrVec
        
        
        Get all nodes from the registry, optionally restricted to the nodes
        that fall under a specified family and/or the default version.
        
        
        Note that this will parse *all* nodes that the registry is aware of
        (unless a family is specified), so this may take some time to run the
        first time it is called.
        
        
        Parameters
        ----------
        family : str
        
        filter : VersionFilter
        
        
        """
    @staticmethod
    def GetNodesByIdentifier(*args, **kwargs):
        """
        
        GetNodesByIdentifier(identifier) -> NdrNodeConstPtrVec
        
        
        Get all nodes matching the specified identifier (multiple nodes of the
        same identifier, but different source types, may exist).
        
        
        If no nodes match the identifier, an empty vector is returned.
        
        
        Parameters
        ----------
        identifier : NdrIdentifier
        
        
        """
    @staticmethod
    def GetNodesByName(*args, **kwargs):
        """
        
        GetNodesByName(name, filter) -> NdrNodeConstPtrVec
        
        
        Get all nodes matching the specified name.
        
        
        Only nodes matching the specified name will be parsed. Optionally, a
        filter can be specified to get just the default version (the default)
        or all versions of the node. If no nodes match an empty vector is
        returned.
        
        
        Parameters
        ----------
        name : str
        
        filter : VersionFilter
        
        
        """
    @staticmethod
    def GetSearchURIs(*args, **kwargs):
        """
        
        GetSearchURIs() -> NdrStringVec
        
        
        Get the locations where the registry is searching for nodes.
        
        
        Depending on which discovery plugins were used, this may include non-
        filesystem paths.
        
        
        
        """
    @staticmethod
    def SetExtraDiscoveryPlugins(*args, **kwargs):
        """
        
        SetExtraDiscoveryPlugins(plugins) -> None
        
        
        Allows the client to set any additional discovery plugins that would
        otherwise NOT be found through the plugin system.
        
        
        Runs the discovery process for the specified plugins immediately.
        
        Note that this method cannot be called after any nodes in the registry
        have been parsed (eg, through GetNode\\*()), otherwise an error will
        result.
        
        
        Parameters
        ----------
        plugins : DiscoveryPluginRefPtrVec
        
        
        
        ----------------------------------------------------------------------
        
        SetExtraDiscoveryPlugins(pluginTypes) -> None
        
        
        Allows the client to set any additional discovery plugins that would
        otherwise NOT be found through the plugin system.
        
        
        Runs the discovery process for the specified plugins immediately.
        
        Note that this method cannot be called after any nodes in the registry
        have been parsed (eg, through GetNode\\*()), otherwise an error will
        result.
        
        
        Parameters
        ----------
        pluginTypes : list[Type]
        
        
        """
    @staticmethod
    def SetExtraParserPlugins(*args, **kwargs):
        """
        
        SetExtraParserPlugins(pluginTypes) -> None
        
        
        Allows the client to set any additional parser plugins that would
        otherwise NOT be found through the plugin system.
        
        
        Note that this method cannot be called after any nodes in the registry
        have been parsed (eg, through GetNode\\*()), otherwise an error will
        result.
        
        
        Parameters
        ----------
        pluginTypes : list[Type]
        
        
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
class Version(Boost.Python.instance):
    """
    """
    @staticmethod
    def GetAsDefault(*args, **kwargs):
        """
        
        GetAsDefault() -> Version
        
        
        Return an equal version marked as default.
        
        
        It's permitted to mark an invalid version as the default.
        
        
        
        """
    @staticmethod
    def GetMajor(*args, **kwargs):
        """
        
        GetMajor() -> int
        
        
        Return the major version number or zero for an invalid version.
        
        
        
        """
    @staticmethod
    def GetMinor(*args, **kwargs):
        """
        
        GetMinor() -> int
        
        
        Return the minor version number or zero for an invalid version.
        
        
        
        """
    @staticmethod
    def GetStringSuffix(*args, **kwargs):
        """
        
        GetStringSuffix() -> str
        
        
        Return the version as a identifier suffix.
        
        
        
        """
    @staticmethod
    def IsDefault(*args, **kwargs):
        """
        
        IsDefault() -> bool
        
        
        Return true iff this version is marked as default.
        
        
        
        """
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
        """
        
        __init__()
        
        
        Create an invalid version.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(major, minor)
        
        
        Create a version with the given major and minor numbers.
        
        
        Numbers must be non-negative, and at least one must be non-zero.  On
        failure generates an error and yields an invalid version.
        
        
        Parameters
        ----------
        major : int
        
        minor : int
        
        
        
        ----------------------------------------------------------------------
        
        __init__(x)
        
        
        Create a version from a string.
        
        
        On failure generates an error and yields an invalid version.
        
        
        Parameters
        ----------
        x : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__(x, arg2)
        
        
        Parameters
        ----------
        x : Version
        
        arg2 : bool
        
        
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
class VersionFilter(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Ndr.VersionFilterDefaultOnly, Ndr.VersionFilterAllVersions)
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
class _AnnotatedBool(Boost.Python.instance):
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
    def message(*args, **kwargs):
        ...
class _FilesystemDiscoveryPlugin(DiscoveryPlugin):
    class Context(DiscoveryPluginContext):
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
            ...
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
        @property
        def expired(*args, **kwargs):
            """
            True if this object has expired, False otherwise.
            """
    @staticmethod
    def DiscoverNodes(*args, **kwargs):
        ...
    @staticmethod
    def GetSearchURIs(*args, **kwargs):
        ...
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
        ...
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
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
VersionFilterAllVersions: VersionFilter  # value = Ndr.VersionFilterAllVersions
VersionFilterDefaultOnly: VersionFilter  # value = Ndr.VersionFilterDefaultOnly
__MFB_FULL_PACKAGE_NAME: str = 'ndr'
