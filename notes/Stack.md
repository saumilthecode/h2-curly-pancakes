> [!summary] Quick View
> Stack = LIFO: Last In, First Out. Add/remove only from the top.

## Stack Trace

<details>
<summary>Push and pop example</summary>
<table>
  <thead>
    <tr><th>Step</th><th>Operation</th><th>Stack after step</th><th>Return</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td><td><code>start</code></td><td><code>[]</code></td><td>-</td></tr>
    <tr><td>2</td><td><code>push("A")</code></td><td><code>["A"]</code></td><td>-</td></tr>
    <tr><td>3</td><td><code>push("B")</code></td><td><code>["A", "B"]</code></td><td>-</td></tr>
    <tr><td>4</td><td><code>peek()</code></td><td><code>["A", "B"]</code></td><td><code>"B"</code></td></tr>
    <tr><td>5</td><td><code>pop()</code></td><td><code>["A"]</code></td><td><code>"B"</code></td></tr>
  </tbody>
</table>
</details>

## Core Operations

| Operation | Meaning | Python list |
| --------- | ------- | ----------- |
| `push(s, x)` | add to top | `s.append(x)` |
| `pop(s)` | remove top | `s.pop()` |
| `peek(s)` | look at top | `s[-1]` |
| `is_empty(s)` | check empty | `s == []` |

> [!important]
> Top of stack = end of Python list.

## Minimal Template

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

Trace:

```text
[] -> push A -> [A]
[A] -> push B -> [A, B]
[A, B] -> pop -> [A] and returns B
```

## Pattern: Reverse

Push everything in, then pop everything out.

```text
input: a b c d
stack after pushes: [a, b, c, d]
pop order: d c b a
```

## Pattern: Denary to Binary

Remainders appear backwards, so stack reverses them.

```python
while n > 0:
    push(s, n % 2)
    n = n // 2

while s != []:
    bits += str(pop(s))
```

## Pattern: Balanced Brackets

Rule:

- opening bracket -> push
- closing bracket -> pop and compare
- valid only if stack is empty at the end

```python
pairs = {")": "(", "]": "[", "}": "{"}
```

## Pattern: Postfix

For `3 4 * 5 +`:

```text
push 3
push 4
* -> pop 4, pop 3, push 12
push 5
+ -> pop 5, pop 12, push 17
answer = 17
```

> [!warning]
> For `-` and `/`, order matters. `A B -` means `A - B`.

## Common Mistakes

- Stack uses `pop()`, not `pop(0)`.
- `peek()` does not remove.
- `pop()` on empty stack should return `None`.
- If stack reverses something, do not reverse it again.

## Related

- [[Data Abstraction]]
- [[Queue]]
- [[C2 - Data representation]]
