from __future__ import annotations
import carb as carb
import omni.kit.browser.core.models.browser_item
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni.kit.browser.core.models.browser_item import CollectionItem
from omni.kit.browser.core.models.browser_item import DetailItem
import omni.kit.browser.core.models.browser_model
from omni.kit.browser.core.models.browser_model import AbstractBrowserModel
from omni.kit.browser.core.models.browser_wrapper import ChildrenModelWrapper
from omni.kit.browser.core.models.browser_wrapper import CollectionModelWrapper
from omni.kit.browser.core.models.browser_wrapper import SingleLevelWrapper
from omni.kit.browser.core.widgets.category_delegate import CategoryDelegate
from omni.kit.browser.core.widgets.category_view import CategoryView
from omni.kit.browser.core.widgets.detail_delegate import DetailDelegate
from omni.kit.browser.core.widgets.overview_view import OverviewView
from omni.kit.browser.core.widgets.thumbnail_view import ThumbnailView
from omni.kit.widget.zoombar.zoom_bar import ZoomBar
from omni import ui
import omni.ui._ui
__all__ = ['AbstractBrowserModel', 'BrowserWidget', 'CategoryDelegate', 'CategoryItem', 'CategoryView', 'ChildrenModelWrapper', 'CollectionItem', 'CollectionModelWrapper', 'DETAIL_VIEW_PADDING', 'DetailDelegate', 'DetailItem', 'OverviewView', 'SingleLevelWrapper', 'ThumbnailView', 'UI_STYLES', 'ZoomBar', 'carb', 'ui']
class BrowserWidget:
    """
    
        Represents the browser widget, including a collection combobox, a category list view, a detail grid view and a overview grid view (if required)
        Args:
            model (BrowserModel): Data model used by the widget.
    
        Keyword Args:
            style (dict): Extra UI style of this widget. Default is empty.
            category_delegate (CatetoryDelegate): delegate object to represent category item. Default using CategoryDelegate.
            category_width (int): width of category view, in pixel. Default 120.
            detail_delegate (DetailDelegate): delegate object to represent detail item. Default using DetailDelegate.
            min_thumbnail_size (int): min thumbnail size used in zoom bar. Default 32.
            max_thumbnail_size (int): max thumbnail size used in zoom bar. Default 512.
            detail_thumbnail_size (int): size of detail item thumbnail, in pixel. Default 128.
            thumbnail_aspect (float): Aspect ratio of thumbnail. Default 1.0 (width / height).
            extra_filter_fn (callable): Extra filter function called to filter items. Return True to show item otherwise hide.
                Default None. Function signure: bool extra_filter_fn(item: DetailItem)
            category_tree_mode (bool): Show category in tree mode or flat mode. Default flat mode (No branches).
            overview_delegate (DetailDelegate): Delegate object to represent item in overview. Default using DetailDelegate.
            overview_thumbnail_size (int): size of overview item thumbnail, in pixel. Default 192.
            overview_thumbnail_aspect (float): Aspect ratio of overview thumbnail. Default 1.0 (width / height).
            overview_thumbnail_padding_width (int): Padding in overview thumbnail width. Default 10.
            overview_thumbnail_padding_height (int): Padding in overview thumbnail height. Default 1.
            always_select_category (bool): Always select category if collect changed. Default True.
            show_category_splitter (bool): Show splitter between category and detail. Default False.
            splitter_extra_width (int): Width added to vertical splitter between category view and detail view.
            show_collection (bool): True to show collection combobox. Default True.
            on_category_selection_changed_fn (Callable[[CategoryItem], None]): Callback when category selection changed.
            multiple_drag (bool): True to allow drag multiple items. Default False.
    
        Properties:
            collection_index (int): index of selected collection item. Read and write.
            collection_selection (Optional[Collection]): selected collection item. Readonly.
            category_selection (List[CategoryItem]): selected category item. Readonly.
            detail_selection (List[DetailItem]): selected detail item. Readonly.
        
    """
    def _BrowserWidget__on_thumbnail_size_changed(self, thumbnail_size: int) -> None:
        ...
    def __init__(self, model: omni.kit.browser.core.models.browser_model.AbstractBrowserModel, style = {}, category_delegate = None, category_width: float = 120, detail_delegate = None, min_thumbnail_size: int = 32, max_thumbnail_size: int = 512, detail_thumbnail_size: int = 128, thumbnail_aspect: float = 1.0, extra_filter_fn: callable = None, category_tree_mode: bool = False, overview_delegate = None, overview_thumbnail_size: int = 192, overview_thumbnail_aspect: float = 1.0, overview_thumbnail_padding_width: int = 10, overview_thumbnail_padding_height: int = 1, always_select_category: bool = True, show_category_splitter: bool = False, splitter_extra_width: int = 4, show_collection: bool = True, on_category_selection_changed_fn: typing.Callable[[omni.kit.browser.core.models.browser_item.CategoryItem], NoneType] = None, extra_ui_style: typing.Dict = {}, multiple_drag: bool = False):
        ...
    def _build_category_view(self):
        ...
    def _build_detail_view(self):
        ...
    def _build_detail_view_internal(self):
        ...
    def _build_left_panel(self):
        ...
    def _build_models(self, model: omni.kit.browser.core.models.browser_model.AbstractBrowserModel) -> None:
        ...
    def _build_overview_view(self):
        ...
    def _build_right_panel(self):
        ...
    def _build_ui(self) -> None:
        ...
    def _extra_ui_style_update(self, add_on_style: dict):
        ...
    def _on_category_selected(self, category_item: omni.kit.browser.core.models.browser_item.CategoryItem) -> None:
        ...
    def _on_collection_selected(self, collection_item: omni.kit.browser.core.models.browser_item.CollectionItem) -> None:
        ...
    def _on_model_item_changed(self, item: typing.Union[omni.kit.browser.core.models.browser_item.CollectionItem, omni.kit.browser.core.models.browser_item.CategoryItem, omni.kit.browser.core.models.browser_item.DetailItem]) -> None:
        ...
    def _splitter_offset_x_changed(self, offset_x: omni.ui._ui.Length) -> None:
        ...
    def add_filter_changed_fn(self, on_filter_changed_fn: callable) -> int:
        """
        
                Add callback function on filter changed.
                Return fuction id used for remove_filter_changed_fn.
                Args:
                    on_filter_changed_fn (callable): Function called when filter changed. Function signture:
                        void on_filter_changed_fn(filter_words: Optional[List[str]])
                
        """
    def add_thumbnail_size_changed_fn(self, on_thumbnail_size_changed_fn: callable) -> int:
        """
        
                Add callback function on thumbnail size changed.
                Return fuction id used for remove_thumbnail_size_changed_fn.
                Args:
                    on_thumbnail_size_changed_fn (callable): Function called when thumbnail size changed. Function signture:
                        void on_thumbnail_size_changed_fn(thumbnail_size: int)
                
        """
    def destroy(self):
        ...
    def filter_details(self, filter_words: typing.Optional[typing.List[str]]):
        """
        
                Filter detail items.
                Args:
                    filter_words: A string list to filter detail items. None means filtering nothing.
                
        """
    def refresh_details(self) -> None:
        """
        
                Refresh detail view for item visibilities.
                
        """
    def remove_filter_changed_fn(self, sub_id: int) -> None:
        """
        
                Remove callback function on filter chagned.
                Args:
                    sub_id: Function id, comes from add_filter_changed_fn.
                
        """
    def remove_thumbnail_size_changed_fn(self, sub_id: int) -> None:
        """
        
                Remove callback function on thumbnail size chagned.
                Args:
                    sub_id: Function id, comes from add_thumbnail_size_changed_fn.
                
        """
    def show_widgets(self, collection: typing.Optional[bool] = None, category: typing.Optional[bool] = None, detail: typing.Optional[bool] = None) -> None:
        """
        
                Show/Hide collection/category/detail widget.
                Args:
                    collection (Optional[bool]): True to show collection combobox and False to hide. Default None means no change.
                    category (Optional[bool]): True to show category view and False to hide. Default None means no change.
                    detail (Optional[bool]): True to show detail view and False to hide. Default None means no change.
                
        """
    def sort_changed(self) -> None:
        """
        
                Notify sort changed. Refresh thumbnail view if necessary.
                
        """
    @property
    def category_selection(self) -> typing.List[omni.kit.browser.core.models.browser_item.CategoryItem]:
        """
        Selected category items
        """
    @category_selection.setter
    def category_selection(self, items: typing.List[omni.kit.browser.core.models.browser_item.CategoryItem]) -> None:
        ...
    @property
    def collection_index(self) -> int:
        ...
    @collection_index.setter
    def collection_index(self, value):
        ...
    @property
    def collection_selection(self) -> typing.Optional[omni.kit.browser.core.models.browser_item.CollectionItem]:
        ...
    @property
    def detail_selection(self) -> typing.List[omni.kit.browser.core.models.browser_item.DetailItem]:
        """
        Selected detail items
        """
    @detail_selection.setter
    def detail_selection(self, selection: typing.List[omni.kit.browser.core.models.browser_item.DetailItem]) -> None:
        ...
    @property
    def model(self) -> omni.ui._ui.AbstractItemModel:
        """
        Model used in this widget
        """
    @model.setter
    def model(self, new_model: omni.kit.browser.core.models.browser_model.AbstractBrowserModel) -> None:
        ...
    @property
    def visible(self) -> bool:
        """
        widget visibility
        """
    @visible.setter
    def visible(self, value) -> None:
        ...
