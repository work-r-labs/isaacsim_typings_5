"""
This module provides a widget for displaying and editing USD Shade materials within the NVIDIA Omniverse Kit framework.
"""
from __future__ import annotations
import asyncio as asyncio
import omni.kit.property.material.scripts.widgets.usdshade.base_widget
from omni.kit.property.material.scripts.widgets.usdshade.base_widget import UsdShadeBaseWidget
from omni.kit.property.material.scripts.widgets.usdshade.utils import create_nonpersistant_attribute
from omni.kit.property.material.scripts.widgets.usdshade.utils import get_display_group_for_render_context
import omni.kit.property.usd.prim_selection_payload
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
import omni.kit.property.usd.usd_property_widget
from omni.kit.property.usd.usd_property_widget import UiDisplayGroup
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
from omni import ui
from pxr import Sdf
import pxr.Sdf
import pxr.Usd
from pxr import Usd
from pxr import UsdShade
import typing
__all__: list = ['UsdShadeMaterialWidget']
class UsdShadeMaterialWidget(omni.kit.property.material.scripts.widgets.usdshade.base_widget.UsdShadeBaseWidget):
    """
    A widget for displaying and editing USD Shade materials.
    
        This widget extends the UsdShadeBaseWidget to provide a user interface for interacting with materials defined in USD (Universal Scene Description) files. It allows users to view and modify material properties, including shader parameters and render contexts. The widget dynamically updates to reflect changes in the underlying USD file and provides a way to visualize different shader effects.
    
        The widget is designed to work within the NVIDIA Omniverse Kit framework and interacts with various USD and Omniverse Kit APIs to manage material properties. It subscribes to changes in application settings to reflect updates in the UI and supports async operations for handling material attributes.
    
        Args:
            title (str): The title of the widget, defaulting to 'Material and Shader'.
    """
    DISPLAY_BASE_SHADER_SETTINGS_PATH: typing.ClassVar[str] = '/persistent/app/properties/material/displayBaseShader'
    RENDER_CONTEXTS_SETTING_PATH: typing.ClassVar[str] = '/persistent/app/hydra/material/renderContexts'
    @staticmethod
    def _create_paused_attribute(material_paths: typing.List[str]) -> None:
        """
        
                Create the 'paused' attribute which is used by the Material Graph editor.
                If it's value is set to True, the material code in the Hydra render delegate will skip processing this material.
                
        """
    def __init__(self, title: str = 'Material and Shader'):
        """
        Initializes the UsdShadeMaterialWidget with optional title.
        """
    def _activate_frame(self, frame_id: int) -> None:
        """
        
                Callback trigged when a render context button is pressed, the corresponing frame containing the shader parameters for that conext will be displayed.
                
        """
    def _build_nested_group_frame(self, stage, prim_paths: list, display_group: omni.kit.property.usd.usd_property_widget.UiDisplayGroup, level: int, prefix: str):
        ...
    def _build_shader_frame(self, stage, prim_paths: list, display_group: omni.kit.property.usd.usd_property_widget.UiDisplayGroup, level: int, prefix: str):
        """
        
                Create the "Shader" frame.
                Emulate a traditional tabbed widet by adding buttons to allow the user to select one of the multiple render contexts to be displayed.
                
        """
    def _customize_props_layout(self, props: typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]) -> typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]:
        """
        
                For those input properties that exist on the base/terminal/root shader prims but are displayed in the Material widget
                    set the prim_paths attribute to the path of the underlying UsdShade.Shader prims.
                This way the UI reflects the values and/or connections on those prims.
                
        """
    def _display_base_shader_changed(self, *args, **kwargs) -> None:
        """
        
                Set the title of the widget depending upon if the user wants the terminal shader parameters displayed.
                
        """
    def _get_builder_args(self) -> dict:
        ...
    def _get_shader_prim_paths(self, prim: pxr.Usd.Prim) -> None:
        """
        
                Set the list of terminal shader nodes connected to this material.
                
        """
    def _path_requires_rebuild(self, path: pxr.Sdf.Path) -> bool:
        """
        
                If a property on the underlying shader this prim represents changes then trigger a rebuild.
                
        """
    def _render_context_changed(self, *args, **kwargs) -> None:
        """
        
                Callback executed when the user selects a render context other than the one that is currently being displayed by the widget.
                
        """
    def _sort_properties_for_ui(self, props: typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]) -> typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]:
        """
        
                Sort the output ports so that the universal output ports appear first (sorted alphabetically),
                followed by the ports for the other contexts (MDL, Material-X)
                
        """
    def clean(self) -> None:
        """
        Clean up function to be called before destroying the object.
        """
    def on_new_payload(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload) -> bool:
        """
        Handles a new payload for the widget.
        
                Args:
                    payload (:obj:`PrimSelectionPayload`): The new payload to be handled by the widget.
        
                Returns:
                    bool: True if the prims contained within the payload can be represented by this widget.
        """
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
