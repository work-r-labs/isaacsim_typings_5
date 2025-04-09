from __future__ import annotations
import carb as carb
from omni.kit.material.library import material_config_utils
import omni.kit.material.library.pages.material_config_widget
from omni.kit.material.library.pages.material_config_widget import EditableListItemDelegate
from omni.kit.material.library.pages.material_config_widget import EditableListModel
from omni.kit.material.library.pages.material_config_widget import EditableListWidget
from omni.mdl import pymdlsdk
from omni import ui
import omni.ui._ui
import omni.ui.color_utils
import os as os
import pathlib as pathlib
import typing
__all__ = ['EditableListItemDelegate', 'EditableListModel', 'EditableListWidget', 'MdlCustomPathListModel', 'MdlCustomPathListWidget', 'MdlDefaultPathListModel', 'MdlDefaultPathListWidget', 'MdlPathItem', 'carb', 'cl', 'material_config_utils', 'os', 'pathlib', 'pymdlsdk', 'ui']
class MdlCustomPathListModel(omni.kit.material.library.pages.material_config_widget.EditableListModel):
    def __init__(self, setting_path):
        ...
    def find_path(self, path):
        ...
    def populate_items(self):
        ...
    def sanity_check_paths(self):
        ...
    def save_entries_to_settings(self):
        ...
    def save_to_material_config_file(self):
        ...
class MdlCustomPathListWidget(omni.kit.material.library.pages.material_config_widget.EditableListWidget):
    def __init__(self):
        ...
    def on_add_new_entry_button_clicked(self):
        ...
    def on_file_picker_apply_clicked(self, filename, dirname, selections):
        ...
    def on_save_button_clicked(self):
        ...
class MdlDefaultPathListModel(omni.ui._ui.AbstractItemModel):
    SOURCE_ADDITIONAL_SYSTEM_PATHS: typing.ClassVar[int] = 2
    SOURCE_ADDITIONAL_USER_PATHS: typing.ClassVar[int] = 3
    SOURCE_MDL_SYSTEM_PATH: typing.ClassVar[int] = 0
    SOURCE_MDL_USER_PATH: typing.ClassVar[int] = 1
    SOURCE_RENDERER_REQUIRED: typing.ClassVar[int] = 4
    SOURCE_RENDERER_TEMPLATES: typing.ClassVar[int] = 5
    def __init__(self, mode):
        ...
    def _get_omni_neuray_api(self):
        ...
    def _get_paths_from_array_setting(self, mode):
        ...
    def _get_paths_from_mdl_config(self, mode):
        ...
    def _get_paths_from_setting(self, mode):
        ...
    def get_item_children(self, item):
        ...
    def get_item_value_model(self, item, column_id):
        ...
    def get_item_value_model_count(self, item):
        ...
    def get_items(self):
        ...
class MdlDefaultPathListWidget:
    _FRAME_STYLE: typing.ClassVar[dict] = {'CollapsableFrame': {'margin': 0, 'padding': 3, 'border_width': 0, 'border_radius': 0, 'secondary_color': 4281216556}}
    _TREEVIEW_STYLE: typing.ClassVar[dict] = {'TreeView.Item': {'margin': 3, 'font_size': 16.0, 'color': 4286019447}}
    def __init__(self, **kwargs):
        ...
    def _add_path_list_widget(self, title, model):
        ...
class MdlPathItem(omni.ui._ui.AbstractItem):
    _URLPREFIXES: typing.ClassVar[tuple] = ('omniverse://', 'http://', 'https://')
    def __init__(self, text):
        ...
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
