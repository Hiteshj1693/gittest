class GCDComputer:
    """
    Calculation of  GCD using recursion.
    """

    @staticmethod
    def compute(num1: int, num2: int) -> int:
        """
        Calculate the GCD of two numbers using recursion.

        Args:
            num1 (int): The first integer.
            num2 (int): The second integer.

        Returns:
            int: The GCD of the input integers.
        """
        if num2 == 0:
            return num1
        else:
            return GCDComputer.compute(num2, num1 % num2)