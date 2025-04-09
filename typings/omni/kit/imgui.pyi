"""
pybind11 carb.imgui bindings
"""
from __future__ import annotations
import carb._carb
import typing
__all__ = ['Condition', 'Context', 'ImGui', 'MouseCursor', 'Style', 'StyleColor', 'StyleColorsPreset', 'StyleVar', 'WINDOW_FLAG_ALWAYS_AUTO_RESIZE', 'WINDOW_FLAG_ALWAYS_HORIZONTAL_SCROLLBAR', 'WINDOW_FLAG_ALWAYS_USE_WINDOW_PADDING', 'WINDOW_FLAG_ALWAYS_VERTICAL_SCROLLBAR', 'WINDOW_FLAG_HORIZONTAL_SCROLLBAR', 'WINDOW_FLAG_MENU_BAR', 'WINDOW_FLAG_NO_BACKGROUND', 'WINDOW_FLAG_NO_BRING_TO_FRONT_ON_FOCUS', 'WINDOW_FLAG_NO_COLLAPSE', 'WINDOW_FLAG_NO_DOCKING', 'WINDOW_FLAG_NO_FOCUS_ON_APPEARING', 'WINDOW_FLAG_NO_MOUSE_INPUTS', 'WINDOW_FLAG_NO_MOVE', 'WINDOW_FLAG_NO_NAV_FOCUS', 'WINDOW_FLAG_NO_NAV_INPUTS', 'WINDOW_FLAG_NO_RESIZE', 'WINDOW_FLAG_NO_SAVED_SETTINGS', 'WINDOW_FLAG_NO_SCROLLBAR', 'WINDOW_FLAG_NO_SCROLL_WITH_MOUSE', 'WINDOW_FLAG_NO_TITLE_BAR', 'WINDOW_FLAG_UNSAVED_DOCUMENT', 'acquire_imgui']
class Condition:
    """
    Members:
    
      ALWAYS
    
      APPEARING
    
      FIRST_USE_EVER
    
      ONCE
    """
    ALWAYS: typing.ClassVar[Condition]  # value = <Condition.ALWAYS: 1>
    APPEARING: typing.ClassVar[Condition]  # value = <Condition.APPEARING: 8>
    FIRST_USE_EVER: typing.ClassVar[Condition]  # value = <Condition.FIRST_USE_EVER: 4>
    ONCE: typing.ClassVar[Condition]  # value = <Condition.ONCE: 2>
    __members__: typing.ClassVar[dict[str, Condition]]  # value = {'ALWAYS': <Condition.ALWAYS: 1>, 'APPEARING': <Condition.APPEARING: 8>, 'FIRST_USE_EVER': <Condition.FIRST_USE_EVER: 4>, 'ONCE': <Condition.ONCE: 2>}
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
class Context:
    pass
