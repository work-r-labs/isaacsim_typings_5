from __future__ import annotations
import numpy
import typing
import typing_extensions
__all__: list[str] = ['AccessType', 'AuxType', 'CoordsType', 'ElementFlags', 'FrameAtTime', 'FrameOfReference', 'GMOIOConfig', 'GenericModelOutput', 'GenericModelOutputIOFactory', 'IGenericModelOutputIO', 'Modality', 'MotionCompensationState', 'OutputType', 'getMagicNumberGMO', 'getModelOutputFromBuffer']
class AccessType:
    """
    Members:
    
      READ
    
      RECORD_BASIC
    
      RECORD_FULL
    """
    READ: typing.ClassVar[AccessType]  # value = <AccessType.READ: 0>
    RECORD_BASIC: typing.ClassVar[AccessType]  # value = <AccessType.RECORD_BASIC: 1>
    RECORD_FULL: typing.ClassVar[AccessType]  # value = <AccessType.RECORD_FULL: 2>
    __members__: typing.ClassVar[dict[str, AccessType]]  # value = {'READ': <AccessType.READ: 0>, 'RECORD_BASIC': <AccessType.RECORD_BASIC: 1>, 'RECORD_FULL': <AccessType.RECORD_FULL: 2>}
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
class AuxType:
    """
    Members:
    
      NONE
    
      BASIC
    
      EXTRA
    
      FULL
    """
    BASIC: typing.ClassVar[AuxType]  # value = <AuxType.BASIC: 1>
    EXTRA: typing.ClassVar[AuxType]  # value = <AuxType.EXTRA: 2>
    FULL: typing.ClassVar[AuxType]  # value = <AuxType.FULL: 3>
    NONE: typing.ClassVar[AuxType]  # value = <AuxType.NONE: 0>
    __members__: typing.ClassVar[dict[str, AuxType]]  # value = {'NONE': <AuxType.NONE: 0>, 'BASIC': <AuxType.BASIC: 1>, 'EXTRA': <AuxType.EXTRA: 2>, 'FULL': <AuxType.FULL: 3>}
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
class CoordsType:
    """
    Members:
    
      CARTESIAN
    
      SPHERICAL
    
      NOT_APPLICABLE
    """
    CARTESIAN: typing.ClassVar[CoordsType]  # value = <CoordsType.CARTESIAN: 0>
    NOT_APPLICABLE: typing.ClassVar[CoordsType]  # value = <CoordsType.NOT_APPLICABLE: 2>
    SPHERICAL: typing.ClassVar[CoordsType]  # value = <CoordsType.SPHERICAL: 1>
    __members__: typing.ClassVar[dict[str, CoordsType]]  # value = {'CARTESIAN': <CoordsType.CARTESIAN: 0>, 'SPHERICAL': <CoordsType.SPHERICAL: 1>, 'NOT_APPLICABLE': <CoordsType.NOT_APPLICABLE: 2>}
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
class ElementFlags:
    """
    Members:
    
      FLAG_1
    
      FLAG_2
    
      FLAG_3
    
      FLAG_4
    
      FLAG_5
    
      FLAG_6
    
      FLAG_7
    
      VALID
    """
    FLAG_1: typing.ClassVar[ElementFlags]  # value = <ElementFlags.FLAG_1: 0>
    FLAG_2: typing.ClassVar[ElementFlags]  # value = <ElementFlags.FLAG_2: 1>
    FLAG_3: typing.ClassVar[ElementFlags]  # value = <ElementFlags.FLAG_3: 2>
    FLAG_4: typing.ClassVar[ElementFlags]  # value = <ElementFlags.FLAG_4: 4>
    FLAG_5: typing.ClassVar[ElementFlags]  # value = <ElementFlags.FLAG_5: 8>
    FLAG_6: typing.ClassVar[ElementFlags]  # value = <ElementFlags.FLAG_6: 16>
    FLAG_7: typing.ClassVar[ElementFlags]  # value = <ElementFlags.FLAG_7: 32>
    VALID: typing.ClassVar[ElementFlags]  # value = <ElementFlags.VALID: 64>
    __members__: typing.ClassVar[dict[str, ElementFlags]]  # value = {'FLAG_1': <ElementFlags.FLAG_1: 0>, 'FLAG_2': <ElementFlags.FLAG_2: 1>, 'FLAG_3': <ElementFlags.FLAG_3: 2>, 'FLAG_4': <ElementFlags.FLAG_4: 4>, 'FLAG_5': <ElementFlags.FLAG_5: 8>, 'FLAG_6': <ElementFlags.FLAG_6: 16>, 'FLAG_7': <ElementFlags.FLAG_7: 32>, 'VALID': <ElementFlags.VALID: 64>}
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
class FrameAtTime:
    orientation: list[float]
    posM: list[float]
    timestampNs: int
    def __init__(self) -> None:
        ...
