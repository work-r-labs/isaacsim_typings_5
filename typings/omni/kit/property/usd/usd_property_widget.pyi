from __future__ import annotations
import carb as carb
from collections import defaultdict
import contextlib as contextlib
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.property.adapter import core as ac
from omni.kit.property.usd.usd_model_base import UsdBase
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
from omni.kit.property.usd.usd_property_widget_builder import get_ui_style
from omni.kit.window.property.templates.simple_property_widget import SimplePropertyWidget
from omni import ui
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
import pxr.Usd
from pxr import UsdUtils
import traceback as traceback
import typing
__all__: list = ['UsdPropertyUiEntry', 'UiDisplayGroup', 'UsdPropertiesWidget', 'SchemaPropertiesWidget', 'MultiSchemaPropertiesWidget', 'RawUsdPropertiesWidget']
class MultiSchemaPropertiesWidget(UsdPropertiesWidget):
    """
    
        MultiSchemaPropertiesWidget filters properties and only show the onces from a given IsA schema or schema subclass list.
        
    """
    _MultiSchemaPropertiesWidget__known_api_schemas: typing.ClassVar[set] = set()
    def __del__(self):
        ...
    def __init__(self, title: str, schema, schema_subclasses: list, include_list: list = None, exclude_list: list = None, api_schemas: typing.Sequence[str] = None, group_api_schemas: bool = False):
        """
        
                Constructor.
        
                Args:
                    title (str): Title of the widgets on the Collapsable Frame.
                    schema: The USD IsA schema or applied API schema to filter properties.
                    schema_subclasses (list): list of subclasses
                    include_list (list): list of additional schema named to add
                    exclude_list (list): list of additional schema named to remove
                    api_schemas (sequence): a sequence of AppliedAPI schema names that this widget handles
                    group_api_schemas (bool): whether to create default groupings for any AppliedSchemas on the Usd.Prim
                
        """
    def _customize_props_layout(self, props):
        ...
    def _filter_props_to_build(self, props):
        """
        
                See UsdPropertiesWidget._filter_props_to_build
                
        """
    def clean(self):
        """
        
                See PropertyWidget.clean
                
        """
    def on_new_payload(self, payload):
        """
        
                See PropertyWidget.on_new_payload
                
        """
class RawUsdPropertiesWidget(UsdPropertiesWidget):
    MULTI_SELECTION_LIMIT_DO_NOT_ASK_SETTING_PATH: typing.ClassVar[str] = '/exts/omni.kit.property.usd/multi_selection_limit_do_not_ask'
    MULTI_SELECTION_LIMIT_SETTING_PATH: typing.ClassVar[str] = '/persistent/exts/omni.kit.property.usd/raw_widget_multi_selection_limit'
    def __init__(self, title: str, collapsed: bool, multi_edit: bool = True, enable_adapter: bool = False):
        ...
    def _multi_selection_protected(self):
        ...
    def _no_multi_selection_protection_this_session(self):
        ...
    def _on_collapsed_changed(self, collapsed):
        ...
    def build_impl(self):
        ...
    def build_items(self):
        ...
    def on_new_payload(self, payload):
        ...
class SchemaPropertiesWidget(UsdPropertiesWidget):
    """
    
        SchemaPropertiesWidget only filters properties and only show the onces from a given IsA schema or applied API schema.
        
    """
    def __init__(self, title: str, schema, include_inherited: bool):
        """
        
                Constructor.
        
                Args:
                    title (str): Title of the widgets on the Collapsible Frame.
                    schema: The USD IsA schema or applied API schema to filter properties.
                    include_inherited (bool): Whether the filter should include inherited properties.
                
        """
    def _filter_props_to_build(self, props):
        """
        
                See UsdPropertiesWidget._filter_props_to_build
                
        """
    def on_new_payload(self, payload):
        """
        
                See PropertyWidget.on_new_payload
                
        """
class UiDisplayGroup:
    def __init__(self, name: str, ordered: bool, props: typing.Optional[typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]] = None):
        ...
    def __repr__(self):
        ...
    def add_prop(self, prop: UsdPropertyUiEntry, nested_groups: typing.List[str]) -> None:
        ...
    def get_children(self) -> typing.List[typing.Union[typing.Type[ForwardRef('UiDisplayGroup')], omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]]:
        ...
    def get_sub_props(self) -> typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]:
        ...
