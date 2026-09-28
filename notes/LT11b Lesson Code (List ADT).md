> [!summary] Quick View
> The tree algorithms in Python: **search** (`contains`), **insert** (`insert_tree`), the three **traversals** and **BFS**, all built on the lesson's list ADT `[entry, left, right]`.
> Papers ask for these as descriptions or pointer pseudocode, not this exact code. The exam answers are in [[LT11b Binary Tree]].

## The Binary Tree ADT

Your ADT stores a tree as a **3-element list**: `[entry, left, right]`. An empty tree is `[]`.

```python
def make_empty_tree():                return []                    # constructors
def make_tree(entry, left, right):    return [entry, left, right]
def entry(tree):                      return tree[0]               # accessors
def left_branch(tree):                return tree[1]
def right_branch(tree):               return tree[2]
def is_empty(tree):                   return (tree == [])          # predicate
```

A leaf has **both** branches empty. Build bottom-up: children first, since `make_tree` takes them as arguments:

```python
three = make_tree(3, make_empty_tree(), make_empty_tree())
four  = make_tree(4, three, make_empty_tree())        # 3 is 4's left child
```

> [!warning]
> Always build the empty branches with `make_empty_tree()`, never a bare `[]`. The `[]` is the *representation*, and in an [[LT10a Data Abstraction|ADT]] only the constructors and accessors touch that.

> [!example]- The lecture's `five` tree
> ```python
> eight        = make_tree(8, make_empty_tree(), make_empty_tree())
> twenty_seven = make_tree(27, make_empty_tree(), make_empty_tree())
> twenty_four  = make_tree(24, make_empty_tree(), twenty_seven)
> fifteen      = make_tree(15, eight, twenty_four)
> five         = make_tree(5, four, fifteen)
> ```
>
> ```mermaid
> flowchart TD
>   f5[5] --> f4[4]
>   f5 --> f15[15]
>   f4 --> f3[3]
>   f4 ~~~ g1:::hid
>   f15 --> f8[8]
>   f15 --> f24[24]
>   f24 ~~~ g2:::hid
>   f24 --> f27[27]
>   classDef hid fill:none,stroke:none,color:transparent
> ```
>
> ```python
> [5, [4, [3, [], []], []], [15, [8, [], []], [24, [], [27, [], []]]]]
> ```

> [!note]
> `print_tree()` requires `from LT11b_module import *`, which **overwrites** your `make_tree`, `entry`, `left_branch`, `right_branch`, `make_empty_tree` and `is_empty`. Import before your definitions to keep yours.

## Searching a BST: `contains`

The recursion is the same shape as [[LT11a Search|binary search]]: compare, then throw away the half that cannot hold the key.

```python
def contains(x, tree):
    if is_empty(tree):
        return False            # base case - ran off the bottom
    elif x == entry(tree):
        return True             # base case - found it
    elif x < entry(tree):
        return contains(x, left_branch(tree))     # go left
    else:
        return contains(x, right_branch(tree))    # go right
```

> [!important]
> `return` recursive calls. Otherwise the function returns `None`.

The slides name this function `is_element_of_set(x, s)`.

## Inserting: `insert_tree`

Insert as a **new leaf**: follow the search path to an empty branch.

```python
def insert_tree(x, tree):
    if is_empty(tree):
        return make_tree(x, make_empty_tree(), make_empty_tree())
    elif x < entry(tree):
        return make_tree(entry(tree), insert_tree(x, left_branch(tree)), right_branch(tree))
    elif x > entry(tree):
        return make_tree(entry(tree), left_branch(tree), insert_tree(x, right_branch(tree)))
    else:
        return tree                 # x is already here, keys stay distinct
```

> [!important] Why the fourth branch matters
> A plain `else` on the last case puts a **duplicate** in the right subtree, breaking rule 1. Inserting `3` into `[1, 2, 3, 5]`:
>
> | Version | Result |
> | ------- | ------ |
> | `elif x > entry(tree)` … `else: return tree` | `[1, 2, 3, 5]` (unchanged) |
> | plain `else` | `[1, 2, 3, 3, 5]` (duplicate) |

Each call rebuilds its node with **one** branch replaced. Use the returned tree:

```python
insert_tree(5, t1)           # wrong - the new tree is thrown away
t1 = insert_tree(5, t1)      # right
```

## Writing the Traversals

Only `[entry(tree)]` changes position:

```python
def flatten_pre(tree):                                              # Q3
    if is_empty(tree):
        return []
    return [entry(tree)] + flatten_pre(left_branch(tree)) + flatten_pre(right_branch(tree))

def flatten(tree):                                                  # Q2 - in-order
    if is_empty(tree):
        return []
    return flatten(left_branch(tree)) + [entry(tree)] + flatten(right_branch(tree))

def flatten_post(tree):                                             # Q4
    if is_empty(tree):
        return []
    return flatten_post(left_branch(tree)) + flatten_post(right_branch(tree)) + [entry(tree)]
```

The empty tree returns `[]`, so `+` joins the pieces on the way back up.

BFS can't recurse like that. It needs a [[LT10c Queue|queue]] to hold the nodes waiting at the next level. Part 3 gives you `queue_adt`:

```python
from queue_adt import *          # make_empty_queue, enqueue, dequeue, is_empty_queue

def flatten_bfs(tree):
    if is_empty(tree):
        return []
    result = []
    q = make_empty_queue()
    enqueue(q, tree)                              # the node, not just its value
    while not is_empty_queue(q):
        node = dequeue(q)
        result.append(entry(node))
        if not is_empty(left_branch(node)):
            enqueue(q, left_branch(node))
        if not is_empty(right_branch(node)):
            enqueue(q, right_branch(node))
    return result
```

> [!important]
> Enqueue the **node**, not `entry(node)`. You need its branches again when it comes off the queue. Guard each branch with `is_empty` or you enqueue `[]` and crash on `entry([])`.

> [!tip] BFS and DFS are the same loop
> Swap the queue for a [[LT10b Stack|stack]] and push **right before left**, and that loop outputs pre-order instead. FIFO spreads across the level. LIFO dives down the branch.

## Related

- [[LT11b Binary Tree]]
- [[LT10a Data Abstraction]]
- [[LT10c Queue]]
