# LT 6 - Tuples: Complete Coursemology Questions

- **Assessment URL:** https://yijc.coursemology.org/courses/3257/assessments/88727
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 14

## Learning outcomes and assessment context

```python
LO 2.2 	Programming Elements and Constructs  Use programming language elements and constructs to write recursive and non-recursive programs to solve a variety of problems. 2.2.1	Understand the different types: integer, real, char, string and Boolean and initialise arrays (1dimensional and 2-dimensional).
```

```python
Core skills:
1. Know that tuples are immutable.
2. Know how to construct and add (join) tuples together.
3. Know how to use indexing on a tuple.
4. Know how to iterate through elements in a tuple.
```

 

Please download the lecture slides and watch the lecture videos before attempting the lecture training!
 

- [LT6 Tuples](https://yijc.coursemology.org/courses/3257/videos/24863) (16:14)

Please feel free to post questions via the comment box tagged to the lecture video. Have fun!

---

## Question 1: Question 1

A tuple is a Python data structure that holds a sequence of values. To define a tuple, we include a list of values inside a pair of parentheses, separated by commas. If there is only one value in the tuple, a comma after the last element is required. The values inside a tuple need not be numerical - they can be strings or even some other tuples.

Please select all **valid**** tuple(s)** from the following options:

### Choices

- 1. ('C', 'T', 'C', 'C', 20, 1, 5)
- 2. ('C')
- 3. ('Grand', 'Wizard', )
- 4. {2.5, 3.5, 4.5, 3.333333333}
- 5. ('tuple', 'is', ,)
- 6. ('C',)
- 7. ('Grand', 'Wizard')

---

## Question 2: Question 2

Previously, we have dealt with string indexing. Every character in a string can be accessed by both its positive and negative indices. 
Given `my_str = 'Emmanuel'`, if you count from left to right, the characters have indices from 0 to 7.

Now if `my_tuple = ('tuple', 'is', 'simple')`, what will `my_tuple[1]`, `my_tuple[-1]` and `my_tuple[4]` return?

### Choices

- 'tuple', 'simple' and 'tuple'
- 'tuple', 'simple' and IndexError
- 'is', 'simple' and 'tuple'
- 'is', 'simple', IndexError
- 'is', 'is', IndexError
- None of the above.

---

## Question 3: Question 3

To check equality in Python, we use either `==` or `is`. The difference is that `==` checks value while `is` checks identity.

Given the code below:

```python
bar = ("a", "b")
foo = ("a", "b")
bat = bar
bar = foo
```

What will be the result for this code: `bat is foo`?

### Choices

- False
- True
- 0
- 1

---

## Question 4: Question 4

You are given that 

```python
a = 3.5
b = 3.2 + 0.3
```

What values will you get when you evaluate the following boolean expressions?
( 1, 2, 3) == (1, (2, 3))
(1, 2, 3) == (1, 2, (3))
a is b
a == b

### Choices

- False True True True
- False True False True
- False False False True
- True True False True

---

## Question 5: Question 5

Given the code below:

```python
foo = (1, 2)
bar = (3, 4)
foobar = (foo, bar)
```

Which expression should we enter to retrieve a value of `2` from the variable `foobar`?

### Choices

- foobar[0][0]
- foobar[0][1]
- foobar[1][0]
- foobar[1][1]

---

## Question 6: Average

Write a function `average(values)` that accepts a tuple values containing integer elements and returns the average value of the elements within the argument.

### Public test cases

| Expression | Expected |
|---|---|
| `average((1, 2, 3))` | `2` |
| `average((-3, 2, 8, -1))` | `1.5` |

---

## Question 7: Mid-Point

Write a function `mid_point` that accepts two sets of coordinates of points as arguments and returns a set of coordinates for the middle location of the two points.

The x- and y- coordinates of a point in the x-y plane are represented by a tuples containing two elements.

Examples of points: (1 , 1.5), (2 , -3), (-3.5 , 0). 

**Calculation of mid-point:**

The midpoint of (1,2) and (3,5) is calculated by taking the average value of x's and y's, that is ((1+3)/2 , (2+5)/2) = (2 , 3.5)

### Public test cases

| Expression | Expected |
|---|---|
| `mid_point((1, 1), (3, 3))` | `(2, 2)` |
| `mid_point((0, 1), (5, 6))` | `(2.5, 3.5)` |

---

## Question 8: Even Rank

Write a Python function called even_rank(tup) that takes in a tuple tup as the argument and returns a tuple containing all the elements of the even rank (ie the odd indices, every second element from the left) from the input tuple tup. 

For example :

even_rank(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'))

it will return ('b', 'd', 'f', 'h') .

### Public test cases

| Expression | Expected |
|---|---|
| `even_rank(('a', 'v', 'b', 'w', 'c', 'x', 'd', 'y', 'e', 'z'))` | `('v', 'w', 'x', 'y', 'z')` |
| `even_rank(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'))` | `('b', 'd', 'f', 'h')` |
| `even_rank(('every','good','boy','does','fine'))` | `('good', 'does')` |

---

## Question 9: Sum of numbers in Odd and Even indices

(This question uses the definition of Even Rank in the previous question.)

Write a function called odd_even_sums that takes in a tuple of numbers as its only argument and returns a tuple of two elements: the first is the sum of all odd-ranked numbers in the input tuple, whereas the second element is the sum of all even-ranked elements in the input.

Example execution:

odd_even_sums ((1, 3, 2, 4, 5)) will return (8, 7),

odd_even_sums ((1, )) will return (1, 0),

odd_even_sums (()) will return (0, 0).

### Public test cases

| Expression | Expected |
|---|---|
| `odd_even_sums ((1, 3, 2, 4, 5))` | `(8, 7)` |
| `odd_even_sums ((1, ))` | `(1, 0)` |
| `odd_even_sums (())` | `(0, 0)` |

---

## Question 10: Changing Tuple Value

Tuple is an immutable data type which means that once it is created, the value inside the tuple cannot be changed.

For example, if you have `t = (1, 2, 3)`, `t[2] = 10` will give you TypeError: 'tuple' object does not support item assignment.

If you want to change a particular value inside the tuple, you have to construct a new one.

Now implement a function `change_value_at_index(tup, i, value)` to return a **new tuple** with the element in the tuple tup at the index i replaced with a new value value. If the index i is out of range, then just return the original tuple tup.

**Note:** Only positive value index will be considered for this question.

### Public test cases

| Expression | Expected |
|---|---|
| `change_value_at_index((1, 2, 3), 1, -1)` | `(1, -1, 3)` |
| `change_value_at_index((1, 2, 3), 10, -1)` | `(1, 2, 3)` |
| `change_value_at_index((1, 2, 3), 0, 'huh')` | `('huh', 2, 3)` |
| `change_value_at_index((1, 2, 3, 4, 5), 4, 'huh')` | `(1, 2, 3, 4, 'huh')` |
| `change_value_at_index((1, 2, 3, 4, 5), 3, 'huh')` | `(1, 2, 3, 'huh', 5)` |
| `change_value_at_index((6, 7, 8, 9, 10), 2, 'huh')` | `(6, 7, 'huh', 9, 10)` |
| `change_value_at_index((2, 2, 3, 3, 4, 4), 2, 5)` | `(2, 2, 5, 3, 4, 4)` |

---

## Question 11: Tuple Membership

The Python keyword is is used to check if an object** identical **to an element within a tuple.

Write a function contains(obj, tup) that will check if an object obj is inside the tuple tup.

For example,

x = (1,2)

y = (3,4)

a = ((1,2),(3,4))

b = (x, (3,4))

contains(x,a) => False

contains(x,b) => True

contains(y,b) => False

You may assume that the object obj is not hidden deep within the tuple tup.

### Public test cases

| Expression | Expected |
|---|---|
| `contains(x, a)` | `False` |
| `contains(x, b)` | `True` |
| `contains(x, c)` | `True` |
| `contains(y, b)` | `False` |

---

## Question 12: Copying of a Tuple

Write a function `copy_tuple(tup)` to copy all the elements in a given tuple tup and return a new tuple.

You may assume that the given tuple tup do not contain any tuple. 

**Note: **

1. Assignment (`=`) will not copy the tuple.

2. Do not use any Python's built-in module to do the copying.

### Public test cases

| Expression | Expected |
|---|---|
| `b` | `(1, 2, 3, 4)` |
| `a==b` | `True` |
| `a is b` | `False` |

---

## Question 13: Max and Min

Functions can only return a single value but sometimes, we may want functions to return multiple values. Tuples can come in handy in such cases. We can create a tuple containing multiple values and return the tuple instead of a single value.

Write a function `max_and_min(values)` that accepts a tuple of values containing integers and returns an output tuple (largest, smallest) containing the largest and smallest integer values.

**Hint:** Use iteration to loop through each value of the tuple parameter to find the maximum and minimum values.

- Do not use any Python built-in functions, eg `max()` or `min()`.
- Do not use `max` or `min` as a variable name.

### Public test cases

| Expression | Expected |
|---|---|
| `max_and_min((1, 2, 3, 4, 5))` | `(5, 1)` |
| `max_and_min((5, -2, -3, 4, -1))` | `(5, -3)` |
| `max_and_min((2, 2))` | `(2, 2)` |

---

## Question 14: Tuple Iteration

You are given the following tuple of tuples which contains the name and age of some people:

```python
data=(("John",20), ("Gary",15), ("Chan",17), ("May",18))
```

Write function `getage(name)` which accepts the `name` of a person and performs the followings:

- iterate through the tuple to search for the tuple containing the input name.
- if found, returns the age of the person; otherwise, returns a message **'Not found'**.

Two samples of the output are given as follows:

```python
>>> getage('May')18
```

```python
>>> getage('Peter')Not found
```

### Public test cases

| Expression | Expected |
|---|---|
| `getage('May')` | `18` |
| `getage('Peter')` | `'Not found'` |

---

*Archive scope: complete prompts, choices, prompt code, diagrams/alt text, linked starter templates where supplied, and public tests. Submitted answers, grades, feedback/comments, statistics, and correct-answer markings are excluded.*
