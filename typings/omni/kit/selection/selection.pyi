from __future__ import annotations
import omni as omni
from omni.kit.selection.selection_actions import deregister_actions
from omni.kit.selection.selection_actions import register_actions
from pxr import Gf
from pxr import Kind
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
from pxr import UsdGeom
import typing
__all__ = ['Gf', 'HideUnselectedCommand', 'Kind', 'Sdf', 'SelectAllCommand', 'SelectHierarchyCommand', 'SelectInvertCommand', 'SelectKindCommand', 'SelectLeafCommand', 'SelectListCommand', 'SelectNoneCommand', 'SelectParentCommand', 'SelectSimilarCommand', 'SelectionExtension', 'Tf', 'Trace', 'Usd', 'UsdGeom', 'deregister_actions', 'omni', 'register_actions']
class HideUnselectedCommand(omni.kit.commands.command.Command):
    """
    
        Hide prims not selected.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def do(*args, **kwargs):
        ...
    def __init__(self):
        ...
    def _get_all_children(self, prim):
        ...
    def _get_parent_prims(self, stage, prim):
        ...
    def undo(self):
        ...
class SelectAllCommand(omni.kit.commands.command.Command):
    """
    
        Select all prims.
    
        Args:
            type (Optional[str]): Specific type name. If it's None, it will select
            all prims. If it has type str with value "", it will select all prims without any type.
            Otherwise, it will select prims with that type.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def do(*args, **kwargs):
        ...
    def __init__(self, type = None):
        ...
    def undo(self):
        ...
class SelectHierarchyCommand(omni.kit.commands.command.Command):
    """
    
        Set the new selection to all child prims of the current selection.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self):
        ...
    def _collect_hierarchy(self, prim, hierarchy_set):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class SelectInvertCommand(omni.kit.commands.command.Command):
    """
    
        Deselect current prims, and select everything else not selected before.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def do(*args, **kwargs):
        ...
    def __init__(self):
        ...
    def undo(self):
        ...
class SelectKindCommand(omni.kit.commands.command.Command):
    """
    
        Set the new selection to all prim with the given kind.
    
        Keyword Args:
            kind (str): kind of prim to select.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def do(*args, **kwargs):
        ...
    def __init__(self, **kwargs):
        ...
    def undo(self):
        ...
class SelectLeafCommand(omni.kit.commands.command.Command):
    """
    
        Set the new selection to all descendant prims of the current selection.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self):
        ...
    def collect_leafs(self, prim, leaf_set):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class SelectListCommand(omni.kit.commands.command.Command):
    """
    
        Set the new selection from the given list of prim paths.
    
        Keyword Args:
            selection (List[str]): the new selection to set.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, **kwargs):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class SelectNoneCommand(omni.kit.commands.command.Command):
    """
    
        Deselect all selected prims.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class SelectParentCommand(omni.kit.commands.command.Command):
    """
    
        Set the new selection to all parent prims of the current selection.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class SelectSimilarCommand(omni.kit.commands.command.Command):
    """
    
        Select all prims with the same type of the current selection.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class SelectionExtension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
