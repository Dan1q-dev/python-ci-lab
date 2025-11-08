# Flask Docker App

![Docker Build](https://img.shields.io/badge/docker-build%20passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Flask](https://img.shields.io/badge/flask-3.0.0-lightgrey)

## Описание проекта

Простое веб-приложение на Flask, демонстрирующее принципы **Continuous Delivery (CD)** с использованием Docker-контейнеризации. Проект показывает полный цикл от разработки до автоматического развертывания.

## Цель проекта

Научиться применять DevOps-подход Continuous Delivery и стандарты **ISO/IEC 25010** (качество ПО) и **IEEE 828** (управление конфигурацией).

## Функциональность

Приложение предоставляет следующие API endpoints:

- **GET /** — главная страница с информацией о приложении
- **GET /api/health** — проверка состояния приложения
- **GET /api/info** — информация о системе и версии
- **GET /api/time** — получение текущего времени

## Структура проекта

```
flask-docker-app/
├── .github/
│   └── workflows/
│       └── docker-build.yml    # CI/CD для Docker
├── app.py                      # Flask приложение
├── requirements.txt            # Зависимости Python
├── Dockerfile                  # Конфигурация Docker
├── .dockerignore              # Исключения для Docker
├── .gitignore
└── README.md
```

## Локальная разработка

### Запуск без Docker

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск приложения
python app.py
```

Приложение будет доступно по адресу: http://localhost:5000

### Сборка Docker образа

```bash
# Сборка образа
docker build -t flask-docker-app:latest .

# Запуск контейнера
docker run -d -p 5000:5000 --name flask-app flask-docker-app:latest

# Проверка работы
curl http://localhost:5000/api/health

# Остановка контейнера
docker stop flask-app
docker rm flask-app
```

## CI/CD Pipeline

Проект использует **GitHub Actions** для автоматизации процесса сборки и публикации:

### Этапы CI/CD:

1. **Checkout Code** — получение кода из репозитория
2. **Docker Buildx Setup** — настройка Docker для мультиплатформенной сборки
3. **Docker Hub Login** — авторизация в Docker Hub
4. **Build Docker Image** — сборка Docker образа
5. **Test Image** — тестирование образа (запуск и проверка health endpoint)
6. **Push to Registry** — публикация образа в Docker Hub

### Требуемые секреты GitHub:

- `DOCKER_USERNAME` — имя пользователя Docker Hub
- `DOCKER_PASSWORD` — пароль или токен доступа Docker Hub

## Связь со стандартами DevOps

| Этап CD | Инструмент | Стандарт | Цель стандарта |
|---------|------------|----------|----------------|
| Контейнеризация | Docker | ISO/IEC 25010 | Обеспечение качества и переносимости ПО |
| Управление конфигурацией | Dockerfile | IEEE 828 | Стандартизация конфигурации окружения |
| Автоматическая сборка | GitHub Actions | ISO/IEC 12207 | Автоматизация процессов разработки |
| Реестр образов | Docker Hub | ITIL v4 | Управление релизами и версиями |
| Тестирование | curl + health check | ISO/IEC 25010 | Контроль качества развертывания |

## Преимущества контейнеризации

- **Переносимость** — приложение работает одинаково на любой платформе
- **Изоляция** — независимость от окружения хост-системы
- **Масштабируемость** — легкое развертывание множества экземпляров
- **Воспроизводимость** — гарантированная идентичность окружения
- **Быстрое развертывание** — автоматическая сборка и публикация образов

## Автоматическое развертывание

При каждом push в ветку `main`:

1. ✅ Автоматически собирается новый Docker образ
2. ✅ Образ тестируется на работоспособность
3. ✅ Успешный образ публикуется в Docker Hub
4. ✅ Образ доступен для развертывания на любом сервере

## Использование опубликованного образа

```bash
# Скачивание и запуск образа из Docker Hub
docker pull <username>/flask-docker-app:latest
docker run -d -p 5000:5000 <username>/flask-docker-app:latest
```

## Технологический стек

- **Backend**: Flask 3.0.0
- **WSGI Server**: Gunicorn 21.2.0
- **Контейнеризация**: Docker
- **CI/CD**: GitHub Actions
- **Реестр**: Docker Hub

## Автор

Практическая работа по курсу DevOps and Continuous Integration Standards

## Лицензия

MIT License
