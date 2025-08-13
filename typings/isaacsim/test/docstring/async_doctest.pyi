from __future__ import annotations
import doctest as doctest
import isaacsim as isaacsim
from isaacsim.test.docstring import _doctest
import omni as omni
import sys as sys
import typing
__all__: list[str] = ['AsyncDocTestCase', 'doctest', 'isaacsim', 'omni', 'sys']
class AsyncDocTestCase(omni.kit.test.async_unittest.AsyncTestCase):
    """
    Base class for all async test cases with doctest support for checking docstrings examples
    
        .. note::
    
            Derive from it to make the tests auto discoverable.
            Test methods must start with the ``test_`` prefix
    
        This class add the following methods:
    
        * ``assertDocTest``: Check that the examples in docstrings pass for a class/module member
        * ``assertDocTests``: Check that the examples in docstrings pass for all class/module's members (names)
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.test.docstring
            >>> tester = isaacsim.test.docstring.AsyncDocTestCase()
            >>> tester.__class__.__name__
            'AsyncDocTestCase'
        
    """
    _classSetupFailed: typing.ClassVar[bool] = False
    _class_cleanups: typing.ClassVar[list] = list()
    def __init__(self, *args, **kwargs) -> None:
        ...
    def assertDocTest(self, expr: object, msg: str = '', flags: int = 1036) -> None:
        """
        Check that the examples in docstrings pass for a class/module member
        
                Args:
                    expr: module function or class definition, property or method to check docstrings examples for
                    msg (str): custom message to display when failing
                    flags (int): doctest's option flags
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.test.docstring import AsyncDocTestCase
                    >>>
                    >>> tester.assertDocTest(AsyncDocTestCase)
                
        """
    def assertDocTests(self, expr: object, msg: str = '', flags: int = 1036, order: list[tuple[object, int]] = list(), exclude: list[object] = list(), stop_on_failure: bool = False, await_update: bool = True) -> None:
        """
        Check that the examples in docstrings pass for all class/module's members (names)
        
                Args:
                    expr: module or class definition to check members' docstrings examples for
                    msg (str): custom message to display when failing
                    flags (int): doctest's option flags
                    order (list[tuple[object, int]]): list of pair (name, index) to modify the examples execution order
                    exclude (list[object]): list of class/module names to exclude for testing
                    stop_on_failure (bool): stop testing docstrings example at fist encountered failure
                    await_update (bool): await next kit application update async before running each docstrings example
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.test.docstring import AsyncDocTestCase
                    >>> from omni.kit.async_engine import run_coroutine
                    >>>
                    >>> async def task():
                    ...     await tester.assertDocTests(AsyncDocTestCase, exclude=[AsyncDocTestCase.assertDocTests])
                    ...
                    >>> run_coroutine(task())  # doctest: +NO_CHECK
                
        """
