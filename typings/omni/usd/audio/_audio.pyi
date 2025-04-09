"""

        This module contains bindings for the omni::usd::audio module.
        This provides functionality for playing and managing sound prims in
        USD scenes.

        Sound files may be in RIFF/WAV, Ogg, or FLAC format.
        Data in the sound files may use 8, 16, 24, or 32 bit integer samples,
        or 32 bit floating point samples.  Channel counts may be from 1 to 64
        If more channels of data are provided than the audio device can play,
        some channels will be blended together automatically.
    
"""
from __future__ import annotations
import carb._carb
import carb.audio._audio
import carb.events._events
import omni.usd._usd
import typing
__all__ = ['AssetLoadStatus', 'EventType', 'FeatureDefault', 'INVALID_STREAMER_ID', 'SoundLengthType', 'StreamListener', 'test_hydra_plugin']
class AssetLoadStatus:
    """
    Members:
    
      IN_PROGRESS
    
      DONE
    
      FAILED
    
      NOT_REGISTERED
    """
    DONE: typing.ClassVar[AssetLoadStatus]  # value = <AssetLoadStatus.DONE: 0>
    FAILED: typing.ClassVar[AssetLoadStatus]  # value = <AssetLoadStatus.FAILED: 2>
    IN_PROGRESS: typing.ClassVar[AssetLoadStatus]  # value = <AssetLoadStatus.IN_PROGRESS: 1>
    NOT_REGISTERED: typing.ClassVar[AssetLoadStatus]  # value = <AssetLoadStatus.NOT_REGISTERED: 3>
    __members__: typing.ClassVar[dict[str, AssetLoadStatus]]  # value = {'IN_PROGRESS': <AssetLoadStatus.IN_PROGRESS: 1>, 'DONE': <AssetLoadStatus.DONE: 0>, 'FAILED': <AssetLoadStatus.FAILED: 2>, 'NOT_REGISTERED': <AssetLoadStatus.NOT_REGISTERED: 3>}
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
class EventType:
    """
    Members:
    
      METADATA_CHANGE
    
      LISTENER_LIST_CHANGE
    
      ACTIVE_LISTENER_CHANGE
    """
    ACTIVE_LISTENER_CHANGE: typing.ClassVar[EventType]  # value = <EventType.ACTIVE_LISTENER_CHANGE: 3>
    LISTENER_LIST_CHANGE: typing.ClassVar[EventType]  # value = <EventType.LISTENER_LIST_CHANGE: 2>
    METADATA_CHANGE: typing.ClassVar[EventType]  # value = <EventType.METADATA_CHANGE: 1>
    __members__: typing.ClassVar[dict[str, EventType]]  # value = {'METADATA_CHANGE': <EventType.METADATA_CHANGE: 1>, 'LISTENER_LIST_CHANGE': <EventType.LISTENER_LIST_CHANGE: 2>, 'ACTIVE_LISTENER_CHANGE': <EventType.ACTIVE_LISTENER_CHANGE: 3>}
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
class FeatureDefault:
    """
    Members:
    
      ON
    
      OFF
    
      FORCE_ON
    
      FORCE_OFF
    """
    FORCE_OFF: typing.ClassVar[FeatureDefault]  # value = <FeatureDefault.FORCE_OFF: 3>
    FORCE_ON: typing.ClassVar[FeatureDefault]  # value = <FeatureDefault.FORCE_ON: 2>
    OFF: typing.ClassVar[FeatureDefault]  # value = <FeatureDefault.OFF: 1>
    ON: typing.ClassVar[FeatureDefault]  # value = <FeatureDefault.ON: 0>
    __members__: typing.ClassVar[dict[str, FeatureDefault]]  # value = {'ON': <FeatureDefault.ON: 0>, 'OFF': <FeatureDefault.OFF: 1>, 'FORCE_ON': <FeatureDefault.FORCE_ON: 2>, 'FORCE_OFF': <FeatureDefault.FORCE_OFF: 3>}
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
class SoundLengthType:
    """
    Members:
    
      PLAY_LENGTH
    
      SOUND_LENGTH
    
      ASSET_LENGTH
    """
    ASSET_LENGTH: typing.ClassVar[SoundLengthType]  # value = <SoundLengthType.ASSET_LENGTH: 2>
    PLAY_LENGTH: typing.ClassVar[SoundLengthType]  # value = <SoundLengthType.PLAY_LENGTH: 0>
    SOUND_LENGTH: typing.ClassVar[SoundLengthType]  # value = <SoundLengthType.SOUND_LENGTH: 1>
    __members__: typing.ClassVar[dict[str, SoundLengthType]]  # value = {'PLAY_LENGTH': <SoundLengthType.PLAY_LENGTH: 0>, 'SOUND_LENGTH': <SoundLengthType.SOUND_LENGTH: 1>, 'ASSET_LENGTH': <SoundLengthType.ASSET_LENGTH: 2>}
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
class StreamListener:
    def __init__(self, p: carb.events._events.IEventStream, open: typing.Callable[[carb.audio._audio.SoundFormat], None], writeData: typing.Callable[[list], None], close: typing.Callable[[], None]) -> None:
        ...
