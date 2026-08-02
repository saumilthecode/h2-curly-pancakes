> [!summary] Quick View
> Queue = FIFO: First In, First Out. Add at tail, remove from head.

## Queue Trace

<details open>
<summary>Enqueue and dequeue example</summary>

| Step | Operation | Queue after step | Return |
| ---- | --------- | ---------------- | ------ |
| 1 | start | `[]` | - |
| 2 | `enqueue("A")` | `["A"]` | - |
| 3 | `enqueue("B")` | `["A", "B"]` | - |
| 4 | `front()` | `["A", "B"]` | `"A"` |
| 5 | `dequeue()` | `["B"]` | `"A"` |

</details>

## Core Operations

| Operation | Meaning | Python list |
| --------- | ------- | ----------- |
| `enqueue(q, x)` | add to tail | `q.append(x)` |
| `dequeue(q)` | remove head | `q.pop(0)` |
| `front(q)` | look at head | `q[0]` |
| `is_empty(q)` | check empty | `q == []` |
| `size(q)` | count items | `len(q)` |

> [!important]
> Head = index `0`. Tail = end of list.

## Minimal Template

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

Trace:

```text
[] -> enqueue 5 -> [5]
[5] -> enqueue 3 -> [5, 3]
[5, 3] -> dequeue -> [3] and returns 5
```

## Stack vs Queue

| Structure | Remove from | Order |
| --------- | ----------- | ----- |
| stack | top/end | LIFO |
| queue | head/index `0` | FIFO |

```text
Stack: [1, 2, 3] -> pop()     -> 3
Queue: [1, 2, 3] -> dequeue() -> 1
```

## Common Patterns

Printer queue:

| Problem word | Queue operation |
| ------------ | --------------- |
| send job | `enqueue(printq, job)` |
| print next job | `dequeue(printq)` |
| see next job | `front(printq)` |
| cancel job | `printq.remove(job)` |

Rotating queue:

```python
item = dequeue(q)
enqueue(q, item)
```

Pass-the-bomb idea:

```text
rotate n times, then dequeue one player
repeat until one player remains
```

## Common Mistakes

- Queue uses `pop(0)`, not `pop()`.
- `front()` does not remove.
- `dequeue()` on empty queue should return `None`.
- After `pop(0)`, all later items shift left.

## Related

- [[Data Abstraction]]
- [[Stack]]
