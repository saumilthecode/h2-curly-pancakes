# LT3a Coursemology Complete Questions

- **Assessment URL:** https://yijc.coursemology.org/courses/3257/assessments/88734
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 7

## Learning outcomes

LO 2.2 	Programming Elements and Constructs  
 
Use programming language elements and constructs to write recursive and non-recursive programs to solve a variety of problems. 
2.2.4 	Use functions and procedures to modularise problem into chunks of code. 
2.2.6 	Trace the steps and list the results of recursive and non-recursive programs.

## Question 1: Question 1

Which of the following are valid function definition(s)? Select all that apply.

```
# A
def foo(a, b):
    return a + a
# B
def foo():
    return
# C
def foo:
    return b
# D
define foo(a):
    return a 
# E
def foo(a, b, c):
    a + b + c
# F
def foo(a)
return a
```

## Question 2: Question 2

Which of the following is the correct output for the code snippet below?

```
def square(x):
    return x * x
def double(x):
    return x + x
print(double(square(2)) - square(double(2)))
```

##### Trace the code before using Jupyter or Python IDLE to run the code.

## Question 3: Question 3

A particular cosmopolitan city uses three languages: English, Klingon and Elvish.

Write a function `greet(name, language)` that takes in a person's name and one of 3 languages, and returns a string greeting to the person in his/her language.

For example, 

greet('Ben', 'English') => 'Nice to meet you Ben'

greet('Mary', 'Klingon') => 'nuqneH Mary'

greet('Jenny', 'Elvish') => 'Gi suilon Jenny'

Do not use the built-in function `print()` to print the greeting, greet(name, language) should return a `string`.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | greet('David', 'English') | 'Nice to meet you David' |
| greet('Okrand', 'Klingon') | 'nuqneH Okrand' |
| greet('Elrond', 'Elvish') | 'Gi suilon Elrond' |
| greet('Ms Foo', 'English') | 'Nice to meet you Ms Foo' |
| greet('Max', 'Klingon') | 'nuqneH Max' |
| greet('Malcom', 'Elvish') | 'Gi suilon Malcom' |

## Question 4: Question 4

The function `area_rect(x, y)` returns the area of a rectangle of length `x` and breadth `y`. 

Define a function `area_square(x)` such that it:

- returns the area of a square of length `x` ,

- returns `0` if the input parameter is negative.

The area_square(x) function should make use of the provided  area_rect(x, y) function, you do not need to know how the area of a rectangular is calculated. 

Note: You must use the given function area_rect(x, y) in your solution. You need not write the code for area_rect(x, y) , it has been provided in the question.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | area_square(5) | 25 |
| area_square(-1) | 0 |
| area_square_uses_area_rect | True |

## Question 5: Question 5

You are to implement the following three functions with the following specifications:

- `is_odd(x)` returns `True` if the input parameter `x` is odd, `False` otherwise.

- `is_negative(x)` returns `True` if the input parameter `x` is negative, `False` otherwise.

- `is_even_and_positive(x)` returns `True` if the input parameter `x` is even AND positive, `False` otherwise.

You should try to reuse the functions whenever possible!

Note: 0 is neither a positive nor a negative number.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | is_odd(1) | True |
| is_negative(1) | False |
| is_even_and_positive(1) | False |
| is_even_and_positive(-4) | False |
| is_even_and_positive(4) | True |
| is_even_and_positive(0) | False |

## Question 6: Question 6

```
def bool_eval(x):
    if x :
        return True
    else:
        return False
```

```
def str_eval(x):
    if x :
        return 'True' 
    else:
        return 'False'
```

Which of the following expressions return the boolean `True` when evaluated?

Note: Although the string 'True' and the boolean `True` are different, 

print('True') and print(`True`) produce outputs that are indistinguishable.

## Question 7: Question 7

Which of the following is the correct output for the code snippet below?

```
x = 2
def square(x):
    x = 3
    return x * x
print(square(x), x, square(5))
```

---

*Archive scope: complete question-facing prompts, choices, diagrams/alt text, and public test cases visible on the authenticated assessment pages. Student submissions, grades, comments, statistics, feedback, and correctness markings are excluded.*
