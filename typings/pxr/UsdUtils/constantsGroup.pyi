"""
A module for creating groups of constants. This is similar to the enum
module, but enum is not available in Python 2's standard library.
"""
from __future__ import annotations
import sys as sys
import types as types
__all__ = ['ConstantsGroup', 'defineConstantsGroup', 'sys', 'types']
class ConstantsGroup:
    """
    The base constant group class, intended to be inherited by actual groups
        of constants.
        
    """
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
class _MetaConstantsGroup(type):
    """
    A meta-class which handles the creation and behavior of ConstantsGroups.
        
    """
    @staticmethod
    def __new__(metacls, cls, bases, classdict):
        """
        Discover constants and create a new ConstantsGroup class.
        """
    @classmethod
    def __delattr__(cls, name):
        """
        Prevent deletion of properties after a group is created.
        """
    @classmethod
    def __setattr__(cls, name, value):
        """
        Prevent modification of properties after a group is created.
        """
    def __contains__(self, value):
        """
        Check if a constant exists in the group.
        """
    def __iter__(self):
        """
        Iterate over each constant in the group.
        """
    def __len__(self):
        """
        Get the number of constants in the group.
        """
defineConstantsGroup: str = '\nclass ConstantsGroup(object, metaclass=_MetaConstantsGroup):\n    """The base constant group class, intended to be inherited by actual groups\n    of constants.\n    """\n\n    def __new__(cls, *args, **kwargs):\n        raise TypeError("ConstantsGroup objects cannot be created.")\n'
