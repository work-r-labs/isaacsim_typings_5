from __future__ import annotations
from collections import namedtuple
from pathlib import Path
import typing
__all__: list = ['AssetTypeDef', 'ASSET_TYPE_ANIM_USD', 'ASSET_TYPE_CACHE_USD', 'ASSET_TYPE_CURVE_ANIM_USD', 'ASSET_TYPE_GEO_USD', 'ASSET_TYPE_MATERIAL_USD', 'ASSET_TYPE_PROJECT_USD', 'ASSET_TYPE_SEQ_USD', 'ASSET_TYPE_SKEL_USD', 'ASSET_TYPE_SKEL_ANIM_USD', 'ASSET_TYPE_USD_SETTINGS', 'ASSET_TYPE_USD', 'ASSET_TYPE_FBX', 'ASSET_TYPE_OBJ', 'ASSET_TYPE_MATERIAL', 'ASSET_TYPE_IMAGE', 'ASSET_TYPE_SOUND', 'ASSET_TYPE_SCRIPT', 'ASSET_TYPE_VOLUME', 'ASSET_TYPE_FOLDER', 'ASSET_TYPE_ICON', 'ASSET_TYPE_HIDDEN', 'ASSET_TYPE_UNKNOWN', 'init_asset_types', 'known_asset_types', 'clear_asset_types', 'register_file_extensions', 'asset_type_exts', 'is_asset_type', 'is_udim_sequence', 'get_asset_type', 'get_icon', 'get_thumbnail']
class AssetTypeDef(tuple):
    """
    AssetTypeDef(glyph, thumbnail, matching_exts)
    """
    __match_args__: typing.ClassVar[tuple] = ('glyph', 'thumbnail', 'matching_exts')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('glyph', 'thumbnail', 'matching_exts')
    @staticmethod
    def __new__(_cls, glyph, thumbnail, matching_exts):
        """
        Create new instance of AssetTypeDef(glyph, thumbnail, matching_exts)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new AssetTypeDef object from a sequence or iterable
        """
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
    def _asdict(self):
        """
        Return a new dict which maps field names to their values.
        """
    def _replace(self, **kwds):
        """
        Return a new AssetTypeDef object replacing specified fields with new values
        """
def asset_type_exts(asset_type: str) -> typing.List[str]:
    """
    
        Returns a list of file extensions associated with the given asset type.
    
        Args:
            asset_type (str): The asset type identifier.
    
        Returns:
            List[str]: A list of file extensions that match the given asset type.
        
    """
def clear_asset_types():
    """
    clear known asset types.
    """
def get_asset_type(filename: str) -> str:
    """
    
        Returns asset type, based on extension of given filename.
    
        Args:
            filename (str): Given file's name.
    
        Returns:
            str: The give file's asset type.
    
        
    """
def get_icon(filename: str) -> str:
    """
    
        Returns icon for specified file.
    
        Args:
            filename (str)
    
        Returns:
            str: Fullpath to the icon file, None if not found.
    
        
    """
def get_thumbnail(filename: str) -> str:
    """
    
        Returns thumbnail for specified file.
    
        Args:
            filename (str)
    
        Returns:
            str: Fullpath to the thumbnail file, None if not found.
    
        
    """
def init_asset_types():
    """
     Init default asset types's value 
    """
def is_asset_type(filename: str, asset_type: str) -> bool:
    """
    
        Returns True if given filename is of specified type.
    
        Args:
            filename (str)
            asset_type (str): Tested type name.
    
        Returns:
            bool
    
        
    """
def is_udim_sequence(filename: str):
    """
    
        Checks if the given filename represents a UDIM sequence image.
    
        Args:
            filename (str): The filename to check.
    
        Returns:
            bool: True if the filename represents a UDIM sequence image, False otherwise.
        
    """
def known_asset_types():
    """
    
        Initializes and returns a dictionary of known asset types.
    
        Returns:
            dict: A dictionary containing known asset types, where the keys are asset type
            identifiers, and the values are instances of the `AssetTypeDef` class.
    
        Example:
            >>> asset_types = known_asset_types()
            >>> print(asset_types[ASSET_TYPE_ICON])
            AssetTypeDef(None, None, ['.svg'])
    
        
    """
def register_file_extensions(asset_type: str, exts: [str], replace: bool = False):
    """
    
        Adds an asset type to the recognized list.
    
        Args:
            asset_type (str): Name of asset type.
            exts ([str]): List of extensions to associate with this asset type, e.g. [".usd", ".usda"].
            replace (bool): If True, replaces extensions in the existing definition. Otherwise, append
                to the existing list.
    
        
    """
