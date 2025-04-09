from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
__all__ = ['ByteCapture', 'Capture', 'FileCapture', 'MultiAOVByteCapture', 'MultiAOVFileCapture', 'RenderCapture', 'asyncio', 'carb', 'omni']
class ByteCapture(MultiAOVByteCapture):
    """
    Class to capture a single AOVs (defaulting to color) to a user callback
    """
    def __init__(self, callback_fn: typing.Callable = None, aov_name: str = '', **kwargs):
        ...
class Capture:
    """
    Base capture delegate
    """
    def __init__(self, *args, **kwargs):
        ...
    def _set_completed(self, value: typing.Any = True):
        ...
    def capture(self, aov_map, frame_info, hydra_texture, result_handle):
        ...
    def wait_for_result(self, completion_frames: int = 2):
        ...
class FileCapture(MultiAOVFileCapture):
    """
    Class to capture a single AOVs (defaulting to color) into one file
    """
    def __init__(self, file_path: str, aov_name: str = '', **kwargs):
        ...
class MultiAOVByteCapture(RenderCapture):
    """
    Class to deliver multiple AOVs buffer/bytes to a callback function
    """
    def __init__(self, aov_names: typing.Sequence[str], callback_fns: typing.Sequence[typing.Callable] = None, **kwargs):
        ...
    def capture_aov(self, callback_fn: typing.Callable, aov: dict):
        ...
    def on_capture_completed(self, buffer, buffer_size, width, height, byte_format):
        ...
class MultiAOVFileCapture(RenderCapture):
    """
    Class to capture multiple AOVs into multiple files
    """
    def __init__(self, aov_names: typing.Sequence[str], file_paths: typing.Sequence[str], format_desc: dict = None, **kwargs):
        ...
    def capture_aov(self, file_path: str, aov: dict, format_desc: dict = None):
        ...
    @property
    def format_desc(self):
        ...
    @format_desc.setter
    def format_desc(self, value: dict):
        ...
class RenderCapture(Capture):
    """
    Viewport capturing delegate that iterates over multiple aovs and calls user defined capture_aov method for all
        of interest
    """
    def __init__(self, aov_names: typing.Sequence[str], per_aov_data: typing.Sequence[typing.Any] = None, **kwargs):
        ...
    def capture(self, aov_map, frame_info, hydra_texture, result_handle):
        ...
    def capture_aov(self, user_data, aov: dict):
        ...
    def deliver_aov_buffer(self, callback_fn: typing.Callable, aov: dict):
        ...
    def save_aov_to_file(self, file_path: str, aov: dict, format_desc: dict = None):
        ...
    def save_product_to_file(self, file_path: str, render_product: str):
        ...
    @property
    def aov_data(self):
        ...
    @property
    def aov_names(self):
        ...
    @property
    def frame_info(self):
        ...
    @property
    def frame_number(self):
        ...
    @property
    def hydra_texture(self):
        ...
    @property
    def projection(self):
        ...
    @property
    def render_capture(self):
        ...
    @property
    def resolution(self):
        ...
    @property
    def result_handle(self):
        ...
    @property
    def view(self):
        ...
    @property
    def viewport_handle(self):
        ...
