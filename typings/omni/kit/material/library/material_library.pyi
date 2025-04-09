"""
Material library utility functions.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import dataclasses
from dataclasses import dataclass
import enum
from enum import Enum
from enum import IntEnum
import fnmatch as fnmatch
import functools as functools
from itertools import chain
import json as json
import omni as omni
from omni.kit.material.library.drop_material import _drop_material
from omni.kit.material.library.material_actions import deregister_actions
from omni.kit.material.library.material_actions import register_actions
from omni.kit.material.library.material_extensions import MaterialUIExtensions
from omni.kit.material.library.mdl_schema import MDLSchema
from omni.kit.material.library.multi_descendents_dialog import _multi_descendents_dialog
import os as os
from pathlib import Path
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
from pxr import Usd
import pxr.Usd
from pxr import UsdShade
import re as re
import typing
__all__: list = ['bind_material_to_selected_prims', 'get_material_prim_path', 'create_mdl_material', 'create_mtlx_material', 'get_material_filename_from_prim', 'CreateAndBindMdlMaterialFromLibrary', 'CreateAndBindMtlxSurfaceFromLibrary', 'CreateAndBindPreviewSurfaceFromLibrary', 'CreateAndBindPreviewSurfaceTextureFromLibrary', 'MaterialLibraryExtension', 'get_mdl_lib_paths', 'get_mdl_lib_paths_private', 'get_mdl_usd_source_asset_list', 'get_material_hidden_list', 'get_material_show_list', 'get_mdl_list_async', 'get_mdl_list', 'add_material_list_refresh_callback', 'remove_material_list_refresh_callback', 'delayed_material_list_refresh', 'add_material_list_item', 'remove_material_list_item', 'material_list_refresh', 'get_material_list', 'custom_material_dialog', 'get_instance', 'get_subidentifier_from_material', 'get_subidentifier_from_mdl', 'drop_material', 'multi_descendents_dialog', 'remove_mdl_from_cache', 'get_material_enums', 'bind_material_to_prims_dialog', 'add_usd_source_asset_path_to_mtl_lib', 'remove_usd_source_asset_path_from_mtl_lib', 'add_to_mtl_lib', 'remove_from_mtl_lib', 'get_cache_filename']
class CreateAndBindMdlMaterialFromLibrary(omni.kit.commands.command.Command):
    """
    
        Creates material prim from Core MDL Library.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, mdl_name: str, mtl_name: str = '', mtl_created_list: list = None, bind_selected_prims: list = False, select_new_prim: bool = True, prim_name: str = '', on_created_fn: callable = None):
        """
        
                Creates material prim from Core MDL Library, and bind to provided prim list.
        
                Args:
                    mdl_name (str): MDL name from Core MDL Library.
                    mtl_name (str): The material name from MDL. It's also the sub-identifier to be used for the shader.
                                    If `prim_name` param is not specified, it will also be used as the prim_name. If mtl_name is empty,
                                    it will use file name of `mdl_name` (without extension) by default.
                    mtl_created_list (list): Created prims with get added to this list.
                    bind_selected_prims (List[Sdf.Path]): Prims to be bound to the newly created material prim.
                    select_new_prim: If it's to select the newly created material prim.
                    prim_name (str): The prim name to be created. It will be created with path "/$RootPrimName/Looks/$prim_name".
                                    If prim_name is not specified, it will use `mtl_name` instead.
                    on_created_fn (callable): function called when material prim is created & attributes are loaded
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateAndBindMtlxSurfaceFromLibrary(omni.kit.commands.command.Command):
    """
    
        Creates MaterialX surface material prim.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, mtlx_id: str = None, mtl_name: str = None, mtl_created_list: list = None, bind_selected_prims: list = False):
        """
        
                Creates MaterialX surface material prim.
        
                Args:
                    mtlx_id (str): ID from MaterialX node library. It must be a surface shader node.
                    mtl_name (str): The material prim name.
                    mtl_created_list (list): List a add created prim to.
                    bind_selected_prims (list): List of prims to bind materials to.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateAndBindPreviewSurfaceFromLibrary(omni.kit.commands.command.Command):
    """
    
        Creates PreviewSurface material prim.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, mtl_created_list: list = None, bind_selected_prims: list = False):
        """
        
                Creates PreviewSurface material prim.
        
                Args:
                    mtl_created_list (list): List a add created prim to.
                    bind_selected_prims (list): List of prims to bind materials to.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateAndBindPreviewSurfaceTextureFromLibrary(omni.kit.commands.command.Command):
    """
    
        Creates PreviewSurfaceTexture material prim.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, mtl_created_list: list = None, bind_selected_prims: list = False):
        """
        
                Creates PreviewSurfaceTexture material prim.
        
                Args:
                    mtl_created_list (list): List a add created prim to.
                    bind_selected_prims (list): List of prims to bind materials to.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class MaterialItem:
    """
    MaterialItem(name: str, create_fn: <built-in function callable> = None, block: bool = True, submenu: str = '', is_private: bool = False)
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'name': Field(name='name',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'create_fn': Field(name='create_fn',type=<built-in function callable>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'block': Field(name='block',type=<class 'bool'>,default=True,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'submenu': Field(name='submenu',type=<class 'str'>,default='',default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'is_private': Field(name='is_private',type=<class 'bool'>,default=False,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('name', 'create_fn', 'block', 'submenu', 'is_private')
    block: typing.ClassVar[bool] = True
    create_fn = None
    is_private: typing.ClassVar[bool] = False
    submenu: typing.ClassVar[str] = ''
    def __eq__(self, other):
        ...
    def __getitem__(self, key):
        ...
    def __init__(self, name: str, create_fn: callable = None, block: bool = True, submenu: str = '', is_private: bool = False) -> None:
        ...
    def __repr__(self):
        ...
class MaterialLibraryExtension(omni.ext._extensions.IExt):
    """
    Material extension class.
    """
    class SubIDEntry:
        """
        SubIDEntry is helper class to assist with neuraylib data and name string.
        """
        def __init__(self, name: str, annotations: dict, is_material: bool):
            """
            Initialize class function.
            
                        Args:
                            name (str): Name of material  sub-identifier.
                            annotations (dict): Dictionary of values from neuraylib for this material.
                            is_material (bool): Is this a material entry? Value from neuraylib.
                        
            """
        def __repr__(self) -> str:
            ...
        def __str__(self) -> str:
            ...
        def replace(self, oldvalue, newvalue):
            """
            String replace on material name.
            
                        Args:
                            oldvalue (str): The string to search for.
                            newvalue (str): The string to replace the `oldvalue` with.
            
                        Returns:
                            (str): new string.
                        
            """
    _MaterialLibraryExtension__StaticDataModel = MaterialLibraryExtension.__StaticDataModel
    @staticmethod
    def _create_material_and_assign(create_fn, *_):
        ...
    @staticmethod
    def _custom_material_dialog(static_data: MaterialLibraryExtension.__StaticDataModel, absolute_mdl_path: str, on_complete_fn: callable, bind_prim_paths: list):
        ...
    @staticmethod
    def _on_create_custom_mdl_material(mtl_created_list = None, bind_selected_prims = True):
        ...
    @staticmethod
    def _on_create_custom_mtlx_material(mtl_created_list = None, bind_selected_prims = True):
        ...
    @staticmethod
    def _on_create_mdl_material(mdl_url: str, mdl_name: str, mtl_name: str, mtl_created_list: list = None, bind_selected_prims: list = False, prim_name: str = ''):
        ...
    @staticmethod
    def _on_create_mtlx_material(mtlx_id: str, mtl_name: str, mtl_created_list: list = None, bind_selected_prims: list = False):
        ...
    @staticmethod
    def _on_create_preview_surface(mtl_created_list = None, bind_selected_prims = True):
        ...
    @staticmethod
    def _on_create_preview_surface_texture(mtl_created_list = None, bind_selected_prims = True):
        ...
    @staticmethod
    def _on_selected_mdl(filename: str, dirname: str, bind_prim_paths = list()):
        ...
    @staticmethod
    def _on_selected_mtlx(filename: str, dirname: str, bind_prim_paths = list()):
        ...
    @staticmethod
    def _show_mdl_importer(title: str, click_apply_fn: callable = None):
        ...
    @staticmethod
    def _show_mtlx_importer(title: str, click_apply_fn: callable = None):
        ...
    def _MaterialLibraryExtension__preload_base_material_subids(self, on_complete_fn: callable = None, only_preload: str = '', spreadload: bool = False):
        ...
    def _MaterialLibraryExtension__process_rtx_neuraylib(self, mdl_file: str, module_process_fn: callable):
        ...
    def __init__(self):
        ...
    def _build_menus(self):
        ...
    def _free_rtx_mdl(self):
        ...
    def _preload_base_material(self):
        ...
    def _preload_rtx_mdl(self):
        ...
    def _refresh_create_menu(self):
        ...
    def _register_material_actions(self):
        ...
    def _register_page(self):
        ...
    def _reload_material_subids(self, new_lib_paths, event_type):
        ...
    def _remove_create_menu(self):
        ...
    def _show_alert_message(self, message):
        ...
    def _unregister_page(self):
        ...
    def get_cache_filename(self):
        ...
    def get_subidentifier_from_material(self, prim, on_complete_fn: callable, use_functions: bool = False, show_alert: bool = False):
        """
        
                get sub-identifier list from material prim asynchronously.
        
                Args:
                    prim (Usd.Prim): prim to get material & material sub-identifiers from.
                    on_complete_fn (callable): function to call with list of sub-identifier when completed.
                    use_functions (bool): if True only list materials and not functions otherwise return all sub-identifiers.
                    show_alert (bool): show alert if bad material.
        
                Returns:
                    (list): list of sub-identifier
        
                
        """
    def get_subidentifier_from_mdl(self, mdl_file: str, on_complete_fn: callable = None, use_functions: bool = False, show_alert: bool = False):
        """
        
                get sub-identifier list from mdl file asynchronously.
        
                Args:
                    mdl_file (str): mdl_file to get material sub-identifiers from.
                    on_complete_fn (callable): function to call with list of sub-identifier when completed.
                    use_functions (bool): if True only list materials and not functions otherwise return all sub-identifiers.
                    show_alert (bool): show alert if bad material.
        
                Returns:
                    (list): list of sub-identifier
        
                
        """
    def on_shutdown(self):
        """
        Shutdown function
        """
    def on_startup(self, ext_id):
        """
        Startup function
        
                Args:
                    ext_id (str): Extension id.
                
        """
    def remove_mdl_from_cache(self, shader_prim_path: str):
        """
        
                Remove material from cache. Call by Material Watcher when re-loading modified mdl files.
        
                Args:
                    shader_prim_path (str): material prim path to remove from cache.
                
        """
class ReadyState(enum.IntEnum):
    """
    An enumeration.
    """
    ALL_READY: typing.ClassVar[ReadyState]  # value = <ReadyState.ALL_READY: 3>
    APP_READY: typing.ClassVar[ReadyState]  # value = <ReadyState.APP_READY: 2>
    JSON_READY: typing.ClassVar[ReadyState]  # value = <ReadyState.JSON_READY: 1>
    NOT_READY: typing.ClassVar[ReadyState]  # value = <ReadyState.NOT_READY: 0>
def add_material_list_item(name: str, on_call_fn: callable, refresh: bool = True):
    """
    
        Add custom material, this will also get added to context menu Create menu.
    
        Args:
            name (str): Material name.
            on_call_fn (callable): Material created callback.
            refresh (bool): Refresh UI Flag.
        
    """
def add_material_list_refresh_callback(on_refresh_fn: callable):
    """
    
        Add callback to trigger when material library UI refreshes.
    
        Args:
            on_refresh_fn (callable): Callback to be called when UI refreshes.
        
    """
def add_to_mtl_lib(folder_paths: list[str], is_private: bool = False) -> list[str]:
    """
    
        Add custom folder to list of folders to generate context menu "Create/Materials" from.
    
        Args:
            folder_paths (list): List of folder paths to add.
            is_private: (bool): Actions start with "_" to be excluded from actions_api.md
        Returns:
            (list): Updated list of folders used to generate context menu "Create/Materials".
        
    """
def add_usd_source_asset_path_to_mtl_lib(source_asset_path: str, source_asset_subid: str, group_name: str, submenu_name: str = None, display_name: str = None):
    """
    
        Adds a material to the context menu.
    
        Args:
            source_asset_path (str): The USD Identifier corresponding to the source asset path of a USD Shader Node.
            source_asset_subid (str): The USD Sub-identifier corresponding to the source asset sub-identifier of a USD Shader Node.
            group_name (str): The menu entries are grouped. Select an existing one or creates a new group.
            submenu_name (str): Entries can be sorted into a submenu. If not set, the entry will appear top-level.
            display_name (str): Display name of the entry in the menu. If not set, a default value will be used.
    
        Returns:
            (bool): True on success otherwise False.
        
    """
def bind_material_to_prims_dialog(stage: pxr.Usd.Stage, prims: list) -> None:
    """
    
        Show dialog to user, so they an select material and bind to prims.
    
        Args:
            stage (Usd.Stage): stage
            prims (list): list of prims to bind to.
        
    """
def bind_material_to_selected_prims(material_prim_path: pxr.Sdf.Path, paths: list):
    """
    
        Bind material to selected prims.
    
        Args:
            material_prim_path (Sdf.Path): Prim path of material.
            paths (list): List of prims to bind material to.
    
        
    """
def create_mdl_material(stage: pxr.Usd.Stage, mtl_url: str, mtl_name: str, on_create_fn: callable, mtl_real_name: str = ''):
    """
    
        Create material prim from .mdl file.
    
        Args:
            stage (Usd.Stage): stage.
            mtl_url (str): path of material mdl file.
            mtl_name (str): Prim material name to create.
            on_create_fn (callable): Callback when material is created.
            mtl_real_name (str): Optional override for `mtl_name`
    
        Returns:
            (str): new material path or None.
        
    """
def create_mtlx_material(stage: pxr.Usd.Stage, mtlx_url: str, on_create_fn: callable, base_name: str = ''):
    """
    
        Create materialX prim from .mdl file.
    
        Args:
            stage (Usd.Stage): stage.
            mtlx_url (str): path of materialX mdl file.
            on_create_fn (callable): Callback when materialX is created.
            base_name (str): Optional override for materialX name
    
        Returns:
            (str): new materialX path or None.
        
    """
def custom_material_dialog(mdl_path: str, on_complete_fn: callable = None, bind_prim_paths: list = list()):
    """
    
        Show custom material dialog.
    
        Args:
            mdl_path (str): Mdl path.
            on_complete_fn (callable): Function called when material dialog Cleated button is clicked.
            bind_prim_paths (list): List of prims path to bind material to.
        
    """
def delayed_material_list_refresh():
    """
    
        Async refresh material_list.
        
    """
def drop_material(prim_path: str, model_path: str, apply_material_fn: callable):
    """
    
        Build bind material menu UI.
    
        Args:
            prim_path (str): Prim path.
            model_path (str): Model Path:
            apply_material_fn (callable): Bind material callback.
        
    """
def get_cache_filename():
    ...
def get_material_enums():
    """
    
        Get material Enum data.
    
        Returns:
            (dict): material enum dictionary.
        
    """
def get_material_filename_from_prim(prim: pxr.Usd.Prim) -> str:
    """
    
        Gets material thumbnail image path for prim.
    
        Args:
            prim (Usd.Prim): Prim to get thumbnail image path for.
    
        Returns:
            (str): Thumbnail image path, image path may not exist.
        
    """
def get_material_hidden_list():
    """
    
        Gets list of hidden materials, which is /exts/omni.kit.material.library/ui_hidden_list.
        
    """
def get_material_list():
    """
    
        Builds a list of materials and other information, used by omni.kit.context_menu and omni.kit.menu.create
    
        Returns:
            (list) list of lists:
                sub-list is either:
                    "GROUP" & material group name.
                    Material name, create material function, blocking parameter passed to create_material_and_assign, list of material sub identifiers.
        
    """
def get_material_prim_path(material_prim_name: str):
    """
    
        Make valid material prim path from material_prim_name.
    
        Args:
            material_prim_name (str): Prim path of material.
    
        Returns:
            (str): Path of "/Looks" prim
            (Sdf.Path): Valid material prim path.
        
    """
def get_material_show_list():
    """
    
        Get material show list, this is used to create a subset of materials for `get_material_list` function.
        Uses "/exts/omni.kit.material.library/ui_show_list"
        
    """
def get_mdl_lib_paths():
    """
    
        Get material library paths. Which is "/exts/omni.kit.material.library/lib_paths"
    
        Returns:
            (list): list of paths
        
    """
def get_mdl_lib_paths_private():
    """
    
        Get material library paths with additional private info. Which is "/exts/omni.kit.material.library/lib_paths"
    
        Returns:
            (list): list of tuple(path, is_private)
        
    """
def get_mdl_list(use_hidden = False, get_private = False):
    """
    
        Gets list of materials asynchronously. Can return [] if mdl_list_cache is not complete yet.
    
        Args:
            use_hidden (bool): Include hidden materials. See `get_material_hidden_list`
    
        Returns:
            (list): list of materials
        
    """
def get_mdl_list_async(use_hidden = False, wait_for_ready = True, get_private = False):
    """
    
        Gets list of materials asynchronously. Can wait if mdl_list_cache is not complete yet.
    
        Args:
            use_hidden (bool): Include hidden materials. See `get_material_hidden_list`
    
        Returns:
            (list): list of materials
        
    """
def get_mdl_usd_source_asset_list():
    """
    
        Get material source asset file, from "/exts/omni.kit.material.library/usd_source_asset_list".
        used by `add_usd_source_asset_path_to_mtl_lib` function.
        
    """
def get_path_private_state(path: str):
    ...
def get_private_marker(item):
    ...
def get_subidentifier_from_material(prim: pxr.Usd.Prim, on_complete_fn: callable, use_functions: bool = False, show_alert: bool = False):
    """
    
        get sub-identifier list from material prim asynchronously.
    
        Args:
            prim (Usd.Prim): prim to get material & material sub-identifier from.
            on_complete_fn (callable): function to call with list of sub-identifier when completed.
            use_functions (bool): if True only list materials and not functions otherwise return all sub-identifiers.
            show_alert (bool): show alert if bad material.
    
        Returns:
            (list): list of sub-identifier
    
        
    """
def get_subidentifier_from_mdl(mdl_file: str, on_complete_fn: callable = None, use_functions: bool = False, show_alert: bool = False):
    """
    
        get sub-identifier list from mdl file asynchronously.
    
        Args:
            mdl_file (str): mdl_file to get material sub-identifiers from.
            on_complete_fn (callable): function to call with list of sub-identifier when completed.
            use_functions (bool): if True only list materials and not functions otherwise return all sub-identifiers.
            show_alert (bool): show alert if bad material.
    
        Returns:
            (list): list of sub-identifier
    
        
    """
def material_list_refresh():
    """
    
        Remove custom material, this will also get removed from context menu Create menu.
    
        Args:
            name (str): Material name.
            refresh (bool): Refresh UI Flag.
        
    """
def multi_descendents_dialog(prim_paths: list, on_click_fn: callable):
    """
    
        Show multi descendants dialog.
    
        Args:
            prim_paths (list): Prim path list.
            apply_material_fn (callable): Prim selected callback.
        
    """
def remove_from_mtl_lib(folder_paths: list[str]) -> list[str]:
    """
    
        Remove custom folder to list of folders to generate context menu "Create/Materials" from.
    
        Args:
            folder_paths (list): List of folder paths to remove.
    
        Returns:
            (list): Updated list of folders usded to generate context menu "Create/Materials".
        
    """
def remove_material_list_item(name: str, refresh: bool = True):
    """
    
        Remove custom material, this will also get removed from context menu Create menu.
    
        Args:
            name (str): Material name.
            refresh (bool): Refresh UI Flag.
        
    """
def remove_material_list_refresh_callback(on_refresh_fn: callable):
    """
    
        Remove callback to trigger when material library UI refreshes.
    
        Args:
            on_refresh_fn (callable): Callback to be removed.
        
    """
def remove_mdl_from_cache(shader_prim_path: str):
    """
    
        Remove material from cache. Call by Material Watcher when re-loading modified mdl files.
    
        Args:
            shader_prim_path (str): material prim path.
        
    """
def remove_usd_source_asset_path_from_mtl_lib(source_asset_path: str, source_asset_subid: str):
    """
    
        Removes a material from the context menu.
    
        Args:
            source_asset_path (str):    The USD Identifier corresponding to the source asset path of a USD Shader Node.
            source_asset_subid (str):   The USD Sub-identifier corresponding to the source asset sub-identifier of a USD Shader Node.
        
    """
def set_path_private_state(path: str, is_private: bool):
    ...
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
SETTING_MATERIAL_LIBRARY_LIB_PATHS: str = '/exts/omni.kit.material.library/lib_paths'
SETTING_MATERIAL_LIBRARY_USD_SOURCE_ASSET_LIST: str = '/exts/omni.kit.material.library/usd_source_asset_list'
full_subid_list: bool = True
material_instance: MaterialLibraryExtension  # value = <omni.kit.material.library.material_library.MaterialLibraryExtension object>
material_ready_state: int = 3
mdl_list_cache: dict = {'all': [['OmniGlass_Opacity', '/home/chris/isaacsim/kit/mdl/core/Base/OmniGlass_Opacity.mdl', None, False], ['OmniSurface_IncandescentBulb', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_BrushedMetal', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Chrome', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Copper', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Gold', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Foam', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Rubber', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_CarPaint', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_CarPaintMetallic', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_GlossyPaint', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_TwoToneCarPaint', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Default', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_PeanutButter', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_SkimMilk', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_WholeMilk', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Ceramic', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Clay', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Plastic', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Skin_1', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Skin_2', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Skin_3', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Skin_4', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Velvet', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Honey', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_MapleSyrup', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_OrangeJuice', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_DustedGlass', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_FrostedGlass', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Glass', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Blood', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Bubble', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Wax', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Polyethylene', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Diamond', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Jade', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_ClearWater', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_DeepWater', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniHair_Blonde', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHairPresets.mdl', 'OmniHairPresets', False], ['OmniHair_Brown', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHairPresets.mdl', 'OmniHairPresets', False], ['OmniHair_Auburn', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHairPresets.mdl', 'OmniHairPresets', False], ['OmniHair_Black', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHairPresets.mdl', 'OmniHairPresets', False], ['OmniHair_Wet', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHairPresets.mdl', 'OmniHairPresets', False], ['SimPBR_Translucent', '/home/chris/isaacsim/kit/mdl/core/Base/SimPBR_Translucent.mdl', None, False], ['OmniGlass', '/home/chris/isaacsim/kit/mdl/core/Base/OmniGlass.mdl', None, False], ['OmniSurfaceBlend', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfaceBlend.mdl', None, False], ['OmniEmissive', '/home/chris/isaacsim/kit/mdl/core/Base/OmniEmissive.mdl', None, False], ['OmniSurfaceLite', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfaceLite.mdl', None, False], ['OmniPBR_Opacity', '/home/chris/isaacsim/kit/mdl/core/Base/OmniPBR_Opacity.mdl', None, False], ['OmniPBR_ClearCoat', '/home/chris/isaacsim/kit/mdl/core/Base/OmniPBR_ClearCoat.mdl', None, False], ['OmniPBR_ClearCoat_Opacity', '/home/chris/isaacsim/kit/mdl/core/Base/OmniPBR_ClearCoat_Opacity.mdl', None, False], ['SimPBR_Model', '/home/chris/isaacsim/kit/mdl/core/Base/SimPBR_Model.mdl', None, False], ['OmniPBR', '/home/chris/isaacsim/kit/mdl/core/Base/OmniPBR.mdl', None, False], ['SimPBR', '/home/chris/isaacsim/kit/mdl/core/Base/SimPBR.mdl', None, False], ['OmniHair', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHair.mdl', None, False], ['OmniSurface', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurface.mdl', None, False], ['OmniPBRBase', '/home/chris/isaacsim/kit/mdl/core/Base/OmniPBRBase.mdl', None, False], ['OmniVolumeDensity', '/home/chris/isaacsim/kit/mdl/core/Volume/OmniVolumeDensity.mdl', None, False], ['OmniVolumeWorleyNoise', '/home/chris/isaacsim/kit/mdl/core/Volume/OmniVolumeNoise.mdl', 'OmniVolumeNoise', False], ['OmniVolumePerlinNoise', '/home/chris/isaacsim/kit/mdl/core/Volume/OmniVolumeNoise.mdl', 'OmniVolumeNoise', False]], 'hidden': [['OmniSurface_IncandescentBulb', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_BrushedMetal', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Chrome', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Copper', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Gold', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Foam', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Rubber', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_CarPaint', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_CarPaintMetallic', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_GlossyPaint', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_TwoToneCarPaint', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Default', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_PeanutButter', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_SkimMilk', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_WholeMilk', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Ceramic', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Clay', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Plastic', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Skin_1', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Skin_2', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Skin_3', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Skin_4', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Velvet', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Honey', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_MapleSyrup', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_OrangeJuice', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_DustedGlass', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_FrostedGlass', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Glass', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Blood', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Bubble', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Wax', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Polyethylene', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Diamond', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_Jade', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_ClearWater', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniSurface_DeepWater', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfacePresets.mdl', 'OmniSurfacePresets', False], ['OmniHair_Blonde', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHairPresets.mdl', 'OmniHairPresets', False], ['OmniHair_Brown', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHairPresets.mdl', 'OmniHairPresets', False], ['OmniHair_Auburn', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHairPresets.mdl', 'OmniHairPresets', False], ['OmniHair_Black', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHairPresets.mdl', 'OmniHairPresets', False], ['OmniHair_Wet', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHairPresets.mdl', 'OmniHairPresets', False], ['SimPBR_Translucent', '/home/chris/isaacsim/kit/mdl/core/Base/SimPBR_Translucent.mdl', None, False], ['OmniGlass', '/home/chris/isaacsim/kit/mdl/core/Base/OmniGlass.mdl', None, False], ['OmniSurfaceBlend', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfaceBlend.mdl', None, False], ['OmniEmissive', '/home/chris/isaacsim/kit/mdl/core/Base/OmniEmissive.mdl', None, False], ['OmniSurfaceLite', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurfaceLite.mdl', None, False], ['OmniPBR_ClearCoat', '/home/chris/isaacsim/kit/mdl/core/Base/OmniPBR_ClearCoat.mdl', None, False], ['OmniPBR', '/home/chris/isaacsim/kit/mdl/core/Base/OmniPBR.mdl', None, False], ['SimPBR', '/home/chris/isaacsim/kit/mdl/core/Base/SimPBR.mdl', None, False], ['OmniHair', '/home/chris/isaacsim/kit/mdl/core/Base/OmniHair.mdl', None, False], ['OmniSurface', '/home/chris/isaacsim/kit/mdl/core/Base/OmniSurface.mdl', None, False], ['OmniPBRBase', '/home/chris/isaacsim/kit/mdl/core/Base/OmniPBRBase.mdl', None, False], ['OmniVolumeDensity', '/home/chris/isaacsim/kit/mdl/core/Volume/OmniVolumeDensity.mdl', None, False], ['OmniVolumeWorleyNoise', '/home/chris/isaacsim/kit/mdl/core/Volume/OmniVolumeNoise.mdl', 'OmniVolumeNoise', False], ['OmniVolumePerlinNoise', '/home/chris/isaacsim/kit/mdl/core/Volume/OmniVolumeNoise.mdl', 'OmniVolumeNoise', False]]}
