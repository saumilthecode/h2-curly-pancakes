> [!summary] Quick View
> Hashing turns data into a hash value. Hash tables use `hash(item) % table_size` to decide where to store/search.

## Hashing Idea

Hashing creates a digital fingerprint of data.

- The output is called a hash value, digest, or checksum.
- It is mainly for checking/comparison, not encryption.
- A good hash is fixed-size and hard to reverse.
- Collisions can happen: different data can produce the same index or hash.

![[hash-checksum.svg]]

## Simple Hash Function

This lesson hash uses ASCII values and position weights.

```python
def hash_value(string):
    total = 0

    for i in range(len(string)):
        total += ord(string[i]) * (i + 1)

    return total
```

Example:

```text
"abcde"
= 97*1 + 98*2 + 99*3 + 100*4 + 101*5
= 1495

1495 % 10 = 5
```

> [!warning]
> Python already has a built-in `hash()` function. In exams, use the function name given by the question. In your own notes/code, `hash_value()` is clearer.

## Checksum Pattern

Checksum means attaching a check value to the data.

```python
def transmit(data):
    total = 0

    for i in range(len(data)):
        total += int(data[i]) * ((2 * i) + 1)

    return data + str(total % 10)
```

Example:

```python
print(transmit("12345"))  # 123455
```

Use cases:

- NRIC check letter
- vehicle plate check character
- ISBN check digit
- credit card validation

## Hash Table

A hash table is an array/list where the hash value decides the index.

```text
index = hash_value(item) % len(table)
```

![[hash-table-index.svg]]

Without collisions:

```python
def init_table(n):
    return [""] * n

def hashtable(seq):
    table = init_table(len(seq))

    for item in seq:
        index = hash_value(item) % len(table)
        if table[index] == "":
            table[index] = item
        else:
            print(item, "cannot be added, collision")

    return table
```

Search without collisions:

```python
def search(table, item):
    index = hash_value(item) % len(table)
    return table[index] == item
```

## Collision

A collision happens when two items want the same index.

Example:

```text
hash_value("dbac") % 5 = 3
hash_value("badc") % 5 = 3
```

## Separate Chaining

Separate chaining stores a list at the collided index.

![[hash-chain.svg]]

```python
def hashtable_chain(seq):
    table = init_table(len(seq))

    for item in seq:
        index = hash_value(item) % len(table)

        if table[index] == "":
            table[index] = item
        elif isinstance(table[index], list):
            table[index].append(item)
        else:
            table[index] = [table[index], item]

    return table
```

Search with separate chaining:

```python
def search_chain(table, item):
    index = hash_value(item) % len(table)

    if table[index] == "":
        return False
    if isinstance(table[index], list):
        return item in table[index]
    return table[index] == item
```

## Linear Probing

Linear probing searches for the next empty slot.

- Start at the hashed index.
- If full, try the next index.
- If at the end, wrap back to index `0`.
- Stop after checking at most `len(table)` slots.

![[hash-linear.svg]]

Core wrap-around pattern:

```python
index = (index + 1) % len(table)
```

Hash table with linear probing:

```python
def hashtable_probe(seq):
    table = init_table(len(seq))

    for item in seq:
        index = hash_value(item) % len(table)
        checked = 0

        while table[index] != "" and checked < len(table):
            index = (index + 1) % len(table)
            checked += 1

        if checked < len(table):
            table[index] = item

    return table
```

Search with linear probing:

```python
def search_probe(table, item):
    index = hash_value(item) % len(table)
    checked = 0

    while checked < len(table):
        if table[index] == item:
            return True
        if table[index] == "":
            return False

        index = (index + 1) % len(table)
        checked += 1

    return False
```

## Collision Methods

| Method | Idea | Where collided item goes |
| ------ | ---- | ------------------------ |
| separate chaining | store a list at the slot | same index, inside a list |
| linear probing | scan for another empty slot | next available index |

## Common Mistakes

- Forgetting `% len(table)`, so the index may go out of range.
- Thinking hashing is encryption. It is not meant to be reversed.
- Assuming collisions never happen.
- In linear probing, forgetting wrap-around with `% len(table)`.
- In linear probing, using `while True` without a limit. This can infinite loop if the table is full.
- In separate chaining, forgetting that a slot may store either a string or a list.

## Related

- [[Data Abstraction]]
- [[C2 - Data representation]]
