# LT12d Merge Sort: Coursemology Questions Missing from Notebook

Source: https://yijc.coursemology.org/courses/3257/assessments/88732  
Extracted: 1 September 2026

## Why this file exists

The local notebook represents Coursemology Questions 1, 2 and 4 to 7. Questions 3 and 8 are missing, so they are preserved here for any notes tool scanning this folder.

## Learning coverage added

- Visualising recursive splitting as a tree
- Describing Merge Sort in words

## Q3: Seeing the “Tree”

After splitting the list:

```text
[5, 2, 1, 8, 9]
```

into:

```text
(([5], [2]), ([1], ([8], [9])))
```

draw a tree diagram showing how this nested structure looks. The lecture notes may be used as a reference. Coursemology suggests using https://app.diagrams.net/ to draw the boxes and connecting lines.

This tests recognition of the recursive divide tree and the singleton base cases.

## Q8: Describe Merge Sort

Describe how Merge Sort sorts an array of numbers.

Use the keywords **divide**, **merge** and **repeat** to assist your explanation.

The description should track these stages:

1. Repeatedly divide the array into halves until each sub-array contains one element.
2. Merge pairs of sorted sub-arrays by comparing their front elements and placing them in order.
3. Repeat the merging process until one fully sorted array remains.

## Already represented in the notebook

Questions 1, 2 and 4 to 7 cover splitting once, splitting recursively, merging increasingly general sorted lists and combining the helpers into `merge_sort(seq)`.
