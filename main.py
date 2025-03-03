# main.py

from prac1.word_to_num import WordToNumConverter
from prac1.num_to_word import NumToWordConverter
from prac1.gcd import GCDComputer

def main():
    try:
        word_to_num_converter = WordToNumConverter()
        num_to_word_converter = NumToWordConverter()

        inputstr1 = input("Please enter input 1: ").lower()
        inputnum1 = int(word_to_num_converter.convert(inputstr1))

        inputstr2 = input("Please enter input 2: ").lower()
        inputnum2 = int(word_to_num_converter.convert(inputstr2))

        gcd_num = str(GCDComputer.compute(inputnum1, inputnum2))

        print(f"GCD of {inputstr1} and {inputstr2} is {num_to_word_converter.convert(gcd_num)}")

    except TypeError:
        print("Please Enter a valid Word.")
    except ValueError:
        print("Invalid numeric value entered.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()