# LT12b Insertion Sort: Coursemology Questions Missing from Notebooks

Source: https://yijc.coursemology.org/courses/3257/assessments/88722  
Extracted: 1 September 2026

## Why this file exists

The template and walkthrough notebooks use inconsistent question numbering. This file preserves the Coursemology prompts that are absent or only partly represented, so a notes tool can track the complete LT coverage.

## Learning coverage added

- Tracing the insertion-sort pseudocode
- Explaining the algorithm in words
- Worst-case time complexity

## Q1: Trace Table for the Insertion Sort pseudocode

The following pseudocode implements Insertion Sort:

```text
FOR Pointer <- 2 TO NumberOfItems
    ItemToBeInserted <- MyList[Pointer]
    CurrentItem <- Pointer - 1

    WHILE (MyList[CurrentItem] > ItemToBeInserted)
          AND (CurrentItem > 0)
        MyList[CurrentItem + 1] <- MyList[CurrentItem]
        CurrentItem <- CurrentItem - 1
    ENDWHILE

    MyList[CurrentItem + 1] <- ItemToBeInserted
ENDFOR
```

Draw a trace table showing the changing contents of `MyList` as Insertion Sort is applied to:

```text
MyList = [53, 21, 60, 18, 42, 19]
```

The index for `MyList` starts from 1, not 0. The Coursemology trace-table columns include:

- `Pointer` from 2 to 6
- `ItemToBeInserted`
- `CurrentItem`
- `MyList[CurrentItem] > ItemToBeInserted`
- `CurrentItem > 0`
- `MyList[1]` through `MyList[6]`

The walkthrough notebook discusses the pseudocode, but the full Coursemology trace-table task is preserved here.

## Q2: Insertion Sort algorithm

Describe the Insertion Sort algorithm used to sort a list in ascending order.

The explanation should cover:

- Treating the first element as the initial sorted sub-list
- Selecting the next key from the unsorted part
- Comparing it with elements in the sorted part
- Shifting larger elements to the right
- Inserting the key in the vacated position
- Repeating until every element is in the sorted sub-list

## Q5: Time complexity

What is the worst-case time complexity for Insertion Sort?

Choices:

- `O(n)`
- `O(n²)`
- `O(log n)`
- `O(n log n)`

## Already represented in the notebooks

The notebooks cover shifting the last element into position, implementing in-place Insertion Sort and counting comparisons. The Coursemology numbers for these are Questions 3, 4 and 6, although the local template uses different numbers for some of them.
