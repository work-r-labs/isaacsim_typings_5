from __future__ import annotations
import omni as omni
from omni.kit.window.material_graph.usdshade_graph_model import UsdShadeGraphModel
from omni.ui.tests.test_base import OmniUiTest
import pathlib
from pathlib import Path
from pxr import Usd
from pxr import UsdShade
import typing
__all__ = ['CURRENT_PATH', 'OmniUiTest', 'Path', 'TestMaterialGraphModel', 'Usd', 'UsdShade', 'UsdShadeGraphModel', 'omni']
class TestMaterialGraphModel(omni.ui.tests.test_base.OmniUiTest):
    _classSetupFailed: typing.ClassVar[bool] = False
    _class_cleanups: typing.ClassVar[list] = list()
    def setUp(self):
        ...
    def tearDown(self):
        ...
    def test_model(self):
        ...
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/omni/kit/window/material_graph/tests/../../../../../data/tests')
