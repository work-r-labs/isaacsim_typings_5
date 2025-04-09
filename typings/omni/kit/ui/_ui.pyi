from __future__ import annotations
import carb._carb
import carb.events._events
import omni.kit.ui.editor_menu
import omni.ui._ui
import typing
__all__ = ['BroadcastModel', 'Button', 'CheckBox', 'ClippingType', 'CollapsingFrame', 'ColorRgb', 'ColorRgba', 'ColumnLayout', 'ComboBox', 'ComboBoxInt', 'Container', 'ContainerBase', 'ContentWindow', 'DelegateAction', 'DelegateResult', 'DockPreference', 'DragDouble', 'DragDouble2', 'DragDouble3', 'DragDouble4', 'DragInt', 'DragInt2', 'DragUInt', 'DraggingType', 'FieldDouble', 'FieldInt', 'FileDialogDataSource', 'FileDialogOpenMode', 'FileDialogSelectType', 'FilePicker', 'Image', 'Label', 'Length', 'ListBox', 'MODEL_META_SERIALIZED_CONTENTS', 'MODEL_META_WIDGET_TYPE', 'Mat44', 'Menu', 'MenuEventType', 'Model', 'ModelChangeInfo', 'ModelEventType', 'ModelNodeType', 'ModelWidget', 'Percent', 'Pixel', 'Popup', 'ProgressBar', 'RowColumnLayout', 'RowLayout', 'ScalarXYZ', 'ScalarXYZW', 'ScrollingFrame', 'Separator', 'SimpleTreeView', 'SimpleValueWidgetBool', 'SimpleValueWidgetColorRgb', 'SimpleValueWidgetColorRgba', 'SimpleValueWidgetDouble', 'SimpleValueWidgetDouble2', 'SimpleValueWidgetDouble3', 'SimpleValueWidgetDouble4', 'SimpleValueWidgetInt', 'SimpleValueWidgetInt2', 'SimpleValueWidgetMat44', 'SimpleValueWidgetString', 'SimpleValueWidgetUint', 'SliderDouble', 'SliderDouble2', 'SliderDouble3', 'SliderDouble4', 'SliderInt', 'SliderInt2', 'SliderUInt', 'Spacer', 'TextBox', 'Transform', 'UnitType', 'ValueWidgetBool', 'ValueWidgetColorRgb', 'ValueWidgetColorRgba', 'ValueWidgetDouble', 'ValueWidgetDouble2', 'ValueWidgetDouble3', 'ValueWidgetDouble4', 'ValueWidgetInt', 'ValueWidgetInt2', 'ValueWidgetMat44', 'ValueWidgetString', 'ValueWidgetUint', 'ViewCollapsing', 'ViewFlat', 'ViewTreeGrid', 'WINDOW_FLAGS_FORCE_HORIZONTAL_SCROLLBAR', 'WINDOW_FLAGS_FORCE_VERTICAL_SCROLLBAR', 'WINDOW_FLAGS_MODAL', 'WINDOW_FLAGS_NONE', 'WINDOW_FLAGS_NO_CLOSE', 'WINDOW_FLAGS_NO_COLLAPSE', 'WINDOW_FLAGS_NO_FOCUS_ON_APPEARING', 'WINDOW_FLAGS_NO_MOVE', 'WINDOW_FLAGS_NO_RESIZE', 'WINDOW_FLAGS_NO_SAVED_SETTINGS', 'WINDOW_FLAGS_NO_SCROLLBAR', 'WINDOW_FLAGS_NO_TITLE_BAR', 'WINDOW_FLAGS_SHOW_HORIZONTAL_SCROLLBAR', 'Widget', 'Window', 'WindowEventType', 'WindowMainStandalone', 'WindowStandalone', 'activate_menu_item', 'get_custom_glyph_code', 'get_editor_menu_legacy', 'get_main_window']
class BroadcastModel(Model):
    def __init__(self) -> None:
        ...
    def add_target(self, arg0: Model, arg1: str, arg2: str) -> int:
        ...
    def remove_target(self, arg0: int) -> None:
        ...
class Button(Label):
    """
    
                Button Widget.
    
                Args:
                    text (str): Text on button.
                    is_image (bool): Text is an image filename.
            
    """
    url: str
    def __init__(self, text: str = '', is_image: bool = False, default_color: int = 4294967295) -> None:
        ...
    def set_clicked_fn(self, arg0: typing.Callable[[Widget], None]) -> None:
        ...
class CheckBox(SimpleValueWidgetBool):
    """
    
                CheckBox Widget.
    
                Args:
                    text (str, default=""): Text on label.
                    value (bool, default=False): Initial value.
                    left_handed (bool, default=False): Initial value.
                    styled (bool, default=False): Initial value
            
    """
    styled: bool
    def __init__(self, text: str = '', value: bool = False, left_handed: bool = False, styled: bool = False) -> None:
        ...
class ClippingType:
    """
    Supported text clipping types.
    
    Members:
    
      NONE
    
      ELLIPSIS_LEFT
    
      ELLIPSIS_RIGHT
    
      WRAP
    """
    ELLIPSIS_LEFT: typing.ClassVar[ClippingType]  # value = <ClippingType.ELLIPSIS_LEFT: 1>
    ELLIPSIS_RIGHT: typing.ClassVar[ClippingType]  # value = <ClippingType.ELLIPSIS_RIGHT: 2>
    NONE: typing.ClassVar[ClippingType]  # value = <ClippingType.NONE: 0>
    WRAP: typing.ClassVar[ClippingType]  # value = <ClippingType.WRAP: 3>
    __members__: typing.ClassVar[dict[str, ClippingType]]  # value = {'NONE': <ClippingType.NONE: 0>, 'ELLIPSIS_LEFT': <ClippingType.ELLIPSIS_LEFT: 1>, 'ELLIPSIS_RIGHT': <ClippingType.ELLIPSIS_RIGHT: 2>, 'WRAP': <ClippingType.WRAP: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CollapsingFrame(Container):
    open: bool
    title: str
    use_frame_background_color: bool
    visible: bool
    def __init__(self, arg0: str, arg1: bool) -> None:
        ...
class ColorRgb(SimpleValueWidgetColorRgb):
    """
    
                Color Picker Widget (Tuple[float, float, float]).
    
                Args:
                    text (str, default=""): Text on label.
                    value (Tuple[float, float, float], default=(0.0, 0.0, 0.0)): Initial value.
            
    """
    def __init__(self, text: str = '', value: carb._carb.ColorRgb = ...) -> None:
        ...
