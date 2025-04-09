from __future__ import annotations
import omni as omni
from omni.kit.widget.prompt.prompt import PromptManager
__all__ = ['PromptExtension', 'PromptManager', 'omni']
class PromptExtension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
