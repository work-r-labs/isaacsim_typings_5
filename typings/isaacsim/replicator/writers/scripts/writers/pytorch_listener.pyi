from __future__ import annotations
import torch as torch
__all__ = ['PytorchListener', 'torch']
class PytorchListener:
    """
    A Observer/Listener that keeps track of updated data sent by the writer. Is passed in the
        initialization of a PytorchWriter at which point it is pinged by the writer after any data is
        passed to the writer.
    """
    def __init__(self):
        ...
    def get_rgb_data(self) -> typing.Optional[torch.Tensor]:
        """
        Returns RGB data as a batched tensor from the current data stored.
        
                Returns:
                    images (Optional[torch.Tensor]): images in batched pytorch tensor form
                
        """
    def write_data(self, data: dict) -> None:
        """
        Updates the existing data in the listener with the new data provided.
        
                Args:
                    data (dict): new data retrieved from writer.
                
        """