class ImGui:
    def begin(self, arg0: str, arg1: bool, arg2: int) -> tuple:
        ...
    def begin_child(self, arg0: str, arg1: carb._carb.Float2, arg2: bool, arg3: int) -> bool:
        ...
    def begin_popup_modal(self, arg0: str, arg1: bool, arg2: int) -> bool:
        ...
    def bullet(self) -> None:
        ...
    def button(self, arg0: str) -> bool:
        ...
    def checkbox(self, arg0: str, arg1: bool) -> tuple:
        ...
    def close_current_popup(self) -> None:
        ...
    def collapsing_header(self, arg0: str, arg1: int) -> bool:
        ...
    def color_edit3(self, arg0: str, arg1: carb._carb.Float3) -> tuple:
        ...
    def color_edit4(self, arg0: str, arg1: carb._carb.Float4) -> tuple:
        ...
    def combo(self, arg0: str, arg1: int, arg2: list[str]) -> tuple:
        ...
    def dock_builder_dock_window(self, arg0: str, arg1: int) -> None:
        ...
    def dummy(self, arg0: carb._carb.Float2) -> None:
        ...
    def end(self) -> None:
        ...
    def end_child(self) -> None:
        ...
    def end_popup(self) -> None:
        ...
    def get_display_size(self) -> carb._carb.Float2:
        ...
    def get_mouse_cursor(self) -> MouseCursor:
        ...
    def get_style(self) -> Style:
        ...
    def indent(self, arg0: float) -> None:
        ...
    def input_float(self, arg0: str, arg1: float, arg2: float) -> tuple:
        ...
    def input_int(self, arg0: str, arg1: int, arg2: int) -> tuple:
        ...
    def input_text(self, arg0: str, arg1: str, arg2: int) -> tuple:
        ...
    def is_valid(self) -> bool:
        ...
    def menu_item_ex(self, arg0: str, arg1: str, arg2: bool, arg3: bool) -> tuple:
        ...
    def open_popup(self, arg0: str) -> None:
        ...
    def plot_lines(self, arg0: str, arg1: list[float], arg2: int, arg3: int, arg4: str, arg5: float, arg6: float, arg7: carb._carb.Float2, arg8: int) -> None:
        ...
    def pop_id(self) -> None:
        ...
    def pop_item_width(self) -> None:
        ...
    def pop_style_color(self) -> None:
        ...
    def pop_style_var(self) -> None:
        ...
    def progress_bar(self, arg0: float, arg1: carb._carb.Float2, arg2: str) -> None:
        ...
    def push_id_int(self, arg0: int) -> None:
        ...
    def push_id_string(self, arg0: str) -> None:
        ...
    def push_item_width(self, arg0: float) -> None:
        ...
    def push_style_color(self, arg0: StyleColor, arg1: carb._carb.Float4) -> None:
        ...
    def push_style_var_float(self, arg0: StyleVar, arg1: float) -> None:
        ...
    def push_style_var_float2(self, arg0: StyleVar, arg1: carb._carb.Float2) -> None:
        ...
    def same_line(self) -> None:
        ...
    def same_line_ex(self, pos_x: float = 0.0, spacing_w: float = -1.0) -> None:
        ...
    def separator(self) -> None:
        ...
    def set_display_size(self, arg0: carb._carb.Float2) -> None:
        ...
    def set_mouse_cursor(self, arg0: MouseCursor) -> None:
        ...
    def set_next_window_pos(self, arg0: carb._carb.Float2, arg1: Condition, arg2: carb._carb.Float2) -> None:
        ...
    def set_next_window_size(self, arg0: carb._carb.Float2, arg1: Condition) -> None:
        ...
    def set_scroll_here_y(self, arg0: float) -> None:
        ...
    def set_style_colors(self, arg0: Style, arg1: StyleColorsPreset) -> None:
        ...
    def show_demo_window(self, arg0: bool) -> None:
        ...
    def show_style_editor(self, arg0: Style) -> None:
        ...
    def slider_float(self, arg0: str, arg1: float, arg2: float, arg3: float) -> tuple:
        ...
    def slider_int(self, arg0: str, arg1: int, arg2: int, arg3: int) -> tuple:
        ...
    def small_button(self, arg0: str) -> bool:
        ...
    def spacing(self) -> None:
        ...
    def text(self, arg0: str) -> None:
        ...
    def text_unformatted(self, arg0: str) -> None:
        ...
    def text_wrapped(self, arg0: str) -> None:
        ...
    def tree_node_ptr(self, arg0: int, arg1: str) -> bool:
        ...
    def tree_pop(self) -> None:
        ...
    def unindent(self, arg0: float) -> None:
        ...
