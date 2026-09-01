> [!summary] Quick View
> Queue = **FIFO**, First In First Out. Add at the tail, remove from the head.

```text
              +---+---+---+---+
  dequeue <-- | A | B | C | D | <-- enqueue
              +---+---+---+---+
                ^           ^
              head         tail
              q[0]         q[-1]
```

## Core Operations

| Operation | Meaning | Python list |
| --------- | ------- | ----------- |
| `enqueue(q, x)` | add to tail | `q.append(x)` |
| `dequeue(q)` | remove and return head | `q.pop(0)` |
| `front(q)` | look at head, don't remove | `q[0]` |
| `is_empty(q)` | is it empty? | `q == []` |
| `size(q)` | count items | `len(q)` |
| `make_queue(seq)` | build one from a sequence | `list(seq)` |
| `clear(q)` | remove everything, **in place** | `q.clear()` |

> [!important]
> Head = index `0`. Tail = end of the list. A queue removes from the **front**, so it uses `pop(0)`.

> [!warning] Modifiers mutate in place
> `enqueue`, `dequeue` and `clear` must change the queue passed in — *"they should not return a new queue"*. `q = []` inside `clear` rebinds the local name and leaves the caller's list untouched. `q.clear()` empties it.

An **array-based fixed-size queue** needs two pointers: a **head pointer** marking the next item to leave, and a **tail pointer** marking the last item added. Papers ask for these by name. The Python-list version below doesn't need them — `append()` and `pop(0)` handle the positions.

## Template

```python
def enqueue(q, item):
    q.append(item)

def dequeue(q):
    if q == []:
        return None
    return q.pop(0)

def front(q):
    if q == []:
        return None
    return q[0]
```

