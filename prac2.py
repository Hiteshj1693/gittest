"""
2. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Constraints:

        - 1 <= n <= 8

    Example 1:

        - Input: n = 3

        - Output: ["((()))","(()())","(())()","()(())","()()()"]

        - Example 2:

    Example 2:

        - Input: n = 1

        - Output: ["()"] 
"""

from typing import List

class ParenthesesGenerator:
    """
    A class to generate all valid combinations of n pairs of parentheses.
    """
    def __init__(self, n: int):
        self.n = n
        self.combinations: List[str] = []

    def generate(self) -> List[str]:
        """
        Generates all valid parentheses combinations using DFS.
        
        Returns:
            List[str]: A list containing all valid combinations.
        
        Time Complexity: O(4^n / sqrt(n))

        Catalan Number Formula
        """
        self._backtrack('', 0, 0)
        return self.combinations

    def _backtrack(self, curr: str, open_brac: int, close_brac: int):
        """
        Generate parentheses using backtracking.
        
        Args:
            curr (str): The current sequence of parentheses being built.
            open_brac (int): Number of open brackets used.
            close_brac (int): Number of close brackets used.
        """
        if len(curr) == self.n * 2:
            self.combinations.append(curr)
            return

        if open_brac < self.n:
            self._backtrack(curr + '(', open_brac + 1, close_brac)
        
        if close_brac < open_brac:
            self._backtrack(curr + ')', open_brac, close_brac + 1)

class UserInput:
    @staticmethod
    def get_input() -> int:
        """
        Takes user input
        Validate non-negative integer
        
        Returns:
            int: The number of bracket pairs.
        """
        while True:
            try:
                num_brac = int(input("Number of Bracket Pairs: "))
                if num_brac < 0:
                    raise ValueError("Invalid input: Number of brackets cannot be negative.")
                return num_brac
            except ValueError as e:
                print(e)

def main():
    num_brac = UserInput.get_input()

    if num_brac == 0:
        print([])
    else:
        generator = ParenthesesGenerator(num_brac)
        print(generator.generate())

if __name__ == '__main__':
    main()


"""

"""