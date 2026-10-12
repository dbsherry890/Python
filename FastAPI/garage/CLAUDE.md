# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`garage` is an early-stage FastAPI + SQLModel app for tracking cars (makes, models, cars, service records) backed by SQLite. It is a learning project and is still being scaffolded: there are no routes, tests, or lint config yet.

It lives inside a larger git repo rooted at `/Users/ds/Coding/Python` that holds many unrelated practice projects. Keep changes, and git operations, scoped to this directory. The repo has no `.gitignore`, so `.venv/`, `__pycache__/` and `garage.db` will show up as untracked — do not stage them.

## Commands

The project is managed with `uv` (Python 3.13, see `.python-version`).

```bash
uv sync                        # install dependencies into .venv
uv add <package>               # add a dependency (updates pyproject.toml + uv.lock)
uv run fastapi dev main.py     # dev server with reload (see caveat below)
uv run python main.py          # run main() directly
```

No test runner or linter is configured. If tests are added, pytest would need to be added as a dev dependency first (`uv add --dev pytest`).

## Architecture

- `db.py` — owns the engine and session plumbing. `init_db()` calls `SQLModel.metadata.create_all(engine)`; `SessionDep` is the `Annotated[Session, Depends(get_session)]` alias routes should use for a per-request session. The SQLite URL is relative (`sqlite:///./garage.db`), so the database file is created in whatever directory the process is started from. `echo=True` logs every SQL statement.
- `models.py` — SQLModel classes, using the base/table split: a plain `...Base(SQLModel)` class carries the shared validated fields, and the `table=True` subclass adds the primary key. Follow this split for new tables so request/response schemas can inherit from the base.
- `main.py` — builds the app and wires `init_db()` into the lifespan. The `import models` line looks unused but is load-bearing: a table only exists in `SQLModel.metadata` once its class has been imported, so `create_all` would silently create nothing without it. Any new models module must be imported before `init_db()` runs.
- `keep.py` — not a module. It is a parking lot of planned models (`Make`, `Car`, `ServiceRecord`, `Tag`) with no imports, so importing it raises `NameError`. Move classes from here into `models.py` as they are implemented; `ServiceRecord` has no primary key yet and there are no relationships/foreign keys between the tables.

## Current state caveats

- `app` is created as a local variable inside `main()` in `main.py`, so there is no module-level `app` for `fastapi dev` / uvicorn to discover, and `main()` itself builds the app and returns without serving it. The app needs to be hoisted to module level before the dev server command works.
- `lifespan` is a plain generator function; FastAPI expects an async context manager (`@asynccontextmanager` on an `async def`).
