from __future__ import annotations
import carb as carb
import copy as copy
import isaacsim.core.api.sensors.base_sensor
from isaacsim.core.api.sensors.base_sensor import BaseSensor
from isaacsim.core.nodes.bindings import _isaacsim_core_nodes
from isaacsim.core.utils.carb import get_carb_setting
from isaacsim.core.utils.prims import define_prim
from isaacsim.core.utils.prims import get_all_matching_child_prims
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import get_prim_path
from isaacsim.core.utils.prims import get_prim_type_name
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.render_product import get_resolution
from isaacsim.core.utils.render_product import set_camera_prim_path
from isaacsim.core.utils.render_product import set_resolution
import math as math
import numpy
import numpy as np
import omni as omni
from omni.graph import core as og
from omni.isaac.IsaacSensorSchema import IsaacRtxLidarSensorAPI
from omni.replicator import core as rep
from omni.syntheticdata import _syntheticdata
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import Vt
__all__ = ['BaseSensor', 'Camera', 'IsaacRtxLidarSensorAPI', 'R_U_TRANSFORM', 'Sdf', 'U_R_TRANSFORM', 'U_W_TRANSFORM', 'Usd', 'UsdGeom', 'Vt', 'W_U_TRANSFORM', 'carb', 'copy', 'define_prim', 'distort_point_kannala_brandt', 'distort_point_rational_polynomial', 'get_all_camera_objects', 'get_all_matching_child_prims', 'get_carb_setting', 'get_prim_at_path', 'get_prim_path', 'get_prim_type_name', 'get_resolution', 'is_prim_path_valid', 'math', 'np', 'og', 'omni', 'point_to_theta', 'rep', 'set_camera_prim_path', 'set_resolution']
class Camera(isaacsim.core.api.sensors.base_sensor.BaseSensor):
    """
    Provides high level functions to deal with a camera prim and its attributes/ properties.
        If there is a camera prim present at the path, it will use it. Otherwise, a new Camera prim at
        the specified prim path will be created.
    
        Args:
            prim_path (str): prim path of the Camera Prim to encapsulate or create.
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "camera".
            frequency (Optional[int], optional): Frequency of the sensor (i.e: how often is the data frame updated).
                                                 Defaults to None.
            dt (Optional[str], optional): dt of the sensor (i.e: period at which a the data frame updated). Defaults to None.
            resolution (Optional[Tuple[int, int]], optional): resolution of the camera (width, height). Defaults to None.
            position (Optional[Sequence[float]], optional): position in the world frame of the prim. shape is (3, ).
                                                        Defaults to None, which means left unchanged.
            translation (Optional[Sequence[float]], optional): translation in the local frame of the prim
                                                            (with respect to its parent prim). shape is (3, ).
                                                            Defaults to None, which means left unchanged.
            orientation (Optional[Sequence[float]], optional): quaternion orientation in the world/ local frame of the prim
                                                            (depends if translation or position is specified).
                                                            quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                            Defaults to None, which means left unchanged.
            render_product_path (str): path to an existing render product, will be used instead of creating a new render product
                                       the resolution and camera attached to this render product will be set based on the input arguments.
                                       Note: Using same render product path on two Camera objects with different camera prims, resolutions is not supported
                                       Defaults to None
    
        
    """
    def __del__(self):
        """
        detach annotators on destroy and destroy the internal render product if it exists
        """
    def __init__(self, prim_path: str, name: str = 'camera', frequency: typing.Optional[int] = None, dt: typing.Optional[str] = None, resolution: typing.Optional[typing.Tuple[int, int]] = None, position: typing.Optional[numpy.ndarray] = None, orientation: typing.Optional[numpy.ndarray] = None, translation: typing.Optional[numpy.ndarray] = None, render_product_path: str = None) -> None:
        ...
    def _data_acquisition_callback(self, event: carb.events._events.IEvent):
        ...
    def _stage_open_callback_fn(self, event):
        ...
    def _timeline_timer_callback_fn(self, event):
        ...
    def add_bounding_box_2d_loose_to_frame(self, init_params: dict = None) -> None:
        """
        Attach the bounding_box_2d_loose annotator to this camera.
                Args:
                    init_params: Optional annotator parameters (e.g. init_params={"semanticTypes": ["prim"]})
        
                The bounding_box_2d_loose annotator returns:
        
                    np.array
                    shape: (num_objects, 1)
                    dtype: np.dtype([
        
                                        ("semanticId", "<u4"),
                                        ("x_min", "<i4"),
                                        ("y_min", "<i4"),
                                        ("x_max", "<i4"),
                                        ("y_max", "<i4"),
                                        ("occlusionRatio", "<f4"),
        
                                    ])
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#bounding-box-2d-loose
                
        """
    def add_bounding_box_2d_tight_to_frame(self, init_params: dict = None) -> None:
        """
        Attach the bounding_box_2d_tight annotator to this camera.
                Args:
                    init_params: Optional annotator parameters (e.g. init_params={"semanticTypes": ["prim"]})
        
                The bounding_box_2d_tight annotator returns:
                    np.array
                    shape: (num_objects, 1)
                    dtype: np.dtype([
        
                                        ("semanticId", "<u4"),
                                        ("x_min", "<i4"),
                                        ("y_min", "<i4"),
                                        ("x_max", "<i4"),
                                        ("y_max", "<i4"),
                                        ("occlusionRatio", "<f4"),
        
                                    ])
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#bounding-box-2d-tight
                
        """
    def add_bounding_box_3d_to_frame(self, init_params: dict = None) -> None:
        """
        Attach the bounding_box_3d annotator to this camera.
                Args:
                    init_params: Optional annotator parameters (e.g. init_params={"semanticTypes": ["prim"]})
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#bounding-box-3d
                
        """
    def add_distance_to_camera_to_frame(self, init_params: dict = None) -> None:
        """
        Attach the distance_to_camera_to_frame annotator to this camera.
                Args:
                    init_params: Optional annotator parameters
                The distance_to_camera_to_frame annotator returns:
        
                    np.array
                    shape: (width, height, 1)
                    dtype: np.float32
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#distance-to-camera
                
        """
    def add_distance_to_image_plane_to_frame(self, init_params: dict = None) -> None:
        """
        Attach the distance_to_image_plane annotator to this camera.
                Args:
                    init_params: Optional annotator parameters
                The distance_to_image_plane annotator returns:
        
                    np.array
                    shape: (width, height, 1)
                    dtype: np.float32
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#distance-to-image-plane
                
        """
    def add_instance_id_segmentation_to_frame(self, init_params: dict = None) -> None:
        """
        Attach the instance_id_segmentation annotator to this camera.
                Args:
                    init_params: Optional parameters specifying the parameters to initialize the annotator with
        
                The instance_id_segmentation annotator returns:
        
                    np.array
                    shape: (width, height, 1) or (width, height, 4) if `colorize` is set to true
                    dtype: np.uint32 or np.uint8 if `colorize` is set to true (e.g. init_params={"colorize": True})
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#instance-id-segmentation
                
        """
    def add_instance_segmentation_to_frame(self, init_params: dict = None) -> None:
        """
        Attach the instance_segmentation annotator to this camera.
                The main difference between instance id segmentation and instance segmentation are that instance segmentation annotator goes down the hierarchy to the lowest level prim which has semantic labels, which instance id segmentation always goes down to the leaf prim.
                Args:
                    init_params: Optional parameters specifying the parameters to initialize the annot (e.g. init_params={"colorize": True})
                The instance_segmentation annotator returns:
        
                    np.array
                    shape: (width, height, 1) or (width, height, 4) if `colorize` is set to true
                    dtype: np.uint32 or np.uint8 if `colorize` is set to true
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#instance-segmentation
                
        """
    def add_motion_vectors_to_frame(self, init_params: dict = None) -> None:
        """
        Attach the motion vectors annotator to this camera.
                Args:
                    init_params: Optional annotator parameters
                The motion vectors annotator returns:
        
                    np.array
                    shape: (width, height, 4)
                    dtype: np.float32
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#motion-vectors
                
        """
    def add_normals_to_frame(self, init_params: dict = None) -> None:
        """
        Attach the normals annotator to this camera.
                Args:
                    init_params: Optional annotator parameters
                The normals annotator returns:
        
                    np.array
                    shape: (width, height, 4)
                    dtype: np.float32
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#normals
                
        """
    def add_occlusion_to_frame(self, init_params: dict = None) -> None:
        """
        Attach the occlusion annotator to this camera.
                Args:
                    init_params: Optional annotator parameters
                The occlusion annotator returns:
        
                    np.array
                    shape: (num_objects, 1)
                    dtype: np.dtype([("instanceId", "<u4"), ("semanticId", "<u4"), ("occlusionRatio", "<f4")])
                
        """
    def add_pointcloud_to_frame(self, include_unlabelled: bool = False, init_params: dict = None) -> None:
        """
        Attach the pointcloud annotator to this camera.
                Args:
                    include_unlabelled: Optional parameter to include unlabelled points in the pointcloud
                    init_params: Optional parameters specifying the parameters to initialize the annotator with
                The pointcloud annotator returns:
        
                    np.array
                    shape: (num_points, 3)
                    dtype: np.float32
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#point-cloud
                
        """
    def add_semantic_segmentation_to_frame(self, init_params: dict = None) -> None:
        """
        Attach the semantic_segmentation annotator to this camera.
                Args:
                    init_params: Optional parameters specifying the parameters to initialize the annotator with
                The semantic_segmentation annotator returns:
        
                    np.array
                    shape: (width, height, 1) or (width, height, 4) if `colorize` is set to true
                    dtype: np.uint32 or np.uint8 if `colorize` is set to true (e.g. init_params={"colorize": True})
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#semantic-segmentation
                
        """
    def get_aspect_ratio(self) -> float:
        """
        
                Returns:
                    float: ratio between width and height
                
        """
    def get_clipping_range(self) -> typing.Tuple[float, float]:
        """
        
                Returns:
                    Tuple[float, float]: near_distance and far_distance respectively.
                
        """
    def get_current_frame(self, clone = False) -> dict:
        """
        
                Args:
                    clone (bool, optional): if True, returns a deepcopy of the current frame. Defaults to False.
                Returns:
                    dict: returns the current frame of data
                
        """
    def get_depth(self) -> numpy.ndarray:
        """
        
                Returns:
                    depth (np.ndarray): (n x m x 1) depth data for each point.
                
        """
    def get_dt(self) -> float:
        """
        
                Returns:
                    float:  gets the dt to acquire new data frames
                
        """
    def get_fisheye_polynomial_properties(self) -> typing.Tuple[float, float, float, float, float, typing.List]:
        """
        
                Returns:
                    Tuple[float, float, float, float, float, List]: nominal_width, nominal_height, optical_centre_x,
                                                                   optical_centre_y, max_fov and polynomial respectively.
                
        """
    def get_focal_length(self) -> float:
        """
        
                Returns:
                    float: Longer Lens Lengths Narrower FOV, Shorter Lens Lengths Wider FOV
                
        """
    def get_focus_distance(self) -> float:
        """
        
                Returns:
                    float: Distance from the camera to the focus plane (in stage units).
                
        """
    def get_frequency(self) -> float:
        """
        
                Returns:
                    float: gets the frequency to acquire new data frames
                
        """
    def get_horizontal_aperture(self) -> float:
        """
        _
                Returns:
                    float:  Emulates sensor/film width on a camera
                
        """
    def get_horizontal_fov(self) -> float:
        """
        
                Returns:
                    float: horizontal field of view in pixels
                
        """
    def get_image_coords_from_world_points(self, points_3d: numpy.ndarray) -> numpy.ndarray:
        """
        Using pinhole perspective projection, this method projects 3d points in the world frame to the image
                   plane giving the pixel coordinates [[0, width], [0, height]]
        
                Args:
                    points_3d (np.ndarray): 3d points (X, Y, Z) in world frame. shape is (n, 3) where n is the number of points.
        
                Returns:
                    np.ndarray: 2d points (u, v) corresponds to the pixel coordinates. shape is (n, 2) where n is the number of points.
                
        """
    def get_intrinsics_matrix(self) -> numpy.ndarray:
        """
        
                Returns:
                    np.ndarray: the intrinsics of the camera (used for calibration)
                
        """
    def get_lens_aperture(self) -> float:
        """
        
                Returns:
                    float: controls lens aperture (i.e focusing). 0 turns off focusing.
                
        """
    def get_local_pose(self, camera_axes: str = 'world') -> None:
        """
        Gets prim's pose with respect to the local frame (the prim's parent frame in the world axes).
        
                Args:
                    camera_axes (str, optional): camera axes, world is (+Z up, +X forward), ros is (+Y up, +Z forward) and usd is (+Y up and -Z forward). Defaults to "world".
        
                Returns:
                    Tuple[np.ndarray, np.ndarray]: first index is position in the local frame of the prim. shape is (3, ).
                                                   second index is quaternion orientation in the local frame of the prim.
                                                   quaternion is scalar-first (w, x, y, z). shape is (4, ).
                
        """
    def get_pointcloud(self) -> numpy.ndarray:
        """
        
                Returns:
                    pointcloud (np.ndarray):  (N x 3) 3d points (X, Y, Z) in camera frame. Shape is (N x 3) where N is the number of points.
                Note:
                    This currently uses the depth annotator to generate the pointcloud. In the future, this will be switched to use
                    the pointcloud annotator.
                
        """
    def get_projection_mode(self) -> str:
        """
        
                Returns:
                    str: perspective or orthographic.
                
        """
    def get_projection_type(self) -> str:
        """
        
                Returns:
                    str: pinhole, fisheyeOrthographic, fisheyeEquidistant, fisheyeEquisolid, fisheyePolynomial or fisheyeSpherical
                
        """
    def get_render_product_path(self) -> str:
        """
        
                Returns:
                    string: gets the path to the render product attached to this camera
                
        """
    def get_resolution(self) -> typing.Tuple[int, int]:
        """
        
                Returns:
                    Tuple[int, int]: width and height respectively.
                
        """
    def get_rgb(self) -> numpy.ndarray:
        """
        
                Returns:
                    rgb (np.ndarray): (N x 3) RGB color data for each point.
                
        """
    def get_rgba(self) -> numpy.ndarray:
        """
        
                Returns:
                    rgba (np.ndarray): (N x 4) RGBa color data for each point.
                
        """
    def get_shutter_properties(self) -> typing.Tuple[float, float]:
        """
        
                Returns:
                    Tuple[float, float]: delay_open and delay close respectively.
                
        """
    def get_stereo_role(self) -> str:
        """
        
                Returns:
                    str: mono, left or right.
                
        """
    def get_vertical_aperture(self) -> float:
        """
        
                Returns:
                    float: Emulates sensor/film height on a camera.
                
        """
    def get_vertical_fov(self) -> float:
        """
        
                Returns:
                    float: vertical field of view in pixels
                
        """
    def get_view_matrix_ros(self):
        """
        3D points in World Frame -> 3D points in Camera Ros Frame
        
                Returns:
                    np.ndarray: the view matrix that transforms 3d points in the world frame to 3d points in the camera axes
                                with ros camera convention.
                
        """
    def get_world_points_from_image_coords(self, points_2d: numpy.ndarray, depth: numpy.ndarray):
        """
        Using pinhole perspective projection, this method does the inverse projection given the depth of the
                   pixels
        
                Args:
                    points_2d (np.ndarray): 2d points (u, v) corresponds to the pixel coordinates. shape is (n, 2) where n is the number of points.
                    depth (np.ndarray): depth corresponds to each of the pixel coords. shape is (n,)
        
                Returns:
                    np.ndarray: (n, 3) 3d points (X, Y, Z) in world frame. shape is (n, 3) where n is the number of points.
                
        """
    def get_world_pose(self, camera_axes: str = 'world') -> typing.Tuple[numpy.ndarray, numpy.ndarray]:
        """
        Gets prim's pose with respect to the world's frame (always at [0, 0, 0] and unity quaternion not to be confused with /World Prim)
        
                Args:
                    camera_axes (str, optional): camera axes, world is (+Z up, +X forward), ros is (+Y up, +Z forward) and usd is (+Y up and -Z forward). Defaults to "world".
        
                Returns:
                    Tuple[np.ndarray, np.ndarray]: first index is position in the world frame of the prim. shape is (3, ).
                                                   second index is quaternion orientation in the world frame of the prim.
                                                   quaternion is scalar-first (w, x, y, z). shape is (4, ).
                
        """
    def initialize(self, physics_sim_view = None) -> None:
        """
        To be called before using this class after a reset of the world
        
                Args:
                    physics_sim_view (_type_, optional): _description_. Defaults to None.
                
        """
    def is_paused(self) -> bool:
        """
        
                Returns:
                    bool: is data collection paused.
                
        """
    def pause(self) -> None:
        """
        pauses data collection and updating the data frame
        """
    def post_reset(self) -> None:
        ...
    def remove_bounding_box_2d_loose_from_frame(self) -> None:
        ...
    def remove_bounding_box_2d_tight_from_frame(self) -> None:
        ...
    def remove_bounding_box_3d_from_frame(self) -> None:
        ...
    def remove_distance_to_camera_from_frame(self) -> None:
        ...
    def remove_distance_to_image_plane_from_frame(self) -> None:
        ...
    def remove_instance_id_segmentation_from_frame(self) -> None:
        ...
    def remove_instance_segmentation_from_frame(self) -> None:
        ...
    def remove_motion_vectors_from_frame(self) -> None:
        ...
    def remove_normals_from_frame(self) -> None:
        ...
    def remove_occlusion_from_frame(self) -> None:
        ...
    def remove_pointcloud_from_frame(self) -> None:
        ...
    def remove_semantic_segmentation_from_frame(self) -> None:
        ...
    def resume(self) -> None:
        """
        resumes data collection and updating the data frame
        """
    def set_clipping_range(self, near_distance: typing.Optional[float] = None, far_distance: typing.Optional[float] = None) -> None:
        """
        Clips the view outside of both near and far range values.
        
                Args:
                    near_distance (Optional[float], optional): value to be used for near clipping. Defaults to None.
                    far_distance (Optional[float], optional): value to be used for far clipping. Defaults to None.
                
        """
    def set_dt(self, value: float) -> None:
        """
        
                Args:
                    value (float):  sets the dt to acquire new data frames
        
                
        """
    def set_fisheye_polynomial_properties(self, nominal_width: typing.Optional[float], nominal_height: typing.Optional[float], optical_centre_x: typing.Optional[float], optical_centre_y: typing.Optional[float], max_fov: typing.Optional[float], polynomial: typing.Optional[typing.Sequence[float]]) -> None:
        """
        
                Args:
                    nominal_width (Optional[float]): Rendered Width (pixels)
                    nominal_height (Optional[float]): Rendered Height (pixels)
                    optical_centre_x (Optional[float]): Horizontal Render Position (pixels)
                    optical_centre_y (Optional[float]): Vertical Render Position (pixels)
                    max_fov (Optional[float]): maximum field of view (pixels)
                    polynomial (Optional[Sequence[float]]): polynomial equation coefficients (sequence of 5 numbers) starting from A0, A1, A2, A3, A4
                
        """
    def set_focal_length(self, value: float):
        """
        
                Args:
                    value (float): Longer Lens Lengths Narrower FOV, Shorter Lens Lengths Wider FOV
                
        """
    def set_focus_distance(self, value: float):
        """
        The distance at which perfect sharpness is achieved.
        
                Args:
                    value (float): Distance from the camera to the focus plane (in stage units).
                
        """
    def set_frequency(self, value: int) -> None:
        """
        
                Args:
                    value (int): sets the frequency to acquire new data frames
                
        """
    def set_horizontal_aperture(self, value: float) -> None:
        """
        
                Args:
                    value (Optional[float], optional): Emulates sensor/film width on a camera. Defaults to None.
                
        """
    def set_kannala_brandt_properties(self, nominal_width: float, nominal_height: float, optical_centre_x: float, optical_centre_y: float, max_fov: typing.Optional[float], distortion_model: typing.Sequence[float]) -> None:
        """
        Approximates kannala brandt distortion with ftheta fisheye polynomial coefficients.
                Args:
                    nominal_width (float): Rendered Width (pixels)
                    nominal_height (float): Rendered Height (pixels)
                    optical_centre_x (float): Horizontal Render Position (pixels)
                    optical_centre_y (float): Vertical Render Position (pixels)
                    max_fov (Optional[float]): maximum field of view (pixels)
                    distortion_model (Sequence[float]): kannala brandt generic distortion model coefficients (k1, k2, k3, k4)
                
        """
    def set_lens_aperture(self, value: float):
        """
        Controls Distance Blurring. Lower Numbers decrease focus range, larger
                    numbers increase it.
        
                Args:
                    value (float): controls lens aperture (i.e focusing). 0 turns off focusing.
                
        """
    def set_local_pose(self, translation: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None, camera_axes: str = 'world') -> None:
        """
        Sets prim's pose with respect to the local frame (the prim's parent frame in the world axes).
        
                Args:
                    translation (Optional[Sequence[float]], optional): translation in the local frame of the prim
                                                                  (with respect to its parent prim). shape is (3, ).
                                                                  Defaults to None, which means left unchanged.
                    orientation (Optional[Sequence[float]], optional): quaternion orientation in the local frame of the prim.
                                                                  quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                                  Defaults to None, which means left unchanged.
                    camera_axes (str, optional): camera axes, world is (+Z up, +X forward), ros is (+Y up, +Z forward) and usd is (+Y up and -Z forward). Defaults to "world".
                
        """
    def set_matching_fisheye_polynomial_properties(self, nominal_width: float, nominal_height: float, optical_centre_x: float, optical_centre_y: float, max_fov: typing.Optional[float], distortion_model: typing.Sequence[float], distortion_fn: typing.Callable) -> None:
        """
        Approximates given distortion with ftheta fisheye polynomial coefficients.
                Args:
                    nominal_width (float): Rendered Width (pixels)
                    nominal_height (float): Rendered Height (pixels)
                    optical_centre_x (float): Horizontal Render Position (pixels)
                    optical_centre_y (float): Vertical Render Position (pixels)
                    max_fov (Optional[float]): maximum field of view (pixels)
                    distortion_model (Sequence[float]): distortion model coefficients
                    distortion_fn (Callable): distortion function that takes points and returns distorted points
                
        """
    def set_projection_mode(self, value: str) -> None:
        """
        Sets camera to perspective or orthographic mode.
        
                Args:
                    value (str): perspective or orthographic.
        
                
        """
    def set_projection_type(self, value: str) -> None:
        """
        
                Args:
                    value (str): pinhole: Standard Camera Projection (Disable Fisheye)
                                 fisheyeOrthographic: Full Frame using Orthographic Correction
                                 fisheyeEquidistant: Full Frame using Equidistant Correction
                                 fisheyeEquisolid: Full Frame using Equisolid Correction
                                 fisheyePolynomial: 360 Degree Spherical Projection
                                 fisheyeSpherical: 360 Degree Full Frame Projection
                
        """
    def set_rational_polynomial_properties(self, nominal_width: float, nominal_height: float, optical_centre_x: float, optical_centre_y: float, max_fov: typing.Optional[float], distortion_model: typing.Sequence[float]) -> None:
        """
        Approximates rational polynomial distortion with ftheta fisheye polynomial coefficients.
                Args:
                    nominal_width (float): Rendered Width (pixels)
                    nominal_height (float): Rendered Height (pixels)
                    optical_centre_x (float): Horizontal Render Position (pixels)
                    optical_centre_y (float): Vertical Render Position (pixels)
                    max_fov (Optional[float]): maximum field of view (pixels)
                    distortion_model (Sequence[float]): rational polynomial distortion model coefficients (k1, k2, p1, p2, k3, k4, k5, k6)
                
        """
    def set_resolution(self, value: typing.Tuple[int, int]) -> None:
        """
        
        
                Args:
                    value (Tuple[int, int]): width and height respectively.
        
                
        """
    def set_shutter_properties(self, delay_open: typing.Optional[float] = None, delay_close: typing.Optional[float] = None) -> None:
        """
        
                Args:
                    delay_open (Optional[float], optional): Used with Motion Blur to control blur amount, increased values delay shutter opening. Defaults to None.
                    delay_close (Optional[float], optional): Used with Motion Blur to control blur amount, increased values forward the shutter close. Defaults to None.
                
        """
    def set_stereo_role(self, value: str) -> None:
        """
        
                Args:
                    value (str): mono, left or right.
                
        """
    def set_vertical_aperture(self, value: float) -> None:
        """
        
                Args:
                    value (Optional[float], optional): Emulates sensor/film height on a camera. Defaults to None.
                
        """
    def set_world_pose(self, position: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None, camera_axes: str = 'world') -> None:
        """
        Sets prim's pose with respect to the world's frame (always at [0, 0, 0] and unity quaternion not to be confused with /World Prim).
        
                Args:
                    position (Optional[Sequence[float]], optional): position in the world frame of the prim. shape is (3, ).
                                                               Defaults to None, which means left unchanged.
                    orientation (Optional[Sequence[float]], optional): quaternion orientation in the world frame of the prim.
                                                                  quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                                  Defaults to None, which means left unchanged.
                    camera_axes (str, optional): camera axes, world is (+Z up, +X forward), ros is (+Y up, +Z forward) and usd is (+Y up and -Z forward). Defaults to "world".
                
        """
    @property
    def supported_annotators(self) -> typing.List[str]:
        """
        
                Returns:
                    List[str]: annotators supported by the camera
                
        """
