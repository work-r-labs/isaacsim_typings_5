from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.kit.usd.layers._impl.event import LayerEventType
from omni.kit.usd.layers._impl.interface_utils import get_layer_event_payload
from omni.kit.usd.layers._impl.interface_utils import post_notification
from omni.kit.usd.layers._impl.layer_utils import LayerUtils
from omni.kit.usd.layers._impl.live_session_channel_manager import LiveSessionChannelManager
from omni.kit.usd.layers._impl.live_session_channel_manager import LiveSessionUser
from omni.kit.usd.layers._omni_kit_usd_layers import ILayersInstance
from omni.kit.usd.layers._omni_kit_usd_layers import acquire_live_syncing_interface
from omni.kit.usd.layers._omni_kit_usd_layers import release_live_syncing_interface
import pxr.Sdf
from pxr import Sdf
from pxr import Usd
import urllib as urllib
import weakref as weakref
__all__: list = ['get_live_session_name_from_shared_link', 'LiveSession', 'LiveSyncing', 'LiveSessionUser']
class LiveSession:
    """
    
        Python instance of ILayersInstance for the convenience of accessing
        and querying properties and states of a Live Session.
        
    """
    def __init__(self, handle, session_channel, live_syncing):
        """
        Internal constructor.
        """
    def __str__(self) -> str:
        ...
    def _set_session_handle(self, session_handle):
        ...
    def get_last_modified_time(self) -> int:
        """
        
                Gets the last modified time of the Live Session. The modified time is
                fetched from the session config file. It can be used to sort the Live Session
                list in access order.
                
        """
    def get_peer_user_info(self, user_id) -> omni.kit.usd.layers._impl.live_session_channel_manager.LiveSessionUser:
        """
        Gets the info of peer user by user id if this session is joined.
        """
    @property
    def base_layer_identifier(self) -> str:
        """
        The base layer identifier of the Live Session.
        """
    @property
    def channel_url(self) -> str:
        """
        The channel url of the Live Session that shares by all users to do communication.
        """
    @property
    def joined(self) -> bool:
        """
        Returns True if this session is joined locally.
        """
    @property
    def logged_user(self) -> omni.kit.usd.layers._impl.live_session_channel_manager.LiveSessionUser:
        """
        
                The user that connects the server of base layer. It's also the user that joins the Live Session, and
                can be uniquely identified in the Live Session with user id.
                
        """
    @property
    def logged_user_id(self) -> str:
        """
        The user id that connects the server of base layer. And it's also the user that joins the Live Session.
        """
    @property
    def logged_user_name(self) -> str:
        """
        The user name that connects the server of base layer. And it's also the user that joins the Live Session.
        """
    @property
    def merge_permission(self) -> bool:
        """
        
                Whether local user has permission to merge the Live Session or not. It's possible that
                the local user is the owner but this returns False as if multiple instances of the same
                user join the same session, only one of them will be the runtime owner.
                
        """
    @property
    def name(self) -> str:
        """
        The name of the Live Session.
        """
    @property
    def owner(self) -> str:
        """
        
                The owner name of the Live Session. It returns the static owner name of the session only.
                If it has multiple instances of the same user join the same session, only one of the owner
                has the real merge_permission.
                
        """
    @property
    def peer_users(self) -> typing.List[omni.kit.usd.layers._impl.live_session_channel_manager.LiveSessionUser]:
        """
        All peer users in the Live Session if the session is joined.
        """
    @property
    def root(self) -> str:
        """
        The url of the root.live layer for the Live Session in the server.
        """
    @property
    def shared_link(self) -> str:
        """
        
                The session link to be shared. Shared link is different as
                url, so url points to the physical location of the Live Session
                that local user can get access to, while session link is the URL
                that you can share to others, and can be launched from Omniverse launcher
                and other apps could parse it and decide the action from it. The session
                name is passed as the query parameter to the base layer url, for example,
                omniverse://localhost/test/stage.usd?live_session_name=my_session.
                
        """
    @property
    def url(self) -> str:
        """
        The physical url of the Live Session in the server.
        """
    @property
    def valid(self) -> bool:
        """
        Returns true if the session is valid. Or it's removed.
        """
