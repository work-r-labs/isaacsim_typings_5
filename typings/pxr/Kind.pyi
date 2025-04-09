"""
Python bindings for libKind
"""
from __future__ import annotations
import typing
__all__ = ['Registry', 'Tokens']
class Registry(Boost.Python.instance):
    """
    
    A singleton that holds known kinds and information about them. See
    Kind Overview for a description of why kind exists, what the builtin
    registered kinds are, and how to extend the core kinds.
    
    KindRegistry Threadsafty
    ========================
    
    KindRegistry serves performance-critical clients that operate under
    the stl threading model, and therefore itself follows that model in
    order to avoid locking during HasKind() and IsA() queries.
    
    To make this robust, KindRegistry exposes no means to mutate the
    registry. All extensions must be accomplished via plugInfo.json files,
    which are consumed once during the registry initialization (See
    Extending the KindRegistry)
    
    """
    @staticmethod
    def GetAllKinds(*args, **kwargs):
        """
        
        **classmethod** GetAllKinds() -> list[str]
        
        
        Return an unordered vector of all kinds known to the registry.
        
        
        
        """
    @staticmethod
    def GetBaseKind(*args, **kwargs):
        """
        
        **classmethod** GetBaseKind(kind) -> str
        
        
        Return the base kind of the given kind.
        
        
        If there is no base, the result will be an empty token. Issues a
        coding error if *kind* is unknown to the registry.
        
        
        Parameters
        ----------
        kind : str
        
        
        """
    @staticmethod
    def HasKind(*args, **kwargs):
        """
        
        **classmethod** HasKind(kind) -> bool
        
        
        Test whether *kind* is known to the registry.
        
        
        Parameters
        ----------
        kind : str
        
        
        """
    @staticmethod
    def IsA(*args, **kwargs):
        """
        
        **classmethod** IsA(derivedKind, baseKind) -> bool
        
        
        Test whether *derivedKind* is the same as *baseKind* or has it as a
        base kind (either directly or indirectly).
        
        
        It is *not* required that *derivedKind* or *baseKind* be known to the
        registry: if they are unknown but equal, IsA will return ``true`` ;
        otherwise if either is unknown, we will simply return false.
        
        Therefore this method will not raise any errors.
        
        
        Parameters
        ----------
        derivedKind : str
        
        baseKind : str
        
        
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
class Tokens(Boost.Python.instance):
    assembly: typing.ClassVar[str] = 'assembly'
    component: typing.ClassVar[str] = 'component'
    group: typing.ClassVar[str] = 'group'
    model: typing.ClassVar[str] = 'model'
    subcomponent: typing.ClassVar[str] = 'subcomponent'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'kind'