class MouseCursor:
    """
    Members:
    
      NONE
    
      ARROW
    
      TEXT_INPUT
    
      RESIZE_ALL
    
      RESIZE_NS
    
      RESIZE_EW
    
      RESIZE_NESW
    
      RESIZE_NWSE
    
      HAND
    
      NOT_ALLOWED
    
      CROSSHAIR
    """
    ARROW: typing.ClassVar[MouseCursor]  # value = <MouseCursor.ARROW: 0>
    CROSSHAIR: typing.ClassVar[MouseCursor]  # value = <MouseCursor.CROSSHAIR: 9>
    HAND: typing.ClassVar[MouseCursor]  # value = <MouseCursor.HAND: 7>
    NONE: typing.ClassVar[MouseCursor]  # value = <MouseCursor.NONE: -1>
    NOT_ALLOWED: typing.ClassVar[MouseCursor]  # value = <MouseCursor.NOT_ALLOWED: 8>
    RESIZE_ALL: typing.ClassVar[MouseCursor]  # value = <MouseCursor.RESIZE_ALL: 2>
    RESIZE_EW: typing.ClassVar[MouseCursor]  # value = <MouseCursor.RESIZE_EW: 4>
    RESIZE_NESW: typing.ClassVar[MouseCursor]  # value = <MouseCursor.RESIZE_NESW: 5>
    RESIZE_NS: typing.ClassVar[MouseCursor]  # value = <MouseCursor.RESIZE_NS: 3>
    RESIZE_NWSE: typing.ClassVar[MouseCursor]  # value = <MouseCursor.RESIZE_NWSE: 6>
    TEXT_INPUT: typing.ClassVar[MouseCursor]  # value = <MouseCursor.TEXT_INPUT: 1>
    __members__: typing.ClassVar[dict[str, MouseCursor]]  # value = {'NONE': <MouseCursor.NONE: -1>, 'ARROW': <MouseCursor.ARROW: 0>, 'TEXT_INPUT': <MouseCursor.TEXT_INPUT: 1>, 'RESIZE_ALL': <MouseCursor.RESIZE_ALL: 2>, 'RESIZE_NS': <MouseCursor.RESIZE_NS: 3>, 'RESIZE_EW': <MouseCursor.RESIZE_EW: 4>, 'RESIZE_NESW': <MouseCursor.RESIZE_NESW: 5>, 'RESIZE_NWSE': <MouseCursor.RESIZE_NWSE: 6>, 'HAND': <MouseCursor.HAND: 7>, 'NOT_ALLOWED': <MouseCursor.NOT_ALLOWED: 8>, 'CROSSHAIR': <MouseCursor.CROSSHAIR: 9>}
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
class Style:
    pass
