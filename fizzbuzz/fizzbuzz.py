#!/usr/bin/env python3


def is_divisible(dividend, divisor):
    return dividend % divisor == 0


def is_divisible_by_3(dividend):
    return is_divisible(dividend, 3)


def is_divisible_by_5(dividend):
    return is_divisible(dividend, 5)


def is_divisible_by_15(dividend):
    return is_divisible(dividend, 15)


def fizzbuzz(input):
    if is_divisible_by_15(input):
        return 'fizzbuzz'
    elif is_divisible_by_3(input):
        return 'fizz'
    elif is_divisible_by_5(input):
        return 'buzz'
    else:
        return str(input)


for i in range(1, 31):
    print(fizzbuzz(i))
