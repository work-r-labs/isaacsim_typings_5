from __future__ import annotations
import calendar as calendar
import omni.kit.window.filepicker.datetime.models
from omni.kit.window.filepicker.datetime.models import DateModel
from omni import ui
__all__ = ['CalendarWidget', 'DateModel', 'calendar', 'select_circle_style', 'ui', 'unselect_circle_style']
class CalendarWidget:
    """
    
        Represents a calendar to show year month and day
        Keyword Args:
            model (DateModel): Widget model.
            width (int): Widget width. Default 160.
            height (int): Widget height. Default 140.
            year_min (int): min year in year combobox. default 2000,
            year_max (int): max year in year combobox. default 2050,
        
    """
    def __del__(self):
        ...
    def __init__(self, model: omni.kit.window.filepicker.datetime.models.DateModel, width: int = 175, height: int = 195, year_min: int = 2000, year_max: int = 2050):
        ...
    def _build_week_days(self):
        ...
    def _on_date_changed(self, model):
        ...
    def _on_day_changed(self, b, day: int):
        ...
    def _on_month_changed(self, model, item):
        ...
    def _on_year_changed(self, model, item):
        ...
    def destroy(self):
        ...
    @property
    def model(self):
        ...
select_circle_style: dict  # value = {'border_color': 'blue_light'}
unselect_circle_style: dict  # value = {'border_color': 'transparent'}
