from __future__ import annotations
import pxr.Tf
import typing
__all__ = ['DefaultResolver', 'DefaultResolverContext', 'Notice', 'ResolvedPath', 'Resolver', 'ResolverContext', 'ResolverContextBinder', 'ResolverScopedCache', 'Timestamp']
class DefaultResolver(Resolver):
    """
    
    Default asset resolution implementation used when no plugin
    implementation is provided.
    
    In order to resolve assets specified by relative paths, this resolver
    implements a simple"search path"scheme. The resolver will anchor the
    relative path to a series of directories and return the first absolute
    path where the asset exists.
    
    The first directory will always be the current working directory. The
    resolver will then examine the directories specified via the following
    mechanisms (in order):
    
       - The currently-bound ArDefaultResolverContext for the calling
         thread
    
       - ArDefaultResolver::SetDefaultSearchPath
    
       - The environment variable PXR_AR_DEFAULT_SEARCH_PATH. This is
         expected to be a list of directories delimited by the platform's
         standard path separator.
    
    ArDefaultResolver supports creating an ArDefaultResolverContext via
    ArResolver::CreateContextFromString by passing a list of directories
    delimited by the platform's standard path separator.
    
    """
    @staticmethod
    def SetDefaultSearchPath(*args, **kwargs):
        """
        
        **classmethod** SetDefaultSearchPath(searchPath) -> None
        
        
        Set the default search path that will be used during asset resolution.
        
        
        This must be called before the first call to ArGetResolver. The
        specified paths will be searched *in addition to, and before* paths
        specified via the environment variable PXR_AR_DEFAULT_SEARCH_PATH
        
        
        Parameters
        ----------
        searchPath : list[str]
        
        
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
class DefaultResolverContext(Boost.Python.instance):
    """
    
    Resolver context object that specifies a search path to use during
    asset resolution. This object is intended for use with the default
    ArDefaultResolver asset resolution implementation; see documentation
    for that class for more details on the search path resolution
    algorithm.
    
    Example usage:
    
    .. code-block:: text
    
      ArDefaultResolverContext ctx({"/Local/Models", "/Installed/Models"});
      {
          // Bind the context object:
          ArResolverContextBinder binder(ctx);
      
         // While the context is bound, all calls to ArResolver::Resolve
         // (assuming ArDefaultResolver is the underlying implementation being
         // used) will include the specified paths during resolution.
         std::string resolvedPath = resolver.Resolve("ModelName/File.txt")
      }
      
      // Once the context is no longer bound (due to the ArResolverContextBinder
      // going out of scope), its search path no longer factors into asset
      // resolution.
    
    
    """
    @staticmethod
    def GetSearchPath(*args, **kwargs):
        """
        
        GetSearchPath() -> list[str]
        
        
        Return this context's search path.
        
        
        
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
        
        
        Default construct a context with no search path.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(searchPath)
        
        
        Construct a context with the given ``searchPath`` .
        
        
        Elements in ``searchPath`` should be absolute paths. If they are not,
        they will be anchored to the current working directory.
        
        
        Parameters
        ----------
        searchPath : list[str]
        
        
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
class Notice(Boost.Python.instance):
    """
    """
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
    """
    
    Represents a resolved asset path.
    
    """
    __instance_size__: typing.ClassVar[int] = 24
    @staticmethod
    def GetPathString(*args, **kwargs):
        """
        
        GetPathString() -> str
        
        
        Return the resolved path held by this object as a string.
        
        
        
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
        
        __init__(resolvedPath)
        
        
        Construct an ArResolvedPath holding the given ``resolvedPath`` .
        
        
        Parameters
        ----------
        resolvedPath : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__(resolvedPath)
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        resolvedPath : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rhs)
        
        
        Parameters
        ----------
        rhs : ResolvedPath
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rhs)
        
        
        Parameters
        ----------
        rhs : ResolvedPath
        
        
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
class Resolver(Boost.Python.instance):
    """
    
    Interface for the asset resolution system. An asset resolver is
    responsible for resolving asset information (including the asset's
    physical path) from a logical path.
    
    See ar_implementing_resolver for information on how to customize asset
    resolution behavior by implementing a subclass of ArResolver. Clients
    may use ArGetResolver to access the configured asset resolver.
    
    """
    @staticmethod
    def CanWriteAssetToPath(*args, **kwargs):
        """
        
        CanWriteAssetToPath(resolvedPath, whyNot) -> bool
        
        
        Returns true if an asset may be written to the given ``resolvedPath``
        , false otherwise.
        
        
        If this function returns false and ``whyNot`` is not ``nullptr`` , it
        may be filled with an explanation.
        
        
        Parameters
        ----------
        resolvedPath : ResolvedPath
        
        whyNot : str
        
        
        """
    @staticmethod
    def CreateContextFromString(*args, **kwargs):
        """
        
        CreateContextFromString(contextStr) -> ResolverContext
        
        
        Return an ArResolverContext created from the primary ArResolver
        implementation using the given ``contextStr`` .
        
        
        Parameters
        ----------
        contextStr : str
        
        
        
        ----------------------------------------------------------------------
        
        CreateContextFromString(uriScheme, contextStr) -> ResolverContext
        
        
        Return an ArResolverContext created from the ArResolver registered for
        the given ``uriScheme`` using the given ``contextStr`` .
        
        
        An empty ``uriScheme`` indicates the primary resolver and is
        equivalent to CreateContextFromString(string).
        
        If no resolver is registered for ``uriScheme`` , returns an empty
        ArResolverContext.
        
        
        Parameters
        ----------
        uriScheme : str
        
        contextStr : str
        
        
        """
    @staticmethod
    def CreateContextFromStrings(*args, **kwargs):
        """
        
        CreateContextFromStrings(contextStrs) -> ResolverContext
        
        
        Return an ArResolverContext created by combining the ArResolverContext
        objects created from the given ``contextStrs`` .
        
        
        ``contextStrs`` is a list of pairs of strings. The first element in
        the pair is the URI scheme for the ArResolver that will be used to
        create the ArResolverContext from the second element in the pair. An
        empty URI scheme indicates the primary resolver.
        
        For example:
        
        .. code-block:: text
        
          ArResolverContext ctx = ArGetResolver().CreateContextFromStrings(
             { {"", "context str 1"}, 
               {"my_scheme", "context str 2"} });
        
        This will use the primary resolver to create an ArResolverContext
        using the string"context str 1"and use the resolver registered for
        the"my_scheme"URI scheme to create an ArResolverContext using"context
        str 2". These contexts will be combined into a single
        ArResolverContext and returned.
        
        If no resolver is registered for a URI scheme in an entry in
        ``contextStrs`` , that entry will be ignored.
        
        
        Parameters
        ----------
        contextStrs : list[tuple[str, str]]
        
        
        """
    @staticmethod
    def CreateDefaultContext(*args, **kwargs):
        """
        
        CreateDefaultContext() -> ResolverContext
        
        
        Return an ArResolverContext that may be bound to this resolver to
        resolve assets when no other context is explicitly specified.
        
        
        The returned ArResolverContext will contain the default context
        returned by the primary resolver and all URI resolvers.
        
        
        
        """
    @staticmethod
    def CreateDefaultContextForAsset(*args, **kwargs):
        """
        
        CreateDefaultContextForAsset(assetPath) -> ResolverContext
        
        
        Return an ArResolverContext that may be bound to this resolver to
        resolve the asset located at ``assetPath`` or referenced by that asset
        when no other context is explicitly specified.
        
        
        The returned ArResolverContext will contain the default context for
        ``assetPath`` returned by the primary resolver and all URI resolvers.
        
        
        Parameters
        ----------
        assetPath : str
        
        
        """
    @staticmethod
    def CreateIdentifier(*args, **kwargs):
        """
        
        CreateIdentifier(assetPath, anchorAssetPath) -> str
        
        
        Returns an identifier for the asset specified by ``assetPath`` .
        
        
        If ``anchorAssetPath`` is not empty, it is the resolved asset path
        that ``assetPath`` should be anchored to if it is a relative path.
        
        
        Parameters
        ----------
        assetPath : str
        
        anchorAssetPath : ResolvedPath
        
        
        """
    @staticmethod
    def CreateIdentifierForNewAsset(*args, **kwargs):
        """
        
        CreateIdentifierForNewAsset(assetPath, anchorAssetPath) -> str
        
        
        Returns an identifier for a new asset specified by ``assetPath`` .
        
        
        If ``anchorAssetPath`` is not empty, it is the resolved asset path
        that ``assetPath`` should be anchored to if it is a relative path.
        
        
        Parameters
        ----------
        assetPath : str
        
        anchorAssetPath : ResolvedPath
        
        
        """
    @staticmethod
    def GetAssetInfo(*args, **kwargs):
        """
        
        GetAssetInfo(assetPath, resolvedPath) -> ArAssetInfo
        
        
        Returns an ArAssetInfo populated with additional metadata (if any)
        about the asset at the given ``assetPath`` .
        
        
        ``resolvedPath`` is the resolved path computed for the given
        ``assetPath`` .
        
        
        Parameters
        ----------
        assetPath : str
        
        resolvedPath : ResolvedPath
        
        
        """
    @staticmethod
    def GetCurrentContext(*args, **kwargs):
        """
        
        GetCurrentContext() -> ResolverContext
        
        
        Returns the asset resolver context currently bound in this thread.
        
        
        
        ArResolver::BindContext, ArResolver::UnbindContext
        
        
        
        """
    @staticmethod
    def GetExtension(*args, **kwargs):
        """
        
        GetExtension(assetPath) -> str
        
        
        Returns the file extension for the given ``assetPath`` .
        
        
        The returned extension does not include a"."at the beginning.
        
        
        Parameters
        ----------
        assetPath : str
        
        
        """
    @staticmethod
    def GetModificationTimestamp(*args, **kwargs):
        """
        
        GetModificationTimestamp(assetPath, resolvedPath) -> Timestamp
        
        
        Returns an ArTimestamp representing the last time the asset at
        ``assetPath`` was modified.
        
        
        ``resolvedPath`` is the resolved path computed for the given
        ``assetPath`` . If a timestamp cannot be retrieved, return an invalid
        ArTimestamp.
        
        
        Parameters
        ----------
        assetPath : str
        
        resolvedPath : ResolvedPath
        
        
        """
    @staticmethod
    def IsContextDependentPath(*args, **kwargs):
        """
        
        IsContextDependentPath(assetPath) -> bool
        
        
        Returns true if ``assetPath`` is a context-dependent path, false
        otherwise.
        
        
        A context-dependent path may result in different resolved paths
        depending on what asset resolver context is bound when Resolve is
        called. Assets located at the same context-dependent path may not be
        the same since those assets may have been loaded from different
        resolved paths. In this case, the assets'resolved paths must be
        consulted to determine if they are the same.
        
        
        Parameters
        ----------
        assetPath : str
        
        
        """
    @staticmethod
    def RefreshContext(*args, **kwargs):
        """
        
        RefreshContext(context) -> None
        
        
        Refresh any caches associated with the given context.
        
        
        If doing so would invalidate asset paths that had previously been
        resolved, an ArNotice::ResolverChanged notice will be sent to inform
        clients of this.
        
        
        Parameters
        ----------
        context : ResolverContext
        
        
        """
    @staticmethod
    def Resolve(*args, **kwargs):
        """
        
        Resolve(assetPath) -> ResolvedPath
        
        
        Returns the resolved path for the asset identified by the given
        ``assetPath`` if it exists.
        
        
        If the asset does not exist, returns an empty ArResolvedPath.
        
        
        Parameters
        ----------
        assetPath : str
        
        
        """
    @staticmethod
    def ResolveForNewAsset(*args, **kwargs):
        """
        
        ResolveForNewAsset(assetPath) -> ResolvedPath
        
        
        Returns the resolved path for the given ``assetPath`` that may be used
        to create a new asset.
        
        
        If such a path cannot be computed for ``assetPath`` , returns an empty
        ArResolvedPath.
        
        Note that an asset might or might not already exist at the returned
        resolved path.
        
        
        Parameters
        ----------
        assetPath : str
        
        
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
class ResolverContext(Boost.Python.instance):
    """
    
    An asset resolver context allows clients to provide additional data to
    the resolver for use during resolution. Clients may provide this data
    via context objects of their own (subject to restrictions below). An
    ArResolverContext is simply a wrapper around these objects that allows
    it to be treated as a single type. Note that an ArResolverContext may
    not hold multiple context objects with the same type.
    
    A client-defined context object must provide the following:
    
       - Default and copy constructors
    
       - operator<
    
       - operator==
    
       - An overload for size_t hash_value(const T&)
    
    Note that the user may define a free function:
    
    std::string ArGetDebugString(const Context & ctx); (Where Context is
    the type of the user's path resolver context.)
    
    This is optional; a default generic implementation has been
    predefined. This function should return a string representation of the
    context to be utilized for debugging purposes(such as in TF_DEBUG
    statements).
    
    The ArIsContextObject template must also be specialized for this
    object to declare that it can be used as a context object. This is to
    avoid accidental use of an unexpected object as a context object. The
    AR_DECLARE_RESOLVER_CONTEXT macro can be used to do this as a
    convenience.
    
    AR_DECLARE_RESOLVER_CONTEXT
    
    ArResolver::BindContext
    
    ArResolver::UnbindContext
    
    ArResolverContextBinder
    
    """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        Get() -> ContextObj
        
        
        Returns pointer to the context object of the given type held in this
        resolver context.
        
        
        Returns None if this resolver context is not holding an object of the
        requested type.
        
        
        
        """
    @staticmethod
    def GetDebugString(*args, **kwargs):
        """
        
        GetDebugString() -> str
        
        
        Returns a debug string representing the contained context objects.
        
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Returns whether this resolver context is empty.
        
        
        
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
        
        
        Construct an empty asset resolver context.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(objs)
        
        
        Construct a resolver context using the given objects ``objs`` .
        
        
        Each argument must either be an ArResolverContext or a registered
        context object. See class documentation for requirements on context
        objects.
        
        If an argument is a context object, it will be added to the
        constructed ArResolverContext. If an argument is an ArResolverContext,
        all of the context objects it holds will be added to the constructed
        ArResolverContext.
        
        Arguments are ordered from strong-to-weak. If a context object is
        encountered with the same type as a previously-added object, the
        previously-added object will remain and the other context object will
        be ignored.
        
        
        Parameters
        ----------
        objs : Objects...
        
        
        
        ----------------------------------------------------------------------
        
        __init__(ctxs)
        
        
        Construct a resolver context using the ArResolverContexts in ``ctxs``
        .
        
        
        All of the context objects held by each ArResolverContext in ``ctxs``
        will be added to the constructed ArResolverContext.
        
        Arguments are ordered from strong-to-weak. If a context object is
        encountered with the same type as a previously-added object, the
        previously-added object will remain and the other context object will
        be ignored.
        
        
        Parameters
        ----------
        ctxs : list[ResolverContext]
        
        
        """
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
    """
    
    Helper object for managing the binding and unbinding of
    ArResolverContext objects with the asset resolver.
    
    Asset Resolver Context Operations
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(context)
        
        
        Bind the given ``context`` with the asset resolver.
        
        
        Calls ArResolver::BindContext on the configured asset resolver and
        saves the bindingData populated by that function.
        
        
        Parameters
        ----------
        context : ResolverContext
        
        
        
        ----------------------------------------------------------------------
        
        __init__(assetResolver, context)
        
        
        Bind the given ``context`` to the given ``assetResolver`` .
        
        
        Calls ArResolver::BindContext on the given ``assetResolver`` and saves
        the bindingData populated by that function.
        
        
        Parameters
        ----------
        assetResolver : Resolver
        
        context : ResolverContext
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ResolverScopedCache(Boost.Python.instance):
    """
    
    Helper object for managing asset resolver cache scopes.
    
    A scoped resolution cache indicates to the resolver that results of
    calls to Resolve should be cached for a certain scope. This is
    important for performance and also for consistency  it ensures that
    repeated calls to Resolve with the same parameters will return the
    same result.
    
    Scoped Resolution Cache
    
    """
    __instance_size__: typing.ClassVar[int] = 24
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
        arg1 : ResolverScopedCache
        
        
        
        ----------------------------------------------------------------------
        
        __init__()
        
        
        Begin an asset resolver cache scope.
        
        
        Calls ArResolver::BeginCacheScope on the configured asset resolver and
        saves the cacheScopeData populated by that function.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(parent)
        
        
        Begin an asset resolver cache scope that shares data with the given
        ``parent`` scope.
        
        
        Calls ArResolver::BeginCacheScope on the configured asset resolver,
        saves the cacheScopeData stored in ``parent`` and passes that to that
        function.
        
        
        Parameters
        ----------
        parent : ResolverScopedCache
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Timestamp(Boost.Python.instance):
    """
    
    Represents a timestamp for an asset. Timestamps are represented by
    Unix time, the number of seconds elapsed since 00:00:00 UTC 1/1/1970.
    
    """
    __instance_size__: typing.ClassVar[int] = 24
    @staticmethod
    def GetTime(*args, **kwargs):
        """
        
        GetTime() -> float
        
        
        Return the time represented by this timestamp as a double.
        
        
        If this timestamp is invalid, issue a coding error and return a quiet
        NaN value.
        
        
        
        """
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        IsValid() -> bool
        
        
        Return true if this timestamp is valid, false otherwise.
        
        
        
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
        
        __init__()
        
        
        Create an invalid timestamp.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(time)
        
        
        Create a timestamp at ``time`` , which must be a Unix time value.
        
        
        Parameters
        ----------
        time : float
        
        
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
class _PyAnnotatedBoolResult(Boost.Python.instance):
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
__MFB_FULL_PACKAGE_NAME: str = 'ar'