> [!important] Guard both ends
> `dequeue` must check **empty**, and on a fixed-size queue `enqueue` must check **full**. The y27 specimen Paper 2 writes both into the spec — `enqueue()` *"returns False if the queue is full"*, `dequeue()` *"returns -1 if the queue is empty"* — so each guard is carrying marks. See [The y27 Specimen Version](#the-y27-specimen-version).

> [!example]- Trace: enqueue and dequeue
> | Step | Operation | Queue after | Returns |
> | ---- | --------- | ----------- | ------- |
> | 1 | `make_queue()` | `[]` | — |
> | 2 | `dequeue(q)` | `[]` | `None` — nothing to dequeue |
> | 3 | `enqueue(q, 5)` | `[5]` | — |
> | 4 | `enqueue(q, 3)` | `[5, 3]` | — |
> | 5 | `front(q)` | `[5, 3]` | `5` |
> | 6 | `dequeue(q)` | `[3]` | `5` |
> | 7 | `dequeue(q)` | `[]` | `3` |
> | 8 | `is_empty(q)` | `[]` | `True` |

## When the Queue Is Given as a Class

Assessments hand you a ready-made `Queue` in a module. You **use** its methods instead of writing your own:

```python
from queue_module import *

q = Queue()                    # create
q.enqueue(("Sophia", 28))      # add to tail
q.dequeue()                    # remove head and return it
q.size()                       # number of items
q.display()                    # print the queue
```

Same FIFO idea — only the call style changes: `q.enqueue(x)` instead of `enqueue(q, x)`. Check emptiness with `q.size() != 0`, since there may be no `is_empty` method.

## Linear vs Circular Queue

> [!important] Syllabus 2.1.1 names **linear and circular**. Asked 2020 Q3(h) `[2]` and 2023 Q4(d)(iv) `[2]`.

In a **fixed-size array**, every `dequeue` moves the head forward and leaves a dead slot behind it. The queue eventually reports "full" while the front of the array sits empty.

```text
size 5 - three enqueued, two dequeued

index   0     1     2     3     4
      +-----+-----+-----+-----+-----+
      |  .  |  .  |  C  |     |     |
      +-----+-----+-----+-----+-----+
         ^     ^     ^     ^
         |     |     |     +- next free slot (after tail)
         |     |     +------- head
         +-----+------------- dead space
```

A **circular queue** wraps the pointers back to `0`, so the vacated slots are reused.

```python
tail = (tail + 1) % size      # enqueue
head = (head + 1) % size      # dequeue
```

| | Linear | Circular |
| --- | ------ | -------- |
| When tail hits the end | queue is "full", even with free slots at the front | wraps round to index `0` |
| Vacated front slots | wasted | reused |
| Fix without wrapping | shift every element left — slow | not needed |
| Full test | `tail == size - 1` | `count == size` |

**Two differences (2020 answer):** the circular queue wraps its pointers using modulo so the array is reused, whereas the linear queue's space is used once and then wasted.

**Advantage (2023 answer):** memory is used efficiently — freed positions are reclaimed, so a fixed array does not fill up prematurely and elements never need shifting.

> [!warning]
> `head == tail` doesn't tell you the state on its own — it can mean one item, empty, or full. Keep a separate count, or leave one slot permanently unused.

> [!example]- Specimen Paper 1 Q2(c) — the same queue on the theory paper
> A circular queue holding at most 5 items, `China` at index 2 (HeadPointer) and `Oman` at index 3 (TailPointer).
>
> **(i) Purpose of the two pointers** `[2]` — the head pointer holds the position of the item that will be removed next; the tail pointer holds the position of the last item added, so the next enqueue goes after it.
>
> **(ii) After `Dequeue()`, `Enqueue("Togo")`, `Enqueue("USA")`, `Dequeue()`** `[2]`
>
> | Index | 0 | 1 | 2 | 3 | 4 |
> | ----- | - | - | - | - | - |
> | Data | USA | | | | Togo |
>
> HeadPointer = `4`, TailPointer = `0`. `USA` wraps to index 0 because the tail was already at 4. That wrap is what the question tests.
>
> The dequeued items, `China` and `Oman`, then get inserted into a binary search tree — see [[LT11b Binary Tree]].

### The y27 Specimen Version

> [!important] Specimen Paper 2, Tasks 2.1, 2.2 and 2.5 — **8 marks altogether**, the model for your 2027 lab paper.
> A 1-D array of 10 initialised to `-1`, pointers named `headpointer` and `tailpointer` both starting at `-1`, and `items_in_queue` starting at `0`. That third variable is the "keep a separate count" fix above — the paper hands it to you rather than making you invent it.
>
> | Task | What it asks for | Marks |
> | ---- | ---------------- | ----- |
> | 2.1 | declare and initialise the array, both pointers, `items_in_queue` | `[1]` |
> | 2.2 | `enqueue()` — return `False` if full; else store, update pointer(s) and count, return `True` | `[4]` |
> | 2.5 | `dequeue()` — return `-1` if empty; else return the next element and update pointer(s) and count | `[3]` |
>
> The marks sit on the **guard**, the **wrap**, and updating **both** the pointer and the count.

The paper states the convention: *"`tailpointer` stores the index of the **last element** in the queue"*. A worked answer to 2.1, 2.2 and 2.5:

```python
MAX_SIZE = 10
queue = [-1] * MAX_SIZE
headpointer = -1
tailpointer = -1
items_in_queue = 0

def enqueue(item):
    global headpointer, tailpointer, items_in_queue

    if items_in_queue == MAX_SIZE:
        return False

    if items_in_queue == 0:
        headpointer = 0
        tailpointer = 0
    else:
        tailpointer = (tailpointer + 1) % MAX_SIZE

    queue[tailpointer] = item
    items_in_queue += 1
    return True

def dequeue():
    global headpointer, tailpointer, items_in_queue

    if items_in_queue == 0:
        return -1

    item = queue[headpointer]
    queue[headpointer] = -1
    items_in_queue -= 1

    if items_in_queue == 0:
        headpointer = -1
        tailpointer = -1
    else:
        headpointer = (headpointer + 1) % MAX_SIZE

    return item
```

> [!warning]
> Other books put the tail at the **next free slot** instead. Both work, but the initial values and the full/empty tests differ. Pick one and stick to it.

## Stack vs Queue

| | [[LT10b Stack\|Stack]] | Queue |
| --- | ----- | ----- |
| Order | LIFO | FIFO |
| Add | `push` | `enqueue` |
| Remove | `pop` — from the top | `dequeue` — from the head |
| Look | `peek` — top | `front` — head |
| Openings | **one** — in and out at the top | **two** — in at the tail, out at the head |
| Shape | vertical | horizontal |

```text
Stack: [1, 2, 3] -> pop()     -> 3    (last in)
Queue: [1, 2, 3] -> dequeue() -> 1    (first in)
```

## Applications

Used whenever arrival order must be preserved:

- process scheduling
- network printer queue
- keyboard buffer

| Problem wording | Queue operation |
| --------------- | --------------- |
| send a job | `enqueue(printq, job)` |
| print the next job | `dequeue(printq)` |
| see what's next | `front(printq)` |
| cancel a job | not a queue operation — rotate it out using the ones you're given |

## Rotating a Queue

```python
item = dequeue(q)
enqueue(q, item)
```

```text
[A, B, C, D]  ->  rotate  ->  [B, C, D, A]
```

Pass-the-parcel pattern: rotate `n` times, then dequeue one player, and repeat until one remains.

## Common Mistakes

- Using `pop()` instead of `pop(0)` — that turns it into a stack.
- Treating `front()` as if it removes the item.
- Dequeuing an empty queue instead of returning `None`.
- Forgetting that after `pop(0)` every later item shifts left by one.

## Related

- [[LT10a Data Abstraction]]
- [[LT10b Stack]]
- [[LT11b Binary Tree]]
