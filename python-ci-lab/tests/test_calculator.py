"""
Юнит-тесты для модуля calculator.
"""
import pytest
import sys
import os

# Добавляем путь к модулю src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import sum_numbers, multiply_numbers, is_palindrome, calculate_rectangle_area


class TestSumNumbers:
    """Тесты для функции sum_numbers"""
    
    def test_sum_positive_numbers(self):
        """Тест сложения положительных чисел"""
        assert sum_numbers(5, 3) == 8
    
    def test_sum_negative_numbers(self):
        """Тест сложения отрицательных чисел"""
        assert sum_numbers(-5, -3) == -8
    
    def test_sum_mixed_numbers(self):
        """Тест сложения положительного и отрицательного числа"""
        assert sum_numbers(10, -3) == 7
    
    def test_sum_with_zero(self):
        """Тест сложения с нулем"""
        assert sum_numbers(0, 5) == 5


class TestMultiplyNumbers:
    """Тесты для функции multiply_numbers"""
    
    def test_multiply_positive_numbers(self):
        """Тест умножения положительных чисел"""
        assert multiply_numbers(4, 5) == 20
    
    def test_multiply_by_zero(self):
        """Тест умножения на ноль"""
        assert multiply_numbers(10, 0) == 0
    
    def test_multiply_negative_numbers(self):
        """Тест умножения отрицательных чисел"""
        assert multiply_numbers(-3, -4) == 12


class TestIsPalindrome:
    """Тесты для функции is_palindrome"""
    
    def test_simple_palindrome(self):
        """Тест простого палиндрома"""
        assert is_palindrome("radar") == True
    
    def test_palindrome_with_spaces(self):
        """Тест палиндрома с пробелами"""
        assert is_palindrome("А роза упала на лапу Азора") == True
    
    def test_not_palindrome(self):
        """Тест строки, которая не является палиндромом"""
        assert is_palindrome("hello") == False
    
    def test_single_character(self):
        """Тест одного символа"""
        assert is_palindrome("a") == True


class TestCalculateRectangleArea:
    """Тесты для функции calculate_rectangle_area"""
    
    def test_positive_dimensions(self):
        """Тест с положительными размерами"""
        assert calculate_rectangle_area(5, 4) == 20
    
    def test_square(self):
        """Тест квадрата"""
        assert calculate_rectangle_area(5, 5) == 25
    
    def test_zero_dimension(self):
        """Тест с нулевым размером"""
        assert calculate_rectangle_area(0, 5) == 0
    
    def test_negative_width(self):
        """Тест с отрицательной шириной"""
        with pytest.raises(ValueError):
            calculate_rectangle_area(-5, 4)
    
    def test_negative_height(self):
        """Тест с отрицательной высотой"""
        with pytest.raises(ValueError):
            calculate_rectangle_area(5, -4)
