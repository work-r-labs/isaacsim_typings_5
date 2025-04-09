"""

        This module contains bindings to the C++ omni::audio::IAudioDeviceEnum
        interface.  This provides functionality for enumerating available audio devices
        and collecting some basic information on each one.

        Sound devices attached to the system may change at any point due to user
        activity (ie: connecting or unplugging a USB audio device).  When enumerating
        devices, it is important to collect all device information directly instead
        of caching it.

        The device information is suitable to be used to display to a user in a menu
        to allow them to choose a device to use by name.
"""
from __future__ import annotations
from omni.kit.audiodeviceenum._audiodeviceenum import Direction
from omni.kit.audiodeviceenum._audiodeviceenum import IAudioDeviceEnum
from omni.kit.audiodeviceenum._audiodeviceenum import SampleType
from omni.kit.audiodeviceenum._audiodeviceenum import acquire_audio_device_enum_interface
from omni.kit.audiodeviceenum.extension import _AudioExtension
from . import _audiodeviceenum
from . import audio_page
from . import extension
__all__ = ['Direction', 'IAudioDeviceEnum', 'SampleType', 'acquire_audio_device_enum_interface', 'audio_page', 'extension', 'get_audio_device_enum_interface']
def get_audio_device_enum_interface() -> _audiodeviceenum.IAudioDeviceEnum:
    """
    
        helper method to retrieve a cached version of the IAudioDeviceEnum interface.
    
        Returns:
            The cached :class:`omni.kit.audiodeviceenum.IAudioDeviceEnum` interface.  This will
            only be retrieved on the first call.  All subsequent calls will return the cached
            interface object.
        
    """
