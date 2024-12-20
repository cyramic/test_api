FROM python:3.10-slim-buster

WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY ./health_app ./health_app

WORKDIR /app/health_app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-cache --no-interaction

RUN mkdir /tmp/uploads
RUN chmod +w /tmp/uploads

# Set the environment variable to use Poetry's virtual environment
ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app

# Run the Uvicorn server
CMD ["uvicorn", "health_app.backend_api.main:app", "--host", "0.0.0.0", "--port", "8000"]