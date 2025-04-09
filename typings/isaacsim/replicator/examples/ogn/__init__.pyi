from __future__ import annotations
from . import OgnSampleBetweenSpheresDatabase
from . import OgnSampleInSphereDatabase
from . import OgnSampleOnSphereDatabase
from . import tests
__all__ = ['OgnSampleBetweenSpheresDatabase', 'OgnSampleInSphereDatabase', 'OgnSampleOnSphereDatabase', 'tests']
_NODE_IMPLEMENTATIONS: dict = {'OgnSampleBetweenSpheresDatabase': python.nodes.OgnSampleBetweenSpheres.OgnSampleBetweenSpheres, 'OgnSampleOnSphereDatabase': python.nodes.OgnSampleOnSphere.OgnSampleOnSphere, 'OgnSampleInSphereDatabase': python.nodes.OgnSampleInSphere.OgnSampleInSphere}