DETAIL_VIEW_PADDING: int = 2
UI_STYLES: dict  # value = {'CollectionList': {'background_color': 'shade:4280492319;light=4283650900', 'selected_color': 'shade:4283189827;light=4282927176', 'color': 'shade:4288782753;light=4292927712', 'border_radius': 1}, 'TreeView': {'background_color': 0, 'background_selected_color': 4285427310}, 'TreeView:selected': {'background_color': 0, 'secondary_color': 0}, 'TreeView.Frame': {'background_color': 'shade:4280492319;light=4283650900', 'secondary_color': 'shade:4286611584;light=4288585374', 'border_radius': 0, 'scrollbar_size': 10}, 'TreeView.Branch.Line': {'color': 'shade:4284177243', 'background_color': 'shade:4284177243', 'margin': 0}, 'TreeView.Item': {'color': 'shade:4289045925', 'border_width': 1.5, 'border_color': 'shade:4289045925'}, 'TreeView.Item:selected': {'color': 'shade:4289045925'}, 'TreeView.Item.Name': {'background_color': 0, 'color': 'shade:4288782753;light=4292927712'}, 'TreeView.Item.Name:selected': {'color': 'shade:4294952756;light=4291137818'}, 'TreeView.Item.Count': {'background_color': 0, 'color': 'shade:4283453264;light=4288782753'}, 'TreeView.Item.Count:selected': {'color': 'shade:4288782753;light=4292927712'}, 'TreeView.Mark': {'color': 0, 'border_width': 4}, 'TreeView.Mark:selected': {'color': 'shade:4294952756;light=4291137818', 'border_width': 4}, 'GridView.Frame': {'background_color': 'shade:4280492319;light=4283650900', 'secondary_color': 'shade:4286611584;light=4288585374', 'border_radius': 0, 'scrollbar_size': 10}, 'GridView.Grid': {'background_color': 0}, 'GridView.Item': {'background_color': 0, 'color': 'shade:4288782753;light=4292927712'}, 'GridView.Image': {'border_width': 0}, 'GridView.Image:selected': {'border_width': 2, 'border_color': 'shade:4294952756;light=4291137818', 'border_radius': 3.0}, 'GridView.Image.Placeholder': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.browser.core-2.3.11/icons/cloud_download.svg', 'color': 'shade:4289243304'}, 'CollapsableFrame': {'background_color': 0, 'secondary_color': 0, 'padding': 0, 'margin': 0}, 'Overview.Frame': {'background_color': 0}, 'Overview.Header.Arrow': {'background_color': 4287795858}, 'Overview.Header.Label': {'color': 4287795858}, 'Overview.Header.Line': {'color': 4285558896}, 'SearchBar.Button': {'background_color': 0, 'padding': 3, 'margin': 0, 'stack_direction': <Direction.LEFT_TO_RIGHT: 0>}, 'SearchBar.Button:hovered': {'background_color': 4282006074}, 'SearchBar.Button:pressed': {'background_color': 'shade:4280492319;light=4283650900'}, 'SearchBar.Button:selected': {'background_color': 'shade:4280492319;light=4283650900'}, 'SearchBar.Button.Image::navigation': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.browser.core-2.3.11/icons/navtree.svg', 'color': 'shade:4289243304'}, 'SearchBar.Button.Image::options': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.browser.core-2.3.11/icons/options.svg', 'color': 'shade:4289243304'}, 'SearchBar.Button.Label': {'color': 4289506476}, 'Splitter': {'background_color': 0, 'margin_width': 0}, 'Splitter:hovered': {'background_color': 4289753147}, 'Splitter:pressed': {'background_color': 4289753147}}
