from __future__ import annotations
import omni as omni
from omni.kit.window.material_graph.graph_window import GraphWindow
from omni.kit.window.material_graph.usdshade_graph_model import UsdShadeGraphModel
from omni import ui
from omni.ui.tests.test_base import OmniUiTest
from pathlib import Path
from pxr import Sdf
from pxr import Usd
from pxr import UsdShade
from pxr import UsdUI
import typing
__all__ = ['GraphWindow', 'OmniUiTest', 'Path', 'Sdf', 'TestCommand', 'Usd', 'UsdShade', 'UsdShadeGraphModel', 'UsdUI', 'omni', 'ui']
class TestCommand(omni.ui.tests.test_base.OmniUiTest):
    _classSetupFailed: typing.ClassVar[bool] = False
    _class_cleanups: typing.ClassVar[list] = list()
    def setUp(self):
        ...
    def tearDown(self):
        ...
    def test_create_usd_material_graph(self):
        """
        Create a new material which has a subgraph so we can test most of the commands
        """
    def test_import_compound(self):
        ...