class UsdPropertiesWidget(omni.kit.window.property.templates.simple_property_widget.SimplePropertyWidget):
    """
    
        UsdPropertiesWidget provides functionalities to automatically populates UsdProperties on given prim(s). The UI will
        and models be generated according to UsdProperties's value type. Multi-prim editing works for shared Properties
        between all selected prims if instantiated with multi_edit = True.
        
    """
    @staticmethod
    def _on_usd_changed(*args, **kwargs):
        ...
    def __init__(self, title: str, collapsed: bool, multi_edit: bool = True, enable_adapter: bool = False, maintain_property_order: bool = False):
        """
        
                Constructor.
        
                Args:
                    title (str): title of the widget.
                    collapsed (bool): whether the collapsable frame should be collapsed for this widget.
                    multi_edit (bool): whether multi-editing is supported.
                    enable_adapter (bool): use stage_adapters
                    maintain_property_order (bool): _customize_props_layout returns a list of properties to display on the widget.
                
        """
    def _build_extra_properties(self, stage, prim_paths: list, display_group: UiDisplayGroup, prefix: str, sub_props: typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]):
        ...
    def _build_framestack(self, prefix, display_group):
        ...
    def _build_group_additional_header_context_menu(self, group_name: str, group_id: str, props: typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry] = None):
        """
        
                Override this function to build the additional context menu to Kit's built-in ones when right click on a Collapsable group header
        
                Args:
                    group_name: Display name of the group. If it's not a subgroup, it's the title of the widget.
                    group_id: A unique identifier for group context menu.
                    props: Properties under this group. It contains all properties in its subgroups as well.
                
        """
    def _build_group_builtin_header_context_menu(self, group_name: str, group_id: str, props: typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry] = None):
        ...
    def _build_header_context_menu(self, group_name: str, group_id: str, props: typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry] = None):
        """
        
                Override this function to build the context menu when right click on a Collapsable group header
        
                Args:
                    group_name: Display name of the group. If it's not a subgroup, it's the title of the widget.
                    group_id: A unique identifier for group context menu.
                    props: Properties under this group. It contains all properties in its subgroups as well.
                
        """
    def _build_nested_group_frame(self, stage, prim_paths: list, display_group: UiDisplayGroup, level: int, prefix: str):
        ...
    def _build_nested_group_props(self, stage, prim_paths, props):
        ...
    def _create_property_entry(self, name: str, display_group: str, metadata: dict, prop_type) -> UsdPropertyUiEntry:
        """
        Override in a derived class if UsdPropertyUiEntry needs to be constructed differently or if
                a class derived from UsdPropertyUiEntry is required, which would be the case if one of the UsdPropertyUiEntry methods
                needs to be overridden.
                
        """
    def _customize_props_layout(self, props):
        """
        
                When deriving from UsdPropertiesWidget, override this function to reorder/regroup properties to build.
                To reorder the properties display order, reorder entries in props list.
                To override display group or name, call prop.override_display_group or prop.override_display_name respectively.
                If you want to hide/add certain property, remove/add them to the list.
        
                NOTE: All above changes won't go back to USD, they're pure UI overrides.
        
                Args:
                    props: List of Tuple(property_name, property_group, metadata)
        
                Example:
        
                    for prop in props:
                        # Change display group:
                        prop.override_display_group("New Display Group")
        
                        # Change display name (you can change other metadata, it won't be write back to USD, only affect UI):
                        prop.override_display_name("New Display Name")
        
                    # add additional "property" that doesn't exist.
                    props.append(UsdPropertyUiEntry("PlaceHolder", "Group", { Sdf.PrimSpec.TypeNameKey: "bool"}, Usd.Property))
                
        """
    def _delayed_dirty_handler(self):
        ...
    def _filter_props_to_build(self, props):
        """
        
                When deriving from UsdPropertiesWidget, override this function to filter properties to build.
                Args:
                    props: List of Usd.Property on a selected prim.
                
        """
    def _get_prim(self, prim_path):
        ...
    def _get_prim_properties(self, prim: pxr.Usd.Prim):
        """
        UsdPrim.GetProperties() returns a vector of UsdProperty's.
                This method can be overridden in a derived class if an alternate class is holding the data.
                If this is the case such a derived class would need to implement several of the methods in UsdProperty
                such as GetName(), GetAllMetadata(), etc in order to property integrate it with this widget.
                
        """
    def _get_shared_properties_from_selected_prims(self, anchor_prim):
        ...
    def _on_bus_event(self, event: carb.events._events.IEvent):
        ...
    def _register_header_context_menu_entry(self, menu: typing.Dict, group_id: str):
        """
        
                Registers a menu entry to Collapsable group header
        
                Args:
                    menu: The menu entry to be registered.
                    group_id: A unique identifier for group context menu.
        
                Return:
                    The subscription object of the menu entry to be kept alive during menu's life span.
                
        """
    def add_custom_schema_attribute(self, attribute_name, classify_fn, create_fn, display_group, value_dict):
        ...
    def add_custom_schema_attributes_to_props(self, props) -> None:
        ...
    def add_listener_adapters(self, attr_names):
        ...
    def build_items(self):
        """
        
                See SimplePropertyWidget.build_items
                
        """
    def build_nested_group_frames(self, stage, display_group: UiDisplayGroup):
        """
        
                Override this function to build group frames differently.
                
        """
    def build_property_item(self, stage, ui_prop: UsdPropertyUiEntry, prim_paths: typing.List[pxr.Sdf.Path]):
        """
        
                Override this function to customize property building.
                
        """
    def clean(self):
        """
        
                See PropertyWidget.clean
                
        """
    def get_additional_kwargs(self, ui_prop: UsdPropertyUiEntry):
        """
        
                Override this function if you want to supply additional arguments when building the label or ui widget.
                
        """
    def get_valid_stage_adapter(self, prim_path, attr_name):
        ...
    def is_custom_schema_attribute_used(self, prim) -> list:
        ...
    def on_new_payload(self, payload):
        ...
    def request_rebuild(self):
        ...
    def reset(self):
        """
        
                See PropertyWidget.reset
                
        """
    def reset_models(self):
        ...
