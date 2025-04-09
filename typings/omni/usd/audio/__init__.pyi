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
import carb as carb
import omni as omni
from omni.usd.audio._audio import AssetLoadStatus
from omni.usd.audio._audio import EventType
from omni.usd.audio._audio import FeatureDefault
from omni.usd.audio._audio import SoundLengthType
from omni.usd.audio._audio import StreamListener
from omni.usd.audio._audio import test_hydra_plugin
from . import _audio
__all__: list = ['AssetLoadStatus', 'EventType', 'FeatureDefault', 'SoundLengthType', 'StreamListener', 'IStageAudio', 'test_hydra_plugin', 'get_stage_audio_interface', 'INVALID_STREAMER_ID']
class IStageAudio:
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
    mgr = None
    def __init__(self):
        """
        
                Constructor for the IStageAudio interface instance.
                This will raise an Exception if it was unable to obtain an instance of
                the USD context interface.
                
        """
    def _get_invalid_streamer_id(self):
        ...
    def create_capture_streamer(self):
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
    def create_event_stream_for_capture(self, id):
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
    def destroy_capture_streamer(self, id):
        """
        
                Destroys a capture streamer.
        
                Note that if the capture streamer is still running, this will
                asynchronously stop the capture streamer, so the file may not be
                finished being written by the time this call returns.
                If you need to ensure that capture has finished, call stop_capture() then
                call wait_for_capture() on that streamer before calling this function.
        
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
    def draw_waveform(self, prim, width, height, flags = 34, channel = 0, background = [0, 0, 0, 1.0], colors = list()):
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
                             The channel parameter is not used when this flag is set.
                           - AUDIO_IMAGE_FLAG_ALPHA_BLEND: Each pixel drawn is alpha
                             blended into the output image.
                             This is only useful if the colors specified don't have
                             an alpha component of 1.0.
                           - AUDIO_IMAGE_FLAG_SPLIT_CHANNELS: Each channel is rendered
                             separately, organized vertically.
                             This cannot be used in combination with AUDIO_IMAGE_FLAG_MULTI_CHANNEL;
                             the rendering style chosen in this case is undefined.
                             The channel parameter is not used when this flag is set.
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
    def get_active_listener(self):
        """
        
                Get the active listener prim in the scene.
        
                Args:
                    No arguments.
        
                Returns:
                    The active listener is returned, if an active listener prim is bound.
        
                    None is returned if no active listener prim is bound, which means
                    the active camera is being used as the active listener.
                
        """
    def get_concurrent_voices(self):
        """
        
                Get the minimum number of sounds in a scene that can be played
                concurrently.
        
                Args:
                    No arguments.
        
                Returns:
                    The minimum number of sounds in a scene that can be played
                    concurrently.
                
        """
    def get_distance_delay_default(self):
        """
        
                Get the default value for whether distance delayed audio is enable for
                the current USD Stage.
        
                Args:
                    No arguments.
        
                Returns:
                    The default value for whether distance delayed audio is enable for
                    the current USD Stage.
                
        """
    def get_doppler_default(self):
        """
        
                Get the default value for whether doppler calculations are enabled for
                the current USD Stage.
        
                Args:
                    No arguments.
        
                Returns:
                    The default value for whether doppler calculations are enabled for
                    the current USD Stage.
                
        """
    def get_doppler_limit(self):
        """
        
                Gets the Limit on the maximum Doppler pitch shift that can be applied
                to a playing voice.
        
                Args:
                    No arguments.
        
                Returns:
                    The Limit on the maximum Doppler pitch shift that can be applied to
                    a playing voice.
                
        """
    def get_doppler_scale(self):
        """
        
                Gets the scaler that can exaggerate or lessen the Doppler effect.
        
                Args:
                    No arguments.
        
                Returns:
                    The scaler that can exaggerate or lessen the Doppler effect.
                
        """
    def get_interaural_delay_default(self):
        """
        
                Get the default value for whether interaural delay is enabled for the
                current USD Stage.
        
                Args:
                    No arguments.
        
                Returns:
                    The default value for whether interaural delay is enabled for the
                    current USD Stage.
                
        """
    def get_listener_by_index(self, index):
        """
        
                Retrieves a single listener prim currently in the stage.
        
                Args:
                    index: The zero based index of the listener to retrieve the SDF path
                           for.  This should be strictly less than the most recent return
                           value of _get_listener_count().
        
                Returns:
                    The requested indexed listener prim in the stage if the index is valid.
        
                    None is returned if the given index was out of bounds of the number of
                    listeners in the stage.
                
        """
    def get_listener_count(self):
        """
        
                Retrieves the total number of listener prims currently in the stage.
        
                Args:
                    No arguments.
        
                Returns:
                    The total number of listener prims currently in the stage.  Note that
                    this may change at any time due to user or script action so it is best
                    to call this immediately before enumerating listeners.
                
        """
    def get_metadata_change_stream(self):
        """
        
                Retrieve the event stream for metadata changes.
        
                Args:
                    mgr: The stage audio manager instance that this function acts upon.
                         This must not be None.
        
                Returns:
                    An IEventStream which is pushed when metadata is changed.
        
                    None if the event stream could not be created for some reason.
                
        """
    def get_nonspatial_time_scale(self):
        """
        
                Gets the timescale modifier for all non-spatial voices.
        
                Args:
                    No arguments.
        
                Returns:
                    The timescale modifier for all non-spatial voices.
                
        """
    def get_sound_asset_status(self, prim):
        """
        
                Queries whether the asset of an individual sound has been fully loaded.
        
                Once the asset of a sound has been fully loaded, it should be possible
                to play with play_sound().
        
                NOTE: this function is deprecated and will be replaced with a sound
                     asset loaded callback.
        
                Args:
                    path The path to sound prim to retrieve the status of.
        
                Returns:
                    AssetLoadStatus.IN_PROGRESS if the asset is in the process of loading.
                    AssetLoadStatus.DONE if the asset has finished loading and is ready
                    for immediate playback.
                    AssetLoadStatus.FAILED if the audio manager has not loaded.
                    AssetLoadStatus.FAILED if the asset has failed to load.
                    AssetLoadStatus.NOT_REGISTERED if the sound prim is not of type Sound
                    or the path corresponds to a prim that doesn't exist.
                
        """
    def get_sound_count(self):
        """
        
                Retrieves the total number of registered sound objects in the USD stage.
        
                Returns:
                    The total number of sound prims in the current USD stage.
        
                    Sounds that have not had their asset loaded yet (or their asset
                    failed to load) will not show up in the sound count unless they've
                    been passed to an IStageAudio function.
                
        """
    def get_sound_length(self, prim, length_type = ...):
        """
        
                Retrieves length of a sound in seconds (if known).
        
                This calculates the length of a USD stage sound in seconds.  This will be the lesser of
                the difference between the sound's start and end times (if an end time is set on the prim)
                or the length of the actual sound asset itself (if not looping).  In either case, this
                will be the amount of time that the sound would be expected to play for if it were
                triggered.  For sounds that are set to loop, the returned time will include all scheduled
                loop iterations.  For sounds that are set to loop infinitely, this will be INFINITY.
        
                Args:
                    prim: The USD prim to query the length of.
                          This must be of type OmniAudioSchemaOmniSound.
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
    def get_spatial_time_scale(self):
        """
        
                This gets the timescale modifier for all spatial voices.
        
                Args:
                    No arguments.
        
                Returns:
                    The timescale modifier for all spatial voices.
                
        """
    def get_speed_of_sound(self):
        """
        
                Gets the speed of sound in the medium surrounding the listener.
                This is measured in meters per second.
        
                Args:
                    No arguments.
        
                Returns:
                    The speed of sound in the medium surrounding the listener.
                
        """
    def has_audio(self):
        """
        
                Test if audio is working.
                If the audio manager has failed to load or has been explicitly disabled,
                this function will return False.
                This function will otherwise return True.
        
                Returns:
                    True if audio is in a working state.
                    False if audio is in a disabled state.
                
        """
    def is_sound_playing(self, prim):
        """
        
                Queries whether a sound object is currently playing.
        
                This queries whether a sound is currently playing.  If this fails, that may mean that the
                sound ended naturally on its own or it was explicitly stopped.  Note that this may continue
                to return true for a short period after a sound has been stopped with stop_sound() or
                stop_all_sounds().  This period may be up to 20 milliseconds in extreme cases but will
                usually not exceed 10 milliseconds.
        
                This only checks the most recently playing instance of a sound, if multiple
                simultaneous sounds have been spawned with playSound().
        
                Args:
                    prim: The USD prim to query the playing state for.
                          This must be of type OmniAudioSchemaOmniSound.
        
                Returns:
                    true if the sound object is currently playing.
        
                    false if the sound has either finished playing or has not been played yet.
                
        """
    def play_sound(self, prim):
        """
        
                Immediately plays the requested USD stage sound if it is loaded.
        
                This plays a single non-looping instance of a USD stage sound immediately.  The sound must
                have already been loaded.  If the sound resource was missing or couldn't be loaded, this
                call will simply be ignored.  This will return immediately after scheduling the sound to
                play.  It will never block for the duration of the sound playback.  This sound may be
                prematurely stopped with stop_sound().
        
                The loopCount parameter of the prim parameter is ignored in this call.
                This functionality will be added in a future revision.
        
                Sound prims that are scheduled to play in an animation should not also be
                played with playSound(), since it may prevent them from playing when they
                are scheduled to play.
                This will be fixed in a future revision.
        
                Args:
                    prim: The USD prim to play.
                          This must be of type OmniAudioSchemaOmniSound.
        
                Returns:
                    No return value.
                
        """
    def set_active_listener(self, prim):
        """
        
                Change the active Listener prim in the scene.
        
                Note that updating the active Listener's uniform attributes, such as
                orientationFromView, will reset the active listener back to the active
                camera.
        
                Args:
                    prim: The prim to set as the active listener.
                          This can be None to use the active camera as the active
                          listener.
        
                Returns:
                    True if the prim at @p path was set as the active prim.
                    False if the prim at @p path was not registered with hydra.
                    This can occur if hydra has not informed the audio manager about
                    its existence yet.
                
        """
    def set_capture_filename(self, id, filename):
        """
        
                Sets the filename that a capture streamer will write to.
        
                Args:
                    mgr: the audio manager that owns the streamer id.  This may not be None.
                    id: the streamer to set the filename for.  This handle will have been
                        returned from a previous call to create_capture_streamer().  This may
                        not be INVALID_STREAMER_ID.
                    filename: the name and path of the file to write the streamer's data to once
                              its capture is started.  If the filename is set here, a None
                              filename may be passed into start_capture().
        
                Returns:
                    no return value.
                
        """
    def set_concurrent_voices(self, value = 64):
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
                    value: The new value for the number of concurrent voices.
        
                Returns:
                    No return value.
                
        """
    def set_device(self, deviceName):
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
                    deviceName: The name or GUID of the device to set as active.  This must
                                exactly match the name or GUID of one of the devices attached
                                to the system at the time.  If the given name or GUID doesn't
                                match one of the connected devices, the default device will be
                                used instead.  This may be set to nullptr or an empty string
                                to use the system's default device.  This device name or
                                identifier may be retrieved from the IAudioDeviceEnum
                                interface.
        
                Returns:
                    No return value.
                
        """
    def set_distance_delay_default(self, value = ...):
        """
        
                Set the default value for whether distance delayed audio is enable for
                the current USD Stage.
        
                This will append the USD Stage metadata to add this new scene setting.
        
                Args:
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
    def set_doppler_default(self, value = ...):
        """
        
                Set the default value for whether doppler calculations are enabled for
                the current USD Stage.
        
                This will append the USD Stage metadata to add this new scene setting.
        
                Args:
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
    def set_doppler_limit(self, value = 2.0):
        """
        
                Sets a Limit on the maximum Doppler pitch shift that can be applied to
                a playing voice. Since Omniverse Kit does not handle supersonic spatial
                audio, a maximum frequency shift must be set for prims that move toward
                the listener at or faster than the speed of sound.
                This is mostly useful for handling edge cases such as teleporting an
                object far away while it's playing a sound.
        
                Args:
                    value: The new value for the doppler limit.
        
                Returns:
                    No return value.
                
        """
    def set_doppler_scale(self, value = 1.0):
        """
        
                Sets a scaler that can exaggerate or lessen the Doppler effect.
                Setting this above 1.0 will exaggerate the Doppler effect.
                Setting this below 1.0 will lessen the Doppler effect.
                Negative values and zero are not allowed.
                Doppler effects alter the pitch of a sound based on its relative
                velocity to the listener.
        
                Args:
                    value: The new value for the doppler scale.
        
                Returns:
                    No return value.
                
        """
    def set_interaural_delay_default(self, value = ...):
        """
        
                Set the default value for whether interaural delay is enabled for the
                current USD Stage.
        
                This will append the USD Stage metadata to add this new scene setting.
        
                Args:
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
    def set_nonspatial_time_scale(self, value = 1.0):
        """
        
                Sets the timescale modifier for all non-spatial voices.
                Each prim multiplies its timeScale attribute by this value.
                For example, setting this to 0.5 will play all non-spatial sounds at
                half speed and setting this to 2.0 will play all non-spatial sounds at
                double speed.
                Altering the playback speed of a sound will affect the pitch of the sound.
                The limits of this setting under Omniverse Kit are [1/1024, 1024].
        
                Args:
                    value: The new value for the non-spatial timescale.
        
                Returns:
                    No return value.
                
        """
    def set_spatial_time_scale(self, value = 1.0):
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
                    value: The new value for the spatial timescale.
        
                Returns:
                    No return value.
                
        """
    def set_speed_of_sound(self, value = 340.0):
        """
        
                Sets the speed of sound in the medium surrounding the listener
                (typically air).
                This is measured in meters per second.
                This would typically be adjusted when doing an underwater scene.
                The speed of sound in dry air at sea level is approximately 340.0m/s.
        
                Args:
                    value: The new value for the speed of sound.
        
                Returns:
                    No return value.
                
        """
    def spawn_voice(self, prim):
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
                    path: The path to sound prim to spawn a voice from.
        
                Returns:
                    This returns the new voice that was spawned.
                    This voice's settings are only a snapshot of the sound prim that
                    they were based off. Updates to these parameters will have to be
                    performed on the returned voice through the IAudioPlayback interface.
        
                    this returns nullptr if a new voice could not be spawned.
                
        """
    def start_capture(self, id, filename = None):
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
        
                    False if the streamer could not be started.
                
        """
    def start_captures(self, ids):
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
    def stop_all_sounds(self):
        """
        
                Stops all currently playing USD stage sounds.
        
                This stops all currently playing stage sounds.  Any sounds that have been queued for
                playback will be stopped.  UI sounds will not be affected.  This is intended to be used
                to reset the sound playback system when an animation sequence is stopped.  This will be
                automatically called internally whenever the animation sequence is stopped or it loops.
        
                Returns:
                    No return value.
                
        """
    def stop_capture(self, id):
        """
        
                Stops the capture on a single streamer.
        
                This will asynchronously stop the capture streamer, so the file may not
                be finished being written by the time this call returns.
                If you need to ensure that capture has finished, call wait_for_capture().
        
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
    def stop_captures(self, ids):
        """
        
                Stops the capture on multiple streamers simultaneously.
        
                This will asynchronously stop the capture streamer, so the file may not
                be finished being written by the time this call returns.
                If you need to ensure that capture has finished, call wait_for_capture().
        
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
    def stop_sound(self, prim):
        """
        
                Immediately schedules the stop of the playback of a sound.
        
                This stops the playback of an active sound.  If the sound was not playing or had already
                naturally stopped on its own, this call is ignored.  Note that is_sound_playing() may
                continue to return true for a short period after a sound has been stopped for a period
                of up to 20 milliseconds in extreme cases but will usually not exceed 10 milliseconds.
        
                This only stops the most recently played instance of a sound, if
                multiple overlapping instances of a sound were played with playSound().
        
                Args:
                    prim: The USD prim to stop.
                          This must be of type OmniAudioSchemaOmniSound.
        
                Returns:
                    No return value.
                
        """
    def subscribe_to_asset_load(self, prim, callback):
        """
        
                Bind a callback for when assets are loaded.
        
                This will fire the callback when the sound's asset is loaded or
                immediately if the asset was already loaded.
                The callback will only fire once.
        
                Args:
                    prim: The sound prim to bind a callback to.
                    callback: The callback to fire once a load has occurred.
        
                Returns:
                    true if the callback was bound successfully.
                    true if the callback was executed immediately.
                    false if the prim path passed corresponds to a prim that's not of
                    type Sound.
                    false if an unexpected error prevents the callback from occurring.
                
        """
    def wait_for_capture(self, id, timeout_milliseconds):
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
    @property
    def INVALID_STREAMER_ID(self):
        ...
def get_stage_audio_interface() -> IStageAudio:
    """
    
        helper method to retrieve a cached version of the IStageAudio interface.
    
        Returns:
            The :class:`omni.usd.audio.IStageAudio` interface.
        
    """
INVALID_STREAMER_ID: int = 18446744073709551615
