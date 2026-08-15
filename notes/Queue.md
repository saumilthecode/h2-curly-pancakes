> [!summary] Quick View
> Queue = **FIFO**, First In First Out. Add at the tail, remove from the head.

```text
  dequeue ◀──┌───┬───┬───┬───┐◀── enqueue
             │ A │ B │ C │ D │
             └───┴───┴───┴───┘
             head          tail
             q[0]          q[-1]
```

## Core Operations

| Operation | Meaning | Python list |
| --------- | ------- | ----------- |
| `enqueue(q, x)` | add to tail | `q.append(x)` |
| `dequeue(q)` | remove and return head | `q.pop(0)` |
| `front(q)` | look at head, don't remove | `q[0]` |
| `is_empty(q)` | is it empty? | `q == []` |
| `size(q)` | count items | `len(q)` |

> [!important]
> Head = index `0`. Tail = end of the list. A queue removes from the **front**, so it uses `pop(0)`.

Implementing a queue needs **two pointers**: a **head pointer** marking the next item to leave, and a **tail pointer** marking where the next item is added. Papers ask for these by name.

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

Assessments often hand you a ready-made `Queue` in a module. You **use** its methods rather than writing your own functions:

```python
from queue_module import *

q = Queue()                    # create
q.enqueue(("Sophia", 28))      # add to tail
q.dequeue()                    # remove head and return it
q.size()                       # number of items
q.display()                    # print the queue
```

Same FIFO idea — only the call style changes: `q.enqueue(x)` instead of `enqueue(q, x)`. Check emptiness with `q.size() != 0`, since there may be no `is_empty` method.

## Stack vs Queue

| | [[Stack]] | Queue |
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
| cancel a job | `printq.remove(job)` |

## Rotating a Queue

Take from the head, put straight back on the tail.

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

- [[Data Abstraction]]
- [[Stack]]