def _create_capture_streamer(mgr: omni.usd._usd.AudioManager) -> int:
    """
            Creates a new capture streamer.  This streamer object may be used multiple times to
            capture audio for a stage.  Once a capture has been stopped on it, this streamer
            can be reused for another capture without issue.  It must be destroyed with
            destroy_capture_streamer() when it is no longer needed.
    
            Args:
                mgr: the audio manager to create the new streamer on.  This may not be None.
    
            Returns:
                The handle to a new capture streamer if it is successfully created.  When this
                handle is no longer needed, it must be destroyed with destroy_capture_streamer().
    
                INVALID_STREAMER_ID if the new capture streamer could not be created.
    """
def _create_event_stream_for_capture(mgr: omni.usd._usd.AudioManager, id: int) -> carb.events._events.IEventStream:
    """
            Creates an event stream that the capture streamer will send data to.
    
            Args:
                mgr: the audio manager that owns the streamer id.  This may not be None.
                id: the streamer to set the filename for.  This handle will have been
                    returned from a previous call to create_capture_streamer().  This may
                    not be INVALID_STREAMER_ID.
    
            Returns:
                An event stream object.
                Call omni.usd.audio.create_event_listener() to receive callbacks
                for this object.
                Although you can directly subscribe to this callback, python is
                unsuitable for the required data conversion this needs.
    """
def _destroy_capture_streamer(mgr: omni.usd._usd.AudioManager, id: int) -> None:
    """
            Destroys a capture streamer.
    
            Args:
                mgr: the audio manager to destroy the streamer for.  This may not be None.
                id: the streamer to be destroyed.  If this streamer is currently running a
                    capture, it will be stopped first.  Note that currently stopping one
                    streamer will stop all installed streamers.  All but the removed one
                    will be restarted afterward.  This will have the side effect of
                    overwriting each other streamer's file though.  This can be avoided
                    by stopping all streamers simultaneously first with stop_captures().
    
            Returs:
                no return value.
    """
def _draw_waveform(mgr: omni.usd._usd.AudioManager, primPath: str, width: int, height: int, flags: int, channel: int, background: carb._carb.Float4, colors: list[carb._carb.Float4]) -> list[int]:
    """
            This will draw an RGBA image of the waveform of the sound asset in
            use by a `Sound` prim.
    
            Args:
                prim: The prim which has the sound asset that will be rendered.
                      Note that the `mediaOffsetStart` and `mediaOffsetEnd`
                      properties of the prim are used to choose the region of
                      the sound that is drawn.
                      The asset for this prim must have been loaded or the
                      call will fail.
                width: The width, in pixels, of the output image.
                height: The width, in pixels, of the output image.
                flags: Flags that alter the style of the rendered image.
                       This must be a combination of carb.audio.AUDIO_IMAGE_FLAG*.
                        - AUDIO_IMAGE_FLAG_USE_LINES: The sound samples in the output
                          image will be connected with lines, rather than just being
                          individual points.
                        - AUDIO_IMAGE_FLAG_NOISE_COLOR: Each sound sample is given
                          a random color and the colors parameter is ignored.
                        - AUDIO_IMAGE_FLAG_MULTI_CHANNEL: Each channel is drawn
                          on top of the previous channel.
                        - AUDIO_IMAGE_FLAG_ALPHA_BLEND: Each pixel drawn is alpha
                          blended into the output image.
                          This is only useful if the colors specified don't have
                          an alpha component of 1.0.
                        - AUDIO_IMAGE_FLAG_SPLIT_CHANNELS: Each channel is rendered
                          separately, organized vertically.
                          This cannot be used in combination with AUDIO_IMAGE_FLAG_MULTI_CHANNEL;
                          the rendering style chosen in this case is undefined.
                channel: Which audio channel will be rendered.
                         This is only used if AUDIO_IMAGE_FLAG_MULTI_CHANNEL
                         and AUDIO_IMAGE_FLAG_SPLIT_CHANNELS are not set.
                background: A normalized RGBA color to use as the background of
                            the image.
                colors: Normalized RGBA colors to use for each channel.
                        If AUDIO_IMAGE_FLAG_MULTI_CHANNEL or AUDIO_IMAGE_FLAG_SPLIT_CHANNELS
                        are used, each index into this list is the color of that audio
                        channel.
                        When those flags are not set, index 0 into this list is
                        always used to render the selected channel.
                        If a color is not specified, a default color is used instead.
    
            Returns:
                A raw RGBA image with the rendered waveform.
                If the prim was not a sound prim or its asset had not been loaded
                yet, an empty list will be returned.
    """
