from __future__ import annotations
import omni as omni
__all__ = ['CLOSE_ALL', 'COPY_NODES', 'EXPAND_ALL', 'FOCUS_ON_NODES', 'LAYOUT_ALL', 'MATERIAL_UNPAUSE_AND_PAUSE', 'MINIMIZE_ALL', 'PASTE_NODES', 'TOGGLE_MATERIAL_COMPILATION', 'deregister_actions', 'omni', 'register_actions']
def deregister_actions(extension_id):
    ...
def register_actions(extension_id: str, ext_instance):
    ...
CLOSE_ALL: str = 'close_all_nodes'
COPY_NODES: str = 'copy_nodes'
EXPAND_ALL: str = 'expand_all_nodes'
FOCUS_ON_NODES: str = 'focus_on_nodes'
LAYOUT_ALL: str = 'layout_all_nodes'
MATERIAL_UNPAUSE_AND_PAUSE: str = 'material_unpause_and_pause'
MINIMIZE_ALL: str = 'minimize_all_nodes'
PASTE_NODES: str = 'paste_nodes'
TOGGLE_MATERIAL_COMPILATION: str = 'toggle_material_compilation'
