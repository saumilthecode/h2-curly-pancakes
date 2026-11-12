#queue ADT

def make_empty_queue():
    return []

def make_queue(seq):
    q = make_empty_queue()
    for ele in seq:
        enqueue(q, ele)
    return q

def enqueue(queue, item):
    queue.append(item)

def is_empty_queue(queue):
    return len(queue) == 0

def front(queue):
    if is_empty_queue(queue):
        return None
    else:
        return queue[0]

def dequeue(queue):
    if is_empty_queue(queue):
        return None
    else:
        return queue.pop(0)