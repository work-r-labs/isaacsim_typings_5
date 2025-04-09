from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.client.utils import utils as clientutils
from omni.kit import asset_converter
from omni.kit.asset_converter.impl.omni_client_wrapper import OmniClientWrapper
from omni.kit import notification_manager as nm
from omni.kit.tool.asset_importer.progress_popup import ProgressPopup
from omni.kit.tool.asset_importer.utils import Utils
from omni.kit.widget.prompt.prompt import PromptButtonInfo
from omni.kit.widget.prompt.prompt import PromptManager
from omni.kit.window import content_browser as content
import os as os
from pxr import Sdf
__all__ = ['BuiltinImporter', 'OmniClientWrapper', 'ProgressPopup', 'PromptButtonInfo', 'PromptManager', 'Sdf', 'Utils', 'asset_converter', 'asyncio', 'carb', 'clientutils', 'content', 'nm', 'omni', 'os']
class BuiltinImporter:
    def _refresh_current_directory(self):
        ...
    def _show_waiting_popup_convert(self):
        ...
    def _show_waiting_popup_upload(self):
        ...
    def create_import_task(self, converting_assets: bool, asset_absolute_paths: typing.List[str], asset_relative_paths: typing.List[str], output_dir: str, output_file_name: str, output_file_format: str, asset_upload_context: omni.kit.asset_converter.impl.context.AssetConverterContext):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
