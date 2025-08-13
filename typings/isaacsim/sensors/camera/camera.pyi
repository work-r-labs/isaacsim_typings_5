from __future__ import annotations
import carb as carb
import copy as copy
import isaacsim.core.api.sensors.base_sensor
from isaacsim.core.api.sensors.base_sensor import BaseSensor
from isaacsim.core.nodes.bindings import _isaacsim_core_nodes
from isaacsim.core.utils.carb import get_carb_setting
from isaacsim.core.utils import numpy as np_utils
from isaacsim.core.utils.prims import define_prim
from isaacsim.core.utils.prims import get_all_matching_child_prims
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import get_prim_path
from isaacsim.core.utils.prims import get_prim_type_name
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.render_product import get_resolution
from isaacsim.core.utils.render_product import set_camera_prim_path
from isaacsim.core.utils.render_product import set_resolution
from isaacsim.core.utils import torch as torch_utils
from isaacsim.core.utils import warp as warp_utils
import math as math
import numpy as np
import numpy
import omni as omni
from omni.graph import core as og
from omni.isaac.IsaacSensorSchema import IsaacRtxLidarSensorAPI
from omni.replicator import core as rep
from omni.syntheticdata import _syntheticdata
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import Vt
import torch as torch
import typing
import warp as wp
__all__: list[str] = ['BaseSensor', 'Camera', 'FTHETA_ATTRIBUTE_MAP', 'IsaacRtxLidarSensorAPI', 'KANNALA_BRANDT_K3_ATTRIBUTE_MAP', 'OPENCV_FISHEYE_ATTRIBUTE_MAP', 'OPENCV_PINHOLE_ATTRIBUTE_MAP', 'RAD_TAN_THIN_PRISM_ATTRIBUTE_MAP', 'R_U_TRANSFORM', 'Sdf', 'USD_CAMERA_TENTHS_TO_STAGE_UNIT', 'U_R_TRANSFORM', 'U_W_TRANSFORM', 'Usd', 'UsdGeom', 'Vt', 'W_U_TRANSFORM', 'carb', 'copy', 'define_prim', 'distort_point_kannala_brandt', 'distort_point_rational_polynomial', 'get_all_camera_objects', 'get_all_matching_child_prims', 'get_carb_setting', 'get_prim_at_path', 'get_prim_path', 'get_prim_type_name', 'get_resolution', 'is_prim_path_valid', 'math', 'np', 'np_utils', 'og', 'omni', 'point_to_theta', 'rep', 'set_camera_prim_path', 'set_resolution', 'torch', 'torch_utils', 'warp_utils', 'wp']
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
            dt (Optional[float], optional): dt of the sensor (i.e: period at which a the data frame updated). Defaults to None.
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
        Destructor that calls destroy() to clean up resources.
        """
    def __init__(self, prim_path: str, name: str = 'camera', frequency: int | None = None, dt: float | None = None, resolution: tuple[int, int] | None = None, position: np.ndarray | None = None, orientation: np.ndarray | None = None, translation: np.ndarray | None = None, render_product_path: str = None, annotator_device: str = None) -> None:
        ...
    def _data_acquisition_callback(self, event: carb.events.IEvent):
        ...
    def _get_lens_distortion_properties(self, distortion_model_attr: str, attr_names: list[str], coefficient_map: list[str]) -> tuple[float]:
        """
        Gets lens distortion model parameters if camera prim is using lens distortion model.
        
                Returns:
                    Tuple[float, float, Tuple[float, float], float, List[float]]:
                        nominal_height, nominal_width, optical_center, max_fov, distortion_coefficients
                        where distortion_coefficients are in order:
                
        """
    def _maintain_square_pixel_aperture(self, mode: str = 'horizontal'):
        """
        Ensure apertures are in sync with aspect ratio to maintain square pixels.
        
                Args:
                    mode (str): 'horizontal' to use horizontal aperture as source, 'vertical' to use vertical as source. Defaults to 'horizontal' if None or invalid.
                
        """
    def _set_lens_distortion_properties(self, distortion_model: str, distortion_model_attr: str, coefficient_map: list[str], coefficients: list[float], **kwargs) -> None:
        """
        Sets lens distortion model parameters if camera prim is using lens distortion model.
        """
    def _stage_open_callback_fn(self, event):
        ...
    def _timeline_timer_callback_fn(self, event):
        ...
    def add_bounding_box_2d_loose_to_frame(self, init_params: dict = {}) -> None:
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
    def add_bounding_box_2d_tight_to_frame(self, init_params: dict = {}) -> None:
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
    def add_bounding_box_3d_to_frame(self, init_params: dict = {}) -> None:
        """
        Attach the bounding_box_3d annotator to this camera.
                Args:
                    init_params: Optional annotator parameters (e.g. init_params={"semanticTypes": ["prim"]})
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#bounding-box-3d
                
        """
    def add_distance_to_camera_to_frame(self, init_params: dict = {}) -> None:
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
    def add_distance_to_image_plane_to_frame(self, init_params: dict = {}) -> None:
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
    def add_instance_id_segmentation_to_frame(self, init_params: dict = {}) -> None:
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
    def add_instance_segmentation_to_frame(self, init_params: dict = {}) -> None:
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
    def add_motion_vectors_to_frame(self, init_params: dict = {}) -> None:
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
    def add_normals_to_frame(self, init_params: dict = {}) -> None:
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
    def add_occlusion_to_frame(self, init_params: dict = {}) -> None:
        """
        Attach the occlusion annotator to this camera.
                Args:
                    init_params: Optional annotator parameters
                The occlusion annotator returns:
        
                    np.array
                    shape: (num_objects, 1)
                    dtype: np.dtype([("instanceId", "<u4"), ("semanticId", "<u4"), ("occlusionRatio", "<f4")])
                
        """
    def add_pointcloud_to_frame(self, include_unlabelled: bool = True, init_params: dict = {}) -> None:
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
    def add_rgb_to_frame(self, init_params: dict = {}) -> None:
        """
        Attach the rgb annotator to this camera.
                Args:
                    init_params: Optional annotator parameters
        
                The rgbannotator returns:
        
                    np.array
                    shape: (width, height, 4)
                    dtype: np.float32
        
                See more details: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#ldrcolor
                
        """
    def add_semantic_segmentation_to_frame(self, init_params: dict = {}) -> None:
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
    def attach_annotator(self, annotator_name: str, **kwargs) -> None:
        """
        Attach an annotator to the camera.
        
                Args:
                    annotator_name (str): Name of the annotator to attach.
                    **kwargs: Additional arguments to pass to the annotator.
        
                Raises:
                    rep.annotators.AnnotatorRegistryError: If the annotator is not found.
                
        """
    def destroy(self) -> None:
        """
        Destroy the camera by detaching all annotators and destroying the internal render product.
        """
    def detach_annotator(self, annotator_name: str) -> None:
        """
        Detach an annotator from the camera.
        
                Args:
                    annotator_name (str): Name of the annotator to detach.
                
        """
    def get_aspect_ratio(self) -> float:
        """
        
                Returns:
                    float: ratio between width and height
                
        """
    def get_camera_points_from_image_coords(self, points_2d, depth, device: str = None, backend_utils_cls: type = None):
        """
        Using pinhole perspective projection, this method does the inverse projection given the depth of the
                    pixels to get 3D points in camera frame.
        
                Args:
                    points_2d: 2d points (u, v) corresponds to the pixel coordinates. shape is (n, 2) where n is the number of points.
                    depth: depth corresponds to each of the pixel coords. shape is (n,)
                    device: str, optional, default is None. If None, uses self._device.
                        Device to place tensors on. Select from ['cpu', 'cuda', 'cuda:<device_index>']
                    backend_utils_cls: type, optional, default is None. If None, the class will be inferred from self._backend_utils.
                        Supported classes are np_utils, torch_utils, and warp_utils.
        
                Returns:
                    np.ndarray | torch.Tensor | wp.array: (n, 3) 3d points (X, Y, Z) in camera frame.
                        +Z points forward (optical axis), +X right, +Y down
                
        """
    def get_clipping_range(self) -> tuple[float, float]:
        """
        Gets near and far clipping distances of camera prim.
        
                Returns:
                    Tuple[float, float]: Near and far clipping distances (in stage units).
                
        """
    def get_current_frame(self, clone = False) -> dict:
        """
        
                Args:
                    clone (bool, optional): if True, returns a deepcopy of the current frame. Defaults to False.
                Returns:
                    dict: returns the current frame of data
                
        """
    def get_depth(self, device: str = None) -> np.ndarray | wp.types.array:
        """
        Gets the depth data from the camera sensor as distance to image plane.
        
                Args:
                    device (str, optional): Device to hold data in. Select from `['cpu', 'cuda', 'cuda:<device_index>']`.
                        Defaults to None, which uses the device specified on annotator initialization (annotator_device)
                Returns:
                    depth (np.ndarray): (n x m) depth data for each point.
                    wp.types.array: (n x m) depth data for each point.
                
        """
    def get_dt(self) -> float:
        """
        
                Returns:
                    float:  gets the dt to acquire new data frames
                
        """
    def get_fisheye_polynomial_properties(self) -> tuple[float, float, float, float, float, list]:
        """
        
                Returns:
                    Tuple[float, float, float, float, float, List]: nominal_width, nominal_height, optical_centre_x,
                                                                   optical_centre_y, max_fov and polynomial respectively.
                
        """
    def get_focal_length(self) -> float:
        """
        
                Gets focal length of camera prim, in stage units. Longer focal length corresponds to narrower FOV, shorter focal length corresponds to wider FOV.
        
                Returns:
                    float: Value of camera prim focalLength attribute, converted to stage units.
                
        """
    def get_focus_distance(self) -> float:
        """
        Gets distance from the camera to the focus plane (in stage units).
        
                Returns:
                    float: Value of camera prim focusDistance attribute, measuring distance from the camera to the focus plane (in stage units).
                
        """
    def get_frequency(self) -> float:
        """
        
                Returns:
                    float: gets the frequency to acquire new data frames
                
        """
    def get_ftheta_properties(self) -> tuple[float, float, tuple[float, float], float, list[float]]:
        """
        Gets F-theta lens distortion model parameters if camera prim is using F-theta distortion model.
        
                Returns:
                    Tuple[float, float, Tuple[float, float], float, List[float]]:
                        nominal_height (pixels), nominal_width (pixels), optical_center (x,y in pixels), max_fov (degrees), distortion_coefficients
                        where distortion_coefficients are in order:
                        [k0, k1, k2, k3, k4] - radial distortion coefficients
                
        """
    def get_horizontal_aperture(self) -> float:
        """
        Get horizontal aperture (sensor width) in stage units.
        
                Only square pixels are supported; vertical aperture should match aspect ratio.
        
                Returns:
                    float: Horizontal aperture in stage units.
                
        """
    def get_horizontal_fov(self) -> float:
        """
        
                Returns:
                    float: horizontal field of view in pixels
                
        """
    def get_image_coords_from_world_points(self, points_3d: np.ndarray) -> np.ndarray:
        """
        Using pinhole perspective projection, this method projects 3d points in the world frame to the image
                   plane giving the pixel coordinates [[0, width], [0, height]]
        
                Args:
                    points_3d (np.ndarray): 3d points (X, Y, Z) in world frame. shape is (n, 3) where n is the number of points.
        
                Returns:
                    np.ndarray: 2d points (u, v) corresponds to the pixel coordinates. shape is (n, 2) where n is the number of points.
                
        """
    def get_intrinsics_matrix(self, device: str = None, backend_utils_cls: type = None):
        """
        Get the intrinsics matrix of the camera.
        
                Args:
                    device: str, optional, default is None. If None, uses self._device.
                        Device to place tensors on. Select from ['cpu', 'cuda', 'cuda:<device_index>']
                    backend_utils_cls: type, optional, default is None. If None, the class will be inferred from self._backend_utils.
                        Supported classes are np_utils, torch_utils, and warp_utils.
        
                Returns:
                    np.ndarray | torch.Tensor | wp.array: The intrinsics matrix of the camera (used for calibration)
                
        """
    def get_kannala_brandt_k3_properties(self) -> tuple[float, float, tuple[float, float], float, list[float]]:
        """
        Gets Kannala-Brandt K3 lens distortion model parameters if camera prim is using Kannala-Brandt K3 distortion model.
        
                Returns:
                    Tuple[float, float, Tuple[float, float], float, List[float]]:
                        nominal_height, nominal_width, optical_center, max_fov, distortion_coefficients
                        where distortion_coefficients are in order:
                        [k0, k1, k2, k3] - radial distortion coefficients
                
        """
    def get_lens_aperture(self) -> float:
        """
        Gets value of camera prim fStop attribute, which controls distance blurring. Lower numbers decrease focus range, larger
                    numbers increase it.
        
                Returns:
                    float: Value of camera prim fStop attribute. 0 turns off focusing.
                
        """
    def get_lens_distortion_model(self) -> str:
        """
        
                Gets the `omni:lensdistortion:model` property of the camera prim.
                
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
    def get_lut_properties(self) -> tuple[float, float, tuple[float, float], str, str]:
        """
        Gets LUT lens distortion model parameters if camera prim is using LUT distortion model.
        
                Returns:
                    Tuple[float, float, Tuple[float, float], str, str]:
                        nominal_height (pixels), nominal_width (pixels), optical_center (x,y in pixels),
                        ray_enter_direction_texture, ray_exit_position_texture
                
        """
    def get_opencv_fisheye_properties(self) -> tuple[float, float, float, float, list]:
        """
        
                If camera prim is using OpenCV fisheye distortion model, returns corresponding distortion parameters.
        
                Returns:
                    Tuple[float, float, float, float, List]: cx, cy, fx, fy, and OpenCV fisheye parameters [k1, k2, k3, k4] respectively.
                
        """
    def get_opencv_pinhole_properties(self) -> tuple[float, float, float, float, list]:
        """
        
                If camera prim is using OpenCV pinhole distortion model, returns corresponding distortion parameters.
        
                Returns:
                    Tuple[float, float, float, float, List]: cx, cy, fx, fy, and OpenCV pinhole parameters [k1, k2, p1, p2, k3, k4, k5, k6, s1, s2, s3, s4] respectively.
                
        """
    def get_pointcloud(self, device: str = None, world_frame: bool = True) -> np.ndarray | wp.array:
        """
        Get a 3D pointcloud from the camera sensor.
        
                This method attempts to use the pointcloud annotator first, falling back to depth-based
                calculation using the distance_to_image_plane annotator and perspective projection with
                the camera's intrinsic parameters.
        
                Args:
                    device: Device to place tensors on. Select from ['cpu', 'cuda', 'cuda:<device_index>'].
                        If None, uses self._annotator_device.
                    world_frame: If True, returns points in world frame. If False, returns points in camera frame.
        
                Returns:
                    np.ndarray | wp.array: A (N x 3) array of 3D points (X, Y, Z) in either world or camera frame,
                           where N is the number of points.
                Note:
                    The fallback method uses the depth (distance_to_image_plane) annotator and
                    performs a perspective projection using the camera's intrinsic parameters to generate the pointcloud.
                    Point ordering may differ between the pointcloud annotator and depth-based fallback methods,
                    even though the 3D locations are equivalent.
                
        """
    def get_projection_mode(self) -> str:
        """
        
                Gets projection model of the camera prim.
        
                Returns:
                    str: perspective or orthographic.
                
        """
    def get_projection_type(self) -> str:
        """
        
                [DEPRECATED] Gets the `cameraProjectionType` property of the camera prim.
        
                Returns:
                    str: omni:lensdistortion:model attribute of camera prim. If unset, returns "pinhole".
                
        """
    def get_rad_tan_thin_prism_properties(self) -> tuple[float, float, tuple[float, float], float, list[float]]:
        """
        Gets Radial-Tangential Thin Prism lens distortion model parameters if camera prim is using Radial-Tangential Thin Prism distortion model.
        
                Returns:
                    Tuple[float, float, Tuple[float, float], float, List[float]]:
                        nominal_height, nominal_width, optical_center, max_fov, distortion_coefficients
                        where distortion_coefficients are in order:
                        [k0, k1, k2, k3, k4, k5] - radial distortion coefficients
                        [p0, p1] - tangential distortion coefficients
                        [s0, s1, s2, s3] - thin prism distortion coefficients
                
        """
    def get_render_product_path(self) -> str:
        """
        
                Returns:
                    string: gets the path to the render product attached to this camera
                
        """
    def get_resolution(self) -> tuple[int, int]:
        """
        
                Returns:
                    Tuple[int, int]: width and height respectively.
                
        """
    def get_rgb(self, device: str = None) -> np.ndarray | wp.types.array:
        """
        
                Args:
                    device (str, optional): Device to hold data in. Select from `['cpu', 'cuda', 'cuda:<device_index>']`.
                        Defaults to None, which uses the device specified on annotator initialization (annotator_device)
        
                Returns:
                    rgb (np.ndarray): (N x 3) RGB color data for each point.
                    wp.types.array: (N x 3) RGB color data for each point.
                
        """
    def get_rgba(self, device: str = None) -> np.ndarray | wp.types.array:
        """
        
                Args:
                    device (str, optional): Device to hold data in. Select from `['cpu', 'cuda', 'cuda:<device_index>']`.
                        Defaults to None, which uses the device specified on annotator initialization (annotator_device)
        
                Returns:
                    rgba (np.ndarray): (N x 4) RGBa color data for each point.
                    wp.types.array: (N x 4) RGBa color data for each point.
                
        """
    def get_shutter_properties(self) -> tuple[float, float]:
        """
        
                Returns:
                    Tuple[float, float]: delay_open and delay close respectively.
                
        """
    def get_stereo_role(self) -> str:
        """
        
                Gets stereo role of the camera prim.
                Returns:
                    str: "mono", "left" or "right".
                
        """
    def get_vertical_aperture(self) -> float:
        """
        Get vertical aperture (sensor height) in stage units.
        
                This function ensures the vertical aperture is always synchronized with the aspect ratio and horizontal aperture to maintain square pixels. If not, it will automatically correct the value.
        
                Returns:
                    float: Vertical aperture in stage units, always in sync with the aspect ratio and horizontal aperture.
                
        """
    def get_vertical_fov(self) -> float:
        """
        
                Returns:
                    float: vertical field of view in pixels
                
        """
    def get_view_matrix_ros(self, device: str = None, backend_utils_cls: type = None):
        """
        3D points in World Frame -> 3D points in Camera Ros Frame
        
                Args:
                    device: str, optional, default is None. If None, uses self._device.
                        Device to place tensors on. Select from ['cpu', 'cuda', 'cuda:<device_index>']
                    backend_utils_cls: type, optional, default is None. If None, the class will be inferred from self._backend_utils.
                        Supported classes are np_utils, torch_utils, and warp_utils.
        
                Returns:
                    The view matrix that transforms 3d points in the world frame to 3d points in the camera axes
                        with ros camera convention.
                
        """
    def get_world_points_from_image_coords(self, points_2d, depth, device: str = None, backend_utils_cls: type = None):
        """
        Using pinhole perspective projection, this method does the inverse projection given the depth of the
                    pixels to get 3D points in world frame.
        
                Args:
                    points_2d: 2d points (u, v) corresponds to the pixel coordinates. shape is (n, 2) where n is the number of points.
                    depth: depth corresponds to each of the pixel coords. shape is (n,)
                    device: str, optional, default is None. If None, uses self._device.
                        Device to place tensors on. Select from ['cpu', 'cuda', 'cuda:<device_index>']
                    backend_utils_cls: type, optional, default is None. If None, the class will be inferred from self._backend_utils.
                        Supported classes are np_utils, torch_utils, and warp_utils.
        
                Returns:
                    np.ndarray | torch.Tensor | wp.array: (n, 3) 3d points (X, Y, Z) in world frame.
                
        """
    def get_world_pose(self, camera_axes: str = 'world') -> tuple[np.ndarray, np.ndarray]:
        """
        Gets prim's pose with respect to the world's frame (always at [0, 0, 0] and unity quaternion not to be confused with /World Prim)
        
                Args:
                    camera_axes (str, optional): camera axes, world is (+Z up, +X forward), ros is (+Y up, +Z forward) and usd is (+Y up and -Z forward). Defaults to "world".
        
                Returns:
                    Tuple[np.ndarray, np.ndarray]: first index is position in the world frame of the prim. shape is (3, ).
                                                   second index is quaternion orientation in the world frame of the prim.
                                                   quaternion is scalar-first (w, x, y, z). shape is (4, ).
                
        """
    def initialize(self, physics_sim_view = None, attach_rgb_annotator = True) -> None:
        """
        To be called before using this class after a reset of the world
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
                    attach_rgb_annotator (bool, optional): True to attach the rgb annotator to the camera. Defaults to True. Set to False to improve performance.
                
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
        """
        Detach the bounding_box_2d_loose annotator from the camera.
        """
    def remove_bounding_box_2d_tight_from_frame(self) -> None:
        """
        Detach the bounding_box_2d_tight annotator from the camera.
        """
    def remove_bounding_box_3d_from_frame(self) -> None:
        """
        Detach the bounding_box_3d annotator from the camera.
        """
    def remove_distance_to_camera_from_frame(self) -> None:
        """
        Detach the distance_to_camera annotator from the camera.
        """
    def remove_distance_to_image_plane_from_frame(self) -> None:
        """
        Detach the distance_to_image_plane annotator from the camera.
        """
    def remove_instance_id_segmentation_from_frame(self) -> None:
        """
        Detach the instance_id_segmentation annotator from the camera.
        """
    def remove_instance_segmentation_from_frame(self) -> None:
        """
        Detach the instance_segmentation annotator from the camera.
        """
    def remove_motion_vectors_from_frame(self) -> None:
        ...
    def remove_normals_from_frame(self) -> None:
        """
        Detach the normals annotator from the camera.
        """
    def remove_occlusion_from_frame(self) -> None:
        """
        Detach the occlusion annotator from the camera.
        """
    def remove_pointcloud_from_frame(self) -> None:
        """
        Detach the pointcloud annotator from the camera.
        """
    def remove_rgb_from_frame(self) -> None:
        """
        Detach the rgb annotator from the camera.
        """
    def remove_semantic_segmentation_from_frame(self) -> None:
        """
        Detach the semantic_segmentation annotator from the camera.
        """
    def resume(self) -> None:
        """
        resumes data collection and updating the data frame
        """
    def set_clipping_range(self, near_distance: float | None = None, far_distance: float | None = None) -> None:
        """
        Sets near and far clipping distances of camera prim.
        
                Args:
                    near_distance (Optional[float], optional): Value to be used for near clipping (in stage units). Defaults to None.
                    far_distance (Optional[float], optional): Value to be used for far clipping (in stage units). Defaults to None.
                
        """
    def set_dt(self, value: float) -> None:
        """
        
                Args:
                    value (float):  sets the dt to acquire new data frames
        
                
        """
    def set_fisheye_polynomial_properties(self, nominal_width: float | None, nominal_height: float | None, optical_centre_x: float | None, optical_centre_y: float | None, max_fov: float | None, polynomial: typing.Sequence[float] | None) -> None:
        """
        [DEPRECATED] Sets distortion parameters for the fisheyePolynomial projection model.
        
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
        Sets focal length of camera prim, in stage units. Longer focal length corresponds to narrower FOV, shorter focal length corresponds to wider FOV.
        
                Args:
                    value (float): Desired focal length of camera prim, in stage units.
                
        """
    def set_focus_distance(self, value: float):
        """
        Sets distance from the camera to the focus plane (in stage units).
        
                Args:
                    value (float): Sets value of camera prim focusDistance attribute (in stage units).
                
        """
    def set_frequency(self, value: int) -> None:
        """
        
                Args:
                    value (int): sets the frequency to acquire new data frames
                
        """
    def set_ftheta_properties(self, nominal_height: float | None = None, nominal_width: float | None = None, optical_center: tuple[float, float] | None = None, max_fov: float | None = None, distortion_coefficients: typing.Sequence[float] | None = None) -> None:
        """
        Applies F-theta lens distortion model to camera prim, then sets distortion parameters.
        
                Args:
                    nominal_height (Optional[float]): Height of the calibrated sensor in pixels
                    nominal_width (Optional[float]): Width of the calibrated sensor in pixels
                    optical_center (Optional[Tuple[float, float]]): Optical center (x, y) in pixels
                    max_fov (Optional[float]): Maximum field of view in degrees
                    distortion_coefficients (Optional[Sequence[float]]): Distortion coefficients in order:
                        [k0, k1, k2, k3, k4] - radial distortion coefficients
                        Missing coefficients default to 0.0
                
        """
    def set_horizontal_aperture(self, value: float, maintain_square_pixels: bool = True) -> None:
        """
        Set horizontal aperture (sensor width) in stage units and update vertical for square pixels.
        
                Only square pixels are supported; vertical aperture is updated to match aspect ratio.
        
                Args:
                    value (float): Horizontal aperture in stage units.
                    maintain_square_pixels (bool): If True, keep apertures in sync for square pixels.
                
        """
    def set_kannala_brandt_k3_properties(self, nominal_height: float | None = None, nominal_width: float | None = None, optical_center: tuple[float, float] | None = None, max_fov: float | None = None, distortion_coefficients: typing.Sequence[float] | None = None) -> None:
        """
        Applies Kannala-Brandt K3 lens distortion model to camera prim, then sets distortion parameters.
        
                Args:
                    nominal_height (Optional[float]): Height of the calibrated sensor in pixels
                    nominal_width (Optional[float]): Width of the calibrated sensor in pixels
                    optical_center (Optional[Tuple[float, float]]): Optical center (x, y) in pixels
                    max_fov (Optional[float]): Maximum field of view in degrees
                    distortion_coefficients (Optional[Sequence[float]]): Distortion coefficients in order:
                        [k0, k1, k2, k3] - radial distortion coefficients
                        Missing coefficients default to 0.0
                
        """
    def set_kannala_brandt_properties(self, nominal_width: float, nominal_height: float, optical_centre_x: float, optical_centre_y: float, max_fov: float | None, distortion_model: typing.Sequence[float]) -> None:
        """
        [DEPRECATED] Approximates kannala brandt distortion with ftheta fisheye polynomial coefficients.
                Note: This method was designed to approximate the OpenCV fisheye distortion model using ftheta fisheye polynomial parameterization.
                The OpenCV fisheye distortion model is now directly supported, so this method will use that model directly.
        
                Args:
                    nominal_width (float): Rendered Width (pixels)
                    nominal_height (float): Rendered Height (pixels)
                    optical_centre_x (float): Horizontal Render Position (pixels)
                    optical_centre_y (float): Vertical Render Position (pixels)
                    max_fov (Optional[float]): DEPRECATED. maximum field of view (pixels)
                    distortion_model (Sequence[float]): kannala brandt generic distortion model coefficients (k1, k2, k3, k4)
                
        """
    def set_lens_aperture(self, value: float):
        """
        Sets value of camera prim fStop attribute, which controls distance blurring. Lower numbers decrease focus range, larger
                    numbers increase it.
        
                Args:
                    value (float): Sets value of camera prim fStop attribute. 0 turns off focusing.
                
        """
    def set_lens_distortion_model(self, value: str) -> None:
        """
        
                Sets the `omni:lensdistortion:model` property of the camera prim and applies the corresponding schema.
                Note: `cameraProjectionType` has been deprecated in favor of `omni:lensdistortion:model`. `fisheyeOrthographic`, `fisheyeEquidistant`, `fisheyeEquisolid`, and `fisheyeSpherical` are no longer supported.
        
                Args:
                    value (str): Name of the distortion schema to apply, or "pinhole" to remove any distortion schemas and unset `omni:lensdistortion:model`.
                
        """
    def set_local_pose(self, translation: typing.Sequence[float] | None = None, orientation: typing.Sequence[float] | None = None, camera_axes: str = 'world') -> None:
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
    def set_lut_properties(self, nominal_height: float | None = None, nominal_width: float | None = None, optical_center: tuple[float, float] | None = None, ray_enter_direction_texture: str | None = None, ray_exit_position_texture: str | None = None) -> None:
        """
        Applies LUT lens distortion model to camera prim, then sets distortion parameters.
        
                Args:
                    nominal_height (Optional[float]): Height of the calibrated sensor in pixels
                    nominal_width (Optional[float]): Width of the calibrated sensor in pixels
                    optical_center (Optional[Tuple[float, float]]): Optical center (x, y) in pixels
                    ray_enter_direction_texture (Optional[str]): Path to ray enter direction texture
                    ray_exit_position_texture (Optional[str]): Path to ray exit position texture
                
        """
    def set_matching_fisheye_polynomial_properties(self, nominal_width: float, nominal_height: float, optical_centre_x: float, optical_centre_y: float, max_fov: float | None, distortion_model: typing.Sequence[float], distortion_fn: typing.Callable) -> None:
        """
        [DEPRECATED] Approximates provided OpenCV fisheye distortion with ftheta fisheye polynomial coefficients.
        
                Args:
                    nominal_width (float): Rendered Width (pixels)
                    nominal_height (float): Rendered Height (pixels)
                    optical_centre_x (float): Horizontal Render Position (pixels)
                    optical_centre_y (float): Vertical Render Position (pixels)
                    max_fov (Optional[float]): maximum field of view (pixels)
                    distortion_model (Sequence[float]): distortion model coefficients
                    distortion_fn (Callable): distortion function that takes points and returns distorted points
                
        """
    def set_opencv_fisheye_properties(self, cx: float | None = None, cy: float | None = None, fx: float | None = None, fy: float | None = None, fisheye: list[float] | None = None) -> None:
        """
        
                Applies OpenCV fisheye distortion model to camera prim, then sets distortion parameters.
        
                Args:
                    cx (float): Horizontal Render Position (pixels)
                    cy (float): Vertical Render Position (pixels)
                    fx (float): Horizontal Focal Length (pixels)
                    fy (float): Vertical Focal Length (pixels)
                    fisheye (List[float]): OpenCV fisheye parameters [k1, k2, k3, k4]
                
        """
    def set_opencv_pinhole_properties(self, cx: float | None = None, cy: float | None = None, fx: float | None = None, fy: float | None = None, pinhole: list[float] | None = None) -> None:
        """
        
                Applies OpenCV pinhole distortion model to camera prim, then sets distortion parameters.
        
                Args:
                    cx (float): Horizontal Render Position (pixels)
                    cy (float): Vertical Render Position (pixels)
                    fx (float): Horizontal Focal Length (pixels)
                    fy (float): Vertical Focal Length (pixels)
                    pinhole (List[float]): OpenCV pinhole parameters [k1, k2, p1, p2, k3, k4, k5, k6, s1, s2, s3, s4]
                
        """
    def set_projection_mode(self, value: str) -> None:
        """
        Sets projection model of the camera prim to perspective or orthographic.
        
                Args:
                    value (str): "perspective" or "orthographic".
        
                
        """
    def set_projection_type(self, value: str) -> None:
        """
        
                [DEPRECATED] Sets the `cameraProjectionType` property of the camera prim.
        
                Args:
                    value (str): Name of the projection type to apply, or "pinhole" to remove any distortion schemas and unset `omni:lensdistortion:model`.
                
        """
    def set_rad_tan_thin_prism_properties(self, nominal_height: float | None = None, nominal_width: float | None = None, optical_center: tuple[float, float] | None = None, max_fov: float | None = None, distortion_coefficients: typing.Sequence[float] | None = None) -> None:
        """
        Applies Radial-Tangential Thin Prism lens distortion model to camera prim, then sets distortion parameters.
        
                Args:
                    nominal_height (Optional[float]): Height of the calibrated sensor
                    nominal_width (Optional[float]): Width of the calibrated sensor
                    optical_center (Optional[Tuple[float, float]]): Optical center (x, y)
                    max_fov (Optional[float]): Maximum field of view in degrees
                    distortion_coefficients (Optional[Sequence[float]]): Distortion coefficients in order:
                        [k0, k1, k2, k3, k4, k5] - radial distortion coefficients
                        [p0, p1] - tangential distortion coefficients
                        [s0, s1, s2, s3] - thin prism distortion coefficients
                        Missing coefficients default to 0.0
                
        """
    def set_rational_polynomial_properties(self, nominal_width: float, nominal_height: float, optical_centre_x: float, optical_centre_y: float, max_fov: float | None, distortion_model: typing.Sequence[float]) -> None:
        """
        [DEPRECATED] Approximates rational polynomial distortion with ftheta fisheye polynomial coefficients.
                Note: This method was designed to approximate the OpenCV pinhole distortion model using ftheta fisheye polynomial parameterization.
                The OpenCV pinhole distortion model is now directly supported, so this method will use that model directly.
        
                Args:
                    nominal_width (float): Rendered Width (pixels)
                    nominal_height (float): Rendered Height (pixels)
                    optical_centre_x (float): Horizontal Render Position (pixels)
                    optical_centre_y (float): Vertical Render Position (pixels)
                    max_fov (Optional[float]): DEPRECATED. maximum field of view (pixels)
                    distortion_model (Sequence[float]): rational polynomial distortion model coefficients (k1, k2, p1, p2, k3, k4, k5, k6, s1, s2, s3, s4)
                
        """
    def set_resolution(self, value: tuple[int, int], maintain_square_pixels: bool = True) -> None:
        """
        Set the resolution of the camera sensor. This will check and update the apertures to maintain square pixels.
        
                Args:
                    value (Tuple[int, int]): width and height respectively.
                    maintain_square_pixels (bool): If True, keep apertures in sync for square pixels.
                
        """
    def set_shutter_properties(self, delay_open: float | None = None, delay_close: float | None = None) -> None:
        """
        
                Args:
                    delay_open (Optional[float], optional): Used with Motion Blur to control blur amount, increased values delay shutter opening. Defaults to None.
                    delay_close (Optional[float], optional): Used with Motion Blur to control blur amount, increased values forward the shutter close. Defaults to None.
                
        """
    def set_stereo_role(self, value: str) -> None:
        """
        
                Sets stereo role of the camera prim to mono, left or right.
        
                Args:
                    value (str): "mono", "left" or "right".
                
        """
    def set_vertical_aperture(self, value: float, maintain_square_pixels: bool = True) -> None:
        """
        Set vertical aperture (sensor height) in stage units and update horizontal for square pixels.
        
                Only square pixels are supported; horizontal aperture is updated to match aspect ratio.
        
                Args:
                    value (float): Vertical aperture in stage units.
                    maintain_square_pixels (bool): If True, keep apertures in sync for square pixels.
                
        """
    def set_world_pose(self, position: typing.Sequence[float] | None = None, orientation: typing.Sequence[float] | None = None, camera_axes: str = 'world') -> None:
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
    def supported_annotators(self) -> list[str]:
        """
        
                Returns:
                    List[str]: annotators supported by the camera
                
        """
def distort_point_kannala_brandt(camera_matrix, distortion_model, x, y):
    """
    [DEPRECATED] This helper function distorts point(s) using Kannala Brandt fisheye model.
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
    [DEPRECATED] This helper function distorts point(s) using rational polynomial model.
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
FTHETA_ATTRIBUTE_MAP: list = ['k0', 'k1', 'k2', 'k3', 'k4']
KANNALA_BRANDT_K3_ATTRIBUTE_MAP: list = ['k0', 'k1', 'k2', 'k3']
OPENCV_FISHEYE_ATTRIBUTE_MAP: list = ['k1', 'k2', 'k3', 'k4']
OPENCV_PINHOLE_ATTRIBUTE_MAP: list = ['k1', 'k2', 'p1', 'p2', 'k3', 'k4', 'k5', 'k6', 's1', 's2', 's3', 's4']
RAD_TAN_THIN_PRISM_ATTRIBUTE_MAP: list = ['k0', 'k1', 'k2', 'k3', 'k4', 'k5', 'p0', 'p1', 's0', 's1', 's2', 's3']
R_U_TRANSFORM: numpy.ndarray  # value = array([[ 1,  0,  0,  0],...
USD_CAMERA_TENTHS_TO_STAGE_UNIT: float = 10.0
U_R_TRANSFORM: numpy.ndarray  # value = array([[ 1,  0,  0,  0],...
U_W_TRANSFORM: numpy.ndarray  # value = array([[ 0, -1,  0,  0],...
W_U_TRANSFORM: numpy.ndarray  # value = array([[ 0,  0, -1,  0],...