def _get_active_listener(mgr: omni.usd._usd.AudioManager) -> str:
    """
            Get the path to the active listener prim in the scene.
    
            Args:
                No arguments.
    
            Returns:
                The path to active listener is returned, if an active listener prim
                is bound.
    
                None is returned if no active listener prim is bound, which means
                the active camera is being used as the active listener.
    """
def _get_concurrent_voices(mgr: omni.usd._usd.AudioManager) -> int:
    """
            Get the minimum number of sounds in a scene that can be played
            concurrently.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
    
            Returns:
                The minimum number of sounds in a scene that can be played
                concurrently.
    """
def _get_distance_delay_default(mgr: omni.usd._usd.AudioManager) -> FeatureDefault:
    """
            Get the default value for whether distance delayed audio is enable for
            the current USD Stage.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
    
            Returns:
                The default value for whether distance delayed audio is enable for
                the current USD Stage.
    """
def _get_doppler_default(mgr: omni.usd._usd.AudioManager) -> FeatureDefault:
    """
            Get the default value for whether doppler calculations are enabled for
            the current USD Stage.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
    
            Returns:
                The default value for whether doppler calculations are enabled for
                the current USD Stage.
    """
def _get_doppler_limit(mgr: omni.usd._usd.AudioManager) -> float:
    ...
def _get_doppler_scale(mgr: omni.usd._usd.AudioManager) -> float:
    """
            Gets the scaler that can exaggerate or lessen the Doppler effect.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
    
            Returns:
                The scaler that can exaggerate or lessen the Doppler effect.
    """
def _get_interaural_delay_default(mgr: omni.usd._usd.AudioManager) -> FeatureDefault:
    """
            Get the default value for whether interaural delay is enabled for the
            current USD Stage.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
    
            Returns:
                The default value for whether interaural delay is enabled for the
                current USD Stage.
    """
def _get_listener_by_index(mgr: omni.usd._usd.AudioManager, index: int) -> typing.Any:
    """
            Retrieves the SDF path of a single listener prim currently in the stage.
    
            Args:
                index: The zero based index of the listener to retrieve the SDF path
                       for.  This should be strictly less than the most recent return
                       value of _get_listener_count().
    
            Returns:
                The path to the requested indexed listener in the stage.
    
                None is returned if the given index was out of bounds of the number of
                listeners in the stage.
    """
def _get_listener_count(mgr: omni.usd._usd.AudioManager) -> int:
    """
            Retrieves the total number of listener prims currently in the stage.
    
            Args:
                No arguments.
    
            Returns:
                The total number of listener prims currently in the stage.  Note that
                this may change at any time due to user or script action so it is best
                to call this immediately before enumerating listeners.
    """
def _get_metadata_change_stream(mgr: omni.usd._usd.AudioManager) -> carb.events._events.IEventStream:
    """
            Retrieve the event stream for metadata changes.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
    
            Returns:
                An IEventStream which is pushed when metadata is changed.
    
                None if the event stream could not be created for some reason.
    """
def _get_nonspatial_time_scale(mgr: omni.usd._usd.AudioManager) -> float:
    """
            Gets the timescale modifier for all non-spatial voices.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
    
            Returns:
                The timescale modifier for all non-spatial voices.
    """
