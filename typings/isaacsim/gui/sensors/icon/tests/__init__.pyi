from __future__ import annotations
import carb as carb
from isaacsim.gui.sensors.icon.impl.scene import SensorIcon
from isaacsim.gui.sensors.icon.tests.test_sensor_icon import TestSensorIcon
from isaacsim.gui.sensors.icon.tests.test_sensor_icon import create_test_object
from isaacsim.gui.sensors.icon.tests.test_sensor_icon import is_viewport_legacy
import omni as omni
from omni.kit import ui_test
from omni.kit.viewport.utility import get_active_viewport
from omni.kit.viewport.utility import get_active_viewport_window
from omni.ui.tests.test_base import OmniUiTest
import pathlib
from pathlib import Path
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from . import test_sensor_icon
__all__: list[str] = ['CURRENT_PATH', 'Gf', 'OmniUiTest', 'Path', 'SHOW_TITLE_PATH', 'Sdf', 'SensorIcon', 'TEST_DATA_PATH', 'TEST_DATA_PATH_ICON', 'TEST_OBJECT_PRIM_PATH', 'TestSensorIcon', 'Usd', 'VISIBLE_SETTING', 'carb', 'create_test_object', 'get_active_viewport', 'get_active_viewport_window', 'is_viewport_legacy', 'omni', 'test_sensor_icon', 'ui_test']
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/exts/isaacsim.gui.sensors.icon/isaacsim/gui/sensors/icon/tests')
SHOW_TITLE_PATH: str = 'exts/omni.kit.prim.icon/showTitle'
TEST_DATA_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/exts/isaacsim.gui.sensors.icon/data/tests')
TEST_DATA_PATH_ICON: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/exts/isaacsim.gui.sensors.icon/icons')
TEST_OBJECT_PRIM_PATH: str = '/test_obj'
VISIBLE_SETTING: str = '/persistent/exts/isaacsim.gui.sensors.icon/visible_on_startup'
