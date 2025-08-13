"""
Python bindings for libSdr
"""
from __future__ import annotations
import pxr.Ndr
import typing
__all__: list[str] = ['NodeContext', 'NodeMetadata', 'NodeRole', 'PropertyMetadata', 'PropertyRole', 'PropertyTypes', 'Registry', 'ShaderNode', 'ShaderNodeList', 'ShaderProperty']
class NodeContext(Boost.Python.instance):
    Displacement: typing.ClassVar[str] = 'displacement'
    DisplayFilter: typing.ClassVar[str] = 'displayFilter'
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
    Tag: typing.ClassVar[str] = 'tag'
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
    @staticmethod
    def GetShaderNodeByIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderNodeByIdentifierAndType(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderNodeByName(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderNodeByNameAndType(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderNodeFromAsset(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderNodeFromSourceCode(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderNodesByFamily(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderNodesByIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderNodesByName(*args, **kwargs):
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
    @staticmethod
    def GetAdditionalPrimvarProperties(*args, **kwargs):
        ...
    @staticmethod
    def GetAllVstructNames(*args, **kwargs):
        ...
    @staticmethod
    def GetAssetIdentifierInputNames(*args, **kwargs):
        ...
    @staticmethod
    def GetCategory(*args, **kwargs):
        ...
    @staticmethod
    def GetDefaultInput(*args, **kwargs):
        ...
    @staticmethod
    def GetDepartments(*args, **kwargs):
        ...
    @staticmethod
    def GetHelp(*args, **kwargs):
        ...
    @staticmethod
    def GetImplementationName(*args, **kwargs):
        ...
    @staticmethod
    def GetLabel(*args, **kwargs):
        ...
    @staticmethod
    def GetPages(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimvars(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyNamesForPage(*args, **kwargs):
        ...
    @staticmethod
    def GetRole(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderInput(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderOutput(*args, **kwargs):
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
class ShaderNodeList(Boost.Python.instance):
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
class ShaderProperty(pxr.Ndr.Property):
    @staticmethod
    def GetDefaultValueAsSdfType(*args, **kwargs):
        ...
    @staticmethod
    def GetHelp(*args, **kwargs):
        ...
    @staticmethod
    def GetHints(*args, **kwargs):
        ...
    @staticmethod
    def GetImplementationName(*args, **kwargs):
        ...
    @staticmethod
    def GetLabel(*args, **kwargs):
        ...
    @staticmethod
    def GetOptions(*args, **kwargs):
        ...
    @staticmethod
    def GetPage(*args, **kwargs):
        ...
    @staticmethod
    def GetVStructConditionalExpr(*args, **kwargs):
        ...
    @staticmethod
    def GetVStructMemberName(*args, **kwargs):
        ...
    @staticmethod
    def GetVStructMemberOf(*args, **kwargs):
        ...
    @staticmethod
    def GetValidConnectionTypes(*args, **kwargs):
        ...
    @staticmethod
    def GetWidget(*args, **kwargs):
        ...
    @staticmethod
    def IsAssetIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def IsDefaultInput(*args, **kwargs):
        ...
    @staticmethod
    def IsVStruct(*args, **kwargs):
        ...
    @staticmethod
    def IsVStructMember(*args, **kwargs):
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
__MFB_FULL_PACKAGE_NAME: str = 'sdr'
