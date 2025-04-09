from __future__ import annotations
from collections import namedtuple
from omni.kit.property.physx import database
from omni.physx.bindings import _physx as pxb
from pxr import PhysxSchema
from pxr import UsdPhysics
import typing
__all__ = ['PhysxSchema', 'RefreshCache', 'UsdPhysics', 'database', 'namedtuple', 'patch_refresh_cache_to_prim', 'pxb']
class RefreshCache(tuple):
    """
    RefreshCache(applied_schemas, is_a_base_joint, has_rigidbody_api, has_collision_api, canadd_filteredpairs, canadd_massapi, hasconflictingapis_RigidBodyAPI, hasconflictingapis_CollisionAPI, hasconflictingapis_ArticulationRoot, over_subtree_limit)
    """
    __match_args__: typing.ClassVar[tuple] = ('applied_schemas', 'is_a_base_joint', 'has_rigidbody_api', 'has_collision_api', 'canadd_filteredpairs', 'canadd_massapi', 'hasconflictingapis_RigidBodyAPI', 'hasconflictingapis_CollisionAPI', 'hasconflictingapis_ArticulationRoot', 'over_subtree_limit')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('applied_schemas', 'is_a_base_joint', 'has_rigidbody_api', 'has_collision_api', 'canadd_filteredpairs', 'canadd_massapi', 'hasconflictingapis_RigidBodyAPI', 'hasconflictingapis_CollisionAPI', 'hasconflictingapis_ArticulationRoot', 'over_subtree_limit')
    @staticmethod
    def __new__(_cls, applied_schemas, is_a_base_joint, has_rigidbody_api, has_collision_api, canadd_filteredpairs, canadd_massapi, hasconflictingapis_RigidBodyAPI, hasconflictingapis_CollisionAPI, hasconflictingapis_ArticulationRoot, over_subtree_limit):
        """
        Create new instance of RefreshCache(applied_schemas, is_a_base_joint, has_rigidbody_api, has_collision_api, canadd_filteredpairs, canadd_massapi, hasconflictingapis_RigidBodyAPI, hasconflictingapis_CollisionAPI, hasconflictingapis_ArticulationRoot, over_subtree_limit)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new RefreshCache object from a sequence or iterable
        """
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
    def _asdict(self):
        """
        Return a new dict which maps field names to their values.
        """
    def _replace(self, **kwds):
        """
        Return a new RefreshCache object replacing specified fields with new values
        """
def patch_refresh_cache_to_prim(p, lmt = 100000):
    ...
