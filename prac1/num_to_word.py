# from prac1.mappings import digits
# from prac1.conversion_base import ConversionBase

# class NumToWordConverter(ConversionBase):
#     """
#     Converts a number to its word representation.
#     """

#     def __init__(self):
#         self.output = ""

#     def convert(self, num: str) -> str:
#         """
#         Converts a numeric string into words.

#         Args:
#             num (str): A string representing a numeric value.

#         Returns:
#             str: A word representation of the number.
#         """
#         if num == '':
#             return ''
#         return self.output + digits[num[0]] + self.convert(num[1:])

# from prac1.mappings import digits
# from prac1.conversion_base import ConversionBase

# class NumToWordConverter(ConversionBase):
#     def __init__(self):
#         self.digits = digits

#     def convert(self, num: str) -> str:
#         if not num.strip():
#             raise ValueError("Error: Input cannot be empty. Execution stopped.")

#         if not num.isdigit():
#             raise ValueError(f"Error: Invalid numeric input: '{num}'. Execution stopped.")

#         return " ".join(self.digits[d] for d in num)

from prac1.mappings import digits
from prac1.conversion_base import ConversionBase

class NumToWordConverter(ConversionBase):
    """
    Converts a number to its word representation.
    """

    def __init__(self):
        self.output = ""

    def convert(self, num: str) -> str:
        """
        Converts a numeric string into words.

        Args:
            num (str): A string representing a numeric value.

        Returns:
            str: A word representation of the number.

        Raises:
            ValueError: If the input contains non-numeric characters.
        """
        if num == '':
            return ''

        # Check if the first character is a valid digit
        if not ('0' <= num[0] <= '9'):
            raise ValueError(f"Error: Invalid numeric input: '{num[0]}'. Execution stopped.")

        return self.output + digits[num[0]] + " " + self.convert(num[1:]) if num[1:] else digits[num[0]]
