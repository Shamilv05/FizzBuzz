import pytest
import sys
sys.path.insert(0, '/Users/shamilv05/Documents/FizzBuzz/FizzBuzz/src')

from Fizzbuzz import fizzbuzz


def test_fizzbuzz_25():
    assert(fizzbuzz(25) == "buzz")


def test_fizzbuzz_24():
    assert(fizzbuzz(24) == "fizz")


def test_fizzbuzz_15():
    assert(fizzbuzz(15) == "fizzbuzz")


def test_fizzbuzz_17():
    assert(fizzbuzz(17) == ":( 17 :(")
