from __future__ import annotations
import omni as omni
from omni.kit.usd.layers._impl.auto_authoring import AutoAuthoring
from omni.kit.usd.layers._impl.layers_state import LayersState
from omni.kit.usd.layers._impl.live_syncing import LiveSyncing
from omni.kit.usd.layers._impl.specs_linking import SpecsLinking
from omni.kit.usd.layers._impl.specs_locking import SpecsLocking
from omni.kit.usd.layers._omni_kit_usd_layers import LayerEditMode
from omni.kit.usd.layers._omni_kit_usd_layers import LayerErrorType
__all__: list = ['Layers']
class Layers:
    """
    
        Layers is the Python container of ILayersInstance, through which you can access all interfaces. For each UsdContext,
        it has a separate Layers instance.
        
    """
    def __init__(self, layers_instance, usd_context: omni.usd._usd.UsdContext) -> None:
        ...
    def _destroy(self):
        ...
    def get_auto_authoring(self) -> omni.kit.usd.layers._impl.auto_authoring.AutoAuthoring:
        """
        Gets AutoAuthoring interface.
        """
    def get_edit_mode(self) -> omni.kit.usd.layers._omni_kit_usd_layers.LayerEditMode:
        """
        Gets the current edit mode.
        """
    def get_event_stream(self):
        """
        Gets event stream of Layers instance.
        """
    def get_last_error_string(self):
        """
        Gets the last error string.
        """
    def get_last_error_type(self) -> omni.kit.usd.layers._omni_kit_usd_layers.LayerErrorType:
        """
        Gets the last error type.
        """
    def get_layers_state(self) -> omni.kit.usd.layers._impl.layers_state.LayersState:
        """
        Gets LayersState interface.
        """
    def get_live_syncing(self) -> omni.kit.usd.layers._impl.live_syncing.LiveSyncing:
        """
        Gets LiveSyncing interface.
        """
    def get_specs_linking(self) -> omni.kit.usd.layers._impl.specs_linking.SpecsLinking:
        """
        Gets SpecsLinking interface.
        """
    def get_specs_locking(self) -> omni.kit.usd.layers._impl.specs_locking.SpecsLocking:
        """
        Gets SpecsLocking interface.
        """
    def set_edit_mode(self, edit_mode: omni.kit.usd.layers._omni_kit_usd_layers.LayerEditMode):
        """
        Sets the current edit mode.
        """
    @property
    def usd_context(self) -> omni.usd._usd.UsdContext:
        """
        The UsdContext this instance is bound to.
        """
