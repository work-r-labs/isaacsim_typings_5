from __future__ import annotations
from functools import partial
from omni.kit.asset_converter.impl.context import AssetConverterContext
from omni.kit.tool.asset_importer.filebrowser import FileBrowserMode
from omni.kit.tool.asset_importer.filebrowser import FileBrowserSelectionType
from omni.kit.tool.asset_importer.minimal_model import MinimalItem
from omni.kit.tool.asset_importer.minimal_model import MinimalModal
from omni.kit.tool.asset_importer.utils import Utils
from omni.kit.window import content_browser as content
from omni import ui
import os as os
from pathlib import Path
__all__ = ['AssetConverterContext', 'BuiltinImporterOptions', 'BuiltinImporterOptionsBuilder', 'FileBrowserMode', 'FileBrowserSelectionType', 'MinimalItem', 'MinimalModal', 'OPTIONS_STYLE', 'Path', 'Utils', 'content', 'os', 'partial', 'ui']
class BuiltinImporterOptions:
    def __init__(self) -> None:
        ...
class BuiltinImporterOptionsBuilder:
    def __init__(self, usd_context):
        ...
    def _build_option_checkbox(self, text, default_value, tooltip = '', indent = 0):
        ...
    def _build_option_combobox(self, default_index, items, text, tooltip = '', indent = 0):
        ...
    def _clear(self):
        ...
    def build_pane(self, asset_paths: typing.List[str]):
        ...
    def destroy(self):
        ...
    def get_import_options(self):
        ...
    def set_default_target_folder(self, folder: str):
        ...
OPTIONS_STYLE: dict = {'Button.Image::folder': {'image_url': 'resources/glyphs/folder.svg', 'color': 4288585374, 'image_width': 20, 'image_height': 20, 'background_color': 0}, 'Button.Image::folder:hovered': {'image_url': 'resources/glyphs/folder_open.svg'}, 'Button::folder': {'background_color': 0, 'margin': 0}, 'Field': {'background_color': 4280492319}, 'RadioButton': {'background_color': 0}, 'RadioButton:checked': {'background_color': 0}, 'RadioButton:hovered': {'background_color': 0}, 'RadioButton:pressed': {'background_color': 0}, 'RadioButton.Image': {'image_url': '${omni.kit.tool.asset_importer}/data/icons/radio_off.svg', 'color': 4288585374}, 'RadioButton.Image:checked': {'image_url': '${omni.kit.tool.asset_importer}/data/icons/radio_on.svg'}, 'RadioButton.Image:hovered': {'image_url': '${omni.kit.tool.asset_importer}/data/icons/radio_on.svg'}}
