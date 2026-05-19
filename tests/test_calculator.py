"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

@pytest.fixture
def calc():
    return Calculator()

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected


    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_large_with_normal(self, calc):
        """Test adding large numbers with normal values."""
        # Arrange
        a = 1000011
        b = 1000
        expected = f"Input value {a} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.add(a, b)

        assert result.value.args[0] == expected

    def test_add_normal_with_large(self, calc):
        """Test adding large numbers with normal values."""
        a = 100
        b = 1000011
        expected = f"Input value {b} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.add(a, b)

        assert result.value.args[0] == expected

    def test_add_small_with_normal(self, calc):
        """Test adding small numbers."""
        a = -1000011
        b = 1000
        expected = f"Input value {a} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.add(a, b)

        assert result.value.args[0] == expected

    def test_add_normal_with_small(self, calc):
        """Test adding large numbers with normal values."""
        a = 100
        b = -1000011
        expected = f"Input value {b} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.add(a, b)

        assert result.value.args[0] == expected

    def test_add_max_value(self, calc):
        """Test adding with max value is excepted"""
        a = 1000000
        b = 1
        expected = 1000001
        result = calc.add(a, b)
        assert result == expected

    def test_add_min_value(self, calc):
        """Test adding with min value is excepted"""
        a = -1000000
        b = 1
        expected = -999999
        result = calc.add(a, b)
        assert result == expected

class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_numbers(self, calc):
        """Test subtracting negative numbers."""

        # Arrange
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_and_negative(self, calc):
        """Test subtracting positive and negative numbers."""

        # Arrange
        a = 5
        b = -3
        expected = 8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_and_positive(self, calc):
        """Test subtracting negative and positive numbers."""

        # Arrange
        a = -5
        b = 3
        expected = -8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_with_zero(self, calc):
        """Test subtracting positive number with zero."""

        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.subtract(a, b)

        # Arrange
        assert result == expected

    def test_subtract_negative_with_zero(self, calc):
        """Test subtracting negative number with zero."""

        # Arrange
        a = -5
        b = 0
        expected = -5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_zero_with_positive(self, calc):
        """Test subtracting zero with positive number."""

        # Arrange
        a = 0
        b = 3
        expected = -3

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_zero_with_negative(self, calc):
        """Test subtracting zero with negative number."""

        # Arrange
        a = 0
        b = -3
        expected = 3

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_floats(self, calc):
        """Test subtracting floating point numbers."""
        a = 5.5
        b = 1.1
        expected = 4.4

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_add_large_with_normal(self, calc):
        """Test adding large numbers with normal values."""
        # Arrange
        a = 1000011
        b = 1000
        expected = f"Input value {a} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.add(a, b)

        assert result.value.args[0] == expected

    def test_subtract_normal_with_large(self, calc):
        """Test subtracting large numbers with normal values."""
        a = 100
        b = 1000011
        expected = f"Input value {b} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.subtract(a, b)

        assert result.value.args[0] == expected

    def test_subtract_small_with_normal(self, calc):
        """Test subtracting small numbers."""
        a = -1000011
        b = 1000
        expected = f"Input value {a} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.subtract(a, b)

        assert result.value.args[0] == expected

    def test_subtract_normal_with_small(self, calc):
        """Test subtracting large numbers with normal values."""
        a = 100
        b = -1000011
        expected = f"Input value {b} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.subtract(a, b)

        assert result.value.args[0] == expected

    def test_subtract_max_value(self, calc):
        """Test subtracting with max value is excepted"""
        a = 1000000
        b = 1
        expected = 999999
        result = calc.subtract(a, b)
        assert result == expected

    def test_subtract_min_value(self, calc):
        """Test subtracting with min value is excepted"""
        a = -1000000
        b = 1
        expected = -1000001
        result = calc.subtract(a, b)
        assert result == expected

