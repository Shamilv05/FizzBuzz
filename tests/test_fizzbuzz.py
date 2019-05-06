import pytest

from src.Fizzbuzz import fizzbuzz


def test_fizzbuzz_25():
    assert(fizzbuzz(25) == "buzz")


def test_fizzbuzz_24():
    assert(fizzbuzz(24) == "fizz")


def test_fizzbuzz_33():
    assert(fizzbuzz(33) == "fizz")


def test_fizzbuzz_15():
    assert(fizzbuzz(15) == "fizzbuzz")


def test_fizzbuzz_30():
    assert(fizzbuzz(30) == "fizzbuzz")


def test_fizzbuzz_60():
    assert(fizzbuzz(60) == "fizzbuzz")


def test_fizzbuzz_17():
    assert(fizzbuzz(17) == ":( 17 :(")


def test_fizzbuzz_301():
    assert(fizzbuzz(301) == "I dont work with big and negative numbers")


def test_fizzbuzz_negative():
    assert(fizzbuzz(-5) == "I dont work with big and negative numbers")
