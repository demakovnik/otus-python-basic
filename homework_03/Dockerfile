
FROM python:3.9-bullseye

WORKDIR /app

RUN pip install --upgrade pip setuptools "poetry==1.5.1"
RUN poetry config virtualenvs.create false
COPY pyproject.toml ./
RUN poetry lock
RUN poetry install --no-root --only main
COPY . .
EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --port 8000
