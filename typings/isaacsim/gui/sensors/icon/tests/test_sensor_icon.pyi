from __future__ import annotations
import carb as carb
from isaacsim.gui.sensors.icon.impl.scene import SensorIcon
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
import typing
__all__: list[str] = ['CURRENT_PATH', 'Gf', 'OmniUiTest', 'Path', 'SHOW_TITLE_PATH', 'Sdf', 'SensorIcon', 'TEST_DATA_PATH', 'TEST_DATA_PATH_ICON', 'TEST_OBJECT_PRIM_PATH', 'TestSensorIcon', 'Usd', 'VISIBLE_SETTING', 'carb', 'create_test_object', 'get_active_viewport', 'get_active_viewport_window', 'is_viewport_legacy', 'omni', 'ui_test']
class TestSensorIcon(omni.ui.tests.test_base.OmniUiTest):
    _classSetupFailed: typing.ClassVar[bool] = False
    _class_cleanups: typing.ClassVar[list] = list()
    def _dock_viewport(self, width = 1200, height = 900, block_device = False):
        """
        Utility function to dock viewport window and focus on turntable panel.
        """
    def setUp(self):
        ...
    def tearDown(self):
        ...
    def test_sensoricon_default(self):
        ...
    def test_sensoricon_path_types(self):
        """
        Tests handling of str and Sdf.Path for prim_path arguments.
        """
    def test_sensoricon_saved_stage(self):
        ...
    def test_sensoricon_usd_listening(self):
        """
        Tests USD listening and icon visibility.
        """
def create_test_object(prim_path = '/test_obj', prim_type = 'Generic', attrs = None):
    ...
def is_viewport_legacy():
    ...
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/exts/isaacsim.gui.sensors.icon/isaacsim/gui/sensors/icon/tests')
SHOW_TITLE_PATH: str = 'exts/omni.kit.prim.icon/showTitle'
TEST_DATA_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/exts/isaacsim.gui.sensors.icon/data/tests')
TEST_DATA_PATH_ICON: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/exts/isaacsim.gui.sensors.icon/icons')
TEST_OBJECT_PRIM_PATH: str = '/test_obj'
VISIBLE_SETTING: str = '/persistent/exts/isaacsim.gui.sensors.icon/visible_on_startup'
