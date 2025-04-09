from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.usd.layers._impl.event import LayerEventType
from omni.kit.usd.layers._impl.interface_utils import get_layer_event_payload
from omni.kit.usd.layers._impl.layer_utils import LayerUtils
from omni.kit.usd.layers._omni_kit_usd_layers import ILayersInstance
from omni.kit.usd.layers._omni_kit_usd_layers import acquire_layers_state_interface
from omni.kit.usd.layers._omni_kit_usd_layers import release_layers_state_interface
from pxr import Sdf
from urllib.parse import unquote
__all__: list = ['LayersState', 'SETTINGS_AUTO_RELOAD_SUBLAYERS', 'SETTINGS_AUTO_RELOAD_NON_SUBLAYERS', 'SETTINGS_IGNORE_OUTDATE_NOTIFICATION']
class LayersState:
    def _LayersState__send_layer_event(self, layer_identifier, event_type: omni.kit.usd.layers._impl.event.LayerEventType):
        ...
    def __init__(self, layers_instance: omni.kit.usd.layers._omni_kit_usd_layers.ILayersInstance, usd_context) -> None:
        ...
    def _destroy(self):
        ...
    def _on_layer_event(self, event: carb.events._events.IEvent):
        ...
    def _on_stage_event(self, event):
        ...
    def _populate_all_identifiers(self, item: carb.dictionary._dictionary.Item, not_in_session = True, not_auto = False):
        ...
    def add_auto_reload_layer(self, layer_identifier: str):
        """
        Adds layer into auto-reload list. So if layer is outdated, it will be auto-reloaded.
        """
    def get_all_outdated_layer_identifiers(self, not_in_session = False, not_auto = False) -> typing.List[str]:
        """
        Gets all layer identifiers in the stage that are outdated currently while skipping any live-sessions
        """
    def get_auto_reload_layers(self) -> typing.List[str]:
        """
        Returns a list of layer identifiers that are configured as auto-reload when they are outdated.
        """
    def get_dirty_layer_identifiers(self, not_in_session = False) -> typing.List[str]:
        """
        Gets all layer identifiers that have pending edits that are not saved.
        """
    def get_layer_name(self, layer_identifier: str) -> str:
        ...
    def get_layer_owner(self, layer_identifier: str) -> str:
        """
        Gets file owner of layer file. It's empty if file system does not support it.
        """
    def get_local_layer_identifiers(self, include_session_layers = False, include_anonymous_layers = True, include_invalid_layers = False) -> typing.List[str]:
        """
        Gets layer identifiers in the local layer stack of the current stage.
        """
    def get_outdated_non_sublayer_identifiers(self, not_in_session = False, not_auto = False) -> typing.List[str]:
        """
        
                Ges all layer identifiers except ones in the local layer stack of the stage that are outdated currently.
                Those layers include ones that are inserted as references or payloads.
                
        """
    def get_outdated_sublayer_identifiers(self, not_in_session = False, not_auto = False) -> typing.List[str]:
        """
        Ges all sublayer identifiers in the local layer stack of the stage that are outdated currently.
        """
    def has_local_layer(self, layer_identifier) -> bool:
        """
        Layer is in the local layer stack of current stage.
        """
    def has_used_layer(self, layer_identifier) -> bool:
        """
        Layer is in the used layers of current stage.
        """
    def is_auto_reload_layer(self, layer_identifier: str) -> bool:
        """
        Whether layer will be auto-reloaded when it's outdated or not.
        """
    def is_layer_globally_muted(self, layer_identifier: str) -> bool:
        """
        
                Checks if layer is globally muted or not in this usd context.
                Global muteness is a customize concept in Kit that's not from USD. It's used for complement
                the USD muteness, that works for two purposes:
                1. It's stage bound. So a layer is globally muted in this stage will not influence others.
                2. It's persistent. Right now, it's saved inside the custom data of root layer.
        
                After stage load, it will be read to initialize the muteness of layers. Also, global muteness
                only takes effective when it's in global state mode. See omni.usd.UsdContext.set_layer_muteness_scope
                about how to switch muteness scope. When it's not in global state mode, authoring global
                muteness will not incluence layer's muteness in stage.
                
        """
    def is_layer_locally_muted(self, layer_identifier: str) -> bool:
        ...
    def is_layer_locked(self, layer_identifier: str) -> bool:
        ...
    def is_layer_outdated(self, layer_identifier: str) -> bool:
        """
        If layer is out of sync. This only works for layer inside Nucleus server but not local disk.
        """
    def is_layer_readonly_on_disk(self, layer_identifier: str) -> bool:
        """
        
                Checks if this layer is physically read-only on disk.
                
        """
    def is_layer_savable(self, layer_identifier: str) -> bool:
        """
        
                Checks if this layer is savable. If it's savable means it's true by checking is_layer_writable and not anonymous.
                
        """
    def is_layer_writable(self, layer_identifier: str) -> bool:
        """
        
                Checks if layer is writable. A layer is writable means it can be set as edit target, which should satisfy:
                1. It's not read-only on disk.
                2. It's not locked by set_layer_lock_state.
                3. It's not muted.
                It still can be set as edit target with scripts, while this can be used for guardrails.
                
        """
    def is_muteness_global(self) -> bool:
        """
        
                Global muteness is an extended concept for Omniverse so muteness can be authored into
                USD for persistence. When you set muteness scope as global with set_muteness_scope,
                all muteness of sublayers will be stored to root layer's custom data and it will be
                loaded for next stage open.
                
        """
    def reload_all_outdated_layers(self, not_in_session = True, not_auto = False) -> None:
        """
        Reloads all oudated layers to fetch latest updates. We only want to reload layers that are not in session
        """
    def reload_outdated_non_sublayers(self, not_in_session = True, not_auto = False) -> None:
        """
        
                Reloads all outdated non-sublayers in the stage to fetch latest changes. If a layer is both inserted
                as sublayer and reference, it will be treated as sublayer only and will not be reloaded in this function.
                
        """
    def reload_outdated_sublayers(self, not_in_session = True, not_auto = False) -> None:
        """
        Reloads all oudated sublayers that are in the stage's local layer stack to fetch latest changes.
        """
    def remove_auto_reload_layer(self, layer_identifier: str):
        """
        Remove layer from auto-reload list.
        """
    def set_layer_lock_state(self, layer_identifier: str, locked: bool) -> None:
        """
        
                Layer lock is an extended concept in Omniverse that works for lock this layer temporarily without real change
                the file permission of this layer. It's just authored as a meta inside layer's custom data section, and read by
                UI.
                
        """
    def set_layer_name(self, layer_identifier: str, name: str) -> None:
        ...
    def set_muteness_scope(self, global_scope: bool) -> None:
        ...
    @property
    def usd_context(self):
        ...
SETTINGS_AUTO_RELOAD_NON_SUBLAYERS: str = '/persistent/ext/omni.kit.widget.stage/auto_reload_non_sublayers'
SETTINGS_AUTO_RELOAD_SUBLAYERS: str = '/persistent/ext/omni.kit.usd.layers/auto_reload_sublayers'
SETTINGS_IGNORE_OUTDATE_NOTIFICATION: str = '/persistent/ext/omni.kit.user.layers/ignore_outdate_notification'