def _get_sound_asset_status(mgr: omni.usd._usd.AudioManager, path: str) -> AssetLoadStatus:
    """
            Queries whether the asset of an individual sound has been fully loaded.
    
            Once the asset of a sound has been fully loaded, it should be possible
            to play with _play_sound().
    
            Args:
                mgr: the AudioManager instance that this function acts upon.
                path The path to sound prim to retrieve the status of.
    
            Returns:
                AssetLoadStatus.IN_PROGRESS if the asset is in the process of loading.
                AssetLoadStatus.DONE if the asset has finished loading and is ready
                for immediate playback.
                AssetLoadStatus.FAILED if the asset has failed to load.
                AssetLoadStatus.NOT_REGISTERED if the sound prim is not of type Sound
                or the path corresponds to a prim that doesn't exist.
    """
def _get_sound_count(mgr: omni.usd._usd.AudioManager) -> int:
    """
            Retrieves the total number of registered sound objects in the USD stage.
    
            Args:
                mgr: the AudioManager instance that this function acts upon.
    
            Returns:
                The total number of sound prims in the current USD stage.
    """
def _get_sound_length(mgr: omni.usd._usd.AudioManager, path: str, length_type: SoundLengthType = ...) -> float:
    """
            Retrieves length of a sound in seconds (if known).
    
            This calculates the length of a USD stage sound in seconds.  This will be the lesser of
            the difference between the sound's start and end times (if an end time is set on the prim)
            or the length of the actual sound asset itself (if not looping).  In either case, this
            will be the amount of time that the sound would be expected to play for if it were
            triggered.  For sounds that are set to loop, the returned time will include all scheduled
            loop iterations.  For sounds that are set to loop infinitely, this will be a very large
            number (on the scale of 100 days).
    
            Args:
                mgr: The AudioManager instance that this function acts upon.
                path: The SDF path of the sound prim to query the length of.
                length_type: How the length of the sound is measured.
                  Valid values are:
                   * SoundLengthType.PLAY_LENGTH: The length of time the sound is estimated to play
                     for in the stage once it's triggered.
                     This will be the lesser of the difference between the sound's start and end
                     times (if an end time is set on the prim) or the length of the actual sound
                     itself, multiplied by loop count.
                     Note that timeScale is taken into account when calculating the play time
                     of an asset.
                     For sounds that are set to loop infinitely, this will be a very large number
                     (on the scale of 100 days).
                   * SoundLengthType.SOUND_LENGTH: The length of the sound.
                     This doesn't include the sound's start time, end time or loop count.
                     This is calculated using mediaOffsetStart and mediaOffsetEnd if those are set;
                     otherwise, this just returns the sound asset's length.
                   * SoundLengthType.ASSET_LENGTH: The length of the underlying sound asset,
                     ignoring any USD parameters.
    
            Returns:
                The play length of the sound in seconds if the asset is loaded and the length can be
                calculated.
    
                0.0 if the sound asset is not available yet or the length could not be properly
                calculated.
    """
def _get_spatial_time_scale(mgr: omni.usd._usd.AudioManager) -> float:
    """
            This gets the timescale modifier for all spatial voices.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
    
            Returns:
                The timescale modifier for all spatial voices.
    """
def _get_speed_of_sound(mgr: omni.usd._usd.AudioManager) -> float:
    """
            Gets the speed of sound in the medium surrounding the listener.
            This is measured in meters per second.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
    
            Returns:
                The speed of sound in the medium surrounding the listener.
    """
def _is_sound_playing(mgr: omni.usd._usd.AudioManager, path: str) -> bool:
    """
            Queries whether a sound object is currently playing.
    
            This queries whether a sound is currently playing.  If this fails, that may mean that the
            sound ended naturally on its own or it was explicitly stopped.  Note that this may continue
            to return true for a short period after a sound has been stopped with stop_sound() or
            stop_all_sounds().  This period may be up to 20 milliseconds in extreme cases but will
            usually not exceed 10 milliseconds.
    
            This only checks the most recently playing instance of a sound,
            if multiple simultaneous sounds have been spawned with playSound().
    
            Args:
                mgr: the AudioManager instance that this function acts upon.
                path: the SDF path of the sound prim to query the playing state for.
    
            Returns:
                true if the sound object is currently playing.
    
                false if the sound has either finished playing or has not been played yet.
    """
