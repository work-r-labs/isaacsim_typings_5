"""
UI Toolkit

Starting with the release 2020.1, Omniverse Kit UI Toolkit has been replaced by the alternative UI toolkit :mod:`Omni::UI <omni.ui>`. Currently the Omniverse Kit UI Toolkit is deprecated.

Omniverse Kit UI Toolkit is retained mode UI library which enables extending and changing Omniverse Kit look and feel in any direction.

It contains fundamental building primitives, like windows, containers, layouts, widgets. As well as additional API (built on top of it) to create widgets for USD attributes and omni.kit settings.

Typical example to create a window with a drag slider widget:

.. code-block::

    import omni.kit.ui
    window = omni.kit.ui.Window('My Window')
    d = omni.kit.ui.DragDouble()
    d.width = omni.kit.ui.Percent(30)
    window.layout.add_child(d)

All objects are python-friendly reference counted object. You don't need to explicitly release or control lifetime. In the code example above `window` will be kept alive until `window` is released.

Core:
------

* :class:`.Window`
* :class:`.Popup`
* :class:`.Container`
* :class:`.Value`
* :class:`.Length`
* :class:`.UnitType`
* :class:`.Widget`

Widgets:
--------

* :class:`.Label`
* :class:`.Button`
* :class:`.Spacer`
* :class:`.CheckBox`
* :class:`.ComboBox`
* :class:`.ComboBoxInt`
* :class:`.ListBox`
* :class:`.SliderInt`
* :class:`.SliderDouble`
* :class:`.DragInt`
* :class:`.DragInt2`
* :class:`.DragDouble`
* :class:`.DragDouble2`
* :class:`.DragDouble3`
* :class:`.DragDouble4`
* :class:`.Transform`
* :class:`.FieldInt`
* :class:`.FieldDouble`
* :class:`.TextBox`
* :class:`.ColorRgb`
* :class:`.ColorRgba`
* :class:`.Image`

Containers:
-----------

* :class:`.ColumnLayout`
* :class:`.RowLayout`
* :class:`.RowColumnLayout`
* :class:`.CollapsingFrame`
* :class:`.ScrollingFrame`




"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.ui._ui import BroadcastModel
from omni.kit.ui._ui import Button
from omni.kit.ui._ui import CheckBox
from omni.kit.ui._ui import ClippingType
from omni.kit.ui._ui import CollapsingFrame
from omni.kit.ui._ui import ColorRgb
from omni.kit.ui._ui import ColorRgba
from omni.kit.ui._ui import ColumnLayout
from omni.kit.ui._ui import ComboBox
from omni.kit.ui._ui import ComboBoxInt
from omni.kit.ui._ui import Container
from omni.kit.ui._ui import ContainerBase
from omni.kit.ui._ui import ContentWindow
from omni.kit.ui._ui import DelegateAction
from omni.kit.ui._ui import DelegateResult
from omni.kit.ui._ui import DockPreference
from omni.kit.ui._ui import DragDouble
from omni.kit.ui._ui import DragDouble2
from omni.kit.ui._ui import DragDouble3
from omni.kit.ui._ui import DragDouble4
from omni.kit.ui._ui import DragInt
from omni.kit.ui._ui import DragInt2
from omni.kit.ui._ui import DragUInt
from omni.kit.ui._ui import DraggingType
from omni.kit.ui._ui import FieldDouble
from omni.kit.ui._ui import FieldInt
from omni.kit.ui._ui import FileDialogDataSource
from omni.kit.ui._ui import FileDialogOpenMode
from omni.kit.ui._ui import FileDialogSelectType
from omni.kit.ui._ui import FilePicker
from omni.kit.ui._ui import Image
from omni.kit.ui._ui import Label
from omni.kit.ui._ui import Length
from omni.kit.ui._ui import ListBox
from omni.kit.ui._ui import Mat44
from omni.kit.ui._ui import Menu
from omni.kit.ui._ui import MenuEventType
from omni.kit.ui._ui import Model
from omni.kit.ui._ui import ModelChangeInfo
from omni.kit.ui._ui import ModelEventType
from omni.kit.ui._ui import ModelNodeType
from omni.kit.ui._ui import ModelWidget
from omni.kit.ui._ui import Percent
from omni.kit.ui._ui import Pixel
from omni.kit.ui._ui import Popup
from omni.kit.ui._ui import ProgressBar
from omni.kit.ui._ui import RowColumnLayout
from omni.kit.ui._ui import RowLayout
from omni.kit.ui._ui import ScalarXYZ
from omni.kit.ui._ui import ScalarXYZW
from omni.kit.ui._ui import ScrollingFrame
from omni.kit.ui._ui import Separator
from omni.kit.ui._ui import SimpleTreeView
from omni.kit.ui._ui import SimpleValueWidgetBool
from omni.kit.ui._ui import SimpleValueWidgetColorRgb
from omni.kit.ui._ui import SimpleValueWidgetColorRgba
from omni.kit.ui._ui import SimpleValueWidgetDouble
from omni.kit.ui._ui import SimpleValueWidgetDouble2
from omni.kit.ui._ui import SimpleValueWidgetDouble3
from omni.kit.ui._ui import SimpleValueWidgetDouble4
from omni.kit.ui._ui import SimpleValueWidgetInt
from omni.kit.ui._ui import SimpleValueWidgetInt2
from omni.kit.ui._ui import SimpleValueWidgetMat44
from omni.kit.ui._ui import SimpleValueWidgetString
from omni.kit.ui._ui import SimpleValueWidgetUint
from omni.kit.ui._ui import SliderDouble
from omni.kit.ui._ui import SliderDouble2
from omni.kit.ui._ui import SliderDouble3
from omni.kit.ui._ui import SliderDouble4
from omni.kit.ui._ui import SliderInt
from omni.kit.ui._ui import SliderInt2
from omni.kit.ui._ui import SliderUInt
from omni.kit.ui._ui import Spacer
from omni.kit.ui._ui import TextBox
from omni.kit.ui._ui import Transform
from omni.kit.ui._ui import UnitType
from omni.kit.ui._ui import ValueWidgetBool
from omni.kit.ui._ui import ValueWidgetColorRgb
from omni.kit.ui._ui import ValueWidgetColorRgba
from omni.kit.ui._ui import ValueWidgetDouble
from omni.kit.ui._ui import ValueWidgetDouble2
from omni.kit.ui._ui import ValueWidgetDouble3
from omni.kit.ui._ui import ValueWidgetDouble4
from omni.kit.ui._ui import ValueWidgetInt
from omni.kit.ui._ui import ValueWidgetInt2
from omni.kit.ui._ui import ValueWidgetMat44
from omni.kit.ui._ui import ValueWidgetString
from omni.kit.ui._ui import ValueWidgetUint
from omni.kit.ui._ui import ViewCollapsing
from omni.kit.ui._ui import ViewFlat
from omni.kit.ui._ui import ViewTreeGrid
from omni.kit.ui._ui import Widget
from omni.kit.ui._ui import Window
from omni.kit.ui._ui import WindowEventType
from omni.kit.ui._ui import WindowMainStandalone
from omni.kit.ui._ui import WindowStandalone
from omni.kit.ui._ui import activate_menu_item
from omni.kit.ui._ui import get_custom_glyph_code
from omni.kit.ui._ui import get_editor_menu_legacy
from omni.kit.ui._ui import get_main_window
from omni.kit.ui.editor_menu import EditorMenu
import weakref as weakref
from . import _ui
from . import actions
from . import editor_menu
__all__ = ['BroadcastModel', 'Button', 'CheckBox', 'ClippingType', 'CollapsingFrame', 'ColorRgb', 'ColorRgba', 'ColumnLayout', 'ComboBox', 'ComboBoxInt', 'Container', 'ContainerBase', 'ContentWindow', 'DelegateAction', 'DelegateResult', 'DockPreference', 'DragDouble', 'DragDouble2', 'DragDouble3', 'DragDouble4', 'DragInt', 'DragInt2', 'DragUInt', 'DraggingType', 'EditorMenu', 'FieldDouble', 'FieldInt', 'FileDialogDataSource', 'FileDialogOpenMode', 'FileDialogSelectType', 'FilePicker', 'Image', 'Label', 'Length', 'ListBox', 'MODEL_META_SERIALIZED_CONTENTS', 'MODEL_META_WIDGET_TYPE', 'Mat44', 'Menu', 'MenuEventType', 'Model', 'ModelChangeInfo', 'ModelEventType', 'ModelNodeType', 'ModelWidget', 'Percent', 'Pixel', 'Popup', 'ProgressBar', 'RowColumnLayout', 'RowLayout', 'ScalarXYZ', 'ScalarXYZW', 'ScrollingFrame', 'Separator', 'SimpleTreeView', 'SimpleValueWidgetBool', 'SimpleValueWidgetColorRgb', 'SimpleValueWidgetColorRgba', 'SimpleValueWidgetDouble', 'SimpleValueWidgetDouble2', 'SimpleValueWidgetDouble3', 'SimpleValueWidgetDouble4', 'SimpleValueWidgetInt', 'SimpleValueWidgetInt2', 'SimpleValueWidgetMat44', 'SimpleValueWidgetString', 'SimpleValueWidgetUint', 'SliderDouble', 'SliderDouble2', 'SliderDouble3', 'SliderDouble4', 'SliderInt', 'SliderInt2', 'SliderUInt', 'Spacer', 'TextBox', 'Transform', 'UnitType', 'ValueWidgetBool', 'ValueWidgetColorRgb', 'ValueWidgetColorRgba', 'ValueWidgetDouble', 'ValueWidgetDouble2', 'ValueWidgetDouble3', 'ValueWidgetDouble4', 'ValueWidgetInt', 'ValueWidgetInt2', 'ValueWidgetMat44', 'ValueWidgetString', 'ValueWidgetUint', 'ViewCollapsing', 'ViewFlat', 'ViewTreeGrid', 'WINDOW_FLAGS_FORCE_HORIZONTAL_SCROLLBAR', 'WINDOW_FLAGS_FORCE_VERTICAL_SCROLLBAR', 'WINDOW_FLAGS_MODAL', 'WINDOW_FLAGS_NONE', 'WINDOW_FLAGS_NO_CLOSE', 'WINDOW_FLAGS_NO_COLLAPSE', 'WINDOW_FLAGS_NO_FOCUS_ON_APPEARING', 'WINDOW_FLAGS_NO_MOVE', 'WINDOW_FLAGS_NO_RESIZE', 'WINDOW_FLAGS_NO_SAVED_SETTINGS', 'WINDOW_FLAGS_NO_SCROLLBAR', 'WINDOW_FLAGS_NO_TITLE_BAR', 'WINDOW_FLAGS_SHOW_HORIZONTAL_SCROLLBAR', 'Widget', 'Window', 'WindowEventType', 'WindowMainStandalone', 'WindowStandalone', 'actions', 'activate_menu_item', 'add_item_attached', 'carb', 'create_window_hook', 'editor_menu', 'get_custom_glyph_code', 'get_editor_menu', 'get_editor_menu_legacy', 'get_main_window', 'init_ui', 'legacy_mode', 'omni', 'using_legacy_mode', 'weakref']
def add_item_attached(self: _ui.Menu, *args, **kwargs):
    ...
def create_window_hook(self, title: str, *args, **kwargs):
    ...
def get_editor_menu():
    ...
def init_ui():
    ...
def using_legacy_mode():
    ...
MODEL_META_SERIALIZED_CONTENTS: str = 'serializedContents'
MODEL_META_WIDGET_TYPE: str = 'widgetType'
WINDOW_FLAGS_FORCE_HORIZONTAL_SCROLLBAR: int = 512
WINDOW_FLAGS_FORCE_VERTICAL_SCROLLBAR: int = 256
WINDOW_FLAGS_MODAL: int = 4096
WINDOW_FLAGS_NONE: int = 0
WINDOW_FLAGS_NO_CLOSE: int = 2048
WINDOW_FLAGS_NO_COLLAPSE: int = 16
WINDOW_FLAGS_NO_FOCUS_ON_APPEARING: int = 1024
WINDOW_FLAGS_NO_MOVE: int = 4
WINDOW_FLAGS_NO_RESIZE: int = 2
WINDOW_FLAGS_NO_SAVED_SETTINGS: int = 32
WINDOW_FLAGS_NO_SCROLLBAR: int = 8
WINDOW_FLAGS_NO_TITLE_BAR: int = 1
WINDOW_FLAGS_SHOW_HORIZONTAL_SCROLLBAR: int = 128
legacy_mode: bool = False
