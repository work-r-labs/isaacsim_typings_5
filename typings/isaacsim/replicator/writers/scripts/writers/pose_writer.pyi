from PIL import Image
from PIL import ImageDraw
from __future__ import annotations
from functools import partial
from isaacsim.replicator.writers.scripts.utils import calculate_truncation_ratio_simple
import numpy as np
from omni.replicator.core.scripts.annotators import AnnotatorRegistry
from omni.replicator.core.scripts.backends.dispatcher import BackendDispatch
from omni.replicator.core.scripts.functional.io_functions import write_image
from omni.replicator.core.scripts.functional.io_functions import write_json
import omni.replicator.core.scripts.writers
from omni.replicator.core.scripts.writers import Writer
from pxr import Gf
import typing
__all__ = ['AnnotatorRegistry', 'BackendDispatch', 'Gf', 'Image', 'ImageDraw', 'PoseWriter', 'Writer', 'calculate_truncation_ratio_simple', 'np', 'partial', 'write_image', 'write_json']
class PoseWriter(omni.replicator.core.scripts.writers.Writer):
    """
    Pose Writer
    
        Args:
            output_dir:
                Output directory string that indicates the directory to save the results.
            use_subfolders:
                If True, the writer will create subfolders for each render product, otherwise all data is saved in the same folder.
            visibility_threshold:
                Objects with visibility below this threshold will be skipped.  Default: ``0.0`` (fully occluded)
            skip_empty_frames:
                If True, the writer will skip frames that do not have visible objects.
            write_debug_images:
                If True, the writer will include rgb images overlaid with the projected 3d bounding boxes.
            frame_padding:
                Pad the frame number with leading zeroes.  Default: ``4``
            format:
                Specifies which format the data will be outputted as. Default: ``None`` (will write most of the available data)
        
    """
    BB3D_ANNOT_NAME: typing.ClassVar[str] = 'bounding_box_3d_fast'
    CAM_PARAMS_ANNOT_NAME: typing.ClassVar[str] = 'camera_params'
    CUBOID_EDGE_COLORS: typing.ClassVar[dict] = {'front': 'red', 'back': 'blue', 'connecting': 'green'}
    CUBOID_KEYPOINTS_ORDER_DEFAULT: typing.ClassVar[list] = ['Center', 'LDB', 'LDF', 'LUB', 'LUF', 'RDB', 'RDF', 'RUB', 'RUF']
    CUBOID_KEYPOINT_COLORS: typing.ClassVar[list] = ['white', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'orange', 'purple']
    CUBOID_KEYPOINT_ORDER_DOPE: typing.ClassVar[list] = ['LUF', 'RUF', 'RDF', 'LDF', 'LUB', 'RUB', 'RDB', 'LDB', 'Center']
    RGB_ANNOT_NAME: typing.ClassVar[str] = 'rgb'
    SUPPORTED_FORMATS: typing.ClassVar[set] = {'centerpose', 'dope'}
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, output_dir: str, use_subfolders: bool = False, visibility_threshold: float = 0.0, skip_empty_frames: bool = True, write_debug_images: bool = False, frame_padding: int = 6, format: str = None, use_s3: bool = False, s3_bucket: str = None, s3_endpoint_url: str = None, s3_region: str = None):
        ...
    def _draw_local_frame_axes(self, draw, local_to_world_transform, camera_view_matrix, camera_projection_matrix, screen_size, size_local = [1, 1, 1], origin_local = [0, 0, 0], axes_length_perc = 0.25):
        ...
    def _draw_projected_keypoints(self, draw, keypoints, point_size = 4, edge_size = 2):
        ...
    def _draw_world_frame_axes_bottom_left(self, draw, camera_view_matrix, camera_projection_matrix, screen_size, axes_scale = 0.03, margin_percentage = 0.03):
        ...
    def _process_bounding_boxes(self, bounding_box_3d_data: dict, camera_params: dict) -> list:
        ...
    def _process_camera_parameters(self, camera_params) -> dict:
        ...
    def _process_frame_data(self, bounding_box_3d_data: dict, camera_params_data: dict) -> int:
        ...
    def _project_camera_point_to_screen(self, camera_point, projection_matrix, screen_size):
        ...
    def _project_world_point_to_screen(self, world_point, view_matrix, projection_matrix, screen_size):
        ...
    def _world_point_to_camera_point(self, world_point, view_matrix):
        ...
    def _write_debug_data(self, rgb_data: dict, render_product_subfolder: str = ''):
        ...
    def _write_frame_data(self, rgb_data: dict, render_product_subfolder: str = ''):
        ...
    def detach(self):
        ...
    def get_current_frame_id(self):
        ...
    def write(self, data: dict):
        ...
__version__: str = '0.1.0'