def _play_sound(mgr: omni.usd._usd.AudioManager, path: str) -> None:
    """
            Immediately plays the requested USD stage sound if it is loaded.
    
            This plays a single non-looping instance of a USD stage sound immediately.  The sound must
            have already been loaded.  If the sound resource was missing or couldn't be loaded, this
            call will simply be ignored.  This will return immediately after scheduling the sound to
            play.  It will never block for the duration of the sound playback.  This sound may be
            prematurely stopped with stop_sound().
    
            The loopCount parameter of the prim parameter is ignored in this call.
            This functionality will be added in a future revision.
    
            Sound prims that are scheduled to play in an animation should not also
            be played with playSound(), since it may prevent them from playing
            when they are scheduled to play.
            This will be fixed in a future revision.
    
            Args:
                mgr: the AudioManager instance that this function acts upon.
                path: the SDF path of the sound prim to play.
    
            Returns:
                No return value.
    """
def _set_active_listener(mgr: omni.usd._usd.AudioManager, path: str) -> bool:
    """
            Change the active Listener prim in the scene.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
                path: The path to the Listener prim to set.
                      This can be None to leave the active camera as the active
                      listener.
    
            Returns:
                True if the prim at @p path was set as the active prim.
                False if the prim at @p path was not registered with hydra.
                This can occur if hydra has not informed the audio manager about
                its existence yet.
    """
def _set_capture_filename(mgr: omni.usd._usd.AudioManager, id: int, filename: str) -> bool:
    """
            Sets the filename that a capture streamer will write to.
    
            Args:
                mgr: the audio manager that owns the streamer id.  This may not be None.
                id: the streamer to set the filename for.  This handle will have been
                    returned from a previous call to create_capture_streamer().  This may
                    not be INVALID_STREAMER_ID.
                filename: the name and path of the file to write the streamer's data to once
                          its capture is started.  If the filename is set here, a None
                          filename may be passed into start_capture().  This may be an
                          empty string to clear the streamer's filename.
    
            Returns:
                True if the given filename is valid and writable.
                False if the given filename could not be opened for writing.
    """
def _set_concurrent_voices(mgr: omni.usd._usd.AudioManager, value: int) -> None:
    """
            The minimum number of sounds in a scene that can be played
            concurrently.
    
            In a scene where `concurrentVoices` is set to `N` and `N + 1`
            sounds are played concurrently, Omniverse Kit will choose to not play
            the `N+1` th sound to the audio device and just track it as a 'virtual'
            voice.
            The voices chosen to become 'virtual' will be the lowest priority or
            silent. A 'virtual' voice should begin playing again once there is an
            empty voice to play on.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
                value: The new value for the number of concurrent voices.
    
            Returns:
                No return value.
    """
def _set_device(mgr: omni.usd._usd.AudioManager, deviceName: str) -> None:
    """
            Switches to use a new device for for audio output.
    
            This sets the device that the audio manager will use for its output.  If the
            requested device cannot be used for any reason, the default output device will
            be used instead.  The device may change the final output format.  If a streamer
            is attached to the previous output, its stream will be closed before opening
            a new stream on the new device.  Even if the new device name matches the current
            device's name, the device will still be changed and any stream reset.
    
            If multiple devices attached to the system have the same name, the one that is
            chosen may be undefined.  This can be a common issue with certain devices showing
            up in the system as simply "Speakers".  Using the device's GUID instead will allow
            a specific device to be used instead, even its name exactly matches that of another
            device.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be ptr.
                deviceName: The name or GUID of the device to set as active.  This must
                            exactly match the name or GUID of one of the devices attached
                            to the system at the time.  If the given name or GUID doesn't
                            match one of the connected devices, the default device will be
                            used instead.  This may be set to nullptr or an empty string
                            to use the system's default device.  This device name may be
                            retrieved from the IAudioDeviceEnum interface.
    
            Returns:
                No return value.
    """
def _set_distance_delay_default(mgr: omni.usd._usd.AudioManager, value: FeatureDefault) -> None:
    """
            Set the default value for whether distance delayed audio is enable for
            the current USD Stage.
    
            This will append the USD Stage metadata to add this new scene setting.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
                value: The value to set this as.
                       This must be one of the following values:
    
                       - FeatureDefault.ON: Sounds with enableDistanceDelay set to
                         "default" will have distance delay effects applied.
                       - FeatureDefault.OFF:  Sounds with enableDistanceDelay set
                         to "default" will not have distance delay effects applied.
                         This is the default because distance delay can have a very
                         confusing effect if worldUnitScale hasn't been set
                         correctly.
                       - FeatureDefault.FORCE_ON: all Sounds will have distance
                         delay effects applied.  This setting is intended to let
                         users test what effect distance delay is having on their
                         scene without requiring all Sounds to have their
                         enableDistanceDelay property set to "default".
                       - FeatureDefault.FORCE_OFF: all Sounds will have distance
                         delay effects disabled.  This setting is intended to let
                         users test what effect distance delay having on their
                         scene without requiring all Sounds to have their
                         enableDistanceDelay property set to "default".
    
            Returns:
                No return value.
    """