class UsdPropertyUiEntry:
    __hash__: typing.ClassVar[None] = None
    attr_name = ...
    def __eq__(self, other):
        ...
    def __getitem__(self, key):
        ...
    def __init__(self, prop_name: str, display_group: str, metadata, property_type, build_fn = None, display_group_collapsed: bool = False, prim_paths: typing.List[pxr.Sdf.Path] = None):
        """
        
                Constructor.
        
                Args:
                    prop_name: name of the Usd Property. This is not the display name.
                    display_group: group of the Usd Property when displayed on UI.
                    metadata: metadata associated with the Usd Property.
                    property_type: type of the property. Either Usd.Property or Usd.Relationship.
                    build_fn: a custom build function to build the UI. If not None the default builder will not be used.
                    display_group_collapsed: if the display group should be collapsed. Group only collapses when ALL its contents request such.
                    prim_paths: to override what prim paths this property will be built upon. Leave it to None to use default (currently selected paths, or last selected path if multi-edit is off).
                
        """
    def __repr__(self):
        ...
    def _compare_metadata(self, meta1, meta2) -> bool:
        ...
    def add_custom_metadata(self, key: str, value):
        """
        
                If value is not None, add it to the custom data of the metadata using the specified key.  Otherwise, remove that
                key from the custom data.
        
                Args:
                    key: the key that should contain the custom metadata value
                    value: the value that should be added to the custom metadata if not None
                
        """
    def get_nested_display_groups(self):
        ...
    def override_display_group(self, display_group: str, collapsed: bool = False):
        """
        
                Overrides the display group of the property. It only affects UI and DOES NOT write back DisplayGroup metadata to USD.
        
                Args:
                    display_group: new display group to override to.
                    collapsed: if the display group should be collapsed. Group only collapses when ALL its contents request such.
                
        """
    def override_display_name(self, display_name: str):
        """
        
                Overrides the display name of the property. It only affects UI and DOES NOT write back DisplayName metadata to USD.
        
                Args:
                    display_group: new display group to override to.
                
        """
    def override_doc_string(self, doc_string: str):
        """
        
                Overrides the doc string of the property, which is used for tooltips. It only affects UI and DOES NOT write
                back Documentation metadata to USD.
        
                Args:
                    doc_string: new doc string
                
        """
def create_primspec_asset(default_asset_path = ''):
    ...
def create_primspec_bool(default_bool = False):
    ...
def create_primspec_float(default_float = 0.0):
    ...
def create_primspec_int(default_int = 0):
    ...
def create_primspec_string(default_str = ''):
    ...
def create_primspec_token(tokens, default_token):
    ...
def get_group_properties_clipboard():
    ...
def set_group_properties_clipboard(properties_to_copy: typing.Dict[pxr.Sdf.Path, typing.Any]):
    ...
ADDITIONAL_CHANGED_PATH_EVENT_TYPE: int = 17954634024720962805
ENABLE_ADAPTER_SETTINGS: str = '/ext/omni.kit.property.usd/enableAdapter'
__properties_to_copy: dict = {}