class ColorRgba(SimpleValueWidgetColorRgba):
    """
    
                Color Picker Widget (Tuple[float, float, float, float]).
    
                Args:
                    text (str, default=""): Text on label.
                    value (Tuple[float, float, float, float], default=(0.0, 0.0, 0.0)): Initial value.
            
    """
    def __init__(self, text: str = '', value: carb._carb.ColorRgba = ...) -> None:
        ...
class ColumnLayout(Container):
    def __init__(self, spacing: int = -1, padding_x: int = -1, padding_y: int = -1) -> None:
        ...
class ComboBox(SimpleValueWidgetString):
    """
    
                ComboBox Widget.
    
                Args:
                    text (str, default=""): Text on label.
                    items (List[[str], default=[]): List of elements.
                    display_names (List[str], default=[]): List of element display names. Optional.
            
    """
    selected_index: int
    def __init__(self, text: str = '', items: list[str] = [], display_names: list[str] = []) -> None:
        ...
    def add_item(self, item: str, display_name: str = '') -> None:
        ...
    def clear_items(self) -> None:
        ...
    def get_item_at(self, arg0: int) -> str:
        ...
    def get_item_count(self) -> int:
        ...
    def remove_item(self, arg0: int) -> None:
        ...
    def set_items(self, items: list[str], display_names: list[str] = []) -> None:
        ...
class ComboBoxInt(SimpleValueWidgetInt):
    """
    
                ComboBox Widget.
    
                Args:
                    text (str, default=""): Text on label.
                    items (List[[int], default=[]): List of elements.
                    display_names (List[int], default=[]): List of element display names. Optional.
            
    """
    selected_index: int
    def __init__(self, text: str = '', items: list[int] = [], display_names: list[str] = []) -> None:
        ...
    def add_item(self, item: int, display_name: str = '') -> None:
        ...
    def clear_items(self) -> None:
        ...
    def get_item_at(self, arg0: int) -> int:
        ...
    def get_item_count(self) -> int:
        ...
    def remove_item(self, arg0: int) -> None:
        ...
    def set_items(self, items: list[int], display_names: list[str] = []) -> None:
        ...
class Container(Widget):
    """
    Base class for all UI containers. Container can hold arbitrary number of other :class:`.Widget` s
    """
    child_spacing: carb._carb.Float2
    def add_child(self, arg0: Widget) -> Widget:
        ...
    def clear(self) -> None:
        ...
    def get_child_at(self, arg0: int) -> Widget:
        ...
    def get_child_count(self) -> int:
        ...
    def remove_child(self, arg0: Widget) -> None:
        ...
class ContainerBase(Widget):
    """
    Class for the complex widget that can have children, but doesn;t allow to add children for the external user.
    """
    def draw(self, arg0: float) -> None:
        ...
