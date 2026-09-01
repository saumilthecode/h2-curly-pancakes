> [!summary] Quick View
> `random` generates **pseudo-random** values for simulations, games and sampling.

## Pseudo-Random

Python's random numbers are not truly random — they come from a deterministic formula.

- The same **seed** always produces the same sequence.
- With no seed, Python takes one from the operating system.

```python
from random import *

seed(30)     # optional - makes results repeatable for testing
```

## Numbers

| Function | Gives | In BTB4? |
| -------- | ----- | -------- |
| `random()` | float from `0.0` up to but **not including** `1.0` | yes |
| `randint(a, b)` | integer from `a` to `b`, **both included** | yes |
| `randrange(start, stop, step)` | integer from a range, `stop` excluded | no |

```python
x = randint(1, 6)              # a dice roll
x = round(random() * 5, 2)     # float from 0 to 5, 2 decimal places
```

## Choosing From a List

| Function | Gives | In BTB4? |
| -------- | ----- | -------- |
| `choice(lst)` | one item | yes |
| `sample(lst, k)` | `k` items, no repeats | yes |
| `choices(lst, k=k)` | `k` items, repeats allowed | yes |
| `shuffle(lst)` | reorders the list **in place** | no |

> [!note]
> `randrange` and `shuffle` are **not** in the BTB4 lecture — they're here because the Paper 2 Reference Guide lists them. Conversely `seed`, `choice`, `choices`, `sample` and `normalvariate` are taught but aren't on that handout. The Reference Guide is a quick-reference sheet; it does not define what's allowed. It also leaves out `.strip()`, which your own mark scheme gives a mark for.

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

- [[LT7 Lists]]
- [[LT5 Iteration]]
- [[LT1 basic python]]
