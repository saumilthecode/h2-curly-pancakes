> [!summary] Quick View
> `if` / `elif` / `else` choose between paths. **At most one block runs.**

## Structure

```python
if condition:
    statement(s)
elif other_condition:
    statement(s)
else:
    statement(s)
```

- `elif` and `else` are both optional.
- `else` has no condition — it catches everything left over.

## How It Runs

> [!important] The one rule
> Conditions are tested **top to bottom**. The first one that is `True` runs its block, and every remaining condition is skipped. If none are `True`, `else` runs.

```text
        ┌─ if cond1  ── True ──▶ block 1 ──┐
input ──┼─ elif cond2 ─ True ──▶ block 2 ──┼──▶ continue after
        ├─ elif cond3 ─ True ──▶ block 3 ──┤
        └─ else ───────────────▶ block 4 ──┘
```

## Order Matters

Once a gate is taken, the rest are never tested. Overlapping conditions must go **narrowest first**.

```python
# WRONG — a mark of 95 prints "Pass", never "Distinction"
if mark >= 50:
    print("Pass")
elif mark >= 75:
    print("Distinction")

# RIGHT — the stricter test goes first
if mark >= 75:
    print("Distinction")
elif mark >= 50:
    print("Pass")
```

## Indentation

Indentation defines the block — it is not decoration. Use 4 spaces, consistently.

```python
if a > 0:
    print("positive")   # inside the if
print("done")           # always runs
```

## `pass`

`pass` does nothing. Use it as a placeholder when a block is required but you have no code yet.

> [!note]
> `break` and `continue` control **loops**, not conditionals — see [[LT5 Iteration|Iteration]].

## Common Mistakes

- Missing the colon after the condition.
- Putting the broader condition before the narrower one.
- **Check every branch is reachable.** One mistyped bound silently kills every branch below it:

```python
if 0 < volume <= 140000:        # typo — should be 14000
elif 14000 < volume <= 30000:   # dead: already caught above
elif 30000 < volume <= 70000:   # dead
```
- Using `=` instead of `==` in the condition.
- Expecting more than one branch to run — only the first match does.

> [!tip]
> Flowcharts are **not in the 9569 syllabus**, so don't spend revision time drawing them.

## Related

- [[LT1 basic python|basic python]]
- [[LT5 Iteration|Iteration]]
- [[LT3 Functions (functional abstraction)|Functions (functional abstraction)]]
