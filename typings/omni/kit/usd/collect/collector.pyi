from __future__ import annotations
import asyncio as asyncio
import carb as carb
import enum
from enum import Enum
from enum import IntFlag
import hashlib as hashlib
import json as json
import omni as omni
from omni.kit.usd.collect.async_utils import _open_layer as aio_open_layer
from omni.kit.usd.collect.async_utils import _replace_all as aio_replace_all
from omni.kit.usd.collect.async_utils import _sub_all as aio_re_sub_all
from omni.kit.usd.collect.mdl_parser import MDLParser
from omni.kit.usd.collect.omni_client_wrapper import OmniClientWrapper
from omni.kit.usd.collect.utils import Utils
import os as os
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
from pxr import Usd
from pxr import UsdLux
from pxr import UsdShade
from pxr import UsdUtils
import sys as sys
import time as time
import traceback as traceback
import typing
__all__: list = ['CollectorStatus', 'CollectorFailureOptions', 'CollectorTaskType', 'CollectorException', 'Collector', 'DefaultPrimOnlyOptions', 'FlatCollectionTextureOptions', 'COLLECT_MAPPING_FILE_NAME']
class Collector:
    """
    Collector provides API to collect USD file with its dependencies that are scattered around different places.
    """
    @staticmethod
    def _Collector__get_external_references(*args, **kwargs):
        ...
    @staticmethod
    def _Collector__modify_external_references(*args, **kwds):
        ...
    @staticmethod
    def _Collector__open_and_analyze_layer(*args, **kwargs):
        ...
    @staticmethod
    def _Collector__open_and_analyze_mdl(*args, **kwargs):
        ...
    @staticmethod
    def _Collector__resolve_layer(*args, **kwargs):
        ...
    @staticmethod
    def _caculate_flat_target_path(*args, **kwds):
        ...
    @staticmethod
    def _calculate_target_path(*args, **kwds):
        ...
    @staticmethod
    def _collect_internal(*args, **kwargs):
        ...
    @staticmethod
    def _get_total_steps(*args, **kwargs):
        ...
    @staticmethod
    def collect(*args, **kwargs) -> typing.Tuple[bool, str]:
        """
        Collects stage in an asynchronous way.
        
                Args:
                    progress_callback (Callable[[int, int], None]): The progress callback that notifies the current progress in
                        (current_step, total_steps) style.
                    finish_callback (Callable[[], None]): Finish callback when task is done or cancelled.
        
                Returns:
                    Tuple[bool, str]: The success status and the path of the collected stage root if it exists.
                
        """
    def _Collector__add_copy_task(self, source, target, skip_if_existed = False, collect_item_key = None):
        ...
    def _Collector__add_layer_resolve_task(self, source_layer_path, target_layer):
        ...
    def _Collector__add_pending_read_paths(self, paths):
        ...
    def _Collector__add_read_task(self, path):
        ...
    def _Collector__add_source_target_mapping(self, source_path, target_path, overwrite_if_exists = False):
        ...
    def _Collector__append_checkpoint_to_url_if_possible(self, source_path):
        ...
    def _Collector__cancel_all_tasks(self):
        ...
    def _Collector__copy_asset(self, source_url, target_url, set_target_writable_if_read_only = False, collect_item_key = None):
        ...
    def _Collector__filter_url_with_exclusion_rules(self, url):
        ...
    def _Collector__generate_hash(self, stat):
        ...
    def _Collector__get_target_url(self, source_url):
        ...
    def _Collector__is_cancelled(self):
        ...
    def _Collector__is_source_path_mapped(self, source_path):
        ...
    def _Collector__mapping_source_path(self, source_path, parent_asset = None):
        ...
    def _Collector__populate_udim_textures(self, udim_texture_path):
        ...
    def _Collector__report_one_progress(self):
        ...
    def _Collector__report_one_total_step(self, step = 1):
        ...
    def _Collector__reset(self):
        ...
    def __init__(self, usd_path: str, collect_dir: str, usd_only: bool = False, flat_collection: bool = False, material_only: bool = False, failure_options = ..., skip_existing: bool = False, max_concurrent_tasks = 32, texture_option = ..., force_non_read_only = True, exclusion_rules = {}, default_prim_only = False, **kwargs):
        """
        Constructor.
        
                Args:
                    usd_path (str): The usd stage to be collected.
        
                    collect_dir (str): The target folder to collect the usd stage to.
        
                    usd_only (bool, Optional): Collects usd files only or not. If it's True, it will ignore all asset types except USD files. Default is False.
        
                    flat_collection (bool, Optional): Collects stage without keeping the original dir structure. Default is False.
        
                    material_only (bool, Optional): Collects material and textures only or not. If it's True, it will ignore all other asset types. Default is False.
                        If both `usd_only` and `material_only` are true, it will collect all asset types.
        
                    skip_existing (bool, Optional): If files already exist in the target location, don't copy them again. Default is False.
        
                    max_concurrent_tasks (int, Optional): The maximum concurrent tasks to run at the same time. Default is 32.
        
                    texture_option (FlatCollectionTextureOptions, Optional): Specifies how textures are grouped in flat collection mode.
                        This is to avoid name collision which results in textures overwriting each other in the cases where textures
                        for different assets are not uniquely named.
        
                    force_non_read_only (bool, Optional): If it's true and source file copied is read-only, it will set the target file writable.
                        By default, it's true, which means to make all copied files writable. For USD and MDL files, they will
                        always be writable after copy as it needs to be modified during collecting.
        
                    exclusion_rules (Dict[str, str], Optional): Collector will collect and re-map all dependencies if no exclusion rules are given.
                        It allows you to specify the rules to exclude specified URLs so they won't be collected, and provide
                        options to map them to new locations. Here is an example.
        
                        .. code-block:: python
        
                            {
                                "s3://test-path/": "/mount/test-path/",
                                "s3://another-path/": None
                            }
        
                        Here, it defines two rules to exclude the urls prefixed by the key.
                        The first rule will map those URLs prefixed with "s3://test-path/" into location "/mount/test-path/",
                        and the second one will keep those URLs untouched in the collected file.
        
                    default_prim_only (bool, Optional): If it's True, it will only collect the assets under the default prim, and only save default prim
                        in the main usd file. By default, it's false, which means to collect all the assets. See :class:`DefaultPrimOnlyOptions`
                        for more customizations.
        
                Keyword Args:
                    default_prim_option (DefaultPrimOnlyOptions, Optional): Specifies how to collect default prims when default_prim_only is True.
                        This option can be used to skip collecting assets that are not used in the stage composition.
                        By default, it only collects default prim for root layer. REMINDER: When the option is to collect default prim
                        only for all layers, it's likely that non-default prims in a layer are referenced in any layers and they are
                        removed which causes invalid references.
        
                    convert_usda_to_usdc (bool, Optional): If it's True, it will convert ascii USD files (.usda) to binary format (.usdc).
                        By default, it is False and keeps the original format for all USD files.
                
        """
    def _load_mapping_file(self):
        ...
    def _make_sure_unique_path(self, path):
        ...
    def _raise_or_log(self, path, error, force_raise = False):
        ...
    def _remove_all_materials_and_bindings(self, stage_path):
        ...
    def _remove_all_prims_except_default(self, target_layer):
        ...
    def _remove_prim_spec(self, layer: pxr.Sdf.Layer, prim_spec):
        ...
    def _save_mapping_file(self):
        ...
    def add_copy_task(self, source: str, target: str, skip_if_existed = False):
        """
        
                Internal. Adds a copy task that copies file from source to target.
        
                Args:
                    source (str): The source url to copy.
                    target (str): The target url to copy source url into.
                    skip_if_existed (bool, Optional): If it should skip copy when the target file exists already.
                
        """
    def add_write_task(self, target: str, content: typing.Union[str, bytes]):
        """
        
                Internal. Adds a write task that writes target file.
        
                Args:
                    target (str): The target url to write.
                    content: (Union[str, bytes]): The content to write. It could be str, or bytes.
                
        """
    def cancel(self):
        """
        Cancel the collector if it's in progress.
        """
    def destroy(self):
        """
        Destructor to release all resources.
        """
    def get_source_target_url_mapping(self) -> typing.Dict[str, str]:
        """
        
                Gets the mapping of all source files to target files. It returns valid
                value when collect task is done. See :func:`.get_status` to query
                collector status.
        
                Returns:
                    Dict[str, str]: A dict that key is the source url of files, and value is the target url of files.
                
        """
    def get_status(self) -> CollectorStatus:
        """
        
                Gets the collector status. See :class:`.CollectorStatus` for more details.
        
                Returns:
                    CollectorStatus: The current status of the collector.
                
        """
    def get_target_url(self, source_url: str) -> str:
        """
        
                Gets the target url that the source url is collected to. It returns valid
                value when collect task is done. See :func:`get_status` to query
                collector status.
        
                Args:
                    source_url (str): The source url to query.
        
                Returns:
                    str: The corresponding target url that the source url has been collected to.
                
        """
    def is_cancelled(self):
        """
        
                Collector is cancelled or not. REMINDER: This function is DEPRECATED. See :func:`.get_status` for more accurate status.
        
                Returns:
                    bool: Collection is cancelled or not.
                
        """
    def is_copy_skipped(self, source_url) -> bool:
        """
        
                Checkes if it skips copying source_url during collection.
                It returns valid value when collect task is done. See :func:`.get_status` to query
                collector status.
        
                Returns:
                    bool: Successful or not.
                
        """
    def is_finished(self):
        """
        
                Collect is done or not. It returns True no matter it's cancelled or successfully done.
                REMINDER: This function is DEPRECATED. See :func:`.get_status` for more accurate status.
        
                Returns:
                    bool: Collection is finished or not.
                
        """
    def open_or_create_layer(self, layer_path, clear = True):
        """
        Deprecated.
        """
    def wait_all_unfinished_tasks(self, all_completed = False):
        """
        Internal.
        """
    @property
    def collect_mapping_file_url(self):
        """
        
                The mapping file path. Mapping file records the collection history of this collector.
                It can help avoiding duplication in collection if the target file exists and is not changed.
                
        """
    @property
    def source_stage_url(self) -> str:
        """
        The source url to be collected.
        """
    @property
    def target_folder(self) -> str:
        """
        The target folder to collect assets into.
        """
