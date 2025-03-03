from prac1.conversion_base import ConversionBase
from prac1.mappings import word_to_digit_map

class WordToNumConverter(ConversionBase):
    """
    A class to convert numbers written in words into their numeric form.
    """
    
    def __init__(self):
        self.word_to_digit_map = word_to_digit_map
    
    def convert(self, word: str) -> int:
        """
        Converts  Word number into an integer.
        
        Args:
            word (str): A number written in words
        
        Returns:
            int: The number of that word which entered by user
        """
        
        def word_to_digit(part: str, remaining: str, num: str) -> tuple:
            """
            A recursive function to process the input word and map it to its numeric value.
            
            Args:
                part (str): A substring currently being processed.
                remaining (str): The rest of the input word.
                num (str): Accumulated numeric representation.
            
            Returns:
                tuple: (numeric string, leftover unmatched characters)
            """

            if not remaining:
                return num, part
            
            part += remaining[0]

            if part in self.word_to_digit_map:
                num += self.word_to_digit_map[part] 
                part = ''
            return word_to_digit(part, remaining[1:], num)
        num, lft = word_to_digit('', word, '')
        return int(num) if not lft else -1