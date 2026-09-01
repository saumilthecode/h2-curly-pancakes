> [!summary] Quick View
> A hash function turns a key into an index. A hash table gives expected `O(1)` insertion and lookup, but collisions must be handled correctly.

## Two Uses of Hashing

The word *hash* is used for two related but different jobs:

| | Hash-table function | Cryptographic hash |
| --- | --- | --- |
| Purpose | map a key to a table index | make a fixed-length fingerprint of data |
| Priorities | fast, deterministic, evenly distributed | one-way and collision-resistant |
| Collision | expected and handled by the table | possible, but deliberately hard to find |
| Examples | weighted character sum, `key % size` | SHA-256 |

> [!important] "State three features of a good hashing algorithm" `[3]` — 2021 Q5(a) and 2022 Q8(d)
> Asked twice in five years, same 3 marks. The marked answer is about the **table**, not security:
>
> | Feature | Meaning |
> | ------- | ------- |
> | Deterministic | the same key always hashes to the same value |
> | Uniform distribution | values spread evenly across the table |
> | Minimises clustering | few keys collide onto the same index |

> [!warning] The lecture's three characteristics answer a different question
> LT10d Part 1 gives *"Secure: non-reversible / Fixed size / Unique\*"*. Those describe a **cryptographic** hash (SHA-256), not the table function above. Use them if a question says *secure hash algorithm*; use the table above when it says *hash table*.
>
> Don't claim the simple weighted-sum function is secure or non-reversible; it exists to place items in a table. `Unique` carries an asterisk in the lecture because **collisions do occur**.

## Why Use a Hash Table

> [!important] 2021 Q5 asked both halves — hash table vs linear search `[2]`, and the disadvantage of binary search here `[2]`.

Without a collision, searching is a **single calculation plus one lookup**. Collisions add extra comparisons.

| Search method | Expected / usual | Worst case | Needs sorted data? |
| ------------- | ---------------- | ---------- | ------------------ |
| Hash table | `O(1)` | `O(n)` if many keys collide | no |
| Linear search | `O(n)` | `O(n)` | no |
| Binary search | `O(log n)` | `O(log n)` | **yes** |

- **vs linear search** — linear may check every record. A hash lookup checks one slot, or a short probe chain after a collision.
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
           +-+-+  +- checksum
             |
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

Real uses: NRIC, vehicle plate numbers, ISBN, credit card (Luhn). Every one is the same shape — **weight each digit, sum, take a modulus** — only the weights, the modulus and the final mapping change.

> [!example]- The two tutorial schemes
> **NRIC** `S1234567D` — weights `2, 7, 6, 5, 4, 3, 2` on the seven digits, `+ 4` if the prefix is `T`, then `% 11` mapped through `J Z I H G F E D C B A` (remainder `0` → `J`).
>
> ```python
> def last_letter(nric):
>     weights = [2, 7, 6, 5, 4, 3, 2]
>     total = 0
>     for i in range(7):
>         total += int(nric[i + 1]) * weights[i]
>     if nric[0] == 'T':
>         total += 4
>     return 'JZIHGFEDCBA'[total % 11]
> ```
>
> `S1234567` totals `106`, `106 % 11 = 7` → `D`. `T1234567` totals `110` → `J`.
>
> **ISBN-10** — weights `10, 9, 8, ..., 2` on the nine digits, check digit `(11 - total % 11) % 11`, and `10` is written `X`.
>
> ```python
> def isbn(string):
>     total = 0
>     for i in range(9):
>         total += int(string[i]) * (10 - i)
>     check = (11 - total % 11) % 11
>     return string + ('X' if check == 10 else str(check))
> ```
>
> `075154926` totals `214`, `214 % 11 = 5`, so the check digit is `6` → `0751549266`.

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
 3  ['dbac', 'badc']   < both live here
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

Make every slot a list from the start and there's no special case:

```python
def make_chained_table(size):
    return [[] for _ in range(size)]

def insert_chained(table, item):
    index = hash(item) % len(table)
    table[index].append(item)

def search_chained(table, item):
    index = hash(item) % len(table)
    return item in table[index]
```

If the question says each slot holds `''`, `-1`, a record or a class, use that — don't swap in your own.

### Linear Probing

From the assigned slot, look for the next empty one, wrapping around at the end.

```text
 badc -> index 3 taken
       -> 4 taken
       -> 0 taken
       -> 1 empty *

 0  'bdac'
 1  'badc'   < ended up here
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

```python
def insert_probe(table, item):
    index = hash(item) % len(table)
    for _ in range(len(table)):
        if table[index] == '':
            table[index] = item
            return True
        index = (index + 1) % len(table)
    return False                         # table is full

def search_probe(table, item):
    index = hash(item) % len(table)
    for _ in range(len(table)):
        if table[index] == item:
            return True
        if table[index] == '':
            return False                # probe chain has ended
        index = (index + 1) % len(table)
    return False
```

## Common Mistakes

- Forgetting `% len(table)`.
- Treating a table hash as encryption or assuming it has cryptographic security.
- Assuming collisions never happen.
- Searching a linear-probed table without following the probe path.
- Forgetting a chained slot may hold either a plain value **or** a list.

## Related

- [[LT10a Data Abstraction]]
- [[LT8 Dictionary]]
- [[LT11a Search]]
- [[LT4a Data validation and verification]]
