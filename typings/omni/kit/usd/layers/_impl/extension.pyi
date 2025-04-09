from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.usd.layers._impl.auto_authoring import AutoAuthoring
from omni.kit.usd.layers._impl.layers_interface import Layers
from omni.kit.usd.layers._impl.layers_state import LayersState
from omni.kit.usd.layers._impl.live_syncing import LiveSyncing
from omni.kit.usd.layers._omni_kit_usd_layers import LayerEditMode
from omni.kit.usd.layers._omni_kit_usd_layers import LayerErrorType
from omni.kit.usd.layers._omni_kit_usd_layers import acquire_layers_interface
from omni.kit.usd.layers._omni_kit_usd_layers import release_layers_interface
from pxr import Sdf
import pxr.Usd
from pxr import Usd
__all__: list = ['get_layers', 'get_auto_authoring', 'get_layers_state', 'get_live_syncing', 'get_last_error_type', 'get_last_error_string', 'LayerEditMode', 'LayerErrorType', 'active_authoring_layer_context', 'Layers']
class Extension(omni.ext._extensions.IExt):
    """
    Extension Class.
    """
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
def _get_layers_interface():
    ...
def active_authoring_layer_context(usd_context) -> pxr.Usd.EditContext:
    """
    
        Gets the edit context for edit target if it's in non-auto authoring mode,
        or edit context for default edit layer if it's in auto authoring mode.
        
    """
def get_auto_authoring(context_name_or_instance: typing.Union[str, omni.usd._usd.UsdContext] = '') -> typing.Optional[omni.kit.usd.layers._impl.auto_authoring.AutoAuthoring]:
    """
    
        Gets the Auto Authoring interface from Layers instance bound to the specified UsdContext.
        REMINDER: Auto Authoring interface is still in experimental stage, which is used to reduce the burden of
        managing deltas inside multi-sublayers, so authoring to stage will be auto-targeted to the layers that
        has its strongest opinions.
        
    """
def get_last_error_string(context_name_or_instance: typing.Union[str, omni.usd._usd.UsdContext] = '') -> str:
    """
    Gets the error string of the API call bound to specified UsdContext.
    """
def get_last_error_type(context_name_or_instance: typing.Union[str, omni.usd._usd.UsdContext] = '') -> omni.kit.usd.layers._omni_kit_usd_layers.LayerErrorType:
    """
    
        Gets the error status of the API call bound to specified UsdContext. Any API calls to Layers interface will change
        the error state. When you want to get the detailed error of your last call, you can use this function to fetch the
        detailed error type.
        
    """
def get_layers(context_name_or_instance: typing.Union[str, omni.usd._usd.UsdContext] = '') -> typing.Optional[omni.kit.usd.layers._impl.layers_interface.Layers]:
    """
    
        Gets Layers instance bound to the context. For each UsdContext, it has unique Layers instance,
        through which, you can access all the interfaces supported.
        
    """
def get_layers_state(context_name_or_instance: typing.Union[str, omni.usd._usd.UsdContext] = '') -> typing.Optional[omni.kit.usd.layers._impl.layers_state.LayersState]:
    """
    
        Gets the Layers State interface from Layers instance bound to the specified UsdContext.
        Layers State interface extends the USD interfaces to access more states of layers, and provides
        utilities for layer operations and event subscription.
        
    """
def get_live_syncing(context_name_or_instance: typing.Union[str, omni.usd._usd.UsdContext] = '') -> typing.Optional[omni.kit.usd.layers._impl.live_syncing.LiveSyncing]:
    """
    
        Gets the Live Syncing interface from Layers instance bound to the specified UsdContext.
        Live Syncing interface is the core of supporting Live Session in Kit, which provides all functionalities to
        manage Live Sessions.
        
    """
_all_layers_instances: dict  # value = {<omni.usd._usd.UsdContext object>: <omni.kit.usd.layers._impl.layers_interface.Layers object>}
_layers_interface: omni.kit.usd.layers._omni_kit_usd_layers.ILayers  # value = <omni.kit.usd.layers._omni_kit_usd_layers.ILayers object>
