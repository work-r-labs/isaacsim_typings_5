from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni.kit.usd import layers
from pxr import Kind
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdLux
from pxr import UsdShade
__all__: list = ['ContextMenu']
class ContextMenu:
    """
    Class for mananging context menu and menu items for the Stage widget.
    """
    @staticmethod
    def add_create_menu(menu_dict):
        """
        
                Adds the menu to the end of the stage context create menu.
                Returns the MenuSubscription object that should be alive all the time. Once the returned object is destroyed,
                the added menu will be destroyed as well.
        
                Args:
                    menu_dict: A dictionary containing menu settings. See ContextMenuExtension docs for information on values.
        
                Returns:
                    MenuSubscription. Keep a copy of this as the custom menu will be removed when `release()` is explicitly
                        called or when this is garbage collected.
                
        """
    @staticmethod
    def add_menu(menu_dict):
        """
        
                Adds the menu to the end of the context menu.
                Returns the MenuSubscription object that should be alive all the time. Once the returned object is destroyed,
                the added menu will be destroyed as well.
        
                Args:
                    menu_dict: A dictionary containing menu settings. See ContextMenuExtension docs for information on values.
        
                Returns:
                    MenuSubscription. Keep a copy of this as the custom menu will be removed when `release()` is explicitly
                        called or when this is garbage collected.
                
        """
    @staticmethod
    def bind_material_to_prim_dialog(objects):
        """
        
                Displays the dialog where users can select materials and bind to selected prims.
                Will not show the dialog if no prims are selected.
        
                Args:
                    objects (Dict): The context object.
                
        """
    @staticmethod
    def bind_material_to_selected_prims(objects):
        """
        
                Binds the hovered material prim to selected prims.
                If either the hovered prim or the prim list is empty, no operation will be done.
        
                Args:
                    objects (Dict): The context object.
                
        """
    @staticmethod
    def clear_default_prim(objects):
        """
        
                Clears the default prim of the stage.
        
                Args:
                    objects (Dict): The context object.
                
        """
    @staticmethod
    def collapse_all(objects):
        """
        
                Collapses all hovered or selected prims.
        
                Args:
                    objects (Dict): The context object.
                
        """
    @staticmethod
    def collapse_to(objects, kind):
        """
        
                Collapses the hovered or selected prims recursively if the kind matches the given Kind.
        
                Args:
                    objects (Dict): The context object.
                    kind (str): The USD Kind to collapse.
                
        """
    @staticmethod
    def expand_all(objects):
        """
        
                Expands all hovered or selected prims.
        
                Args:
                    objects (Dict): The context object.
                
        """
    @staticmethod
    def expand_to(objects, kind):
        """
        
                Expands the hovered or selected prims recursively if the kind matches the given Kind.
        
                Args:
                    objects (Dict): The context object.
                    kind (str): The USD Kind to collapse.
                
        """
    @staticmethod
    def has_default_prim(objects):
        """
        
                Checks if the selected prim is the default prim of the stage.
                If the prim selection is not a single prim (eg. empty selection or multiple selected), returns False. If the
                stage doesn't have a default prim, also returns False.
        
                Args:
                    objects (Dict): The context object.
        
                Returns:
                    bool: Whether the selected prim is the default prim. If the prim selection is not a single prim, returns False.
                
        """
    @staticmethod
    def has_rename_function(objects):
        """
        
                Checks whether there's a provided rename function in the current context object.
        
                Args:
                    objects (Dict): The context object.
        
                Returns:
                    bool: True if 'rename_item' is in function list
                
        """
    @staticmethod
    def is_hovered_prim_material(objects):
        """
        
                Checks if the hoved prim is a USD Material prim.
                If no hovered prim detected, returns False.
        
                Args:
                    objects (Dict): The context object.
        
                Returns:
                    bool: Whether the hovered prim is a USD Material prim. If no hovered prim detected, returns False.
                
        """
    @staticmethod
    def is_prim_active(objects):
        """
        
                Checks if the selected prim is active.
                If the prim selection is not a single prim (eg. empty selection or multiple selected), returns False.
        
                Args:
                    objects (Dict): The context object.
        
                Returns:
                    bool: Whether the selected prim is active. If the prim selection is not a single prim, returns False.
                
        """
    @staticmethod
    def is_prim_not_active(objects):
        """
        
                Checks if the selected prim is NOT active.
                If the prim selection is not a single prim (eg. empty selection or multiple selected), returns True.
        
                Args:
                    objects (Dict): The context object.
        
                Returns:
                    bool: Whether the selected prim is NOT active. If the prim selection is not a single prim, returns True.
                
        """
    @staticmethod
    def is_prim_sudo_root(objects):
        """
        
                Checks if the selected prim is at the root level of the stage.
                If the prim selection is not a single prim (eg. empty selection or multiple selected), returns False.
        
                Args:
                    objects (Dict): The context object.
        
                Returns:
                    bool: Whether the selected prim is at root level. If the prim selection is not a single prim, returns False.
                
        """
    @staticmethod
    def link_selected(link_or_unlink, layer_identifier, hierarchy, objects):
        """
        
                Lock or unlink selected prims.
        
                Args:
                    link_or_unlink (bool): Links the spec paths if True, else the operation is unlink.
                    layer_identifiers (Union[str, List[str]]): List of layer identifiers or single layer identifier.
                    hierarchy (bool): Linking/Unlinking descendant specs or not.
                    objects: The context object.
                
        """
    @staticmethod
    def lock_selected(lock_or_unlock, hierarchy, objects):
        """
        
                Lock or unlock selected prims.
        
                Args:
                    lock_or_unlock (bool): Locks the spec paths if True, else the operation is unlock.
                    hierarchy (bool): Locking/Unlocking descendant specs or not.
                    objects: The context object.
                
        """
    @staticmethod
    def no_default_prim(objects):
        """
        
                Checks if the selected prim is NOT the default prim of the stage.
                If the prim selection is not a single prim (eg. empty selection or multiple selected), returns True. If the
                stage doesn't have a default prim, also returns True.
        
                Args:
                    objects (Dict): The context object.
        
                Returns:
                    bool: Whether the selected prim is NOT the default prim. If the prim selection is not a single prim,
                        returns False.
                
        """
    @staticmethod
    def rename_prim(objects):
        """
        
                Runs the provided 'rename_item' function on a prim.
                If the prim list provided in the context is empty or of multiple prims, it returns False without applying any
                rename function.
        
                Args:
                    objects (Dict): The context object.
        
                Returns:
                    Optional[bool]: False if the prim list provided is empty or is of multiple prims. Otherwise if a rename
                        function is provided, it will run the function without returning.
                
        """
    @staticmethod
    def select_linked_prims(objects):
        """
        
                Select all linked prims in the current usd context.
        
                Args:
                    objects (Dict): The context object. Unused.
                
        """
    @staticmethod
    def select_locked_prims(objects):
        """
        
                Select all locked prims in the current usd context.
        
                Args:
                    objects (Dict): The context object. Unused.
                
        """
    @staticmethod
    def set_default_prim(objects):
        """
        
                Sets the (first) selected prim as the default prim of the stage.
        
                Args:
                    objects (Dict): The context object.
                
        """
    @staticmethod
    def show_close_tree(objects):
        """
        
                If the collapsion related context menu items should be shown for the (first) selected prim.
                If the prim is a light or camera and doesn't have multiple children, items should not be shown. Otherwise, if
                the prim doesn't have any children, items should not be shown.
                If the current prim's associated tree node item is open, then items should be shown.
        
                 Args:
                    objects (Dict): The context object.
        
                Returns:
                    bool: Whether the collapsion related context menu items should be shown for the (first) selected prim.
                
        """
    @staticmethod
    def show_create_menu(objects):
        """
        
                Builds and shows the "Create" and "Add" menu.
        
                Args:
                    objects (Dict): The context object.
                
        """
    @staticmethod
    def show_open_tree(objects):
        """
        
                If the expansion related context menu items should be shown for the (first) selected prim.
                If the prim is a light or camera and doesn't have multiple children, items should not be shown. Otherwise, if
                the prim doesn't have any children, items should not be shown.
                If the current prim's associated tree node item is open, then items should not be shown.
        
                 Args:
                    objects (Dict): The context object.
        
                Returns:
                    bool: Whether the expansion related context menu items should be shown for the (first) selected prim.
                
        """
    def __init__(self):
        """
        Creates the ContextMenu instance.
        """
    def destroy(self):
        """
        Destroys the ContextMenu instance, resets the function list.
        """
    def on_mouse_event(self, event):
        """
        
                ContextMenuEvent handler for the current context menu.
        
                Args:
                    event (omni.kit.widget.stage.stage_delegate.ContextMenuEvent): The incoming ContextMenuEvent. It contains
                        information of the stage, prim path and node expansion status in its payload.
                
        """
