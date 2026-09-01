# LT 11b Binary Tree (Part 2) - Complete Coursemology Questions

- **Source URL:** https://yijc.coursemology.org/courses/3257/assessments/88719
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 8
- **Learning outcomes:** 2.1.3 — Tree operations: Illustrate the use of and implement the create, update (edit, insert, delete), and search operations for binary trees, including binary search trees.

## Assessment overview

**Learning Outcomes**

**2.1.3 — Tree operations:** Illustrate the use of and implement the create, update (edit, insert, delete), and search operations for binary trees, including binary search trees.

**Core Skills**

- Understand the algorithms for search and inserting an item into a Binary Search Tree (BST)
- Write program codes to perform the search and insert operation in a Binary Search Tree

Please download the lecture slides and watch the lecture video before attempting the lecture training!

- [LT11b Binary Tree (Part 2)](https://yijc.coursemology.org/courses/3257/videos/24867) (5:02)

![Diagram (no alt text provided)](https://yijc.coursemology.org/attachments/e30ab087-eed3-40dc-96c9-24b24d89ecb8)

We will be using slides to visualise and test our understanding of the binary search tree. We try to explain and describe the algorithm for performing a search on a binary search tree.

Please feel free to post questions via the comment box tagged to the lecture video. Have fun!

**A visualisation tool:**

[http://liveexample.pearsoncmg.com/liang/animation/web/BST.html](http://liveexample.pearsoncmg.com/liang/animation/web/BST.html)

## Question prompts

### Question 1: Unplugged Activity 1 (Pair work) - Search through a Binary Search Tree (BST)

- **Type:** MultipleResponse

1. Access the applet at [https://kjingkai.github.io/H2CP_DFS_BFS_traversal_applet/](https://kjingkai.github.io/H2CP_DFS_BFS_traversal_applet/)
2. This is a Binary Search Tree (BST) containing at least 20 nodes with values between 1 to 99, across 5 levels
3. Select `Binary Search `on the right under `Traversal type`
4. Select `Practice` --> `New Practice set` --> `Start practice`
5. Click one of the 3 keys (numbers to be searched)
6. Starting from the root node, explore the tree to search. Remember to double click each visited node
7. If you are sure that the key cannot be found in the BST, choose `Declare 'not in this tree'`.

![Diagram (no alt text provided)](https://yijc.coursemology.org/attachments/e0e7b62b-1bc8-432b-95fe-66907857cb80)

Have Fun!

#### Choices

- I am able to find all 3 keys
- All keys cannot be found
- I found 1 key
- I found 2 keys

### Question 2: Algorithm for searching an item in a BST

- **Type:** RubricBasedResponse

Describe the steps you took (algorithm) to check if an item exist in the BST.

Be clear in your description.

### Question 3: Binary Search and Binary Search Tree

- **Type:** MultipleResponse

Which of these statements are true about the binary search and Binary Search Tree (BST)?

#### Choices

- Both binary search and using a BST are faster than performing a linear search.
- Binary search can only be performed on a list which is sorted either in ascending or descending order.
- The time complexity for performing a linear search is O(n), and it is O(lg(n)) for binary search.
- The time complexity for performing a search in a balanced BST is O(lg(n)), and O(n) for the worst case scenario where the BST is skewed.

### Question 4: Searching for an item in a BST

- **Type:** MultipleResponse

How many comparisons are required to search for the following items in the BST?

**Note:**You should always start searching from the Root Node.

![Diagram (no alt text provided)](https://yijc.coursemology.org/attachments/738dad29-4723-4766-beed-617bc4e9cda2)

#### Choices

- Searching for 7 needs to perform 4 comparisons.
- Searching for 2 needs to perform 3 comparisons.
- Searching for 4 needs to perform 3 comparisons.
- Searching for 15 needs to perform 3 comparisons.

### Question 5: Adding a Predicate to the Binary Search Tree ADT

- **Type:** Programming

Write program code for the function `contains(x, tree)` to search for an item `x` in a BST `tree` and return `True` if the item is found in the tree; Otherwise, return `False`.

You may import the `LT11b_module.py` and use `make_empty_tree()`, `make_tree(entry, left, right)`, `entry(tree)`, `left_branch(tree)`, `right_branch(tree)`, `is_empty(tree)` and `print_tree(tree)` provided.

**Suggestion**: Consider using a recursive approach to implement the function.

#### Public test cases

| Expression | Expected |
|---|---|
| `contains(2, t1)` | `True` |
| `contains(1, t2)` | `True` |
| `contains(3, t2)` | `False` |

### Question 6: Unplugged Activity 2 (Group - whole class) : Construct a BST with your Lucky Number

- **Type:** TextResponse

**Objective:** To construct a Binary Search Tree using the Lucky Number of the students.

26S13: [Click here for the link](https://padlet.com/kuang_jingkai3/lt11b-part-2-my-lucky-number-26s13-80i3jj1vshtnehrx)

**Procedure:**

1. Each student is to input his/her birthday in MMDD
2. The top (Root) of the tree is set as 0701
3. Each student writes his/her name+birthday and connect it to the BST as a node in the correct position of the tree (refer to example on top left).
4. Do not intervene whether it is placed correctly or wrongly.
5. Repeat steps 3 to 5 until all students have had their turn.

Use snipping tool to capture the image and submit a picture of the BST below.

### Question 7: Algorithm for inserting an element into a BST

- **Type:** RubricBasedResponse

Describe the steps you took (algorithm) to insert an item into a BST.

Be clear in your description.

### Question 8: Add a Modifier to the Binary Search Tree ADT

- **Type:** Programming

A binary tree is a Binary Search Tree (BST) if it adheres to the following rules:

- The left branch of a node contains only nodes with entries less than the node’s entry.
- The right branch of a node contains only nodes with entries greater than the node’s entry.

Write program code for the function `insert_tree(x, tree)` to insert an item x into a BST and return the modified tree.

You may import the `LT11b_module.py` and use `make_empty_tree()`, `make_tree(entry, left, right)`, `entry(tree)`, `left_branch(tree)`, `right_branch(tree)`, `is_empty(tree)` and `print_tree(tree)` provided.

**Suggestion**: Consider using a recursive approach to implement the function.

**Algorithm:**

When trying to insert the item x into a BST, there are three possible cases:

1) If the tree is empty, we return a tree object with x as the node’s entry and empty left- and right- subtrees.

2) If the tree is not empty:

(a) If x is less than the node’s entry, we will return a new tree with x inserted into the left-subtree.

(b) If x is more than the node’s entry, we will return a new tree with x inserted into the right-subtree.

**Example:**

>>> tree1 = make_tree(5, make_tree(2, make_empty_tree(), make_empty_tree()), make_tree(7, make_empty_tree(), make_empty_tree()))

>>> print_tree(tree1)

5

2 7

>>> tree2 = insert_tree(8, tree1)

>>> print_tree(tree2)

5

2 7

8

>>> tree3 = insert_tree(6, tree2)

>>> print_tree(tree3)

5

2 7

6 8

#### Public test cases

| Expression | Expected |
|---|---|
| `entry(right_branch(right_branch(t1)))` | `5` |
| `entry(left_branch(right_branch(t2)))` | `6` |

## Linked code template notebook cells

Starter-code cells copied read-only from the assessment-linked local template notebook(s). Notebook outputs and walkthrough-solution notebooks are excluded.

### LT11b2.ipynb

#### Code cell 1

```python
# Constructors
def make_empty_tree():
    return []

def make_tree(entry, left, right):
    return [entry,left,right]


# Accessors
def entry(tree):
    return tree[0]
    
    
def left_branch(tree):
    return tree[1]


def right_branch(tree):
    return tree[2]


# Predicate
def is_empty(tree):
    return (tree == [])
```

#### Code cell 2

```python
from LT11b_module import *


def contains(x, tree):
    if is_empty(tree):
        return False
    elif x == entry(tree):
        return True
    elif x < entry(tree): #go left
        return contains(x, left_branch(tree)) 
    else: #go right
        return contains(x, right_branch(tree))


##########Do not remove/modify###################
t1 = make_tree(2, make_tree(1, make_empty_tree(), make_empty_tree()), make_tree(3, make_empty_tree(), make_empty_tree()))
t2 = make_tree(5, make_tree(2, make_tree(1, make_empty_tree(), make_empty_tree()), make_empty_tree()), make_tree(7, make_empty_tree(), make_tree(10, make_empty_tree(), make_empty_tree())))
```

#### Code cell 3

```python
contains(2, t1) # expected True
```

#### Code cell 4

```python
contains(1, t2) # expected True
```

#### Code cell 5

```python
contains(3, t2) # expected False
```

#### Code cell 6

```python
from LT11b_module import *

def insert_tree(x, tree):
    """
    - tree is empty -> return a tree with x as entry and empty left and right branches
    - x < entry -> return new tree with x inserted into left sub tree
    - otherwise -> return new tree with x inserted into right sub tree
    """ 
    if is_empty(tree):
        return make_tree(x, make_empty_tree(), make_empty_tree())
    elif x < entry(tree):
        return make_tree(
            entry(tree),
            insert_tree(x, left_branch(tree)),
            right_branch(tree)
        )
    elif x > entry(tree):
        return make_tree(
            entry(tree),
            left_branch(tree),
            insert_tree(x, right_branch(tree))
        )
    else:
        return tree

##########Do not remove/modify###################
t1 = make_tree(2, make_tree(1, make_empty_tree(), make_empty_tree()), make_tree(3, make_empty_tree(), make_empty_tree()))
t1 = insert_tree(5, t1)

t2 = make_tree(5, make_tree(2, make_tree(1, make_empty_tree(), make_empty_tree()), make_empty_tree()), make_tree(7, make_empty_tree(), make_tree(10, make_empty_tree(), make_empty_tree())))
t2 = insert_tree(6, t2)
```

#### Code cell 7

```python
entry(right_branch(right_branch(t1)))  # expected 5
```

#### Code cell 8

```python
entry(left_branch(right_branch(t2)))   # expected 6
```

#### Code cell 9

```python
entry(t3)  # expected 5
```
