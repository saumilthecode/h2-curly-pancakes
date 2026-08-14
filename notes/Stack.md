> [!summary] Quick View
> Stack = **LIFO**, Last In First Out. Everything happens at the top.

```text
      push ▼    ▲ pop         both act on the TOP
         ┌───────┐
  top →  │   C   │  ← s[-1]   last in, first out
         ├───────┤
         │   B   │
         ├───────┤
bottom → │   A   │  ← s[0]    first in, last out
         └───────┘
```

## Core Operations

| Operation | Meaning | Python list |
| --------- | ------- | ----------- |
| `push(s, x)` | add to top | `s.append(x)` |
| `pop(s)` | remove and return top | `s.pop()` |
| `peek(s)` | look at top, don't remove | `s[-1]` |
| `is_empty(s)` | is it empty? | `s == []` |

> [!important]
> Top of stack = **end** of the Python list. You cannot pop an empty stack.

## Template

```python
def push(s, item):
    s.append(item)

def pop(s):
    if s == []:
        return None
    return s.pop()

def peek(s):
    if s == []:
        return None
    return s[-1]
```

> [!example]- Trace: push and pop
> | Step | Operation | Stack after | Returns |
> | ---- | --------- | ----------- | ------- |
> | 1 | `make_empty_stack()` | `[]` | — |
> | 2 | `pop(s)` | `[]` | `None` — nothing to pop |
> | 3 | `push(s, 7)` | `[7]` | — |
> | 4 | `push(s, 5)` | `[7, 5]` | — |
> | 5 | `push(s, 3)` | `[7, 5, 3]` | — |
> | 6 | `pop(s)` | `[7, 5]` | `3` |
> | 7 | `peek(s)` | `[7, 5]` | `5` |
> | 8 | `is_empty(s)` | `[7, 5]` | `False` |

## Application: Reverse a Sequence

Push everything in, then pop everything out.

```text
input:  a b c d
stack:  [a, b, c, d]
pop:    d c b a
```

## Application: Denary to Binary

Repeated division gives the remainders backwards, so a stack flips them.

```python
while n > 0:
    push(s, n % 2)
    n = n // 2

bits = ""
while s != []:
    bits += str(pop(s))
```

## Application: Balanced Brackets

- Opening bracket → **push** it.
- Closing bracket → **pop** and check it matches.
- Valid only if the stack is **empty at the end**.

```python
pairs = {")": "(", "]": "[", "}": "{"}
```

```text
( [ ] ( { ( ) } ) )   balanced
( ( { } [ ) ] )       not balanced
```

Counting brackets is not enough — order matters, which is why you need a stack.

## Application: Postfix Notation

| Notation | Operator sits | `A + B` written as |
| -------- | ------------- | ------------------ |
| Infix | between operands | `A + B` |
| Prefix | before operands | `+ A B` |
| Postfix | after operands | `A B +` |

Evaluate postfix left to right: push operands, and on an operator pop two, combine, push the result.

```text
3 4 * 5 +          (infix: 3 * 4 + 5)

push 3                    [3]
push 4                    [3, 4]
*  -> pop 4, pop 3, push 12   [12]
push 5                    [12, 5]
+  -> pop 5, pop 12, push 17  [17]

answer = 17
```

> [!warning]
> For `-` and `/` the order matters. `A B -` means `A - B` — the **first** value popped is the right-hand operand.

## Common Mistakes

- Using `pop(0)` — that's a [[Queue]], not a stack.
- Writing `return s.append(x)` in `push`. `.append()` returns `None`, so the function hands back `None`. A `push` should not return anything.
- Reading the underlying list directly (`for item in s:`) instead of calling `pop()`. In an *application of stack* question that throws away the marks for using the ADT — and iterating a list does **not** reverse it the way popping does.
- Treating `peek()` as if it removes the item.
- Popping an empty stack instead of returning `None`.
- Reversing an already-reversed result a second time.

## Related

- [[Data Abstraction]]
- [[Queue]]
- [[Recursion]]
- [[C2 - Data representation]]
