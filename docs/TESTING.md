# How to Run Tests and Add New Ones

_TODO: Add testing instructions._

## Best Practices

- All tests use `pytest` and should mirror the `src/` layout.
- Use fixtures for setup/teardown (see `11-15.md`).
- Run `pytest --cov=src` for coverage; CI will fail if coverage <90% (see `additionaltopics.md`).
- Pre-commit hooks enforce linting and formatting before tests run.

## Related Docs

- [Pre-commit & Formatting](11-15.md)
- [Makefile & Automation](16-20.md)
- [CI/CD Setup](6-10.md)
- [Modular Test Patterns](19-Modular Python Design Patterns in 16-20.md)
