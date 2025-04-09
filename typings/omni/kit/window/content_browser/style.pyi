from __future__ import annotations
from omni import ui
import pathlib
from pathlib import Path
__all__ = ['CURRENT_PATH', 'ICON_COMMON_PATH', 'ICON_PATH', 'Path', 'THEME', 'get_style', 'ui']
def get_style():
    ...
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.content_browser-2.10.3+d02c707b/omni/kit/window/content_browser')
ICON_COMMON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.content_browser-2.10.3+d02c707b/icons/common')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.content_browser-2.10.3+d02c707b/icons/NvidiaDark')
THEME: str = 'NvidiaDark'
