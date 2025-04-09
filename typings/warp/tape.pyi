from __future__ import annotations
from collections import defaultdict
from collections import namedtuple
import typing
import warp as wp
import warp.codegen
import warp.context
import warp.types
__all__ = ['ArrayStatsVisitor', 'GraphvizTapeVisitor', 'Launch', 'RepeatedSequence', 'Tape', 'TapeVisitor', 'defaultdict', 'get_struct_vars', 'namedtuple', 'visit_tape', 'visualize_tape_graphviz', 'wp']
class ArrayStatsVisitor(TapeVisitor):
    class ArrayState(tuple):
        """
        ArrayState(mean, std, min, max)
        """
        __match_args__: typing.ClassVar[tuple] = ('mean', 'std', 'min', 'max')
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('mean', 'std', 'min', 'max')
        @staticmethod
        def __new__(_cls, mean, std, min, max):
            """
            Create new instance of ArrayState(mean, std, min, max)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new ArrayState object from a sequence or iterable
            """
        def __getnewargs__(self):
            """
            Return self as a plain tuple.  Used by copy and pickle.
            """
        def __repr__(self):
            """
            Return a nicely formatted representation string
            """
        def _asdict(self):
            """
            Return a new dict which maps field names to their values.
            """
        def _replace(self, **kwds):
            """
            Return a new ArrayState object replacing specified fields with new values
            """
    def __init__(self):
        ...
    def emit_array_node(self, arr: warp.types.array, label: str, active_scope_stack: typing.List[str], indent_level: int):
        ...
    def emit_kernel_launch_node(self, kernel: warp.context.Kernel, kernel_launch_id: str, launch_data: dict, rendered: bool, indent_level: int):
        ...
class GraphvizTapeVisitor(TapeVisitor):
    @staticmethod
    def dtype2str(dtype):
        ...
    @staticmethod
    def sanitize(s):
        ...
    def __init__(self):
        ...
    def emit_array_node(self, arr: warp.types.array, label: str, active_scope_stack: typing.List[str], indent_level: int):
        ...
    def emit_edge_array_array(self, src: warp.types.array, dst: warp.types.array, indent_level: int):
        ...
    def emit_edge_array_kernel(self, arr_ptr: int, kernel_launch_id: str, kernel_input_id: int, indent_level: int):
        ...
    def emit_edge_kernel_array(self, kernel_launch_id: str, kernel_output_id: int, arr_ptr: int, indent_level: int):
        ...
    def emit_kernel_launch_node(self, kernel: warp.context.Kernel, kernel_launch_id: str, launch_data: dict, rendered: bool, indent_level: int):
        ...
    def emit_scope_begin(self, active_scope_id: int, active_scope_name: str, metadata: dict, indent_level: int):
        ...
    def emit_scope_end(self, indent_level: int):
        ...
class Launch(tuple):
    """
    Launch(id, kernel, dim, max_blocks, inputs, outputs, device, block_dim, metadata)
    """
    __match_args__: typing.ClassVar[tuple] = ('id', 'kernel', 'dim', 'max_blocks', 'inputs', 'outputs', 'device', 'block_dim', 'metadata')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('id', 'kernel', 'dim', 'max_blocks', 'inputs', 'outputs', 'device', 'block_dim', 'metadata')
    @staticmethod
    def __new__(_cls, id, kernel, dim, max_blocks, inputs, outputs, device, block_dim, metadata):
        """
        Create new instance of Launch(id, kernel, dim, max_blocks, inputs, outputs, device, block_dim, metadata)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new Launch object from a sequence or iterable
        """
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
    def _asdict(self):
        """
        Return a new dict which maps field names to their values.
        """
    def _replace(self, **kwds):
        """
        Return a new Launch object replacing specified fields with new values
        """
class RepeatedSequence(tuple):
    """
    RepeatedSequence(start, end, repetitions)
    """
    __match_args__: typing.ClassVar[tuple] = ('start', 'end', 'repetitions')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('start', 'end', 'repetitions')
    @staticmethod
    def __new__(_cls, start, end, repetitions):
        """
        Create new instance of RepeatedSequence(start, end, repetitions)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new RepeatedSequence object from a sequence or iterable
        """
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
    def _asdict(self):
        """
        Return a new dict which maps field names to their values.
        """
    def _replace(self, **kwds):
        """
        Return a new RepeatedSequence object replacing specified fields with new values
        """
