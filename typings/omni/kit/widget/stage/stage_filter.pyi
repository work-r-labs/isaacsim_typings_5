from __future__ import annotations
import carb as carb
from functools import partial
import omni.kit.widget.filter.filter
from omni.kit.widget.filter.filter import FilterButton
from omni.kit.widget.options_menu.option_item import OptionItem
from omni.kit.widget.options_menu.option_separator import OptionSeparator
from pxr import UsdGeom
from pxr import UsdLux
from pxr import UsdPhysics
from pxr import UsdShade
from pxr import UsdSkel
__all__: list = ['StageFilterButton']
class StageFilterButton(omni.kit.widget.filter.filter.FilterButton):
    """
    
        Filter button used in stage widget.
    
        Args:
            filter_provider: Provider where filter functions defined. Use stage widget.
        
    """
    def _StageFilterButton__filter_optional_audio(self, enabled):
        ...
    def __init__(self, filter_provider):
        ...
    def _filter_by_abstract_state(self, enabled):
        """
        Filter Abstract On/Off
        """
    def _filter_by_active_state(self, enabled):
        """
        Filter Active On/Off
        """
    def _filter_by_api_type(self, api_types, enabled):
        """
        
                Set filtering by USD api type.
        
                Args:
                    api_types: The api type or the list of types it's necessary to add or remove from filters.
                    enabled: True to add to filters, False to remove them from the filter list.
                
        """
    def _filter_by_def_state(self, enabled):
        """
        Filter Def On/Off
        """
    def _filter_by_flattener_basemesh(self, enabled):
        ...
    def _filter_by_flattener_decal(self, enabled):
        ...
    def _filter_by_type(self, usd_types, enabled):
        """
        
                Set filtering by USD type.
        
                Args:
                    usd_types: The type or the list of types it's necessary to add or remove from filters.
                    enabled: True to add to filters, False to remove them from the filter list.
                
        """
    def _filter_by_visibility(self, enabled):
        """
        Filter Hidden On/Off
        """
    def _get_item(self, name: str) -> typing.Optional[omni.kit.widget.options_menu.option_item.OptionItem]:
        ...
    def enable_filters(self, usd_type_list: list) -> list:
        """
        
                Enable filters.
        
                Args:
                    usd_type_list (list): List of usd types to be enabled.
        
                Returns:
                    returns usd types not supported
                
        """
