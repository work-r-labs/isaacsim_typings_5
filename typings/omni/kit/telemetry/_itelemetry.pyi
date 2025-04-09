"""

    Provides a helper interface to abstract and simplify some common telemetry related
    tasks.
"""
from __future__ import annotations
from omni.core._core import IObject
from omni.kit.telemetry._telemetry import ITelemetry
from omni.kit.telemetry._telemetry import ITelemetry2
from omni.kit.telemetry._telemetry import RunEnvironment
__all__ = ['IObject', 'ITelemetry', 'ITelemetry2', 'RunEnvironment']
