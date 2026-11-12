# LT 4b - Types of Error and Test Cases: Complete Coursemology Questions

- **Assessment URL:** https://yijc.coursemology.org/courses/3257/assessments/88713
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 8

## Learning outcomes and assessment context

```python
LO 1.5 	Data Validation and Program Testing  Use data validation techniques and design test cases. 1.5.3 	Identify, explain and correct syntax, logic and runtime errors. 1.5.4 	Design appropriate test cases using normal, abnormal and extreme data for testing and debugging programs.
```

 

```python
Core Skills:1. Able to use print() statement for debugging.2. Able to construct test cases (using normal, boundary/Extreme or abnormal data values) for checking the functions.
```

 

Please download the lecture slides and watch the lecture videos before attempting the lecture training!

- [1. Types](https://yijc.coursemology.org/courses/2950/videos/20877)[of Error](https://yijc.coursemology.org/courses/3257/videos/24822/attempt) (6:01)
- [2. Test Cases](https://yijc.coursemology.org/courses/3257/videos/24823/attempt) (5:55)

Please feel free to post questions via the comment box tagged to the lecture video. Have fun!

---

## Question 1: Question 1

What is wrong with the portion of code below?

```python
def area(x, y):    return 1/2 * x * ytemp1 = area(2, 3)area = 3.0temp2 = area(4, 5)
```

Remove the line that causes the problem.

### Public test cases

| Expression | Expected |
|---|---|
| `temp1` | `3.0` |
| `temp2` | `10.0` |

---

## Question 2: Integer division vs Normal division

We want to implement a function to calculate the remainder of a larger integer divided by a smaller integer. The function `remainder(larger, smaller)` takes in two integers and returns the remainder of larger / smaller.

Samuel wants to write it this way:

1. Find the largest integer `k` such that `larger` = `k` * `smaller` + `r`.
2. Consider to rearrange the above equation to get `r`.
3. Return `larger` - `k` * `smaller` as the remainder

What's wrong with the implementation of his idea? Fix the code so that it passes all test cases.

You may assume that both `larger` and `smaller` are positive integers and `larger` is always larger than `smaller`.

### Public test cases

| Expression | Expected |
|---|---|
| `remainder(20, 3)` | `2` |
| `remainder(200, 5)` | `0` |
| `remainder(51, 9)` | `6` |

---

## Question 3: Question 3

Suppose we want to write a function `average(x1, x2)` that calculates the average value of two numbers `x1` and `x2`.

What's wrong with the code below?

```python
def average(x1, x2):    return x1 + x2 / 2
```

Fix it so that it generates correct output.

### Public test cases

| Expression | Expected |
|---|---|
| `average(100, 20)` | `60` |
| `average(3, 4)` | `3.5` |

---

## Question 4: Question 4

Adrian wants to swap the values of two variables. Given two variables `a=1` and `b=2`, he implemented the following method:

```python
a = b
b = a
```

However, when he printed the two variables, he realized that the values were not swapped.

```python
print(a) # => 2
print(b) # => 2
```

Please help him figure out what went wrong and fix it.

**Hint: **You may introduce a third variable, `temp`, if there is a need.

---

## Question 5: Question 5

Brian wrote a simple function in Python to check whether a year is a [leap year](http://en.wikipedia.org/wiki/Leap_year). A year is a leap year if it's divisible by 400 or divisible by 4 but not 100.

Here's his code: 

```python
def divisible(value, divider):
    if value % divider == 0:
        return true
    else:
        return false

def test_leap_year(year):
    if divisible(year, 400):
        return 'Leap year!'
    elif divisible(year, 4) and not divisible(year, 100):
        return 'Leap year!'
    else:
        return 'Not a leap year!'
```

However, he got an error when he ran it in Jupyter/IDLE.

Can you explain the reason for the error and spot the line that causes the error?

Help him to correct the code so that it can pass all test cases.

**Note:** 2016 and 2020 are both leap years.

### Public test cases

| Expression | Expected |
|---|---|
| `test_leap_year(2004)` | `'Leap year!'` |
| `test_leap_year(1904)` | `'Leap year!'` |
| `test_leap_year(1000)` | `'Not a leap year!'` |
| `test_leap_year(2014)` | `'Not a leap year!'` |
| `test_leap_year(2016)` | `'Leap year!'` |
| `test_leap_year(2020)` | `'Leap year!'` |

---

## Question 6: Question 6

Brian was very happy after he fixed his code previously.

Charles saw that his code could be further simplified since the `==` operator returns a Boolean value, so why not make it inline with Boolean operators?

Together they worked out another solution below.

```python
def test_leap_year(year):    if year % 400 == 0 or not (year % 4 == 0 and year % 100 == 0):        return 'Leap year!'    else:        return 'Not a leap year!'
```

The logic is that a leap year is either a year that is divisible by 400 or a year that is not divisible by 100 if it's divisible by 4.

This time they didn't get any error. But their code fails occasionally to produce the correct result.

Can you be the hero to help them fix the code?

**Note:** 2016 and 2020 are both leap years.

### Public test cases

| Expression | Expected |
|---|---|
| `test_leap_year(2004)` | `'Leap year!'` |
| `test_leap_year(1904)` | `'Leap year!'` |
| `test_leap_year(1000)` | `'Not a leap year!'` |
| `test_leap_year(2014)` | `'Not a leap year!'` |
| `test_leap_year(2016)` | `'Leap year!'` |
| `test_leap_year(2020)` | `'Leap year!'` |

---

## Question 7: Debug1 - Trace the Steps

There is a bug in the following code:

```python
def p1(x, y):    return p2(x, y) + p3(x, y)def p2(z, w):    return z * wdef p3(a, b):    return p2(a) + p2(b)
```

Follow the instructions given in `debug1.ipynb`

### Starter code / linked template

```python
def p1(x, y):
    return p2(x, y) + p3(x, y)

def p2(z, w):
    return z * w

def p3(a, b):
    return p2(a) + p2(b)
```

### Public test cases

| Expression | Expected |
|---|---|
| `p1(1,2)` | `7` |

---

## Question 8: Debug2 - Print Statements

There is a bug in the following code:

```python
from math import *

def quadratic (a, b, c):

    delta = b * b - 4 * a * c

    s1 = (-b - sqrt(delta)) / (2 * a)
    s2 = (-b + sqrt(delta)) / (2 * a)

    return s1, s2
```

Follow the instructions given in `debug2.ipynb`

### Starter code / linked template

```python
from math import *

def quadratic (a, b, c):

    delta = b * b - 4 * a * c

    s1 = (-b - sqrt(delta)) / (2 * a)
    s2 = (-b + sqrt(delta)) / (2 * a)

    return s1, s2
```

### Public test cases

| Expression | Expected |
|---|---|
| `quadratic(1,2,-3)` | `(-3.0, 1.0)` |
| `quadratic(548,753,162784)` | `None` |

---

*Archive scope: complete prompts, choices, prompt code, diagrams/alt text, linked starter templates where supplied, and public tests. Submitted answers, grades, feedback/comments, statistics, and correct-answer markings are excluded.*
