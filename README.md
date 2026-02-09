# FastAPI + SQLAlchemy + Alembic Template

A production-ready template for building scalable APIs with FastAPI, SQLAlchemy 2.0 (Async), and Alembic, managed by `uv`.

## 🚀 Features

- **FastAPI**: Modern, fast (high-performance) web framework.
- **SQLAlchemy 2.0**: Async database operations with typed models.
- **Alembic**: Database migrations with async support.
- **uv**: Extremely fast Python package manager and resolver.
- **Docker Compose**: Ready for development with PostgreSQL 18 and **Hot Reload** enabled.
- **Clean Architecture**: Decoupled layers (Domain, Application, Infrastructure).
- **Unit of Work Pattern**: Automatic transaction management via `UnitOfWorkWrapper`.
- **Makefile**: Shortcuts for common development tasks.

## 🏗️ Project Structure

```text
src/
├── api_router.py           # Global API router registration
├── config.py               # Pydantic Settings
├── database.py             # SQLAlchemy engine and session setup
├── main.py                 # FastAPI application entry point
├── shared/                 # Shared infrastructure and utilities
│   └── infrastructure/sqlalchemy/uow.py  # Unit of Work implementation
└── users/                  # Example Module
    ├── application/        # Use Cases
    ├── domain/             # Entities and Repository interfaces
    └── infrastructure/     # API Controllers and Persistence (ORM)
```

## 🛠️ Getting Started

### 1. Prerequisites
- [Docker](https://www.docker.com/) and Docker Compose.
- [uv](https://github.com/astral-sh/uv) (optional, for local development).

### 2. Start with Docker
```bash
make start
```
The API will be available at `http://localhost:8010`.

### 3. Database Migrations
Create a migration:
```bash
make migrate-create msg="initial migration"
```
Apply migrations:
```bash
make migrate-up
```

## 🧪 Example API Usage

**Create a User:**
```bash
curl -X POST http://localhost:8010/users \
     -H "Content-Type: application/json" \
     -d '{"email": "hello@example.com"}'
```

## 📜 Makefile Commands

| Command | Description |
|---------|-------------|
| `make start` | Start services in background |
| `make build` | Rebuild and start services |
| `make stop` | Stop services |
| `make migrate-create msg="..."` | Create a new Alembic migration |
| `make migrate-up` | Apply all pending migrations |
| `make migrate-down` | Rollback last migration |
| `make logs` | Tail logs |

## 🛡️ Unit of Work Wrapper

This template uses a `UnitOfWorkWrapper` to automatically handle database transactions. When a Use Case method is wrapped, it will:
1. Execute the business logic.
2. `commit()` automatically if successful.
3. `rollback()` automatically if an exception is raised.

This ensures your Application layer remains pure and doesn't need to know about SQLAlchemy sessions.
