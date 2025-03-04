# from prac1.conversion_base import ConversionBase
# from prac1.mappings import word_to_digit_map

# class WordToNumConverter(ConversionBase):
#     """
#     A class to convert numbers written in words into their numeric form.
#     """
    
#     def __init__(self):
#         self.word_to_digit_map = word_to_digit_map
    
#     def convert(self, word: str) -> int:
#         """
#         Converts  Word number into an integer.
        
#         Args:
#             word (str): A number written in words
        
#         Returns:
#             int: The number of that word which entered by user
#         """
        
#         def word_to_digit(part: str, remaining: str, num: str) -> tuple:
#             """
#             A recursive function to process the input word and map it to its numeric value.
            
#             Args:
#                 part (str): A substring currently being processed.
#                 remaining (str): The rest of the input word.
#                 num (str): Accumulated numeric representation.
            
#             Returns:
#                 tuple: (numeric string, leftover unmatched characters)
#             """

#             if not remaining:
#                 return num, part
            
#             part += remaining[0]

#             if part in self.word_to_digit_map:
#                 num += self.word_to_digit_map[part] 
#                 part = ''
#             return word_to_digit(part, remaining[1:], num)
#         num, lft = word_to_digit('', word, '')
#         return int(num) if not lft else -1

# from prac1.conversion_base import ConversionBase
# from prac1.mappings import word_to_digit_map

# class WordToNumConverter(ConversionBase):
#     def __init__(self):
#         self.word_to_digit_map = word_to_digit_map

#     def convert(self, word: str) -> int:
#         if not word.strip():
#             raise ValueError("Error: Input cannot be empty. Execution stopped.")

#         def word_to_digit(part: str, remaining: str, num: str) -> tuple:
#             if not remaining:
#                 return num, part

#             part += remaining[0]

#             if part in self.word_to_digit_map:
#                 num += self.word_to_digit_map[part]
#                 part = ''
#             return word_to_digit(part, remaining[1:], num)

#         num, lft = word_to_digit('', word, '')

#         if lft:
#             raise ValueError(f"Error: Invalid word found: '{lft}'. Execution stopped.")

#         return int(num)

from prac1.conversion_base import ConversionBase
from prac1.mappings import word_to_digit_map

class WordToNumConverter(ConversionBase):
    def __init__(self):
        self.word_to_digit_map = word_to_digit_map

    def convert(self, word: str) -> int:
        # Check for empty input manually
        is_empty = True
        for char in word:
            if char != ' ':
                is_empty = False
                break
        if is_empty:
            raise ValueError("Error: Input cannot be empty. Execution stopped.")

        def word_to_digit(part, remaining, num):
            if not remaining:
                return num, part

            part += remaining[0]

            # Check manually if part exists in the map
            exists = False
            for key in self.word_to_digit_map:
                if key == part:
                    exists = True
                    break

            if exists:
                num += self.word_to_digit_map[part]
                part = ''
                
            return word_to_digit(part, remaining[1:], num)

        num, lft = word_to_digit('', word, '')

        # Check manually if any leftover invalid word exists
        if lft:
            raise ValueError(f"Error: Invalid word found: '{lft}'. Execution stopped.")

        # Convert manually constructed numeric string to integer
        result = 0
        for digit in num:
            result = result * 10 + (ord(digit) - ord('0'))

        return result
