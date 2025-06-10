# Project Overview and Best Practices

This document outlines the foundational philosophy and technical best practices for building modular Python repositories.

## Philosophy

- **Fast iteration without sacrificing quality**
- **Clear boundaries between modules**
- **Keep configuration declarative where possible**

## Expert-Level Best Practices

- Use `src/` layout to prevent import ambiguity
- Prefer `pyproject.toml` for unified configuration
- Embrace static typing with `mypy`
- Automate all formatting, linting, and testing with `pre-commit` and CI
- Mirror source layout in tests
- Use `.env.example` for safe env propagation
- Add Docker and GCP compatibility for scale and deployment

This repo structure is built for projects that scale: from Raspberry Pi apps to full GCP deployments, all in one clean and maintainable scaffold.

## Where to Find Best Practices

- See `docs/additionaltopics.md` for advanced Python, CI/CD, and agent design patterns.
- Numbered guides (`docs/11-15.md`, `16-20.md`, etc.) cover pre-commit, testing, security, modularity, and scaling.
- Each topic doc links to related resources for deeper dives.

## Documentation Navigation

- [Directory Structure Guide](02-Directory_Structure_Guide.md)
- [Environment Management](03-Environment_Management_Python_Tools.md)
- [Code Style & Linting](04-Code_Style_And_Linting.md)
- [Dependency Management](05-Dependency_Management.md)
- [Testing](TESTING.md)
- [Deployment](DEPLOYMENT.md)
- [Advanced Topics](additionaltopics.md)
