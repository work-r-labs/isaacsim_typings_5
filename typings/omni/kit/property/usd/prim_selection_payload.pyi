from __future__ import annotations
from pxr import Sdf
from pxr import Usd
import weakref as weakref
__all__: list = ['PrimSelectionPayload']
class PrimSelectionPayload:
    """
    A class to encapsulate the selection payload for a USD stage's prim paths.
    
        This class holds a weak reference to a USD stage and a list of SDF paths representing selected prims. It provides methods to interact with the selection data, including checking the length, iteration, indexing, and determining if the selection exceeds a predefined large selection count.
    
        Args:
            stage (weakref.ReferenceType(:obj:`Usd.Stage`)): A weak reference to the stage from which prims are selected.
            paths (List[:obj:`Sdf.Path`]): A list of SDF paths to selected prims.
        
    """
    def __bool__(self):
        ...
    def __delitem__(self, key):
        ...
    def __getitem__(self, key):
        ...
    def __init__(self, stage: <weakref at 0x709fc815aca0; to 'Boost.Python.class' at 0x41972620 (Stage)>, paths: typing.List[pxr.Sdf.Path]):
        """
        Initializes a new instance of the PrimSelectionPayload.
        """
    def __iter__(self):
        ...
    def __len__(self):
        ...
    def __setitem__(self, key, value):
        ...
    def cleanup_payload(self):
        """
        Removes any deleted prims from payload list and returns valid payload
        """
    def get_large_selection_count(self):
        """
        Gets the count of items considered as a large selection.
        
                Returns:
                    int: The count used to determine large selections.
        """
    def get_paths(self) -> typing.List[pxr.Sdf.Path]:
        """
        Gets the list of paths stored in the payload.
        
                Returns:
                    List[:obj:`Sdf.Path`]: The paths associated with this payload.
        """
    def get_stage(self):
        """
        Retrieves the stage associated with the payload.
        
                Returns:
                    :obj:`weakref.ReferenceType(Usd.Stage)`: The stage if available, otherwise None.
        """
    def is_large_selection(self) -> bool:
        """
        Determines if the current selection is considered large.
        
                Returns:
                    bool: True if the selection is large, otherwise False.
        """
    def set_large_selection_override(self, state: bool):
        """
        Sets the override state for large selection handling.
        
                Args:
                    state (bool): True to ignore large selection checks.
        """
