"""
Модуль для выполнения простых математических операций.
"""


def sum_numbers(a, b):
    """
    Вычисляет сумму двух чисел.
    
    Args:
        a (int, float): Первое число
        b (int, float): Второе число
    
    Returns:
        int, float: Сумма двух чисел
    """
    return a + b


def multiply_numbers(a, b):
    """
    Вычисляет произведение двух чисел.
    
    Args:
        a (int, float): Первое число
        b (int, float): Второе число
    
    Returns:
        int, float: Произведение двух чисел
    """
    return a * b


def is_palindrome(text):
    """
    Проверяет, является ли строка палиндромом.
    
    Args:
        text (str): Строка для проверки
    
    Returns:
        bool: True, если строка является палиндромом, иначе False
    """
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]


def calculate_rectangle_area(width, height):
    """
    Вычисляет площадь прямоугольника.
    
    Args:
        width (int, float): Ширина прямоугольника
        height (int, float): Высота прямоугольника
    
    Returns:
        int, float: Площадь прямоугольника
    
    Raises:
        ValueError: Если ширина или высота отрицательны
    """
    if width < 0 or height < 0:
        raise ValueError("Ширина и высота должны быть положительными числами")
    return width * height
