from __future__ import annotations
import pxr.Tf
import typing
__all__: list[str] = ['AssetInfo', 'DefaultResolver', 'DefaultResolverContext', 'Notice', 'ResolvedPath', 'Resolver', 'ResolverContext', 'ResolverContextBinder', 'ResolverScopedCache', 'Timestamp']
class AssetInfo(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 136
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
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
    def assetName(*args, **kwargs):
        ...
    @assetName.setter
    def assetName(*args, **kwargs):
        ...
    @property
    def resolverInfo(*args, **kwargs):
        ...
    @resolverInfo.setter
    def resolverInfo(*args, **kwargs):
        ...
    @property
    def version(*args, **kwargs):
        ...
    @version.setter
    def version(*args, **kwargs):
        ...
class DefaultResolver(Resolver):
    @staticmethod
    def SetDefaultSearchPath(*args, **kwargs):
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
class DefaultResolverContext(Boost.Python.instance):
    @staticmethod
    def GetSearchPath(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
class Notice(Boost.Python.instance):
    class ResolverChanged(ResolverNotice):
        @staticmethod
        def AffectsContext(*args, **kwargs):
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
    class ResolverNotice(pxr.Tf.Notice):
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
class ResolvedPath(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def GetPathString(*args, **kwargs):
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
class Resolver(Boost.Python.instance):
    @staticmethod
    def CanWriteAssetToPath(*args, **kwargs):
        ...
    @staticmethod
    def CreateContextFromString(*args, **kwargs):
        ...
    @staticmethod
    def CreateContextFromStrings(*args, **kwargs):
        ...
    @staticmethod
    def CreateDefaultContext(*args, **kwargs):
        ...
    @staticmethod
    def CreateDefaultContextForAsset(*args, **kwargs):
        ...
    @staticmethod
    def CreateIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def CreateIdentifierForNewAsset(*args, **kwargs):
        ...
    @staticmethod
    def GetAssetInfo(*args, **kwargs):
        ...
    @staticmethod
    def GetCurrentContext(*args, **kwargs):
        ...
    @staticmethod
    def GetExtension(*args, **kwargs):
        ...
    @staticmethod
    def GetModificationTimestamp(*args, **kwargs):
        ...
    @staticmethod
    def IsContextDependentPath(*args, **kwargs):
        ...
    @staticmethod
    def RefreshContext(*args, **kwargs):
        ...
    @staticmethod
    def Resolve(*args, **kwargs):
        ...
    @staticmethod
    def ResolveForNewAsset(*args, **kwargs):
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
class ResolverContext(Boost.Python.instance):
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDebugString(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
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
class ResolverContextBinder(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ResolverScopedCache(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Timestamp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def GetTime(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
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
class _PyAnnotatedBoolResult(Boost.Python.instance):
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
    def whyNot(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'ar'
