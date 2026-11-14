# LT8 Coursemology Complete Questions

- **Assessment:** LT 8 - Dictionary
- **Source URL:** https://yijc.coursemology.org/courses/3257/assessments/88714
- **Extraction date:** 2026-09-01 (Asia/Singapore)

## Learning outcomes

- **LO 1.2, Programming Constructs:** Use programming language elements and constructs to write recursive and non-recursive programs to solve a variety of problems.
- **1.2.5:** Use Python lists and dictionaries for performing insertion, lookup, update and deletion.
- **1.2.1:** Know and apply the different data types: integers, floating-point numbers, strings and Booleans.
- **1.2.3:** Use abstraction through functions and procedures to modularise problems into chunks of code for reusability and clarity.
- Know that dictionaries are mutable.
- Know how to construct a dictionary, add elements to it and remove elements from it.
- Know how to access keys and values in dictionaries.
- Know how to iterate through the elements in a dictionary.

---

## Question 1: Constructing empty dict

Which of the following are correct ways of creating an empty dictionary? Select all that apply.

- [ ] `{( )}`
- [ ] `{ }`
- [ ] `dict.empty()`
- [ ] `dict()`
- [ ] `dict{}`

## Question 2: Implementing dict (part 1)

Which of the following are correct implementations of a dictionary? Select all that apply.

- [ ] `{2, "apples", (0, 0)}`
- [ ] `{(2, 4), (5, 7)}`
- [ ] `{2:4, 4:6}`
- [ ] `{"biscuit":{"hello":"panda"} }`

## Question 3: Implementing dict (part 2)

Which of the following are correct ways to define and implement a dictionary? Select all that apply.

- [ ] `dict(2: 4)`
- [ ] `dict( (2, 4) )`
- [ ] `dict( (2, 4), )`
- [ ] `dict( ( (2, 4), ) )`
- [ ] `dict( [ (2, 4), ("red", "apple") ] )`
- [ ] `dict( ( [2, 4], ) )`
- [ ] `dict( [ [2, 4], [5, 8] ] )`

## Question 4

Consider the assignment statement:

```python
cat = {'name': 'kitty', 'age': 4, 'stats': {'ht': 12.5, 'wt': 3.7}}
```

Select the expression(s) that evaluate to `True`.

- [ ] `cat['wt'] == 3.7`
- [ ] `cat['name'] == 'kitty'`
- [ ] `'age' in cat`
- [ ] `'kitty' in cat`
- [ ] `cat['age'] > cat['wt']`
- [ ] `cat['age'] < cat['stats']`
- [ ] `cat['age'] < cat['stats']['ht']`

## Question 5

Given the dictionary `roman = {'I': 1, 'II': 2}`, write a line of code to include the key `'III'` and value `3` in the dictionary such that `roman` becomes `{'I': 1, 'II': 2, 'III': 3}`.

**Note:** Assigning `{'I': 1, 'II': 2, 'III': 3}` to `roman` directly is **not** a valid answer.

### Code template

```python
# You may assume that the line of code below was given/executed already
# roman = {'I': 1, 'II': 2}
# Now write a line of code below to include
# the key 'III' with value 3 into the above dictionary roman:
```

### Public test cases

| Expression | Expected |
|---|---:|
| `len(roman)` | `3` |
| `roman == {'I':1,'II':2,'III':3}` | `True` |

## Question 6

```python
scores = {'Phys': (71, 'A'), 'Maths': (56, 'C'), 'Chem': 0}
```

The dictionary `scores` uses the subject as the key to store the result value in a tuple containing the marks and grade obtained.

The value for `'Chem'` is currently `0`. Write a line of code to amend the result to 43 marks and a grade `'C'`.

**Note:** Assigning `{'Phys': (71, 'A'), 'Maths': (56, 'C'), 'Chem': (43, 'S')}` directly to `scores` is **not** a valid answer.

### Code template

```python
# You may assume that the line of code below was given/executed already
# scores = {'Phys': (71, 'A'), 'Maths': (56, 'C'), 'Chem': 0}
# Write a line of code below to change the
# value for 'Chem' to (43, 'S') in the above dictionary scores:
```

### Public test cases

| Expression | Expected |
|---|---:|
| `type(scores['Chem'])` | `<class 'tuple'>` |
| `scores == {'Phys': (71, 'A'), 'Maths': (56, 'C'), 'Chem': (43, 'S')}` | `True` |

