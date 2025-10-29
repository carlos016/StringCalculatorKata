#!/usr/bin/env python
import pytest

"""Tests for `string_calculator_kata` package."""

from string_calculator_kata.string_calculator import StringCalculator


# Before each test, we create a new instance of StringCalculator
@pytest.fixture
def before_each() -> StringCalculator:
    """Función que se ejecuta antes de cada prueba."""
    # Configuración inicial
    return StringCalculator()


# Test adding an empty string
def test_add_empty_string(before_each: StringCalculator) -> None:
    calculator = before_each
    assert calculator.add("") == 0
    assert calculator.add() == 0
