"""

        This module contains bindings to the C++ omni::audio::IAudioDeviceEnum
        interface.  This provides functionality for enumerating available audio
        devices and collecting some basic information on each one.

        Sound devices attached to the system may change at any point due to user
        activity (ie: connecting or unplugging a USB audio device).  When enumerating
        devices, it is important to collect all device information directly instead
        of caching it.

        The device information is suitable to be used to display to a user in a menu
        to allow them to choose a device to use by name.
    
"""
from __future__ import annotations
import typing
__all__ = ['Direction', 'IAudioDeviceEnum', 'SampleType', 'acquire_audio_device_enum_interface']
class Direction:
    """
    The direction to collect device information for.  This is passed to most functions in the `IAudioDeviceEnum` interface to specify which types of devices are currently interesting.
    
    Members:
    
      PLAYBACK : Enumerate audio playback devices only.
    
      CAPTURE : Enumerate audio capture devices only.
    """
    CAPTURE: typing.ClassVar[Direction]  # value = <Direction.CAPTURE: 1>
    PLAYBACK: typing.ClassVar[Direction]  # value = <Direction.PLAYBACK: 0>
    __members__: typing.ClassVar[dict[str, Direction]]  # value = {'PLAYBACK': <Direction.PLAYBACK: 0>, 'CAPTURE': <Direction.CAPTURE: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IAudioDeviceEnum:
    """
    
            This interface contains functions for audio device enumeration.  This is able to
            enumerate all audio devices attached to the system at any given point and collect the
            information for each device.  This is only intended to collect the device information
            needed to display to the user for device selection purposes.  If a device is to be
            chosen based on certain needs (ie: channel count, frame rate, etc), it should be done
            directly through the audio playback or capture context during creation.  This is able
            to collect information for both playback and capture devices.
    
            All the function in this interface are in omni.kit.audio.IAudioDeviceEnum class.
            To retrieve this object, use get_audio_device_enum_interface() method:
    
            >>> import omni.kit.audio
            >>> dev = omni.kit.audio.get_audio_device_enum_interface()
            >>> count = dev.get_device_count(PLAYBACK)
            >>> desc = dev.get_device_description(PLAYBACK, 0)
        
    """
    def get_device_channel_count(self, dir: Direction, index: int) -> int:
        """
                Retrieves the maximum channel count for a requested device.
        
                This retrieves the maximum channel count for a requested device.  This count
                is the maximum number of channels that the device can natively handle without
                having to trim or reprocess the data.  Using a device with a different channel
                count than its maximum is allowed but will result in extra processing time to
                upmix or downmix channels in the stream.  Note that downmixing channel counts
                (ie: 7.1 to stereo) will often result in multiple channels being blended
                together and can result in an unexpected final signal in certain cases.
        
                This function will open the audio device to test on some systems.  The
                caller should ensure that isDirectHardwareBackend() returns false
                before calling this.
        
                Args:
                    dir: the audio direction to get the maximum channel count for.
                    index: the index  of the device to retrieve the channel count for.  This should
                        be between 0 and one less than the most recent return value of getDeviceCount().
        
                Returns:
                    If successful, this returns the maximum channel count of the requested device.
        
                    If the requested device is out of range of those connected to the system, 0
                    is returned.
        """
    def get_device_count(self, dir: Direction) -> int:
        """
                Retrieves the total number of devices attached to the system of a requested type.
        
                Args:
                    dir:  the audio direction to get the device count for.
        
                Returns:
                    If successful, this returns the total number of connected audio devices of the
                    requested type.
        
                    If there are no devices of the requested type connected to the system, 0 is
                    returned.
        """
    def get_device_description(self, dir: Direction, index: int) -> typing.Any:
        """
                Retrieves a descriptive string for a requested audio device.
        
                This retrieves a descriptive string for the requested device.  This string is
                suitable for display to a user in a menu or selection list.
        
                Args:
                    dir: the audio direction to get the description string for.
                    index: the index of the device to retrieve the description for.  This should be
                        between 0 and one less than the most recent return value of getDeviceCount().
        
                Returns:
                    If successful, this returns a python string describing the requested device.
        
                    If the requested device is out of range of those connected to the system, this
                    returns None.
        """
    def get_device_frame_rate(self, dir: Direction, index: int) -> int:
        """
                Retrieves the preferred frame rate of a requested device.
        
                This retrieves the preferred frame rate of a requested device.  The preferred
                frame rate is the rate at which the device natively wants to process audio data.
                Using the device at other frame rates may be possible but would require extra
                processing time.  Using a device at a different frame rate than its preferred
                one may also result in degraded quality depending on what the processing versus
                preferred frame rate is.
        
                This function will open the audio device to test on some systems.  The
                caller should ensure that isDirectHardwareBackend() returns false
                before calling this.
        
                Args:
                    dir: the audio direction to get the preferred frame rate for.
                    index: the index  of the device to retrieve the frame rate for.  This should
                        be between 0 and one less than the most recent return value of
                        getDeviceCount().
        
                Returns:
                    If successful, this returns the preferred frame rate of the requested device.
        
                    If the requested device was out of range of those connected to the system, 0
                    is returned.
        """
    def get_device_id(self, dir: Direction, index: int) -> typing.Any:
        """
                Retrieves the unique identifier for the requested device.
        
                Args:
                    dir: the audio direction to get the device name for.
                    index: the index of the device to retrieve the identifier for.  This
                           should be between 0 and one less than the most recent return
                           value of getDeviceCount().
        
                Returns:
                    If successful, this returns a python string containing the unique identifier
                    of the requested device.
        
                    If the requested device is out of range of those connected to the system, this
                    returns None.
        """
    def get_device_name(self, dir: Direction, index: int) -> typing.Any:
        """
                Retrieves the friendly name of a requested device.
        
                Args:
                    dir: the audio direction to get the device name for.
                    index: the index  of the device to retrieve the name for.  This should be between
                        0 and one less than the most recent return value of getDeviceCount().
        
                Returns:
                    If successful, this returns a python string containing the friendly name of the
                    requested device.
        
                    If the requested device is out of range of those connected to the system, this
                    returns None.
        """
    def get_device_sample_size(self, dir: Direction, index: int) -> int:
        """
                Retrieves the native sample size for a requested device.
        
                This retrieves the bits per sample that a requested device prefers to process
                its data at.  It may be possible to use the device at a different sample size,
                but that would likely result in extra processing time.  Using a device at a
                different sample rate than its native could degrade the quality of the final
                signal.
        
                This function will open the audio device to test on some systems.  The
                caller should ensure that isDirectHardwareBackend() returns false
                before calling this.
        
                Args:
                    dir: the audio direction to get the native sample size for.
                    index: the index  of the device to retrieve the sample size for.  This should
                        be between 0 and one less than the most recent return value of getDeviceCount().
        
                Returns:
                    If successful, this returns the native sample size in bits per sample of the
                    requested device.
        
                    If the requested device is out of range of those connected to the system, 0
                    is returned.
        """
    def get_device_sample_type(self, dir: Direction, index: int) -> SampleType:
        """
                Retrieves the native sample data type for a requested device.
        
                This retrieves the sample data type that a requested device prefers to process
                its data in.  It may be possible to use the device with a different data type,
                but that would likely result in extra processing time.  Using a device with a
                different sample data type than its native could degrade the quality of the
                final signal.
        
                This function will open the audio device to test on some systems.  The
                caller should ensure that isDirectHardwareBackend() returns false
                before calling this.
        
                Args:
                    dir: the audio direction to get the native sample data type for.
                    index: the index  of the device to retrieve the sample data type for.  This should
                        be between 0 and one less than the most recent return value of getDeviceCount().
        
                Returns:
                    If successful, this returns the native sample data type of the requested device.
        
                    If the requested device is out of range of those connected to the system,
                    UNKNOWN is returned.
        """
    def is_direct_hardware_backend(self) -> bool:
        """
                Check if the audio device backend uses direct hardware access.
        
                A direct hardware audio backend is capable of exclusively locking audio
                devices, so devices are not guaranteed to open successfully and opening
                devices to test their format may be disruptive to the system.
        
                ALSA is the only 'direct hardware' backend that's currently supported.
                Some devices under ALSA will exclusively lock the audio device; these
                may fail to open because they're busy.
                Additionally, some devices under ALSA can fail to open because they're
                misconfigured (Ubuntu's default ALSA configuration can contain
                misconfigured devices).
                In addition to this, opening some devices under ALSA can take a
                substantial amount of time (over 100ms).
                For these reasons, it is important to verify that you are not using a
                'direct hardware' backend if you are going to call certain functions in
                this interface.
        
                Returns:
                    This returns `True` if this backend has direct hardware access.
                    This will be returned when ALSA is in use.
                    This returns `False` if the backend is an audio mixing server.
                    This will be returned when Pulse Audio or Window Audio Services
                    are in use.
        """
