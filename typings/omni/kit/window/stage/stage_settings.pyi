from __future__ import annotations
import carb as carb
from omni.kit.usd import layers
from omni.kit.window.stage.singleton import Singleton
__all__: list[str] = ['SETTINGS_KEEP_CHILDREN_ORDER', 'SETTINGS_SHOW_ABSTRACT_PRIMS', 'SETTINGS_SHOW_INACTIVE_PRIMS', 'SETTINGS_SHOW_PRIM_DISPLAYNAME', 'SETTINGS_SHOW_UNDEFINED_PRIMS', 'Singleton', 'carb', 'layers']
SETTINGS_KEEP_CHILDREN_ORDER: str = '/persistent/ext/omni.usd/keep_children_order'
SETTINGS_SHOW_ABSTRACT_PRIMS: str = '/persistent/ext/omni.kit.widget.stage/show_abstract_prims'
SETTINGS_SHOW_INACTIVE_PRIMS: str = '/persistent/ext/omni.kit.widget.stage/show_inactive_prims'
SETTINGS_SHOW_PRIM_DISPLAYNAME: str = '/persistent/ext/omni.kit.widget.stage/show_prim_displayname'
SETTINGS_SHOW_UNDEFINED_PRIMS: str = '/persistent/ext/omni.kit.widget.stage/show_undefined_prims'
