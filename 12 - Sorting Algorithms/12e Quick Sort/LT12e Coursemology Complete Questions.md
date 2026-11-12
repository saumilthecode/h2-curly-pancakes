# LT 12e Quicksort - Complete Coursemology Questions

- **Source URL:** https://yijc.coursemology.org/courses/3257/assessments/88737
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 14
- **Learning outcomes:** 1.2 Fundamental Algorithms1.2.1 Implement sort algorithms (insertion sort, bubble sort, quicksort, merge sort)1.2.2 Use examples to explain sort algorithms1.2.5 Compare and describe the efficiencies of the sort and search algorithms using Big-O notation for time complexity (worst case).

## Assessment overview

**Learning Outcomes**
**1.2 Fundamental Algorithms**
1.2.1 Implement sort algorithms (insertion sort, bubble sort, quicksort, merge sort)
1.2.2 Use examples to explain sort algorithms
1.2.5 Compare and describe the efficiencies of the sort and search algorithms using Big-O notation for time complexity (worst case).

**Core Skills**

1. Understand and explain how quicksort works with relevant examples
2. Implement quicksort in code (with either for first or last element as the pivot)

Please download the lecture slides and watch the lecture videos before attempting the lecture training!

**Unplugged Activity:**

- [Unplugged activity for Quicksort](https://yijc.coursemology.org/courses/3257/videos/24860)(4:34)

**Non In-Place Quicksort Algorithm Walkthrough:**

- [Walkthrough Question 4-5 : Non in-place Quicksort algorithm](https://yijc.coursemology.org/courses/2950/videos/20764) (6:57)

**In-Place Quicksort Algorithm Walkthrough:**

- [Quick Sort Explained (extract)](https://yijc.coursemology.org/courses/3257/videos/24834)[https://yijc.coursemology.org/courses/2380/videos/12530](https://yijc.coursemology.org/courses/2380/videos/12530)(5:46) - In-place Quicksort
- [Walkthrough Question 6-13 : in-place Quicksort algorithm](https://yijc.coursemology.org/courses/3257/videos/24769) (19:55)
  - [0:00](https://youtu.be/b-2a0q5hlCk&t=0s) Core Skill 0
  - [1:58](https://youtu.be/b-2a0q5hlCk&t=118s) Core Skill 1a
  - [2:50](https://youtu.be/b-2a0q5hlCk&t=170s) Core Skill 1b
  - [3:47](https://youtu.be/b-2a0q5hlCk&t=227s) Core Skill 1c
  - [4:25](https://youtu.be/b-2a0q5hlCk&t=265s) Core Skill 1d
  - [5:18](https://youtu.be/b-2a0q5hlCk&t=318s) Core Skill 1 (Summary)
  - [5:50](https://youtu.be/b-2a0q5hlCk&t=350s) Core Skill 2
  - [7:53](https://youtu.be/b-2a0q5hlCk&t=473s) Core Skill 3
  - [8:40](https://youtu.be/b-2a0q5hlCk&t=520s) Step 1: The `partition()` function
  - [13:47](https://youtu.be/b-2a0q5hlCk&t=827s) Step 2: The `qsort()` function using `partition()` as the helper function
  - [15:](https://www.youtube.com/watch?v=EIaVvXl_Cps&t=945s)[4](https://youtu.be/b-2a0q5hlCk&t=945s)[5](https://www.youtube.com/watch?v=EIaVvXl_Cps&t=945s) Step 3: The `quicksort()` wrapper function
  - [17:19](https://youtu.be/b-2a0q5hlCk&t=1039s) Modify `partition()` function to use first element as pivot

**Other Resources:**

- **TED-Ed video:** [What's the fastest way to alphabetize your bookshelf?](https://youtu.be/WaNLJf8xzC4) (4:38)
- [Quick Sort with Hungarian folk dance](https://www.youtube.com/watch?v=ywWBy6J5gz8) (Optional - Play at 1.5x speed)

![Diagram (no alt text provided)](Coursemology%20question%20assets/diagram-024.png)

We will be using videos and cards to learn the sorting algorithm with examples. We will try to explain and elaborate on how the algorithm works.

Please feel free to post questions via the comment box tagged to the lecture video. Have fun!

## Question prompts

### Question 1: Quicksort

- **Type:** MultipleResponse

Which of the following statement(s) about Quicksort is/are True?

#### Choices

- Most, if not all, of the commonly used implementations for Quicksort are in-place algorithms.
- Quicksort is a stable sorting algorithm.
- The best case scenario occurs when the quicksort partitions the array into two equal halves all of the time.
- The worst case occurs when the sequence is already sorted and either the first or last element is being used as the pivot.

### Question 2: The average Time Complexity for Quicksort

- **Type:** MultipleChoice


#### Choices

- O(1), because it takes the same amount of time regardless of the size of the array.
- O(n), because it requires to compare every element during the sort.
- O(log n), because of the divide and conquer approach, so it takes half the amount of time to sort.
- O(n log n), because after dividing the array by half, the quicksort algorithm needs to compare every elements in the left and right partitions.
- O(n²), because the outer loop goes through all the elements and the inner loop also goes through to compare the elements.

### Question 3: The worst case Time Complexity for Quicksort

- **Type:** MultipleResponse


#### Choices

- O(n), because the worst case scenario is like performing a linear search.
- O(n log n), because the time complexity for Quicksort is always the same regardless of how the original sequence is arranged.
- O(n²), because when the sequence is sorted and either the first or last element is used as the pivot. The quicksort algorithm will need to compare every elements after each partition.
- O(n²), because the partitioning resulted in only the left or right partition. Further partitioning also resulted in a single partition. After performing each of the `n` partitions, the algorithm needs to compare every of the `(n-1)` elements.

### Question 4: Non In-Place Quicksort : Partition the sequence once

- **Type:** Programming

Write program code `qsort(seq)` to do the following:

- use the last element of the sequence `seq` as the `pivot`
- iterate through the sequence `seq`, append all the smaller value elements into the list `left` and the larger value elements into the list `right`
- return **a tuple** containing the `left`, `[pivot]` and `right` lists.

#### Public test cases

| Expression | Expected |
|---|---|
| `qsort(random_seq)` | `([7, 2, 4, 5, 1, 6, 0, 3], [8], [])` |

### Question 5: Non In-Place Quicksort : Partition the sequence RECURSIVELY

- **Type:** Programming

Modify the program code `qsort(seq)` written in the previous question to do the following:

- recursively iterate through the `left` and `right` list to separate the smaller value elements and the larger value elements until there is only one or no element in the list.
- this `qsort(seq)` will return **a sorted list**.

Do not use Python's built-in `sort()` or `sorted()` methods.

#### Public test cases

| Expression | Expected |
|---|---|
| `qsort(random_seq)` | `[0, 1, 2, 3, 4, 5, 6, 7, 8]` |

### Question 6: Core Skill 0: Swapping 2 elements

- **Type:** Programming

Traditionally and in other programming language, we will need a temporary variable temp in order to swap 2 elements in an array.

- `Temp` ← `Seq[1]`
  `Seq[1]` ← `Seq[3]`
  `Seq[3]` ← `Temp`

But with Python programming, we can swap the elements using direct assignments.

#### Public test cases

| Expression | Expected |
|---|---|
| `seq` | `[1, 2, 7, 3, 8, 9, 0, 6, 4, 5]` |

### Question 7: Core Skill 1: Summary

- **Type:** Programming

Write program codes for the following:

- Define all the variables: `seq`, `start`, `end`, `pivot`, `lo` and `hi`
- Move `lo` from the first element towards the right until the element value is larger or equal to the `pivot`
- Move `hi` from the last element towards the left until the element value is smaller than the `pivot`
- Swap the `lo` and `hi` elements

#### Public test cases

| Expression | Expected |
|---|---|
| `seq` | `[1, 3, 4, 2, 8, 9, 0, 6, 7, 5]` |

### Question 8: Core Skill 2: Repeatedly moving `Low` and `High`

- **Type:** Programming

Copy and paste the codes from the **Core Skill 1**, modify to do the following:

- repeatedly move `lo` and `hi` with the condition `lo <= hi`
- swap the `lo` and `hi` elements only if `lo <= hi`

#### Public test cases

| Expression | Expected |
|---|---|
| `lo` | `5` |
| `seq` | `[1, 3, 4, 2, 0, 9, 8, 6, 7, 5]` |

### Question 9: Core Skill 3: Move the `Pivot` into the correct position

- **Type:** Programming

Copy and paste the codes from the **Core Skill 2**, modify to do the following:

- swap the `lo` and `pivot` elements

#### Public test cases

| Expression | Expected |
|---|---|
| `pivot` | `5` |
| `seq` | `[1, 3, 4, 2, 0, 5, 8, 6, 7, 9]` |

### Question 10: Step 1: The partition() function

- **Type:** Programming

Write program code for the function `partition(seq, start, end)` to return `lo` as the index of the pivot after partitioning the sequence `seq` **ONCE**.

Your `partition` function will be called with `start` and `end` initialised with the correct start and end indices.

`partition(seq, 0, len(seq) - 1)`

Take extra care not to overwrite the `start` and `end` input argument variables.

#### Public test cases

| Expression | Expected |
|---|---|
| `partition(seq, 0, 9)` | `5` |
| `seq` | `[1, 3, 4, 2, 0, 5, 8, 6, 7, 9]` |

### Question 11: Step 2: The qsort() function - partition the sequence recursively

- **Type:** Programming

Write program code for the function `qsort(seq, start, end)` to partition the sequence `seq` **RECURSIVELY** and return a sorted `seq`.

- the pivot index: `mid`
- the left segment: `start` to `mid-1` index
- the right segment: `mid+1` to `end` index

#### Public test cases

| Expression | Expected |
|---|---|
| `qsort(seq, 0, len(seq)-1)` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` |

### Question 12: Step 3: The quicksort() wrapper function

- **Type:** Programming

Write program code for the function `quicksort(seq)` to:

- initiate the start as the index 0 and end as the index of the last element in the sequence `seq`
- call on the helper function `qsort(seq,start,end)`
- return the sorted sequence `seq`.

#### Public test cases

| Expression | Expected |
|---|---|
| `quicksort(seq)` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` |

### Question 13: Extension: Modify partition() to use the first element as the `Pivot`

- **Type:** Programming

Modify the program code for function `partition(seq,start,end)` to use the **first element** in the sequence `seq` as the `pivot`.

- initiate the `start` as the index 0 and `end` as the index of the last element in the sequence `seq`
- call on the helper function `qsort(seq,start,end)`
- the `quicksort(seq)` mutates the `seq` into a sorted sequence.

#### Public test cases

| Expression | Expected |
|---|---|
| `partition(seq1, 0, len(seq1)-1)` | `6` |
| `seq1` | `[0, 3, 5, 2, 4, 1, 6, 9, 8, 7]` |

### Question 14: Describe Quick Sort

- **Type:** RubricBasedResponse

Describe how the Quick Sort algorithm works to sort an array in ascending order.

Use keywords : **pivot**, **partition**, **repeat**

## Linked code template notebook cells

Starter-code cells copied read-only from the assessment-linked local template notebook(s). Notebook outputs and walkthrough-solution notebooks are excluded.

### LT12e-non-inplace.ipynb

#### Code cell 1

```python
#Run the following code to generate a random sequence with 9 numbers
from random import shuffle

random_seq = list(range(9))
shuffle(random_seq)
print(random_seq)
```

#### Code cell 2

```python
def qsort(seq):
    pivot_index = 
    pivot = 
    left = 
    right = 


qsort(random_seq)  # Test with a random sequence
```

#### Code cell 3

```python
qsort([8, 1, 0, 4, 2, 5, 6, 7, 3])  # Does it match the example?
```

#### Code cell 4

```python
def qsort(seq):
    pass


qsort(random_seq)  # Test with a random sequence
```

#### Code cell 5

```python
qsort([8, 1, 0, 4, 2, 5, 6, 7, 3])  # Does it match the example?
```

### LT12e-inplace.ipynb

#### Code cell 1

```python
# Core Skill 0: Swapping 2 elements in a list

seq = [1, 3, 7, 2, 8, 9, 0, 6, 4, 5]

# swap elements in index 1 and 3


print(seq)
```

#### Code cell 2

```python
# Core Skill 1a: Define variables

seq = [1, 3, 7, 2, 8, 9, 0, 6, 4, 5]

start = 
end = 

pivot =                #using the last element as the pivot
lo =
hi =
```

#### Code cell 3

```python
# Core Skill 1b: Moving `Low` towards the right

while ...

    

print(seq)
print(lo==2)         #lo will stop at index 2 since 7 is larger than the pivot 5.
```

#### Code cell 4

```python
# Core Skill 1c: Moving `High` towards the left

while ...


print(seq)
print(hi==8)         #hi will stop at index 8 since 4 is smaller than the pivot 5.
```

#### Code cell 5

```python
# Core Skill 1d: Swap the `Low` and `High` elements

print('Before swap: ', seq)


#print('After swap: ', seq)
```

#### Code cell 6

```python
# Core Skill 1 (Summary)

seq = [1, 3, 7, 2, 8, 9, 0, 6, 4, 5] 
print('Before swap: ', seq)


# Define the variables


# Moving 'Low' to the right


# Moving 'High' to the left


# Swapping the 'Low' and 'High' elements


#print('After swap: ', seq)
```

#### Code cell 7

```python
# Core Skill 2: Repeatedly moving `Low` and `High` 

seq = [1, 3, 7, 2, 8, 9, 0, 6, 4, 5] 


# Paste your previous codes here:


        
        

print('lo: ', lo)
print('After swap: ', seq)
```

#### Code cell 8

```python
# Core Skill 3: Move the `Pivot` into the correct position

seq = [1, 3, 7, 2, 8, 9, 0, 6, 4, 5] 

# Paste your previous codes here:


        


print('Pivot: ', lo)
print('After swap: ', seq)
```

#### Code cell 9

```python
def partition(seq, start, end):
    pass


seq = [1, 3, 7, 2, 8, 9, 0, 6, 4, 5] 

print('Pivot :', partition(seq, 0, len(seq)-1))
print('After swap: ', seq)
```

#### Code cell 10

```python
#partition the 'right partition' further

print('Pivot :', partition(seq, _, _))
print('After swap: ', seq)
```

#### Code cell 11

```python
#partition the 'right partition' further

print('Pivot :', partition(seq, _, _))
print('After swap: ', seq)
```

#### Code cell 12

```python
#partition the 'left partition' further

print('Pivot :', partition(seq, _, _))
print('After swap: ', seq)
```

#### Code cell 13

```python
#partition the 'left partition' further

print('Pivot :', partition(seq, _, _))
print('After swap: ', seq)
```

#### Code cell 14

```python
#partition the 'left partition' further

print('Pivot :', partition(seq, _, _))
print('After swap: ', seq)
```

#### Code cell 15

```python
# Step 2:

def qsort(seq, start, end):
    pass


        
seq = [1, 3, 7, 2, 8, 9, 0, 6, 4, 5] 
qsort(seq, 0, len(seq)-1)
```

#### Code cell 16

```python
# Step 3:

def quicksort(seq):
    pass

    
    
seq = [1, 3, 7, 2, 8, 9, 0, 6, 4, 5] 

quicksort(seq)
print(seq)
```

#### Code cell 17

```python
# Putting it altogether
```

#### Code cell 18

```python
#Run the following code to generate a random sequence with 9 numbers
from random import shuffle

random_seq = list(range(9))
shuffle(random_seq)


print('Random sequence: ', random_seq)

#print('After Quicksort: ', quicksort(random_seq))
```

#### Code cell 19

```python
# Paste and modify the program code for partition() here:

def partition(seq, start, end): #using the first element as the pivot
    pass


seq1 = [6, 3, 7, 2, 8, 9, 0, 1, 4, 5]

print('Pivot: ', partition(seq1, 0, len(seq1)-1))
print(seq1)
```

#### Code cell 20

```python

def qsort(seq, start, end):                    
    if start < end:
        mid = partition(seq, start, end)       #test with first element as pivot
        qsort(seq, start, mid-1)
        qsort(seq, mid+1, end)
    return seq


def quicksort(seq):                            #wrapper function
    qsort(seq, 0, len(seq)-1)
    return seq


from random import shuffle

random_seq = list(range(9))
shuffle(random_seq)

quicksort(random_seq)
```
