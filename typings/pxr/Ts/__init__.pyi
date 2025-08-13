from __future__ import annotations
import pxr.Tf
from pxr.Ts.TsTest_Comparator import TsTest_Comparator
from pxr.Ts.TsTest_CompareBaseline import TsTest_CompareBaseline
from pxr.Ts.TsTest_Grapher import TsTest_Grapher
import typing
__all__: list[str] = ['ExtrapolationHeld', 'ExtrapolationLinear', 'ExtrapolationType', 'KeyFrame', 'KnotBezier', 'KnotHeld', 'KnotLinear', 'KnotType', 'Left', 'LoopParams', 'Right', 'Side', 'Spline', 'TsTest_Comparator', 'TsTest_CompareBaseline', 'TsTest_Evaluator', 'TsTest_Grapher', 'TsTest_Museum', 'TsTest_Sample', 'TsTest_SampleTimes', 'TsTest_SplineData', 'TsTest_TsEvaluator', 'ValueSample']
class ExtrapolationType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Ts.ExtrapolationHeld, Ts.ExtrapolationLinear)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class KeyFrame(Boost.Python.instance):
    @staticmethod
    def CanSetKnotType(*args, **kwargs):
        """
        
        
        Returns true if the given knot type can be set on this key frame. If it returns false, it also returns the reason why not. The reason can be accessed like this: anim.CanSetKnotType(kf).reasonWhyNot.
        """
    @staticmethod
    def GetValue(*args, **kwargs):
        """
        
        
        Gets the value at this keyframe on the given side.
        """
    @staticmethod
    def IsEquivalentAtSide(*args, **kwargs):
        ...
    @staticmethod
    def SetValue(*args, **kwargs):
        """
        
        
        Sets the value at this keyframe on the given side.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def hasTangents(*args, **kwargs):
        ...
    @property
    def isDualValued(*args, **kwargs):
        """
        True if this Keyframe is dual-valued.
        """
    @isDualValued.setter
    def isDualValued(*args, **kwargs):
        ...
    @property
    def isInterpolatable(*args, **kwargs):
        ...
    @property
    def knotType(*args, **kwargs):
        """
        The knot type of this Keyframe.  It controls how the spline is interpolated around this keyframe.
        """
    @knotType.setter
    def knotType(*args, **kwargs):
        ...
    @property
    def leftLen(*args, **kwargs):
        """
        The left tangent's length.
        """
    @leftLen.setter
    def leftLen(*args, **kwargs):
        ...
    @property
    def leftSlope(*args, **kwargs):
        """
        The left tangent's slope.
        """
    @leftSlope.setter
    def leftSlope(*args, **kwargs):
        ...
    @property
    def rightLen(*args, **kwargs):
        """
        The right tangent's length.
        """
    @rightLen.setter
    def rightLen(*args, **kwargs):
        ...
    @property
    def rightSlope(*args, **kwargs):
        """
        The right tangent's slope.
        """
    @rightSlope.setter
    def rightSlope(*args, **kwargs):
        ...
    @property
    def supportsTangents(*args, **kwargs):
        ...
    @property
    def tangentSymmetryBroken(*args, **kwargs):
        """
        Gets and sets whether symmetry between the left/right tangents is broken. If true, tangent handles will not automatically stay symmetric as they are changed.
        """
    @tangentSymmetryBroken.setter
    def tangentSymmetryBroken(*args, **kwargs):
        ...
    @property
    def time(*args, **kwargs):
        """
        The time of this Keyframe.
        """
    @time.setter
    def time(*args, **kwargs):
        ...
    @property
    def value(*args, **kwargs):
        """
        The value at this Keyframe.  If the keyframe is dual-valued, this will be a tuple of the (left, right) side values; otherwise, it will be the single value.  If you assign a single value to a dual-valued knot, only the right side will be set, and the left side will remain unchanged.  If you assign a dual-value (tuple) to a single-valued keyframe you'll get an exception and the keyframe won't have changed.
        """
    @value.setter
    def value(*args, **kwargs):
        ...
class KnotType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Ts.KnotHeld, Ts.KnotLinear, Ts.KnotBezier)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class LoopParams(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 104
    @staticmethod
    def GetLoopedInterval(*args, **kwargs):
        ...
    @staticmethod
    def GetMasterInterval(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def looping(*args, **kwargs):
        ...
    @looping.setter
    def looping(*args, **kwargs):
        ...
    @property
    def period(*args, **kwargs):
        ...
    @property
    def preRepeatFrames(*args, **kwargs):
        ...
    @property
    def repeatFrames(*args, **kwargs):
        ...
    @property
    def start(*args, **kwargs):
        ...
    @property
    def valueOffset(*args, **kwargs):
        ...
    @valueOffset.setter
    def valueOffset(*args, **kwargs):
        ...
class Side(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Ts.Left, Ts.Right)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Spline(Boost.Python.instance):
    @staticmethod
    def BakeSplineLoops(*args, **kwargs):
        ...
    @staticmethod
    def Breakdown(*args, **kwargs):
        ...
    @staticmethod
    def CanSetKeyFrame(*args, **kwargs):
        """
        
        
        CanSetKeyFrame(kf) -> bool
        
        kf : TsKeyFrame
        
        Returns true if the given keyframe can be set on this spline. If it returns false, it also returns the reason why not. The reason can be accessed like this: anim.CanSetKeyFrame(kf).reasonWhyNot.
        """
    @staticmethod
    def ClearRedundantKeyFrames(*args, **kwargs):
        """
        
        
        Clears all redundant key frames from the spline
        
        """
    @staticmethod
    def ClosestKeyFrame(*args, **kwargs):
        """
        
        
        ClosestKeyFrame(time) -> TsKeyFrame
        
        time : Time
        
        Finds the keyframe closest to the given time. Returns None if there are no keyframes.
        """
    @staticmethod
    def ClosestKeyFrameAfter(*args, **kwargs):
        """
        
        
        ClosestKeyFrameAfter(time) -> TsKeyFrame
        
        time : Time
        
        Finds the closest keyframe after the given time. Returns None if no such keyframe exists.
        """
    @staticmethod
    def ClosestKeyFrameBefore(*args, **kwargs):
        """
        
        
        ClosestKeyFrameBefore(time) -> TsKeyFrame
        
        time : Time
        
        Finds the closest keyframe before the given time. Returns None if no such keyframe exists.
        """
    @staticmethod
    def DoSidesDiffer(*args, **kwargs):
        ...
    @staticmethod
    def Eval(*args, **kwargs):
        """
        
        
        Eval(times) -> sequence<VtValue>
        
        times : tuple<Time>
        
        Evaluates this spline at a tuple or list of times, returning a tuple of results.
        """
    @staticmethod
    def EvalDerivative(*args, **kwargs):
        ...
    @staticmethod
    def EvalHeld(*args, **kwargs):
        ...
    @staticmethod
    def GetKeyFramesInMultiInterval(*args, **kwargs):
        ...
    @staticmethod
    def HasRedundantKeyFrames(*args, **kwargs):
        """
        
        
        True if any key frames are redundant.
        
        """
    @staticmethod
    def IsKeyFrameRedundant(*args, **kwargs):
        """
        
        
        True if the key frame at the provided time is redundant.
        
        If a second parameter is provided it is used as a default valuefor the spline, so that the last knot on a spline can be markedredundant if it is equal to the default value.
        If the TsTime provided does not refer to a frame that has aknot, an exception will be thrown.
        
        True if the key frame is redundant.
        
        If a second parameter is provided it is used as a default valuefor the spline, so that the last knot on a spline can be markedredundant if it is equal to the default value.
        """
    @staticmethod
    def IsLinear(*args, **kwargs):
        ...
    @staticmethod
    def IsSegmentFlat(*args, **kwargs):
        """
        
        
        True if the segment between the two provided TsTimes is flat.
        
        If either TsTime does not refer to a knot then an exception is thrown.
        
        True if the segment between the two provided TsKeyFrames isflat.
        """
    @staticmethod
    def IsSegmentValueMonotonic(*args, **kwargs):
        """
        
        
        True if the segment between the two provided TsTimes is monotonically increasing or monotonically decreasing, i.e. no extremes are present
        
        If either TsTime does not refer to a knot then an exception is thrown.
        
        True if the segment between the two provided TsKeyFrames is monotonically increasing or monotonically decreasing, i.e. no extremes are present
        """
    @staticmethod
    def IsTimeLooped(*args, **kwargs):
        """
        
        
        True if the given time is in the unrolled region of a spline that is looping; i.e. not in the master region
        """
    @staticmethod
    def IsVarying(*args, **kwargs):
        """
        
        
        True if the value of the spline changes over time, whether due to differing values among keyframes, knot sides, or non-flat tangents
        """
    @staticmethod
    def IsVaryingSignificantly(*args, **kwargs):
        """
        
        
        True if the value of the spline changes over time, more than a tiny amount, whether due to differing values among keyframes, knot sides, or non-flat tangents
        """
    @staticmethod
    def Range(*args, **kwargs):
        """
        
        
        Range(startTime, endTime) -> tuple<VtValue>
        
        startTime : Time
        endTime : Time
        
        The minimum and maximum of this spline returned as a tuple pair over the given time domain.
        """
    @staticmethod
    def Sample(*args, **kwargs):
        ...
    @staticmethod
    def SetKeyFrame(*args, **kwargs):
        ...
    @staticmethod
    def SetKeyFrames(*args, **kwargs):
        """
        
        
        SetKeyFrames(keyFrames)
        
        keyFrames : sequence<TsKeyFrame>
        
        Replaces all of the specified keyframes. Keyframes may be specified using any type of Python sequence, such as a list or tuple.
        """
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def has_key(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
    @property
    def empty(*args, **kwargs):
        ...
    @property
    def extrapolation(*args, **kwargs):
        ...
    @extrapolation.setter
    def extrapolation(*args, **kwargs):
        ...
    @property
    def frameRange(*args, **kwargs):
        """
        A list with the first and last frames as elements.
        """
    @property
    def frames(*args, **kwargs):
        """
        A list of the frames for which keyframes exist.
        """
    @property
    def loopParams(*args, **kwargs):
        ...
    @loopParams.setter
    def loopParams(*args, **kwargs):
        ...
    @property
    def typeName(*args, **kwargs):
        """
        Returns the typename of the value type for keyframes in this TsSpline. If no keyframes have been set, returns None.
        """
class TsTest_Evaluator(Boost.Python.instance):
    @staticmethod
    def BakeInnerLoops(*args, **kwargs):
        ...
    @staticmethod
    def Eval(*args, **kwargs):
        ...
    @staticmethod
    def Sample(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class TsTest_Museum(Boost.Python.instance):
    class DataId(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'Test_Museum'
        allValues: typing.ClassVar[tuple]  # value = (Ts.Test_Museum.TwoKnotBezier, Ts.Test_Museum.TwoKnotLinear, Ts.Test_Museum.SimpleInnerLoop, Ts.Test_Museum.Recurve, Ts.Test_Museum.Crossover)
        @staticmethod
        def GetValueFromName(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    Crossover: typing.ClassVar[DataId]  # value = Ts.Test_Museum.Crossover
    Recurve: typing.ClassVar[DataId]  # value = Ts.Test_Museum.Recurve
    SimpleInnerLoop: typing.ClassVar[DataId]  # value = Ts.Test_Museum.SimpleInnerLoop
    TwoKnotBezier: typing.ClassVar[DataId]  # value = Ts.Test_Museum.TwoKnotBezier
    TwoKnotLinear: typing.ClassVar[DataId]  # value = Ts.Test_Museum.TwoKnotLinear
    @staticmethod
    def GetData(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class TsTest_Sample(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def time(*args, **kwargs):
        ...
    @time.setter
    def time(*args, **kwargs):
        ...
    @property
    def value(*args, **kwargs):
        ...
    @value.setter
    def value(*args, **kwargs):
        ...
class TsTest_SampleTimes(Boost.Python.instance):
    class SampleTime(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 40
        @staticmethod
        def __eq__(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __lt__(*args, **kwargs):
            ...
        @staticmethod
        def __ne__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @property
        def pre(*args, **kwargs):
            ...
        @pre.setter
        def pre(*args, **kwargs):
            ...
        @property
        def time(*args, **kwargs):
            ...
        @time.setter
        def time(*args, **kwargs):
            ...
    @staticmethod
    def AddExtrapolationTimes(*args, **kwargs):
        ...
    @staticmethod
    def AddKnotTimes(*args, **kwargs):
        ...
    @staticmethod
    def AddStandardTimes(*args, **kwargs):
        ...
    @staticmethod
    def AddTimes(*args, **kwargs):
        ...
    @staticmethod
    def AddUniformInterpolationTimes(*args, **kwargs):
        ...
    @staticmethod
    def GetTimes(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class TsTest_SplineData(Boost.Python.instance):
    class ExtrapMethod(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'Test_SplineData'
        allValues: typing.ClassVar[tuple]  # value = (Ts.Test_SplineData.ExtrapHeld, Ts.Test_SplineData.ExtrapLinear, Ts.Test_SplineData.ExtrapSloped, Ts.Test_SplineData.ExtrapLoop)
        @staticmethod
        def GetValueFromName(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class Extrapolation(Boost.Python.instance):
        @staticmethod
        def __eq__(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __ne__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @property
        def loopMode(*args, **kwargs):
            ...
        @loopMode.setter
        def loopMode(*args, **kwargs):
            ...
        @property
        def method(*args, **kwargs):
            ...
        @method.setter
        def method(*args, **kwargs):
            ...
        @property
        def slope(*args, **kwargs):
            ...
        @slope.setter
        def slope(*args, **kwargs):
            ...
    class Feature(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'Test_SplineData'
        allValues: typing.ClassVar[tuple]  # value = (Ts.Test_SplineData.FeatureHeldSegments, Ts.Test_SplineData.FeatureLinearSegments, Ts.Test_SplineData.FeatureBezierSegments, Ts.Test_SplineData.FeatureHermiteSegments, Ts.Test_SplineData.FeatureDualValuedKnots, Ts.Test_SplineData.FeatureInnerLoops, Ts.Test_SplineData.FeatureExtrapolatingLoops)
        @staticmethod
        def GetValueFromName(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class InnerLoopParams(Boost.Python.instance):
        @staticmethod
        def IsValid(*args, **kwargs):
            ...
        @staticmethod
        def __eq__(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __ne__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @property
        def closedEnd(*args, **kwargs):
            ...
        @closedEnd.setter
        def closedEnd(*args, **kwargs):
            ...
        @property
        def enabled(*args, **kwargs):
            ...
        @enabled.setter
        def enabled(*args, **kwargs):
            ...
        @property
        def postLoopEnd(*args, **kwargs):
            ...
        @postLoopEnd.setter
        def postLoopEnd(*args, **kwargs):
            ...
        @property
        def preLoopStart(*args, **kwargs):
            ...
        @preLoopStart.setter
        def preLoopStart(*args, **kwargs):
            ...
        @property
        def protoEnd(*args, **kwargs):
            ...
        @protoEnd.setter
        def protoEnd(*args, **kwargs):
            ...
        @property
        def protoStart(*args, **kwargs):
            ...
        @protoStart.setter
        def protoStart(*args, **kwargs):
            ...
        @property
        def valueOffset(*args, **kwargs):
            ...
        @valueOffset.setter
        def valueOffset(*args, **kwargs):
            ...
    class InterpMethod(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'Test_SplineData'
        allValues: typing.ClassVar[tuple]  # value = (Ts.Test_SplineData.InterpHeld, Ts.Test_SplineData.InterpLinear, Ts.Test_SplineData.InterpCurve)
        @staticmethod
        def GetValueFromName(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class Knot(Boost.Python.instance):
        @staticmethod
        def __eq__(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __lt__(*args, **kwargs):
            ...
        @staticmethod
        def __ne__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @property
        def isDualValued(*args, **kwargs):
            ...
        @isDualValued.setter
        def isDualValued(*args, **kwargs):
            ...
        @property
        def nextSegInterpMethod(*args, **kwargs):
            ...
        @nextSegInterpMethod.setter
        def nextSegInterpMethod(*args, **kwargs):
            ...
        @property
        def postAuto(*args, **kwargs):
            ...
        @postAuto.setter
        def postAuto(*args, **kwargs):
            ...
        @property
        def postLen(*args, **kwargs):
            ...
        @postLen.setter
        def postLen(*args, **kwargs):
            ...
        @property
        def postSlope(*args, **kwargs):
            ...
        @postSlope.setter
        def postSlope(*args, **kwargs):
            ...
        @property
        def preAuto(*args, **kwargs):
            ...
        @preAuto.setter
        def preAuto(*args, **kwargs):
            ...
        @property
        def preLen(*args, **kwargs):
            ...
        @preLen.setter
        def preLen(*args, **kwargs):
            ...
        @property
        def preSlope(*args, **kwargs):
            ...
        @preSlope.setter
        def preSlope(*args, **kwargs):
            ...
        @property
        def preValue(*args, **kwargs):
            ...
        @preValue.setter
        def preValue(*args, **kwargs):
            ...
        @property
        def time(*args, **kwargs):
            ...
        @time.setter
        def time(*args, **kwargs):
            ...
        @property
        def value(*args, **kwargs):
            ...
        @value.setter
        def value(*args, **kwargs):
            ...
    class LoopMode(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'Test_SplineData'
        allValues: typing.ClassVar[tuple]  # value = (Ts.Test_SplineData.LoopNone, Ts.Test_SplineData.LoopContinue, Ts.Test_SplineData.LoopRepeat, Ts.Test_SplineData.LoopReset, Ts.Test_SplineData.LoopOscillate)
        @staticmethod
        def GetValueFromName(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    ExtrapHeld: typing.ClassVar[ExtrapMethod]  # value = Ts.Test_SplineData.ExtrapHeld
    ExtrapLinear: typing.ClassVar[ExtrapMethod]  # value = Ts.Test_SplineData.ExtrapLinear
    ExtrapLoop: typing.ClassVar[ExtrapMethod]  # value = Ts.Test_SplineData.ExtrapLoop
    ExtrapSloped: typing.ClassVar[ExtrapMethod]  # value = Ts.Test_SplineData.ExtrapSloped
    FeatureBezierSegments: typing.ClassVar[Feature]  # value = Ts.Test_SplineData.FeatureBezierSegments
    FeatureDualValuedKnots: typing.ClassVar[Feature]  # value = Ts.Test_SplineData.FeatureDualValuedKnots
    FeatureExtrapolatingLoops: typing.ClassVar[Feature]  # value = Ts.Test_SplineData.FeatureExtrapolatingLoops
    FeatureHeldSegments: typing.ClassVar[Feature]  # value = Ts.Test_SplineData.FeatureHeldSegments
    FeatureHermiteSegments: typing.ClassVar[Feature]  # value = Ts.Test_SplineData.FeatureHermiteSegments
    FeatureInnerLoops: typing.ClassVar[Feature]  # value = Ts.Test_SplineData.FeatureInnerLoops
    FeatureLinearSegments: typing.ClassVar[Feature]  # value = Ts.Test_SplineData.FeatureLinearSegments
    InterpCurve: typing.ClassVar[InterpMethod]  # value = Ts.Test_SplineData.InterpCurve
    InterpHeld: typing.ClassVar[InterpMethod]  # value = Ts.Test_SplineData.InterpHeld
    InterpLinear: typing.ClassVar[InterpMethod]  # value = Ts.Test_SplineData.InterpLinear
    LoopContinue: typing.ClassVar[LoopMode]  # value = Ts.Test_SplineData.LoopContinue
    LoopNone: typing.ClassVar[LoopMode]  # value = Ts.Test_SplineData.LoopNone
    LoopOscillate: typing.ClassVar[LoopMode]  # value = Ts.Test_SplineData.LoopOscillate
    LoopRepeat: typing.ClassVar[LoopMode]  # value = Ts.Test_SplineData.LoopRepeat
    LoopReset: typing.ClassVar[LoopMode]  # value = Ts.Test_SplineData.LoopReset
    @staticmethod
    def AddKnot(*args, **kwargs):
        ...
    @staticmethod
    def GetDebugDescription(*args, **kwargs):
        ...
    @staticmethod
    def GetInnerLoopParams(*args, **kwargs):
        ...
    @staticmethod
    def GetIsHermite(*args, **kwargs):
        ...
    @staticmethod
    def GetKnots(*args, **kwargs):
        ...
    @staticmethod
    def GetPostExtrapolation(*args, **kwargs):
        ...
    @staticmethod
    def GetPreExtrapolation(*args, **kwargs):
        ...
    @staticmethod
    def GetRequiredFeatures(*args, **kwargs):
        ...
    @staticmethod
    def SetInnerLoopParams(*args, **kwargs):
        ...
    @staticmethod
    def SetIsHermite(*args, **kwargs):
        ...
    @staticmethod
    def SetKnots(*args, **kwargs):
        ...
    @staticmethod
    def SetPostExtrapolation(*args, **kwargs):
        ...
    @staticmethod
    def SetPreExtrapolation(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class TsTest_TsEvaluator(TsTest_Evaluator):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ValueSample(Boost.Python.instance):
    """
    An individual sample.  A sample is either a blur, defining a rectangle, or linear, defining a line for linear interpolation. In both cases the sample is half-open on the right.
    """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def isBlur(*args, **kwargs):
        """
        True if a blur sample
        """
    @property
    def leftTime(*args, **kwargs):
        """
        Left side time (inclusive)
        """
    @property
    def leftValue(*args, **kwargs):
        """
        Value at left or, for blur, min value
        """
    @property
    def rightTime(*args, **kwargs):
        """
        Right side time (exclusive)
        """
    @property
    def rightValue(*args, **kwargs):
        """
        Value at right or, for blur, max value
        """
class _AnnotatedBoolResult(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def reasonWhyNot(*args, **kwargs):
        ...
ExtrapolationHeld: ExtrapolationType  # value = Ts.ExtrapolationHeld
ExtrapolationLinear: ExtrapolationType  # value = Ts.ExtrapolationLinear
KnotBezier: KnotType  # value = Ts.KnotBezier
KnotHeld: KnotType  # value = Ts.KnotHeld
KnotLinear: KnotType  # value = Ts.KnotLinear
Left: Side  # value = Ts.Left
Right: Side  # value = Ts.Right
__MFB_FULL_PACKAGE_NAME: str = 'ts'
