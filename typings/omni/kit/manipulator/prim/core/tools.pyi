"""
This module provides classes for creating and managing toolbar buttons and tools for primitive manipulation in the Omniverse Kit.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.manipulator.prim.core.settings_constants import Constants as prim_c
from omni.kit.manipulator.prim.core.tool_models import LocalGlobalModeModel
from omni.kit.manipulator.prim.core.toolbar_registry import get_toolbar_registry
from omni.kit.manipulator.tool.snap.toolbutton import SnapToolButton
from omni.kit.manipulator.transform.manipulator import TransformManipulator
from omni.kit.manipulator.transform.toolbar_tool import SimpleToolButton
from omni.kit.manipulator.transform.types import Operation
from pathlib import Path
import traceback as traceback
import typing
__all__: list = ['SelectionPivotTool', 'LocalGlobalTool', 'PrimManipTools']
class LocalGlobalTool(omni.kit.manipulator.transform.toolbar_tool.SimpleToolButton):
    """
    A toolbar button class for toggling between local and global transform spaces.
    
        This class is responsible for creating a toggle button in the UI that allows users to switch between local and global transform modes while performing translate or rotate operations. The button updates its appearance based on the current mode and provides tooltips to indicate the active transform space.
    
        Args:
            args: Variable length argument list.
    
        Keyword Args:
            operation (Operation): The type of operation (translate or rotate) the tool is used for.
            toolbar_payload (dict, optional): A dictionary containing additional parameters for toolbar customization.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @classmethod
    def can_build(cls, manipulator: omni.kit.manipulator.transform.manipulator.TransformManipulator, operation: omni.kit.manipulator.transform.types.Operation) -> bool:
        """
        Determines if the tool can be built with the given manipulator and operation.
        
                Args:
                    manipulator (:obj:`TransformManipulator`): The manipulator that will use the tool.
                    operation (:obj:`Operation`): The operation for which the tool is being considered.
        
                Returns:
                    bool: True if the tool can be built, False otherwise.
        """
    def __init__(self, *args, **kwargs):
        """
        Initializes the LocalGlobalTool.
        """
    def destroy(self):
        """
        Cleans up the resources held by the tool. This should be called before deleting the tool.
        """
class PrimManipTools:
    """
    A class responsible for managing the registration and lifecycle of primitive manipulation tools.
    
        The PrimManipTools class is responsible for handling the registration, enabling, disabling, and destruction of various primitive manipulation tools within an application. It includes tools such as LocalGlobalTool for toggling between local and global transform spaces, SnapToolButton for enabling snapping functionality, and SelectionPivotTool for defining selection pivot placement. This class also manages settings subscriptions for tool state changes and properly cleans up during destruction.
        
    """
    def __del__(self):
        ...
    def __init__(self):
        """
        Initialize the PrimManipTools with default settings and register the necessary tools.
        """
    def _on_setting_changed(self, item, event_type):
        ...
    def _register_main_toolbar_button(self):
        ...
    def _register_tools(self):
        ...
    def _unregister_main_toolbar_button(self):
        ...
    def _unregister_tools(self):
        ...
    def destroy(self):
        """
        Cleans up the resources and unregisters tools upon destruction of the PrimManipTools instance.
        """
class SelectionPivotTool(omni.kit.manipulator.transform.toolbar_tool.SimpleToolButton):
    """
    A class for a toolbar button that provides selection pivot placement functionality.
    
        This class extends SimpleToolButton and acts as a button in the user interface which, when clicked, allows users to change the pivot placement of selected primitives in the scene. It also listens to selection changes to update its visibility state and registers its menu entries upon initialization.
    
        Args:
            args: A variable-length argument list.
    
        Keyword Args:
            usd_context_name (str): The name of the USD context to be used. Defaults to an empty string if not provided.
    
        Note:
            This class assumes the context is "" for VP1 and manages its own menu items for pivot placement settings.
    """
    _SelectionPivotTool__menu_entries: typing.ClassVar[list]  # value = [<omni.kit.widget.context_menu.custom_menu_dict.add_menu.<locals>.MenuSubscription object at 0x709eea35b6a0>, <omni.kit.widget.context_menu.custom_menu_dict.add_menu.<locals>.MenuSubscription object at 0x709eea35b790>, <omni.kit.widget.context_menu.custom_menu_dict.add_menu.<locals>.MenuSubscription object at 0x709eea35b880>, <omni.kit.widget.context_menu.custom_menu_dict.add_menu.<locals>.MenuSubscription object at 0x709eea35b970>, <omni.kit.widget.context_menu.custom_menu_dict.add_menu.<locals>.MenuSubscription object at 0x709eea35ba60>]
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @classmethod
    def can_build(cls, manipulator: omni.kit.manipulator.transform.manipulator.TransformManipulator, operation: omni.kit.manipulator.transform.types.Operation) -> bool:
        """
        Determines if the pivot tool can be built for the given manipulator and operation.
        
                Args:
                    cls (type): The class object representing the SelectionPivotTool.
                    manipulator (:obj:`TransformManipulator`): The manipulator for which the tool is being considered.
                    operation (:obj:`Operation`): The operation type to check compatibility.
        
                Returns:
                    bool: True if the tool can be built, False otherwise.
                
        """
    @classmethod
    def register_menu(cls):
        """
        Registers the pivot tool's menu in the application.
        
                Args:
                    cls (type): The class object representing the SelectionPivotTool.
                
        """
    @classmethod
    def unregister_menu(cls):
        """
        Unregisters the pivot tool's menu from the application.
        
                Args:
                    cls (type): The class object representing the SelectionPivotTool.
                
        """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the SelectionPivotTool.
        """
    def _on_selection_changed(self):
        ...
    def _on_stage_selection_event(self, event: carb.events._events.IEvent):
        ...
    def destroy(self):
        """
        Cleans up resources used by the tool, like event subscriptions.
        """
TOOLS_ENABLED_SETTING_PATH: str = '/exts/omni.kit.manipulator.prim.core/tools/enabled'
