"""
A module for managing audio properties and settings within Omniverse Kit applications.
"""
from __future__ import annotations
import omni as omni
from omni.kit.property.audio.scripts.audio_properties import AudioPropertyExtension
from omni.kit.property.audio.scripts.audio_settings_widget import AudioSettingsWidget
from pxr import UsdMedia
from . import audio_properties
from . import audio_settings_widget
__all__: list = ['AudioPropertyExtension']
