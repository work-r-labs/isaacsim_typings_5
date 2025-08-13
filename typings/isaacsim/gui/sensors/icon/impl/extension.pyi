from __future__ import annotations
import carb as carb
from isaacsim.gui.sensors.icon.impl.model import IconModel
from isaacsim.gui.sensors.icon.impl.scene import IconScene
import omni as omni
from omni.kit.viewport.menubar.core.model.category_model import CategoryStateItem
from omni.kit.viewport.menubar.display.extension import get_instance as get_menubar_display_instance
from pathlib import Path
__all__: list[str] = ['CategoryStateItem', 'IconModel', 'IconScene', 'Path', 'SensorIconExtension', 'VISIBLE_SETTING', 'carb', 'get_instance', 'get_menubar_display_instance', 'omni']
class SensorIconExtension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
def get_instance():
    ...
VISIBLE_SETTING: str = '/persistent/exts/isaacsim.gui.sensors.icon/visible_on_startup'
_extension: SensorIconExtension  # value = <isaacsim.gui.sensors.icon.impl.extension.SensorIconExtension object>
