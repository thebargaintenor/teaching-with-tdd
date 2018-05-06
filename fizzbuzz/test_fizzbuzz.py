#!/usr/bin/env python3

from fizzbuzz import (
    fizzbuzz,
    is_divisible,
    is_divisible_by_3,
    is_divisible_by_5,
    is_divisible_by_15
)


def test_divisibility():
    assert is_divisible(6, 3) is True
    assert is_divisible(5, 3) is False


def test_divisibility_by_3():
    assert is_divisible_by_3(6) is True
    assert is_divisible_by_3(5) is False


def test_divisibility_by_5():
    assert is_divisible_by_5(10) is True
    assert is_divisible_by_5(11) is False


def test_divisibility_by_15():
    assert is_divisible_by_15(30) is True
    assert is_divisible_by_15(40) is False


def test_fizzbuzz():
    assert fizzbuzz(6) == 'fizz'
    assert fizzbuzz(10) == 'buzz'
    assert fizzbuzz(30) == 'fizzbuzz'
    assert fizzbuzz(19) == '19'
