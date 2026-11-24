# db migrations

```bash
uv run alembic revision --autogenerate -m "Create movies table"

uv run alembic upgrade head
uv run alembic upgrade +1

uv run alembic downgrade -1
uv run alembic downgrade -2

uv run alembic history

```