## Question 7

Given the dictionary `scores = {'Phys': (71, 'A'), 'Maths': (56, 'C'), 'Chem': 0}`, write a line of code to remove the entry for `'Chem'` such that `scores` becomes `{'Phys': (71, 'A'), 'Maths': (56, 'C')}`.

**Note:** Assigning `{'Phys': (71, 'A'), 'Maths': (56, 'C')}` directly to `scores` is **not** a valid answer.

### Code template

```python
# You may assume that the line of code below was given/executed already
# scores = {'Phys': (71, 'A'), 'Maths': (56, 'C'), 'Chem': 0}
# Write a line of code below to remove the entry for 'Chem'
# in the above dictionary scores.
```

### Public test cases

| Expression | Expected |
|---|---:|
| `len(scores)` | `2` |
| `scores == {'Phys': (71, 'A'), 'Maths': (56, 'C')}` | `True` |

## Question 8: Increase the quantity of an item in the Dictionary

A fast food restaurant sells three types of burger: ham, chicken and fish burgers. The number of each type sold is kept in a dictionary:

```python
burger = {'ham': 47, 'chicken': 75, 'fish': 27}
```

Write a function `add(item, qty)` such that the number of a particular type of burger sold is increased by `qty`.

The function should return the mutated dictionary `burger`.

### Code template

```python
burger = {'ham': 47, 'chicken': 75, 'fish': 27}  # Do not modify this line

def add(item, qty):
    pass
```

### Public test cases

| Expression | Expected |
|---|---|
| `add('fish', 5)` | `{'ham': 47, 'chicken': 75, 'fish': 32}` |
| `add('chicken', 20)` | `{'ham': 47, 'chicken': 95, 'fish': 32}` |

## Question 9: Iterate through a dictionary

What is the output when the following code is executed?

```python
fruits = {'apple': 4, 'orange': 9, 'banana': 3, 'pear': 7}
for fruit in fruits:
    print(fruit)
```

Options:

- [ ] `apple`
- [ ] `orange`
- [ ] `banana`
- [ ] `pear`
- [ ] `4`
- [ ] `9`
- [ ] `3`
- [ ] `7`
- [ ] `apple:4`
- [ ] `orange:9`
- [ ] `banana:3`
- [ ] `pear:7`

## Question 10: Iterate through a dictionary

What is the output when the following code is executed?

```python
fruits = {'apple': 4, 'orange': 9, 'banana': 3, 'pear': 7}
for a in fruits.items():
    print(a)
```

Options:

- [ ] `apple`
- [ ] `orange`
- [ ] `banana`
- [ ] `pear`
- [ ] `4`
- [ ] `9`
- [ ] `3`
- [ ] `7`
- [ ] `('apple', 4)`
- [ ] `('orange', 9)`
- [ ] `('banana', 3)`
- [ ] `('pear', 7)`

## Question 11: Iterate through a dictionary

What is the output when the following code is executed?

```python
fruits = {'apple': 4, 'orange': 9, 'banana': 3, 'pear': 7}
for fruit in fruits:
    print(fruits[fruit])
```

Options:

- [ ] `apple`
- [ ] `orange`
- [ ] `banana`
- [ ] `pear`
- [ ] `4`
- [ ] `9`
- [ ] `3`
- [ ] `7`
- [ ] `apple:4`
- [ ] `orange:9`
- [ ] `banana:3`
- [ ] `pear:7`

## Question 12: Iterate through a dictionary - find the total

Write program code for a function `total(d)` to return the sum of all the values in the dictionary `d`.

For example:

```python
fruits = {'apple': 4, 'orange': 9, 'banana': 3, 'pear': 7}
total(fruits)  # returns 23
```

### Code template

```python
def total(d):
    pass

fruits = {'apple': 4, 'orange': 9, 'banana': 3, 'pear': 7}
```

### Public test cases

| Expression | Expected |
|---|---:|
| `total(fruits)` | `23` |

## Question 13: Iterate through a dictionary - increase all the values

Write program code for a function `increase(d)` to return the dictionary `d` with all the values increased by 1.

For example:

```python
fruits = {'apple': 4, 'orange': 9, 'banana': 3, 'pear': 7}
increase(fruits)  # returns {'apple': 5, 'orange': 10, 'banana': 4, 'pear': 8}
```

### Code template

