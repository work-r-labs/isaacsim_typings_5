"""
Python bindings for libKind
"""
from __future__ import annotations
import typing
__all__: list[str] = ['Registry', 'Tokens']
class Registry(Boost.Python.instance):
    @staticmethod
    def GetAllKinds(*args, **kwargs):
        ...
    @staticmethod
    def GetBaseKind(*args, **kwargs):
        ...
    @staticmethod
    def HasKind(*args, **kwargs):
        ...
    @staticmethod
    def IsA(*args, **kwargs):
        ...
    @staticmethod
    def IsAssembly(*args, **kwargs):
        ...
    @staticmethod
    def IsComponent(*args, **kwargs):
        ...
    @staticmethod
    def IsGroup(*args, **kwargs):
        ...
    @staticmethod
    def IsModel(*args, **kwargs):
        ...
    @staticmethod
    def IsSubComponent(*args, **kwargs):
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
