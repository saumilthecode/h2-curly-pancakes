# LT1a Coursemology Complete Questions

- **Assessment URL:** https://yijc.coursemology.org/courses/3257/assessments/88707
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 18

## Learning outcomes

LO 2.1 	Coding Standards  
Use common coding standards for programming style (which is dependent on programming language used). 
2.1.1 	Use indentation and white space. 
2.1.2 	Use naming conventions (e.g. meaningful identifier names). 
2.1.3   Write comments (name of programmer, date written, program description and version bookkeeping/control). 

 

LO 2.2 	Programming Elements and Constructs  
Use programming language elements and constructs to write recursive and non-recursive programs to solve a variety of problems. 
2.2.1	Understand the different types: integer, real, char, string and Boolean and initialise arrays (1dimensional and 2-dimensional). 
2.2.2 	Use common library functions for input/output, strings and mathematical operations.

## Question 1: Variable assignment

You can store numbers or strings into variables and reuse it later. For example, `x = 6 `and `y = 4` and `x + y` will output 10.

As an exercise:

1) assign the values 15 and 16 to `num1` and `num2` respectively.

2) assign the strings "Yishun" and "Innova" to `str1` and `str2` respectively.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | num1 | 15 |
| num2 | 16 |
| str1 | "Yishun" |
| str2 | "Innova" |

## Question 2: Variable assignment

```
x = 2020
y = 2021
x = 2022
```

What are x and y?

## Question 3: Variable assignment

Consider the following variable assignments

```
x = 2
y = 6
x = x + 1
y = y - 2
```

What are x and y?

## Question 4: Variable assignment (integers)

Consider the assignment below:

```
a = 1
a += 2
a
>> 3
```

Notice that writing `a += 2` works the same way as` a = a + 2`, and is a convenient way to update the value of a variable. 

Study the following carefully:

```
score = 0
score += 1
match = 5
match -= 2
```

What are score and match?

## Question 5: Variable assignment (integers)

```
a = 1
b = 3
c = a + b
a = a + 5
b = 2 * b
c = a + b + c
```

What are a, b, and c?

## Question 6: Variable assignment (strings)

Consider the following:

```
a = 'apple'
b = 'ball'
c = 'cat'
a = b
c += b
```

Which of the following is/are True?

## Question 7: Variable assignment

```
name = 'John'
age =  17
name += 'ny'
age += 2
```

What are name and age?

## Question 8: Type checking

Which is the most accurate way to determine the type of a variable?

## Question 9: Type checking

Python comes with a in-built function that can help us to check the type of a variable. For example, `type('this is a string')` will output string type.

As an exercise, assign the types of `x`, `y` and `z` respectively to `x_type`, `y_type`, `z_type`. The first example has been completed for you.

Hint: Similar to numbers, you can also store types as values into variables.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | x_type | <class 'int'> |
| y_type | <class 'float'> |
| z_type | <class 'str'> |

## Question 10: Recognising the type() ?

#### [Questions 10 to 15 are linked in sequence]

What is the type() for user_data when the user enters 101 at the following command?

```
user_data = input()
```

## Question 11: Recognising the type()

Continuing from the previous question, what is the type() for user_data after following command?

```
user_data = int(user_data)
```

## Question 12: Recognising the type()

Continuing from the previous question, what is the type() for user_data after the following command?

```
user_data = user_data / 2
```

## Question 13: Recognising the type()

Continuing from the previous question, what is the type() for user_data after the following command?

```
user_data = str(user_data)
```

## Question 14: Recognising the type()

Continuing from the previous question, what is the type() for user_data after the following command?

```
user_data = 'The user has entered ' + user_data
```

## Question 15: Recognising the type()

Continuing from the previous question, what is the type() for user_data after the following command?

```
user_data = print(user_data)
```

## Question 16: Variable types

```
a = 5.0
b = 'a'
c = True
d = 3
e = "hello"
f = None
g = "3.1"
```

`What are the variable types for a, b, c, d, e, f, g?`

## Question 17: Variable types

```
d = 'dog'
e = 2.53
f = 3
```

Which of the following is/are True?

## Question 18: Variable types

```
p = '1234'
q = 5678
r = 'thousand'
```

Which of the following is False?

---

*Archive scope: complete question-facing prompts, choices, diagrams/alt text, and public test cases visible on the authenticated assessment pages. Student submissions, grades, comments, statistics, feedback, and correctness markings are excluded.*
