from __future__ import annotations
import omni as omni
from pxr import Sdf
import re as re
import typing
__all__: list = ['Utils']
class Utils:
    MDL_RE: typing.ClassVar[re.Pattern]  # value = re.compile('^.*\\.(mdl|mtlx)?$', re.IGNORECASE)
    UDIM_GROUP_RE: typing.ClassVar[re.Pattern]  # value = re.compile('^(.*)(<UDIM>|<UVTILE0>|<UVTILE1>)(.*)')
    UDIM_MARKER_RE: typing.ClassVar[re.Pattern]  # value = re.compile('^.*(<UDIM>|<UVTILE0>|<UVTILE1>).*')
    @staticmethod
    def compute_absolute_path(base_path, path) -> str:
        ...
    @staticmethod
    def is_material(path) -> bool:
        ...
    @staticmethod
    def is_omniverse_path(path) -> bool:
        ...
    @staticmethod
    def is_udim_texture(path) -> bool:
        ...
    @staticmethod
    def is_udim_wildcard_texture(path, udim_texture_path) -> bool:
        ...
    @staticmethod
    def is_usd_writable_filetype(path) -> bool:
        ...
    @staticmethod
    def make_relative_path(relative_to, path) -> str:
        ...
    @staticmethod
    def normalize_path(path) -> str:
        ...
