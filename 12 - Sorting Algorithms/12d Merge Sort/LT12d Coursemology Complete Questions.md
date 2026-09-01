# LT 12d  Merge Sort - Complete Coursemology Questions

- **Source URL:** https://yijc.coursemology.org/courses/3257/assessments/88732
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 8
- **Learning outcomes:** 1.2 Fundamental Algorithms1.2.1 Implement sort algorithms (insertion sort, bubble sort, quicksort, merge sort)1.2.2 Use examples to explain sort algorithms1.2.5 Compare and describe the efficiencies of the sort and search algorithms using Big-O notation for time complexity (worst case).

## Assessment overview

**Learning Outcomes**
**1.2 Fundamental Algorithms**
1.2.1 Implement sort algorithms (insertion sort, bubble sort, quicksort, merge sort)
1.2.2 Use examples to explain sort algorithms
1.2.5 Compare and describe the efficiencies of the sort and search algorithms using Big-O notation for time complexity (worst case).

**Core Skills**

1. Understand and explain how merge sort works with relevant examples
2. Implement merge sort in code

Please download the lecture slides and watch the lecture videos before attempting the lecture training!

- [Unplugged activity for Merge Sort](https://youtu.be/jZW0W4RgBog) (4:20)
- [LT12 Merge Sort](https://yijc.coursemology.org/courses/3257/videos/24833) (2:31)
- [Time Complexity](https://yijc.coursemology.org/courses/3257/videos/24835) - Merge Sort vs Bubble Sort (4:31)
- [Merge Sort with Folk Dance](https://www.youtube.com/watch?v=XaqR3G_NVoo) (Optional: play at 1.5x speed)

![Diagram (no alt text provided)](https://yijc.coursemology.org/attachments/e5c04148-e43b-42e8-a88d-76389cf60dca)

We will be using videos and cards to learn the sorting algorithm with examples. We will try to explain and elaborate on how the algorithm works.

Please feel free to post questions via the comment box tagged to the lecture video. Have fun!

## Question prompts

### Question 1: Core Skill 1a : Splitting a List into Two

- **Type:** Programming

Write a function split(seq) which will split a list into two and return the output as a tuple of lists.

Note : If the list contains only one element, then it will return the list as it is.

#### Public test cases

| Expression | Expected |
|---|---|
| `split([5, 2, 1, 8, 9])` | `([5, 2], [1, 8, 9])` |
| `split([1])` | `[1]` |
| `split([1, 8, 9])` | `([1], [8, 9])` |
| `split([5, 2, 1, 8])` | `([5, 2], [1, 8])` |

### Question 2: Core Skill 1b : Splitting the List Recursively

- **Type:** Programming

Modify the function split(seq) , written in Question 1, such that it will split the list into two recursively until all the lists contain only one element.

The output is a tuple of nested lists.

Note : If the list contains only one element, then it will return the list as it is.

#### Public test cases

| Expression | Expected |
|---|---|
| `split([5, 2, 1, 8, 9])` | `(([5], [2]), ([1], ([8], [9])))` |
| `split([1])` | `[1]` |
| `split([1, 8, 9])` | `([1], ([8], [9]))` |

### Question 3: Seeing the 'Tree'

- **Type:** TextResponse

After splitting the list [5, 2, 1, 8, 9] into (([5], [2]), ([1], ([8], [9]))), draw a tree diagram to show how this nested list looks like. (You may refer to your lecture notes)

You can use [https://app.diagrams.net/](https://app.diagrams.net/) to draw boxes and lines.

### Question 4: Core Skill 2a : Merging

- **Type:** Programming

Write a helper function merge(left, right) to merge the two lists, left and right, such that the elements are arranged in ascending order.

Note that left and right both have only 1 element each.

#### Public test cases

| Expression | Expected |
|---|---|
| `merge([8], [9])` | `[8, 9]` |
| `merge([5], [2])` | `[2, 5]` |

### Question 5: Core Skill 2b : Merging

- **Type:** Programming

Modify the helper function merge(left, right) written in **Question 4** so that it can merge the two sorted lists, left and right, note that **one of the two lists**, either left or right will contain more than 1 element, but not both.

The resulting list will be sorted increasingly.

Note: The single element list contains the smallest element.

#### Public test cases

| Expression | Expected |
|---|---|
| `merge([1], [8,9])` | `[1, 8, 9]` |
| `merge([8,9], [1])` | `[1, 8, 9]` |

### Question 6: Core Skill 2c : Merging

- **Type:** Programming

Modify the helper function merge(left, right) written in **Question 5** so that it can merge the two lists, left and right, note that both the two lists, left and right, contain more than 1 element.

#### Public test cases

| Expression | Expected |
|---|---|
| `merge([2, 5],[1,8,9])` | `[1, 2, 5, 8, 9]` |
| `merge([2,6,7], [9,10])` | `[2, 6, 7, 9, 10]` |

### Question 7: Putting them together : merge_sort(seq)

- **Type:** Programming

Use or modify the following:

1. the helper function merge(left, right) written in Question 6;

2. the helper function split(seq) written in Question 2;

and write a program code that will perform the merging after splitting the sequence and name it merge_sort(seq).

#### Public test cases

| Expression | Expected |
|---|---|
| `merge_sort([5, 2, 1, 8, 9])` | `[1, 2, 5, 8, 9]` |

### Question 8: Describe Merge Sort

- **Type:** RubricBasedResponse

Describe how Merge Sort will sort an array of numbers.

Use the keywords : **divide**, **merge**, **repeat** to assist in your explanation.

## Linked code template notebook cells

Starter-code cells copied read-only from the assessment-linked local template notebook(s). Notebook outputs and walkthrough-solution notebooks are excluded.

### LT12d.ipynb

#### Code cell 1

```python
def split(seq):              # return a tuple
    if len(seq) >1:
        l = len(seq)//2
        return(seq[:l],seq[l:])
    else:
        return seq


print(split([5, 2, 1, 8, 9])==([5, 2], [1, 8, 9]))
split([5, 2, 1, 8, 9])
```

#### Code cell 2

```python
def split(seq):              # return a tuple
    if len(seq) > 1:
        middle = len(seq) // 2
        return (split(seq[:middle]), split(seq[middle:]))
    else:
        return seq


print(split([5, 2, 1, 8, 9])==(([5], [2]), ([1], ([8], [9]))))
```

#### Code cell 3

```python
def merge(left, right):    # if left and right only has 1 element each
    if left[0] < right[0]:
        return [left[0],right[0]]
    else:
        return [right[0],left[0]]


print(merge([8], [9])==[8, 9])
print(merge([5], [2])==[2, 5])
merge([8], [9])
```

#### Code cell 4

```python
def merge(left, right):  # if left or right has more than 1 element, but not both
    merged = []

    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged += left
    merged += right

    return merged

print(merge([1], [8,9])==[1, 8, 9])
print(merge([8,9], [1])==[1, 8, 9])
```

#### Code cell 5

```python
def merge(left, right):
    merged = []

    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged += left
    merged += right

    return merged


print(merge([2, 5],[1,8,9])==[1, 2, 5, 8, 9])
print(merge([2,6,7], [9,10])==[2, 6, 7, 9, 10])
```

#### Code cell 6

```python
def split(seq):              # return a tuple
    if len(seq) > 1:
        middle = len(seq) // 2
        return (split(seq[:middle]), split(seq[middle:]))
    else:
        return seq

def merge(left, right):
    merged = []

    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged += left
    merged += right

    return merged
```

#### Code cell 7

```python
# def merge_sort(seq):
#     if type(seq) == list:
#         if len(seq) <= 1:
#             return seq
#         seq = split(seq)
#     left, right = seq
#     return merge(merge_sort(left), merge_sort(right))

def merge_sort(seq):
    if len(seq) == 1:
        return seq
    else:
        mid = len(seq)//2
        left = seq[:mid]
        right = seq[mid:]
        return merge(merge_sort(left),merge_sort(right))

print(merge_sort([5, 2, 1, 8, 9]))
```

#### Code cell 8

```python
def sort_age_m(lst):
    pass


#####Do not remove
seq1=[("M", 23), ("F", 19), ("M", 30)]
seq2=[("F", 18), ("M", 23), ("F", 19), ("M", 30)]
seq3=[("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq4=[("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
```

#### Code cell 9

```python
def merge_lists(list1, list2):
    pass
```
