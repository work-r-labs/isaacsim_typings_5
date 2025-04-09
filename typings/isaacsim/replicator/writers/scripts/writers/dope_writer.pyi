from __future__ import annotations
import io as io
from isaacsim.replicator.writers.scripts.utils import NumpyEncoder
import json as json
import numpy as np
from omni.replicator.core.scripts.annotators import AnnotatorRegistry
from omni.replicator.core.scripts.backends.dispatcher import BackendDispatch
import omni.replicator.core.scripts.writers
from omni.replicator.core.scripts.writers import Writer
from omni.replicator.core.scripts.writers import WriterRegistry
from omni.syntheticdata.scripts.SyntheticData import SyntheticData
from omni.syntheticdata.scripts.SyntheticData.SyntheticData import NodeConnectionTemplate
from omni.syntheticdata.scripts.SyntheticData.SyntheticData import NodeTemplate
import typing
__all__ = ['AnnotatorRegistry', 'BackendDispatch', 'DOPEWriter', 'NodeConnectionTemplate', 'NodeTemplate', 'NumpyEncoder', 'SyntheticData', 'Writer', 'WriterRegistry', 'io', 'json', 'np']
class DOPEWriter(omni.replicator.core.scripts.writers.Writer):
    """
    Basic writer capable of writing built-in annotator groundtruth.
    
        Attributes:
            output_dir:
                Output directory string that indicates the directory to save the results. If use_s3 == True, this will be the bucket name.
            semantic_types:
                List of semantic types to consider when filtering annotator data. Default: ["class"]
            image_output_format:
                String that indicates the format of saved RGB images. Default: "png"
            use_s3:
                Boolean value that indicates whether output will be written to s3 bucket. Default: False
    
        Example:
            >>> import omni.replicator.core as rep
            >>> camera = rep.create.camera()
            >>> render_product = rep.create.render_product(camera, (512, 512))
            >>> writer = rep.WriterRegistry.get("DOPEWriter")
            >>> import carb
            >>> tmp_dir = carb.tokens.get_tokens_interface().resolve("${temp}/rgb")
            >>> writer.initialize(output_dir=tmp_dir, class_name_to_index_map=class_name_to_index_map)
            >>> writer.attach([render_product])
            >>> rep.orchestrator.run()
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def register_pose_annotator(config_data: dict):
        ...
    @staticmethod
    def setup_writer(config_data: dict, writer_config: dict):
        """
        Initialize writer and attach render product
                Args:
                    config_data: A dictionary containing the general configurations for the script.
                    writer_config: A dictionary containing writer-specific configurations.
                
        """
    def __init__(self, output_dir: str, class_name_to_index_map: typing.Dict, semantic_types: typing.List[str] = None, image_output_format: str = 'png', use_s3: bool = False, bucket_name: str = '', endpoint_url: str = '', s3_region: str = 'us-east-1'):
        ...
    def _check_frame_validity(self, data: dict) -> bool:
        """
        Check and flag frame as valid if training data is present in the frame.
        
                Args:
                    data (dict): The frame data to check.
        
                Returns:
                    bool: True if frame is valid, False otherwise.
                
        """
    def _write_dope(self, data: dict, render_product_path: str, annotator: str):
        ...
    def _write_rgb(self, data: dict, render_product_path: str, annotator: str):
        ...
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
