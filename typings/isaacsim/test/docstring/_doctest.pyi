from __future__ import annotations
import doctest as doctest
import inspect as inspect
__all__: list[str] = ['DocTest', 'NO_CHECK', 'doctest', 'inspect']
class DocTest:
    def __init__(self, *args, **kwargs) -> None:
        ...
    def _get_names(self, obj, privates: bool = False) -> list[str]:
        """
        Get class/module names without including special methods
        """
    def _is_function_like(self, obj):
        """
        Check if object is function-like (including pybind11 functions)
        """
    def _is_pybind11_module(self, obj):
        """
        Check if this is a pybind11 module
        """
    def checkDocTest(self, expr: object, flags: int = 1036) -> bool:
        """
        Check that the examples in docstrings pass for a class/module member
        
                Args:
                    expr: module function or class definition, property or method to check docstrings examples for
                    flags (int): doctest's option flags
        
                Returns:
                    bool: whether the test passes or fails
                
        """
    def get_members(self, expr: object, order: list[tuple[object, int]] = list(), exclude: list[object] = list(), _globals: dict = {}) -> list[object]:
        """
        Get class/module members (names)
        
                Args:
                    expr: module function or class definition, property or method to check docstrings examples for
                    order (list[tuple[object, int]]): list of pair (name, index) to modify the examples execution order
                    exclude (list[object]): list of class/module names to exclude for testing
                    _globals (dict): current namespace
        
                Returns:
                    list[object]: list of class/module members
                
        """
class _Checker(doctest.OutputChecker):
    """
    Custom doctest's output checker to support the NO_CHECK option
    """
    def check_output(self, want, got, optionflags):
        ...
NO_CHECK: int = 2048
