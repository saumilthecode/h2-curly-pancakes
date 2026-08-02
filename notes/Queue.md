> [!summary] Quick View
> Queue = FIFO: First In, First Out. Add at tail, remove from head.

## Queue Playground

<iframe class="note-widget-frame queue-simulator" src="./pictures/queue-simulator.html" title="Interactive queue playground" style="width:100%;height:520px;border:1px solid #d8d3ca;border-radius:8px;background:#fff;"></iframe>

[Open standalone queue playground](./pictures/queue-simulator.html)

## Operations

| Operation | What it does | List code |
| --------- | ------------ | --------- |
| `make_empty_queue()` | creates empty queue | `[]` |
| `make_queue(seq)` | creates queue from sequence | `list(seq)` |
| `enqueue(queue, item)` | adds item at tail | `append(item)` |
| `dequeue(queue)` | removes and returns head item | `pop(0)` |
| `front(queue)` | returns head item only | `queue[0]` |
| `is_empty(queue)` | checks empty queue | `queue == []` |
| `size(queue)` | counts items | `len(queue)` |
| `clear(queue)` | removes everything | `clear()` |

> [!important]
> Head = index `0`. Tail = end of the Python list.

## Template

```python
def make_empty_queue():
    return []

def make_queue(seq):
    return list(seq)

def is_empty(queue):
    return queue == []

def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if is_empty(queue):
        return None
    return queue.pop(0)

def front(queue):
    if is_empty(queue):
        return None
    return queue[0]

def size(queue):
    return len(queue)

def clear(queue):
    queue.clear()
```

## Trace

```text
start:          []
enqueue 5:      [5]
enqueue 3:      [5, 3]
dequeue -> 5:   [3]
dequeue -> 3:   []
```

## Stack vs Queue

| Feature | Stack | Queue |
| ------- | ----- | ----- |
| Order | LIFO | FIFO |
| Add | `push()` at top | `enqueue()` at tail |
| Remove | `pop()` from top | `dequeue()` from head |
| Inspect | `peek()` | `front()` |
| List removal | `pop()` | `pop(0)` |

```text
Stack: [1, 2, 3] -> pop()     -> 3
Queue: [1, 2, 3] -> dequeue() -> 1
```

## Uses

- printer queue
- keyboard buffer
- process scheduling
- customers waiting in order
- rotating games/playlists

## Pattern 1: Printer Queue

Rename queue operations to match the problem.

```python
def make_print_queue():
    return make_empty_queue()

def send_job(printq, job):
    enqueue(printq, job)

def print_job(printq):
    return dequeue(printq)

def cancel_job(printq, job):
    if job in printq:
        printq.remove(job)

def next_job(printq):
    return front(printq)

def num_jobs(printq):
    return size(printq)
```

```python
hp_printer = make_print_queue()
send_job(hp_printer, "phys quiz.doc")
send_job(hp_printer, "maths quiz.doc")
cancel_job(hp_printer, "maths quiz.doc")
print(print_job(hp_printer))  # phys quiz.doc
```

## Pattern 2: Rotating Queue

Rotate once = dequeue head, enqueue it at tail.

```python
def current_song(playlist, minutes):
    song_queue = make_queue(playlist)
    if size(song_queue) == 0:
        return None

    songs_completed = int(minutes // 4)
    rotations = songs_completed % size(song_queue)

    for i in range(rotations):
        finished_song = dequeue(song_queue)
        enqueue(song_queue, finished_song)

    return front(song_queue)
```

## Pattern 3: Pass the Bomb

This follows the notebook rule: rotate `n` times, then remove the next player.

Tiny trace for players `[A, B, C]`, `n = 1`:

```python
def who_wins(players, n):
    queue = make_queue(players)

    while size(queue) != 1:
        for i in range(n):
            player = dequeue(queue)
            enqueue(queue, player)
        dequeue(queue)

    return front(queue)
```

## Common Mistakes

- Queue uses `pop(0)`, not `pop()`.
- `front()` does not remove.
- `dequeue()` on an empty queue should return `None`.

## Related

- [[Data Abstraction]]
- [[Stack]]
