from __future__ import annotations
import carb as carb
import contextlib as contextlib
import copy as copy
import omni as omni
from omni.kit.property.adapter import core as ac
from omni.kit.property.adapter.core.scripts.core_adapter import AttributeAdapter
from omni.kit.property.adapter.core.scripts.core_adapter import StageAdapter
from omni.kit.property.usd.control_state_manager import ControlStateManager
from omni.kit.property.usd.placeholder_attribute import PlaceholderAttribute
from omni.kit.usd.layers._impl.event import LayerEventType
from omni.kit.usd.layers._impl.extension import get_layers
from omni.kit.usd.layers._impl.interface_utils import get_layer_event_payload
from pxr import Ar
from pxr import Gf
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
import pxr.Usd
__all__: list = ['UsdBase']
class UsdBase:
    """
    A base class for USD attributes and properties management.
    
        This class provides functionality to handle USD stage interactions, listen to changes,
        manage control states, and perform value manipulation for USD attributes. It is designed to
        be a common base class for USD model implementations, offering a rich set of features for
        USD data handling.
    
        Args:
            stage (:obj:`Usd.Stage`): The USD stage to interact with.
            object_paths (List[Sdf.Path]): A list of Sdf.Path objects representing the USD attributes or properties.
            self_refresh (bool): If True, the model will listen for USD changes itself; otherwise, it will rely on external update triggers.
            metadata (Optional[dict]): Additional metadata associated with the USD attributes or properties. Defaults to None.
            change_on_edit_end (bool): If True, changes to the USD are only committed when the edit ends (e.g., focus lost), improving performance during rapid edits. Defaults to True.
            treat_array_entry_as_comp (bool): Treats each entry in an array as a separate component, which is useful for building UI widgets that indicate non-default or ambiguous states at the entry level.
    
        Keyword Args:
            auto_target_session_layer_def (bool): Targets session layer definition for edits by default.
            min: The minimum allowed value for the attribute; this acts as a lower bound.
            max: The maximum allowed value for the attribute; this acts as an upper bound.
    """
    @staticmethod
    def _on_usd_changed(*args, **kwargs):
        ...
    @staticmethod
    def update_value_by_comp(from_value, to_value, comp: int):
        """
        Updates the value of a specific component.
        
                Args:
                    from_value (Any): The value to update from.
                    to_value (Any): The value to update to.
                    comp (int): The component index to update.
        """
    def __init__(self, stage: pxr.Usd.Stage, object_paths: typing.List[pxr.Sdf.Path], self_refresh: bool, metadata: dict = None, change_on_edit_end: bool = True, treat_array_entry_as_comp: bool = False, **kwargs):
        """
        Initializes the UsdBase instance.
        """
    def _change_property(self, path: pxr.Sdf.Path, new_value: typing.Any, old_value: typing.Any):
        """
        To maintain backward compatibility, _change_property function is kept and forwards the call to _change_property_2
        """
    def _change_property_2(self, path, new_value: typing.Any, *args, old_value: typing.Any = None, undoable: bool = True, **kwargs):
        ...
    def _compare_value_by_comp(self, val1, val2, comp: int):
        ...
    def _create_placeholder_attributes(self, attributes):
        ...
    def _get_attributes(self):
        ...
    def _get_comp_num(self):
        ...
    def _get_connected_attr(self, obj, connected_path) -> (pxr.Usd.Prim, pxr.Usd.Attribute):
        ...
    def _get_default_value(self, prop, metadata = None):
        ...
    def _get_edit_target(self, path: pxr.Sdf.Path) -> pxr.Usd.EditTarget:
        """
        Override this function to customize the target layer.
        """
    def _get_obj_type_default_value(self, obj):
        ...
    def _get_objects(self):
        ...
    def _get_type_name(self, obj = None):
        ...
    def _get_usd_context(self):
        ...
    def _get_value_by_comp(self, value, comp: int):
        ...
    def _is_array_type(self, obj = None):
        ...
    def _is_prev_same(self):
        ...
    def _on_adapter_changed(self, evt):
        ...
    def _on_dirty(self):
        ...
    def _on_spec_locks_changed(self, event: carb.events._events.IEvent):
        ...
    def _on_timeline_event(self, e):
        ...
    def _post_notification(self, message):
        ...
    def _read_value(self, obj, time_code):
        ...
    def _save_real_values_as_prev(self):
        ...
    def _set_dirty(self):
        ...
    def _update_stage_adapters(self):
        ...
    def _update_value(self, force = False):
        ...
    def _update_value_by_comp(self, value, comp: int):
        """
        update value from self._value
        """
    def _update_value_objects(self, force: bool, update_attribute: bool):
        ...
    def begin_edit(self):
        """
        Begins an edit operation by increasing the internal editing counter.
        """
    def clean(self):
        """
        Cleans up the instance by removing listeners and resetting state.
        """
    def create_placeholder_attribute(self, name, prim = None, metadata = None):
        """
        Creates a placeholder attribute.
        
                Args:
                    name (str): The name of the placeholder attribute to create.
                    prim (Optional[:obj:`Usd.Prim`]): The USD primitive associated with the attribute.
                    metadata (dict): The metadata to associate with the placeholder attribute.
        """
    def end_edit(self):
        """
        Ends an edit operation by decreasing the internal editing counter and updating the value if changed.
        """
    def get_all_comp_ambiguous(self) -> typing.List[bool]:
        """
        Retrieves a list indicating which components of the attribute's value are ambiguous.
        
                Returns:
                    List[bool]: A list with each element indicating ambiguity of the corresponding component.
        """
    def get_attribute_paths(self) -> typing.List[pxr.Sdf.Path]:
        """
        Retrieves the attribute paths associated with this instance.
        
                Returns:
                    List[Sdf.Path]: The list of attribute paths.
        """
    def get_attributes(self):
        ...
    def get_bad_connection(self) -> tuple[bool, str]:
        ...
    def get_connections(self):
        """
        Returns the list of connections for the last attribute in the model.
        
                Returns:
                    list: The list of connections.
        """
    def get_current_time_code(self):
        """
        Gets the current time code of the stage.
        
                Returns:
                    :obj:`Usd.TimeCode`: The current time code.
        """
    def get_layers_with_strongest_value_opinions(self) -> list[pxr.Sdf.Layer]:
        """
        Gets a list of strongest layers that contribute to the value of each attributes in the model.
        
                Returns:
                    list[Sdf.Layer]: The list of layers contributed to each attribute.
                
        """
    def get_objects(self):
        ...
    def get_prim_paths(self, stage) -> typing.List[pxr.Sdf.Path]:
        """
        Returns the list of Sdf.Paths for the prims associated with this USD model.
        
                Args:
                    stage (:obj:`Usd.Stage`): The stage to query for prim paths.
        
                Returns:
                    List[:obj:`Sdf.Path`]: The list of prim paths.
        """
    def get_property_paths(self) -> typing.List[pxr.Sdf.Path]:
        """
        Retrieves the property paths associated with this instance.
        
                Returns:
                    List[Sdf.Path]: The list of property paths.
        """
    def get_stage(self):
        ...
    def get_valid_stage_adapter_read(self, path):
        """
        Gets the stage adapter that can read the given path.
        
                Args:
                    path (str): The path to check for a valid stage adapter.
        
                Returns:
                    :obj:`Usd.Stage`: The stage that can read from the given path.
        """
    def get_valid_stage_adapter_write(self, path):
        """
        Gets the stage adapter that can write to the given path.
        
                Args:
                    path (str): The path to check for a valid stage adapter.
        
                Returns:
                    :obj:`Usd.Stage`: The stage that can write to the given path.
        """
    def get_value(self):
        """
        Gets the value of the attribute.
        
                Returns:
                    Any: The current value of the attribute.
        """
    def get_value_by_comp(self, comp: int):
        """
        Gets the value of a specific component of the attribute value.
        
                Args:
                    comp (int): The component index to get the value for.
        
                Returns:
                    Any: The value of the specified component.
        """
    def has_connections(self):
        """
        Checks if the last attribute in the model has connections.
        
                Returns:
                    bool: True if there are connections, False otherwise.
        """
    def is_ambiguous(self) -> bool:
        """
        Determines if the attribute's value is ambiguous due to multiple sources.
        
                Returns:
                    bool: True if ambiguous, False otherwise.
        """
    def is_array_type(self) -> bool:
        """
        Determines if the attribute's value is of an array type.
        
                Returns:
                    bool: True if an array type, False otherwise.
        """
    def is_comp_ambiguous(self, index: int) -> bool:
        """
        Determines if a specific component of the attribute's value is ambiguous.
        
                Args:
                    index (int): The index of the component to check.
        
                Returns:
                    bool: True if the specified component is ambiguous, False otherwise.
        """
    def is_different_from_default(self) -> bool:
        """
        Determines if the current value is different from the default value.
        
                Returns:
                    bool: True if different, False otherwise.
        """
    def is_editing(self) -> bool:
        """
        Checks if the model is currently in an editing state.
        
                Returns:
                    bool: True if editing, False otherwise.
        """
    def is_instance_proxy(self):
        """
        Checks if the object is an instance proxy.
        
                Returns:
                    bool: True if the object is an instance proxy, False otherwise.
        """
    def is_locked(self):
        """
        Checks if the attributes are locked.
        
                Returns:
                    bool: True if attributes are locked, False otherwise.
        """
    def is_readonly(self) -> bool:
        """
        Determines if the attribute is read-only.
        
                Returns:
                    bool: True if read-only, False otherwise.
        """
    def is_value_array(self):
        """
        Checks if the attribute value is an array.
        
                Returns:
                    bool: True if the attribute value is an array, False otherwise.
        """
    def might_be_time_varying(self) -> bool:
        """
        Determines if the associated attribute might vary over time.
        
                Returns:
                    bool: True if it might vary, False otherwise.
        """
    def set_default(self, comp = -1):
        """
        Set the UsdAttribute default value if it exists in metadata.
        
                Args:
                    comp (int): The component index to set default for. -1 means all components.
        """
    def set_locked(self, locked):
        """
        Sets the locked state of the attributes.
        
                Args:
                    locked (bool): Whether to lock or unlock the attributes.
        """
    def set_on_control_state_changed_fn(self, fn):
        """
        Sets a callback function to be called when the control state changes.
        
                Args:
                    fn (function): The callback function to be set.
        """
    def set_on_set_default_fn(self, fn):
        """
        Sets a callback function to be called when the default value is set.
        
                Args:
                    fn (function): The callback function to be set.
        """
    def set_soft_range_userdata(self, soft_range_min, soft_range_max):
        """
        Sets the soft range for the attributes.
        
                Args:
                    soft_range_min (float): The minimum value of the soft range.
                    soft_range_max (float): The maximum value of the soft range.
        """
    def set_value(self, value, comp: int = -1) -> bool:
        """
        Sets the value of the attribute. Can set value for a specific component.
        
                Args:
                    value (Any): The new value to set.
                    comp (int): The component index to set the value for.
        """
    def update_control_state(self):
        """
        Updates the control state based on the current conditions.
        """
    @property
    def control_state(self):
        """
        Gets the current control state, it's the icon on the right side of the line with widgets.
        """
    @property
    def metadata(self):
        """
        Gets the metadata associated with this instance.
        """
    @property
    def stage(self):
        """
        Gets the USD stage associated with this instance.
        """
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
