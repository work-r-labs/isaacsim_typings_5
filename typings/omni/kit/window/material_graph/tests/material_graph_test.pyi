from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.window.material_graph.graph_window import GraphWindow
from omni.kit.window.material_graph.usdshade_graph_model import UsdShadeGraphModel
from omni import ui
from omni.ui.tests.test_base import OmniUiTest
import pathlib
from pathlib import Path
from pxr import Sdf
from pxr import UsdShade
import typing
__all__: list[str] = ['CURRENT_PATH', 'GraphWindow', 'OmniUiTest', 'Path', 'Sdf', 'TestMaterialGraph', 'UsdShade', 'UsdShadeGraphModel', 'carb', 'omni', 'ui']
class TestMaterialGraph(omni.ui.tests.test_base.OmniUiTest):
    _classSetupFailed: typing.ClassVar[bool] = False
    _class_cleanups: typing.ClassVar[list] = list()
    def setUp(self):
        ...
    def tearDown(self):
        ...
    def test_general(self):
        ...
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.material_graph-1.8.23/data')
