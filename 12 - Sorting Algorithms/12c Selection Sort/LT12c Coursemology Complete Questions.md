# [OPTIONAL] LT 12c Selection Sort - Complete Coursemology Questions

- **Source URL:** https://yijc.coursemology.org/courses/3257/assessments/88721
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 11
- **Learning outcomes:** (Selection Sort is NOT in the Syllabus)1.2 Fundamental Algorithms1.2.1 Implement sort algorithms (insertion sort, bubble sort, quicksort, merge sort)1.2.2 Use examples to explain sort algorithms1.2.5 Compare and describe the efficiencies of the sort and search algorithms using Big-O notation for time complexity (worst case).

## Assessment overview

Although this Selection Sort algorithm is not in the current syllabus, but since it is a rather simple algorithm, we have included it for completeness sake.

We could not discount the fact that it may be tested during the A Level exam if the pseudocode/algorithm is given in a question.

**Learning Outcomes (****Selection Sort is NOT in the Syllabus****)**
1.2 Fundamental Algorithms
1.2.1 Implement sort algorithms (insertion sort, bubble sort, quicksort, merge sort)
1.2.2 Use examples to explain sort algorithms
1.2.5 Compare and describe the efficiencies of the sort and search algorithms using Big-O notation for time complexity (worst case).

**Core Skills**

1. Understand and explain how bubble sort works with relevant examples
2. Implement bubble sort in code (ascending and descending)

Watch the lecture video