class FrameOfReference:
    """
    Members:
    
      SENSOR
    
      WORLD
    
      CUSTOM
    
      PARENT
    """
    CUSTOM: typing.ClassVar[FrameOfReference]  # value = <FrameOfReference.CUSTOM: 2>
    PARENT: typing.ClassVar[FrameOfReference]  # value = <FrameOfReference.PARENT: 3>
    SENSOR: typing.ClassVar[FrameOfReference]  # value = <FrameOfReference.SENSOR: 0>
    WORLD: typing.ClassVar[FrameOfReference]  # value = <FrameOfReference.WORLD: 1>
    __members__: typing.ClassVar[dict[str, FrameOfReference]]  # value = {'SENSOR': <FrameOfReference.SENSOR: 0>, 'WORLD': <FrameOfReference.WORLD: 1>, 'CUSTOM': <FrameOfReference.CUSTOM: 2>, 'PARENT': <FrameOfReference.PARENT: 3>}
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
class GMOIOConfig:
    accessType: AccessType
    clientName: str
    fileName: str
    groupName: str
    loop: bool
    maxPoints: int
    onlyValid: bool
    def __del__(self) -> None:
        ...
    def __init__(self) -> None:
        ...
class GenericModelOutput:
    auxType: AuxType
    elementsCoordsType: CoordsType
    frameEnd: FrameAtTime
    frameId: int
    frameOfReference: FrameOfReference
    frameStart: FrameAtTime
    magicNumber: int
    majorVersion: int
    minorVersion: int
    motionCompensationState: MotionCompensationState
    numElements: int
    outputType: OutputType
    patchVersion: int
    sizeInBytes: int
    timestampNs: int
    def __init__(self) -> None:
        ...
    @property
    def azimuthOffset(self) -> float:
        ...
    @property
    def channelId(self) -> numpy.ndarray:
        ...
    @property
    def cycleCnt(self) -> int:
        ...
    @property
    def echoId(self) -> numpy.ndarray:
        ...
    @property
    def emitterId(self) -> numpy.ndarray:
        ...
    @property
    def filledAuxMembers(self) -> ...:
        ...
    @property
    def flags(self) -> numpy.ndarray:
        ...
    @property
    def hitNormals(self) -> numpy.ndarray:
        ...
    @property
    def matId(self) -> numpy.ndarray:
        ...
    @property
    def maxAzRad(self) -> float:
        ...
    @property
    def maxElRad(self) -> float:
        ...
    @property
    def maxRangeM(self) -> float:
        ...
    @property
    def maxVelMps(self) -> float:
        ...
    @property
    def minAzRad(self) -> float:
        ...
    @property
    def minElRad(self) -> float:
        ...
    @property
    def minVelMps(self) -> float:
        ...
    @property
    def numSamplesPerSgw(self) -> int:
        ...
    @property
    def numSgws(self) -> int:
        ...
    @property
    def objId(self) -> numpy.ndarray:
        ...
    @property
    def rv_ms(self) -> numpy.ndarray:
        ...
    @property
    def scalar(self) -> numpy.ndarray:
        ...
    @property
    def scanComplete(self) -> bool:
        ...
    @property
    def scanIdx(self) -> int:
        ...
    @property
    def sensorID(self) -> int:
        ...
    @property
    def tickId(self) -> numpy.ndarray:
        ...
    @property
    def tickStates(self) -> numpy.ndarray:
        ...
    @property
    def timeOffSetNs(self) -> numpy.ndarray:
        ...
    @property
    def velocities(self) -> numpy.ndarray:
        ...
    @property
    def x(self) -> numpy.ndarray:
        ...
    @property
    def y(self) -> numpy.ndarray:
        ...
    @property
    def z(self) -> numpy.ndarray:
        ...