class SampleType:
    """
    Names for the type of sample that an audio device can use.
    
    Members:
    
      UNKNOWN : Could not determine the sample type or an invalid device index was given.
    
      PCM_SIGNED_INTEGER : Signed integer PCM samples.  This is usually used for 16-bit an up.
    
      PCM_UNSIGNED_INTEGER : Unsigned integer PCM samples.  This is often used for 8-bit samples.
    
      PCM_FLOAT : Single precision floating point PCM samples.
    
      COMPRESSED : A compressed sample format such as ADPCM, MP3, Vorbis, etc.
    """
    COMPRESSED: typing.ClassVar[SampleType]  # value = <SampleType.COMPRESSED: 4>
    PCM_FLOAT: typing.ClassVar[SampleType]  # value = <SampleType.PCM_FLOAT: 3>
    PCM_SIGNED_INTEGER: typing.ClassVar[SampleType]  # value = <SampleType.PCM_SIGNED_INTEGER: 1>
    PCM_UNSIGNED_INTEGER: typing.ClassVar[SampleType]  # value = <SampleType.PCM_UNSIGNED_INTEGER: 2>
    UNKNOWN: typing.ClassVar[SampleType]  # value = <SampleType.UNKNOWN: 0>
    __members__: typing.ClassVar[dict[str, SampleType]]  # value = {'UNKNOWN': <SampleType.UNKNOWN: 0>, 'PCM_SIGNED_INTEGER': <SampleType.PCM_SIGNED_INTEGER: 1>, 'PCM_UNSIGNED_INTEGER': <SampleType.PCM_UNSIGNED_INTEGER: 2>, 'PCM_FLOAT': <SampleType.PCM_FLOAT: 3>, 'COMPRESSED': <SampleType.COMPRESSED: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
def acquire_audio_device_enum_interface(plugin_name: str = None, library_path: str = None) -> IAudioDeviceEnum:
    ...
