# LT 11b Binary Tree (Part 3) - Complete Coursemology Questions

- **Source URL:** https://yijc.coursemology.org/courses/3257/assessments/88720
- **Extraction date:** 2026-09-01 (Asia/Singapore)
- **Question count:** 5
- **Learning outcomes:** 2.1.4 — Tree traversals: Illustrate the use of and implement pre-order, in-order, and post-order traversals, including applying in-order traversal to binary search trees.  2.1.5 — Tree searching: Illustrate the use of and implement breadth-first search and depth-first search for binary trees.

## Assessment overview

**Learning Outcomes**

- **2.1.4 — Tree traversals:** Illustrate the use of and implement pre-order, in-order, and post-order traversals, including applying in-order traversal to binary search trees.
- **2.1.5 — Tree searching:** Illustrate the use of and implement breadth-first search and depth-first search for binary trees.

**Core Skills**

- Understand the depth-first (in-, pre- and post-order traversal) and breadth-first algorithms
- Write program codes to perform the DFS and BFS algorithms and return a flattened list for the tree

Please download the lecture slides and watch the lecture video before attempting the lecture training!

- [LT11b Binary Tree (Part 3)](https://yijc.coursemology.org/courses/3257/videos/26545) (5:23)

The lesson for this part is structured as follows:

- Perform the traversal on a diagram
- Play the unplugged activity (Pair-work)
- Write the program code for the traversal

You will complete the above for the In-, Pre- and Post-Order Traversal on a Binary Search Tree (BST).

![Diagram (no alt text provided)](https://yijc.coursemology.org/attachments/50011e80-97c0-4dfd-aabf-90648e4fe52e)

We will be using the powerpoint slides to visualise the result. We will deal with 3 examples to check our understanding of all three types of traversals.

**Resource:**A visualisation tool

[https://kjingkai.github.io/H2CP_DFS_BFS_traversal_applet/](https://kjingkai.github.io/H2CP_DFS_BFS_traversal_applet/)

## Question prompts

### Question 1: Traversals Applet

- **Type:** Programming

In this unplugged activity, you will familiarize yourself with the 4 traversals.

Use the applet at [https://kjingkai.github.io/H2CP_DFS_BFS_traversal_applet/](https://kjingkai.github.io/H2CP_DFS_BFS_traversal_applet/) to perform the traversals

![Diagram (no alt text provided)](https://yijc.coursemology.org/attachments/d131cff1-a015-4be2-ae04-844da8c80218)

1. Generate a standard tree on the left using `Bulk Build `
2. Enter the following comma-separated values `31, 18, 11, 30, 14, 28, 86, 39, 34, 76, 71, 82`
3. Choose `Pre-Order` on the right
4. Choose `Practice`, then `Start Practice`
5. Click on a node to visit it.
6. While visiting it, there are a few options you can take:

- visit the sub-tree of that node (i.e. traverse to the left or right side) by clicking on the left/right child of that node
- select the node by double clicking it
- this will reveal its correct relative order

You can also watch a simulation of the traversal

Restart the game if the node that you selected is incorrect (i.e. incorrect order of selection as shown on the right hand side column).

You have successfully executed the traversal if all the nodes are selected in the correct order.

Repeat the process for the other 3 traversals and record the outcomes of the 4 traversals (In-order, pre-order, post-order, and BFS) in the lists `in_order`, `pre_order`, `post_order`, `bfs`

#### Public test cases

| Expression | Expected |
|---|---|
| `pre_order` | `[31, 18, 11, 14, 30, 28, 86, 39, 34, 76, 71, 82]` |
| `in_order` | `[11, 14, 18, 28, 30, 31, 34, 39, 71, 76, 82, 86]` |
| `post_order` | `[14, 11, 28, 30, 18, 34, 71, 82, 76, 39, 86, 31]` |
| `bfs` | `[31, 18, 86, 11, 30, 39, 14, 28, 34, 76, 71, 82]` |

### Question 2: In-order traversal

- **Type:** Programming

The binary tree is represented using a nested sequence. The more elements we have, the deeper the nesting will be.

When we traverse a tree, we convert the tree into a 1-D list and it is known as flattened tree.

Write program code for the function `flatten(tree)` to execute an in-order traversal on the tree and return a list containing the nodes' entries.

You may import the `LT11b_module.py` and use `make_empty_tree()`, `make_tree(entry, left, right)`, `entry(tree)`, `left_branch(tree)`, `right_branch(tree)`, `is_empty(tree)` and `print_tree(tree)` provided.

**Suggestion**:

1. Consider using a recursive approach to implement the function.
2. Use + to concatenate multiple lists. For example:

[value1] + a_list_of_values + [value2] + another_list_of_values

#### Public test cases

| Expression | Expected |
|---|---|
| `flatten(t3)` | `[1, 2, 5, 7, 10]` |

### Question 3: Pre-order traversal

- **Type:** Programming

The binary tree is represented using a nested sequence. The more elements we have, the deeper the nesting will be.

When we traverse a tree, we convert the tree into a 1-D list and it is known as flattened tree.

Write program code for the function `flatten_pre(tree)` to execute an pre-order traversal on the tree and return a list containing the nodes' entries.

You may import the `LT11b_module.py` and use `make_empty_tree()`, `make_tree(entry, left, right)`, `entry(tree)`, `left_branch(tree)`, `right_branch(tree)`, `is_empty(tree)` and `print_tree(tree)` provided.

**Suggestion**:

1. Consider using a recursive approach to implement the function.
2. Use + to concatenate multiple lists. For example:

[value1] + a_list_of_values + [value2] + another_list_of_values

#### Public test cases

| Expression | Expected |
|---|---|
| `flatten_pre(t3)` | `[5, 2, 1, 7, 10]` |

### Question 4: Post-order traversal

- **Type:** Programming

The binary tree is represented using a nested sequence. The more elements we have, the deeper the nesting will be.

When we traverse a tree, we convert the tree into a 1-D list and it is known as flattened tree.

Write program code for the function `flatten_post(tree)` to execute an post-order traversal on the tree and return a list containing the nodes' entries.

You may import the `LT11b_module.py` and use `make_empty_tree()`, `make_tree(entry, left, right)`, `entry(tree)`, `left_branch(tree)`, `right_branch(tree)`, `is_empty(tree)` and `print_tree(tree)` provided.

**Suggestion**:

1. Consider using a recursive approach to implement the function.
2. Use + to concatenate multiple lists. For example:

[value1] + a_list_of_values + [value2] + another_list_of_values

#### Public test cases

| Expression | Expected |
|---|---|
| `flatten_post(t3)` | `[1, 2, 10, 7, 5]` |

### Question 5: Breadth-First Search

- **Type:** Programming

The binary tree is represented using a nested sequence. The more elements we have, the deeper the nesting will be.

When we traverse a tree, we convert the tree into a 1-D list and it is known as a flattened tree.

Write program code for the function `flatten_bfs(tree)` to execute a level-order (BFS) traversal on the tree and return a list containing the nodes' entries.

You may import the `LT11b_module.py` and use `make_empty_tree()`, `make_tree(entry, left, right)`, `entry(tree)`, `left_branch(tree)`, `right_branch(tree)`, `is_empty(tree)` and `print_tree(tree)` provided.

You may also import the `queue_module.py` and use `make_empty_queue()`, `make_queue(seq)`, `enqueue(queue, item)`, `is_empty_queue(queue)`, `front(queue)` and `dequeue(queue)` provided.

**Suggestion:**

1. Consider using a queue to keep track of nodes still to be visited, rather than a recursive approach.
2. Use `+` to concatenate multiple lists. For example:

```
[value1] + a_list_of_values + [value2] + another_list_of_values
```

#### Public test cases

| Expression | Expected |
|---|---|
| `flatten_bfs(t3)` | `[5, 2, 7, 1, 10]` |

## Linked code template notebook cells

Starter-code cells copied read-only from the assessment-linked local template notebook(s). Notebook outputs and walkthrough-solution notebooks are excluded.

### LT11b3.ipynb

#### Code cell 1

```python
from LT11b_module import *


def flatten(tree):
    made_up_tree = []
    """ flattens tree with the following rule:
        visit left branch, visit entry then visit right branch """
    if is_empty(tree):
        return []

    return (flatten(left_branch(tree)) + [entry(tree)] + flatten(right_branch(tree)))


t3 = make_tree(5, make_tree(2, make_tree(1, make_empty_tree(), make_empty_tree()), make_empty_tree()), make_tree(7, make_empty_tree(), make_tree(10, make_empty_tree(), make_empty_tree())))

t3
```

#### Code cell 2

```python
flatten(t3) # expected [1, 2, 5, 7, 10]
```

#### Code cell 3

```python
from LT11b_module import *

def flatten_pre(tree):
    """ flattens tree with the following rule:
        visit entry, visit left branch then visit right branch """
    made_up_tree = []
    if is_empty(tree):
        return []

    return  [entry(tree)]+(flatten_pre(left_branch(tree)) + flatten_pre(right_branch(tree)))


t3 = make_tree(5, make_tree(2, make_tree(1, make_empty_tree(), make_empty_tree()), make_empty_tree()), make_tree(7, make_empty_tree(), make_tree(10, make_empty_tree(), make_empty_tree())))
```

#### Code cell 4

```python
flatten_pre(t3) # expected [5, 2, 1, 7, 10]
```

#### Code cell 5

```python
from LT11b_module import *


def flatten_post(tree):
    """ flattens tree with the following rule:
        visit left branch, visit right branch then visit entry"""
    made_up_tree = []
    if is_empty(tree):
        return []

    return  (flatten_post(left_branch(tree)) + flatten_post(right_branch(tree)) + [entry(tree)])


t3 = make_tree(5, make_tree(2, make_tree(1, make_empty_tree(), make_empty_tree()), make_empty_tree()), make_tree(7, make_empty_tree(), make_tree(10, make_empty_tree(), make_empty_tree())))
```

#### Code cell 6

```python
flatten_post(t3)  # expected [1, 2, 10, 7, 5]
```

#### Code cell 7

```python
from LT11b_module import *
from queue_adt import *

#############
# Do not edit above this line

def flatten_bfs(tree):
    #check for empty tree first
    if is_empty(tree):
        return []
    #setup queue and output list
    made_up_tree = []
    que= make_empty_queue()

    #enqueue root node (not just value) into queue
    enqueue(que,tree)
    #while queue is not empty, dequeue node at front of queue, add its value into output list
    while not is_empty_queue(que):
        current = dequeue(que)
        made_up_tree.append(entry(current))
    #check if right and left branches have nodes, if so, enqueue nodes into queue
        if not is_empty(left_branch(current)):
            enqueue(que,left_branch(current))
        if not is_empty(right_branch(current)):
            enqueue(que,right_branch(current))
    return made_up_tree

# Do not edit below this line
###################
t3 = make_tree(5, make_tree(2, make_tree(1, make_empty_tree(), make_empty_tree()), make_empty_tree()), make_tree(7, make_empty_tree(), make_tree(10, make_empty_tree(), make_empty_tree())))
```

#### Code cell 8

```python
flatten_bfs(t3)   #expected [5, 2, 7, 1, 10]
```

#### Code cell 9

```python
entry(left_branch(right_branch(t2)))   # expected 6
```

#### Code cell 10

```python
entry(t3)  # expected 5
```
