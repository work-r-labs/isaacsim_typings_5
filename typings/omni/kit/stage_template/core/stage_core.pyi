"""
This module provides core functionality for registering and unregistering new stage templates, handling stage creation with templates and setting transformations for USD primitives.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
from inspect import signature
import omni as omni
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
__all__: list = ['CoreStageExtension', 'register_template', 'unregister_template', 'get_stage_template_list', 'get_stage_template', 'get_default_template', 'new_stage', 'new_stage_with_callback', 'new_stage_async']
class CoreStageExtension(omni.ext._extensions.IExt):
    """
    This class provides core functionality for registering and unregistering new stage templates, handling stage creation with templates and setting transformations for USD primitives.
    """
    def on_shutdown(self):
        """
        Called when the extension is shutting down.
        """
    def on_startup(self, ext_id):
        """
        Called when the extension starts up.
        
                Args:
                    ext_id (str): The unique identifier for the extension.
                
        """
def __new_stage_finalize(create_result, error_message, usd_context, template = None, on_new_stage_fn = None):
    """
    Finalizes the creation of a new USD stage after the stage is created.
    
        Args:
            create_result (bool): Result of the stage creation, True if successful.
            error_message (str): Message describing the error if stage creation failed.
            usd_context (:obj:`omni.usd.UsdContext`): Context of the USD stage that is being finalized.
            template (Optional[str]): Name of the template to use for initializing the stage. Uses default if None.
            on_new_stage_fn (Optional[callable]): Callback function to be called after stage finalization.
        
    """
def get_action_name(name):
    """
    Converts a name to a valid action identifier.
    
        This function takes a given name string and converts it to a lowercase string
        that can be used as an action identifier. It replaces hyphens and spaces with underscores.
    
        Args:
            name (str): The name to convert into an action identifier.
    
        Returns:
            str: A valid action identifier derived from the input name.
    """
def get_default_template():
    """
    Get name of default new_stage template. Used when new_stage is called without template name specified
    
        Returns:
            str: The name of the default new_stage template.
    """
def get_stage_template(name):
    """
    Get named new_stage template & create function pointer
    
        Args:
            param1 (str): template name
    
        Returns:
            tuple: new_stage template name & create function pointer
        
    """
def get_stage_template_list():
    """
    Returns a list of loaded new_stage templates.
    
        Returns:
            list or None: A list of groups, each containing new_stage template names and their corresponding creation function pointers, or None if no templates are loaded.
        
    """
def new_stage(on_new_stage_fn = None, template = 'empty', usd_context = None):
    """
    Execute new_stage
    
        Args:
            on_new_stage_fn (Optional[callable]): Callback function to be called when new stage is created.
            template (str): Template name. If not specified, the default template is used.
            usd_context (Optional[:obj:`omni.usd.UsdContext`]): The UsdContext to create a new stage in. If not provided, the current context is used.
        
    """
def new_stage_async(template = 'empty', usd_context = None):
    """
    Execute new_stage asynchronously
    
        This function initializes the creation of a new USD stage asynchronously based on the specified template name. The operation is performed in the context of the given UsdContext. If no UsdContext is provided, the default context is used. The function is a coroutine and should be awaited to ensure the stage creation process is completed.
    
        Args:
            template (str): The name of the template to use for creating the new stage. If not specified, the default 'empty' template is used.
            usd_context (Optional[:obj:`omni.usd.UsdContext`]): The UsdContext in which the new stage will be created. If not provided, the default UsdContext is used.
    
        Returns:
            Tuple[bool, str]: A tuple containing a boolean indicating the success status of the stage creation and an error message, if any occurred.
        
    """
def new_stage_with_callback(on_new_stage_fn = None, template = 'empty', usd_context = None):
    """
    Creates a new USD stage using the specified template and context, then applies post-creation operations via a callback.
    
        Args:
            on_new_stage_fn (Optional[callable]): A callback function to be called after the new stage is created. It should accept two arguments: a boolean indicating the success of the stage creation, and an error message if the creation failed.
            template (str): The name of the template to use for creating the new stage. If not specified, 'empty' is used as the default.
            usd_context (Optional[:obj:`omni.usd.UsdContext`]): The USD context within which the new stage is to be created. If not provided, the default USD context is used.
    
        Returns:
            None
    """
def register_template(name, new_stage_fn, group = 0):
    """
    Registers a new stage template and associates it with an action.
    
        Args:
            name (str): The unique name of the template to register.
            new_stage_fn (callable): The function to create a new stage when this template is used.
            group (int): An identifier to group templates, used by the menu to split into groups with separators.
    
        Returns:
            bool: True if the template was successfully registered, False if the template already exists.
    """
def unregister_template(name):
    """
    Unregisters a previously registered new_stage template.
    
        Args:
            name (str): The name of the template to unregister.
    
        Returns:
            None
        
    """
_clear_dirty_task = None
_template_list: list = [{'empty': ('empty', omni.kit.stage_templates.new_stage.NewStageExtension.new_stage_empty), 'sunlight': ('sunlight', omni.kit.stage_templates.templates.sunlight.SunlightStage.new_stage), 'default stage': ('default stage', omni.kit.stage_templates.templates.default_stage.DefaultStage.new_stage)}]
