from __future__ import annotations
import doctest as doctest
from isaacsim.test.docstring import _doctest
import sys as sys
import typing
import unittest as unittest
__all__: list[str] = ['StandaloneDocTestCase', 'doctest', 'sys', 'unittest']
class StandaloneDocTestCase(unittest.case.TestCase):
    """
    Base class for all standalone test cases with doctest support for checking docstrings examples
    
        .. note::
    
            Test methods must start with the ``test_`` prefix
    
        This class add the following methods:
    
        * ``assertDocTest``: Check that the examples in docstrings pass for a class/module member
        * ``assertDocTests``: Check that the examples in docstrings pass for all class/module's members (names)
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.test.docstring
            >>> tester = isaacsim.test.docstring.StandaloneDocTestCase()
            >>> tester.__class__.__name__
            'StandaloneDocTestCase'
        
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
        
                    >>> from isaacsim.test.docstring import StandaloneDocTestCase
                    >>>
                    >>> tester.assertDocTest(StandaloneDocTestCase)
                
        """
    def assertDocTests(self, expr: object, msg: str = '', flags: int = 1036, order: list[tuple[object, int]] = list(), exclude: list[object] = list(), stop_on_failure: bool = False) -> None:
        """
        Check that the examples in docstrings pass for all class/module's members (names)
        
                Args:
                    expr: module or class definition to check members' docstrings examples for
                    msg (str): custom message to display when failing
                    flags (int): doctest's option flags
                    order (list[tuple[object, int]]): list of pair (name, index) to modify the examples execution order
                    exclude (list[object]): list of class/module names to exclude for testing
                    stop_on_failure (bool): stop testing docstrings example at fist encountered failure
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.test.docstring import StandaloneDocTestCase
                    >>>
                    >>> tester.assertDocTests(StandaloneDocTestCase, exclude=[StandaloneDocTestCase.assertDocTests])
                    ... # doctest: +NO_CHECK
                
        """
