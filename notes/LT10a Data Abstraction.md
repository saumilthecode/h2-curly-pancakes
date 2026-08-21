> [!summary] Quick View
> Data abstraction hides **how data is stored** and exposes only the operations needed to use it.

## Two Kinds of Abstraction

| | Hides | You only need to know |
| --- | ----- | --------------------- |
| Functional abstraction | how a function works | what it does |
| Data abstraction | how data is represented | what data you are dealing with |

## Abstract Data Type

An **ADT** defines:

- the data being represented
- the operations allowed on that data

It does **not** define how the data is stored, or how each operation is implemented.

## ADT Function Types

| Type | Purpose | Example |
| ---- | ------- | ------- |
| Constructor | creates a new ADT value | `make_rat(n, d)` |
| Accessor / Getter | retrieves data | `get_numer(rat)` |
| Modifier / Setter | changes data | `set_class(student, c)` |
| Utility | does something useful with it | `add(rat1, rat2)` |
| Predicate | returns `True` / `False` | `is_whole(rat)` |

## Why It Matters

The same ADT can be stored completely differently, and code using it never changes.

```python
# stored as a list
def make_record(name, nric, cls, addr):
    return [name, nric, cls, addr]

def get_name(student):
    return student[0]


# stored as a dictionary — same names, same calls
def make_record(name, nric, cls, addr):
    return {"name": name, "nric": nric, "class": cls, "address": addr}

def get_name(student):
    return student["name"]
```

Code that calls `get_name(student)` works with both. Swapping the internal representation breaks nothing.

> [!important]
> An ADT can also **withhold** access. A student record may provide no accessor for the NRIC, so nothing outside the ADT can read it.

## Common ADTs

| ADT | Idea | Order | Main operations |
| --- | ---- | ----- | --------------- |
| [[LT10b Stack\|Stack]] | add/remove at the top | LIFO | `push`, `pop`, `peek` |
| [[LT10c Queue\|Queue]] | add at tail, remove at head | FIFO | `enqueue`, `dequeue`, `front` |
| [[LT10d Hashing\|Hashing]] | map data to an index | direct lookup | `hash`, `search` |

## Worked Example: Rational Number

Data: an integer numerator and a non-zero integer denominator.

```python
def make_rat(numer, denom):        # constructor
    return (numer, denom)

def get_numer(rat):                # accessors
    return rat[0]

def get_denom(rat):
    return rat[1]

def add(rat1, rat2):               # utility
    numer = get_numer(rat1) * get_denom(rat2) + get_numer(rat2) * get_denom(rat1)
    denom = get_denom(rat1) * get_denom(rat2)
    return make_rat(numer, denom)

def is_equal(rat1, rat2):          # predicates
    return get_numer(rat1) * get_denom(rat2) == get_numer(rat2) * get_denom(rat1)

def is_whole(rat):
    return get_numer(rat) % get_denom(rat) == 0
```

> [!note]
> The utilities call `get_numer` / `get_denom` rather than `rat[0]` / `rat[1]`, so changing the representation means editing only the constructor and accessors.

Arithmetic:

```text
n1/d1 + n2/d2 = (n1*d2 + n2*d1) / (d1*d2)
n1/d1 - n2/d2 = (n1*d2 - n2*d1) / (d1*d2)
n1/d1 * n2/d2 = (n1*n2) / (d1*d2)
n1/d1 / n2/d2 = (n1*d2) / (d1*n2)

equal   when n1*d2 == n2*d1
whole   when n1 % d1 == 0
```

Simplifying inside the constructor:

```python
from math import gcd

def make_rat(n, d):
    divisor = gcd(n, d)
    return (n // divisor, d // divisor)
```

> [!example]- Position ADT
> Represents the coordinates of a point.
>
> ```python
> make_point(x, y)               # constructor
> get_x(point)  get_y(point)     # accessors
> midpoint(p1, p2)               # utilities
> gradient(p1, p2)
> distance(p1, p2)
> equation(p1, p2)               # returns "y = mx + c"
> display(point)                 # returns "(x, y)"
> ```
>
> ```text
> midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
> gradient = (y2 - y1) / (x2 - x1)
> distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
> ```
>
> ```python
> def make_point(x, y):
>     return (x, y)
>
> def get_x(point):
>     return point[0]
>
> def distance(p1, p2):
>     rise = get_y(p2) - get_y(p1)
>     run = get_x(p2) - get_x(p1)
>     return (rise ** 2 + run ** 2) ** 0.5
> ```

> [!example]- Group ADT — working over a collection
> ```python
> def make_student(name, gender, score):
>     return (name, gender, score)
>
> def get_name(s):    return s[0]
> def get_gender(s):  return s[1]
> def get_score(s):   return s[2]
> def size(group):    return len(group)
>
> def average_score(group):
>     total = 0
>     for student in group:
>         total += get_score(student)
>     return round(total / size(group), 2)
>
> def names_by_gender(group, gender):
>     result = ()
>     for student in group:
>         if get_gender(student) == gender:
>             result += (get_name(student),)
>     return result
> ```

## Common Mistakes

- Reaching into the representation directly (`student[0]`) instead of calling the accessor.
- Writing utilities that assume a tuple, so the ADT can no longer be swapped to a dictionary.
- Forgetting the constructor must return the value — not print it.

## Related

- [[LT3a Functional Abstraction]]
- [[LT3b Good Abstraction]]
- [[LT6 Tuple]]
- [[LT10b Stack]]
- [[LT10c Queue]]
- [[LT10d Hashing]]
- [[BTB2 File Handling]]