class ContentWindow(Widget):
    """
    
                Content Window.
    
                Content Window is container that hosts a file picker widget.
            
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    def get_selected_icon_paths(self) -> tuple:
        ...
    def get_selected_node_paths(self) -> tuple:
        ...
    def navigate_to(self, arg0: str) -> None:
        ...
    def refresh(self) -> None:
        ...
    def set_filter(self, arg0: str) -> None:
        ...
class DelegateAction:
    """
    Members:
    
      CREATE_DEFAULT_WIDGET
    
      SKIP_KEY
    
      USE_CUSTOM_WIDGET
    """
    CREATE_DEFAULT_WIDGET: typing.ClassVar[DelegateAction]  # value = <DelegateAction.CREATE_DEFAULT_WIDGET: 0>
    SKIP_KEY: typing.ClassVar[DelegateAction]  # value = <DelegateAction.SKIP_KEY: 1>
    USE_CUSTOM_WIDGET: typing.ClassVar[DelegateAction]  # value = <DelegateAction.USE_CUSTOM_WIDGET: 2>
    __members__: typing.ClassVar[dict[str, DelegateAction]]  # value = {'CREATE_DEFAULT_WIDGET': <DelegateAction.CREATE_DEFAULT_WIDGET: 0>, 'SKIP_KEY': <DelegateAction.SKIP_KEY: 1>, 'USE_CUSTOM_WIDGET': <DelegateAction.USE_CUSTOM_WIDGET: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DelegateResult:
    action: DelegateAction
    custom_widget: Widget
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: DelegateAction) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Widget) -> None:
        ...
class DockPreference:
    """
    Members:
    
      DISABLED
    
      MAIN
    
      RIGHT
    
      LEFT
    
      RIGHT_TOP
    
      RIGHT_BOTTOM
    
      LEFT_BOTTOM
    """
    DISABLED: typing.ClassVar[DockPreference]  # value = <DockPreference.DISABLED: 0>
    LEFT: typing.ClassVar[DockPreference]  # value = <DockPreference.LEFT: 3>
    LEFT_BOTTOM: typing.ClassVar[DockPreference]  # value = <DockPreference.LEFT_BOTTOM: 6>
    MAIN: typing.ClassVar[DockPreference]  # value = <DockPreference.MAIN: 1>
    RIGHT: typing.ClassVar[DockPreference]  # value = <DockPreference.RIGHT: 2>
    RIGHT_BOTTOM: typing.ClassVar[DockPreference]  # value = <DockPreference.RIGHT_BOTTOM: 5>
    RIGHT_TOP: typing.ClassVar[DockPreference]  # value = <DockPreference.RIGHT_TOP: 4>
    __members__: typing.ClassVar[dict[str, DockPreference]]  # value = {'DISABLED': <DockPreference.DISABLED: 0>, 'MAIN': <DockPreference.MAIN: 1>, 'RIGHT': <DockPreference.RIGHT: 2>, 'LEFT': <DockPreference.LEFT: 3>, 'RIGHT_TOP': <DockPreference.RIGHT_TOP: 4>, 'RIGHT_BOTTOM': <DockPreference.RIGHT_BOTTOM: 5>, 'LEFT_BOTTOM': <DockPreference.LEFT_BOTTOM: 6>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DragDouble(SimpleValueWidgetDouble):
    """
    
                Drag Widget (double).
    
                If `min` >= `max` widget value has no bound.
    
                Args:
                    text (str, default=""): Text on label.
                    value (double, default=0): Initial value.
                    min (double, default=0): Lower value limit.
                    max (double, default=0): Upper value limit.
                    drag_speed (float, default=1.0): Drag speed.
            
    """
    drag_speed: float
    format: str
    max: float
    min: float
    def __init__(self, text: str = '', value: float = 0.0, min: float = 0, max: float = 0, drag_speed: float = 1.0) -> None:
        ...
class DragDouble2(SimpleValueWidgetDouble2):
    """
    
                Drag Widget (Tuple[double, double]).
    
                If `min` >= `max` widget value has no bound.
    
                Args:
                    text (str, default=""): Text on label.
                    value (Tuple[double, double], default=0): Initial value.
                    min (double, default=0): Lower value limit.
                    max (double, default=0): Upper value limit.
                    drag_speed (float, default=1.0): Drag speed.
            
    """
    drag_speed: float
    format: str
    max: float
    min: float
    def __init__(self, text: str = '', value: carb._carb.Double2 = ..., min: float = 0, max: float = 0, drag_speed: float = 1.0) -> None:
        ...
class DragDouble3(SimpleValueWidgetDouble3):
    """
    
                Drag Widget (Tuple[double, double, double]).
    
                If `min` >= `max` widget value has no bound.
    
                Args:
                    text (str, default=""): Text on label.
                    value (Tuple[double, double, double], default=0): Initial value.
                    min (double, default=0): Lower value limit.
                    max (double, default=0): Upper value limit.
                    drag_speed (float, default=1.0): Drag speed.
            
    """
    drag_speed: float
    format: str
    max: float
    min: float
    def __init__(self, text: str = '', value: carb._carb.Double3 = ..., min: float = 0, max: float = 0, drag_speed: float = 1.0) -> None:
        ...
class DragDouble4(SimpleValueWidgetDouble4):
    """
    
                Drag Widget (Tuple[double, double, double, double]).
    
                If `min` >= `max` widget value has no bound.
    
                Args:
                    text (str, default=""): Text on label.
                    value (Tuple[double, double, double, double], default=0): Initial value.
                    min (double, default=0): Lower value limit.
                    max (double, default=0): Upper value limit.
                    drag_speed (float, default=1.0): Drag speed.
            
    """
    drag_speed: float
    format: str
    max: float
    min: float
    def __init__(self, text: str = '', value: carb._carb.Double4 = ..., min: float = 0, max: float = 0, drag_speed: float = 1.0) -> None:
        ...
class DragInt(SimpleValueWidgetInt):
    """
    
                Drag Widget (int).
    
                If `min` >= `max` widget value has no bound.
    
                Args:
                    text (str, default=""): Text on label.
                    value (int, default=0): Initial value.
                    min (int, default=0): Lower value limit.
                    max (int, default=0): Upper value limit.
                    drag_speed (float, default=1.0): Drag speed.
            
    """
    drag_speed: float
    format: str
    max: int
    min: int
    def __init__(self, text: str = '', value: int = 0, min: int = 0, max: int = 0, drag_speed: float = 1.0) -> None:
        ...
class DragInt2(SimpleValueWidgetInt2):
    """
    
                Drag Widget (Tuple[int, int]).
    
                If `min` >= `max` widget value has no bound.
    
                Args:
                    text (str, default=""): Text on label.
                    value (Tuple[int, int], default=0): Initial value.
                    min (int, default=0): Lower value limit.
                    max (int, default=0): Upper value limit.
                    drag_speed (float, default=1.0): Drag speed.
            
    """
    drag_speed: float
    format: str
    max: int
    min: int
    def __init__(self, text: str = '', value: carb._carb.Int2 = ..., min: int = 0, max: int = 0, drag_speed: float = 1.0) -> None:
        ...
class DragUInt(SimpleValueWidgetUint):
    """
    
                Drag Widget (uint32_t).
    
                If `min` >= `max` widget value has no bound.
    
                Args:
                    text (str, default=""): Text on label.
                    value (uint32_t, default=0): Initial value.
                    min (uint32_t, default=0): Lower value limit.
                    max (uint32_t, default=0): Upper value limit.
                    drag_speed (float, default=1.0): Drag speed.
            
    """
    drag_speed: float
    format: str
    max: int
    min: int
    def __init__(self, text: str = '', value: int = 0, min: int = 0, max: int = 0, drag_speed: float = 1.0) -> None:
        ...
class DraggingType:
    """
    Supported dragging types.
    
    Members:
    
      STARTED
    
      STOPPED
    """
    STARTED: typing.ClassVar[DraggingType]  # value = <DraggingType.STARTED: 0>
    STOPPED: typing.ClassVar[DraggingType]  # value = <DraggingType.STOPPED: 1>
    __members__: typing.ClassVar[dict[str, DraggingType]]  # value = {'STARTED': <DraggingType.STARTED: 0>, 'STOPPED': <DraggingType.STOPPED: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class FieldDouble(SimpleValueWidgetDouble):
    """
    
                Field Widget (double).
    
                Args:
                    text (str, default=""): Text on label.
                    value (double, default=0): Initial value.
                    step (double, default=1): Value step.
                    step_fast (double, default=100): Fast value step.        
    """
    format: str
    step: float
    step_fast: float
    def __init__(self, text: str = '', value: float = 0.0, step: float = 1, step_fast: float = 100) -> None:
        ...
class FieldInt(SimpleValueWidgetInt):
    """
    
                Field Widget (int).
    
                Args:
                    text (str, default=""): Text on label.
                    value (int, default=0): Initial value.
                    step (int, default=1): Value step.
                    step_fast (int, default=100): Fast value step.        
    """
    format: str
    step: int
    step_fast: int
    def __init__(self, text: str = '', value: int = 0, step: int = 1, step_fast: int = 100) -> None:
        ...
class FileDialogDataSource:
    """
    Data source of File Dialog.
    
    Members:
    
      LOCAL
    
      OMNIVERSE
    
      ALL
    """
    ALL: typing.ClassVar[FileDialogDataSource]  # value = <FileDialogDataSource.ALL: 2>
    LOCAL: typing.ClassVar[FileDialogDataSource]  # value = <FileDialogDataSource.LOCAL: 0>
    OMNIVERSE: typing.ClassVar[FileDialogDataSource]  # value = <FileDialogDataSource.OMNIVERSE: 1>
    __members__: typing.ClassVar[dict[str, FileDialogDataSource]]  # value = {'LOCAL': <FileDialogDataSource.LOCAL: 0>, 'OMNIVERSE': <FileDialogDataSource.OMNIVERSE: 1>, 'ALL': <FileDialogDataSource.ALL: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class FileDialogOpenMode:
    """
    Open mode of File Dialog.
    
    Members:
    
      OPEN
    
      SAVE
    """
    OPEN: typing.ClassVar[FileDialogOpenMode]  # value = <FileDialogOpenMode.OPEN: 0>
    SAVE: typing.ClassVar[FileDialogOpenMode]  # value = <FileDialogOpenMode.SAVE: 1>
    __members__: typing.ClassVar[dict[str, FileDialogOpenMode]]  # value = {'OPEN': <FileDialogOpenMode.OPEN: 0>, 'SAVE': <FileDialogOpenMode.SAVE: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class FileDialogSelectType:
    """
    File selection type of File Dialog.
    
    Members:
    
      FILE
    
      DIRECTORY
    
      ALL
    """
    ALL: typing.ClassVar[FileDialogSelectType]  # value = <FileDialogSelectType.ALL: 2>
    DIRECTORY: typing.ClassVar[FileDialogSelectType]  # value = <FileDialogSelectType.DIRECTORY: 1>
    FILE: typing.ClassVar[FileDialogSelectType]  # value = <FileDialogSelectType.FILE: 0>
    __members__: typing.ClassVar[dict[str, FileDialogSelectType]]  # value = {'FILE': <FileDialogSelectType.FILE: 0>, 'DIRECTORY': <FileDialogSelectType.DIRECTORY: 1>, 'ALL': <FileDialogSelectType.ALL: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class FilePicker:
    selection_type: FileDialogSelectType
    title: str
    def __init__(self, title: str, mode: FileDialogOpenMode = ..., file_type: FileDialogSelectType = ..., on_file_selected: typing.Callable[[str], None] = None, on_dialog_cancelled: typing.Callable[[], None] = None, width: float = 800.0, height: float = 440.0) -> None:
        ...
    def add_filter(self, arg0: str, arg1: str) -> None:
        ...
    def clear_all_filters(self) -> None:
        ...
    def is_visible(self) -> bool:
        ...
    def set_current_directory(self, arg0: str) -> None:
        ...
    def set_default_save_name(self, name: str) -> None:
        """
        sets the default name to use for the filename on save dialogs.
        
                        This sets the default filename to be used when saving a file.  This name will
                        be ignored if the dialog is not in @ref FileDialogOpenMode::eSave mode.  The
                        given name will still be stored regardless.  This default filename may omit
                        the file extension to take the extension from the current filter.  If an
                        extension is explicitly given here, no extension will be appended regardless
                        of the current filter.
        
                        Args:
                            name: the default filename to use for this dialog.  This may be None
                                  or an empty string to use the USD stage's default prim name.  In
                                  this case, if the prim name cannot be retrieved, "Untitled" will
                                  be used instead.  If a non-empty string is given here, this will
                                  always be used as the initial suggested filename.
        
                        Returns:
                            No return value.
        """
    def set_dialog_cancelled_fn(self, arg0: typing.Callable[[], None]) -> None:
        ...
    def set_file_selected_fn(self, arg0: typing.Callable[[str], None]) -> None:
        ...
    def show(self, data_source: FileDialogDataSource = ...) -> None:
        ...
class Image(Widget):
    url: str
    def __init__(self, url: str = '', width: int = 0, height: int = 0) -> None:
        ...
class Label(Widget):
    """
    
                Label Widget.
    
                Displays non-editable text.
    
                Args:
                    text (str, default=""): Text to display.
            
    """
    text: str
    def __init__(self, text: str = '', useclipboard: bool = False, clippingmode: ClippingType = ..., font_style: omni.ui._ui.FontStyle = ...) -> None:
        ...
    def reset_text_color(self) -> None:
        ...
    def set_clicked_fn(self, arg0: typing.Callable[[Widget], None]) -> None:
        ...
    def set_text_color(self, arg0: carb._carb.ColorRgba) -> None:
        ...
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class Length:
    """
    
            Length.
    
            Represents any length as a value and unit type.
    
            Examples:
    
            >>> l1 = omni.kit.ui.Length(250, omni.kit.ui.UnitType.PIXEL)
            >>> l2 = omni.kit.ui.Pixel(250)
            >>> l3 = omni.kit.ui.Percent(30)
    
            `l1` and `l2` represent the same value: 250 in pixels.
            `l3` is 30%.
    
            
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: ...) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def unit(self) -> ...:
        """
        (:obj:`.UnitType.`) Unit.
        """
    @unit.setter
    def unit(self, arg0: ...) -> None:
        ...
    @property
    def value(self) -> float:
        """
        (float) Value
        """
    @value.setter
    def value(self, arg0: float) -> None:
        ...
