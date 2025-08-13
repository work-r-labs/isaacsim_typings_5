from __future__ import annotations
from omni import ui
import pathlib
from pathlib import Path
__all__: list[str] = ['CURRENT_PATH', 'ICON_COMMON_PATH', 'ICON_PATH', 'Path', 'THEME', 'get_style', 'ui']
def get_style():
    ...
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.content_browser-3.1.1+8131b85d/omni/kit/window/content_browser')
ICON_COMMON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.content_browser-3.1.1+8131b85d/icons/common')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.content_browser-3.1.1+8131b85d/icons/NvidiaDark')
THEME: str = 'NvidiaDark'
