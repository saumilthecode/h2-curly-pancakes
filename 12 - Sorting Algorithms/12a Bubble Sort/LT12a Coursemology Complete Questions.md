# LT 12a Bubble Sort - Complete Coursemology Questions

- **Source URL:** https://yijc.coursemology.org/courses/3257/assessments/88731
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 11
- **Learning outcomes:** 1.2 Fundamental Algorithms1.2.1 Implement sort algorithms (bubble sort, insertion sort, merge sort, quicksort)1.2.2 Use examples to explain sort algorithms1.2.5 Compare and describe the efficiencies of the sort and search algorithms using Big-O notation for time complexity (worst case).

## Assessment overview

**Learning Outcomes**
1.2 Fundamental Algorithms
1.2.1 Implement sort algorithms (bubble sort, insertion sort, merge sort, quicksort)
1.2.2 Use examples to explain sort algorithms
1.2.5 Compare and describe the efficiencies of the sort and search algorithms using Big-O notation for time complexity (worst case).

**Core Skills**

1. Understand and explain how bubble sort works with relevant examples
2. Implement the simple bubble sort algorithm (ascending and descending)

- [Bubble Sort](https://yijc.coursemology.org/courses/3257/videos/24705) ( 8:25)
- [Bubble Sort Hungarian Folk Dance (YouTube Play at 150% Speed)](https://www.youtube.com/watch?v=lyZQPjUT5B4&t=48s) (Optional)

![Diagram (no alt text provided)](https://yijc.coursemology.org/attachments/27486676-d9df-4283-ae5f-ee52675a8501)

![Diagram (no alt text provided)](https://yijc.coursemology.org/attachments/50011e80-97c0-4dfd-aabf-90648e4fe52e)

Please feel free to post questions via the comment box tagged to the lecture video.

Have fun!

## Question prompts

### Question 1: Number of passes needed

- **Type:** MultipleChoice

For the array [6,5,4,3,2,1], what is the maximum number of passes required to sort the array using the Bubble Sort algorithm?

#### Choices

- 4
- 5
- 6
- 7

### Question 2: Bubble sort algorithm

- **Type:** RubricBasedResponse

Describe a bubble sort algorithm to sort a sequence (of size n) in ascending order.

Note: You should use key words like "pass", "compare", "repeat", "adjacent" and "swap" in your description. Describe the first 3 passes to aid your explanation.

### Question 3: Concept of in-place sorting

- **Type:** MultipleResponse

Which of the following is/are true about in-place sorting of an array?

#### Choices

- Bubble sort does not require additional memory space for an additional array.
- At the end of the bubble sort, a new sorted array is created.
- The original array is mutated during the bubble sort.

### Question 4: Concept of Stability of Sorting Algorithm

- **Type:** MultipleResponse

The original array arr = [9, 4, 3, 9, 3, 1] is unsorted.

These are the possible results after sorting:

Result 1: arr = [1, 3, 3, 4, 9, 9]

Result 2: arr = [1, 3, 3, 4, 9, 9]

Result 3: arr = [1, 3, 3, 4, 9, 9]

Which of the following is/are true about stability of a sorting algorithm?

#### Choices

- a. Result 1 shows the result of a stable sort.
- b. Result 2 shows the result of a stable sort.
- c. Result 3 shows the result of a stable sort.
- d. Whether a sort is stable depends on the type of sort.
- e. Whether a sort is stable or not depends on the algorithm.

### Question 5: Time complexity (Bubble sort)

- **Type:** MultipleChoice

What is the worse-case time complexity for bubble sort?

Hint: consider a case where elements in an array are arranged in the reversed order.

#### Choices

- O(n)
- O(n2)
- O(lg n)
- O(n lg n)

### Question 6: Core Skill 1: Swap Two Adjacent Elements

- **Type:** Programming

Sorting an array involves swapping elements.

Write program code to swap two adjacent elements.

Sample execution in Python IDLE Shell:

```
>>> seq1 = [23, 12]
>>> ___missing program code___
>>> seq1
[12, 23]

>>> seq2 = [23, 12, 8]   ##swapping the second two adjacent elements
>>> ___missing program code___
>>> seq2
[23, 8, 12]
```

#### Public test cases

| Expression | Expected |
|---|---|
| `seq1` | `[12, 23]` |
| `seq2` | `[23, 8, 12]` |
| `lst` | `[0, 1, 3, 2, 4, 5, 6, 7, 8]` |
| `a` | `['a', 'b', 'c', 'e', 'd', 'f', 'g']` |

### Question 7: Core Skill 2: Swap adjacent elements down a sequence in a single pass

- **Type:** Programming

Write a function `single_pass(seq)` that takes in a sequence `seq`, scan every adjacent pair, and swap them if the first element is **larger than** the second element. Notice that this would send the largest element in `seq` to the end of the sequence. This would form the inner loop of the bubble sort program.

**Sample execution**

```
>>> seq1 = [23, 12]
>>> single_pass(seq1)
>>> seq1
[12, 23]

>>> seq2 = [23, 12, 8]
>>> single_pass(seq2)
>>> seq2
[12, 8, 23]

>>> seq3 = [23, 12, 8, 14, 17, 11, 19]
>>> single_pass(seq3)
>>> seq3
[12, 8, 14, 17, 11, 19, 23]
```

#### Public test cases

| Expression | Expected |
|---|---|
| `seq1` | `[12, 23]` |
| `seq2` | `[12, 8, 23]` |
| `seq3` | `[12, 8, 14, 17, 11, 19, 23]` |

### Question 8: Simple Bubble Sort Algorithm

- **Type:** Programming

Write program code for the function `simple_bubblesort(seq)` to sort the elements in the sequence `seq` using the following algorithm:

1. Iterate the sequence `n` number of times, where `n` is the no. of element in the sequence.

2. For each of the iteration, starting from the first element, compare 2 consecutive elements each time until the last element in the sequence.

- If the left element is larger than the right element, swap their position.
- Otherwise, do not swap the elements.

3. Return the sorted sequence at the end of `n` iteration.

#### Public test cases

| Expression | Expected |
|---|---|
| `simple_bubblesort([5,4,3,2,1,0])` | `[0, 1, 2, 3, 4, 5]` |
| `simple_bubblesort(['y', 'i', 's', 'h', 'u', 'n'])` | `['h', 'i', 'n', 's', 'u', 'y']` |

### Question 9: Improved Bubble Sort Algorithm

- **Type:** Programming

Write program code for the function `improved_bubblesort(seq)` to sort the elements in the sequence `seq` using the following algorithm:

1. Iterate the sequence `n-1` number of times (the correct number of passes), where `n` is the no. of element in the sequence.

2. For each of the iteration, starting from the first element, compare 2 consecutive elements each time. (Do not need to compare with the "largest element" of the previous iteration.)

- If the left element is larger than the right element, swap their position.
- Otherwise, do not swap the elements.

3. Return the sorted sequence at the end of `n-1` iteration.

#### Public test cases

| Expression | Expected |
|---|---|
| `improved_bubblesort([5,4,3,2,1,0])` | `[0, 1, 2, 3, 4, 5]` |
| `improved_bubblesort(['y', 'i', 's', 'h', 'u', 'n'])` | `['h', 'i', 'n', 's', 'u', 'y']` |

### Question 10: Optimised Bubble Sort Algorithm

- **Type:** Programming

Write program code for the function `optimised_bubblesort(seq)` to sort the elements in the sequence `seq` using the following algorithm:

1. Iterate the sequence `n-1` number of times, where `n` is the no. of element in the sequence.

2. For each of the iteration, starting from the first element, compare 2 consecutive elements each time. (Do not need to compare with the "largest element" of the previous iteration.)

- If the left element is larger than the right element, swap their position.
- Otherwise, do not swap the elements.

3. If there is no swapping of elements during an iteration, stop and return the sorted sequence.

#### Public test cases

| Expression | Expected |
|---|---|
| `optimised_bubblesort([5,4,3,2,1,0])` | `[0, 1, 2, 3, 4, 5]` |
| `optimised_bubblesort([5,4,0,1,2,3])` | `[0, 1, 2, 3, 4, 5]` |
| `optimised_bubblesort(['y', 'i', 's', 'h', 'u', 'n'])` | `['h', 'i', 'n', 's', 'u', 'y']` |

### Question 11: No. of Comparison for Simple, Improved and Optimized Bubble Sort

- **Type:** Programming

Write program code for the functions `simple_comparison(seq)`, `improved_comparison(seq)`, and `optimised_comparison(seq)`, using the simple, improved and optimised bubble sort algorithms respectively, to count and return the number of comparisons needed to sort the elements in `seq` in ascending order.

#### Public test cases

| Expression | Expected |
|---|---|
| `simple_comparison([5, 4, 3, 2, 1, 0])` | `30` |
| `improved_comparison([5, 4, 3, 2, 1, 0])` | `15` |
| `optimised_comparison([5, 4, 3, 2, 1, 0])` | `15` |
| `simple_comparison([5, 4, 0, 1, 2, 3])` | `30` |
| `improved_comparison([5, 4, 0, 1, 2, 3])` | `15` |
| `optimised_comparison([5, 4, 0, 1, 2, 3])` | `12` |
| `simple_comparison([3, 0, 2, 4, 1, 5])` | `30` |
| `improved_comparison([3, 0, 2, 4, 1, 5])` | `15` |
| `optimised_comparison([3, 0, 2, 4, 1, 5])` | `14` |

## Linked code template notebook cells

Starter-code cells copied read-only from the assessment-linked local template notebook(s). Notebook outputs and walkthrough-solution notebooks are excluded.

### LT12a.ipynb

#### Code cell 1

```python
###Do not remove/modify
seq1= [23, 12]
##swap the first two adjacent elements
###your swapping code here:
temp = seq1[0]
seq1[0] = seq1[1]
seq1[1]=temp


###Do not remove/modify
seq2= [23, 12, 8]
###swap the second two adjacent elements
###your swapping code here:
seq2[1],seq2[2] = seq2[2],seq2[1]

###Do not remove/modify
lst = [0,1,2,3,4,5,6,7,8]
###swap the third two adjacent elements
###your swapping code here:
lst[2],lst[3] = lst[3],lst[2]


###Do not remove/modify
a=['a','b','c','d','e','f','g']
###swap the fourth two adjacent elements
###your swapping code here:
a[3],a[4] = a[4],a[3]
```

#### Code cell 2

```python
def single_pass(seq):
    for i in range(len(seq) - 1):
        if seq[i] > seq[i + 1]:
            seq[i], seq[i + 1] = seq[i + 1], seq[i]
```

#### Code cell 3

```python
def simple_bubblesort(seq):
    for ijk in range(len(seq)):
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq


lst = [5, 4, 3, 2, 1, 0]

print(simple_bubblesort(lst))
```

#### Code cell 4

```python
def improved_bubblesort(seq):
def optimised_bubblesort(seq):
    for pass_num in range(len(seq) - 1):
        swapped = False      #swap to be false for a new pass
        for i in range(len(seq) - 1 - pass_num):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        if not swapped:
            break

    return seq


lst = [5,4,3,2,1,0]
improved_bubblesort([5,4,3,2,1,0])
```

#### Code cell 5

```python
def optimised_bubblesort(seq):
    for pass_num in range(len(seq) - 1):
        swapped = False      #swap to be false for a new pass
        for i in range(len(seq) - 1 - pass_num):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        if not swapped:
            break
    return seq

lst1 = [5,4,3,2,1,0]
lst2 = [5,4,0,1,2,3]
```

#### Code cell 6

```python
def simple_comparison(seq):
    count = 0
    for ijk in range(len(seq)):
        for i in range(len(seq) - 1):
            count += 1
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return count


def improved_comparison(seq):
    count = 0
    for pass_num in range(len(seq) - 1):
        for i in range(len(seq) - 1 - pass_num):
            count += 1
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return count


def optimised_comparison(seq):
    count = 0
    for pass_num in range(len(seq) - 1):
        swapped = False
        for i in range(len(seq) - 1 - pass_num):
            count += 1
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        if not swapped:
            break
    return count


#####Do not modify
lst1=[5, 4, 3, 2, 1, 0]
lst2=[5, 4, 0, 1, 2, 3]
```
