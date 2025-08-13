from __future__ import annotations
import enum
from enum import IntEnum
from omni.kit.tool.asset_importer.file_picker import FilePicker
from omni.kit.tool.asset_importer.filebrowser import FileBrowserMode
from omni.kit.tool.asset_importer.filebrowser import FileBrowserSelectionType
from omni.kit.tool.asset_importer.utils import Utils
from omni.kit.window import content_browser as content
from omni import ui
import omni.ui._ui
import typing
import webbrowser as webbrowser
__all__: list[str] = ['Destination', 'FileBrowserMode', 'FileBrowserSelectionType', 'FilePicker', 'Format', 'IntEnum', 'SharedImportOptions', 'SharedImportOptionsBuilder', 'Utils', 'content', 'ui', 'webbrowser']
class Destination(enum.IntEnum):
    Reference: typing.ClassVar[Destination]  # value = <Destination.Reference: 1>
    Stage: typing.ClassVar[Destination]  # value = <Destination.Stage: 0>
    @classmethod
    def __new__(cls, value):
        ...
    def __format__(self, format_spec):
        ...
class Format(enum.IntEnum):
    USD: typing.ClassVar[Format]  # value = <Format.USD: 0>
    USDA: typing.ClassVar[Format]  # value = <Format.USDA: 1>
    USDC: typing.ClassVar[Format]  # value = <Format.USDC: 2>
    USDZ: typing.ClassVar[Format]  # value = <Format.USDZ: 3>
    @classmethod
    def __new__(cls, value):
        ...
    def __format__(self, format_spec):
        ...
class SharedImportOptions:
    def __init__(self) -> None:
        ...
class SharedImportOptionsBuilder:
    def __init__(self):
        ...
    def _build_advanced_options(self, show_advanced_options: bool, destination_collection: omni.ui._ui.RadioCollection):
        """
        
                If supported, display advanced converter options
                Args:
                    show_advanced_options (bool): True if converter supports USD Stage Cache
                    destination_collection (ui.RadioCollection): Radio Collection
                
        """
    def _build_dest_header(self, _: bool, title: str):
        ...
    def _build_ref_in_stage_option(self):
        """
        
                If the Import workflow is True, do not display checkbox for adding reference in current stage
                
        """
    def _check_workflow(self, is_workflow_import):
        """
        
                Check user-selected workflow. If 'Import' workflow selected, set add_reference to true by default
                
        """
    def _get_current_dir_in_content_window(self):
        ...
    def _open_scene_optimizer_ui_doc(self):
        ...
    def _radio_collection_value_changed(self, model: omni.ui._ui.SimpleIntModel) -> None:
        ...
    def _select_picked_file_callback(self, paths):
        ...
    def _select_picked_folder_callback(self, paths):
        ...
    def _set_persist_value(self, model: omni.ui._ui.SimpleBoolModel):
        """
        
                Callback. Set persist value when 'Convert to USD' workflow is selected
                
        """
    def _show_file_picker(self):
        ...
    def _show_folder_picker(self):
        ...
    def build_ui(self, is_workflow_import, multiselect, show_dest_frame, show_advanced_options, show_scene_optimizer_config_frame):
        ...
    def destroy(self):
        ...
    def get_options(self):
        ...
    def set_default_target_file_name(self, file_name: str):
        ...
    def set_default_target_folder(self, folder: str):
        ...