def _set_doppler_default(mgr: omni.usd._usd.AudioManager, value: FeatureDefault) -> None:
    """
            Set the default value for whether doppler calculations are enabled for
            the current USD Stage.
    
            This will append the USD Stage metadata to add this new scene setting.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
                value: The value to set this as.  This must be one of the following
                       values:
    
                       - FeatureDefault.ON: Sounds with enableDoppler set to
                         "default" will have Doppler effects applied.
                       - FeatureDefault.OFF:  Sounds with enableDoppler set to
                         "default" will not have Doppler effects applied.
                         This is the default because Doppler effect's implementation
                         is still experimental. The default will be switched to
                         FeatureDefault.ON when the feature is stabilized.
                       - FeatureDefault.FORCE_ON: all Sounds will have Doppler
                         effects applied.
                         This setting is intended to let users test what effect the
                         Doppler effect is having on their scene without requiring
                         all Sounds to have their enableDoppler property set to
                         "default".
                       - FeatureDefault.FORCE_OFF: all Sounds will have Doppler
                         effects disabled.
                         This setting is intended to let users test what effect the
                         Doppler effect having on their scene without requiring all
                         Sounds to have their enableDoppler property set to
                         "default".
    
            Returns:
                No return value.
    """
def _set_doppler_limit(mgr: omni.usd._usd.AudioManager, value: float) -> None:
    ...
def _set_doppler_scale(mgr: omni.usd._usd.AudioManager, value: float) -> None:
    """
            Sets a scaler that can exaggerate or lessen the Doppler effect.
            Setting this above 1.0 will exaggerate the Doppler effect.
            Setting this below 1.0 will lessen the Doppler effect.
            Negative values and zero are not allowed.
            Doppler effects alter the pitch of a sound based on its relative
            velocity to the listener.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
                value: The new value for the doppler scale.
    
            Returns:
                No return value.
    """
def _set_interaural_delay_default(mgr: omni.usd._usd.AudioManager, value: FeatureDefault) -> None:
    """
            Set the default value for whether interaural delay is enabled for the
            current USD Stage.
    
            This will append the USD Stage metadata to add this new scene setting.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
                value: The value to set.  This must be one of the following values:
    
                       - FeatureDefault.ON: Sounds with enableInterauralDelay set
                         to "default" will have interaural delay effects applied.
                         This is the default.
                       - FeatureDefault.OFF:  Sounds with enableInterauralDelay set
                         to "default" will not have interaural delay effects applied.
                       - FeatureDefault.FORCE_ON: all Sounds will have interaural
                         delay effects applied.
                         This setting is intended to let users test what effect
                         interaural delay is having on their scene without
                         requiring all Sounds to have their enableInterauralDelay
                         property set to "default".
                       - FeatureDefault.FORCE_OFF: all Sounds will have distance
                         delay effects disabled.
                         This setting is intended to let users test what effect
                         interaural delay having on their scene without requiring
                         all Sounds to have their enableInterauralDelay property
                         set to "default".
    
            Returns:
                No return value.
    """
def _set_nonspatial_time_scale(mgr: omni.usd._usd.AudioManager, value: float) -> None:
    """
            Sets the timescale modifier for all non-spatial voices.
            Each prim multiplies its timeScale attribute by this value.
            For example, setting this to 0.5 will play all non-spatial sounds at
            half speed and setting this to 2.0 will play all non-spatial sounds at
            double speed.
            Altering the playback speed of a sound will affect the pitch of the sound.
            The limits of this setting under Omniverse Kit are [1/1024, 1024].
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
                value: The new value for the non-spatial timescale.
    
            Returns:
                No return value.
    """
def _set_spatial_time_scale(mgr: omni.usd._usd.AudioManager, value: float) -> None:
    """
            This sets the timescale modifier for all spatial voices.
            Each prim multiplies its timeScale attribute by this value.
            For example, setting this to 0.5 will play all spatial sounds at half
            speed and setting this to 2.0 will play all non-spatial sounds at
            double speed.
            This affects delay times for the distance delay effect.
            Altering the playback speed of a sound will affect the pitch of the sound.
            The limits of this setting under Omniverse Kit are [1/1024, 1024].
            This feature is intended to allow time-dilation to be performed with the
            sound effects in the scene without affecting non-spatial elements like
            the background music.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
                value: The new value for the spatial timescale.
    
            Returns:
                No return value.
    """