class StyleColor:
    """
    Members:
    
      Text
    
      TextDisabled
    
      WindowBg
    
      ChildBg
    
      PopupBg
    
      Border
    
      BorderShadow
    
      FrameBg
    
      FrameBgHovered
    
      FrameBgActive
    
      TitleBg
    
      TitleBgActive
    
      TitleBgCollapsed
    
      MenuBarBg
    
      ScrollbarBg
    
      ScrollbarGrab
    
      ScrollbarGrabHovered
    
      ScrollbarGrabActive
    
      CheckMark
    
      SliderGrab
    
      SliderGrabActive
    
      Button
    
      ButtonHovered
    
      ButtonActive
    
      Header
    
      HeaderHovered
    
      HeaderActive
    
      Separator
    
      SeparatorHovered
    
      SeparatorActive
    
      ResizeGrip
    
      ResizeGripHovered
    
      ResizeGripActive
    
      Tab
    
      TabHovered
    
      TabActive
    
      TabUnfocused
    
      TabUnfocusedActive
    
      DockingPreview
    
      DockingEmptyBg
    
      PlotLines
    
      PlotLinesHovered
    
      PlotHistogram
    
      PlotHistogramHovered
    
      TableHeaderBg
    
      TableBorderStrong
    
      TableBorderLight
    
      TableRowBg
    
      TableRowBgAlt
    
      TextSelectedBg
    
      DragDropTarget
    
      NavHighlight
    
      NavWindowingHighlight
    
      NavWindowingDimBg
    
      ModalWindowDimBg
    
      WindowShadow
    
      CustomText
    
      Count
    """
    Border: typing.ClassVar[StyleColor]  # value = <StyleColor.Border: 5>
    BorderShadow: typing.ClassVar[StyleColor]  # value = <StyleColor.BorderShadow: 6>
    Button: typing.ClassVar[StyleColor]  # value = <StyleColor.Button: 21>
    ButtonActive: typing.ClassVar[StyleColor]  # value = <StyleColor.ButtonActive: 23>
    ButtonHovered: typing.ClassVar[StyleColor]  # value = <StyleColor.ButtonHovered: 22>
    CheckMark: typing.ClassVar[StyleColor]  # value = <StyleColor.CheckMark: 18>
    ChildBg: typing.ClassVar[StyleColor]  # value = <StyleColor.ChildBg: 3>
    Count: typing.ClassVar[StyleColor]  # value = <StyleColor.Count: 57>
    CustomText: typing.ClassVar[StyleColor]  # value = <StyleColor.CustomText: 56>
    DockingEmptyBg: typing.ClassVar[StyleColor]  # value = <StyleColor.DockingEmptyBg: 39>
    DockingPreview: typing.ClassVar[StyleColor]  # value = <StyleColor.DockingPreview: 38>
    DragDropTarget: typing.ClassVar[StyleColor]  # value = <StyleColor.DragDropTarget: 50>
    FrameBg: typing.ClassVar[StyleColor]  # value = <StyleColor.FrameBg: 7>
    FrameBgActive: typing.ClassVar[StyleColor]  # value = <StyleColor.FrameBgActive: 9>
    FrameBgHovered: typing.ClassVar[StyleColor]  # value = <StyleColor.FrameBgHovered: 8>
    Header: typing.ClassVar[StyleColor]  # value = <StyleColor.Header: 24>
    HeaderActive: typing.ClassVar[StyleColor]  # value = <StyleColor.HeaderActive: 26>
    HeaderHovered: typing.ClassVar[StyleColor]  # value = <StyleColor.HeaderHovered: 25>
    MenuBarBg: typing.ClassVar[StyleColor]  # value = <StyleColor.MenuBarBg: 13>
    ModalWindowDimBg: typing.ClassVar[StyleColor]  # value = <StyleColor.ModalWindowDimBg: 54>
    NavHighlight: typing.ClassVar[StyleColor]  # value = <StyleColor.NavHighlight: 51>
    NavWindowingDimBg: typing.ClassVar[StyleColor]  # value = <StyleColor.NavWindowingDimBg: 53>
    NavWindowingHighlight: typing.ClassVar[StyleColor]  # value = <StyleColor.NavWindowingHighlight: 52>
    PlotHistogram: typing.ClassVar[StyleColor]  # value = <StyleColor.PlotHistogram: 42>
    PlotHistogramHovered: typing.ClassVar[StyleColor]  # value = <StyleColor.PlotHistogramHovered: 43>
    PlotLines: typing.ClassVar[StyleColor]  # value = <StyleColor.PlotLines: 40>
    PlotLinesHovered: typing.ClassVar[StyleColor]  # value = <StyleColor.PlotLinesHovered: 41>
    PopupBg: typing.ClassVar[StyleColor]  # value = <StyleColor.PopupBg: 4>
    ResizeGrip: typing.ClassVar[StyleColor]  # value = <StyleColor.ResizeGrip: 30>
    ResizeGripActive: typing.ClassVar[StyleColor]  # value = <StyleColor.ResizeGripActive: 32>
    ResizeGripHovered: typing.ClassVar[StyleColor]  # value = <StyleColor.ResizeGripHovered: 31>
    ScrollbarBg: typing.ClassVar[StyleColor]  # value = <StyleColor.ScrollbarBg: 14>
    ScrollbarGrab: typing.ClassVar[StyleColor]  # value = <StyleColor.ScrollbarGrab: 15>
    ScrollbarGrabActive: typing.ClassVar[StyleColor]  # value = <StyleColor.ScrollbarGrabActive: 17>
    ScrollbarGrabHovered: typing.ClassVar[StyleColor]  # value = <StyleColor.ScrollbarGrabHovered: 16>
    Separator: typing.ClassVar[StyleColor]  # value = <StyleColor.Separator: 27>
    SeparatorActive: typing.ClassVar[StyleColor]  # value = <StyleColor.SeparatorActive: 29>
    SeparatorHovered: typing.ClassVar[StyleColor]  # value = <StyleColor.SeparatorHovered: 28>
    SliderGrab: typing.ClassVar[StyleColor]  # value = <StyleColor.SliderGrab: 19>
    SliderGrabActive: typing.ClassVar[StyleColor]  # value = <StyleColor.SliderGrabActive: 20>
    Tab: typing.ClassVar[StyleColor]  # value = <StyleColor.Tab: 33>
    TabActive: typing.ClassVar[StyleColor]  # value = <StyleColor.TabActive: 35>
    TabHovered: typing.ClassVar[StyleColor]  # value = <StyleColor.TabHovered: 34>
    TabUnfocused: typing.ClassVar[StyleColor]  # value = <StyleColor.TabUnfocused: 36>
    TabUnfocusedActive: typing.ClassVar[StyleColor]  # value = <StyleColor.TabUnfocusedActive: 37>
    TableBorderLight: typing.ClassVar[StyleColor]  # value = <StyleColor.TableBorderLight: 46>
    TableBorderStrong: typing.ClassVar[StyleColor]  # value = <StyleColor.TableBorderStrong: 45>
    TableHeaderBg: typing.ClassVar[StyleColor]  # value = <StyleColor.TableHeaderBg: 44>
    TableRowBg: typing.ClassVar[StyleColor]  # value = <StyleColor.TableRowBg: 47>
    TableRowBgAlt: typing.ClassVar[StyleColor]  # value = <StyleColor.TableRowBgAlt: 48>
    Text: typing.ClassVar[StyleColor]  # value = <StyleColor.Text: 0>
    TextDisabled: typing.ClassVar[StyleColor]  # value = <StyleColor.TextDisabled: 1>
    TextSelectedBg: typing.ClassVar[StyleColor]  # value = <StyleColor.TextSelectedBg: 49>
    TitleBg: typing.ClassVar[StyleColor]  # value = <StyleColor.TitleBg: 10>
    TitleBgActive: typing.ClassVar[StyleColor]  # value = <StyleColor.TitleBgActive: 11>
    TitleBgCollapsed: typing.ClassVar[StyleColor]  # value = <StyleColor.TitleBgCollapsed: 12>
    WindowBg: typing.ClassVar[StyleColor]  # value = <StyleColor.WindowBg: 2>
    WindowShadow: typing.ClassVar[StyleColor]  # value = <StyleColor.WindowShadow: 55>
    __members__: typing.ClassVar[dict[str, StyleColor]]  # value = {'Text': <StyleColor.Text: 0>, 'TextDisabled': <StyleColor.TextDisabled: 1>, 'WindowBg': <StyleColor.WindowBg: 2>, 'ChildBg': <StyleColor.ChildBg: 3>, 'PopupBg': <StyleColor.PopupBg: 4>, 'Border': <StyleColor.Border: 5>, 'BorderShadow': <StyleColor.BorderShadow: 6>, 'FrameBg': <StyleColor.FrameBg: 7>, 'FrameBgHovered': <StyleColor.FrameBgHovered: 8>, 'FrameBgActive': <StyleColor.FrameBgActive: 9>, 'TitleBg': <StyleColor.TitleBg: 10>, 'TitleBgActive': <StyleColor.TitleBgActive: 11>, 'TitleBgCollapsed': <StyleColor.TitleBgCollapsed: 12>, 'MenuBarBg': <StyleColor.MenuBarBg: 13>, 'ScrollbarBg': <StyleColor.ScrollbarBg: 14>, 'ScrollbarGrab': <StyleColor.ScrollbarGrab: 15>, 'ScrollbarGrabHovered': <StyleColor.ScrollbarGrabHovered: 16>, 'ScrollbarGrabActive': <StyleColor.ScrollbarGrabActive: 17>, 'CheckMark': <StyleColor.CheckMark: 18>, 'SliderGrab': <StyleColor.SliderGrab: 19>, 'SliderGrabActive': <StyleColor.SliderGrabActive: 20>, 'Button': <StyleColor.Button: 21>, 'ButtonHovered': <StyleColor.ButtonHovered: 22>, 'ButtonActive': <StyleColor.ButtonActive: 23>, 'Header': <StyleColor.Header: 24>, 'HeaderHovered': <StyleColor.HeaderHovered: 25>, 'HeaderActive': <StyleColor.HeaderActive: 26>, 'Separator': <StyleColor.Separator: 27>, 'SeparatorHovered': <StyleColor.SeparatorHovered: 28>, 'SeparatorActive': <StyleColor.SeparatorActive: 29>, 'ResizeGrip': <StyleColor.ResizeGrip: 30>, 'ResizeGripHovered': <StyleColor.ResizeGripHovered: 31>, 'ResizeGripActive': <StyleColor.ResizeGripActive: 32>, 'Tab': <StyleColor.Tab: 33>, 'TabHovered': <StyleColor.TabHovered: 34>, 'TabActive': <StyleColor.TabActive: 35>, 'TabUnfocused': <StyleColor.TabUnfocused: 36>, 'TabUnfocusedActive': <StyleColor.TabUnfocusedActive: 37>, 'DockingPreview': <StyleColor.DockingPreview: 38>, 'DockingEmptyBg': <StyleColor.DockingEmptyBg: 39>, 'PlotLines': <StyleColor.PlotLines: 40>, 'PlotLinesHovered': <StyleColor.PlotLinesHovered: 41>, 'PlotHistogram': <StyleColor.PlotHistogram: 42>, 'PlotHistogramHovered': <StyleColor.PlotHistogramHovered: 43>, 'TableHeaderBg': <StyleColor.TableHeaderBg: 44>, 'TableBorderStrong': <StyleColor.TableBorderStrong: 45>, 'TableBorderLight': <StyleColor.TableBorderLight: 46>, 'TableRowBg': <StyleColor.TableRowBg: 47>, 'TableRowBgAlt': <StyleColor.TableRowBgAlt: 48>, 'TextSelectedBg': <StyleColor.TextSelectedBg: 49>, 'DragDropTarget': <StyleColor.DragDropTarget: 50>, 'NavHighlight': <StyleColor.NavHighlight: 51>, 'NavWindowingHighlight': <StyleColor.NavWindowingHighlight: 52>, 'NavWindowingDimBg': <StyleColor.NavWindowingDimBg: 53>, 'ModalWindowDimBg': <StyleColor.ModalWindowDimBg: 54>, 'WindowShadow': <StyleColor.WindowShadow: 55>, 'CustomText': <StyleColor.CustomText: 56>, 'Count': <StyleColor.Count: 57>}
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
class StyleColorsPreset:
    """
    Members:
    
      NvidiaDark
    
      NvidiaLight
    
      Dark
    
      Light
    
      Classic
    
      Count
    """
    Classic: typing.ClassVar[StyleColorsPreset]  # value = <StyleColorsPreset.Classic: 4>
    Count: typing.ClassVar[StyleColorsPreset]  # value = <StyleColorsPreset.Count: 5>
    Dark: typing.ClassVar[StyleColorsPreset]  # value = <StyleColorsPreset.Dark: 2>
    Light: typing.ClassVar[StyleColorsPreset]  # value = <StyleColorsPreset.Light: 3>
    NvidiaDark: typing.ClassVar[StyleColorsPreset]  # value = <StyleColorsPreset.NvidiaDark: 0>
    NvidiaLight: typing.ClassVar[StyleColorsPreset]  # value = <StyleColorsPreset.NvidiaLight: 1>
    __members__: typing.ClassVar[dict[str, StyleColorsPreset]]  # value = {'NvidiaDark': <StyleColorsPreset.NvidiaDark: 0>, 'NvidiaLight': <StyleColorsPreset.NvidiaLight: 1>, 'Dark': <StyleColorsPreset.Dark: 2>, 'Light': <StyleColorsPreset.Light: 3>, 'Classic': <StyleColorsPreset.Classic: 4>, 'Count': <StyleColorsPreset.Count: 5>}
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
class StyleVar:
    """
    Members:
    
      Alpha
    
      WindowPadding
    
      WindowRounding
    
      WindowBorderSize
    
      WindowMinSize
    
      WindowTitleAlign
    
      ChildRounding
    
      ChildBorderSize
    
      PopupRounding
    
      PopupBorderSize
    
      FramePadding
    
      FrameRounding
    
      FrameBorderSize
    
      ItemSpacing
    
      ItemInnerSpacing
    
      CellPadding
    
      IndentSpacing
    
      ScrollbarSize
    
      ScrollbarRounding
    
      GrabMinSize
    
      GrabRounding
    
      TabRounding
    
      ButtonTextAlign
    
      SelectableTextAlign
    
      DockSplitterSize
    """
    Alpha: typing.ClassVar[StyleVar]  # value = <StyleVar.Alpha: 0>
    ButtonTextAlign: typing.ClassVar[StyleVar]  # value = <StyleVar.ButtonTextAlign: 22>
    CellPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.CellPadding: 15>
    ChildBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.ChildBorderSize: 7>
    ChildRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.ChildRounding: 6>
    DockSplitterSize: typing.ClassVar[StyleVar]  # value = <StyleVar.DockSplitterSize: 24>
    FrameBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.FrameBorderSize: 12>
    FramePadding: typing.ClassVar[StyleVar]  # value = <StyleVar.FramePadding: 10>
    FrameRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.FrameRounding: 11>
    GrabMinSize: typing.ClassVar[StyleVar]  # value = <StyleVar.GrabMinSize: 19>
    GrabRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.GrabRounding: 20>
    IndentSpacing: typing.ClassVar[StyleVar]  # value = <StyleVar.IndentSpacing: 16>
    ItemInnerSpacing: typing.ClassVar[StyleVar]  # value = <StyleVar.ItemInnerSpacing: 14>
    ItemSpacing: typing.ClassVar[StyleVar]  # value = <StyleVar.ItemSpacing: 13>
    PopupBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.PopupBorderSize: 9>
    PopupRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.PopupRounding: 8>
    ScrollbarRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.ScrollbarRounding: 18>
    ScrollbarSize: typing.ClassVar[StyleVar]  # value = <StyleVar.ScrollbarSize: 17>
    SelectableTextAlign: typing.ClassVar[StyleVar]  # value = <StyleVar.SelectableTextAlign: 23>
    TabRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.TabRounding: 21>
    WindowBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.WindowBorderSize: 3>
    WindowMinSize: typing.ClassVar[StyleVar]  # value = <StyleVar.WindowMinSize: 4>
    WindowPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.WindowPadding: 1>
    WindowRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.WindowRounding: 2>
    WindowTitleAlign: typing.ClassVar[StyleVar]  # value = <StyleVar.WindowTitleAlign: 5>
    __members__: typing.ClassVar[dict[str, StyleVar]]  # value = {'Alpha': <StyleVar.Alpha: 0>, 'WindowPadding': <StyleVar.WindowPadding: 1>, 'WindowRounding': <StyleVar.WindowRounding: 2>, 'WindowBorderSize': <StyleVar.WindowBorderSize: 3>, 'WindowMinSize': <StyleVar.WindowMinSize: 4>, 'WindowTitleAlign': <StyleVar.WindowTitleAlign: 5>, 'ChildRounding': <StyleVar.ChildRounding: 6>, 'ChildBorderSize': <StyleVar.ChildBorderSize: 7>, 'PopupRounding': <StyleVar.PopupRounding: 8>, 'PopupBorderSize': <StyleVar.PopupBorderSize: 9>, 'FramePadding': <StyleVar.FramePadding: 10>, 'FrameRounding': <StyleVar.FrameRounding: 11>, 'FrameBorderSize': <StyleVar.FrameBorderSize: 12>, 'ItemSpacing': <StyleVar.ItemSpacing: 13>, 'ItemInnerSpacing': <StyleVar.ItemInnerSpacing: 14>, 'CellPadding': <StyleVar.CellPadding: 15>, 'IndentSpacing': <StyleVar.IndentSpacing: 16>, 'ScrollbarSize': <StyleVar.ScrollbarSize: 17>, 'ScrollbarRounding': <StyleVar.ScrollbarRounding: 18>, 'GrabMinSize': <StyleVar.GrabMinSize: 19>, 'GrabRounding': <StyleVar.GrabRounding: 20>, 'TabRounding': <StyleVar.TabRounding: 21>, 'ButtonTextAlign': <StyleVar.ButtonTextAlign: 22>, 'SelectableTextAlign': <StyleVar.SelectableTextAlign: 23>, 'DockSplitterSize': <StyleVar.DockSplitterSize: 24>}
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
def acquire_imgui(plugin_name: str = None, library_path: str = None) -> ImGui:
    ...
