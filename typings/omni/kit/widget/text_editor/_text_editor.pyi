from __future__ import annotations
import omni.ui._ui
import typing
__all__ = ['TextEditor']
class TextEditor(omni.ui._ui.Widget):
    """
    The binding for ImGuiColorTextEdit.
    
    """
    class Syntax:
        """
        
        
        Members:
        
          NONE
        
          PYTHON
        
          CPLUSPLUS
        
          HLSL
        
          GLSL
        
          C
        
          SQL
        
          ANGELSCRIPT
        
          LUA
        """
        ANGELSCRIPT: typing.ClassVar[TextEditor.Syntax]  # value = <Syntax.ANGELSCRIPT: 7>
        C: typing.ClassVar[TextEditor.Syntax]  # value = <Syntax.C: 5>
        CPLUSPLUS: typing.ClassVar[TextEditor.Syntax]  # value = <Syntax.CPLUSPLUS: 2>
        GLSL: typing.ClassVar[TextEditor.Syntax]  # value = <Syntax.GLSL: 4>
        HLSL: typing.ClassVar[TextEditor.Syntax]  # value = <Syntax.HLSL: 3>
        LUA: typing.ClassVar[TextEditor.Syntax]  # value = <Syntax.LUA: 8>
        NONE: typing.ClassVar[TextEditor.Syntax]  # value = <Syntax.NONE: 0>
        PYTHON: typing.ClassVar[TextEditor.Syntax]  # value = <Syntax.PYTHON: 1>
        SQL: typing.ClassVar[TextEditor.Syntax]  # value = <Syntax.SQL: 6>
        __members__: typing.ClassVar[dict[str, TextEditor.Syntax]]  # value = {'NONE': <Syntax.NONE: 0>, 'PYTHON': <Syntax.PYTHON: 1>, 'CPLUSPLUS': <Syntax.CPLUSPLUS: 2>, 'HLSL': <Syntax.HLSL: 3>, 'GLSL': <Syntax.GLSL: 4>, 'C': <Syntax.C: 5>, 'SQL': <Syntax.SQL: 6>, 'ANGELSCRIPT': <Syntax.ANGELSCRIPT: 7>, 'LUA': <Syntax.LUA: 8>}
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
    def __init__(self, **kwargs) -> None:
        """
        Constructor.
        
            `kwargs : dict`
                See below
        
        ### Keyword Arguments:
        
            `width : ui.Length`
                This property holds the width of the widget relative to its parent. Do not use this function to find the width of a screen.
        
            `height : ui.Length`
                This property holds the height of the widget relative to its parent. Do not use this function to find the height of a screen.
        
            `name : str`
                The name of the widget that user can set.
        
            `style_type_name_override : str`
                By default, we use typeName to look up the style. But sometimes it's necessary to use a custom name. For example, when a widget is a part of another widget. (Label is a part of Button) This property can override the name to use in style.
        
            `identifier : str`
                An optional identifier of the widget we can use to refer to it in queries.
        
            `visible : bool`
                This property holds whether the widget is visible.
        
            `visibleMin : float`
                If the current zoom factor and DPI is less than this value, the widget is not visible.
        
            `visibleMax : float`
                If the current zoom factor and DPI is bigger than this value, the widget is not visible.
        
            `tooltip : str`
                Set a basic tooltip for the widget, this will simply be a Label, it will follow the Tooltip style
        
            `tooltip_fn : Callable`
                Set dynamic tooltip that will be created dynamiclly the first time it is needed. the function is called inside a ui.Frame scope that the widget will be parented correctly.
        
            `tooltip_offset_x : float`
                Set the X tooltip offset in points. In a normal state, the tooltip position is linked to the mouse position. If the tooltip offset is non zero, the top left corner of the tooltip is linked to the top left corner of the widget, and this property defines the relative position the tooltip should be shown.
        
            `tooltip_offset_y : float`
                Set the Y tooltip offset in points. In a normal state, the tooltip position is linked to the mouse position. If the tooltip offset is non zero, the top left corner of the tooltip is linked to the top left corner of the widget, and this property defines the relative position the tooltip should be shown.
        
            `enabled : bool`
                This property holds whether the widget is enabled. In general an enabled widget handles keyboard and mouse events; a disabled widget does not. And widgets display themselves differently when they are disabled.
        
            `selected : bool`
                This property holds a flag that specifies the widget has to use eSelected state of the style.
        
            `checked : bool`
                This property holds a flag that specifies the widget has to use eChecked state of the style. It's on the Widget level because the button can have sub-widgets that are also should be checked.
        
            `dragging : bool`
                This property holds if the widget is being dragged.
        
            `opaque_for_mouse_events : bool`
                If the widgets has callback functions it will by default not capture the events if it is the top most widget and setup this option to true, so they don't get routed to the child widgets either
        
            `explicit_hover : bool`
                If the widgets has callback functions it will by default not capture the events if it is the top most widget and setup this option to true, so they don't get routed to the child widgets either
        
            `skip_draw_when_clipped : bool`
                The flag that specifies if it's necessary to bypass the whole draw cycle if the bounding box is clipped with a scrolling frame. It's needed to avoid the limitation of 65535 primitives in a single draw list.
        
            `mouse_moved_fn : Callable`
                Sets the function that will be called when the user moves the mouse inside the widget. Mouse move events only occur if a mouse button is pressed while the mouse is being moved. void onMouseMoved(float x, float y, int32_t modifier)
        
            `mouse_pressed_fn : Callable`
                Sets the function that will be called when the user presses the mouse button inside the widget. The function should be like this: void onMousePressed(float x, float y, int32_t button, carb::input::KeyboardModifierFlags modifier) Where 'button' is the number of the mouse button pressed. 'modifier' is the flag for the keyboard modifier key.
        
            `mouse_released_fn : Callable`
                Sets the function that will be called when the user releases the mouse button if this button was pressed inside the widget. void onMouseReleased(float x, float y, int32_t button, carb::input::KeyboardModifierFlags modifier)
        
            `mouse_double_clicked_fn : Callable`
                Sets the function that will be called when the user presses the mouse button twice inside the widget. The function specification is the same as in setMousePressedFn. void onMouseDoubleClicked(float x, float y, int32_t button, carb::input::KeyboardModifierFlags modifier)
        
            `mouse_wheel_fn : Callable`
                Sets the function that will be called when the user uses mouse wheel on the focused window. The function specification is the same as in setMousePressedFn. void onMouseWheel(float x, float y, carb::input::KeyboardModifierFlags modifier)
        
            `mouse_hovered_fn : Callable`
                Sets the function that will be called when the user use mouse enter/leave on the focused window. function specification is the same as in setMouseHovedFn. void onMouseHovered(bool hovered)
        
            `drag_fn : Callable`
                Specify that this Widget is draggable, and set the callback that is attached to the drag operation.
        
            `accept_drop_fn : Callable`
                Specify that this Widget can accept specific drops and set the callback that is called to check if the drop can be accepted.
        
            `drop_fn : Callable`
                Specify that this Widget accepts drops and set the callback to the drop operation.
        
            `computed_content_size_changed_fn : Callable`
                Called when the size of the widget is changed.
        """
    def call_edited_fn(self, arg0: bool) -> None:
        """
        Sets the function that will be called when the editor text changes from the user input. The function specification is: void onEdited(bool edited)
        """
    def has_edited_fn(self) -> bool:
        """
        Sets the function that will be called when the editor text changes from the user input. The function specification is: void onEdited(bool edited)
        """
    def set_edited_fn(self, fn: typing.Callable[[bool], None]) -> None:
        """
        Sets the function that will be called when the editor text changes from the user input. The function specification is: void onEdited(bool edited)
        """
    def set_error_markers(self, markers: dict[int, str]) -> None:
        """
        The error markers show the error message at the specific line.
        """
    @property
    def current_line_text(self) -> str:
        """
        The text on the current line.
        """
    @property
    def overwrite(self) -> bool:
        """
        Insert mode. It's possible to activate ot with the key INS.
        """
    @property
    def read_only(self) -> bool:
        """
        Read Only mode is when the user can select, but can't edit.
        """
    @read_only.setter
    def read_only(self, arg1: bool) -> None:
        ...
    @property
    def selected_text(self) -> str:
        """
        Current selection.
        """
    @property
    def syntax(self) -> TextEditor.Syntax:
        """
        This property holds the language for syntax highlighting.
        """
    @syntax.setter
    def syntax(self, arg1: TextEditor.Syntax) -> None:
        ...
    @property
    def text(self) -> str:
        """
        Get the text to the widget.
        """
    @text.setter
    def text(self, arg1: str) -> None:
        ...
    @property
    def text_lines(self) -> list[str]:
        """
        Get the text lines to the widget.
        """
    @text_lines.setter
    def text_lines(self, arg1: list[str]) -> None:
        ...
    @property
    def total_lines(self) -> int:
        """
        Number of lines in the widget.
        """
