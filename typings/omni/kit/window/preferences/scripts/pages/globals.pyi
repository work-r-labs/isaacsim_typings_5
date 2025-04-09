from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni import ui
__all__ = ['GlobalPreferences', 'PreferenceBuilder', 'asyncio', 'carb', 'omni', 'ui']
class GlobalPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def __del__(self):
        ...
    def __init__(self):
        ...
    def build(self):
        ...