ASSET_TYPE_ANIM_USD: str = 'anim_usd'
ASSET_TYPE_CACHE_USD: str = 'cache_usd'
ASSET_TYPE_CURVE_ANIM_USD: str = 'curve_anim_usd'
ASSET_TYPE_FBX: str = 'fbx'
ASSET_TYPE_FOLDER: str = 'folder'
ASSET_TYPE_GEO_USD: str = 'geo_usd'
ASSET_TYPE_HIDDEN: str = 'hidden'
ASSET_TYPE_ICON: str = 'icon'
ASSET_TYPE_IMAGE: str = 'image'
ASSET_TYPE_MATERIAL: str = 'material'
ASSET_TYPE_MATERIAL_USD: str = 'material_usd'
ASSET_TYPE_OBJ: str = 'obj'
ASSET_TYPE_PROJECT_USD: str = 'project_usd'
ASSET_TYPE_SCRIPT: str = 'script'
ASSET_TYPE_SEQ_USD: str = 'seq_usd'
ASSET_TYPE_SKEL_ANIM_USD: str = 'skel_anim_usd'
ASSET_TYPE_SKEL_USD: str = 'skel_usd'
ASSET_TYPE_SOUND: str = 'sound'
ASSET_TYPE_UNKNOWN: str = 'unknown'
ASSET_TYPE_USD: str = 'usd'
ASSET_TYPE_USD_SETTINGS: str = 'settings_usd'
ASSET_TYPE_VOLUME: str = 'volume'
_known_asset_types: dict  # value = {'settings_usd': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/settings_usd.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/settings_usd_256.png', matching_exts=['.settings.usd', '.settings.usda', '.settings.usdc', '.settings.usdz']), 'anim_usd': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/anim_usd.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/anim_usd_256.png', matching_exts=['.anim.usd', '.anim.usda', '.anim.usdc', '.anim.usdz']), 'cache_usd': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/cache_usd.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/cache_usd_256.png', matching_exts=['.cache.usd', '.cache.usda', '.cache.usdc', '.cache.usdz']), 'curve_anim_usd': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/anim_usd.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/curve_anim_usd_256.png', matching_exts=['.curveanim.usd', '.curveanim.usda', '.curveanim.usdc', '.curveanim.usdz']), 'geo_usd': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/geo_usd.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/geo_usd_256.png', matching_exts=['.geo.usd', '.geo.usda', '.geo.usdc', '.geo.usdz']), 'material_usd': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/material_usd.png', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/material_usd_256.png', matching_exts=['.material.usd', '.material.usda', '.material.usdc', '.material.usdz']), 'project_usd': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/project_usd.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/project_usd_256.png', matching_exts=['.project.usd', '.project.usda', '.project.usdc', '.project.usdz']), 'seq_usd': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/sequence_usd.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/sequence_usd_256.png', matching_exts=['.seq.usd', '.seq.usda', '.seq.usdc', '.seq.usdz']), 'skel_usd': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/skel_usd.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/skel_usd_256.png', matching_exts=['.skel.usd', '.skel.usda', '.skel.usdc', '.skel.usdz']), 'skel_anim_usd': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/anim_usd.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/skel_anim_usd_256.png', matching_exts=['.skelanim.usd', '.skelanim.usda', '.skelanim.usdc', '.skelanim.usdz']), 'fbx': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/usd_stage.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/fbx_256.png', matching_exts=['.fbx']), 'obj': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/usd_stage.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/obj_256.png', matching_exts=['.obj']), 'material': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/mdl.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/mdl_256.png', matching_exts=['.mdl', '.mtlx']), 'image': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/image.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/image_256.png', matching_exts=['.bmp', '.gif', '.jpg', '.jpeg', '.png', '.tga', '.tif', '.tiff', '.hdr', '.dds', '.exr', '.psd', '.ies', '.tx']), 'sound': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/sound.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/sound_256.png', matching_exts=['.wav', '.wave', '.ogg', '.oga', '.flac', '.fla', '.mp3', '.m4a', '.spx', '.opus', '.adpcm']), 'script': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/script.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/script_256.png', matching_exts=['.py']), 'volume': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/volume.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/volume_256.png', matching_exts=['.nvdb', '.vdb']), 'icon': AssetTypeDef(glyph=None, thumbnail=None, matching_exts=['.svg']), 'hidden': AssetTypeDef(glyph=None, thumbnail=None, matching_exts=['.thumbs']), 'usd': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/icons/NvidiaDark/usd_stage.svg', thumbnail='/home/chris/isaacsim/extscache/omni.kit.helper.file_utils-0.1.9+d02c707b/data/thumbnails/usd_stage_256.png', matching_exts=['.FBX', '.OBJ', '.abc', '.drc', '.glb', '.gltf', '.live', '.lxo', '.md5', '.metricsAssembler', '.omniabc', '.usd', '.usda', '.usdc', '.usdz']), 'urdf': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/isaacsim.asset.importer.urdf-2.3.10+106.4.0.lx64.r.cp310/icons/icoFileURDF.png', thumbnail='/home/chris/isaacsim/extscache/isaacsim.asset.importer.urdf-2.3.10+106.4.0.lx64.r.cp310/icons/icoFileURDF.png', matching_exts=['.urdf', '.URDF']), 'mjcf': AssetTypeDef(glyph='/home/chris/isaacsim/extscache/isaacsim.asset.importer.mjcf-2.3.3+106.3.0.lx64.r.cp310/icons/icoFileMJCF.png', thumbnail='/home/chris/isaacsim/extscache/isaacsim.asset.importer.mjcf-2.3.3+106.3.0.lx64.r.cp310/icons/icoFileMJCF.png', matching_exts=['.xml', '.XML'])}