class CollectorException(Exception):
    """
    General collector excpetion. See :class:`.CollectorFailureOptions` for options to customize exception behaviors.
    """
    def __init__(self, error: str):
        ...
    def __str__(self):
        ...
class CollectorFailureOptions(enum.IntFlag):
    """
    Options to customize failure options for collector.
    """
    EXTERNAL_USD_REFERENCES: typing.ClassVar[CollectorFailureOptions]  # value = <CollectorFailureOptions.EXTERNAL_USD_REFERENCES: 1>
    OTHER_EXTERNAL_REFERENCES: typing.ClassVar[CollectorFailureOptions]  # value = <CollectorFailureOptions.OTHER_EXTERNAL_REFERENCES: 4>
    SILENT: typing.ClassVar[CollectorFailureOptions]  # value = <CollectorFailureOptions.SILENT: 0>
class CollectorItem:
    """
    
        CollectorItem represents an item that's collected from the source. For each file collected from
        the source url, it has one corresponding record. This info can be used to check if it needs to
        re-collect the file or not.
        
    """
    @staticmethod
    def _from_dict(json_dict: dict):
        ...
    def __init__(self):
        ...
    def __str__(self) -> str:
        ...
    def _to_dict(self, collection_dir):
        ...
class CollectorStatus(enum.Enum):
    """
    Collector status.
    """
    CANCELLED: typing.ClassVar[CollectorStatus]  # value = <CollectorStatus.CANCELLED: 3>
    FINISHED: typing.ClassVar[CollectorStatus]  # value = <CollectorStatus.FINISHED: 2>
    IN_PROGRESS: typing.ClassVar[CollectorStatus]  # value = <CollectorStatus.IN_PROGRESS: 1>
    NOT_STARTED: typing.ClassVar[CollectorStatus]  # value = <CollectorStatus.NOT_STARTED: 0>