class ListBox(Label):
    """
    
                ListBox Widget.
    
                Args:
                    text (str, default=""): Text on label.
                    multi_select (bool, default=True): Multi selection enabled.
                    item_height_count (int, default=-1): Height in items.
                    items (List[str], default=[]): List of elements.
            
    """
    item_height_count: int
    multi_select: bool
    def __init__(self, text: str = '', multi_select: bool = True, item_height_count: int = -1, items: list[str] = []) -> None:
        ...
    def add_item(self, arg0: str) -> None:
        ...
    def clear_items(self) -> None:
        ...
    def clear_selection(self) -> None:
        ...
    def get_item_at(self, arg0: int) -> str:
        ...
    def get_item_count(self) -> int:
        ...
    def get_selected(self) -> list[int]:
        ...
    def remove_item(self, arg0: int) -> None:
        ...
    def set_selected(self, arg0: int, arg1: bool) -> None:
        ...
    def set_selection_changed_fn(self, arg0: typing.Callable[[Widget], None]) -> None:
        ...
class Mat44:
    """
    """
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: Mat44) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Mat44) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __str__(self) -> str:
        ...
    def get_row(self, arg0: int) -> carb._carb.Double4:
        ...
    def set_row(self, arg0: int, arg1: carb._carb.Double4) -> carb._carb.Double4:
        ...
class Menu(Widget):
    """
    
                Menu.
            
    """
    static_class: typing.ClassVar[omni.kit.ui.editor_menu.EditorMenu]  # value = <omni.kit.ui.editor_menu.EditorMenu object>
    @staticmethod
    def get_editor_menu():
        ...
    @staticmethod
    def using_legacy_mode():
        ...
    def __init__(self) -> None:
        ...
    def add_item(self, menu_path: str, on_click: typing.Callable[[str, bool], None] = None, toggle: bool = False, priority: int = 0, value: bool = False, enabled: bool = True, original_svg_color: bool = False, auto_release: bool = True) -> carb._carb.Subscription:
        ...
    def add_item_attached(self, *args, **kwargs):
        ...
    def get_item_count(self) -> int:
        ...
    def get_items(self) -> list[str]:
        ...
    def get_value(self, arg0: str) -> bool:
        ...
    def has_item(self, arg0: str) -> bool:
        ...
    def remove_item(self, arg0: str) -> None:
        ...
    def set_action(self, arg0: str, arg1: str, arg2: str) -> None:
        ...
    def set_enabled(self, arg0: str, arg1: bool) -> None:
        ...
    def set_hotkey(self, menu_path: str, modifier: int, key: int) -> None:
        """
                    Set menu hotkey.
        
                    Args:
                        menu_path (str): Path to menu item.
                        modifier(int): Keyboard modifier from :mod:`carb.input`.
                        key(int): Keyboard key code from :class:`carb.input.KeyboardInput`.
        """
    def set_on_click(self, menu_path: str, on_click: typing.Callable[[str, bool], None] = None) -> None:
        ...
    def set_on_right_click(self, menu_path: str, on_click: typing.Callable[[str, bool], None] = None) -> None:
        ...
    def set_priority(self, arg0: str, arg1: int) -> None:
        ...
    def set_value(self, arg0: str, arg1: bool) -> None:
        ...
