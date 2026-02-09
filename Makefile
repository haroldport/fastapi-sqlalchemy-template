.PHONY: start stop build migrate-create migrate-up migrate-down logs

# Docker commands
start:
	docker compose up -d

stop:
	docker compose down

build:
	docker compose up --build -d

logs:
	docker compose logs -f

# Migration commands (run locally with uv)
# Usage: make migrate-create msg="initial migration"
migrate-create:
	uv run alembic revision --autogenerate -m "$(msg)"

migrate-up:
	uv run alembic upgrade head

migrate-down:
	uv run alembic downgrade -1
