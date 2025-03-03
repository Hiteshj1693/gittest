from typing import List

class ParenthesisGenerator:
    def __init__(self, n: int):
        self.n = n

    def generate(self) -> List[str]:
        """Generates all valid combinations of n pairs of parentheses."""
        return list(self._backtrack('', 0, 0))

    def _backtrack(self, curr: str, open_p: int, close_p: int):
        """Recursive generator function to generate parentheses."""
        if open_p == close_p == self.n:
            yield curr
            return

        if open_p < self.n:
            yield from self._backtrack(curr + '(', open_p + 1, close_p)

        if close_p < open_p:
            yield from self._backtrack(curr + ')', open_p, close_p + 1)


# Example Usage:
if __name__ == "__main__":
    generator = ParenthesisGenerator(3)
    result = generator.generate()
    print(result)  # Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