class MenuEventType:
    """
    
            menu operation results.
            
    
    Members:
    
      ACTIVATE
    """
    ACTIVATE: typing.ClassVar[MenuEventType]  # value = <MenuEventType.ACTIVATE: 0>
    __members__: typing.ClassVar[dict[str, MenuEventType]]  # value = {'ACTIVATE': <MenuEventType.ACTIVATE: 0>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Model:
    def __init__(self) -> None:
        ...
    def get_type(self, arg0: str, arg1: str) -> ModelNodeType:
        ...
    def signal_change(self, path: str, meta: str = '', type: ModelEventType = ..., sender: int = 0) -> None:
        ...
class ModelChangeInfo:
    sender: int
    transient: bool
    def __init__(self) -> None:
        ...
class ModelEventType:
    """
    Model event types.
    
    Members:
    
      NODE_ADD
    
      NODE_REMOVE
    
      NODE_TYPE_CHANGE
    
      NODE_VALUE_CHANGE
    """
    NODE_ADD: typing.ClassVar[ModelEventType]  # value = <ModelEventType.NODE_ADD: 0>
    NODE_REMOVE: typing.ClassVar[ModelEventType]  # value = <ModelEventType.NODE_REMOVE: 1>
    NODE_TYPE_CHANGE: typing.ClassVar[ModelEventType]  # value = <ModelEventType.NODE_TYPE_CHANGE: 2>
    NODE_VALUE_CHANGE: typing.ClassVar[ModelEventType]  # value = <ModelEventType.NODE_VALUE_CHANGE: 3>
    __members__: typing.ClassVar[dict[str, ModelEventType]]  # value = {'NODE_ADD': <ModelEventType.NODE_ADD: 0>, 'NODE_REMOVE': <ModelEventType.NODE_REMOVE: 1>, 'NODE_TYPE_CHANGE': <ModelEventType.NODE_TYPE_CHANGE: 2>, 'NODE_VALUE_CHANGE': <ModelEventType.NODE_VALUE_CHANGE: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ModelNodeType:
    """
    Model node types.
    
    Members:
    
      UNKNOWN
    
      OBJECT
    
      ARRAY
    
      STRING
    
      BOOL
    
      NUMBER
    """
    ARRAY: typing.ClassVar[ModelNodeType]  # value = <ModelNodeType.ARRAY: 2>
    BOOL: typing.ClassVar[ModelNodeType]  # value = <ModelNodeType.BOOL: 4>
    NUMBER: typing.ClassVar[ModelNodeType]  # value = <ModelNodeType.NUMBER: 5>
    OBJECT: typing.ClassVar[ModelNodeType]  # value = <ModelNodeType.OBJECT: 1>
    STRING: typing.ClassVar[ModelNodeType]  # value = <ModelNodeType.STRING: 3>
    UNKNOWN: typing.ClassVar[ModelNodeType]  # value = <ModelNodeType.UNKNOWN: 0>
    __members__: typing.ClassVar[dict[str, ModelNodeType]]  # value = {'UNKNOWN': <ModelNodeType.UNKNOWN: 0>, 'OBJECT': <ModelNodeType.OBJECT: 1>, 'ARRAY': <ModelNodeType.ARRAY: 2>, 'STRING': <ModelNodeType.STRING: 3>, 'BOOL': <ModelNodeType.BOOL: 4>, 'NUMBER': <ModelNodeType.NUMBER: 5>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ModelWidget(Widget):
    """
    
                Model Widget.
            
    """
    def get_model(self) -> Model:
        ...
    def get_model_root(self) -> str:
        ...
    def get_model_stream(self) -> carb.events._events.IEventStream:
        ...
    def set_model(self, model: Model, root: str = '', isTimeSampled: bool = False, value: float = -1.0) -> None:
        ...
    @property
    def is_time_sampled_widget(self) -> bool:
        ...
    @property
    def time_code(self) -> float:
        ...
class Percent(Length):
    """
    Convenience class to express :class:`.Length` in percents.
    """
    def __init__(self, arg0: float) -> None:
        ...
class Pixel(Length):
    """
    Convenience class to express :class:`.Length` in pixels.
    """
    def __init__(self, arg0: float) -> None:
        ...
class Popup:
    height: float
    layout: Container
    pos: carb._carb.Float2
    title: str
    width: float
    def __init__(self, title: str, modal: bool = False, width: float = 0.0, height: float = 0.0, auto_resize: bool = False) -> None:
        ...
    def hide(self) -> None:
        ...
    def is_visible(self) -> bool:
        ...
    def set_close_fn(self, arg0: typing.Callable[[], None]) -> None:
        ...
    def set_update_fn(self, arg0: typing.Callable[[float], None]) -> None:
        ...
    def show(self) -> None:
        ...
class ProgressBar(Widget):
    """
    
                ProgressBar Widget.
    
                Displays a progress bar.
    
                Args:
                    width (:class:`.Length`): Width.
                    height (:class:`.Length`, default=omni.kit.ui.Pixel(0)): Height.
            
    """
    overlay: str
    progress: float
    @typing.overload
    def __init__(self, width: Length, height: Length = ...) -> None:
        ...
    @typing.overload
    def __init__(self, width: float) -> None:
        ...
    def set_progress(self, value: float, text: str = None) -> None:
        ...
class RowColumnLayout(Container):
    def __init__(self, column_count: int, borders: bool = False) -> None:
        ...
    def get_column_width(self, arg0: int) -> Length:
        ...
    def set_column_width(self, index: int, val: typing.Any, min: float = 0.0, max: float = 0.0) -> None:
        """
                        Set column width.
        
                        Args:
                            index: column index.
                            val: width value. Should be either a :class:`.Length` or `float` (treated as :class:`.Pixel` length).
        """
class RowLayout(Container):
    def __init__(self) -> None:
        ...