class CollectorTaskType(enum.Enum):
    """
    Internal. Task type of collector.
    """
    COPY_TASK: typing.ClassVar[CollectorTaskType]  # value = <CollectorTaskType.COPY_TASK: 2>
    READ_TASK: typing.ClassVar[CollectorTaskType]  # value = <CollectorTaskType.READ_TASK: 0>
    RESOLVE_TASK: typing.ClassVar[CollectorTaskType]  # value = <CollectorTaskType.RESOLVE_TASK: 3>
    WRITE_TASK: typing.ClassVar[CollectorTaskType]  # value = <CollectorTaskType.WRITE_TASK: 1>
class DefaultPrimOnlyOptions(enum.Enum):
    """
    Options for collecting USD with 'default prim only' mode.
    """
    ALL_LAYERS: typing.ClassVar[DefaultPrimOnlyOptions]  # value = <DefaultPrimOnlyOptions.ALL_LAYERS: 1>
    ROOT_LAYER_ONLY: typing.ClassVar[DefaultPrimOnlyOptions]  # value = <DefaultPrimOnlyOptions.ROOT_LAYER_ONLY: 0>
class FlatCollectionTextureOptions(enum.Enum):
    """
    Collection options for textures under 'Flat Collection' mode.
    """
    BY_MDL: typing.ClassVar[FlatCollectionTextureOptions]  # value = <FlatCollectionTextureOptions.BY_MDL: 0>
    BY_USD: typing.ClassVar[FlatCollectionTextureOptions]  # value = <FlatCollectionTextureOptions.BY_USD: 1>
    FLAT: typing.ClassVar[FlatCollectionTextureOptions]  # value = <FlatCollectionTextureOptions.FLAT: 2>
COLLECT_MAPPING_FILE_NAME: str = '.collect.mapping.json'
COLLECT_MAPPING_FILE_RECORDS_KEY: str = 'file_records'
COLLECT_MAPPING_FILE_VERSION: str = '1.0'
COLLECT_MAPPING_FILE_VERSION_KEY: str = 'version'
