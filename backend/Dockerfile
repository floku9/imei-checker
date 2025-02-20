FROM python:3.12-slim

RUN pip install poetry

WORKDIR /imei-checker-backend
COPY pyproject.toml poetry.lock /imei-checker-backend/
RUN poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "-m", "uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
