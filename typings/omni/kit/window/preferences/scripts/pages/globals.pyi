from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb.eventdispatcher import get_eventdispatcher
import omni as omni
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni import ui
import os as os
__all__: list[str] = ['GlobalPreferences', 'PreferenceBuilder', 'asyncio', 'carb', 'get_eventdispatcher', 'omni', 'os', 'ui']
class GlobalPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def __del__(self):
        ...
    def __init__(self):
        ...
    def build(self):
        ...
