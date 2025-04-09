from __future__ import annotations
import carb as carb
import inspect as inspect
from omni.kit import notification_manager as nm
import omni.kit.tool.asset_importer.importer_delegate
from omni.kit.tool.asset_importer.importer_delegate import AbstractImporterDelegate
from omni.kit.tool.asset_importer.importer_delegate import BuiltInImporterDelegate
from omni.kit.tool.asset_importer.shared_options_builder import SharedImportOptionsBuilder
from omni.kit.usd.layers._impl.extension import get_layers
from omni import ui
from pathlib import Path
from pxr import Sdf
__all__ = ['AbstractImporterDelegate', 'BuiltInImporterDelegate', 'ImportersManager', 'OPTIONS_STYLE', 'Path', 'Sdf', 'SharedImportOptionsBuilder', 'carb', 'get_layers', 'inspect', 'nm', 'ui']
class ImportersManager:
    def __init__(self, usd_context, buitin_importer):
        ...
    def add_importer(self, importer_delegate: omni.kit.tool.asset_importer.importer_delegate.AbstractImporterDelegate):
        ...
    def added_references(self, assets: typing.Dict[str, typing.Tuple[str, pxr.Sdf.Path]]):
        ...
    def build_options_pane(self, paths: typing.List[str], add_reference_to_stage: bool = True):
        ...
    def convert_assets(self, paths: typing.List[str], add_reference = False) -> typing.Dict[str, typing.Optional[str]]:
        ...
    def destroy(self):
        ...
    def get_all_filters(self) -> typing.Tuple[typing.List[str], typing.List[str]]:
        ...
    def is_supported_format(self, path: str):
        ...
    def remove_importer(self, importer):
        ...
    def set_builtin_importer_default_target_file_name(self, paths: str):
        ...
    def set_builtin_importer_default_target_folder(self, folder: str):
        ...
OPTIONS_STYLE: dict = {'Button.Image::folder': {'image_url': 'resources/glyphs/folder.svg', 'color': 4288585374, 'image_width': 20, 'image_height': 20, 'background_color': 0}, 'Button.Image::folder:hovered': {'image_url': 'resources/glyphs/folder_open.svg'}, 'Button::folder': {'background_color': 0, 'margin': 0}, 'Field': {'background_color': 4280492319}, 'RadioButton': {'background_color': 0}, 'RadioButton:checked': {'background_color': 0}, 'RadioButton:hovered': {'background_color': 0}, 'RadioButton:pressed': {'background_color': 0}, 'RadioButton.Image': {'image_url': '${omni.kit.tool.asset_importer}/data/icons/radio_off.svg', 'color': 4288585374}, 'RadioButton.Image:checked': {'image_url': '${omni.kit.tool.asset_importer}/data/icons/radio_on.svg'}, 'RadioButton.Image:hovered': {'image_url': '${omni.kit.tool.asset_importer}/data/icons/radio_on.svg'}}
