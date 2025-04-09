from PIL import Image
from PIL import ImageDraw
from __future__ import annotations
import carb as carb
import numpy as np
from omni.replicator.core.scripts.annotators import AnnotatorRegistry
from omni.replicator.core.scripts.backends.dispatcher import BackendDispatch
import omni.replicator.core.scripts.writers
from omni.replicator.core.scripts.writers import Writer
import typing
__all__ = ['AnnotatorRegistry', 'BackendDispatch', 'DataVisualizationWriter', 'Image', 'ImageDraw', 'Writer', 'carb', 'np']
class DataVisualizationWriter(omni.replicator.core.scripts.writers.Writer):
    """
    Data Visualization Writer
    
        This writer can be used to visualize various annotator data.
    
        Supported annotators:
        - bounding_box_2d_tight
        - bounding_box_2d_loose
        - bounding_box_3d
    
        Supported backgrounds:
        - rgb
        - normals
    
        Args:
            output_dir (str):
                Output directory for the data visualization files forwarded to the backend writer.
            bounding_box_2d_tight (bool, optional):
                If True, 2D tight bounding boxes will be drawn on the selected background (transparent by default).
                Defaults to False.
            bounding_box_2d_tight_params (dict, optional):
                Parameters for the 2D tight bounding box annotator. Defaults to None.
            bounding_box_2d_loose (bool, optional):
                If True, 2D loose bounding boxes will be drawn on the selected background (transparent by default).
                Defaults to False.
            bounding_box_2d_loose_params (dict, optional):
                Parameters for the 2D loose bounding box annotator. Defaults to None.
            bounding_box_3d (bool, optional):
                If True, 3D bounding boxes will be drawn on the selected background (transparent by default). Defaults to False.
            bounding_box_3d_params (dict, optional):
                Parameters for the 3D bounding box annotator. Defaults to None.
            frame_padding (int, optional):
                Number of digits used for the frame number in the file name. Defaults to 4.
    
        
    """
    BB_2D_LOOSE: typing.ClassVar[str] = 'bounding_box_2d_loose_fast'
    BB_2D_TIGHT: typing.ClassVar[str] = 'bounding_box_2d_tight_fast'
    BB_3D: typing.ClassVar[str] = 'bounding_box_3d_fast'
    SUPPORTED_BACKGROUNDS: typing.ClassVar[list] = ['rgb', 'normals']
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, output_dir: str, bounding_box_2d_tight: bool = False, bounding_box_2d_tight_params: dict = None, bounding_box_2d_loose: bool = False, bounding_box_2d_loose_params: dict = None, bounding_box_3d: bool = False, bounding_box_3d_params: dict = None, frame_padding: int = 4):
        ...
    def _draw_2d_bounding_boxes(self, draw: PIL.ImageDraw, annot_data: dict, write_params: dict):
        ...
    def _draw_3d_bounding_boxes(self, draw: PIL.ImageDraw, annot_data: dict, camera_params: dict, write_params: dict):
        ...
    def _get_background_image(self, annotators_data: dict, background_type: str, resolution: tuple) -> PIL.Image:
        ...
    def _is_valid_background(self, background: str) -> bool:
        ...
    def detach(self):
        ...
    def write(self, data: dict):
        ...
__version__: str = '0.1.0'
