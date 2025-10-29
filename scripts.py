import subprocess
import sys


def run(cmd: str) -> None:
    """Ejecuta un comando del sistema dentro del entorno virtual de Poetry."""
    print(f"👉 Ejecutando: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)


def lint() -> None:
    """Ejecuta linters y chequeos de calidad."""
    run("black --check .")
    run("isort --check-only .")
    run("flake8 .")
    run("mypy src/")


def format() -> None:
    """Formatea el código automáticamente."""
    run("isort .")
    run("black .")


def test() -> None:
    """Ejecuta los tests unitarios."""
    run("pytest -q --maxfail=1")


def check() -> None:
    """Ejecuta lint + tests (flujo completo de validación)."""
    lint()
    test()
