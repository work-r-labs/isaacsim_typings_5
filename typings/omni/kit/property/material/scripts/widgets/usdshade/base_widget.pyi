"""
This module defines a base widget for interacting with USD Shade elements within the omni.kit.property.material extension.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import copy as copy
import omni as omni
from omni.kit.property.material.scripts.widgets.usdshade.models.builder import get_custom_ui_prop_build_fn
from omni.kit.property.material.scripts.widgets.usdshade.placeholder import GetPlaceholderPropertiesForPrim
from omni.kit.property.material.scripts.widgets.usdshade.placeholder.placeholder import UsdShadePropertyPlaceholder
from omni.kit.property.material.scripts.widgets.usdshade.usdshade_property_ui_entry import UsdShadePropertyUiEntry
from omni.kit.property.material.scripts.widgets.usdshade.utils import get_shader_info
from omni.kit.property.material.scripts.widgets.usdshade.utils import remove_properties_and_connections
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from omni.kit.property.usd.usd_property_widget import UsdPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from omni.kit.property.usd.usd_property_widget import create_primspec_bool
import pxr.Sdf
from pxr import Sdf
from pxr import Sdr
from pxr import Tf
from pxr import Usd
import pxr.Usd
from pxr import UsdShade
import typing
__all__: list = ['UsdShadeBaseWidget']
class UsdShadeBaseWidget(omni.kit.property.usd.usd_property_widget.UsdPropertiesWidget):
    """
    A base class for creating widgets for USD Shade elements.
    
        This class provides a foundation for deriving custom widgets that interact with USD Shading prims, such as shaders and materials. It handles common functionalities like managing USD schema objects, setting up white mode exceptions, and responding to MDL module loads. It also facilitates the customization of the widget's UI, including property ordering and group collapsing.
    
        Args:
            schema (:obj:`Usd.SchemaBase`): The USD schema this widget targets.
            title (str): The top level group name in the UI.
            schema_ignore (Optional[List[:obj:`Usd.SchemaBase`]]): Optional list of USD schema types ignored by this widget.
        
    """
    MATERIAL_ADAPTER_SETTING_PATH: typing.ClassVar[str] = '/ext/omni.kit.property.material/enableAdapter'
    MATERIAL_WHITE_MODE_EXCEPTION_INPUT: typing.ClassVar[str] = 'inputs:excludeFromWhiteMode'
    MATERIAL_WHITE_MODE_EXCEPTION_LIST_SETTING_PATH: typing.ClassVar[str] = '/persistent/app/rendering/whiteModeExceptions'
    PRINT_LAYOUT: typing.ClassVar[bool] = False
    PRINT_LAYOUT_METADATA: typing.ClassVar[bool] = False
    UI_ORDER: typing.ClassVar[list] = ['Description', 'inputs', 'outputs', 'info', 'Material Flags', 'ui']
    def __init__(self, schema: pxr.Usd.SchemaBase, title: str, schema_ignore: typing.Optional[typing.List[pxr.Usd.SchemaBase]] = None):
        """
        Initializes the UsdShadeBaseWidget.
        
                This method initializes the widget with a USD schema and various settings.
        """
    def _cancel_pending_rebuild(self) -> None:
        ...
    def _create_property_entry(self, name: str, display_group: str, metadata: dict, prop_type) -> omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry:
        ...
    def _customize_props_layout(self, props: typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]) -> typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]:
        """
        
                This function does the following:
                    1. Sort the properties based on how we want them to appear in the UI.
                    2. Adds build functions for any custom widgets.
                    3. Set the collapsed state of UI groups.
                
        """
    def _filter_props_to_build(self, props: typing.List[omni.kit.property.material.scripts.widgets.usdshade.placeholder.placeholder.UsdShadePropertyPlaceholder]) -> typing.List[omni.kit.property.material.scripts.widgets.usdshade.placeholder.placeholder.UsdShadePropertyPlaceholder]:
        """
        
                If multiple prims are selected and they are not identical then we will only show the [inputs, ui] properties.
                
        """
    def _get_builder_args(self) -> dict:
        """
        
                Return a dictionary of args that can be passed to the UsdShadePropertyPlaceholder builders.
                
        """
    def _get_prim_properties(self, prim: pxr.Usd.Prim) -> typing.List[omni.kit.property.material.scripts.widgets.usdshade.placeholder.placeholder.UsdShadePropertyPlaceholder]:
        """
        
                Return the list of properties to be displayed in the UI for prim.
                Note: rather than return Usd.Property's we create UsdShadePropertyPlaceholder's.
                    see UsdShadePropertyPlaceholder comments for more information as to why these are used.
                
        """
    def _get_shader_source_asset(self, shader_prim_path: pxr.Sdf.Path) -> typing.Optional[pxr.Sdf.AssetPath]:
        """
        
                Return the source asset from the UsdShade.Shader at 'shader_prim_path' if it's source type is MDL
                
        """
    def _identical_selection(self) -> bool:
        """
        
                If multiple prims are selected in the UI, this function will return True/False based on whether or not we determine the prims to be identical,
                    which in turn drives which properties will be displayed in the UI.
                
        """
    def _load_mdl_modules(self) -> None:
        """
        
                Gather a list of the MDL modules needed by this widget that need to be loaded into the registry.
                Modules will be loaded async, when they all have been loaded a callback wll be triggered to rebuild the widget.
                
        """
    def _on_create_white_mode_exception_bool(self, attribute_name: str, value_dict: typing.Dict) -> omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry:
        ...
    def _on_mdl_module_load(self, notice, sender) -> None:
        """
        
                Callback triggered when an MDL module has been loaded.
                When the list of MDL modules we are waiting on to load reaches 0 we trigger a rebuild
                
        """
    def _on_mdl_module_reload(self, notice, sender) -> None:
        """
        
                Callback triggered when an MDL module has been reloaded.
                If the module is one used by the current set of shader prims request a rebuild.
                
        """
    def _on_usd_changed(self, notice: pxr.Usd.ObjectsChanged, stage: pxr.Usd.Stage) -> bool:
        """
        
                The USD properties have changed - most likely due to a user or script changing a property value.
                Check to see if the changed property affects this widget and if so trigger a complete rebuild of the widget if the change demands it.
                
        """
    def _on_white_mode_list_changed(self, *args, **kwargs) -> None:
        ...
    def _path_requires_rebuild(self, path: pxr.Sdf.Path) -> bool:
        """
        
                Called from _on_usd_changed, a return value of True indicates that changes to the attribute at this path require a rebuild of the widget.
                The path will be from one of the following:
                    1. Usd.Notice.ObjectsChanged.GetChangedInfoOnlyPaths()
                    2. Usd.Notice.ObjectsChanged.GetResyncedPaths()
                
        """
    def _setup_white_mode(self) -> None:
        ...
    def _sort_properties_for_ui(self, props: typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]) -> typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]:
        """
        
                Sort by the following:
                    1. annotation UI order - for inputs and outputs only
                    2. the UI_ORDER declared above.
                
        """
    def clean(self) -> None:
        """
        Cleans up resources and unsubscribes from events before the widget is destroyed.
        """
    def get_additional_kwargs(self, ui_prop: omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry) -> typing.Tuple[typing.Optional[dict], typing.Optional[dict]]:
        """
        Generates additional keyword arguments for the UI properties.
        
                Args:
                    ui_prop (:obj:`UsdPropertyUiEntry`): The UI property for which to generate the kwargs.
        """
    def on_new_payload(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload) -> bool:
        """
        Handles a new payload for the widget.
        
                Args:
                    payload (:obj:`PrimSelectionPayload`): The new payload to be handled by the widget.
        
                Returns:
                    bool: Whether the payload can be represented by this widget.
        """
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
