from __future__ import annotations
import pxr.UsdGeom
import typing
__all__ = ['SpatialAudio', 'Tokens']
class SpatialAudio(pxr.UsdGeom.Xformable):
    """
    
    The SpatialAudio primitive defines basic properties for encoding
    playback of an audio file or stream within a USD Stage. The
    SpatialAudio schema derives from UsdGeomXformable since it can support
    full spatial audio while also supporting non-spatial mono and stereo
    sounds. One or more SpatialAudio prims can be placed anywhere in the
    namespace, though it is advantageous to place truly spatial audio
    prims under/inside the models from which the sound emanates, so that
    the audio prim need only be transformed relative to the model, rather
    than copying its animation.
    
    Timecode Attributes and Time Scaling
    ====================================
    
    *startTime* and *endTime* are timecode valued attributes which gives
    them the special behavior that layer offsets affecting the layer in
    which one of these values is authored are applied to the attribute's
    value itself during value resolution. This allows audio playback to be
    kept in sync with time sampled animation as the animation is affected
    by layer offsets in the composition. But this behavior brings with it
    some interesting edge cases and caveats when it comes to layer offsets
    that include scale.
    
    Although authored layer offsets may have a time scale which can scale
    the duration between an authored *startTime* and *endTime*, we make no
    attempt to infer any playback dilation of the actual audio media
    itself. Given that *startTime* and *endTime* can be independently
    authored in different layers with differing time scales, it is not
    possible, in general, to define an"original timeframe"from which we
    can compute a dilation to composed stage-time. Even if we could
    compute a composed dilation this way, it would still be impossible to
    flatten a stage or layer stack into a single layer and still retain
    the composed audio dilation using this schema.
    
    Although we do not expect it to be common, it is possible to apply a
    negative time scale to USD layers, which mostly has the effect of
    reversing animation in the affected composition. If a negative scale
    is applied to a composition that contains authored *startTime* and
    *endTime*, it will reverse their relative ordering in time. Therefore,
    we stipulate when *playbackMode*
    is"onceFromStartToEnd"or"loopFromStartToEnd", if *endTime* is less
    than *startTime*, then begin playback at *endTime*, and continue until
    *startTime*. When *startTime* and *endTime* are inverted, we do not,
    however, stipulate that playback of the audio media itself be
    inverted, since doing so"successfully"would require perfect knowledge
    of when, within the audio clip, relevant audio ends (so that we know
    how to offset the reversed audio to align it so that we reach
    the"beginning"at *startTime*), and sounds played in reverse are not
    likely to produce desirable results.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdMediaTokens. So to set an attribute to the value"rightHanded",
    use UsdMediaTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateAuralModeAttr(*args, **kwargs):
        """
        
        CreateAuralModeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetAuralModeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateEndTimeAttr(*args, **kwargs):
        """
        
        CreateEndTimeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetEndTimeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateFilePathAttr(*args, **kwargs):
        """
        
        CreateFilePathAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetFilePathAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateGainAttr(*args, **kwargs):
        """
        
        CreateGainAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetGainAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateMediaOffsetAttr(*args, **kwargs):
        """
        
        CreateMediaOffsetAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetMediaOffsetAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreatePlaybackModeAttr(*args, **kwargs):
        """
        
        CreatePlaybackModeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetPlaybackModeAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateStartTimeAttr(*args, **kwargs):
        """
        
        CreateStartTimeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetStartTimeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> SpatialAudio
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> SpatialAudio
        
        
        Return a UsdMediaSpatialAudio holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdMediaSpatialAudio(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetAuralModeAttr(*args, **kwargs):
        """
        
        GetAuralModeAttr() -> Attribute
        
        
        Determines how audio should be played.
        
        
        Valid values are:
        
           - spatial: Play the audio in 3D space if the device can support
             spatial audio. if not, fall back to mono.
        
           - nonSpatial: Play the audio without regard to the SpatialAudio
             prim's position. If the audio media contains any form of stereo or
             other multi-channel sound, it is left to the application to determine
             whether the listener's position should be taken into account. We
             expect nonSpatial to be the choice for ambient sounds and music sound-
             tracks.
        
        Declaration
        
        ``uniform token auralMode ="spatial"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        spatial, nonSpatial
        
        
        
        """
    @staticmethod
    def GetEndTimeAttr(*args, **kwargs):
        """
        
        GetEndTimeAttr() -> Attribute
        
        
        Expressed in the timeCodesPerSecond of the containing stage, *endTime*
        specifies when the audio stream will cease playing during animation
        playback if the length of the referenced audio clip is longer than
        desired.
        
        
        This only applies if *playbackMode* is set to onceFromStartToEnd or
        loopFromStartToEnd, otherwise the *endTimeCode* of the stage is used
        instead of *endTime*. If *endTime* is less than *startTime*, it is
        expected that the audio will instead be played from *endTime* to
        *startTime*. Note that *endTime* is expressed as a timecode so that
        the stage can properly apply layer offsets when resolving its value.
        See Timecode Attributes and Time Scaling for more details and caveats.
        
        Declaration
        
        ``uniform timecode endTime = 0``
        
        C++ Type
        
        SdfTimeCode
        
        Usd Type
        
        SdfValueTypeNames->TimeCode
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetFilePathAttr(*args, **kwargs):
        """
        
        GetFilePathAttr() -> Attribute
        
        
        Path to the audio file.
        
        
        In general, the formats allowed for audio files is no more constrained
        by USD than is image-type. As with images, however, usdz has stricter
        requirements based on DMA and format support in browsers and consumer
        devices. The allowed audio filetypes for usdz are M4A, MP3, WAV (in
        order of preference).
        
        Usdz Specification
        
        Declaration
        
        ``uniform asset filePath = @@``
        
        C++ Type
        
        SdfAssetPath
        
        Usd Type
        
        SdfValueTypeNames->Asset
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetGainAttr(*args, **kwargs):
        """
        
        GetGainAttr() -> Attribute
        
        
        Multiplier on the incoming audio signal.
        
        
        A value of 0"mutes"the signal. Negative values will be clamped to 0.
        
        Declaration
        
        ``double gain = 1``
        
        C++ Type
        
        double
        
        Usd Type
        
        SdfValueTypeNames->Double
        
        
        
        """
    @staticmethod
    def GetMediaOffsetAttr(*args, **kwargs):
        """
        
        GetMediaOffsetAttr() -> Attribute
        
        
        Expressed in seconds, *mediaOffset* specifies the offset from the
        referenced audio file's beginning at which we should begin playback
        when stage playback reaches the time that prim's audio should start.
        
        
        If the prim's *playbackMode* is a looping mode, *mediaOffset* is
        applied only to the first run-through of the audio clip; the second
        and all other loops begin from the start of the audio clip.
        
        Declaration
        
        ``uniform double mediaOffset = 0``
        
        C++ Type
        
        double
        
        Usd Type
        
        SdfValueTypeNames->Double
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetPlaybackModeAttr(*args, **kwargs):
        """
        
        GetPlaybackModeAttr() -> Attribute
        
        
        Along with *startTime* and *endTime*, determines when the audio
        playback should start and stop during the stage's animation playback
        and whether the audio should loop during its duration.
        
        
        Valid values are:
        
           - onceFromStart: Play the audio once, starting at *startTime*,
             continuing until the audio completes.
        
           - onceFromStartToEnd: Play the audio once beginning at *startTime*,
             continuing until *endTime* or until the audio completes, whichever
             comes first.
        
           - loopFromStart: Start playing the audio at *startTime* and
             continue looping through to the stage's authored *endTimeCode*.
        
           - loopFromStartToEnd: Start playing the audio at *startTime* and
             continue looping through, stopping the audio at *endTime*.
        
           - loopFromStage: Start playing the audio at the stage's authored
             *startTimeCode* and continue looping through to the stage's authored
             *endTimeCode*. This can be useful for ambient sounds that should
             always be active.
        
        Declaration
        
        ``uniform token playbackMode ="onceFromStart"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        onceFromStart, onceFromStartToEnd, loopFromStart, loopFromStartToEnd,
        loopFromStage
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetStartTimeAttr(*args, **kwargs):
        """
        
        GetStartTimeAttr() -> Attribute
        
        
        Expressed in the timeCodesPerSecond of the containing stage,
        *startTime* specifies when the audio stream will start playing during
        animation playback.
        
        
        This value is ignored when *playbackMode* is set to loopFromStage as,
        in this mode, the audio will always start at the stage's authored
        *startTimeCode*. Note that *startTime* is expressed as a timecode so
        that the stage can properly apply layer offsets when resolving its
        value. See Timecode Attributes and Time Scaling for more details and
        caveats.
        
        Declaration
        
        ``uniform timecode startTime = 0``
        
        C++ Type
        
        SdfTimeCode
        
        Usd Type
        
        SdfValueTypeNames->TimeCode
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdMediaSpatialAudio on UsdPrim ``prim`` .
        
        
        Equivalent to UsdMediaSpatialAudio::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdMediaSpatialAudio on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdMediaSpatialAudio (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Tokens(Boost.Python.instance):
    auralMode: typing.ClassVar[str] = 'auralMode'
    endTime: typing.ClassVar[str] = 'endTime'
    filePath: typing.ClassVar[str] = 'filePath'
    gain: typing.ClassVar[str] = 'gain'
    loopFromStage: typing.ClassVar[str] = 'loopFromStage'
    loopFromStart: typing.ClassVar[str] = 'loopFromStart'
    loopFromStartToEnd: typing.ClassVar[str] = 'loopFromStartToEnd'
    mediaOffset: typing.ClassVar[str] = 'mediaOffset'
    nonSpatial: typing.ClassVar[str] = 'nonSpatial'
    onceFromStart: typing.ClassVar[str] = 'onceFromStart'
    onceFromStartToEnd: typing.ClassVar[str] = 'onceFromStartToEnd'
    playbackMode: typing.ClassVar[str] = 'playbackMode'
    spatial: typing.ClassVar[str] = 'spatial'
    startTime: typing.ClassVar[str] = 'startTime'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'usdMedia'