WINDOW_FLAG_ALWAYS_AUTO_RESIZE: int = 64
WINDOW_FLAG_ALWAYS_HORIZONTAL_SCROLLBAR: int = 32768
WINDOW_FLAG_ALWAYS_USE_WINDOW_PADDING: int = 65536
WINDOW_FLAG_ALWAYS_VERTICAL_SCROLLBAR: int = 16384
WINDOW_FLAG_HORIZONTAL_SCROLLBAR: int = 2048
WINDOW_FLAG_MENU_BAR: int = 1024
WINDOW_FLAG_NO_BACKGROUND: int = 128
WINDOW_FLAG_NO_BRING_TO_FRONT_ON_FOCUS: int = 8192
WINDOW_FLAG_NO_COLLAPSE: int = 32
WINDOW_FLAG_NO_DOCKING: int = 2097152
WINDOW_FLAG_NO_FOCUS_ON_APPEARING: int = 4096
WINDOW_FLAG_NO_MOUSE_INPUTS: int = 512
WINDOW_FLAG_NO_MOVE: int = 4
WINDOW_FLAG_NO_NAV_FOCUS: int = 262144
WINDOW_FLAG_NO_NAV_INPUTS: int = 524288
WINDOW_FLAG_NO_RESIZE: int = 2
WINDOW_FLAG_NO_SAVED_SETTINGS: int = 256
WINDOW_FLAG_NO_SCROLLBAR: int = 8
WINDOW_FLAG_NO_SCROLL_WITH_MOUSE: int = 16
WINDOW_FLAG_NO_TITLE_BAR: int = 1
WINDOW_FLAG_UNSAVED_DOCUMENT: int = 1048576
