> [!summary] Quick View
> Python's `random` module generates pseudo-random values for simulations, games, and sampling.

## Pseudo-Random Numbers

Python random numbers are not truly random.

- They are generated using a deterministic formula.
- If the same seed is used, the same sequence is generated.
- If no seed is given, Python usually uses the current system time.

```python
from random import *

seed(30)
```

## Random Float

```python
from random import *

lst = []

for i in range(10):
    x = random()
    lst.append(x)

print(lst)
```

`random()` gives a float from `0.0` up to but not including `1.0`.

To generate a float from `0` to `5` rounded to 2 decimal places:

```python
x = round(random() * 5, 2)
```

## Random Integer

```python
from random import *

x = randint(a, b)
```

`randint(a, b)` includes both `a` and `b`.

```python
lst = []

for i in range(10):
    x = randint(1, 6)
    lst.append(x)
```

## Random Selection From a List

```python
from random import *

lst = ["Adam", "Bob", "Charles", "Daniel"]

single = choice(lst)
pair = sample(lst, 2)

print(single)
print(pair)
```

| Function | Meaning |
| -------- | ------- |
| `choice(lst)` | chooses one item |
| `sample(lst, k)` | chooses `k` unique items |
| `choices(lst, k=k)` | chooses `k` items and may repeat values |

## Normal Distribution

```python
from random import *

lst = []

for i in range(1000):
    x = normalvariate(50, 7)
    lst.append(x)
```

`normalvariate(mean, standard_deviation)` generates numbers using a normal distribution.

## Mean and Standard Deviation

```python
from statistics import mean, stdev

print(mean(lst))
print(stdev(lst))
```

## Related

- [[Lists]]
- [[Iteration]]
- [[basic python]]
