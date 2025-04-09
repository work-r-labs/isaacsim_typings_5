"""
pybind11 omni.kit.raycast.query.IRaycastQuery bindings
"""
from __future__ import annotations
import typing
__all__ = ['IRaycastQuery', 'Ray', 'RayQueryResult', 'Result', 'acquire_raycast_query_interface']
class IRaycastQuery:
    def add_raycast_sequence(self) -> int:
        """
                        Add a sequence of raycast queries that maintains last valid value
                          and will execute raycast on current scene.
        
                        Returns:
                            int: Sequence id in raycast sequence for added.
        """
    def get_latest_result_from_raycast_sequence(self, arg0: int) -> tuple[Ray, RayQueryResult]:
        """
                        Get latest result from a sequence of raycasts.
        
                        Args:
                            sequenceId (int): Sequence id returned by addRaycastSequence.
        
                        Returns:
                            Tuple(:obj:'Ray', :obj:'Result'): Latest ray that was resolved and result of the ray request.
        """
    def remove_raycast_sequence(self, arg0: int) -> Result:
        """
                        Remove a sequence of raycasts.
        
                        Args:
                            sequenceId (int): Sequence id to removed from RaycastSequence.
        
                        Returns:
                            :obj:'Result': Error code if function failed.
        """
    def set_raycast_sequence_array_size(self, arg0: int, arg1: int) -> Result:
        """
                        Set the size of the raycast sequence.
        
                        Args:
                            sequenceId (int): Sequence id returned by addRaycastSequence.
                            size (int): Number of ray casts in sequence.
        
                        Returns:
                            :obj:'Result': Error code if function failed.
        """
    def submit_ray_to_raycast_sequence(self, arg0: int, arg1: Ray) -> Result:
        """
                        Submit a new ray request to a sequence of raycasts.
        
                        Args:
                            sequenceId (int): Sequence id returned by addRaycastSequence.
                            ray (:obj:'Ray'): The ray to submit.
        
                        Returns:
                            :obj:'Result': Error code if function failed.
        """
    def submit_raycast_query(self, ray: Ray, callback: typing.Callable[[Ray, RayQueryResult], None]) -> None:
        """
                        This function adds a raycast query operation in the current scene.
        
                        Args:
                            ray (:obj:'Ray'): The ray to submit.
                            callback (Callable): The callback lambda function to execute when resolved.
                                function signature: void(Ray, RayQueryResult)
        """
class Ray:
    """
    
                Ray represents a ray in 3D space.
            
    """
    def __init__(self, origin: typing.Any, direction: typing.Any, min_t: float = 0.0, max_t: float = ..., adjust_for_section: bool = True) -> None:
        """
                        A ray is defined by an origin point, a direction vector, and minimum and maximum distances along the ray.
                        The ray can optionally be adjusted to fit within a specific section of space.
        
                        Args:
                            origin (Vec3): The origin point of the ray.
                            direction (Vec3): The direction vector of the ray.
                            min_t (float, optional): The minimum distance along the ray. Defaults to 0.0.
                            max_t (float, optional): The maximum distance along the ray. Defaults to positive infinity.
                            adjust_for_section (bool, optional): Whether to adjust the ray to fit within a specific section of space.
                                Defaults to True.
        """
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @property
    def forward(self) -> typing.Any:
        """
        direction of the ray
        """
    @forward.setter
    def forward(self, arg1: typing.Any) -> None:
        ...
    @property
    def max_t(self) -> float:
        """
        t value at end of ray
        """
    @max_t.setter
    def max_t(self, arg1: float) -> None:
        ...
    @property
    def min_t(self) -> float:
        """
        t value of start of ray
        """
    @min_t.setter
    def min_t(self, arg1: float) -> None:
        ...
    @property
    def origin(self) -> typing.Any:
        """
        origin of the ray
        """
    @origin.setter
    def origin(self, arg1: typing.Any) -> None:
        ...
class RayQueryResult:
    def __init__(self) -> None:
        """
        Create a new RayQueryResult
        """
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def get_target_usd_path(self) -> str:
        """
                        This function returns the usd path of geometry that was hit.
        
                        Return:
                            str: Usd path of object that is the target, or an empty string if nothing was hit
        """
    @property
    def hit_position(self) -> typing.Any:
        """
        position of hit
        """
    @property
    def hit_t(self) -> float:
        """
        t value of hit position
        """
    @property
    def instance_id(self) -> int:
        """
        instance id
        """
    @property
    def normal(self) -> typing.Any:
        """
        normal of geometry at hit point
        """
    @property
    def primitive_id(self) -> int:
        """
        primitive id
        """
    @property
    def valid(self) -> bool:
        """
        indicates whether result is valid
        """
class Result:
    """
    
                Result stat code for raycast query.
            
    
    Members:
    
      SUCCESS : The operation was successful
    
      INVALID_PARAMETER : The parameter provided is invalid
    
      PARAMETER_IS_NULL : The parameter is a null value
    
      RAYCAST_SEQUENCE_DOES_NOT_EXIST : The raycast sequence does not exist
    
      RAYCAST_QUERY_MANAGER_DOES_NOT_EXIT : The raycast query manager does not exist
    
      RAYCAST_SEQUENCE_ADDITION_FAILED : The addition of the raycast sequence failed
    """
    INVALID_PARAMETER: typing.ClassVar[Result]  # value = <Result.INVALID_PARAMETER: 1>
    PARAMETER_IS_NULL: typing.ClassVar[Result]  # value = <Result.PARAMETER_IS_NULL: 2>
    RAYCAST_QUERY_MANAGER_DOES_NOT_EXIT: typing.ClassVar[Result]  # value = <Result.RAYCAST_QUERY_MANAGER_DOES_NOT_EXIT: 4>
    RAYCAST_SEQUENCE_ADDITION_FAILED: typing.ClassVar[Result]  # value = <Result.RAYCAST_SEQUENCE_ADDITION_FAILED: 5>
    RAYCAST_SEQUENCE_DOES_NOT_EXIST: typing.ClassVar[Result]  # value = <Result.RAYCAST_SEQUENCE_DOES_NOT_EXIST: 3>
    SUCCESS: typing.ClassVar[Result]  # value = <Result.SUCCESS: 0>
    __members__: typing.ClassVar[dict[str, Result]]  # value = {'SUCCESS': <Result.SUCCESS: 0>, 'INVALID_PARAMETER': <Result.INVALID_PARAMETER: 1>, 'PARAMETER_IS_NULL': <Result.PARAMETER_IS_NULL: 2>, 'RAYCAST_SEQUENCE_DOES_NOT_EXIST': <Result.RAYCAST_SEQUENCE_DOES_NOT_EXIST: 3>, 'RAYCAST_QUERY_MANAGER_DOES_NOT_EXIT': <Result.RAYCAST_QUERY_MANAGER_DOES_NOT_EXIT: 4>, 'RAYCAST_SEQUENCE_ADDITION_FAILED': <Result.RAYCAST_SEQUENCE_ADDITION_FAILED: 5>}
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
def acquire_raycast_query_interface(plugin_name: str = None, library_path: str = None) -> ...:
    """
                    This function returns the RaycastQuery interface object to use.
    
                    Return:
                        :obj:'IRaycastQuery': RaycastQuery interface object.
    """
