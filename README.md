# Teaching with TDD

Test-Driven Development (TDD) is, in short, a software design process in which all behaviors are defined first as unit test, then implemented so that the tests pass.  I realize this process may seem counter-intuitive and onerous at first, but let's examine the process anyway through some short exercises.

These exercises will be written in python to keep boilerplate and overall amount of typing to a minimum.  Most of the variation between python and a "heavier" language like Kotlin, C#, or really whatever other one you pick lies within how the unit tests themselves are written (just because of the framework being different).  Apart from that, the code that we'll write through the exercises will remain very modular and will likely look very similar when ported to another language of your choice.

"But my student doesn't know Python!" you exclaim.  So?  This can also be an exercise in pair programming.  Do the driving yourself, and let the student worry only about thinking through the problem and breaking it down into manageable pieces.

### Dependencies

* Python (I used 3.6, but it really makes little difference)
* Pytest: `pip install pytest`

That's really about it.  Since the unit test framework handles all the verification of functionality, you won't even need to worry about print statements in your code until you've pieced together the whole problem, and then it should run on the first try anyway, assuming your tests were all passing.  To run your tests, say for the fizzbuzz example:

```
cd fizzbuzz
pytest
```

Easy.  Pytest will find all the unit tests (starting with `test_`) in the test files with the same prefix.  You can also run pytest on a single file to find the test methods in it, but I recommend for simplicity just keeping the tests separate for now.  If you need a little more detail down the road, [this documentation](https://github.com/pluralsight/intro-to-pytest) may help.

## Fizzbuzz

For a sequence of numbers:
* If the number is divisible by 3, print `fizz`
* If the number is divisible by 5, print `buzz`
* If the number is divisible by 15, print `fizzbuzz`

### Breaking down the problem

The fundamental operation of Fizzbuzz is determining divisibility.  Not by any particular number, but simply the general case.  Let's start by defining what we expect the behavior to be:

```python
def test_divisibility():
    assert is_divisible(6, 3) is True
    assert is_divisible(5, 3) is False
```

There are infinitely many cases, but you only need two branches to adequately capture the behavior.  Let's run it.

```
    def test_divisibility():
>       assert is_divisible(6, 3) is True
E       NameError: name 'is_divisible' is not defined

test_fizzbuzz.py:4: NameError
```

Right.  We don't have the function defined.  Let's do that.  Don't forget that you'll have to import your method into the test file.

*Remember to have your student try to reason through at least how this could look before just writing in the solution.  It's only a mod operation.  Checking equality explicitly coerces the result to a boolean.  The correct boolean.  For python (and C), nonzero values are truthy and will evaluate as such, giving you the converse of the answer you want.*

**fizzbuzz**
```python
def is_divisible(dividend, divisor):
    return dividend % divisor == 0
```

**test_fizzbuzz**
```python
from fizzbuzz import (
    is_divisible
)

def test_divisibility():
    assert is_divisible(6, 3) is True
    assert is_divisible(5, 3) is False
```

Let's run the test again.

```
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.6.4, pytest-3.4.0, py-1.5.2, pluggy-0.6.0
rootdir: /Users/tmonchamp/dev/teaching-with-tdd/fizzbuzz, inifile:
plugins: hypothesis-3.45.1
collected 1 item

test_fizzbuzz.py .                                                       [100%]

=========================== 1 passed in 0.01 seconds ===========================
```

Great! We defined the behavior, and we wrote the implementation to pass the test.  I'll omit the test output beyond this point so we don't have as much clutter here.

Now we can use this behavior to define more complex ones.  Yes, tests come first.  This might seem like too much code for this example (and it really is), but the general principle of composing functions like ths will make more sense in more complex systems.  Let's do the divisibility by 3.

```python
def test_divisibility_by_3():
    assert is_divisible_by_3(6) is True
    assert is_divisible_by_3(5) is False
```

If you run your tests again, your first test should still pass, and only this one will fail.  How will we implement this?  You shouldn't need to reinvent code you've already written.  I don't want to see any %'s in the function.

```python
def is_divisible_by_3(dividend):
    return is_divisible(dividend, 3)
```

What's that?  It still fails?  With a NameError?  Did you remember to import the method?  Go do that.  It should pass now.

Now you know everything you need to implement tests and functions for divisibility by 5 and 15.  Remember, test first, run tests, *then* implement.  Don't do it all at once.  That's a bad habit that makes you miss things.

### Fizzing and Buzzing

Now that we have the underlying pieces for divisibility covered, we can implement the rules of Fizzbuzz.  The test can simply be assertion for each of the rules in the problem:

```python
def test_fizzbuzz():
    assert fizzbuzz(6) == 'fizz'
    assert fizzbuzz(10) == 'buzz'
    assert fizzbuzz(30) == 'fizzbuzz'
    assert fizzbuzz(19) == '19'
```

Yes, that 19 was returned as a string.  Let's keep it consistent for behavior.  Python doesn't mind.  A strongly typed language would not be happy (unless you went crazy and used some union type in F#, but why did you have to do that).

At this point, this is the important step for reasoning through the logic of these rules, and how order matters for this implementation.

```python
def fizzbuzz(input):
    if is_divisible_by_15(input):
        return 'fizzbuzz'
    elif is_divisible_by_3(input):
        return 'fizz'
    elif is_divisible_by_5(input):
        return 'buzz'
    else:
        return str(input)
```

Each branch uses `return` here as printing the result works only as a side effect and isn't testable easily.  We don't want side effects.

Like I mentioned, Python doesn't really need `str(input)` as a result, and simply returning the number would be sufficient and compatible with testing.  For purposes of thinking through compatibility though, here's the same logic in Kotlin:

```kotlin
fun fizzbuzz(input: Int) = when(input) {
    isDivisibleBy15(_) -> "fizzbuzz"
    isDivisibleBy3(_) -> "fizz"
    isDivisibleBy5(_) -> "buzz"
    s -> s.toString()
}
```

The interpreter in this case is inferring the return type from the implementation and will throw a build error if the return types don't match.  Explicitly declaring a return type would only make it obvious that an inconsistent return value is present.

### Putting It All Together
We're almost there!  It's finally time to complete the problem and see if the behaviors you've implemented complete the whole problem.  Let's check 1 through 30.

```python
for i in range(1, 31):  # upper bound for range() is exclusive
    print(fizzbuzz(i))
```

And if we run it?

```
$ python fizzbuzz.py
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizzbuzz
```

Look at that!  All the rules do exactly what they were supposed to on the first run of the whole exercise.  Let's unpack the TDD process here again:

1. Define the problem's behavior
1. Define that behavior as a set of rules (composed of smaller rules as needed)
1. Implement those rules as unit tests
1. Write code so that the tests pass

If you write the correct tests for behavior, your code will behave correctly!  OK, so it sounds like a tautology, but it's important - if your tests don't cover the exact behavior you want, you can't guarantee correct functionality.  The same applies for writing code *then* testing it.  If you're writing tests based on existing code, it will be harder to prove correctness of the code or the tests.

## Caesar Cipher

Coming soon.

## Further Reading

* [TDD - Wikipedia](https://en.wikipedia.org/wiki/Test-driven_development)
* [The Way of Testivus](https://www.artima.com/weblogs/viewpost.jsp?thread=203994)
* [What Is So Wrong with TDD](https://hackernoon.com/what-is-so-wrong-with-tdd-aa60112aadd0)