class GenericModelOutputIOFactory:
    @staticmethod
    def createInstance() -> IGenericModelOutputIO:
        ...
    def __init__(self) -> None:
        ...
class IGenericModelOutputIO:
    def __init__(self) -> None:
        ...
    def addPacket(self, arg0: capsule, arg1: int) -> None:
        ...
    def init(self, arg0: GMOIOConfig) -> None:
        ...
    def readModelOutput(self, groupName: str = '', frameId: int = -1) -> GenericModelOutput:
        ...
    def writeModelOutput(self, arg0: GenericModelOutput) -> None:
        ...
class Modality:
    """
    Members:
    
      NONE
    
      LIDAR
    
      RADAR
    
      USS
    
      IDS
    """
    IDS: typing.ClassVar[Modality]  # value = <Modality.IDS: 4>
    LIDAR: typing.ClassVar[Modality]  # value = <Modality.LIDAR: 1>
    NONE: typing.ClassVar[Modality]  # value = <Modality.NONE: 0>
    RADAR: typing.ClassVar[Modality]  # value = <Modality.RADAR: 2>
    USS: typing.ClassVar[Modality]  # value = <Modality.USS: 3>
    __members__: typing.ClassVar[dict[str, Modality]]  # value = {'NONE': <Modality.NONE: 0>, 'LIDAR': <Modality.LIDAR: 1>, 'RADAR': <Modality.RADAR: 2>, 'USS': <Modality.USS: 3>, 'IDS': <Modality.IDS: 4>}
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
class MotionCompensationState:
    """
    Members:
    
      NONCOMPENSATED
    
      COMPENSATED
    
      NOT_APPLICABLE
    """
    COMPENSATED: typing.ClassVar[MotionCompensationState]  # value = <MotionCompensationState.COMPENSATED: 1>
    NONCOMPENSATED: typing.ClassVar[MotionCompensationState]  # value = <MotionCompensationState.NONCOMPENSATED: 0>
    NOT_APPLICABLE: typing.ClassVar[MotionCompensationState]  # value = <MotionCompensationState.NOT_APPLICABLE: 2>
    __members__: typing.ClassVar[dict[str, MotionCompensationState]]  # value = {'NONCOMPENSATED': <MotionCompensationState.NONCOMPENSATED: 0>, 'COMPENSATED': <MotionCompensationState.COMPENSATED: 1>, 'NOT_APPLICABLE': <MotionCompensationState.NOT_APPLICABLE: 2>}
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
class OutputType:
    """
    Members:
    
      POINTCLOUD
    """
    POINTCLOUD: typing.ClassVar[OutputType]  # value = <OutputType.POINTCLOUD: 0>
    __members__: typing.ClassVar[dict[str, OutputType]]  # value = {'POINTCLOUD': <OutputType.POINTCLOUD: 0>}
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
def getMagicNumberGMO() -> int:
    """
    Get magic number for GenericModelOutput.
    """
def getModelOutputFromBuffer(arg0: typing_extensions.Buffer) -> ...:
    """
    Get model output from binary buffer.
    """
