> [!summary] Quick View
> `random` generates **pseudo-random** values for simulations, games and sampling.

## Pseudo-Random

Python's random numbers are not truly random — they come from a deterministic formula.

- The same **seed** always produces the same sequence.
- With no seed, Python uses the current system time.

```python
from random import *

seed(30)     # optional — makes results repeatable for testing
```

## Numbers

| Function | Gives |
| -------- | ----- |
| `random()` | float from `0.0` up to but **not including** `1.0` |
| `randint(a, b)` | integer from `a` to `b`, **both included** |
| `randrange(start, stop, step)` | integer from a range, `stop` excluded |

```python
x = randint(1, 6)              # a dice roll
x = round(random() * 5, 2)     # float from 0 to 5, 2 decimal places
```

## Choosing From a List

| Function | Gives |
| -------- | ----- |
| `choice(lst)` | one item |
| `sample(lst, k)` | `k` items, no repeats |
| `choices(lst, k=k)` | `k` items, repeats allowed |
| `shuffle(lst)` | reorders the list **in place** |

```python
from random import *

lst = ["Adam", "Bob", "Charles", "Daniel"]

print(choice(lst))       # 'Bob'
print(sample(lst, 2))    # ['Daniel', 'Adam']
```

## Normal Distribution

```python
lst = []
for i in range(1000):
    lst.append(normalvariate(50, 7))    # mean 50, standard deviation 7
```

Check the result:

```python
from statistics import mean, stdev

print(mean(lst))
print(stdev(lst))
```

## Common Mistakes

- Expecting `randint(1, 6)` to exclude `6` — it doesn't, unlike `range`.
- Expecting `shuffle()` to return the list; it returns `None` and shuffles in place.
- Calling `sample(lst, k)` with `k` larger than the list — that's an error.
- Setting a seed and then wondering why the "random" values never change.

## Related

- [[Lists]]
- [[Iteration]]
- [[basic python]]
