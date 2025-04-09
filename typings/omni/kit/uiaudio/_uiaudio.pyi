"""

        This module contains bindings to the C++ omni::audio::IUiAudio interface.
        This provides functionality for playing sounds through the editor UI.

        Sound files may be in RIFF/WAV, Ogg, or FLAC format.
        Data in the sound files may use 8, 16, 24, or 32 bit integer samples,
        or 32 bit floating point samples.  Channel counts may be from 1 to 64
        If more channels of data are provided than the audio device can play,
        some channels will be blended together automatically.
    
"""
from __future__ import annotations
__all__ = ['IUiAudio', 'UiSound', 'acquire_ui_audio_interface']
class IUiAudio:
    """
    
            This interface contains functions for playing audio in editor UI.  This is intended to be used
            to provide auditory feedback to the user for events such as errors or long processing steps
            completing.
    
            The sounds loaded by this interface will persist until destroyed and can be played any number of
            times as needed.  Any particular sound file will only be loaded into memory once and will be shared
            by all callers that try to load it.  Each call to create a new sound object must be paired with a
            call to destroy it once it is no longer needed.
    
            Up to 64 sounds may be playing at any given time for the editor UI.  Playing a sound will only
            schedule it to be played then return immediately.  The sound will continue to play.  Callers can
            block until a sound has finished playing or query whether it has finished playing by using The
            IUiAudio::isSoundPlaying() call.  It is best practice to use monaural or stereo sounds for
            this interface since they use less memory, are processed more easily, and will typically play
            as expected through all devices.
    
            Note that if a single long sound object is played multiple times simultaneously, attempting to
            stop or query the playing sound will only affect the most recently played instance of it.  In
            this case, all other instances will continue playing until they finish naturally.
    
            All the function in this interface are in omni.kit.audio.IUiAudio class.  To retrieve
            this object, use get_ui_audio_interface() method:
    
            >>> import omni.kit.audio
            >>> a = omni.kit.audio.get_ui_audio_interface()
            >>> sound = a.create_sound("${sounds}/test.wav")
            >>> a.play_sound(sound)
        
    """
    def create_sound(self, filename: str) -> UiSound:
        """
                Loads a UI sound from local disk.
        
                This loads a sound that can be played with play_sound() at a later time.  This
                sound only needs to be loaded once but can be played as many times as needed.
                When no longer needed, the sound will be destroyed when it is cleared out or
                is garbage collected.
        
                File names passed in here may contain special path markers.  The guaranteed
                set of markers are as follows (note that other special paths may also exist
                but are not included here):
        
                * "*${executable}*": resolves to the directory containing the main executable
                  file.
                * "*${resources}*": resolves to the 'resources/' folder in the same directory
                  as the main executable file.
                * "*${sounds}*": resolves to the 'resources/sounds/' folder in the same directory
                  as the main executable.
                * "*${icons}*": resolves to the 'resources/icons/' folder in the same directory
                  as the main executable.
        
                Args:
                    filename: the path to the sound file to load.  This should be an absolute
                        path, but can be a relative path that will be resolved using the current
                        working directory for the process.  Parts of this path may include some
                        special path specifiers that will be resolved when trying to open the
                        file.  See above for more info on special paths.  This may not be *None*
                        or an empty string.
        
                Returns:
                    If successful, this return the sound object representing the new loaded sound.
                    This sound can be passed to play_sound() later.  Each sound object returned
                    here will be destroyed when it is cleared out or garbage collected.  Note that
                    destroying the sound object will stop all playing instances of it.  However, if
                    more than one reference to the same sound object still exists, destroying one of
                    the sound objects (ie: assigning it to *None* or letting it get garbage collected)
                    will not stop any of the instances from playing.  It is best practice to always
                    explicitly stop a sound before destroying it.
        
                    If the requested sound file could not be found or loaded, None will be returned.
        """
    def get_sound_length(self, sound: UiSound) -> float:
        """
                Retrieves length of a sound in seconds (if known).
        
                This calculates the length of a UI sound in seconds.  This is just the length
                of the sound asset in seconds.
        
                Args:
                    sound: the sound to retrieve the length for.  This may not be *None*.
        
                Returns:
                    The play length of the sound in seconds if the asset is loaded and the length
                    can be calculated, or 0.0 otherwise.
        """
    def is_sound_playing(self, sound: UiSound) -> bool:
        """
                Queries whether a sound object is currently playing.
        
                This queries whether a sound is currently playing.  If this fails, that may mean the
                sound ended naturally on its own or it was explicitly stopped.  Note that this may
                continue to return true for a short period after a sound has been stopped with
                stop_sound().  This period may be up to 20 milliseconds in extreme cases but will
                usually not exceed 10 milliseconds.
        
                Args:
                    sound: the sound to query the playing state for.  This may not be *None*.
        
                Returns:
                    true if the sound object is currently playing, or false if the sound has either
                    finished playing or has not been played yet.
        """
    def play_sound(self, sound: UiSound) -> None:
        """
                Immediately plays the requested UI sound if it is loaded.
        
                This plays a single non-looping instance of a UI sound immediately.  The UI sound
                must have already been loaded with create_sound().  If the sound resource was missing
                or couldn't be loaded, this call will simply be ignored.  This will return immediately
                after scheduling the sound to play.  It will never block for the duration of the sound's
                playback.  This sound may be prematurely stopped with stop_sound().
        
                Args:
                    sound: the sound to be played.  This may not be *None*.
        
                Returns:
                    No return value.
        """
    def stop_sound(self, sound: UiSound) -> None:
        """
                Immediately stops the playback of a sound.
        
                This stops the playback of an active sound.  If the sound was not playing or had
                already naturally stopped on its own, this call is ignored.
        
                Args:
                    sound: the sound object to stop playback for.  This may not be *None*.
        
                Returns:
                    No return value.
        """
class UiSound:
    """
    
            An opaque object representing a loaded UI sound.  This object is used for the
            IUiAudio interface.  These objects may be passed to many of the other methods in
            the IUiAudio interface to operate on.  These objects are acquired from the create_sound()
            method.  The sound object will be destroyed when it is either cleared out (ie: assigned
            *None*) or gets garbage collected.
        
    """
def acquire_ui_audio_interface(plugin_name: str = None, library_path: str = None) -> IUiAudio:
    ...
