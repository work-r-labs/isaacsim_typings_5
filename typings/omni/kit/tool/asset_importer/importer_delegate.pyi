from __future__ import annotations
import omni as omni
from omni.kit.tool.asset_importer.builtin_importer import BuiltinImporter
from omni.kit.tool.asset_importer.builtin_options_builder import BuiltinImporterOptionsBuilder
import os as os
from pxr import Sdf
import re as re
__all__ = ['AbstractImporterDelegate', 'BuiltInImporterDelegate', 'BuiltinImporter', 'BuiltinImporterOptionsBuilder', 'Sdf', 'omni', 'os', 're']
class AbstractImporterDelegate:
    """
    
        AbstractImporterDelegate is abstract class for extending
        external importers into asset_importer framework.
        
    """
    def added_reference(self, assets: typing.Dict[str, typing.Tuple[str, pxr.Sdf.Path]]):
        """
        The post process to assets that are imported to current stage.
                It will only be called if it's imported from menu `File -> Import`.
        
                Args:
                    asset_pair: The dict of all assets that successfully imported and added
                    as references. The key is the original asset path to be converted,
                    and value is a tuple, of which the first element is the target path this
                    asset is converted to, and the second one is prim path that the converted
                    USD is added as reference.
                
        """
    def build_options(self, paths: typing.List[str]) -> None:
        """
        Options pane builder for file picker after paths are selected.
                It will only include those paths that are supported by this importer
                filtered with regex filters.
        
                Args:
                    paths (List[str]): The list of selected paths from file picker.
                
        """
    def convert_assets(self, paths: typing.List[str], **kargs) -> typing.Dict[str, typing.Optional[str]]:
        """
        The real worker to convert assets.
                It will only include those paths that are supported by this importer
                filtered with regex filters.
        
                Args:
                    paths (List[str]): The list of selected paths from file picker.
                    **kwargs: Optional arguments. Following args are supported currently:
                        add_reference: If it will be added into stage after convert.
        
                Returns:
                    Dict[str, Union[str, None]]: The key is the asset path to be converted, and
                    the value is the target path or stage ID within UsdStageCache that this asset converted to.
                    If value is None, it means it's failed to be converted.
                
        """
    def is_supported_format(self, path: str) -> bool:
        """
        If the asset is supported by this importer.
        """
    def show_destination_frame(self):
        """
        Whether the option panel show destination frame
        """
    def show_scene_optimizer_config_frame(self):
        """
        Whether the option panel show scene optimizer config frame
        """
    def supports_usd_stage_cache(self):
        """
        Whether the importer can write to UsdStageCache for us to retrieve data from
        """
    @property
    def filter_descriptions(self) -> typing.List[str]:
        """
        List of descriptions for each regex filter. It will be
                used for filter description in the file picker.
        
                Args:
                    None
        
                Return:
                    List of regex descriptions.
                
        """
    @property
    def filter_regexes(self) -> typing.List[str]:
        """
        List of regex filters of this importer supported.
                It's provided as a list because it's possible that the importer
                will support multiple formats and share the same options list.
        
                Args:
                    None
        
                Return:
                    List of regex strings.
                
        """
    @property
    def name(self) -> str:
        ...
class BuiltInImporterDelegate(AbstractImporterDelegate):
    def __init__(self, usd_context, builtin_importer: omni.kit.tool.asset_importer.builtin_importer.BuiltinImporter, filter_regexes: typing.List[str], filter_descriptions: typing.List[str]) -> None:
        ...
    def added_reference(self, assets: typing.Dict[str, typing.Tuple[str, pxr.Sdf.Path]]):
        ...
    def build_options(self, paths: typing.List[str]) -> None:
        ...
    def convert_assets(self, paths: typing.List[str], **kargs) -> typing.Dict[str, typing.Optional[str]]:
        ...
    def destroy(self):
        ...
    def set_default_target_folder(self, folder: str):
        ...
    @property
    def filter_descriptions(self) -> typing.List[str]:
        ...
    @property
    def filter_regexes(self) -> typing.List[str]:
        ...
    @property
    def name(self) -> str:
        ...