class ScalarXYZ(ValueWidgetDouble3):
    """
    
                ScalarXYZ Widget.
    
                If `min` >= `max` widget value has no bound.
    
                Args:
                    format_string (str, default="%0.1f"): Format string.
                    drag_speed (float, default=1.0): Drag speed.
                    value_wrap (float, default=0.0): Value wrap.
                    min (double, default=0.0): Lower value limit.
                    max (double, default=0.0): Upper value limit.
                    value (Tuple[double, double, double], default=(0, 0, 0)): Initial value.
            
    """
    def __init__(self, format_string: str = '%0.1f', drag_speed: float = 1.0, wrap_value: float = 0.0, min: float = 0.0, max: float = 0.0, dead_zone: float = 0.0, value: carb._carb.Double3 = ...) -> None:
        ...
    def skip_ypos_update(self, arg0: bool) -> None:
        ...
class ScalarXYZW(ValueWidgetDouble4):
    """
    
                ScalarXYZW Widget.
    
                If `min` >= `max` widget value has no bound.
    
                Args:
                    format_string (str, default="%0.1f"): Format string.
                    drag_speed (float, default=1.0): Drag speed.
                    value_wrap (float, default=0.0): Value wrap.
                    min (double, default=0.0): Lower value limit.
                    max (double, default=0.0): Upper value limit.
                    value (Tuple[double, double, double, double], default=(0, 0, 0, 0)): Initial value.
            
    """
    def __init__(self, format_string: str = '%0.1f', drag_speed: float = 1.0, wrap_value: float = 0.0, min: float = 0.0, max: float = 0.0, value: carb._carb.Double4 = ...) -> None:
        ...
class ScrollingFrame(Container):
    def __init__(self, arg0: str, arg1: float, arg2: float) -> None:
        ...
    def scroll_to(self, arg0: float) -> None:
        ...
class Separator(Widget):
    """
    
                Separator.
    
                Separator UI element.
            
    """
    def __init__(self) -> None:
        ...
class SimpleTreeView(Widget):
    """
    
                SimpleTreeView Widget.
    
                Args:
                    items (List[str], default=[]): List of string as the source of the Tree hierarchy.
                    separator(str, default='/'): A string separator to parse the strings into tree node tokens
            
    """
    def __init__(self, items: list[str] = [], separator: str = '/') -> None:
        ...
    def clear_selection(self) -> None:
        ...
    def get_selected_item_name(self) -> str:
        ...
    def set_clicked_fn(self, arg0: typing.Callable[[Widget], None]) -> None:
        ...
    def set_tree_data(self, arg0: list[str]) -> None:
        ...
class SimpleValueWidgetBool(ValueWidgetBool):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SimpleValueWidgetColorRgb(ValueWidgetColorRgb):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SimpleValueWidgetColorRgba(ValueWidgetColorRgba):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SimpleValueWidgetDouble(ValueWidgetDouble):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SimpleValueWidgetDouble2(ValueWidgetDouble2):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SimpleValueWidgetDouble3(ValueWidgetDouble3):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SimpleValueWidgetDouble4(ValueWidgetDouble4):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SimpleValueWidgetInt(ValueWidgetInt):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SimpleValueWidgetInt2(ValueWidgetInt2):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SimpleValueWidgetMat44(ValueWidgetMat44):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SimpleValueWidgetString(ValueWidgetString):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SimpleValueWidgetUint(ValueWidgetUint):
    """
    
                Model Widget with single value for simple controls.
            
    """
    left_handed: bool
    text: str
    @property
    def tooltip(self) -> Widget:
        """
        Widget to be shown when mouse is over the Widget as a tooltip.
        """
    @tooltip.setter
    def tooltip(self, arg0: Widget) -> None:
        ...
class SliderDouble(SimpleValueWidgetDouble):
    """
    
                Slider Widget (double).
    
                Args:
                    text (str, default=""): Text on label.
                    value (double, default=0): Initial value.
                    min (double, default=0): Lower value limit.
                    max (double, default=100): Upper value limit.
            
    """
    format: str
    max: float
    min: float
    power: float
    def __init__(self, text: str = '', value: float = 0.0, min: float = 0, max: float = 100) -> None:
        ...
class SliderDouble2(SimpleValueWidgetDouble2):
    """
    
                Slider Widget (Tuple[double, double]).
    
                Args:
                    text (str, default=""): Text on label.
                    value (Tuple[double, double], default=0): Initial value.
                    min (Tuple[double, double], default=0): Lower value limit.
                    max (Tuple[double, double], default=100): Upper value limit.
            
    """
    format: str
    max: float
    min: float
    power: float
    def __init__(self, text: str = '', value: carb._carb.Double2 = ..., min: float = 0, max: float = 100) -> None:
        ...
class SliderDouble3(SimpleValueWidgetDouble3):
    """
    
                Slider Widget (Tuple[double, double, double]).
    
                Args:
                    text (str, default=""): Text on label.
                    value (Tuple[double, double, double], default=0): Initial value.
                    min (Tuple[double, double, double], default=0): Lower value limit.
                    max (Tuple[double, double, double], default=100): Upper value limit.
            
    """
    format: str
    max: float
    min: float
    power: float
    def __init__(self, text: str = '', value: carb._carb.Double3 = ..., min: float = 0, max: float = 100) -> None:
        ...
class SliderDouble4(SimpleValueWidgetDouble4):
    """
    
                Slider Widget (Tuple[double, double, double, double]).
    
                Args:
                    text (str, default=""): Text on label.
                    value (Tuple[double, double, double, double], default=0): Initial value.
                    min (Tuple[double, double, double, double], default=0): Lower value limit.
                    max (Tuple[double, double, double, double], default=100): Upper value limit.
            
    """
    format: str
    max: float
    min: float
    power: float
    def __init__(self, text: str = '', value: carb._carb.Double4 = ..., min: float = 0, max: float = 100) -> None:
        ...
class SliderInt(SimpleValueWidgetInt):
    """
    
                Slider Widget (int).
    
                Args:
                    text (str, default=""): Text on label.
                    value (int, default=0): Initial value.
                    min (int, default=0): Lower value limit.
                    max (int, default=100): Upper value limit.
            
    """
    format: str
    max: int
    min: int
    power: float
    def __init__(self, text: str = '', value: int = 0, min: int = 0, max: int = 100) -> None:
        ...
class SliderInt2(SimpleValueWidgetInt2):
    """
    
                Slider Widget (Tuple[int, int]).
    
                Args:
                    text (str, default=""): Text on label.
                    value (Tuple[int, int], default=0): Initial value.
                    min (Tuple[int, int], default=0): Lower value limit.
                    max (Tuple[int, int], default=100): Upper value limit.
            
    """
    format: str
    max: int
    min: int
    power: float
    def __init__(self, text: str = '', value: carb._carb.Int2 = ..., min: int = 0, max: int = 100) -> None:
        ...
