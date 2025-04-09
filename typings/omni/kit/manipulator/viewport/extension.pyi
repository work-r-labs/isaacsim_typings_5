from __future__ import annotations
import omni as omni
from omni.kit.manipulator.viewport.manipulator_factory import ManipulatorFactory
__all__ = ['ManipulatorCore', 'ManipulatorFactory', 'omni']
class ManipulatorCore(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