class LiveSyncing:
    """
    
        Live Syncing includes the interfaces to management Live Sessions of all layers in the bound UsdContext.
        A Live Session is a concept that extends non-destructive live workflow for USD layers so all connectors
        can join the session to co-work together.
    
        Each Live Session is bound to an USD file with unique URL to be identified. And it has only unique instance
        in the same UsdContext for each layer, which means the Live Sessions can be joined multiple times.
        User can only join the Live Sessions that belong to the used layers in the bound UsdContext, either those layers
        are added as sublayers or references/payloads. If a layer is added as both a local sublayer or reference/payload,
        the sublayer and reference/payload cannot join the same Live Session at the same time. However, a Live Session
        can be joined multiple times if the corresponding layer is added as multiple references/payloads.
    
        Thread Safety: All interfaces of LiveSyncing are not thread-safe. And It's recommended to call
        those interfaces in the same loop thread as UsdContext.
        
    """
    def _LiveSyncing__get_context_and_stage(self, stage_or_context):
        ...
    def _LiveSyncing__get_live_session_prim_paths(self, session_handle):
        """
        Gets the prim that joins this Live Session.
        """
    def _LiveSyncing__on_post_move_prim(self, params, undo):
        ...
    def _LiveSyncing__on_pre_move_prim(self, params, undo):
        ...
    def __init__(self, layers_instance: omni.kit.usd.layers._omni_kit_usd_layers.ILayersInstance, usd_context, layers_state) -> None:
        ...
    def _destroy(self):
        """
        Destructor. Don't call this manually.
        """
    def _on_layer_event(self, event: carb.events._events.IEvent):
        ...
    def _on_stage_event(self, event):
        ...
    def _reset(self):
        ...
    def _to_live_session(self, session_handle, base_layer_identifier):
        ...
    def broadcast_merge_done_message_async(self, destroy: bool = True, layer_identifier: str = None):
        """
        
                Broadcasts merge finished message to other peer clients. This is normally
                called after merging the Live Session to its base layer.
        
                "Args:
                    destroy (bool): If it needs to destroy the session channel after merging.
        
                    layer_identifier (str): The base layer of the Live Session.
                
        """
    def broadcast_merge_started_message_async(self, layer_identifier: str = None):
        """
        
                Broadcasts merge started message to other peer clients. This is normally
                called before merging the Live Session to its base layer.
                
        """
    def create_live_session(self, name: str, layer_identifier: str = None) -> LiveSession:
        """
        
                Creates a named Live Session.
        
                Args:
                    name (str): Name of the session. Currently, name should be unique across all Live Sessions.
        
                    layer_identifier (str): The base layer to create a Live Session. If it's not provided,
                                            it will be root layer by default.
        
                Returns:
                    The Live Session handle if it's success, or None otherwise.
                    See Layers.get_last_error_type to get more details.
                
        """
    def find_live_session_by_name(self, layer_identifier: str, session_name: str) -> LiveSession:
        """
        
                Finds the Live Session with name specified by `session_name`. If it has multiple sessions that
                has the same name, it will return the first one found.
        
                Args:
                    layer_identifier (str): The base layer to search Live Sessions.
                    session_name (str): The session name.
                
        """
    def get_all_current_live_sessions(self, prim_path: pxr.Sdf.Path = None) -> typing.List[omni.kit.usd.layers._impl.live_syncing.LiveSession]:
        """
        
                Gets all Live Sessions that are joined for all sublayers of the stage or a specific prim.
        
                Args:
                    prim_spec (Sdf.Path): Specified prim to query. If prim_path is not None, it will
                        return all live sessions joined for this prim. If it's None, it will return
                        the live sessions joined for all sublayers of the current stage.
                
        """
    def get_all_live_sessions(self, layer_identifier: str = None) -> typing.List[omni.kit.usd.layers._impl.live_syncing.LiveSession]:
        """
        
                Gets all existing Live Sessions on disk (including joined and not joined ones) for a specific layer.
                See `get_current_live_session` to query joined session for a specific layer.
        
                Args:
                    layer_identifier (str): The base layer to query Live Sessions.
                                            If it's empty, it will be root layer by default.
        
                Returns:
                    A list of Live Sessions.
                
        """
    def get_current_live_session(self, layer_identifier: str = None) -> LiveSession:
        """
        
                Gets the current Live Session of the base layer joined.
        
                Args:
                    layer_identifier (str): Base layer identifier. It's root layer if it's not provided.
                
        """
    def get_current_live_session_layers(self, layer_identifier: str = None) -> typing.List[str]:
        """
        
                [DEPRECATED] Returns the Live Session layers attached to this Live Session of specifc base layer.
                
        """
    def get_current_live_session_peer_users(self, layer_identifier: str = None) -> typing.List[omni.kit.usd.layers._impl.live_session_channel_manager.LiveSessionUser]:
        """
        
                [DEPRECATED] Returns the list of users that joined in this Live Session.
        
                Args:
                    layer_identifier (str): It's root layer if it's not provided.
                
        """
    def get_live_session_by_url(self, session_url) -> LiveSession:
        """
        
                Gets the Live Session by the url. It can only get the Live Session belongs to one of the used layers
                in the current stage.
                
        """
    def get_live_session_for_live_layer(self, live_layer_identifier: str) -> LiveSession:
        """
        
                Gets the Live Session that the live layer is attached to.
        
                Args:
                    live_layer_identifier (str): The .live layer that's in the Live Session.
                
        """
    def is_in_live_session(self) -> bool:
        """
        [DEPRECATED] If root layer is in a Live Session.
        """
    def is_layer_in_live_session(self, layer_identifier: str = None, live_prim_only: bool = False) -> bool:
        """
        
                Checks if the given layer is in a Live Session or not.
        
                Args:
                    layer_identifier (str): Base layer identifier. Root layer by default.
                    live_prim_only (bool): When live_prim_only is True, it will only check the Live Sessions
                                           that are bound to reference/payload prims for the base layer.
                                           Otherwise, it will check all. False by default.
                
        """
    def is_live_session_layer(self, layer_identifier: str) -> bool:
        """
        Checks if the layer is the live layer (.live layer) of a Live Session.
        """
    def is_live_session_merge_notice_muted(self, layer_identifier: str) -> bool:
        """
        Checks if layer identifier is in the mute list.
        """
    def is_prim_in_live_session(self, prim_path: pxr.Sdf.Path, layer_identifier: str = None, from_reference_or_payload_only = False) -> bool:
        """
        
                If the prim is in any Live Session.
        
                Args:
                    prim_path (Sdf.Path): Prim path to check.
                    layer_identifier (str): If layer identifier is specified, it will check if prim is in
                        the Live Session of that layer only.
                    from_reference_or_payload_only (bool): If it's True, it will check only references and payloads
                        to see if the same Live Session is enabled already. Otherwise, it checks both the prim specificed
                        by primPath and its references and payloads. This is normally used to check if the Live Session can
                        be stopped as the prim that is in the Live Session may not own the Live Session, which is owned by its
                        references or payloads, so it cannot stop the Live Session with the specified prim.
                
        """
    def is_stage_in_live_session(self) -> bool:
        """
        Checks if any layers that are in the used layers of the current stage are in a Live Session.
        """
    def join_live_session(self, live_session: LiveSession, prim_path: typing.Union[pxr.Sdf.Path, str] = None) -> bool:
        """
        
                Joins the Live Session.
        
                Args:
                    live_session (LiveSession): The Live Session to join. The base layer of the Live Session must
                        be in the used layers of the current stage.
                    prim_path (Union[Sdf.Path, str]): If prim path is provided, it means to join a Live Session for
                        a reference or payload prim.
        
                Returns:
                    True if it joins the session successfully. False otherwise.
                    See Layers.get_last_error_type to get more details.
                
        """
    def join_live_session_by_url(self, layer_identifier: str, live_session_url: str, create_if_not_existed: bool = False) -> bool:
        """
        
                Joins the Live Session specified by the Live Session URL.
        
                Args:
                    layer_identifier (str): The base layer of the Live Session.
        
                    live_session_url (str): The unique URL of the Live Session. The Live Session must be created against
                                            with the base layer, otherwise, it will fail to join.
        
                    create_if_not_existed (bool): Creates the Live Session if it does not exist.
        
                Returns:
                    True if it joins the session successfully. False otherwise.
                    See Layers.get_last_error_type to get more details.
                
        """
    def merge_and_stop_live_session_async(self, target_layer: str = None, comment = '', pre_merge: typing.Callable[[omni.kit.usd.layers._impl.live_syncing.LiveSession], typing.Awaitable] = None, post_merge: typing.Callable[[bool], typing.Awaitable] = None, layer_identifier: str = None) -> bool:
        """
        Saves chagnes of Live Session to their base layer if it's in live mode.
        
                Args:
                    target_layer (str): Target layer to merge all live changes to.
        
                    comment (str): The checkpoint comments.
        
                    pre_merge (Callable[[LiveSession], Awaitable]): It will be called before merge.
        
                    post_merge (Callable[[bool, str], Awaitable]): It will be called after merge is done. The first
                                                                   param means if it's successful, and the second includes
                                                                   the error message if it's not.
        
                    layer_identifier (str): The base layer of the Live Session. It's root layer if it's not provided.
                
        """
    def merge_changes_to_base_layers(self, stop_session: bool) -> bool:
        """
        
                [DEPRECATED] Merges changes of root layer's Live Session to its base layer.
                
        """
    def merge_changes_to_specific_layer(self, target_layer_identifier: str, stop_session: bool, clear_target_layer: bool) -> bool:
        """
        
                [DEPRECATED] Merges changes of root layer's Live Session to specified layer.
                
        """
    def merge_live_session_changes(self, layer_identifier: str, stop_session: bool) -> bool:
        """
        
                Merge Live Session for base layer.
        
                Args:
                    layer_identifier (str): The base layer to merge Live Session.
                    stop_session (bool): Stops the Live Session or not after merging.
        
                Returns:
                    True if it's successful, or False otherwise. If it returns False,
                    it's possible that the layer is not in the used layers of the current stage. Or
                    it has no Live Session joined. Or it has not permissions to merge the Live Session.
                    See Layers.get_last_error_type to get more details.
                
        """
    def merge_live_session_changes_to_specific_layer(self, layer_identifier: str, target_layer_identifier: str, stop_session: bool, clear_target_layer: bool) -> bool:
        """
        
                Merge Live Session for base layer to specified target layer.
        
                Args:
                    layer_identifier (str): The base layer to merge Live Session.
                    target_layer_identifier (str): The target layer to merge the Live Session.
                    stop_session (bool): Stops the Live Session or not after merging.
                    clear_target_layer (bool): If it needs to clear the target layer before merging.
        
                Returns:
                    True if it's successful, or False otherwise. If it returns False,
                    it's possible that the layer is not in the used layers of the current stage. Or
                    it has no Live Session joined. Or it has not permissions to merge the Live Session.
                    See Layers.get_last_error_type to get more details.
                
        """
    def mute_live_session_merge_notice(self, layer_identifier: str):
        """
        
                By default, when session owner merges the session, it will
                notify peer clients to leave the session by showing a prompt.
                This is used to disable the prompt and stop session directly
                so it will not be disruptive especially for applications that
                don't have layer window and manages all layers' Live Sessions
                with scripting and don't want to receive prompt for leaving
                sessions.
                
        """
    def open_stage_with_live_session_async(self, stage_url, session_name = None) -> typing.Tuple[bool, str]:
        """
        
                Opens stage with Live Session joined. This function is used to reduce the composition cost of
                opening a stage, then joining a Live Session by preparing the Live Session in the session layer
                before opening the stage. It supports to pass the name of Live Session as query string, for example,
                `omniverse://localhost/test/stage.usd?live_session_name=my_session`.
        
                Args:
                    stage_url (str): The stage url to open.
                    session_name (str): If the session name is not provided in the stage url, this param will be used.
                        If both stage url and this param don't include a valid session, it will return false.
        
                Returns:
                    A (bool, str) tutple, where the first element means if it's success, and the error string int the second.
                
        """
    def register_open_stage_addon(self, callback):
        ...
    def stop_all_live_sessions(self):
        """
        Stops all the Live Sessions that are enabled for the current stage.
        """
    def stop_live_session(self, layer_identifier: str = None, prim_path: pxr.Sdf.Path = None):
        """
        
                Stops the Live Session for specificed layer or prim.
        
                Args:
                    layer_identifier (str): The base layer to stop its current Live Session. If it's None and prim_path is None,
                                            it's root layer by default.
                    prim_path (Sdf.Path): The specified prim to stop the Live Session. If prim_path is given, and
                                          layer_identifier is None, it will stop all joined Live Sessions for this prim.
                                          Or if layer_identifier is not None, it will stop only the Live Session for the layer.
                
        """
    def try_cancelling_live_session_join(self, layer_identifier: str) -> typing.Optional[omni.kit.usd.layers._impl.live_syncing.LiveSession]:
        """
        
                Try to cancel the Live Session when LayerEventType.LIVE_SESSION_JOINING is received.
        
                Args:
                    layer_identifier (str): The base layer to cancel.
        
                Returns:
                    Instance of Live Session if it's cancelled successfully. Or None otherwise.
                
        """
    def unmute_live_session_merge_notice(self, layer_identifier: str):
        """
        Remove layer identifier from mute list.
        """
    @property
    def layers_instance(self) -> omni.kit.usd.layers._omni_kit_usd_layers.ILayersInstance:
        """
        Native handle of Layers instance that's bound to an UsdContext.
        """
    @property
    def permission_to_merge_current_session(self, layer_identifier: str = None) -> bool:
        """
        
                [DEPRECATED] Checks to see if it can merge the current Live Session of specified layer.
        
                Args:
                    layer_identifier (str): The base layer of the Live Session. It's root layer if it's not provided.
                
        """
    @property
    def usd_context(self) -> omni.usd._usd.UsdContext:
        """
        Instance of UsdContext.
        """
class _CallbackRegistrySubscription:
    """
    
        Simple subscription.
    
        _Event has callback while this object exists.
        
    """
    def __del__(self):
        """
        Called by GC.
        """
    def __init__(self, callback_list: typing.List, callback: typing.Callable):
        """
        
                Save the callback in the given list.
                
        """
def _get_app():
    ...
def get_live_session_name_from_shared_link(shared_session_link: str) -> str:
    """
    Gets the name of Live Session from the url.
    """
