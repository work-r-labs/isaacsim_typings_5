from __future__ import annotations
from omni import ui
import pathlib
from pathlib import Path
__all__: list[str] = ['CURRENT_PATH', 'ICON_PATH', 'PROPERTY_STYLES', 'Path', 'ui']
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.browser.folder.core-1.10.9/omni/kit/browser/folder/core/property')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.browser.folder.core-1.10.9/data/icons')
PROPERTY_STYLES: dict = {'PropertyToolBar.Button': {'background_color': 0, 'padding': 3, 'margin': 0}, 'PropertyToolBar.Button:selected': {'background_color': 'shade:4280492319;light=4283650900'}, 'Splitter': {'background_color': 0, 'margin_width': 0}, 'Splitter:hovered': {'background_color': 4289753147}, 'Splitter:pressed': {'background_color': 4289753147}}
