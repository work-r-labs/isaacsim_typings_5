from __future__ import annotations
from omni import ui
import pathlib
from pathlib import Path
__all__ = ['CURRENT_PATH', 'ICON_PATH', 'PROPERTY_STYLES', 'Path', 'ui']
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.browser.folder.core-1.10.1/omni/kit/browser/folder/core/property')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.browser.folder.core-1.10.1/data/icons')
PROPERTY_STYLES: dict = {'PropertyToolBar.Button': {'background_color': 0, 'padding': 3, 'margin': 0}, 'PropertyToolBar.Button:selected': {'background_color': 'shade:4280492319;light=4283650900'}, 'Splitter': {'background_color': 0, 'margin_width': 0}, 'Splitter:hovered': {'background_color': 4289753147}, 'Splitter:pressed': {'background_color': 4289753147}}
