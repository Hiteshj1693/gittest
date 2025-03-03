from typing import List
from collections import defaultdict
class AnagramFinder:
    """
    Find and group anagrams from a given list of words (Class)
    """

    def __init__(self, words: List[str]):
        self.words = words

    def find_anagrams(self) -> List[List[str]]:
        """
        Finds and groups anagrams from the list of words

        Returns:
            List[List[str]]: A list of lists, where each sublist contains anagram words.
        """
        anagram_dict = defaultdict(list)

        for word in self.words:
            key = ''.join(sorted(word))
            if key in anagram_dict:
                anagram_dict[key].append(word)
            else:
                anagram_dict[key] = [word]

        return list(anagram_dict.values())


class UserInput:
    """
    A class to handle user input.
    """

    @staticmethod
    def get_input() -> List[str]:
        """
        User input for the number of words and the words themselves
        
        Returns:
            List[str]: A list of words entered by the user
        """
        try:
            number_of_words = int(input("Number of Words: "))
            if number_of_words < 0:
                raise ValueError("Invalid input: Number of words cannot be negative.")
            return [input() for _ in range(number_of_words)]
        except ValueError as e:
            print(e)
            return []


def main():
    words = UserInput.get_input()

    if not words:
        print([])
    else:
        anagram_finder = AnagramFinder(words)
        print(anagram_finder.find_anagrams())


if __name__ == '__main__':
    main()


"""
Time Complexity: O(n * m log m)
    - n: Number of words
    - m: Average length of each word
    - Sorting each word -  O(m log m)
    - Insert and Append in  dictionary  - O(1)
"""