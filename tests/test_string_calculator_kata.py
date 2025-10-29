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


# Test adding a non-empty string
def test_add_non_empty_string(before_each: StringCalculator) -> None:
    calculator = before_each
    assert calculator.add("0") == 0
    assert calculator.add("10") == 10
    assert calculator.add("1,2") == 3
    assert calculator.add("5,7,2") == 14
    assert calculator.add("10,20,30,40") == 100


# Test adding with invalid input that should raise an exception
def test_add_invalid_input(before_each: StringCalculator) -> None:
    calculator = before_each
    with pytest.raises(ValueError):
        calculator.add("a")
    with pytest.raises(ValueError):
        calculator.add("1,b")
    with pytest.raises(ValueError):
        calculator.add("c,d")


# Test adding with separators other than commas
def test_add_invalid_separators(before_each: StringCalculator) -> None:
    calculator = before_each
    with pytest.raises(ValueError):
        calculator.add("1|2|3")
    with pytest.raises(ValueError):
        calculator.add("1;2;3")
    with pytest.raises(ValueError):
        calculator.add("1.2.3")
