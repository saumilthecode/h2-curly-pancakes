# LT3b Coursemology Complete Questions

- **Assessment URL:** https://yijc.coursemology.org/courses/3257/assessments/88724
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 6

## Learning outcomes

LO 2.2 	Programming Elements and Constructs  
Use programming language elements and constructs to write recursive and non-recursive programs to solve a variety of problems. 
2.2.4 	Use functions and procedures to modularise problem into chunks of code. 
2.2.6 	Trace the steps and list the results of recursive and non-recursive programs.

## Question 1: Square Function

Write a function `square(x)` that takes in a number `x `and returns the square of it (x2)

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | square(3) | 9 |
| square(-4) | 16 |
| square(0) | 0 |

## Question 2: Area of Circle

Write a function `circle_area(circum)` that takes the circumference of a circle as input and returns its area, correct to 3 decimal places. You are to make use of the `square(x)` function that you have written in Qn 1 as a helper function. There is no need to include the square(x) function in your code as it is already included in the back end.

If a negative value is entered for circumference, return `None`.

We use from math import * to import the Python library `math`.

You may use the `round(x)` inbuilt function in Python (refer to the example here):

```
>>> a = 21.4523
>>> b = round(a, 2) # this rounds off a to 3 decimal places and stores it in b
>>> print(b)
21.45
```

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | circle_area(2*pi) | 3.142 |
| circle_area(34) | 91.992 |
| circle_area(-2*pi) | None |
| circle_area(0) | 0 |
| circle_area_calls_square | True |

## Question 3: Sum of Squares

Write a function `sum_of_squares(x, y)` which takes in 2 numbers (`x` and `y`) and returns the sum of their squares.

You are to make use of the `square(x)` function that you have written in Qn 1 as a helper function. There is no need to include the `square(x)` function in your code as it is already included in the back end.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | sum_of_squares(2, 4) | 20 |
| sum_of_squares(3, -3) | 18 |
| sum_of_squares(0.25, 0.5) | 0.3125 |
| sum_of_squares_calls_square | 2 |

## Question 4: Sum of Larger Squares

Define a function bigger_sum2(x,y,z) that takes three integers as arguments and returns the sum of the squares of the two larger numbers.

You are to make use of the `sum_of_squares(x, y)` function that you have written in Qn 4 as a helper function. 

The `square(x)`  and sum_of_squares(x, y) functions are already included in the back end.

Note: Although `min()` `max()` `sorted()` functions exist to help you identify the maximum and minimum number out of a series of numbers, for the sake of practice, DO NOT use these functions here.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | bigger_sum2(1,2,3) | 13 |
| bigger_sum2(6,-3,8) | 100 |
| bigger_sum2(3,1,-2) | 10 |
| bigger_sum2_calls_sum_of_squares>=1 | True |
| bigger_sum2(-2,-1,-3) | 5 |
| bigger_sum2(-2,-3,-10) | 13 |
| bigger_sum2(3,4,2) | 25 |

## Question 5: Get The Digit

Implement a function: 

```
def get_nth_digit(k,n):
```

that accepts a 6 digit number `k`, (i.e. 100000 <= `k` <= 999999) and a single digit `n` (i.e. 1<= `n` <=6), and returns the `n`th digit in `k`. The first digit is the digit on the right most of `k`. Check the test cases for the expected outputs of the various inputs.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | get_nth_digit(375416, 4) | 5 |
| get_nth_digit(987654, 1) | 4 |
| get_nth_digit(123456, 6) | 1 |
| type(get_nth_digit(123456, 6)) | <class 'int'> |

## Question 6: The Leap Year

Write a function `is_leap_year(year)` that uses an integer parameter year to decide whether it corresponds to a leap year, 

i.e. `is_leap_year` returns `True` if the input parameter is a leap year, and `False` otherwise. 

 

So which years are leap years? Well, accordingly to Wikipedia:
 

```
In the Gregorian calendar, the current standard calendar in most of 
the world, most years that are integer multiples of 4 are leap 
years. In each leap year, the month of February has 29 days instead of 
28. Adding an extra day to the calendar every four years compensates 
for the fact that a period of 365 days is shorter than a solar year by 
almost 6 hours. This calendar was first used in 1582. 

Some exceptions to this rule are required since the duration of a 
solar year is slightly less than 365.25 days. Over a period of four 
centuries, the accumulated error of adding a leap day every four years 
amounts to about three extra days. The Gregorian Calendar therefore 
omits 3 leap days every 400 years, omitting February 29 in the 3 
century years (integer multiples of 100) that are not also integer 
multiples of 400. For example, 1600 was a leap year, but 1700, 
1800 and 1900 were not. Similarly, 2000 was a leap year, but 2100, 
2200, and 2300 will not be. By this rule, the average number of days 
per year is 365 + 1/4 − 1/100 + 1/400 = 365.2425.
```

Think of designing a flowchart to understand this text, before you write code for it.

Check your flowchart by searching and comparing with other flowcharts online.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | is_leap_year(2000) | True |
| is_leap_year(1800) | False |
| is_leap_year(2014) | False |
| is_leap_year(2100) | False |
| is_leap_year(2104) | True |

---

*Archive scope: complete question-facing prompts, choices, diagrams/alt text, and public test cases visible on the authenticated assessment pages. Student submissions, grades, comments, statistics, feedback, and correctness markings are excluded.*
