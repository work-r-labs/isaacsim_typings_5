import Semantics as Semantics
from __future__ import annotations
import carb as carb
from isaacsim.core.utils import prims as prim_utils
from isaacsim.core.utils.stage import get_current_stage
from isaacsim.core.utils.stage import get_current_stage_id
import omni as omni
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
from pxr import UsdSemantics
__all__: list[str] = ['Semantics', 'Usd', 'UsdGeom', 'UsdSemantics', 'add_labels', 'add_update_semantics', 'carb', 'check_incorrect_labels', 'check_incorrect_semantics', 'check_missing_labels', 'check_missing_semantics', 'count_labels_in_scene', 'count_semantics_in_scene', 'get_current_stage', 'get_current_stage_id', 'get_labels', 'get_semantics', 'omni', 'prim_utils', 'remove_all_semantics', 'remove_labels', 'upgrade_prim_semantics_to_labels']
def add_labels(prim: pxr.Usd.Prim, labels: list[str], instance_name: str = 'class', overwrite: bool = True) -> None:
    """
    Apply semantic labels to a prim using the UsdSemantics.LabelsAPI.
    
        Args:
            prim (Usd.Prim): Usd Prim to add or update labels on.
            labels (list): The list of labels to apply.
            instance_name (str, optional): The name of the semantic instance. Defaults to "class".
            overwrite (bool, optional): If True (default), existing labels for this instance are replaced.
                                       If False, the new labels are appended to existing ones (if any).
        
    """
def add_update_semantics(prim: pxr.Usd.Prim, semantic_label: str, type_label: str = 'class', suffix = '') -> None:
    """
    [DEPRECATED] Apply a semantic label to a prim or update an existing label using the old SemanticsAPI.
    
        Args:
            prim (Usd.Prim): Usd Prim to add or update semantics on
            semantic_label (str): The label we want to apply
            type_label (str): The type of semantic information we are specifying (default = "class")
            suffix (str): Additional suffix used to specify multiple semantic attribute names.
        
    """
def check_incorrect_labels(prim_path: str | None = None) -> list[list[str]]:
    """
    Returns a list of [prim_path, label] for meshes where at least one semantic label (LabelsAPI)
           is not found within the prim's path string (case-insensitive, ignoring '_' and '-').
    
        Args:
            prim_path (str | None): This will check Prim path and its childrens' labels. If None, checks the whole stage.
    
        Returns:
            list[list[str]]: List containing pairs of [prim_path, first_incorrect_label].
        
    """
def check_incorrect_semantics(prim_path: str = None) -> typing.List[typing.List[str]]:
    """
    [DEPRECATED] Returns a list of prim path of meshes with different semantics labels (old SemanticsAPI) than their prim path and their semantic labels
    
        Args:
            prim_path (str): This will check Prim path and its childrens' semantics
    
        Returns:
            List[List[str]]: List of prim path and semantic label
        
    """
def check_missing_labels(prim_path: str | None = None) -> list[str]:
    """
    Returns a list of prim paths of meshes with missing semantic labels (UsdSemantics.LabelsAPI).
    
        Args:
            prim_path (str | None): This will check Prim path and its childrens' labels. If None, checks the whole stage.
    
        Returns:
            list[str]: Prim paths of meshes with no LabelsAPI applied.
        
    """
def check_missing_semantics(prim_path: str = None) -> typing.List[str]:
    """
    [DEPRECATED] Returns a list of prim path of meshes with missing semantics (old SemanticsAPI)
    
        Args:
            prim_path (str): This will check Prim path and its childrens' semantics
    
        Returns:
            List[str]: Prim paths
        
    """
def count_labels_in_scene(prim_path: str | None = None) -> dict[str, int]:
    """
    Returns a dictionary of semantic labels (UsdSemantics.LabelsAPI) and their corresponding count.
    
        Args:
            prim_path (str | None): This will check Prim path and its childrens' labels. If None, checks the whole stage.
    
        Returns:
            dict[str, int]: Dictionary mapping individual labels to their total count across all instances.
                           Includes a 'missing_labels' count for meshes with no LabelsAPI.
        
    """
def count_semantics_in_scene(prim_path: str = None) -> typing.Dict[str, int]:
    """
    [DEPRECATED] Returns a dictionary of labels (old SemanticsAPI) and the corresponding count
    
        Args:
            prim_path (str): This will check Prim path and its childrens' semantics
    
        Returns:
            Dict[str, int]: labels and count
        
    """
def get_labels(prim: pxr.Usd.Prim) -> dict[str, list[str]]:
    """
    Returns semantic labels (UsdSemantics.LabelsAPI) applied to a prim.
    
        Args:
            prim (Usd.Prim): Prim to return labels for.
    
        Returns:
            dict[str, list[str]]: Dictionary mapping instance names to a list of labels.
                                  Returns an empty dict if no LabelsAPI instances are found.
        
    """
def get_semantics(prim: pxr.Usd.Prim) -> typing.Dict[str, typing.Tuple[str, str]]:
    """
    [DEPRECATED] Returns semantics (old SemanticsAPI) that are applied to a prim
    
        Args:
            prim (Usd.Prim): Prim to return semantics for
    
        Returns:
            Dict[str, Tuple[str,str]]: Dictionary containing the name of the applied semantic, and the type and data associated with that semantic.
        
    """
def remove_all_semantics(prim: pxr.Usd.Prim, recursive: bool = False) -> None:
    """
    [DEPRECATED] Removes all semantic tags (old SemanticsAPI) from a given prim and its children
    
        Args:
            prim (Usd.Prim): Prim to remove any applied semantic APIs on
            recursive (bool, optional): Also traverse children and remove semantics recursively. Defaults to False.
        
    """
def remove_labels(prim: pxr.Usd.Prim, instance_name: str | None = None, include_descendants: bool = False) -> None:
    """
    Removes semantic labels (UsdSemantics.LabelsAPI) from a prim.
    
        Args:
            prim (Usd.Prim): Prim to remove labels from.
            instance_name (str | None, optional): Specific instance name to remove.
                                                  If None (default), removes *all* LabelsAPI instances.
            include_descendants (bool, optional): Also traverse children and remove labels recursively. Defaults to False.
        
    """
def upgrade_prim_semantics_to_labels(prim: pxr.Usd.Prim, include_descendants: bool = False) -> int:
    """
    Upgrades a prim and optionally its descendants from the deprecated SemanticsAPI
        to the new UsdSemantics.LabelsAPI.
    
        Converts each found SemanticsAPI instance on the processed prim(s) to a corresponding
        LabelsAPI instance. The old 'semanticType' becomes the new LabelsAPI
        'instance_name', and the old 'semanticData' becomes the single label in the
        new 'labels' list. The old SemanticsAPI is always removed after upgrading.
    
        Args:
            prim (Usd.Prim): The starting prim to upgrade.
            include_descendants (bool, optional): If True, upgrades the prim and all its descendants.
                                         If False (default), upgrades only the specified prim.
    
        Returns:
            int: The total number of SemanticsAPI instances successfully upgraded to LabelsAPI.
        
    """
