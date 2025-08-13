from __future__ import annotations
from omni import ui
import omni.ui.color_utils
import pathlib
from pathlib import Path
__all__: list[str] = ['CURRENT_PATH', 'ICON_PATH', 'Path', 'UI_STYLE', 'cl', 'ui']
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.widget.filter-1.1.4+8131b85d/omni/kit/widget/filter')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.widget.filter-1.1.4+8131b85d/data/icons')
UI_STYLE: dict  # value = {'FilterButton': {'background_color': 0, 'margin_width': 0, 'padding': 2, 'border_radius': 2}, 'FilterButton:selected': {'background_color': 'shade:4280230179'}, 'FilterButton.Image': {'background_color': 0, 'color': 'shade:4289243304', 'image_url': '/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.widget.filter-1.1.4+8131b85d/data/icons/filter_tint.svg', 'alignment': <Alignment.CENTER: 72>}, 'FilterButton.Image:selected': {'color': 'shade:4294952756'}, 'FilterButton:hovered': {'background_color': 4285427310}, 'FilterButton.Carot': {'background_color': 'shade:4289243304'}, 'FilterButton.Carot:selected': {'background_color': 'shade:4294952756'}}
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