def distort_point_kannala_brandt(camera_matrix, distortion_model, x, y):
    """
    This helper function distorts point(s) using Kannala Brandt fisheye model.
        It should be equivalent to the following reference that uses OpenCV:
    
        def distort_point_kannala_brandt2(camera_matrix, distortion_model, x, y):
            import cv2
            ((fx,_,cx),(_,fy,cy),(_,_,_)) = camera_matrix
            pt_x, pt_y, pt_z  = (x-cx)/fx, (y-cy)/fy, np.full(x.shape, 1.0)
            points3d = np.stack((pt_x, pt_y, pt_z), axis = -1)
            rvecs, tvecs = np.array([0.0,0.0,0.0]), np.array([0.0,0.0,0.0])
            cameraMatrix, distCoeffs = np.array(camera_matrix), np.array(distortion_model)
            points, jac = cv2.fisheye.projectPoints(np.expand_dims(points3d, 1), rvecs, tvecs, cameraMatrix, distCoeffs)
            return np.array([points[:,0,0], points[:,0,1]])
        
    """
def distort_point_rational_polynomial(camera_matrix, distortion_model, x, y):
    """
    This helper function distorts point(s) using rational polynomial model.
        It should be equivalent to the following reference that uses OpenCV:
    
        def distort_point_rational_polynomial(x, y)
            import cv2
            ((fx,_,cx),(_,fy,cy),(_,_,_)) = camera_matrix
            pt_x, pt_y, pt_z  = (x-cx)/fx, (y-cy)/fy, np.full(x.shape, 1.0)
            points3d = np.stack((pt_x, pt_y, pt_z), axis = -1)
            rvecs, tvecs = np.array([0.0,0.0,0.0]), np.array([0.0,0.0,0.0])
            cameraMatrix, distCoeffs = np.array(camera_matrix), np.array(distortion_coefficients)
            points, jac = cv2.projectPoints(points3d, rvecs, tvecs, cameraMatrix, distCoeffs)
            return np.array([points[:,0,0], points[:,0,1]])
        
    """
def get_all_camera_objects(root_prim: str = '/'):
    """
    Retrieve isaacsim.sensors.camera Camera objects for each camera in the scene.
    
        Args:
            root_prim (str): Root prim where the world exists.
    
        Returns:
            Camera[]: A list of isaacsim.sensors.camera Camera objects
        
    """
def point_to_theta(camera_matrix, x, y):
    """
    This helper function returns the theta angle of the point.
    """
R_U_TRANSFORM: numpy.ndarray  # value = array([[ 1,  0,  0,  0],...
U_R_TRANSFORM: numpy.ndarray  # value = array([[ 1,  0,  0,  0],...
U_W_TRANSFORM: numpy.ndarray  # value = array([[ 0, -1,  0,  0],...
W_U_TRANSFORM: numpy.ndarray  # value = array([[ 0,  0, -1,  0],...