def _set_speed_of_sound(mgr: omni.usd._usd.AudioManager, value: float) -> None:
    """
            Sets the speed of sound in the medium surrounding the listener
            (typically air).
            This is measured in meters per second.
            This would typically be adjusted when doing an underwater scene.
            The speed of sound in dry air at sea level is approximately 340.0m/s.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be None.
                value: The new value for the speed of sound.
    
            Returns:
                No return value.
    """
def _spawn_voice(mgr: omni.usd._usd.AudioManager, path: str) -> carb.audio._audio.Voice:
    """
            Immediately plays the requested USD stage sound as a new
            carb.audio.Voice if it is loaded.
    
            This begins playing the requested sound as a new carb.audio.Voice.
            The sound must have already been loaded or None will be returned.
            The spawned voice plays the sound asynchronously for the lifetime
            of the voice.
            This is intended for cases where the behavior of playSound() is too
            limiting.
    
            stopAllSounds() and stopSound() do not affect the playing voices
            spawned from this call.
    
            Unlike playSound(), the loopCount parameter of the prim is used, so
            the voice must be explicitly stopped if the voice is infinitely
            looping.
    
            Unlike playSound(), these voice handles are managed separately from
            the voice handles of the timeline, so spawning a voice from a sound
            that will play on the timeline shouldn't affect that sound's timeline
            playback.
            Stopping the timeline will also not stop these playing voices.
    
            Args:
                mgr: The stage audio manager instance that this function acts upon.
                     This must not be nullptr.
                path: The path to sound prim to spawn a voice from.
    
            Returns:
                This returns the new voice that was spawned.
                This voice's settings are only a snapshot of the sound prim that
                they were based off. Updates to these parameters will have to be
                performed on the returned voice through the IAudioPlayback interface.
    
                this returns nullptr if a new voice could not be spawned.
    """
def _start_capture(mgr: omni.usd._usd.AudioManager, id: int, filename: str) -> bool:
    """
            Starts the capture on a single streamer.
    
            Args:
                mgr: the audio manager that owns the streamer id.  This may not be None.
                id: the handle of the streamer to start.  This handle will have been
                    returned from a previous call to create_capture_streamer().  This
                    may not be INVALID_STREAMER_ID.
                filename: the name and path of the filename to write the streamer's data to
                          once its capture is started.  If a filename was set with a previous
                          call to set_capture_filename() on the same streamer, this may be
                          None to use that filename.  If a non-None and non-empty
                          filename is given here, it will always override any filename
                          previously set on the streamer.
    
            Returns:
                True if the streamer is successfully started.  Note that starting a streamer
                currently has the side effect of stopping and restarting all other streamers
                that are currently running a capture.  This will result in each streamer's
                output file being overwritten.  If multiple streamers need to be started
                simultaneously, start_captures() should be used instead.
    
                False if the streamer could not be started or the filename was not valid
                or writable.
    """
def _start_captures(mgr: omni.usd._usd.AudioManager, ids: list[int]) -> bool:
    """
            Starts multiple streamers simultaneously.  This attempts to start one or more streamers
            simultaneously.  If successful, all streamers are guaranteed to be started in sync with
            each other such that their first written audio frame matches.  If this method is used
            to start multiple streamers, the stop_captures() function must also be used to stop
            those same streamers simultaneously.  If another streamer starts or stops independently,
            it will cause all streamers to be closed then reopened which will overwrite each of
            their files.
    
            Args:
                mgr:     the audio manager that owns the streamer handles in ids.  This
                         may not be None.
                ids:     the list of streamers to start a capture on.  Any entries that
                         are set to INVALID_STREAMER_ID in this list will be ignored.
                         Each valid entry must have had its filename set with
                         set_capture_filename() first otherwise it will be skipped.  Any
                         streamer that is already running a capture will be skipped, but
                         a side effect of this operation will be that its stream will be
                         closed and reopened thereby overwriting its file.  this may not
                         be None.
    
            Returns:
                True if at least one streamer is successfully started.
    
                False if no streamers could be started or all streamers were skipped for one
                of the reasons listed under streamers.
    """
