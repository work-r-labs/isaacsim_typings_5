from __future__ import annotations
__all__ = ['find_root_prim_path_from_regex', 'find_unique_string_name']
def find_root_prim_path_from_regex(prim_path_regex: str) -> typing.Tuple[str, int]:
    """
    Find the first prim above the regex pattern prim and its position.
    
        Args:
            prim_path_regex (str): full prim path including the regex pattern prim.
    
        Returns:
            Tuple[str, int]: First position is the prim path to the parent of the regex prim.
                        Second position represents the level of the regex prim in the USD stage tree representation.
    
        
    """
def find_unique_string_name(initial_name: str, is_unique_fn: typing.Callable[[str], bool]) -> str:
    """
    Find a unique string name based on the predicate function provided.
    
        The string is appended with "_N", where N is a natural number till the resultant string
        is unique.
    
        Args:
            initial_name (str): The initial string name.
            is_unique_fn (Callable[[str], bool]): The predicate function to validate against.
    
        Returns:
            str: A unique string based on input function.
        
    """
