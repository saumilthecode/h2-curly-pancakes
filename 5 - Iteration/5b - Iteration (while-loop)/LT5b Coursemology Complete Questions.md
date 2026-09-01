# LT 5b - Iteration (while-loop) (2025): Complete Coursemology Questions

- **Assessment URL:** https://yijc.coursemology.org/courses/3257/assessments/88729
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 8

## Learning outcomes and assessment context

```python
LO 1.1 	Algorithmic Representation
Write algorithms in pseudo-code and flowchart for given problems.
1.1.3 	Use a combination of various control structures

LO 2.2 	Programming Elements and Constructs
Use programming language elements and constructs to write recursive and non-recursive programs to solve a variety of problems.
2.2.2 	Use common library functions for input/output, strings and mathematical operations.
2.2.3 	Apply the fundamental programming constructs to control the flow of program execution: – Sequence – Selection – Iteration
2.2.4 	Use functions and procedures to modularise problem into chunks of code.
2.2.6 	Trace the steps and list the results of recursive and non-recursive programs.
```

 

```python
Core Skills:1. Able to explain iteration, and its components2. Able to examine code to identify iteration, and its components3. Able to identify and use while-loops4. Set meaningful terminating conditions for while-loops5. Use iteration to present data in a readable structure
```

Please download the lecture slides and watch the lecture videos before attempting the lecture training!

