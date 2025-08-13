"""
Python bindings for libNdr
"""
from __future__ import annotations
import pxr.Tf
import typing
__all__: list[str] = ['DiscoveryPlugin', 'DiscoveryPluginContext', 'DiscoveryPluginList', 'DiscoveryUri', 'Node', 'NodeDiscoveryResult', 'NodeList', 'Property', 'Registry', 'Version', 'VersionFilter', 'VersionFilterAllVersions', 'VersionFilterDefaultOnly']
class DiscoveryPlugin(Boost.Python.instance):
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
    @staticmethod
    def GetSourceType(*args, **kwargs):
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
    __instance_size__: typing.ClassVar[int] = 48
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
    __instance_size__: typing.ClassVar[int] = 88
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
    @staticmethod
    def GetContext(*args, **kwargs):
        ...
    @staticmethod
    def GetFamily(*args, **kwargs):
        ...
    @staticmethod
    def GetIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def GetInfoString(*args, **kwargs):
        ...
    @staticmethod
    def GetInput(*args, **kwargs):
        ...
    @staticmethod
    def GetInputNames(*args, **kwargs):
        ...
    @staticmethod
    def GetMetadata(*args, **kwargs):
        ...
    @staticmethod
    def GetName(*args, **kwargs):
        ...
    @staticmethod
    def GetOutput(*args, **kwargs):
        ...
    @staticmethod
    def GetOutputNames(*args, **kwargs):
        ...
    @staticmethod
    def GetResolvedDefinitionURI(*args, **kwargs):
        ...
    @staticmethod
    def GetResolvedImplementationURI(*args, **kwargs):
        ...
    @staticmethod
    def GetSourceCode(*args, **kwargs):
        ...
    @staticmethod
    def GetSourceType(*args, **kwargs):
        ...
    @staticmethod
    def GetVersion(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        ...
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
    @staticmethod
    def __init__(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 48
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
    @staticmethod
    def CanConnectTo(*args, **kwargs):
        ...
    @staticmethod
    def GetArraySize(*args, **kwargs):
        ...
    @staticmethod
    def GetDefaultValue(*args, **kwargs):
        ...
    @staticmethod
    def GetInfoString(*args, **kwargs):
        ...
    @staticmethod
    def GetMetadata(*args, **kwargs):
        ...
    @staticmethod
    def GetName(*args, **kwargs):
        ...
    @staticmethod
    def GetType(*args, **kwargs):
        ...
    @staticmethod
    def GetTypeAsSdfType(*args, **kwargs):
        ...
    @staticmethod
    def IsArray(*args, **kwargs):
        ...
    @staticmethod
    def IsConnectable(*args, **kwargs):
        ...
    @staticmethod
    def IsDynamicArray(*args, **kwargs):
        ...
    @staticmethod
    def IsOutput(*args, **kwargs):
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
class Registry(Boost.Python.instance):
    @staticmethod
    def GetAllNodeSourceTypes(*args, **kwargs):
        ...
    @staticmethod
    def GetNodeByIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def GetNodeByIdentifierAndType(*args, **kwargs):
        ...
    @staticmethod
    def GetNodeByName(*args, **kwargs):
        ...
    @staticmethod
    def GetNodeByNameAndType(*args, **kwargs):
        ...
    @staticmethod
    def GetNodeFromAsset(*args, **kwargs):
        ...
    @staticmethod
    def GetNodeFromSourceCode(*args, **kwargs):
        ...
    @staticmethod
    def GetNodeIdentifiers(*args, **kwargs):
        ...
    @staticmethod
    def GetNodeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetNodesByFamily(*args, **kwargs):
        ...
    @staticmethod
    def GetNodesByIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def GetNodesByName(*args, **kwargs):
        ...
    @staticmethod
    def GetSearchURIs(*args, **kwargs):
        ...
    @staticmethod
    def SetExtraDiscoveryPlugins(*args, **kwargs):
        ...
    @staticmethod
    def SetExtraParserPlugins(*args, **kwargs):
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
class Version(Boost.Python.instance):
    @staticmethod
    def GetAsDefault(*args, **kwargs):
        ...
    @staticmethod
    def GetMajor(*args, **kwargs):
        ...
    @staticmethod
    def GetMinor(*args, **kwargs):
        ...
    @staticmethod
    def GetStringSuffix(*args, **kwargs):
        ...
    @staticmethod
    def IsDefault(*args, **kwargs):
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
    __instance_size__: typing.ClassVar[int] = 64
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