def _stop_all_sounds(mgr: omni.usd._usd.AudioManager) -> None:
    """
            Stops all currently playing USD stage sounds.
    
            This stops all currently playing stage sounds.  Any sounds that have been queued for
            playback will be stopped.  UI sounds will not be affected.  This is intended to be used
            to reset the sound playback system when an animation sequence is stopped.  This will be
            automatically called internally whenever the animation sequence is stopped or it loops.
    
            Args:
                mgr: the AudioManager instance that this function acts upon.
    
            Returns:
                No return value.
    """
def _stop_capture(mgr: omni.usd._usd.AudioManager, id: int) -> bool:
    """
            Stops the capture on a single streamer.
    
            Args:
                mgr: the audio manager that owns the streamer id.  This may not be None.
                id: the handle to the streamer to stop.  This will have been returned from
                    a previous call to create_capture_streamer().  If a capture is not running
                    on this streamer, it will be ignored.  This may not be
                    INVALID_STREAMER_ID.
    
            Returns:
                True if the streamer is successfully stopped.
    
                False if the streamer handle was invalid or a capture was not running on it.
    """
def _stop_captures(mgr: omni.usd._usd.AudioManager, ids: list[int]) -> bool:
    """
            Stops the capture on multiple streamers simultaneously.
    
            Args:
                mgr: the audio manager that owns the streamer handles in ids.  This
                     may not be None.
                ids: the list of streamers to stop the capture on.  Any
                     INVALID_STREAMER_ID entries will be ignored.  Each valid
                     entry must be currently running a capture otherwise it will be
                     skipped.  This may not be None.
    
            Returns:
                True if at least one streamer is successfully stopped.
    
                False if no streamers could be stopped.
    """
def _stop_sound(mgr: omni.usd._usd.AudioManager, path: str) -> None:
    """
            Immediately schedules the stop of the playback of a sound.
    
            This stops the playback of an active sound.  If the sound was not playing or had already
            naturally stopped on its own, this call is ignored.  Note that is_sound_playing() may
            continue to return true for a short period after a sound has been stopped for a period
            of up to 20 milliseconds in extreme cases but will usually not exceed 10 milliseconds.
    
            This only stops the most recently played instance of a sound, if
            multiple overlapping instances of a sound were played with playSound().
    
            Args:
                mgr: the AudioManager instance that this function acts upon.
                sound: the index of a sound prim to stop playback for.  This can be acquired
                    from get_sound_by_path().  This may not be *kUnknownPrim*.
    
            Returns:
                No return value.
    """
def _subscribe_to_asset_load(mgr: omni.usd._usd.AudioManager, path: str, callback: typing.Callable[[], None]) -> bool:
    """
            Bind a callback for when assets are loaded.
    
            This will fire the callback when the sound's asset is loaded or
            immediately if the asset was already loaded.
            The callback will only fire once.
    
            Args:
                mgr: The AudioManager instance that this function acts upon.
                path: The path to the sound prim to bind a callback to.
                callback: The callback to fire once a load has occurred.
    
            Returns:
                true if the callback was bound successfully.
                true if the callback was executed immediately.
                false if the prim path passed corresponds to a prim that's not of
                type Sound.
                false if the prim path passed did not correspond to any prim.
                false if an unexpected error prevents the callback from occurring.
    """
def _wait_for_capture(mgr: omni.usd._usd.AudioManager, id: int, timeout_milliseconds: int) -> bool:
    """
            Wait until the capture streamer has been disconnected.
    
            Because stop_capture() does not stop the audio system or otherwise block
            to ensure that the streamer is disconnected, you must call wait_for_capture()
            to verify that a capture streamer has actually finished.
            This is mainly useful if you need to verify that a file written by
            a streamer has finished being written.
    
            Args:
                id: the handle to the streamer to wait for.  This will have been returned from
                    a previous call to create_capture_streamer().  If a capture is not running
                    on this streamer, it will be ignored.  This may not be
                    INVALID_STREAMER_ID.
                timeout_milliseconds: The maximum number of milliseconds to wait for the streamer to close.
    
            Returns:
                True if the capture streamer has disconnected.
    
                False if the call timed out before the streamer could disconnect.
    """
def test_hydra_plugin() -> bool:
    """
            Test whether the Hydra audio plugin is accessible.
            This is intended to allow the tests to check whether the Hydra audio
            plugin is still working.
    
            Args:
                No arguments.
    
            Returns:
                True if the plugin is accessible. False otherwise.
    """
INVALID_STREAMER_ID: int = 18446744073709551615
