# Используем базовый образ с Python 3.8
FROM python:3.9

# Копируем requirements.txt в контейнер
COPY requirements.txt /app/requirements.txt

# Устанавливаем зависимости
RUN pip install -r /app/requirements.txt

# Копируем остальные файлы исходного кода бота в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Команда, которая будет запущена при старте контейнера
CMD ["python", "bot.py"]
