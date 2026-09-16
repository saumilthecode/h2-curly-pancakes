# Queue ADT
# Do not modify this file


def make_empty_queue():
    return []


def make_queue(seq):
    return list(seq)


def enqueue(q, item):
    q.append(item)


def dequeue(q):
    return q.pop(0)


def front(q):
    if is_empty(q):
        print("Queue is empty")
        return None
    return q[0]


def size(q):
    return len(q)


def clear(q):
    q.clear()


def is_empty(q):
    return size(q) == 0
