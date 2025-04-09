from __future__ import annotations
import abc as abc
import omni.kit.viewport.menubar.core.model.usd_attribute_model
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDAttributeModel
from omni import ui
__all__: list = ['AbstractCameraSetting']
class AbstractCameraSetting:
    enabled: bool
    def __init__(self, model: omni.kit.viewport.menubar.core.model.usd_attribute_model.USDAttributeModel, enabled: bool = True):
        ...
    def _build_ui(self) -> typing.List[omni.ui._ui.MenuDelegate]:
        ...
