FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY . .

# Ensure the virtual environment is created in a fixed path inside the container
ENV UV_PROJECT_ENVIRONMENT=/app/.venv

RUN uv sync --frozen --no-cache

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
