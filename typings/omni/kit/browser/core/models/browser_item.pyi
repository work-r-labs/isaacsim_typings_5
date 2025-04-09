from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__ = ['BaseItem', 'CategoryItem', 'CollectionItem', 'DetailItem', 'ui']
class BaseItem(omni.ui._ui.AbstractItem):
    """
    
        A common item for BrowserModel
        Args:
            name (str): item name
        
    """
    def __init__(self, name: str):
        ...
    @property
    def name(self) -> str:
        ...
class CategoryItem(BaseItem):
    """
    
        A single AbstractItem item that represents a single category.
        Args:
            name (str): catetory name
            count (int): count of detail items in this category. Default is 0.
        
    """
    def __init__(self, name, count = 0, parent: typing.Optional[omni.kit.browser.core.models.browser_item.BaseItem] = None, is_last_child: typing.Optional[bool] = False):
        ...
    def __repr__(self):
        ...
    def filter(self, filter_words: typing.Optional[typing.List[str]]) -> bool:
        """
        
                Filter detail item. Return True if filtered otherwise False.
                Args:
                    filter_words: A string list to filter detail items. None means filtering nothing.
                
        """
class CollectionItem(BaseItem):
    """
    
        A single AbstractItem item that represents a single collection.
        Args:
            name (str): collection name
            url (str): collection url
        
    """
    def __init__(self, name: str, url: str):
        ...
    def __repr__(self):
        ...
class DetailItem(BaseItem):
    """
    
        A single AbstractItem item that represents a single detail item.
        Args:
            name (str): detail name
            url (str): detail url
            thumbnail (str): detail thumbnail url
        
    """
    def __init__(self, name: str, url: str, thumbnail: str = None):
        ...
    def __repr__(self):
        ...
    def filter(self, filter_words: typing.Optional[typing.List[str]]) -> bool:
        """
        
                Filter detail item. Return True if filtered otherwise False.
                Args:
                    filter_words: A string list to filter detail items. None means filtering nothing.
                
        """