class SliderUInt(SimpleValueWidgetUint):
    """
    
                Slider Widget (uint32_t).
    
                Args:
                    text (str, default=""): Text on label.
                    value (uint32_t, default=0): Initial value.
                    min (uint32_t, default=0): Lower value limit.
                    max (uint32_t, default=100): Upper value limit.
            
    """
    format: str
    max: int
    min: int
    power: float
    def __init__(self, text: str = '', value: int = 0, min: int = 0, max: int = 100) -> None:
        ...
class Spacer(Widget):
    """
    
                Spacer.
    
                Dummy UI element to fill in space.
    
                Args:
                    width (:class:`.Length`): Width.
                    height (:class:`.Length`, default=omni.kit.ui.Pixel(0)): Height.
            
    """
    @typing.overload
    def __init__(self, width: Length, height: Length = ...) -> None:
        ...
    @typing.overload
    def __init__(self, width: float) -> None:
        ...
class TextBox(ValueWidgetString):
    """
    
                TextBox Widget.
    
                Displays editable text.
    
                Args:
                    value (str, default=""): Initial text.
            
    """
    readonly: bool
    show_background: bool
    text: str
    @typing.overload
    def __init__(self, value: str = '', hint: str = '', change_on_enter: bool = False) -> None:
        ...
    @typing.overload
    def __init__(self, value: str = '', change_on_enter: bool = False) -> None:
        ...
    def reset_text_color(self) -> None:
        ...
    def set_list_suggestions_fn(self, arg0: typing.Callable[[Widget, str], list[str]]) -> None:
        ...
    def set_text_changed_fn(self, arg0: typing.Callable[[Widget], None]) -> None:
        ...
    def set_text_color(self, arg0: carb._carb.ColorRgba) -> None:
        ...
    def set_text_finalized_fn(self, arg0: typing.Callable[[Widget], None]) -> None:
        ...
    def text_width(self) -> float:
        ...
    @property
    def clipping_mode(self, arg1: ClippingType) -> ClippingType:
        ...
    @clipping_mode.setter
    def clipping_mode(self, arg1: ClippingType) -> None:
        ...
class Transform(ValueWidgetMat44):
    def __init__(self, position_format_string: str = '%0.1f', position_drag_speed: float = 1.0, position_wrap_value: float = 0.0, position_min: float = 0.0, position_max: float = 0.0, rotation_format_string: str = '%0.1f', rotation_drag_speed: float = 1.0, rotation_wrap_value: float = 0.0, rotation_min: float = 0.0, rotation_max: float = 0.0) -> None:
        ...
class UnitType:
    """
    
                Unit types.
    
                Widths, heights or other UI length can be specified in pixels or relative to window (or child window) size.
            
    
    Members:
    
      PIXEL
    
      PERCENT
    """
    PERCENT: typing.ClassVar[UnitType]  # value = <UnitType.PERCENT: 1>
    PIXEL: typing.ClassVar[UnitType]  # value = <UnitType.PIXEL: 0>
    __members__: typing.ClassVar[dict[str, UnitType]]  # value = {'PIXEL': <UnitType.PIXEL: 0>, 'PERCENT': <UnitType.PERCENT: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ValueWidgetBool(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[bool], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetBool], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> bool:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: bool) -> None:
        ...
class ValueWidgetColorRgb(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[carb._carb.ColorRgb], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetColorRgb], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> carb._carb.ColorRgb:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: carb._carb.ColorRgb) -> None:
        ...
class ValueWidgetColorRgba(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[carb._carb.ColorRgba], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetColorRgba], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> carb._carb.ColorRgba:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: carb._carb.ColorRgba) -> None:
        ...
class ValueWidgetDouble(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[float], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetDouble], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> float:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: float) -> None:
        ...
class ValueWidgetDouble2(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[carb._carb.Double2], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetDouble2], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> carb._carb.Double2:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: carb._carb.Double2) -> None:
        ...
class ValueWidgetDouble3(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[carb._carb.Double3], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetDouble3], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> carb._carb.Double3:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: carb._carb.Double3) -> None:
        ...
class ValueWidgetDouble4(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[carb._carb.Double4], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetDouble4], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> carb._carb.Double4:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: carb._carb.Double4) -> None:
        ...
class ValueWidgetInt(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[int], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetInt], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> int:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: int) -> None:
        ...
class ValueWidgetInt2(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[carb._carb.Int2], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetInt2], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> carb._carb.Int2:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: carb._carb.Int2) -> None:
        ...
class ValueWidgetMat44(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[Mat44], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetMat44], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> Mat44:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: Mat44) -> None:
        ...
class ValueWidgetString(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[str], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetString], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> str:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: str) -> None:
        ...
class ValueWidgetUint(ModelWidget):
    """
    
                Model Widget with single value.
            
    """
    def get_value_ambiguous(self) -> bool:
        ...
    def set_on_changed_fn(self, fn: typing.Callable[[int], None]) -> None:
        """
        Set a callback function to be called when value changes.
        
        Args:
            fn: Function to be called when value changes. New value is passed into the function.
        """
    def set_on_right_click_fn(self, fn: typing.Callable[[ValueWidgetUint], None]) -> None:
        """
        Set a callback function to be called when right mouse button is clicked.
        
        Args:
            fn: Function to be called when right mouse button is clicked. ValueWidget is passed into the function.
        """
    def set_value_ambiguous(self, arg0: bool) -> None:
        ...
    @property
    def value(self) -> int:
        """
        : Widget value property.
        """
    @value.setter
    def value(self, arg1: int) -> None:
        ...
class ViewCollapsing(ModelWidget):
    use_frame_background_color: bool
    def __init__(self, defaultOpen: bool, sort: bool = False) -> None:
        ...
    def set_filter(self, arg0: str) -> None:
        ...
class ViewFlat(ModelWidget):
    def __init__(self, sort: bool = False) -> None:
        ...
    def set_filter(self, arg0: str) -> int:
        ...
class ViewTreeGrid(ModelWidget):
    draw_table_header: bool
    is_root: bool
    text: str
    def __init__(self, default_open: bool, sort: bool = False, column_count: int = 1) -> None:
        ...
    def get_header_cell_widget(self, arg0: int) -> Widget:
        ...
    def set_build_cell_fn(self, arg0: typing.Callable[[Model, str, int, int], DelegateResult]) -> None:
        ...
    def set_header_cell_text(self, arg0: int, arg1: str) -> None:
        ...
    def set_header_cell_widget(self, arg0: int, arg1: Widget) -> None:
        ...
