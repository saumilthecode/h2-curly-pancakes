> [!summary] Quick View
> Hashing turns data into a hash value. Hash tables use `hash(item) % table_size` to choose an index.

## Collision Trace

<details>
<summary>`dbac` and `badc` both hash to index `3` when table size is `5`</summary>
<table>
  <thead>
    <tr><th>Item</th><th>Hash value</th><th>Index calculation</th></tr>
  </thead>
  <tbody>
    <tr><td><code>dbac</code></td><td><code>988</code></td><td><code>988 % 5 = 3</code></td></tr>
    <tr><td><code>badc</code></td><td><code>988</code></td><td><code>988 % 5 = 3</code></td></tr>
  </tbody>
</table>
<p>Both want the same slot, so use separate chaining or linear probing.</p>
</details>

## Hashing Idea

Hashing creates a fixed-ish numeric fingerprint from data.

- Used for quick lookup/checking/comparison.
- Not the same as encryption.
- Collisions can happen.

## Lesson Hash Function

The notebook hash uses ASCII values and position weights.

```python
def hash_value(string):
    total = 0
    for i in range(len(string)):
        total += ord(string[i]) * (i + 1)
    return total
```

Example:

```text
"abcde" -> 97*1 + 98*2 + 99*3 + 100*4 + 101*5 = 1495
1495 % 10 = 5
```

> [!warning]
> Python already has built-in `hash()`. In exam code, use the name given by the question.

## Checksum Pattern

Checksum = append a check value to detect mistakes.

```python
def transmit(data):
    total = 0
    for i in range(len(data)):
        total += int(data[i]) * ((2 * i) + 1)
    return data + str(total % 10)
```

```python
transmit("12345")  # "123455"
```

Uses: NRIC check letter, vehicle plate check character, ISBN, credit card validation.

## Hash Table

Index formula:

```python
index = hash_value(item) % len(table)
```

No collision search:

```python
def search(table, item):
    index = hash_value(item) % len(table)
    return table[index] == item
```

## Collision

Collision = two items want the same index.

```text
hash_value("dbac") % 5 = 3
hash_value("badc") % 5 = 3
```

## Collision Fixes

| Method | Idea | Search consequence |
| ------ | ---- | ------------------ |
| separate chaining | store a list at the slot | check inside the list |
| linear probing | scan to next empty slot | follow same scan path |

Separate chaining insert idea:

```python
if table[index] == "":
    table[index] = item
elif isinstance(table[index], list):
    table[index].append(item)
else:
    table[index] = [table[index], item]
```

Linear probing step:

```python
index = (index + 1) % len(table)
```

Stop after checking at most `len(table)` slots, otherwise a full table can loop forever.

## Common Mistakes

- Forgetting `% len(table)`.
- Thinking hashing means encryption.
- Assuming collisions never happen.
- Searching linear probing without following the probe path.
- Forgetting a chained slot can hold either a string or a list.

## Related

- [[Data Abstraction]]
- [[C2 - Data representation]]
