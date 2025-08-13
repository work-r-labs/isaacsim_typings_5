from __future__ import annotations
import carb as carb
import enum
from enum import StrEnum
import functools as functools
import traceback as traceback
import typing
__all__: list = ['handle_exception', 'get_unicode_normalization_method', 'UnicodeNormalizationMethod']
class UnicodeNormalizationMethod(enum.StrEnum):
    DISABLED: typing.ClassVar[UnicodeNormalizationMethod]  # value = <UnicodeNormalizationMethod.DISABLED: 'Disabled'>
    NFC: typing.ClassVar[UnicodeNormalizationMethod]  # value = <UnicodeNormalizationMethod.NFC: 'NFC'>
    @classmethod
    def __new__(cls, value):
        ...
    def __format__(self, format_spec):
        """
        Return a formatted version of the string as described by format_spec.
        """
    def __str__(self):
        """
        Return str(self).
        """
def get_unicode_normalization_method() -> UnicodeNormalizationMethod:
    """
    
        Get the Unicode normalization method from the settings.
        
    """
def handle_exception(func):
    """
    
        Decorator to print exception in async functions
        
    """
SETTINGS_UNICODE_NORMALIZATION_METHOD: str = '/persistent/app/stage/unicodeNormalizationMethod'
