[tool.poetry]
name = "python-template"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = ">=3.8.0,<3.9"
numpy = "^1.22.2"
replit = "^3.2.4"
Flask = "^2.2.0"
urllib3 = "^1.26.12"
simple-benchmark = "^0.1.0"
matplotlib = "^3.6.2"
matplotlib-terminal = "^0.1a4"
pandas = "^1.5.2"

[tool.poetry.dev-dependencies]
debugpy = "^1.6.2"
replit-python-lsp-server = {extras = ["yapf", "rope", "pyflakes"], version = "^1.5.9"}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
