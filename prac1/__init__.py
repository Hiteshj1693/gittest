"""
This package contains modules for number-word conversion and GCD computation.
"""

from .mappings import digits
from .conversion_base import ConversionBase
from .word_to_num import WordToNumConverter
from .num_to_word import NumToWordConverter
from .gcd import GCDComputer

__all__ = ["digits", "ConversionBase", "WordToNumConverter", "NumToWordConverter", "GCDComputer"]