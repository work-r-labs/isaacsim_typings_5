from __future__ import annotations
import carb as carb
import collections
from collections import OrderedDict
from omni.kit.material.library import material_config_utils
from omni.kit.widget.settings.settings_widget import SettingType
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni import ui
import omni.ui._ui
import omni.ui.color_utils
import os as os
import typing
__all__ = ['OrderedDict', 'PERSISTENT_SETTINGS_PREFIX', 'PreferenceBuilder', 'RenderContextListItem', 'RenderContextListItemDelegate', 'RenderContextListModel', 'RenderContextWidget', 'SettingType', 'carb', 'cl', 'material_config_utils', 'os', 'ui']
class RenderContextListItem(omni.ui._ui.AbstractItem):
    def __init__(self, value, display_name):
        ...
class RenderContextListItemDelegate(omni.ui._ui.AbstractItemDelegate):
    _ITEM_LABEL_STYLE: typing.ClassVar[dict] = {'margin': 3, 'font_size': 16.0, ':selected': {'color': 4281545523}}
    def build_widget(self, model, item, column_id, level, expanded):
        ...
class RenderContextListModel(omni.ui._ui.AbstractItemModel):
    SUPPORTED_CONTEXTS: typing.ClassVar[collections.OrderedDict]  # value = OrderedDict([('mdl', 'MDL'), ('mtlx', 'MaterialX'), ('', 'Default')])
    def __init__(self, message_fn):
        ...
    def drop(self, target_item, source, drop_location = -1):
        ...
    def drop_accepted(self, target_item, source, drop_location = 1):
        ...
    def get_drag_mime_data(self, item):
        ...
    def get_item_children(self, item = None):
        ...
    def get_item_value_model(self, item, column_id):
        ...
    def get_item_value_model_count(self, item):
        ...
    def populate_items(self):
        ...
class RenderContextWidget(omni.ui._ui.Widget):
    def __init__(self, message_fn):
        ...
    def on_item_selection_changed(self, items):
        ...
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
