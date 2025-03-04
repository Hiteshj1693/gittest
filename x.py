'''
1. Write a program for computing GCD of 2 numbers with optimal data structures and less
   time-consuming.

    The program should take input from console or args and should handle unexpected inputs    

    Constraints:

        - For loop is not allowed

        - input should be in words:

            - e.g.: onetwo = 12, sixone = 61

        - words will be within zero to nine

        - Cannot use inbuilt methods like max, min, or any math function    

    Example 1:

        - Input 1: onezero

        - Input 2: twozero

        - Output: onezero

    Example 2:

        - Input 1: twosix

        - Input 2: twofour

        - Output: two
'''

def gcd_of_words(input1: str, input2: str) -> str:
    """
    Computes the Greatest Common Divisor (GCD) of two numbers represented as words.

    Converts the word-form numbers to integers, calculates the GCD using recursion,
    and then converts the result back into word format.

    Parameters:
    input1 (str): First number in word format (e.g., "onetwo" -> 12).
    input2 (str): Second number in word format.

    Returns:
    str: The GCD represented in word format.
    """
    num1 = word_2_digit(input1)
    num2 = word_2_digit(input2)
    if num1 < 0 or num2 < 0:
        raise ValueError()
    gcd = greatest_common_divisor(num1, num2)
    return digit_2_word(gcd)

def word_2_digit(word: str) -> int:
    """
    Converts a number written in words into its integer representation.

    Uses recursion to parse the word character by character and match valid digits.

    Parameters:
    word (str): A string representing a number in words (e.g., "onetwo" -> 12).

    Returns:
    int: The corresponding integer, or -1 if the input is invalid.
    """
    if not isinstance(word, str):
        return -1
    w_2_d = {
        'zero': '0', 
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9'
        }

    def word_2_digit_recursive(part: str, word: str, num: str) -> list:
        """
        Recursively converts a word-based number to its numeric representation.

        Parameters:
        part (str): A partial word being processed.
        word (str): The remaining word to process.
        num (str): The accumulated numeric result.

        Returns:
        list: A list containing the numeric string and any leftover unmatched characters.
        """
        if len(word) == 0:
            return [num, part]
        part += word[0]
        if part in w_2_d:
            num += w_2_d[part]
            part = ''
        return word_2_digit_recursive(part, word[1:], num)
    num, part_left = word_2_digit_recursive('', word, '')
    return int(num) if not part_left else -1

def digit_2_word(digit: int) -> str:
    """
    Converts an integer into its word representation.

    Uses recursion to process each digit and construct the word equivalent.

    Parameters:
    digit (int): A non-negative integer.

    Returns:
    str: The corresponding word representation.
    """
    if not isinstance(digit, int) or isinstance(digit, bool):
        raise TypeError
    d_2_w = {
        '0': 'zero', 
        '1': 'one', 
        '2': 'two', 
        '3': 'three', 
        '4': 'four', 
        '5': 'five', 
        '6': 'six', 
        '7': 'seven', 
        '8': 'eight', 
        '9': 'nine'
        }
    digits = str(digit)

    def digit_2_word_recursive(words: str, digits: str) -> str:
        """
        Recursively converts a numeric string into its word representation.

        Parameters:
        words (str): The accumulated word representation.
        digits (str): The remaining digits to process.

        Returns:
        str: The full number represented as words.
        """
        if not digits:
            return words
        words += d_2_w[digits[0]]
        return digit_2_word_recursive(words, digits[1:])
    return digit_2_word_recursive('', digits)

def greatest_common_divisor(num1: int, num2: int) -> int:
    """
    Computes the Greatest Common Divisor (GCD) using recursion (Euclidean Algorithm).

    Parameters:
    num1 (int): First integer.
    num2 (int): Second integer.

    Returns:
    int: The GCD of num1 and num2.
    """
    big = num1 if num1 > num2 else num2
    small = num2 if num1 > num2 else num1

    def gcd_recursive(big: int, small: int) -> int:
        """
        Recursively calculates the Greatest Common Divisor (GCD) using the Euclidean Algorithm.

        Parameters:
        big (int): The larger number.
        small (int): The smaller number.

        Returns:
        int: The GCD of the two numbers.
        """
        return big if small == 0 else gcd_recursive(small, big % small)

    return gcd_recursive(big, small)

#----------------------------Functions using While Loop Logic----------------------------------
def word_2_digit_with_while(word: str) -> int:
    """
    Converts a number written in words into its integer representation using a while loop.

    Parameters:
    word (str): A string representing a number in words (e.g., "onetwo" -> 12).

    Returns:
    int: The corresponding integer, or -1 if the input is invalid.
    """
    if not isinstance(word, str):
        return -1
    w_2_d = {
        'zero': 0, 
        'one': 1, 
        'two': 2, 
        'three': 3, 
        'four': 4, 
        'five': 5, 
        'six': 6, 
        'seven': 7, 
        'eight': 8, 
        'nine': 9
        }
    i = 0
    n = len(word)
    cur_num = ''
    digit = 0
    while i < n:
        cur_num += word[i]
        if cur_num in w_2_d:
            digit = digit * 10 + w_2_d[cur_num]
            cur_num = ''
        i += 1
    return digit if len(cur_num) == 0 else -1

def digit_2_word_with_while(digit: int) -> str:
    """
    Converts an integer into its word representation using a while loop.

    Parameters:
    digit (int): A non-negative integer.

    Returns:
    str: The corresponding word representation.
    """
    if not isinstance(digit, int) or isinstance(digit, bool):
        raise TypeError
    d_2_w = {
        '0': 'zero', 
        '1': 'one', 
        '2': 'two', 
        '3': 'three', 
        '4': 'four', 
        '5': 'five', 
        '6': 'six', 
        '7': 'seven', 
        '8': 'eight', 
        '9': 'nine'
        }
    word = ''
    digit = str(digit)
    i, n = 0, len(digit)
    while i < n:
        word += d_2_w[digit[i]]
        i += 1
    return word

def gcd_log_time_with_while(num1: int, num2: int) -> int:
    """
    Computes the Greatest Common Divisor (GCD) using a while loop (O(log n) Euclidean Algorithm).

    Parameters:
    num1 (int): First integer.
    num2 (int): Second integer.

    Returns:
    int: The GCD of num1 and num2.
    """
    big = num1 if num1 > num2 else num2
    small = num2 if num1 > num2 else num1

    # Takes logn time where n will be the larger number
    while small != 0:
        big, small = small, big % small

    return big

def gcd_linear_time_with_while(num1: int, num2: int) -> int:
    """
    Computes the Greatest Common Divisor (GCD) using a while loop (Linear Time).

    This approach repeatedly subtracts the smaller number from the larger one.

    Parameters:
    num1 (int): First integer.
    num2 (int): Second integer.

    Returns:
    int: The GCD of num1 and num2.
    """
    big = num1 if num1 > num2 else num2
    small = num2 if num1 > num2 else num1

    # Takes Linear time
    while small != 0:
        big -= small
        if big < small:
            small, big = big, small
    return big


if __name__ == '__main__':
    print('\n------------------Greatest Common Divisor-------------------')
    inp1 = input('\nEnter 1st Number [in words] - ')
    inp2 = input('\nEnter 2nd Number [in words] - ')
    try:
        output = gcd_of_words(inp1, inp2)
        print(f'\nThe gcd of {inp1} and {inp2} is - ', output)
    except ValueError:
        print("\nInvalid input: numbers must be in words from zero to nine.")