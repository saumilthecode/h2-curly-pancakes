> [!summary] Quick View
> Data abstraction hides how data is stored and exposes only the operations needed to use it.

## Abstraction

Functional abstraction hides how a function works.

```python
result = function(input)
```

- You only need to know what the function does.
- You do not need to know the implementation inside the function.

Data abstraction hides how data is represented.

- You only need to know what data you are dealing with.
- You interact with the data through provided functions.
- The internal storage can change without changing the code that uses the ADT.

## Abstract Data Type

An Abstract Data Type (ADT) defines:

- the data being represented
- the operations allowed on that data

It does not define:

- exactly how the data is stored
- exactly how each operation is implemented

## ADT Function Types

| Type | Purpose |
| ---- | ------- |
| Constructor | creates a new ADT value |
| Accessor / Getter | retrieves data from the ADT |
| Modifier / Setter | changes data in the ADT |
| Utility | performs useful operations using the ADT |
| Predicate | returns `True` or `False` about the ADT |

## Common ADTs

| ADT | Main idea | Order rule | Main operations |
| --- | --------- | ---------- | --------------- |
| [[Stack]] | add/remove from the top | LIFO | `push`, `pop`, `peek` |
| [[Queue]] | add at tail, remove from head | FIFO | `enqueue`, `dequeue`, `front` |

## Student Record ADT

Data stored:

- name
- NRIC
- class
- address

Constructor:

```python
make_record(name, id, class_name, address)
```

Accessors:

```python
get_name(student)
get_class(student)
get_address(student)
```

Modifiers:

```python
set_class(student, new_class)
set_address(student, new_address)
```

The ADT may choose not to provide access to sensitive data such as NRIC.

Same ADT, different internal representation:

```python
def make_record(name, nric, class_name, address):
    return [name, nric, class_name, address]

def get_name(student):
    return student[0]
```

```python
def make_record(name, nric, class_name, address):
    student = {}
    student["name"] = name
    student["nric"] = nric
    student["class"] = class_name
    student["address"] = address
    return student

def get_name(student):
    return student["name"]
```

Code using `get_name(student)` does not need to know whether the record is stored as a list or dictionary.

## Position ADT

A position ADT represents the coordinates of a point.

Constructor:

```python
make_point(xcoord, ycoord)
```

Accessors:

```python
get_x(point)
get_y(point)
```

Utility functions:

```python
midpoint(point1, point2)
gradient(point1, point2)
distance(point1, point2)
equation(point1, point2)
display(point)
```

Common formulas:

```text
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
gradient = (y2 - y1) / (x2 - x1)
distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
y = mx + c
```

Example implementation:

```python
def make_point(xcoord, ycoord):
    return (xcoord, ycoord)

def get_x(point):
    return point[0]

def get_y(point):
    return point[1]

def midpoint(point1, point2):
    return ((get_x(point1) + get_x(point2)) / 2,
            (get_y(point1) + get_y(point2)) / 2)

def gradient(point1, point2):
    rise = get_y(point2) - get_y(point1)
    run = get_x(point2) - get_x(point1)
    return rise / run

def distance(point1, point2):
    rise = get_y(point2) - get_y(point1)
    run = get_x(point2) - get_x(point1)
    return (rise ** 2 + run ** 2) ** 0.5
```

## Rational Number ADT

A rational number ADT represents a fraction with:

- integer numerator
- non-zero integer denominator

Constructor:

```python
make_rat(numer, denom)
```

Accessors:

```python
get_numer(rat)
get_denom(rat)
```

Utility functions:

```python
add(rat1, rat2)
sub(rat1, rat2)
mul(rat1, rat2)
div(rat1, rat2)
print_rat(rat)
```

Arithmetic:

```text
n1/d1 + n2/d2 = (n1*d2 + n2*d1) / (d1*d2)
n1/d1 - n2/d2 = (n1*d2 - n2*d1) / (d1*d2)
n1/d1 * n2/d2 = (n1*n2) / (d1*d2)
n1/d1 / n2/d2 = (n1*d2) / (d1*n2)
```

Predicates:

```python
is_equal(rat1, rat2)
is_whole(rat)
```

```text
n1/d1 == n2/d2 when n1*d2 == n2*d1
n1/d1 is whole when n1 % d1 == 0
```

Example implementation:

```python
def make_rat(numer, denom):
    return (numer, denom)

def get_numer(rat):
    return rat[0]

def get_denom(rat):
    return rat[1]

def add(rat1, rat2):
    numer = get_numer(rat1) * get_denom(rat2) + get_numer(rat2) * get_denom(rat1)
    denom = get_denom(rat1) * get_denom(rat2)
    return make_rat(numer, denom)

def is_equal(rat1, rat2):
    return get_numer(rat1) * get_denom(rat2) == get_numer(rat2) * get_denom(rat1)

def is_whole(rat):
    return get_numer(rat) % get_denom(rat) == 0
```

To automatically simplify fractions:

```python
from math import gcd

def make_rat(n, d):
    divisor = gcd(n, d)
    return (n // divisor, d // divisor)
```

## Group ADT Practice

```python
def make_student(name, gender, score):
    return (name, gender, score)

def get_name(student):
    return student[0]

def get_gender(student):
    return student[1]

def get_score(student):
    return student[2]

def size(group):
    return len(group)
```

Average score:

```python
def average_score(group):
    total_score = 0

    for student in group:
        total_score += get_score(student)

    return round(total_score / size(group), 2)
```

Filter names by gender:

```python
def create_list(group, gender):
    result = ()

    for student in group:
        if get_gender(student) == gender:
            result += (get_name(student),)

    return result
```

## Reading Tabulated Data

CSV and TXT files are common ways to store tabulated data.

```python
file = open("data.csv")
lines = file.readlines()

for line in lines[1:]:
    line = line.strip()
    line = line.split(",")
    name, gender, score = line
    print(name, score)

file.close()
```

- `lines[1:]` skips the header.
- `.strip()` removes the newline.
- `.split(",")` separates comma-separated fields.

## Related

- [[Tuple]]
- [[Stack]]
- [[Queue]]
- [[Functions (functional abstraction)]]
- [[File Handling]]
