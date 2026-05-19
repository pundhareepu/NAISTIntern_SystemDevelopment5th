"""
A simple calculator module with basic arithmetic operations.
"""

class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""
    pass


class Calculator:
    """Calculator class providing basic arithmetic operations."""
    MAX_VALUE = 1000000
    MIN_VALUE = -1000000


    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("XXCannot divide by zeroXX")
        self._validate_input(a, b)
        return a / b

    def _validate_input(self, *values):
        """Validate input values and raise exception if any are outside valid range.

        Args:
            values: Input values

        Raises:
            InvalidInputException: If any input is outside valid range
        """

        for value in values:
            if value > self.MAX_VALUE or value < self.MIN_VALUE:
                raise InvalidInputException(f"Input value {value} is outside the valid range {self.MIN_VALUE} to {self.MAX_VALUE}")






