from __future__ import annotations
import carb as carb
import enum
from enum import IntEnum
from omni.kit.usd.layers._omni_kit_usd_layers import LayerEventType as NativeLayerEventType
import typing
__all__: list = ['LayerEventType']
class DerivedLayerEventType(enum.IntEnum):
    """
    An enumeration.
    """
    AUTO_RELOAD_LAYERS_CHANGED: typing.ClassVar[DerivedLayerEventType]  # value = <DerivedLayerEventType.AUTO_RELOAD_LAYERS_CHANGED: 13971227396738620480>
class LayerEventType(enum.IntEnum):
    """
    Layer event types.
    
    Members:
    
      INFO_CHANGED : Layer metadata changed.
    
      DIRTY_STATE_CHANGED : Layers' dirty state changed.
    
      LOCK_STATE_CHANGED : Layers' lock state changed.
    
      MUTENESS_SCOPE_CHANGED : Layers' mute scope changed.
    
      MUTENESS_STATE_CHANGED : Layers' mute state changed.
    
      OUTDATE_STATE_CHANGED : Layers' outdate state changed.
    
      PRIM_SPECS_CHANGED : Layers' prim specs changed.
    
      SUBLAYERS_CHANGED : Layers' sublayer list changed.
    
      EDIT_TARGET_CHANGED : Stage's edit target changed.
    
      SPECS_LOCKING_CHANGED : Stage's locking specs changed.
    
      SPECS_LINKING_CHANGED : Stage's linking specs changed.
    
      EDIT_MODE_CHANGED : Stage's edit mode changed.
    
      DEFAULT_LAYER_CHANGED : Stage's default layer changed when it's in Auto Authoring mode.
    
      LIVE_SESSION_STATE_CHANGED : Layers' Live Session state changed.
    
      LIVE_SESSION_JOINING : Layers are joining Live Session.
    
      LIVE_SESSION_LIST_CHANGED : Layers' Live Session list changed.
    
      LIVE_SESSION_USER_JOINED : New User joined the Live Session.
    
      LIVE_SESSION_USER_LEFT : New User left the Live Session.
    
      LIVE_SESSION_MERGE_STARTED : Merging Live Session started.
    
      LIVE_SESSION_MERGE_ENDED : Merging Live Session ended.
    
      USED_LAYERS_CHANGED : Stage's used layers changed.
    
      LAYER_FILE_PERMISSION_CHANGED : Layer's file permisison changed on file system.
    """
    AUTO_RELOAD_LAYERS_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.AUTO_RELOAD_LAYERS_CHANGED: 13971227396738620480>
    DEFAULT_LAYER_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.DEFAULT_LAYER_CHANGED: 12>
    DIRTY_STATE_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.DIRTY_STATE_CHANGED: 4>
    EDIT_MODE_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.EDIT_MODE_CHANGED: 11>
    EDIT_TARGET_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.EDIT_TARGET_CHANGED: 10>
    INFO_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.INFO_CHANGED: 0>
    LAYER_FILE_PERMISSION_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.LAYER_FILE_PERMISSION_CHANGED: 21>
    LIVE_SESSION_JOINING: typing.ClassVar[LayerEventType]  # value = <LayerEventType.LIVE_SESSION_JOINING: 20>
    LIVE_SESSION_LIST_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.LIVE_SESSION_LIST_CHANGED: 14>
    LIVE_SESSION_MERGE_ENDED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.LIVE_SESSION_MERGE_ENDED: 18>
    LIVE_SESSION_MERGE_STARTED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.LIVE_SESSION_MERGE_STARTED: 17>
    LIVE_SESSION_STATE_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.LIVE_SESSION_STATE_CHANGED: 13>
    LIVE_SESSION_USER_JOINED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.LIVE_SESSION_USER_JOINED: 15>
    LIVE_SESSION_USER_LEFT: typing.ClassVar[LayerEventType]  # value = <LayerEventType.LIVE_SESSION_USER_LEFT: 16>
    LOCK_STATE_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.LOCK_STATE_CHANGED: 3>
    MUTENESS_SCOPE_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.MUTENESS_SCOPE_CHANGED: 1>
    MUTENESS_STATE_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.MUTENESS_STATE_CHANGED: 2>
    OUTDATE_STATE_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.OUTDATE_STATE_CHANGED: 5>
    PRIM_SPECS_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.PRIM_SPECS_CHANGED: 6>
    SPECS_LINKING_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.SPECS_LINKING_CHANGED: 9>
    SPECS_LOCKING_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.SPECS_LOCKING_CHANGED: 8>
    SUBLAYERS_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.SUBLAYERS_CHANGED: 7>
    USED_LAYERS_CHANGED: typing.ClassVar[LayerEventType]  # value = <LayerEventType.USED_LAYERS_CHANGED: 19>
__all_name_values: list = [('INFO_CHANGED', 0), ('DIRTY_STATE_CHANGED', 4), ('LOCK_STATE_CHANGED', 3), ('MUTENESS_SCOPE_CHANGED', 1), ('MUTENESS_STATE_CHANGED', 2), ('OUTDATE_STATE_CHANGED', 5), ('PRIM_SPECS_CHANGED', 6), ('SUBLAYERS_CHANGED', 7), ('EDIT_TARGET_CHANGED', 10), ('SPECS_LOCKING_CHANGED', 8), ('SPECS_LINKING_CHANGED', 9), ('EDIT_MODE_CHANGED', 11), ('DEFAULT_LAYER_CHANGED', 12), ('LIVE_SESSION_STATE_CHANGED', 13), ('LIVE_SESSION_JOINING', 20), ('LIVE_SESSION_LIST_CHANGED', 14), ('LIVE_SESSION_USER_JOINED', 15), ('LIVE_SESSION_USER_LEFT', 16), ('LIVE_SESSION_MERGE_STARTED', 17), ('LIVE_SESSION_MERGE_ENDED', 18), ('USED_LAYERS_CHANGED', 19), ('LAYER_FILE_PERMISSION_CHANGED', 21), ('AUTO_RELOAD_LAYERS_CHANGED', 13971227396738620480)]
