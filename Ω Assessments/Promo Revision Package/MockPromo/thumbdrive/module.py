"""Functional ADT helpers and hash function supplied for MOCK PROMO Paper 2."""

__all__ = [
    "make_empty_queue",
    "is_empty_queue",
    "queue_size",
    "enqueue",
    "dequeue",
    "make_empty_stack",
    "is_empty_stack",
    "hash_locker",
]


# Queue ADT
def make_empty_queue():
    return []


def is_empty_queue(queue):
    return queue == []


def queue_size(queue):
    return len(queue)


def enqueue(queue, item):
    queue.append(item)


def dequeue(queue):
    if is_empty_queue(queue):
        return None
    return queue.pop(0)


# Stack ADT
def make_empty_stack():
    return []


def is_empty_stack(stack):
    return stack == []


# Hash-table helper
def hash_locker(locker_code, table_size):
    """Return the initial table index for a locker code."""
    total = 0
    for character in locker_code:
        total += ord(character)
    return total % table_size
