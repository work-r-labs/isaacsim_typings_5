from __future__ import annotations
from builtins import module as ModuleType
import carb as carb
from collections import defaultdict
from contextlib import suppress
import fnmatch as fnmatch
import omni as omni
from omni.kit.test.unittests import get_tests_to_remove_from_modules
import sys as sys
import typing
import unittest as unittest
__all__ = ['ModuleMap_t', 'ModuleType', 'carb', 'defaultdict', 'extension_from_test_name', 'find_disabled_tests', 'fnmatch', 'get_module_to_extension_map', 'get_tests_to_remove_from_modules', 'omni', 'suppress', 'sys', 'test_only_extension_dependencies', 'unittest']
def extension_from_test_name(test_name: str, module_map: ModuleMap_t) -> tuple[str, bool, str, bool] | None:
    """
    Given a test name, return None if the extension couldn't be inferred from the name, otherwise a tuple
        containing the name of the owning extension, a boolean indicating if it is currently enabled, a string
        indicating in which Python module the test was found, and a boolean indicating if that module is currently
        imported, or None if it was not.
    
        Args:
            test_name: Full name of the test to look up
            module_map: Module to extension mapping. Passed in for sharing as it's expensive to compute.
    
        The algorithm walks backwards from the full name to find the maximum-length Python import module known to be
        part of an extension that is part of the test name. It does this because the exact import paths can be nested or
        not nested. e.g. omni.kit.window.tests is not part of omni.kit.window
    
        Extracting the extension from the test name is a little tricky but all of the information is available. Here is
        how it attempts to decompose a sample test name
    
        .. code-block:: text
    
            omni.graph.nodes.tests.tests_for_samples.TestsForSamples.test_for_sample
            +--------------+ +---+ +---------------+ +-------------+ +-------------+
            Import path      |     |                 |               |
                             Testing subdirectory    |               |
                                   |                 |               |
                                   Test File         Test Class      Test Name
    
        Each extension has a list of import paths of Python modules it explicitly defines, and in addition it will add
        implicit imports for .tests and .ogn.tests submodules that are not explicitly listed in the extension dictionary.
    
        With this structure the user could have done any of these imports:
    
        .. code-block:: python
    
            import omni.graph.nodes
            import omni.graph.nodes.tests
            import omni.graph.nodes.test_for_samples
    
        Each nested one may or may not have been exposed by the parent so it is important to do a greedy match.
    
        This is how the process of decoding works for this test:
    
        .. code-block:: text
    
            Split the test name on "."
                ["omni", "graph", "nodes", "tests", "tests_for_samples", "TestsForSamples", "test_for_sample"]
            Starting at the entire list, recursively remove one element until a match in the module dictionary is found
                Fail: "omni.graph.nodes.tests.tests_for_samples.TestsForSamples.test_for_sample"
                Fail: "omni.graph.nodes.tests.tests_for_samples.TestsForSamples"
                Fail: "omni.graph.nodes.tests.tests_for_samples"
                Succeed: "omni.graph.nodes.tests"
            If no success, of if sys.modules does not contain the found module:
                Return the extension id, enabled state, and None for the module
            Else:
                Check the module recursively for exposed attributes with the rest of the names. In this example:
                    file_object = getattr(module, "tests_for_samples")
                    class_object = getattr(file_object, "TestsForSamples")
                    test_object = getattr(class_object, "test_for_sample")
                    If test_object is valid:
                        Return the extension id, enabled state, and the found module
                    Else:
                        Return the extension id, enabled state, and None for the module
    
        
    """
def find_disabled_tests() -> list[unittest.TestCase]:
    """
    Scan the existing tests and the extension.toml to find all tests that are currently disabled
    """
def get_module_to_extension_map() -> ModuleMap_t:
    """
    Returns a dictionary mapping the names of Python modules in an extension to (OwningExtension, EnabledState)
        e.g. for this extension it would contain {"omni.kit.test": (["omni.kit.test", True])}
        It will be expanded to include the implicit test modules added by the test management.
        
    """
def test_only_extension_dependencies(ext_id: str) -> set[str]:
    """
    Returns a set of extensions with test-only dependencies on the given one.
        Not currently used as dynamically enabling random extensions is not stable enough to use here yet.
        
    """
ModuleMap_t: typing._GenericAlias  # value = typing.Dict[str, typing.Tuple[str, bool]]
