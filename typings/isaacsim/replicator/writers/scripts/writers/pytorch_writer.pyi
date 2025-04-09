from __future__ import annotations
import carb as carb
import isaacsim.replicator.writers.scripts.writers.pytorch_listener
from isaacsim.replicator.writers.scripts.writers.pytorch_listener import PytorchListener
from omni.replicator.core.scripts.annotators import AnnotatorRegistry
from omni.replicator.core.scripts.backends.dispatcher import BackendDispatch
import omni.replicator.core.scripts.writers
from omni.replicator.core.scripts.writers import Writer
import torch as torch
import typing
import warp as wp
__all__ = ['AnnotatorRegistry', 'BackendDispatch', 'PytorchListener', 'PytorchWriter', 'Writer', 'carb', 'torch', 'wp']
class PytorchWriter(omni.replicator.core.scripts.writers.Writer):
    """
    A custom writer that uses omni.replicator API to retrieve RGB data via render products
            and formats them as tensor batches. The writer takes a PytorchListener which is able
            to retrieve pytorch tensors for the user directly after each writer call.
    
        Args:
            listener (PytorchListener): A PytorchListener that is sent pytorch batch tensors at each write() call.
            output_dir (str): directory in which rgb data will be saved in PNG format by the backend dispatch.
                              If not specified, the writer will not write rgb data as png and only ping the
                              listener with batched tensors.
            device (str): device in which the pytorch tensor data will reside. Can be "cpu", "cuda", or any
                          other format that pytorch supports for devices. Default is "cuda".
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def _convert_to_pytorch(*args, **kwds) -> torch.Tensor:
        ...
    @staticmethod
    def _write_rgb(*args, **kwds) -> None:
        ...
    def __init__(self, listener: isaacsim.replicator.writers.scripts.writers.pytorch_listener.PytorchListener, output_dir: str = None, tiled_sensor: bool = False, device: str = 'cuda'):
        ...
    def write(self, data: dict) -> None:
        """
        Sends data captured by the attached render products to the PytorchListener and will write data to
                the output directory if specified during initialization.
        
                Args:
                    data (dict): Data to be pinged to the listener and written to the output directory if specified.
                
        """
__version__: str = '0.0.1'
