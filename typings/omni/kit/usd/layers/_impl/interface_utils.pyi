from __future__ import annotations
import carb as carb
import omni.kit.usd.layers._impl.event
from omni.kit.usd.layers._impl.event import LayerEventType
from pxr import Sdf
__all__: list = ['LayerEventPayload', 'get_layer_event_payload', 'get_short_user_name', 'LayerEventType']
class LayerEventPayload:
    """
    
        LayerEventPayload is a wrapper to carb.events.IEvent sent from module omni.kit.usd.layers.
        Through which, you can query event payload easier with properties.
        
    """
    def __init__(self, event: carb.events._events.IEvent) -> None:
        ...
    def is_layer_influenced(self, layer_identifier_or_handle: typing.Union[str, pxr.Sdf.Layer]) -> bool:
        """
        Checks if specific layer is influenced by the event.
        """
    @property
    def event_type(self) -> omni.kit.usd.layers._impl.event.LayerEventType:
        """
        Layer event type, it's None when the event type is unknown.
        """
    @property
    def identifiers_or_spec_paths(self) -> typing.List[str]:
        """
        
                The influenced layers or prim specs if any. When event type is LayerEventType.SPECS_LOCKING_CHANGED,
                it hosts all influenced prim specs. Otherwise, it hosts all influenced layers for the event.
                
        """
    @property
    def layer_identifier(self) -> str:
        """
        
                This property is non-empty when any layers are influenced. If multiple layers are influenced,
                it's the first one of identifiers_or_spec_paths to keep compatibility.
                
        """
    @property
    def layer_info_data(self) -> typing.Dict[str, typing.List[str]]:
        """
        
                It is non-empty if event type is INFO_CHANGED, of which key is the layer identifier
                that its metadata has changed, and value is the set of strings that represent the metadata tokens
                that's modified. Currently, only the following tokens are notified when they are modified:
        
                UsdGeom.Tokens.upAxis
        
                UsdGeom.Tokens.metersPerUnit
        
                Sdf.Layer.StartTimeCodeKey
        
                Sdf.Layer.EndTimeCodeKey
        
                Sdf.Layer.FramesPerSecond
        
                Sdf.Layer.TimeCodesPerSecond
        
                Sdf.Layer.CommentKey
        
                Sdf.Layer.Documentation
        
                "subLayerOffsets_offset"  # String as there is no python binding from USD.
        
                "subLayerOffsets_scale"
                
        """
    @property
    def layer_spec_paths(self) -> typing.Dict[str, typing.List[str]]:
        """
        
                The influenced spec paths for each layer.
                It's non-empty if event type is PRIM_SPECS_CHANGED or SPECS_LINKING_CHANGED,
                of which, the key is the layer identifier, and value is the list of spec paths.
                
        """
    @property
    def success(self) -> bool:
        """
        
                It's useful if event type is LIVE_SESSION_MERGE_STARTED or LIVE_SESSION_MERGE_ENDED, which
                means if merge of a Live Session is successful or not.
                
        """
    @property
    def user_id(self) -> str:
        """
        It's non-empty if event type is LIVE_SESSION_USER_JOINED or LIVE_SESSION_USER_LEFT.
        """
    @property
    def user_name(self) -> str:
        """
        It's non-empty if event type is LIVE_SESSION_USER_JOINED or LIVE_SESSION_USER_LEFT.
        """
def get_layer_event_payload(event: carb.events._events.IEvent) -> LayerEventPayload:
    """
    Gets the payload of layer events by populating them into an instance of LayerEventPayload.
    """
def get_short_user_name(user_name: str) -> str:
    """
    Gets short name with capitalized first letters of each word.
    """
def post_notification(message: str, info = True):
    ...
