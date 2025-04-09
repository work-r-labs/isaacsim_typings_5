"""
Support for the population of a test list from various configurable sources
"""
from __future__ import annotations
import abc as abc
from omni.kit.test.ext_utils import find_disabled_tests
from omni.kit.test.unittests import get_tests
import typing
import unittest as unittest
__all__: list = ['DEFAULT_POPULATOR_NAME', 'TestPopulator', 'TestPopulateAll', 'TestPopulateDisabled']
class TestPopulateAll(TestPopulator):
    """
    Implementation of the TestPopulator that returns a list of all tests known to Kit
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self):
        ...
    def get_tests(self, call_when_done: callable):
        ...
class TestPopulateDisabled(TestPopulator):
    """
    Implementation of the TestPopulator that returns a list of all tests disabled by their extension.toml file
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self):
        ...
    def get_tests(self, call_when_done: callable):
        ...
class TestPopulator(abc.ABC):
    """
    Base class for the objects used to populate the initial list of tests, before filtering.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'get_tests'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, description: str):
        """
        Set up the populator with the important information it needs for getting tests from some location
                Args:
                    name: Name of the populator, which can be used for a menu
                    description: Verbose description of the populator, which can be used for the tooltip of the menu item
                
        """
    def destroy(self):
        """
        Opportunity to clean up any allocated resources
        """
    def get_tests(self, call_when_done: callable):
        """
        Populate the internal list of raw tests and then call the provided function when it has been done.
                The callable takes one optional boolean 'canceled' that is only True if the test retrieval was not done.
                
        """
DEFAULT_POPULATOR_NAME: str = 'All Tests'
