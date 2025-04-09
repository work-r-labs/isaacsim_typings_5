from __future__ import annotations
import asyncio as asyncio
from binascii import crc32
import carb as carb
import omni.kit.usd.layers._impl.event
from omni.kit.usd.layers._impl.event import LayerEventType
from omni.kit.usd.layers._impl.interface_utils import post_notification
__all__: list = ['LiveSessionUser', 'LiveSessionChannelManager']
class LiveSessionChannelManager:
    def __init__(self, current_session, live_syncing_interface):
        ...
    def _join_channel_async(self, url):
        ...
    def _on_channel_message(self, message):
        ...
    def _send_layer_event(self, event_type: omni.kit.usd.layers._impl.event.LayerEventType, payload = {}):
        ...
    def _stop_channel(self):
        ...
    def broadcast_merge_done_message_async(self):
        ...
    def broadcast_merge_started_message_async(self):
        ...
    def destroy(self):
        ...
    def start_async(self):
        ...
    def stop(self):
        ...
    @property
    def peer_users(self) -> typing.Dict[str, omni.kit.usd.layers._impl.live_session_channel_manager.LiveSessionUser]:
        ...
    @property
    def stopped(self):
        ...
class LiveSessionUser:
    """
    
        LiveSessionUser represents an peer client instance that joins
        the same Live Session.
        
    """
    def _LiveSessionUser__hsl2rgb(self, hsl) -> typing.Tuple[int, int, int]:
        """
        
                Convert an HSL color value into RGB.
                >>> hsl2rgb((0, 1, 0.5))
                (255, 0, 0)
                
        """
    def _LiveSessionUser__string_to_rgb(self, user_id):
        """
        
                The following implement is ported from:
                https://github.com/dimostenis/color-hash-python/blob/main/colorhash/colorhash.py
                
        """
    def __init__(self, user_name, user_id, from_app):
        ...
    @property
    def from_app(self) -> str:
        ...
    @property
    def user_color(self) -> typing.Tuple[int, int, int]:
        """
        Tuple of RGB color with each channel ranging from [0, 255].
        """
    @property
    def user_id(self) -> str:
        ...
    @property
    def user_name(self) -> str:
        ...
MESSAGE_GROUP_KEY: str = '__SESSION_MANAGEMENT__'
MESSAGE_KEY: str = 'message'
MESSAGE_LAYER_IDENTIFIER_KEY: str = 'layer_identifier'
MESSAGE_MERGE_FINISHED: str = 'MERGE_FINISHED'
MESSAGE_MERGE_STARTED: str = 'MERGE_STARTED'
MESSAGE_USER_ID_KEY: str = 'user_id'
MESSAGE_USER_NAME_KEY: str = 'user_name'
SESSION_MANAGEMENT_VERSION: str = '1.0'
SESSION_MANAGEMENT_VERSION_KEY: str = 'version'
