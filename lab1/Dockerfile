FROM python:3.13-slim

WORKDIR /app

# Устанавливаем зависимости с увеличенным таймаутом и зеркалом
RUN pip install --no-cache-dir --default-timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple django

# Копируем проект
COPY . .


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
