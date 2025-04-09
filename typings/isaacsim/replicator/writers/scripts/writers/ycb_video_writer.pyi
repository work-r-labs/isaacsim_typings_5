from PIL import Image
from __future__ import annotations
import io as io
from isaacsim.core.utils.mesh import get_mesh_vertices_relative_to
import numpy
import numpy as np
from omni.replicator.core.scripts.annotators import AnnotatorRegistry
from omni.replicator.core.scripts.backends.dispatcher import BackendDispatch
import omni.replicator.core.scripts.writers
from omni.replicator.core.scripts.writers import Writer
from omni.replicator.core.scripts.writers import WriterRegistry
from omni.syntheticdata.scripts.SyntheticData import SyntheticData
from omni.syntheticdata.scripts.SyntheticData.SyntheticData import NodeConnectionTemplate
from omni.syntheticdata.scripts.SyntheticData.SyntheticData import NodeTemplate
import os as os
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
import pxr.UsdGeom
from scipy.io.matlab._mio import savemat
import typing
__all__ = ['AnnotatorRegistry', 'BackendDispatch', 'Image', 'NodeConnectionTemplate', 'NodeTemplate', 'SyntheticData', 'Usd', 'UsdGeom', 'Writer', 'WriterRegistry', 'YCBVideoWriter', 'get_mesh_vertices_relative_to', 'io', 'np', 'os', 'savemat']
class YCBVideoWriter(omni.replicator.core.scripts.writers.Writer):
    """
    Writer capable of writing annotator groundtruth in the YCB Video Dataset format.
    
        Attributes:
            output_dir:
                Output directory string that indicates the directory to save the results.
            num_frames:
                Total number of frames to be generated.
            semantic_types:
                List of semantic types to consider when filtering annotator data. Default: ["class"]
            rgb:
                Boolean value that indicates whether the rgb annotator will be activated
                and the data will be written or not. Default: False.
            bounding_box_2d_tight:
                Boolean value that indicates whether the bounding_box_2d_tight annotator will be activated
                and the data will be written or not. Default: False.
            semantic_segmentation:
                Boolean value that indicates whether the semantic_segmentation annotator will be activated
                and the data will be written or not. Default: False.
            distance_to_image_plane:
                Boolean value that indicates whether the distance_to_image_plane annotator will be activated
                and the data will be written or not. Default: False.
            image_output_format:
                String that indicates the format of saved RGB images. Default: "png"
            pose:
                Boolean value that indicates whether the pose annotator will be activated
                and the data will be written or not. Default: False.
            class_name_to_index_map:
                Mapping between semantic label and index used in the YCB Video Dataset. This indices are used in the
                'cls_indexes' field of the generated meta.mat file, in addition to being used to color the semantic
                segmentation (where pixels are colored according to the grayscale class index).
            factor_depth:
                Depth scaling factor used in the YCB Video Dataset. Default: 10000.
            intrinsic_matrix:
                Camera intrinsic matrix. shape is (3, 3).
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def register_pose_annotator(config_data: dict):
        """
        Registers the annotators for the specific writer
                Args:
                    config_data: A dictionary containing the configuration data for the current writer.
                
        """
    @staticmethod
    def save_mesh_vertices(mesh_prim: pxr.UsdGeom.Mesh, coord_prim: pxr.Usd.Prim, model_name: str, output_folder: str):
        """
        Create points.xyz file representing vertices of the mesh_prim, defined in the frame of the coord_prim. The
                points.xyz file will be saved in the output_folder/data/models/model_name/ directory.
        
                Args:
                    mesh_prim (UsdGeom.Mesh): mesh prim to get the vertice points.
                    coord_prim (Usd.Prim): prim's coordinate used to define the vertices with respect to.
                    model_name (str): name of the part to get the vertices of. Note: This corresponds to the name used for
                                      the part in the YCB Video Dataset, and is unrelated to the name of the part in the scene.
                    output_folder (str): path of the base output directory.
                
        """
    @staticmethod
    def setup_writer(config_data: dict, writer_config: dict):
        """
        Initialize writer and attach render product
                Args:
                    config_data: A dictionary containing the general configurations for the script.
                    writer_config: A dictionary containing writer-specific configurations.
                
        """
    def __init__(self, output_dir: str, num_frames: int, semantic_types: typing.List[str] = None, rgb: bool = False, bounding_box_2d_tight: bool = False, semantic_segmentation: bool = False, distance_to_image_plane: bool = False, image_output_format: str = 'png', pose: bool = False, class_name_to_index_map: typing.Dict = None, factor_depth: int = 10000, intrinsic_matrix: numpy.ndarray = None):
        ...
    def _check_frame_validity(self, data: dict) -> bool:
        """
        Check and flag frame as valid if training data is present in the frame.
        
                Args:
                    data (dict): The frame data to check.
        
                Returns:
                    bool: True if frame is valid, False otherwise.
                
        """
    def _create_output_folders(self):
        """
        Creates an output directory structure (if necessary), similar to that used in the YCB Video Dataset. Note: A
                single video directory is used to hold all the generated synthetic data, rather than several directories
                (each representing a separate video file, as in the YCB Video Dataset).
                
        """
    def _create_train_text_file(self):
        """
        Creates a text file to specify the set of YCB Video Dataset samples to be used during training of a model.
                Lines include the video basename corresponding to the video that the sample is from, and the image ID of the
                sample. Training samples are written as if a single video is being used (see the note in
                create_output_folders()). Additionally, it is assumed data is generated only for model training (rather than
                for testing or validation).
                
        """
    def _write_bounding_box_data(self, data: dict, render_product_path: str, annotator: str):
        """
        Saves a text file describing bounding boxes of semantically-labeled objects in view for the YCB Video
                   Dataset. Note: Lines of the bounding box text file consist of a class name and the position of the bounding
                   box. The positions of the bounding boxes are represented by the upper-left coordinate, followed by the
                   bottom-right coordinate. Coordinates are expressed in pixels, where the origin of the image is the top-left
                   corner, with +x to the right and +y down.
        
                Args:
                    data (dict): A dictionary containing the annotator data for the current frame.
                    render_product_path (str): Directory name to save data to, corresponding to a specific render product.
                    annotator (str): Annotator name used as a key in the data dictionary, which can also be used to retrieve the
                                     annotator from the annotator registry.
                
        """
    def _write_distance_to_image_plane(self, data: dict, render_product_path: str, annotator: str):
        """
        Saves a depth image for the YCB Video Dataset. Note: Depth images are only for visualization and testing, and
                   would need to be adapted to conform to the exact format used in the YCB Video Dataset.
        
                Args:
                    data (dict): A dictionary containing the annotator data for the current frame.
                    render_product_path (str): Directory name to save data to, corresponding to a specific render product.
                    annotator (str): Annotator name used as a key in the data dictionary, which can also be used to retrieve the
                                     annotator from the annotator registry.
                
        """
    def _write_pose(self, data: dict, render_product_path: str, annotator: str):
        """
        Saves a metadata ".mat" file for the YCB Video Dataset, containing:
                   - Class indexes (from a pre-defined mapping) corresponding to each semantically-labeled object in view.
                   - A depth image scaling factor.
                   - The intrinsic matrix of the camera.
                   - Poses from the frame of each semantically-labeled object in view to the world frame, represented as a
                     rotation matrix and a translation.
                   - The center (in pixel coordinates) of each semantically-labeled object in view. Pixel coordinates are
                     expressed relative to the top-left corner of the image, with +x to the right and +y down.
        
                Args:
                    data (dict): A dictionary containing the annotator data for the current frame.
                    render_product_path (str): Directory name to save data to, corresponding to a specific render product.
                    annotator (str): Annotator name used as a key in the data dictionary, which can also be used to retrieve the
                                     annotator from the annotator registry.
                
        """
    def _write_rgb(self, data: dict, render_product_path: str, annotator: str):
        """
        Saves a RGB image for the YCB Video Dataset.
        
                Args:
                    data (dict): A dictionary containing the annotator data for the current frame.
                    render_product_path (str): Directory name to save data to, corresponding to a specific render product.
                    annotator (str): Annotator name used as a key in the data dictionary, which can also be used to retrieve the
                                     annotator from the annotator registry.
                
        """
    def _write_semantic_segmentation(self, data: dict, render_product_path: str, annotator: str):
        """
        Saves a segmentation label image file for the YCB Video Dataset. Segmentation label is saved as a grayscale
                   image.
        
                Args:
                    data (dict): A dictionary containing the annotator data for the current frame.
                    render_product_path (str): Directory name to save data to, corresponding to a specific render product.
                    annotator (str): Annotator name used as a key in the data dictionary, which can also be used to retrieve the
                                     annotator from the annotator registry.
                
        """
    def is_last_frame_valid(self) -> bool:
        """
        Checks if the last frame was valid (training data was present).
        
                Returns:
                    bool: True if the last frame was valid, False otherwise.
                
        """
    def write(self, data: dict):
        """
        Write function called from the OgnWriter node on every frame to process annotator output.
        
                Args:
                    data: A dictionary containing the annotator data for the current frame.
                
        """
__version__: str = '0.0.1'