- [Iteration : While-loop](https://yijc.coursemology.org/courses/3257/videos/24767/attempt) (18:18)

Please feel free to post questions via the comment box tagged to the lecture video. Have fun!

(You should practice using while-loop, to do all the questions.)

---

## Question 1: while-loop

When must you use a while-loop over a for-loop?

### Choices

- 1. When there is a counter
- 2. When I don't know how many times I want to loop
- 3. When I am writing code to simulate eating: while I am hungry(), I take_a_bite()
- 4. When I need to compute where to start and where to stop.

### Starter code / linked template

```python
#From the four statements, there can be more than 1 correct statement. You may record your notes here.
```

---

## Question 2: Question 2

Write an iterative program `print_to(n)` that prints numbers from 0 to `n``` inclusive of `n`.

There is no need to return.
You must use a while-loop to do this.

### Starter code / linked template

```python
def print_to(n):
    pass
```

### Public test cases

| Expression | Expected |
|---|---|
| `printoutcontains0to8` | `True` |

---

## Question 3: loop: break

This question is a code-tracing practice. Please trace the code manually before verifying the answers using Jupyter.

You may make use of python tutor to help you trace the code:

[http://pythontutor.com/visualize.html#mode=edit](http://pythontutor.com/visualize.html#mode=edit)

What's the output of the code below?

```python
def foo():    i = 0    result = 0    while i < 10:        if i == 3:            break        result = result + i        i = i + 1    return resultprint(foo())
```

### Choices

- 1
- 2
- 3
- 6
- 10

### Starter code / linked template

```python
#Trace the code in the question, keeping track of i and result
#                   result   i
#                   ======  ===
#    Start         :   0     0  (Setup for you)
#After 1 iteration :   ?     ? 
#After 2 iterations:   ?     ?
#After 3 iterations:   ?     ?
#After 4 iterations:   ?     ?
```

---

## Question 4: Question 4

The following function takes an input `n` and calculate the n-factorial to return the value of `1 * 2 * 3 * … * n`.

What's wrong with the code below? Fix the code so that it passes all test cases. 

```python
def factorial(n):  #n is positive integer n>=1    i = 1    result = 0         while i <= n:        result = result * i    return result
```

You may assume that `n` is always positive (ie. `n` >= 1). 

Hint: There are more than 1 mistakes. You must use the `while` loop iteration for this question.

Warning: DO NOT TEST IN COURSEMOLOGY.
An infinite-loop in your code can slow down coursemology. Test cases will be useless and give no feedback.
Test in Jupyter Notebook first, before finalising your submission in coursemology.

### Starter code / linked template

```python
def factorial(n):  #Debug this function. There are more than 1 mistakes.
    i = 1
    result = 0     
    while i <= n:
        result = result * i
    return result
```

### Public test cases

| Expression | Expected |
|---|---|
| `factorial(1)` | `1` |
| `factorial(5)` | `120` |
| `factorial(10)` | `3628800` |

---

## Question 5: Question 5

Define an iterative function `compute(x, n)` that takes two input arguments, `x` and `n`, that returns `x` raise by the exponent `n`, where `n` is an integer greater or equal to 0. Use** while loop for this task. **

For example, when x = 5 and n = 2, `compute(5, 2)` should return 52 = 25.

**Note: You should not be using the math operator ** to calculate the value.**

### Starter code / linked template

```python
def compute(x, n):
    pass
```

### Public test cases

| Expression | Expected |
|---|---|
| `compute(1,0)` | `1` |
| `compute(2,3)` | `8` |
| `compute(5,2)` | `25` |
| `compute(2,5)` | `32` |
| `compute(-5,3)` | `-125` |

---

## Question 6: Question 6

Without using the Python's built-in `math` module, write an iterative function `powers_of_two(n)` that takes in the value `n` which is some number that is a power of two, and return its exponent. 

Eg.
Since 16 is 24, `powers_of_two(16)` should return 4.

Another way of saying this is,

 16 can be consecutively divided by 2 until it becomes the number 1. Output the number of times it has been divided and the answer is 4.

You are to use a while loop to do this question.

### Starter code / linked template

```python
def powers_of_two(n):
    pass
```

### Public test cases

| Expression | Expected |
|---|---|
| `powers_of_two(1)` | `0` |
| `powers_of_two(2)` | `1` |
| `powers_of_two(4)` | `2` |
| `powers_of_two(8)` | `3` |
| `powers_of_two(16)` | `4` |
| `powers_of_two(32)` | `5` |
| `powers_of_two(64)` | `6` |
| `powers_of_two(128)` | `7` |

---

## Question 7: When will I be a millionaire?

Write a function `millionaire(amount)` that takes in the variable `amount` as the starting amount of money.

Every year, the amount of money increases from the interest rate, fixed as 5%.

Your function should return the number of years it takes for the amount to grow to $1000000.

Some sample test cases are provided for you as follows:
millionaire(1000000) should return 0 since you are already a millionaire
millionaire(999999) should return 1 since you need 1 year to elapse to bank in the interest.

### Starter code / linked template

```python
def millionaire(amount):
    pass
```

### Public test cases

| Expression | Expected |
|---|---|
| `millionaire(1000000)` | `0` |
| `millionaire(999999)` | `1` |
| `millionaire(555555)` | `13` |
| `millionaire(100000)` | `48` |
| `millionaire(10000)` | `95` |

---

## Question 8: Sum or Subtract

Write an iterative function `fn(n)` that uses a **while loop** and takes an argument `n`.

Iterate a number from 2 to `n`, inclusive.

Initialise a variable `total` with 0,

- If the number is a multiple of 2 or 3, add it to the `total`.
- Otherwise, subtract the number from the `total`.
- Return the `total` at the end of the iteration.

For example:

`fn(2)` = 2           #iterate from 2 to 2 and stop. 2 is a multiple of 2, so add it to `total` and return 2.

`fn(3)` = 5           #iterate from 2 to 3. Since 2 and 3 are multiple of 2 or 3, add them to `total` and return 2+3=5.

`fn(4)` = 9           #iterate from 2 to 4. Since 2, 3 and 4 are all multiples of 2 or 3, add them to `total` and return 2+3+4=9.

`fn(5)` = 4           #iterate from 2 to 5. Since 2, 3 and 4 are all multiples of 2 or 3, add them to `total`. The value 5 should be subtracted from the `total`, hence return 2+3+4-5=4.

### Starter code / linked template

```python
def fn(n):
    pass
```

### Public test cases

| Expression | Expected |
|---|---|
| `fn(2)` | `2` |
| `fn(4)` | `9` |
| `fn(5)` | `4` |
| `fn(6)` | `10` |
| `fn(9)` | `20` |

---

*Archive scope: complete prompts, choices, prompt code, diagrams/alt text, linked starter templates where supplied, and public tests. Submitted answers, grades, feedback/comments, statistics, and correct-answer markings are excluded.*