- [Selection Sort](https://yijc.coursemology.org/courses/3257/videos/24831) (7:18)
- [Selection Sort with Gypsy folk dance](https://www.youtube.com/watch?v=Ns4TPTC8whw) (Optional. Play at 1.5x Speed)

Please feel free to post questions via the comment box tagged to the lecture video. Have fun!

## Question prompts

### Question 1: Which of the following is/are true about selection sort?

- **Type:** MultipleResponse


#### Choices

- it is an in-place sort
- it involves swapping of adjacent elements
- it involves swapping of the left most element with the smallest element

### Question 2: Describe selection sort algorithm

- **Type:** RubricBasedResponse

Describe selection sort algorithm

You should use the following keywords:

unsorted, repeat, swap, smallest

### Question 3: Stability of selection_sort implementation

- **Type:** TextResponse

This shows the partial progress of the Selection Sort algorithm. Highlighted sub list represents sorted portion.

Original Sequence: 5, 3, 6, 5, 9, 2, 7 .
Smallest value found (in unsorted sub list): 2
After swapping, result: 2, 3, 6, 5, 9, 5, 7
Smallest value found: 3
After swapping, result: 2, 3, 6, 5, 9, 5, 7 (No change)
Smallest value found: 5
After swapping, result: 2, 3, 5, 6, 9, 5, 7
Smallest value found: 5
After swapping, result: 2, 3, 5, 5, 9, 6, 7
...

Comment on whether the selection sort algorithm is stable or unstable. You may use the following template to write your explanation.

The selection_sort is _____________ (stable/unstable) because ________________________________________ (reasons).

Hint : To explain whether a sort is stable or not, you must describe about the relative positions of two items having the same value.

### Question 4: Time complexity (Selection sort)

- **Type:** TextResponse

What is the worse-case time complexity for selection sort?

### Question 5: Trace Table for Selection Sort

- **Type:** FileUpload

In a WHILE loop, there is a chance that the code inside will never be executed because the checking condition is at the start of the loop.
You need to pass the condition to **enter** the loop. In python we use the while statement.

In a REPEAT-UNTIL loop, the code is always executed at least one, because the checking condition is at the end of the loop.
You need to pass the condition to **exit** the loop. In python we use the while True statement, and a if <condition>: break at the end of the loop.

Using the following psedocode for Selection Sort,

```
01: Count <- 102: WHILE Count < NumberOfItems03:     Index <- Count04:     Lowest <- MyList[Index]05:     Pointer <- Count + 106:     REPEAT07:         IF Lowest > MyList[Pointer]:08:             Lowest <- MyList[Pointer]09:             Index <- Pointer10:         ENDIF
11:         Pointer <- Pointer + 112:     UNTIL Pointer > NumberOfItems13:     14:     MyList[Count], MyList[Index] = MyList[Index], MyList[Count]15:     16:     Count <- Count + 117: ENDWHILE
```

Complete the trace table template (`"Selection+Sort+Trace+Table+template.xlsx"`)before uploading the screenshot.

### Question 6: Selecting the minimum term in a sequence

- **Type:** Programming

Without using Python's built-in min(seq) function, write a program smallest(seq) that selects and return the value of the smallest term.

#### Public test cases

| Expression | Expected |
|---|---|
| `smallest([3,5,2,6,4])` | `2` |
| `smallest(['john', 'annie', 'peter', 'siti'])` | `'annie'` |

#### Code template

**template.py**

```python
def smallest(seq):
    pass
```

### Question 7: Selecting the minimum term in a sequence, returning position

- **Type:** Programming

Modify your program smallest(seq) to return the index of the smallest term.

#### Public test cases

| Expression | Expected |
|---|---|
| `smallest([3,5,2,6,4])` | `2` |
| `smallest(['john', 'annie', 'peter', 'siti'])` | `1` |

#### Code template

**template.py**

```python
def smallest(seq):
    pass
```

### Question 8: Swap first term of sequence with minimum term

- **Type:** Programming

Write a program swap_smallest(seq) to swap the minimum term of the sequence with the first term.

#### Public test cases

| Expression | Expected |
|---|---|
| `seq1` | `[2, 5, 3, 6, 4]` |
| `seq2` | `['annie', 'john', 'peter', 'siti']` |

#### Code template

**template.py**

```python
def swap_smallest(seq):
    pass


###Do not remove/modify################
seq1= [3,5,2,6,4]
seq2=['john', 'annie', 'peter', 'siti']
swap_smallest(seq1)
swap_smallest(seq2)
```

### Question 9: Selection sort - repeat selection process

- **Type:** Programming

In selection sort, we repeatedly select the min term of the unsorted section of the sequence and swap it with first term of the unsorted section, until all terms are sorted.

Write a program selection_sort(seq) to sort a sequence using the selection sort algorithm.

#### Public test cases

| Expression | Expected |
|---|---|
| `seq1` | `[2, 3, 4, 5, 6]` |
| `seq2` | `['annie', 'john', 'peter', 'siti']` |

#### Code template

**template.py**

```python
def selection_sort(seq):
    pass


###Do not remove/modify################
seq1= [3,5,2,6,4]
seq2=['john', 'annie', 'peter', 'siti']
selection_sort(seq1)
selection_sort(seq2)
```

### Question 10: Sorting tuples (selection sort)

- **Type:** Programming

Can we sort items other than integers? For this question, you will be sorting tuples!

We represent a person using a tuple `(<gender>, <age>)`. Given a list of people, write a function `sort_age` that uses selection sort to sort the people and return a list in an order such that the older people are at the front of the list. An example of the list of people is `[("M", 23), ("F", 19), ("M", 30)]`. The sorted list would look like `[("M", 30), ("M", 23), ("F", 19)]`.

You may assume that no two members in the list of people are of the same age.

Please do not use the python built-in sort functions.

#### Public test cases

| Expression | Expected |
|---|---|
| `seq1` | `[('M', 30), ('M', 23), ('F', 19)]` |
| `seq2` | `[('M', 30), ('M', 23), ('F', 19), ('F', 18)]` |

#### Code template

**template.py**

```python
##selection sort/ non in-place

def sort_age_s(lst):
    pass


#####Do not remove
seq1=[("M", 23), ("F", 19), ("M", 30)]
seq2=[("F", 18), ("M", 23), ("F", 19), ("M", 30)]
seq3=[("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq4=[("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
sort_age_s(seq1)
sort_age_s(seq2)
sort_age_s(seq3)
sort_age_s(seq4)
```

### Question 11: Sorting tuples (selection sort with number of comparisons)

- **Type:** Programming

Modify your program to count the number of comparisons made.

Note : A comparison occurs when two values are compared.

A sample trace of the selection sort algorithm can be as follows:

![Diagram (no alt text provided)](Coursemology%20question%20assets/diagram-023.png)

#### Public test cases

| Expression | Expected |
|---|---|
| `sort_age_s(seq1)` | `3` |
| `sort_age_s(seq2)` | `6` |

#### Code template

**template.py**

```python
##selection sort/ non in-place

def sort_age_s(lst):
    pass


#####Do not remove
seq1=[("M", 23), ("F", 19), ("M", 30)]
seq2=[("F", 18), ("M", 23), ("F", 19), ("M", 30)]
seq3=[("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq4=[("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
sort_age_s(seq1)
sort_age_s(seq2)
sort_age_s(seq3)
sort_age_s(seq4)
```
