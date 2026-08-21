> [!summary] Quick View
> Solve a problem by solving a **smaller version of the same problem**.

## Three Essential Features

1. A **base case** that returns an answer without recursing.
2. The function **calls itself**.
3. Each call moves towards the base case (a **smaller** problem).

Miss any one and it recurses forever until Python raises a maximum recursion depth error.

```python
def factorial(n):
    if n == 1:          # 1. base case
        return 1
    else:
        return n * factorial(n - 1)   # 2. calls itself  3. smaller
```

> [!tip]
> Applying this to actual problems — the shrinking patterns, choosing base cases, worked examples — is in [[LT9b Recursion (Application)|LT9b]].

## Writing One: Wishful Thinking

Don't try to trace the whole thing in your head. Assume the smaller call already works, and only write the step that turns its answer into yours.

1. What is the **smallest** input, and what's its obvious answer? → base case.
2. Assume `f(n-1)` is correct. What single operation turns it into `f(n)`?

Two ways to shrink the problem:

| Reduction | Size `n` becomes | Example |
| --------- | ---------------- | ------- |
| By one | `n - 1` | `factorial`, list traversal |
| Divide and conquer | `n / 2` | [[LT11a Search\|Search]] — binary search |

## Recursion Tree

Trace by expanding downwards, then returning back up.

```text
factorial(5)
= 5 * factorial(4)
      = 4 * factorial(3)
            = 3 * factorial(2)
                  = 2 * factorial(1)
                        = 1              ◀ base case
                  = 2 * 1   = 2
            = 3 * 2   = 6
      = 4 * 6   = 24
= 5 * 24  = 120
```

Going down defers the multiplications; coming back up performs them.

> [!important]
> Paper 1 asks you to **draw a recursion tree** to trace a call. Show the calls going down and the returned values coming back up.

## How the Stack Is Used

> [!important] Asked in 2020, 2021 and 2024 — worth 3–4 marks each time.

Each call is **pushed onto the call stack** before the previous one finishes.

1. Every call pushes a **stack frame** holding its parameters, local variables and return address.
2. The frames build up because each call is **suspended**, waiting on the call below it.
3. When the **base case** returns, no new frame is pushed.
4. Frames are then **popped** in reverse order (LIFO), each using the returned value to finish its own calculation.

```text
                  stack grows ▼                     stack unwinds ▲
factorial(3)   │ f(3) waiting     │                │ f(3) = 3*2 = 6 │  ◀ answer
factorial(2)   │ f(3), f(2)       │                │ f(2) = 2*1 = 2 │
factorial(1)   │ f(3), f(2), f(1) │  base case ──▶ │ f(1) = 1       │
```

If the base case is never reached, frames keep being pushed until memory runs out — Python raises a **maximum recursion depth** error and the program stops.

## Recursion vs Iteration

**Similarities**

- Both repeat a set of instructions.
- Both need a stopping condition, or they run forever.
- Both can solve the same problems.

**Differences**

| | Recursion | Iteration |
| --- | --------- | --------- |
| Repeats by | the function calling itself | a loop construct |
| Stops when | base case is reached | loop condition becomes `False` |
| Memory | a new stack frame per call — can hit the recursion limit | one frame, constant |
| Speed | slower, call overhead | faster |
| Suits | self-similar problems (trees, nested structures) | simple counting and accumulation |

Papers ask you to convert **both ways**. The mapping is direct:

| Recursive | Iterative |
| --------- | --------- |
| base case | loop's stopping condition |
| the smaller call | the counter update |
| combining on the way back up | the accumulator variable |

```python
def factorial(n):                  # recursive
    if n == 1:
        return 1
    return n * factorial(n - 1)


def factorial(n):                  # iterative
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
```

## The Pattern

- Base case handles the **smallest** input.
- Recursive call takes a **smaller** input.
- Combine the current item with the recursive answer.

```python
def list_sum(arr):
    if len(arr) == 0:            # smallest input
        return 0
    return arr[0] + list_sum(arr[1:])   # current + rest
```

> [!example]- More worked patterns
> Reverse a string — take the last character, recurse on the rest:
>
> ```python
> def reverse_string(s):
>     if len(s) == 0:
>         return ""
>     return s[-1] + reverse_string(s[:-1])
> ```
>
> Palindrome — compare the ends, recurse on the middle:
>
> ```python
> def is_palindrome(s):
>     if len(s) <= 1:
>         return True
>     if s[0] != s[-1]:
>         return False
>     return is_palindrome(s[1:-1])
> ```
>
> Find maximum — compare the head against the best of the tail:
>
> ```python
> def find_max(arr):
>     if len(arr) == 1:
>         return arr[0]
>     rest_max = find_max(arr[1:])
>     if arr[0] > rest_max:
>         return arr[0]
>     return rest_max
> ```
>
> Count with an index — move the index instead of slicing:
>
> ```python
> def count_passes(students, index):
>     if index == len(students):
>         return 0
>     if students[index][1] >= 50:
>         return 1 + count_passes(students, index + 1)
>     return count_passes(students, index + 1)
> ```

## Mutual Recursion

Two functions can call each other. The base case still has to stop the chain.

```python
def ping(n):
    if n == 0:
        return n
    print("Ping!")
    pong(n - 1)

def pong(n):
    if n == 0:
        return n
    print("Pong!")
    ping(n - 1)
```

## Debugging

Put `print(n)` on the first line of the function. If the value is not moving towards the base case, that is the bug.

```python
factorial(-1)    # -1, -2, -3 ... goes past the base case
factorial(2.1)   # 2.1, 1.1, 0.1 ... never equals 1
```

## Common Mistakes

- Forgetting `return` on the recursive call, so the answer is lost.
- A base case the input can step **past** rather than land on.
- Recursing on the same size input, so it never shrinks.

## Related

- [[LT9b Recursion (Application)]]
- [[LT3a Functional Abstraction]]
- [[LT5 Iteration]]
- [[LT10b Stack]]
