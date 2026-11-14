# LT12e Quicksort: Coursemology Questions Missing from Notebooks

Source: https://yijc.coursemology.org/courses/3257/assessments/88737  
Extracted: 1 September 2026

## Why this file exists

The non-in-place notebook begins at Coursemology Question 4, while the in-place notebook is organised as Core Skills and implementation steps. This file preserves Questions 1 to 3 so a notes tool can see the complete conceptual coverage.

## Learning coverage added

- Whether Quicksort is in-place or stable
- Best- and worst-case partition behaviour
- Average time complexity
- Worst-case time complexity

## Q1: Quicksort statements

Which statements about Quicksort are true?

- Most, if not all, commonly used implementations of Quicksort are in-place algorithms.
- Quicksort is a stable sorting algorithm.
- The best-case scenario occurs when Quicksort partitions the array into two equal halves every time.
- The worst case occurs when the sequence is already sorted and the first or last element is used as the pivot.

## Q2: Average time complexity for Quicksort

Select the average time complexity for Quicksort.

Choices:

- `O(1)`, because it takes the same amount of time regardless of the array size.
- `O(n)`, because it compares every element during the sort.
- `O(log n)`, because the divide-and-conquer approach halves the problem.
- `O(n log n)`, because after dividing the array, Quicksort compares elements across the recursive partition levels.
- `O(n²)`, because an outer and inner process both go through the elements.

## Q3: Worst-case time complexity for Quicksort

Select the statements that correctly describe Quicksort's worst-case time complexity.

Choices:

- `O(n)`, because the worst case is like performing a linear search.
- `O(n log n)`, because Quicksort has the same time complexity regardless of the original sequence arrangement.
- `O(n²)`, because a sorted sequence with the first or last element as pivot produces highly unbalanced partitions and repeated comparisons.
- `O(n²)`, because each partition produces only one non-empty side; this repeats for about `n` partitions, with comparisons over the remaining elements.

## Already represented in the notebooks

The non-in-place notebook contains Questions 4 and 5 on partitioning into auxiliary lists and recursively sorting them. The in-place notebook covers swapping, low/high pointer movement, pivot placement, `partition()`, recursive `qsort()`, the wrapper function and changing from a last-element pivot to a first-element pivot.