```python
def increase(d):
    pass

fruits = {'apple': 4, 'orange': 9, 'banana': 3, 'pear': 7}
```

### Public test cases

| Expression | Expected |
|---|---|
| `increase(fruits)` | `{'apple': 5, 'orange': 10, 'banana': 4, 'pear': 8}` |

## Question 14: Counting elements into a dictionary

Write program code for a function `count(seq)` to return a dictionary with each unique element in `seq` as the key and the number of occurrences of each key as the value.

For example:

```python
lst = [1, 2, 3, 1, 1, 2, 3, 1, 1, 3, 2]
count(lst)  # returns {1: 5, 2: 3, 3: 3}
```

Do not use `<str>.count` or `<list>.count` methods.

### Code template

```python
def count(seq):
    pass

lst = [1, 2, 3, 1, 1, 2, 3, 1, 1, 3, 2]
lst2 = ['a', 'b', 'c', 'a', 'a', 'b', 'c', 'a', 'a', 'c', 'b']
```

### Public test cases

| Expression | Expected |
|---|---|
| `count(lst)` | `{1: 5, 2: 3, 3: 3}` |
| `count(lst2)` | `{'a': 5, 'b': 3, 'c': 3}` |

## Question 15: Counting words into a dictionary

A long string can be converted into a list of words using the `string.split()` method.

Write a function `count_words(paragraph)` to return a dictionary with each unique word in the paragraph as the key and the number of occurrences of each key as the value.

Do not use `<str>.count` or `<list>.count` methods.

### Code template

```python
def count_words(paragraph):
    pass

twister = '''Peter Piper picked a peck of pickled peppers
a peck of pickled peppers Peter Piper picked
if Peter Piper picked a peck of pickled peppers
where’s the peck of pickled peppers Peter Piper picked'''

count_words(twister)
```

### Public test cases

| Expression | Expected |
|---|---|
| `count_words(twister)` | `{'Peter': 4, 'Piper': 4, 'picked': 4, 'a': 3, 'peck': 4, 'of': 4, 'pickled': 4, 'peppers': 4, 'if': 1, 'where’s': 1, 'the': 1}` |

## Question 16: Counting vowels into a dictionary

Write a function `count_vowels(word)` that returns a dictionary with the vowels in the word as the keys and the number of occurrences of the vowels as the values.

Do not use `<str>.count` or `<list>.count` methods.

### Code template

```python
def count_vowels(word):
    pass
```

### Public test cases

| Expression | Expected |
|---|---|
| `count_vowels('apple')` | `{'a': 1, 'e': 1}` |
| `count_vowels('singapore')` | `{'i': 1, 'a': 1, 'o': 1, 'e': 1}` |

## Question 17: Average the elements in two dictionaries

The test results for a student are kept in the following dictionaries:

```python
studentA_CT1 = {'H1GP': 58, 'H2MA': 66, 'H2CP': 75, 'H2PH': 55, 'H1EC': 45}
studentA_CT2 = {'H1GP': 62, 'H2MA': 73, 'H2CP': 72, 'H2PH': 61, 'H1EC': 47}
```

Write a function `average(result1, result2)` to return a dictionary containing the average score for each subject.

### Code template

```python
def average(result1, result2):
    pass

# Do not modify the following:
studentA_CT1 = {'H1GP': 58, 'H2MA': 66, 'H2CP': 75, 'H2PH': 55, 'H1EC': 45}
studentA_CT2 = {'H1GP': 62, 'H2MA': 73, 'H2CP': 72, 'H2PH': 61, 'H1EC': 47}
studentB_CT1 = {'H1GP': 60, 'H2MA': 76, 'H2EC': 53, 'H2PH': 66, 'H2CH': 59}
studentB_CT2 = {'H1GP': 62, 'H2MA': 73, 'H2EC': 45, 'H2PH': 61, 'H2CH': 57}
```

### Public test cases

| Expression | Expected |
|---|---|
| `average(studentA_CT1, studentA_CT2)` | `{'H1GP': 60.0, 'H2MA': 69.5, 'H2CP': 73.5, 'H2PH': 58.0, 'H1EC': 46.0}` |
| `average(studentB_CT1, studentB_CT2)` | `{'H1GP': 61.0, 'H2MA': 74.5, 'H2EC': 49.0, 'H2PH': 63.5, 'H2CH': 58.0}` |
