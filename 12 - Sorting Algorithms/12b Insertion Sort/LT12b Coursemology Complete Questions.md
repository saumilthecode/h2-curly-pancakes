# LT 12b Insertion Sort - Complete Coursemology Questions

- **Source URL:** https://yijc.coursemology.org/courses/3257/assessments/88722
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 6
- **Learning outcomes:** 1.2 Fundamental Algorithms1.2.1 Implement sort algorithms (insertion sort, bubble sort, quicksort, merge sort)1.2.2 Use examples to explain sort algorithms1.2.5 Compare and describe the efficiencies of the sort and search algorithms using Big-O notation for time complexity (worst case).

## Assessment overview

**Learning Outcomes**
**1.2 Fundamental Algorithms**
1.2.1 Implement sort algorithms (insertion sort, bubble sort, quicksort, merge sort)
1.2.2 Use examples to explain sort algorithms
1.2.5 Compare and describe the efficiencies of the sort and search algorithms using Big-O notation for time complexity (worst case).

**Core Skills**

1. Understand and explain how insertion sort works with relevant examples
2. Implement insertion sort in code

Please download the lecture slides and watch the lecture videos before attempting the lecture training!

- [Unplugged activity for Insertion Sort](https://youtu.be/QTh2RMHH-T0) (4:41)
- [Insertion Sort](https://yijc.coursemology.org/courses/3257/videos/24832)(8:06)
- [Insertion Sort with Romanian Folk Dance](https://www.youtube.com/embed/ROalU379l3U?start=1&end=142) (Optional: Playback at 1.5x speed)

![Diagram (no alt text provided)](https://yijc.coursemology.org/attachments/50011e80-97c0-4dfd-aabf-90648e4fe52e)

Please feel free to post questions via the comment box tagged to the lecture video. Have fun!

## Question prompts

### Question 1: Trace Table: Insertion Sort Algorithm (Pseudocode)

- **Type:** TextResponse

The following pseudocode implements the Insertion Sort algorithm:

```
FOR Pointer <- 2 TO NumberOfitems    ItemToBeInserted <- MyList[Pointer]    CurrentItem <- Pointer -1    WHILE (MyList[CurrentItem] > ItemToBeInserted) AND (CurrentITEM >0)        MyList[CurrentItem + 1]  <- MyList[CurrentItem]        CurrentItem <- CurrentItem -1    ENDWHILE    MyList[CurrentItem + 1] <- ItemToBeInsertedENDFOR
```

Draw up a trace table showing the changing contents of the array MyList as the Insertion Sort is applied.
MyList = [53, 21, 60, 18, 42, 19]

Note : You may use the MS Excel template provided or click here for the [Google Sheets](https://docs.google.com/spreadsheets/d/197rXA1icVyCq2kNylIBRN3vFqtFnr-F-Y1wHBG6qwHI/edit?usp=sharing).

The index for MyList starts from **1**, not 0.

![Diagram (no alt text provided)](data:image/png;base64,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)

Copy the resulting table and paste in Coursemology for submission.

### Question 2: Insertion Sort Algorithm

- **Type:** RubricBasedResponse

Describe the insertion sort algorithm to sort a list in ascending order.

### Question 3: Core Skill: Shift the last element of a list to the 'correct' position

- **Type:** Programming

The list [1,3,5,7,8,4] contains elements that are **mostly sorted**except for the last element, which is not in the correct position.

Write program code for a helper function `shift(lst)` to shift the last element in the list `lst`, leftward to its "correct" position, resulting in a fully sorted list.

#### Public test cases

| Expression | Expected |
|---|---|
| `shift([1,3,7,8,9])` | `[1, 3, 7, 8, 9]` |
| `shift([1,3,5,7,8,4])` | `[1, 3, 4, 5, 7, 8]` |
| `shift([3,5,7,8,1])` | `[1, 3, 5, 7, 8]` |
| `shift(['ab','ad','am','ap','az','ak'])` | `['ab', 'ad', 'ak', 'am', 'ap', 'az']` |

### Question 4: Insertion Sort

- **Type:** Programming

Write the code for `insertion_sort(lst)` to perform an in-place Insertion Sort.

Note : You may consider using some of the code from `shift(lst)` to perform the insertion sort here.

#### Public test cases

| Expression | Expected |
|---|---|
| `insertion_sort([7,1,3,5,8,4])` | `[1, 3, 4, 5, 7, 8]` |
| `insertion_sort([17,11,13,15,18,14,99,22,33,66])` | `[11, 13, 14, 15, 17, 18, 22, 33, 66, 99]` |

### Question 5: Time complexity (Insertion Sort)

- **Type:** MultipleChoice

What is the worse-case time complexity for Insertion sort?

#### Choices

- O(n)
- O(n2)
- O(lg n)
- O(n lg n)

### Question 6: No. of Comparison for Insertion Sort

- **Type:** Programming

Write program code for the functions `insertion_sort_comparison(seq)` using the insertion sort algorithms to count and return the number of comparisons needed to sort the elements in `seq` in ascending order.

#### Public test cases

| Expression | Expected |
|---|---|
| `insertion_sort_comparison([8,7,5,4,3,1])` | `15` |
| `insertion_sort_comparison([7,1,3,5,8,4])` | `10` |
| `insertion_sort_comparison([1,3,5,4,8,7])` | `7` |

## Linked code template notebook cells

Starter-code cells copied read-only from the assessment-linked local template notebook(s). Notebook outputs and walkthrough-solution notebooks are excluded.

### LT12b.ipynb

#### Code cell 1

```python
def shift(lst):   #key = lst[-1]
    i = len(lst) - 1        #i: index of last element
    while i > 0 and lst[i] < lst[i - 1]:
        lst[i], lst[i - 1] = lst[i - 1], lst[i]
        i -= 1
    return lst


def shift(lst):
    i  = len(lst) -1
    key = lst[i]
    while i >0:
        if lst[i] < lst[i-1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i = i-1
        else:
            break
    return lst

shift([1,3,5,7,8,4])
```

#### Code cell 2

```python
# def insertion_sort(lst):
#     for i in range(1, len(lst)):
#         j = i
#         while j > 0 and lst[j] < lst[j - 1]:
#             lst[j], lst[j - 1] = lst[j - 1], lst[j]
#             j -= 1
#     return lst

def insertion_sort(lst):
    for pointer in range(1,len(lst)):
        item = lst[pointer]
        current = pointer -1
        while lst[current]>item and current > 0:
            lst[current+1] = lst[current]
            current = current -1
        lst[current]= lst[current+1] 
    return lst

insertion_sort([7,1,3,5,8,4])
```

#### Code cell 3

```python
def insertion_sort_comparison(seq):
    count = 0
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1
        while j >= 0 and key < seq[j]:
            
            count += 1
            
            seq[j + 1] = seq[j]
            j -= 1
            
        count += 1 
        
        seq[j + 1] = key
    return count


print(insertion_sort_comparison([8,7,5,4,3,1]))
print(insertion_sort_comparison([7,1,3,5,8,4]))
print(insertion_sort_comparison([1,3,5,4,8,7]))
```

#### Code cell 4

```python
def insertion_sort_comparison(lst):
    count = 0
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            count+=1 # compare and swap

            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
        count +=1 # compare but no swap

    return count
    

print(insertion_sort_comparison([8,7,5,4,3,1]))
print(insertion_sort_comparison([7,1,3,5,8,4]))
print(insertion_sort_comparison([1,3,5,4,8,7]))
```
