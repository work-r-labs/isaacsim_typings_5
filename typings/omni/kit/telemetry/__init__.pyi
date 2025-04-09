"""

    Provides a helper interface to abstract and simplify some common telemetry related
    tasks.
"""
from __future__ import annotations
from omni.core._core import IObject
from omni.kit.telemetry._telemetry import ITelemetry
from omni.kit.telemetry._telemetry import ITelemetry2
from omni.kit.telemetry._telemetry import RunEnvironment
from omni.kit.telemetry.impl import sentry_extension
from omni.kit.telemetry.impl.sentry_extension import remove_sentry_pii_data
from omni.kit.telemetry.impl.sentry_extension import should_enable_sentry
from omni.kit.telemetry.impl.sentry_extension import start_sentry
from . import _itelemetry
from . import _telemetry
from . import impl
__all__: list = ['ITelemetry', 'ITelemetry2', 'RunEnvironment', 'should_enable_sentry', 'start_sentry', 'remove_sentry_pii_data']
