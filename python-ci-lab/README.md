# Python CI Lab

![CI Pipeline](https://img.shields.io/badge/CI-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Описание проекта

Проект демонстрирует применение принципов **Continuous Integration (CI)** для Python-приложения. Включает в себя простые математические функции и автоматизированное тестирование с использованием pytest.

## Цель проекта

Освоить процесс Continuous Integration на примере Python-проекта и понять, как стандарты **ISO/IEC 12207** и **IEEE 829** применяются в DevOps.

## Функциональность

Модуль `calculator.py` предоставляет следующие функции:

- **sum_numbers(a, b)** — вычисление суммы двух чисел
- **multiply_numbers(a, b)** — вычисление произведения двух чисел
- **is_palindrome(text)** — проверка, является ли строка палиндромом
- **calculate_rectangle_area(width, height)** — вычисление площади прямоугольника

## Структура проекта

```
python-ci-lab/
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD конфигурация
├── src/
│   ├── __init__.py
│   └── calculator.py       # Основной модуль
├── tests/
│   └── test_calculator.py  # Юнит-тесты
├── .gitignore
├── requirements.txt        # Зависимости проекта
└── README.md
```

## Установка и запуск

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск тестов

```bash
pytest tests/ -v
```

### Запуск тестов с покрытием кода

```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

## CI/CD Pipeline

Проект использует **GitHub Actions** для автоматизации процесса тестирования:

- ✅ Автоматическая установка зависимостей
- ✅ Запуск тестов при каждом push
- ✅ Тестирование на нескольких версиях Python (3.9, 3.10, 3.11)
- ✅ Генерация отчета о покрытии кода

## Связь со стандартами DevOps

| Этап CI | Инструмент | Стандарт | Цель стандарта |
|---------|------------|----------|----------------|
| Version Control | Git | IEEE 828 | Управление конфигурацией и версиями |
| Automated Testing | pytest | ISO/IEC 25010 | Контроль качества ПО |
| Continuous Integration | GitHub Actions | ISO/IEC 12207 | Автоматизация процессов сборки и тестирования |
| Code Coverage | pytest-cov | IEEE 829 | Документирование тестирования |

## Преимущества CI

- **Раннее обнаружение ошибок** — тесты запускаются автоматически при каждом изменении
- **Повышение качества кода** — постоянный контроль покрытия тестами
- **Ускорение разработки** — автоматизация рутинных процессов
- **Стандартизация процессов** — следование лучшим практикам DevOps

## Автор

Практическая работа по курсу DevOps and Continuous Integration Standards

## Лицензия

MIT License