class Widget:
    """
    
                Widget.
    
                Base class for all UI elements.
    """
    enabled: bool
    font_style: omni.ui._ui.FontStyle
    visible: bool
    def get_font_size(self) -> float:
        ...
    def set_dragdrop_fn(self, arg0: typing.Callable[[Widget, str], None], arg1: str) -> None:
        ...
    def set_dragged_fn(self, arg0: typing.Callable[[Widget, ...], None]) -> None:
        ...
    @property
    def height(self) -> Length:
        """
        (:class:`.Length`, default=omni.kit.ui.Pixel(0)): Height.
        """
    @height.setter
    def height(self, arg1: typing.Any) -> None:
        ...
    @property
    def user_data(self) -> dict:
        """
        :class:`dict` with additional user data attached to widget. Lifetime of it depends on lifetime of the widget.
        """
    @user_data.setter
    def user_data(self, arg1: dict) -> None:
        ...
    @property
    def width(self) -> Length:
        """
        (:class:`.Length`, default=omni.kit.ui.Pixel(0)): Width.
        """
    @width.setter
    def width(self, arg1: typing.Any) -> None:
        ...
class Window:
    """
    
            UI Window.
    
            Window is a starting point for every new UI. It contains a :class:`.Container`, which can contain other :class:`.Widget`'s.
    
            Args:
                title (str): The title to be displayed on window title bar.
                width (int, default=640): Window width in pixels.
                height (int, default=480): Window height in pixels.
                open (bool, default=True): Is window opened when created.
                add_to_menu (bool, default=True): Create main menu item with this window in the Kit.
                menu_path (str, default=""): Menu path if add_to_menu is True. If empty string is passed it is added under "Extensions" menu item.
                is_toggle_menu (bool, default=True): Can menu item be toggled?
                dock (:obj:`omni.ui.DockPreference`, default=LEFT_BOTTOM): Docking preference for a window, see :class:`.DockPreference`
                flags (:obj:`omni.kit.ui.Window`, default=NONE): flags for a window, see :class:`.Window`
            
    """
    flags: int
    height: int
    layout: Container
    width: int
    @staticmethod
    def create_window_hook(*args, **kwargs):
        """
        __init__(self: omni.kit.ui._ui.Window, title: str, width: int = 640, height: int = 480, open: bool = True, add_to_menu: bool = True, menu_path: str = '', is_toggle_menu: bool = True, dock: omni.kit.ui._ui.DockPreference = <DockPreference.LEFT_BOTTOM: 6>, flags: int = 0) -> None
        """
    def __init__(self, title: str, *args, **kwargs):
        ...
    def hide(self) -> None:
        ...
    def is_modal(self) -> bool:
        ...
    def is_visible(self) -> bool:
        ...
    def set_alpha(self, arg0: float) -> None:
        ...
    def set_size(self, arg0: int, arg1: int) -> None:
        ...
    def set_update_fn(self, arg0: typing.Callable[[float], None]) -> None:
        ...
    def set_visibility_changed_fn(self, arg0: typing.Callable[[bool], None]) -> None:
        ...
    def show(self) -> None:
        ...
    def title(self) -> str:
        ...
    @property
    def event_stream(self) -> carb.events._events.IEventStream:
        """
        Event stream with events of type: :class:`.WindowEventType`
        """
    @property
    def menu(self) -> ...:
        """
        Window optional menu bar.
        """
    @menu.setter
    def menu(self, arg0: ...) -> None:
        ...
    @property
    def mouse_pos(self) -> carb._carb.Float2:
        ...
class WindowEventType:
    """
    Members:
    
      VISIBILITY_CHANGE
    
      UPDATE
    """
    UPDATE: typing.ClassVar[WindowEventType]  # value = <WindowEventType.UPDATE: 1>
    VISIBILITY_CHANGE: typing.ClassVar[WindowEventType]  # value = <WindowEventType.VISIBILITY_CHANGE: 0>
    __members__: typing.ClassVar[dict[str, WindowEventType]]  # value = {'VISIBILITY_CHANGE': <WindowEventType.VISIBILITY_CHANGE: 0>, 'UPDATE': <WindowEventType.UPDATE: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class WindowMainStandalone(Container):
    """
    """
    def __init__(self) -> None:
        ...
class WindowStandalone(ContainerBase):
    """
    
            UI Window.
    
            Window is a starting point for every new UI. It contains a :class:`.Container`, which can contain other :class:`.Widget`'s.
    
            Args:
                title (str): The title to be displayed on window title bar.
                width (int, default=640): Window width in pixels.
                height (int, default=480): Window height in pixels.
                open (bool, default=True): Is window opened when created.
                add_to_menu (bool, default=True): Create main menu item with this window in the Kit.
                menu_path (str, default=""): Menu path if add_to_menu is True. If empty string is passed it is added under "Extensions" menu item.
                is_toggle_menu (bool, default=True): Can menu item be toggled?
                dock (:obj:`omni.ui.DockPreference`, default=LEFT_BOTTOM): Docking preference for a window, see :class:`.DockPreference`
                flags (:obj:`omni.kit.ui.Window`, default=NONE): flags for a window, see :class:`.Window`
            
    """
    flags: int
    height: int
    layout: Container
    width: int
    def __init__(self, title: str, width: int = 640, height: int = 480, open: bool = True, add_to_menu: bool = True, menu_path: str = '', is_toggle_menu: bool = True, dock: DockPreference = ..., flags: int = 0) -> None:
        ...
    def hide(self) -> None:
        ...
    def is_visible(self) -> bool:
        ...
    def set_alpha(self, arg0: float) -> None:
        ...
    def set_size(self, arg0: int, arg1: int) -> None:
        ...
    def set_update_fn(self, arg0: typing.Callable[[float], None]) -> None:
        ...
    def set_visibility_changed_fn(self, arg0: typing.Callable[[bool], None]) -> None:
        ...
    def show(self) -> None:
        ...
    @property
    def event_stream(self) -> carb.events._events.IEventStream:
        """
        Event stream with events of type: :class:`.WindowEventType`
        """
    @property
    def menu(self) -> ...:
        """
        Window optional menu bar.
        """
    @menu.setter
    def menu(self, arg0: ...) -> None:
        ...
    @property
    def mouse_pos(self) -> carb._carb.Float2:
        ...
def activate_menu_item(arg0: str) -> None:
    ...
def get_custom_glyph_code(file_path: str, font_style: omni.ui._ui.FontStyle = ...) -> str:
    """
                Get glyph code.
    
                Args:
                    file_path (str): Path to svg file
                    font_style(:class:`.FontStyle`): font style to use.
    """
def get_editor_menu_legacy() -> Menu:
    ...
def get_main_window() -> ...:
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
