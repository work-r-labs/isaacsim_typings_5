from __future__ import annotations
import asyncio as asyncio
from carb.input import KeyboardInput as Key
from functools import partial
import omni as omni
from omni import ui
__all__ = ['DelayedFocus', 'KEYBOARD_MODIFIER_FLAG_CONTROL', 'Key', 'PathFieldModel', 'UI_STYLES', 'asyncio', 'omni', 'partial', 'ui']
class DelayedFocus:
    """
    A helper to run focus_keyboard the next frame
    """
    def _DelayedFocus__delayed_do(self):
        ...
    def __init__(self, field: omni.ui._ui.StringField):
        ...
    def destroy(self):
        ...
    def focus_keyboard(self):
        """
        Execute frame.focus_keyboard in the next frame
        """
class PathFieldModel(omni.ui._ui.AbstractValueModel):
    def _PathFieldModel__build_input(self, width, height):
        ...
    def __init__(self, parent: omni.ui._ui.Widget, theme: str, **kwargs):
        ...
    def _build_ui(self):
        ...
    def _extend_path_by_selected_branch(self, index: int):
        ...
    def _hide_window(self):
        ...
    def _on_key_pressed(self, key: int, key_mod: int, key_down: bool):
        """
        
                Process keys on release.
                
        """
    def _on_main_window_resized(self, *_):
        ...
    def _place_window(self):
        ...
    def _shrink_path_by_tail_branch(self):
        ...
    def _update_tooltips(self, force_update = False):
        """
        Generates list of tips
        """
    def _update_tooltips_menu(self, match_str: str, update_branches: bool, branches: typing.List[str]):
        ...
    def begin_edit(self):
        ...
    def destroy(self):
        ...
    def get_value_as_string(self) -> str:
        ...
    def set_branches(self, branches: [str]):
        ...
    def set_path(self, path: str):
        ...
    def set_value(self, value: str):
        ...
KEYBOARD_MODIFIER_FLAG_CONTROL: int = 2
UI_STYLES: dict  # value = {'NvidiaLight': {'Window': {'secondary_background_color': 0}, 'ScrollingFrame': {'background_color': 4283650900, 'margin': 0, 'padding': 0}, 'Rectangle': {'background_color': 4283650900}, 'InputField': {'background_color': 4283650900, 'color': 4292269782, 'padding': 0}, 'BreadCrumb': {'background_color': 0, 'padding': 0}, 'BreadCrumb.Label': {'color': 4292269782}, 'BreadCrumb:hovered': {'background_color': 4291808447}, 'BreadCrumb.Label:hovered': {'color': 4280952869}, 'BreadCrumb:selected': {'background_color': 4283650900}, 'Tooltips.Menu': {'background_color': 4292927712, 'border_color': 4292927712, 'border_width': 0.5}, 'Tooltips.Item': {'background_color': 4283650900, 'padding': 4}, 'Tooltips.Item:hovered': {'background_color': 4285427310}, 'Tooltips.Item:checked': {'background_color': 4285427310}, 'Tooltips.Item.Label': {'color': 4292269782, 'alignment': <Alignment.LEFT: 2>}, 'Tooltips.Spacer': {'background_color': 0, 'color': 0, 'alignment': <Alignment.LEFT: 2>, 'padding': 0}}, 'NvidiaDark': {'Window': {'secondary_background_color': 0}, 'ScrollingFrame': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'InputField': {'background_color': 0, 'color': 4288585374, 'padding': 0, 'margin': 0}, 'BreadCrumb': {'background_color': 0, 'padding': 0}, 'BreadCrumb:hovered': {'background_color': 4287268727}, 'BreadCrumb:selected': {'background_color': 4287268727}, 'BreadCrumb.Label': {'color': 4288585374}, 'BreadCrumb.Label:hovered': {'color': 4280952869}, 'Tooltips.Menu': {'background_color': 3710066975, 'border_color': 2861205367, 'border_width': 0.5}, 'Tooltips.Item': {'background_color': 0, 'padding': 4}, 'Tooltips.Item:hovered': {'background_color': 4287268727}, 'Tooltips.Item:checked': {'background_color': 4287268727}, 'Tooltips.Item.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT: 2>}, 'Tooltips.Item.Label:hovered': {'color': 4280952869}, 'Tooltips.Item.Label:checked': {'color': 4280952869}, 'Tooltips.Spacer': {'background_color': 0, 'color': 0, 'alignment': <Alignment.LEFT: 2>, 'padding': 0, 'margin': 0}}}
