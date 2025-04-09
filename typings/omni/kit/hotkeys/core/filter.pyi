from __future__ import annotations
import typing
__all__: list = ['HotkeyFilter']
class HotkeyFilter:
    """
    
        Hotkey filter class.
        
    """
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, other):
        ...
    def __init__(self, context: typing.Optional[str] = None, windows: typing.Optional[typing.List[str]] = None):
        """
        
                Define a hotkey filter object.
        
                Keyword Args:
                    context (Optional[str]): Name of context to filter. Default None.
                    windows (Optional[List[str]]): List of window names to filter. Default None
        
                Returns:
                    The hotkey filter object that was created.
                
        """
    def __str__(self):
        ...
    @property
    def windows_text(self):
        """
        
                String of windows defined in this filter.
                
        """
