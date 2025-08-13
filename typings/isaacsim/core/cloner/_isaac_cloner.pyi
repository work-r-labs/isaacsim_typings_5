from __future__ import annotations
__all__: list[str] = list()
def _fabric_clone(arg0: int, arg1: str, arg2: list[str]) -> bool:
    """
            Creates clones of a source prim at specified target paths in the Fabric stage.
            
            This function performs a fabric clone operation, creating copies of a source prim at multiple
            target locations within the Fabric stage. Unlike regular cloning, these clones are created
            directly in the Fabric stage rather than the USD stage, which can be more efficient for
            certain use cases.
    
            Args:
                stage_id (int): The unique identifier of the USD stage where cloning will occur
                source_prim_path (str): The path to the source prim that will be cloned. This prim should be a valid USD prim.
                prim_paths (List[str]): List of target paths where clones will be created. These prims will be created in the Fabric stage, not in the USD stage.
    
            Returns:
                bool: True if cloning was successful, False otherwise.
    
            Warning:
                The source prim must exist at the specified path.
    """