class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""

        # Arrange
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_numbers(self, calc):
        """Test multiplying negative numbers."""

        # Arrange
        a = -5
        b = -3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Arrange
        assert result == expected

    def test_multiply_positive_and_negative(self, calc):
        """Test multiplying positive and negative numbers."""

        # Arrange
        a = 5
        b = -3
        expected = -15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_and_positive(self, calc):
        """Test multiplying negative and positive numbers."""

        # Arrange
        a = -5
        b = 3
        expected = -15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_positive_with_zero(self, calc):
        """Test multiplying positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_with_zero(self, calc):
        """Test multiplying negative number with zero."""
        # Arrange
        a = -5
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_zero_with_positive(self, calc):
        """Test multiplying zero with positive number."""

        # Arrange
        a = 0
        b = 3
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_zero_with_negative(self, calc):
        """Test multiplying zero with negative number."""
        # Arrange
        a = 0
        b = -3
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_floats(self, calc):
        """Test multiplying floating point numbers."""
        # Arrange
        a = 2.52
        b = 3.69
        expected = 9.29

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected, rel=1e-3)

    def test_multiply_large_with_normal(self, calc):
        """Test mutiplying large numbers with normal values."""
        # Arrange
        a = 1000011
        b = 1000
        expected = f"Input value {a} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.multiply(a, b)

        assert result.value.args[0] == expected

    def test_multiply_normal_with_large(self, calc):
        """Test multiplying large numbers with normal values."""
        a = 100
        b = 1000011
        expected = f"Input value {b} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.multiply(a, b)

        assert result.value.args[0] == expected

    def test_multiply_small_with_normal(self, calc):
        """Test multiplying small numbers."""
        a = -1000011
        b = 1000
        expected = f"Input value {a} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.multiply(a, b)

        assert result.value.args[0] == expected

    def test_multiply_normal_with_small(self, calc):
        """Test multiplying large numbers with normal values."""
        a = 100
        b = -1000011
        expected = f"Input value {b} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.multiply(a, b)

        assert result.value.args[0] == expected

    def test_multiply_max_value(self, calc):
        """Test multiplying with max value is excepted"""
        a = 1000000
        b = 1
        expected = 1000000
        result = calc.multiply(a, b)
        assert result == expected

    def test_multiply_min_value(self, calc):
        """Test multiplying with min value is excepted"""
        a = -1000000
        b = 1
        expected = -1000000
        result = calc.multiply(a, b)
        assert result == expected

class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # Arrange
        a = 6
        b = 3
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_numbers(self, calc):
        """Test dividing negative numbers."""
        # Arrange
        a = -6
        b = -3
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_positive_and_negative(self, calc):
        """Test dividing positive and negative numbers."""
        # Arrange
        a = 6
        b = -3
        expected = -2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_and_positive(self, calc):
        """Test dividing negative and positive numbers."""
        # Arrange
        a = -6
        b = 3
        expected = -2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_positive_with_zero(self, calc):
        """Test dividing positive and zero numbers."""
        # Arrange
        a = 6
        b = 0
        expected = "XXCannot divide by zeroXX"

        with pytest.raises(ValueError) as result:
            calc.divide(a, b)

        assert result.value.args[0] == expected

    def test_divide_negative_with_zero(self, calc):
        """Test dividing negative and zero numbers."""
        # Arrange
        a = -6
        b = 0
        expected = "XXCannot divide by zeroXX"

        with pytest.raises(ValueError) as result:
            calc.divide(a, b)

        assert result.value.args[0] == expected

    def test_divide_zero_with_positive(self, calc):
        """Test dividing zero with positive number."""
        # Arrange
        a = 0
        b = 3
        expected = 0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_zero_with_negative(self, calc):
        """Test dividing zero with negative number."""
        # Arrange
        a = 0
        b = -3
        expected = 0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_floats(self, calc):
        """Test dividing floating point numbers."""
        a = 5.5
        b = 1.6
        expected = 3.4375

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_large_with_normal(self, calc):
        """Test dividing large numbers with normal values."""
        # Arrange
        a = 1000011
        b = 1000
        expected = f"Input value {a} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.divide(a, b)

        assert result.value.args[0] == expected

    def test_divide_normal_with_large(self, calc):
        """Test dividing large numbers with normal values."""
        a = 100
        b = 1000011
        expected = f"Input value {b} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.divide(a, b)

        assert result.value.args[0] == expected

    def test_divide_small_with_normal(self, calc):
        """Test dividing small numbers."""
        a = -1000011
        b = 1000
        expected = f"Input value {a} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.divide(a, b)

        assert result.value.args[0] == expected

    def test_divide_normal_with_small(self, calc):
        """Test dividing large numbers with normal values."""
        a = 100
        b = -1000011
        expected = f"Input value {b} is outside the valid range -1000000 to 1000000"

        with pytest.raises(InvalidInputException) as result:
            calc.divide(a, b)

        assert result.value.args[0] == expected

    def test_divide_max_value(self, calc):
        """Test dividing with max value is excepted"""
        a = 1000000
        b = 1
        expected = 1000000
        result = calc.divide(a, b)
        assert result == expected

    def test_divide_min_value(self, calc):
        """Test dividing with min value is excepted"""
        a = -1000000
        b = 1
        expected = -1000000
        result = calc.divide(a, b)
        assert result == expected

