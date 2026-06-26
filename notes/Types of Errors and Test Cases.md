> [!summary] Quick View
> Debugging finds bugs. Test cases check expected behaviour across meaningful input categories.

## Common Error Types

| Type | Meaning |
| ---- | ------- |
| Missing `return` | function produces `None` unintentionally |
| Incompatible types | operation between incompatible types |
| Wrong argument count | call does not match function signature |
| Syntax error | invalid Python grammar |
| Arithmetic error | e.g. division by zero |
| Undeclared variable | name used before assignment |
| Infinite loop/recursion | stop condition never reached |
| Floating point imprecision | binary float rounding issue |
| Logic error | code runs but answer is wrong |

## Debugging Approach

- Read the error message.
- Check variable values.
- Try smaller or different inputs.
- Add `print` statements to trace execution.
- Narrow the bug systematically.

## Test Case Categories

| Category | Purpose |
| -------- | ------- |
| Normal | typical valid input |
| Boundary / extreme | valid edge of accepted range |
| Abnormal | invalid input that should be rejected |
| Volume | large data to test efficiency / response time |

## Example

For percentage calculation:

- normal: `20/80 -> 25%`
- boundary: `0/80 -> 0%`, `60/60 -> 100%`
- abnormal: negative score or score greater than total should return error

## Related

- [[Conditionals]]
- [[Data validation and verification]]
