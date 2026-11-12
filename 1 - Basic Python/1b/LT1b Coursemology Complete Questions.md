# LT1b Coursemology Complete Questions

- **Assessment URL:** https://yijc.coursemology.org/courses/3257/assessments/88708
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 11

## Learning outcomes

LO 2.2 	Programming Elements and Constructs  
Use programming language elements and constructs to write recursive and non-recursive programs to solve a variety of problems. 
2.2.1	Understand the different types: integer, real, char, string and Boolean and initialise arrays (1dimensional and 2-dimensional).

## Question 1: String concatenation

To concatenate strings in python, you can use the plus `+` sign.

For example, "There are 21 students my class" + " and it is great!" will become
"There are 21 students in my class and it is great!"

As an exercise, assign a string using `gunshot_single` and `car_exploded` to `guns_fired` such that `guns_fired` will have the value `'Bang!Boom!'`.

Please do not write guns_fired="Bang!Boom!" as it defeats the purpose of the question and you will be compromising your own learning.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | guns_fired | "Bang!Boom!" |

## Question 2: String concatenation (Greetings)

Strings can be concatenated by adding them together using the plus `+` sign.

The greetings in the following languages has been given (and hidden from your view) and are assigned to the following variables:

`English,`German, Malay, Korean

 

The way to generate a English greeting for Alice is:
 

```
greeting = English + "Alice" 
 
```

and the greeting will be:

```
"Good day, Alice"
```

 

Try to generate the four greetings for the four friends in each of their language.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | greeting1 | "Guten Tag, Anjali" |
| greeting2 | "Annyeonghaseyo, Kim" |
| greeting3 | "Good day, Davidson" |
| greeting4 | "Selamat Pagi, Siti" |

## Question 3: String multiplication

You can multiply strings in python using the multiplication operator: `*`

For example, `"woof!" * 3` will give `"woof!woof!woof!"`

As an exercise, fill in the answer for `fire_3_times` such that it repeats `gunshot_single` for 3 times to get `'Bang!Bang!Bang!'`

Then, fill in the answer `fire_21_times` such that it repeats `gunshot_single` for 21 times to get
`Bang!Bang!Bang!.......Bang!Bang!` where `Bang!` occurs in the string 21 times.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | fire_3_times | "Bang!Bang!Bang!" |

## Question 4: In operator

The `in` operator can be used to check whether a string is contained in another string.

e.g. `"pie" in "applepie" `will return `True`, whereas` "banana" in "applepie"` returns a `False`. 

Which of the following returns a True?

## Question 5: Comparing strings

You can compare strings in python using the comparison operator `==`. For example, `'This is one string' == 'This is one string'` will return `True`.

As an exercise, compare the string in `string_a` with `string_b` and assign the value to `comparison_result`.

Note: Do not mix it up with the assignment operator `=`.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | comparison_result | True |

## Question 6: Length of string

You can use the in-built `len` function in Python to calculate the length of a string. For example, `len('I am a short string')` will output 19.

As an exercise, assign the length of `super_long_string` to `my_length`.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | my_length | 132 |

## Question 7: Length of string

The length of a string can be determined using Python's in-built len() function. 

Make use of the len() function and comparison operators to compare the strings given below.

Please do not hard code the expected results.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | length1 | 66 |
| is_string1_longer_than_string2 | False |

## Question 8: Find and Replace

You can perform `find` and `replace` operations on strings to find and replace certain strings within another string. For example, given `my_string = 'This is my dog'`, you can use `my_string.find('dog')` to obtain the start position of the string `'dog'` in `my_string`. `my_string.find('dog')` will output 11.

You can use `my_string.replace('dog','cat')` to replace all occurrence of `'dog'` in `my_string` to `'cat'`.

As an exercise, assign the value of the position of `'dog'` in the given `long_string` to the variable `position_of_word`. Secondly, replace it with a `'cat'` and assign it to variable `replaced_long_string`.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | position_of_word | 50 |
| replaced_long_string | Whenever I get home, I will always go and find my cat first |

## Question 9: String slicing (Basic)

`s` = "Supercalifragilisticexpialidocious"

You may use Lecture Notes Page 23 to quickly identify which index number each letter is at.

Before you check which of the following is/are `True`, you may want to watch a short video clip.

## Question 10: String slicing

You can perform string slicing to remove portions of string that we may not be interested in. 

For example, given `my_recent_purchase = 'I bought a new toy but it costed me 100 dollars'` and we can do `my_recent_purchase[:18]` to only retain the characters from the start to index 17 of the string. `my_recent_purchase[9:]` will output all the characters from index 9 to the end of the string. You can use also `my_recent_purchase[2:5]` to get the characters from index 2 to 4 of the string. Try them!

As an exercise, assign the string consisting of the index 5 to index 17 (inclusive) from `long_string` to `character_from_5_to_17` using string slicing.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | character_from_5_to_17 | only interest |

## Question 11: String slicing

Consider the following strings:

```
fruit="pineapple"
tree= "mapletree"
```

The word "apple" can be obtained from the variable fruit by slicing, i.e. `fruit[4:9] or``fruit[4:] `

The word "pinetree" can be obtained by writing ` fruit[0:4] + tree[5:9]`

The word "ape" can be obtained by writing `tree[1:3] + tree[4]`

Using string slicing and concatenation, write a single line of code to construct the following words from the given string variables a, b and c:

1. "uber"

2. "microscope"

3. "establishment"

4. "antibiotics"

5. "volcanorain"

Please do not hard code the answers.

### Code template

- File: `template.py`
- The completed assessment view displayed the student's editor contents rather than a separable pristine starter file. Those submitted contents are intentionally excluded. Any starter code embedded in the prompt above is preserved.

### Public test cases

| Expression | Expected |
| --- | --- | --- | word1 | "uber" |
| word2 | "microscope" |
| word3 | "establishment" |

---

*Archive scope: complete question-facing prompts, choices, diagrams/alt text, and public test cases visible on the authenticated assessment pages. Student submissions, grades, comments, statistics, feedback, and correctness markings are excluded.*
