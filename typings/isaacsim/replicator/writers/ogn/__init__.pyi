from __future__ import annotations
from . import OgnDopeDatabase
from . import OgnPoseDatabase
from . import tests
__all__: list[str] = ['OgnDopeDatabase', 'OgnPoseDatabase', 'tests']
_NODE_IMPLEMENTATIONS: dict = {'OgnPoseDatabase': python.nodes.OgnPose.OgnPose, 'OgnDopeDatabase': python.nodes.OgnDope.OgnDope}
