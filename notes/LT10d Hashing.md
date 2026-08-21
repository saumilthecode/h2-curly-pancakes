> [!summary] Quick View
> A hash function turns data into a number. A hash table stores an item at `hash(item) % table_size` so it can be found without searching.

## What Hashing Is

A hash function produces a digital fingerprint of the data — the **hash value**, **digest** or **checksum**.

> [!important] "State three features of a good hashing algorithm" — `[3]`, asked 2021 and 2022
> The three characteristics from the LT10d lecture are the answer.

| Characteristic | Meaning |
| -------------- | ------- |
| Secure | non-reversible — you cannot get the data back from the hash |
| Fixed size | long or short input produces a fixed-size digest |
| Unique\* | ideally no two inputs share a digest |

> [!warning]
> \*Not true in reality — **collisions do occur**. Hashing is for comparison, **not encryption**.

## Why Use a Hash Table

> [!important] 2021 Q5 asked both halves — hash table vs linear search `[2]`, and the disadvantage of binary search here `[2]`.

Searching is a **single calculation plus one lookup** — no scanning.

| Search method | Time complexity | Needs sorted data? |
| ------------- | --------------- | ------------------ |
| Hash table | `O(1)` | no |
| Linear search | `O(n)` | no |
| Binary search | `O(log n)` | **yes** |

- **vs linear search** — linear may check every record, so it gets slower as the data grows. A hash lookup stays constant no matter how large the table is.
- **vs binary search** — binary search is fast, but the data must be kept **sorted**. Maintaining that order on every insertion and deletion is expensive for large, frequently-changing datasets.

## The Lesson Hash Function

Uses the ASCII value of each character, weighted by its position.

> [!warning] Why the weight is needed
> Just summing the ASCII values ignores **order** — `abc`, `bca` and `cab` all total `294`, so anagrams collide every time. Multiplying each character by `i + 1` makes position count.

```python
def hash(string):
    total = 0
    for i in range(len(string)):
        total += ord(string[i]) * (i + 1)
    return total
```

```text
"abcde" -> 97*1 + 98*2 + 99*3 + 100*4 + 101*5 = 1495
1495 % 10 = 5
```

The `% n` is kept **outside** the hash function, because `n` depends on the size of the table.

## Checksum

Append a check value so the receiver can detect transmission errors.

```text
message =  abcde  5
           └─┬─┘  └─ checksum
             │
            data
```

The receiver re-hashes the data and compares it against the checksum.

For 5-digit data the lesson scheme weights the digits `3, 5, 7, 9, 11`:

```python
def transmit(data):
    total = 0
    for i in range(len(data)):
        total += int(data[i]) * ((2 * i) + 3)
    return data + str(total % 10)
```

```text
"12345" -> 1*3 + 2*5 + 3*7 + 4*9 + 5*11 = 125
125 % 10 = 5
transmitted: 123455
```

Real uses: NRIC, vehicle plate numbers, ISBN, credit card (Luhn).

## Hash Table

```python
def init_table(n):
    return [''] * n

index = hash(item) % len(table)
```

Storing `['cdab', 'dbac', 'dabc', 'bdac', 'badc']` in a table of size 5:

| Item | Hash value | `% 5` |
| ---- | ---------- | ----- |
| `cdab` | `982` | `2` |
| `dbac` | `983` | `3` |
| `dabc` | `984` | `4` |
| `bdac` | `985` | `0` |
| `badc` | `988` | `3` ← collision |

Searching without collisions is a single lookup — no linear search needed:

```python
def search(table, item):
    i = hash(item) % len(table)
    return table[i] == item
```

## Collision

Two items hash to the **same index**. Note they need not have the same hash value:

```text
hash("dbac") = 983  ->  983 % 5 = 3
hash("badc") = 988  ->  988 % 5 = 3
```

## Collision Resolution

| Method | Also called | Idea |
| ------ | ----------- | ---- |
| Separate chaining | open hashing | store a list at that slot |
| Linear probing | closed hashing | move to the next empty slot |

### Separate Chaining

```text
 0  'bdac'
 1  ''
 2  'cdab'
 3  ['dbac', 'badc']   ← both live here
 4  'dabc'
```

```python
if tbl[i] == '':
    tbl[i] = ele
elif type(tbl[i]) != list:
    tbl[i] = [tbl[i], ele]      # promote to a list
else:
    tbl[i] = tbl[i] + [ele]
```

Searching: if the slot holds a list, do a linear search inside it (`item in tbl[i]`).

### Linear Probing

From the assigned slot, look for the next empty one, wrapping around at the end.

```text
 badc -> index 3 taken
       -> 4 taken
       -> 0 taken
       -> 1 empty ✓

 0  'bdac'
 1  'badc'   ← ended up here
 2  'cdab'
 3  'dbac'
 4  'dabc'
```

```python
i = (i + 1) % len(table)
```

> [!important]
> Loop at most `len(table)` times. A full table would otherwise probe forever.

Searching must follow the **same probe path** — check the assigned slot, then step forward the same way until you find the item or an empty slot.

## Common Mistakes

- Forgetting `% len(table)`.
- Thinking hashing is encryption — it is one-way and used for comparison.
- Assuming collisions never happen.
- Searching a linear-probed table without following the probe path.
- Forgetting a chained slot may hold either a plain value **or** a list.

## Related

- [[LT10a Data Abstraction]]
- [[LT8 Dictionary]]
- [[LT11a Search]]
- [[LT4a Data validation and verification]]
