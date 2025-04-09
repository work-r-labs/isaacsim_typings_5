from __future__ import annotations
import typing
__all__ = ['AddCmdlineArgs', 'RefinementComplexities']
class RefinementComplexities:
    """
    
        An enum-like container of standard complexity settings.
        
    """
    class _RefinementComplexity:
        """
        
                Class which represents a level of mesh refinement complexity. Each
                level has a string identifier, a display name, and a float complexity
                value.
                
        """
        def __init__(self, compId, name, value):
            ...
        def __repr__(self):
            ...
        @property
        def id(self):
            ...
        @property
        def name(self):
            ...
        @property
        def value(self):
            ...
    HIGH: typing.ClassVar[RefinementComplexities._RefinementComplexity]  # value = high
    LOW: typing.ClassVar[RefinementComplexities._RefinementComplexity]  # value = low
    MEDIUM: typing.ClassVar[RefinementComplexities._RefinementComplexity]  # value = medium
    VERY_HIGH: typing.ClassVar[RefinementComplexities._RefinementComplexity]  # value = veryhigh
    _ordered: typing.ClassVar[tuple]  # value = (low, medium, high, veryhigh)
    @classmethod
    def fromId(cls, compId):
        """
        
                Get a complexity from its identifier.
                
        """
    @classmethod
    def fromName(cls, name):
        """
        
                Get a complexity from its display name.
                
        """
    @classmethod
    def next(cls, comp):
        """
        
                Get the next highest level of complexity. If already at the highest
                level, return it.
                
        """
    @classmethod
    def ordered(cls):
        """
        
                Get a tuple of all complexity levels in order.
                
        """
    @classmethod
    def prev(cls, comp):
        """
        
                Get the next lowest level of complexity. If already at the lowest
                level, return it.
                
        """
def AddCmdlineArgs(argsParser, defaultValue = ..., altHelpText = ''):
    """
    
        Adds complexity-related command line arguments to argsParser.
    
        The resulting 'complexity' argument will be one of the standard
        RefinementComplexities.
        
    """