class Tape:
    """
    
        Record kernel launches within a Tape scope to enable automatic differentiation.
        Gradients can be computed after the operations have been recorded on the tape via
        :meth:`Tape.backward()`.
    
        Example
        -------
    
        .. code-block:: python
    
            tape = wp.Tape()
    
            # forward pass
            with tape:
                wp.launch(kernel=compute1, inputs=[a, b], device="cuda")
                wp.launch(kernel=compute2, inputs=[c, d], device="cuda")
                wp.launch(kernel=loss, inputs=[d, l], device="cuda")
    
            # reverse pass
            tape.backward(l)
    
        Gradients can be accessed via the ``tape.gradients`` dictionary, e.g.:
    
        .. code-block:: python
    
            print(tape.gradients[a])
    
        
    """
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self):
        ...
    def _check_kernel_array_access(self, kernel, args):
        """
        Detect illegal inter-kernel write after read access patterns during launch capture
        """
    def _reset_array_read_flags(self):
        """
        
                Reset all recorded array read flags to False
                
        """
    def backward(self, loss: warp.types.array = None, grads: dict = None):
        """
        
                Evaluate the backward pass of the recorded operations on the tape.
                A single-element array ``loss`` or a dictionary of arrays ``grads``
                can be provided to assign the incoming gradients for the reverse-mode
                automatic differentiation pass.
        
                Args:
                    loss (wp.array): A single-element array that holds the loss function value whose gradient is to be computed
                    grads (dict): A dictionary of arrays that map from Warp arrays to their incoming gradients
        
                
        """
    def get_adjoint(self, a):
        ...
    def record_func(self, backward, arrays):
        """
        
                Records a custom function to be executed only in the backward pass.
        
                Args:
                    backward (Callable): A callable Python object (can be any function) that will be executed in the backward pass.
                    arrays (list): A list of arrays that are used by the backward function. The tape keeps track of these to be able to zero their gradients in Tape.zero()
                
        """
    def record_launch(self, kernel, dim, max_blocks, inputs, outputs, device, block_dim = 0, metadata = None):
        ...
    def record_scope_begin(self, scope_name, metadata = None):
        """
        
                Begin a scope on the tape to group operations together. Scopes are only used in the visualization functions.
                
        """
    def record_scope_end(self, remove_scope_if_empty = True):
        """
        
                End a scope on the tape.
        
                Args:
                    remove_scope_if_empty (bool): If True, the scope will be removed if no kernel launches were recorded within it.
                
        """
    def reset(self):
        """
        
                Clear all operations recorded on the tape and zero out all gradients.
                
        """
    def visualize(self, filename: str = None, simplify_graph = True, hide_readonly_arrays = False, array_labels: typing.Dict[warp.types.array, str] = None, choose_longest_node_name: bool = True, ignore_graph_scopes: bool = False, track_inputs: typing.List[warp.types.array] = None, track_outputs: typing.List[warp.types.array] = None, track_input_names: typing.List[str] = None, track_output_names: typing.List[str] = None, graph_direction: str = 'LR') -> str:
        """
        
                Visualize the recorded operations on the tape as a `GraphViz diagram <https://graphviz.org/>`_.
        
                Example
                -------
        
                .. code-block:: python
        
                    import warp as wp
        
                    tape = wp.Tape()
                    with tape:
                        # record Warp kernel launches here
                        wp.launch(...)
        
                    dot_code = tape.visualize("tape.dot")
        
                This function creates a GraphViz dot file that can be rendered into an image using the GraphViz command line tool, e.g. via
        
                .. code-block:: bash
        
                        dot -Tpng tape.dot -o tape.png
        
                Args:
                    filename (str): The filename to save the visualization to (optional).
                    simplify_graph (bool): If True, simplify the graph by detecting repeated kernel launch sequences and summarizing them in subgraphs.
                    hide_readonly_arrays (bool): If True, hide arrays that are not modified by any kernel launch.
                    array_labels (Dict[wp.array, str]): A dictionary mapping arrays to custom labels.
                    choose_longest_node_name (bool): If True, the automatic name resolution will aim to find the longest name for each array in the computation graph.
                    ignore_graph_scopes (bool): If True, ignore the scopes recorded on the tape when visualizing the graph.
                    track_inputs (List[wp.array]): A list of arrays to track as inputs in the graph to ensure they are shown regardless of the `hide_readonly_arrays` setting.
                    track_outputs (List[wp.array]): A list of arrays to track as outputs in the graph so that they remain visible.
                    track_input_names (List[str]): A list of custom names for the input arrays to track in the graph (used in conjunction with `track_inputs`).
                    track_output_names (List[str]): A list of custom names for the output arrays to track in the graph (used in conjunction with `track_outputs`).
                    graph_direction (str): The direction of the graph layout (default: "LR").
        
                Returns:
                    str: The dot code representing the graph.
        
                
        """
    def zero(self):
        """
        
                Zero out all gradients recorded on the tape.
                
        """
class TapeVisitor:
    def emit_array_node(self, arr: warp.types.array, label: str, active_scope_stack: typing.List[str], indent_level: int):
        ...
    def emit_edge_array_array(self, src: warp.types.array, dst: warp.types.array, indent_level: int):
        ...
    def emit_edge_array_kernel(self, arr: warp.types.array, kernel_launch_id: str, kernel_input_id: int, indent_level: int):
        ...
    def emit_edge_kernel_array(self, kernel_launch_id: str, kernel_output_id: int, arr: warp.types.array, indent_level: int):
        ...
    def emit_kernel_launch_node(self, kernel: warp.context.Kernel, kernel_launch_id: str, launch_data: dict, rendered: bool, indent_level: int):
        ...
    def emit_scope_begin(self, active_scope_id: int, active_scope_name: str, metadata: dict, indent_level: int):
        ...
    def emit_scope_end(self, indent_level: int):
        ...
def get_struct_vars(x: warp.codegen.StructInstance):
    ...
def visit_tape(tape: Tape, visitor: TapeVisitor, simplify_graph = True, hide_readonly_arrays = False, array_labels: typing.Dict[warp.types.array, str] = None, choose_longest_node_name: bool = True, ignore_graph_scopes: bool = False, track_inputs: typing.List[warp.types.array] = None, track_outputs: typing.List[warp.types.array] = None, track_input_names: typing.List[str] = None, track_output_names: typing.List[str] = None):
    ...
def visualize_tape_graphviz(tape: Tape, filename: str, simplify_graph = True, hide_readonly_arrays = False, array_labels: typing.Dict[warp.types.array, str] = None, choose_longest_node_name: bool = True, ignore_graph_scopes: bool = False, track_inputs: typing.List[warp.types.array] = None, track_outputs: typing.List[warp.types.array] = None, track_input_names: typing.List[str] = None, track_output_names: typing.List[str] = None, graph_direction: str = 'LR'):
    ...
