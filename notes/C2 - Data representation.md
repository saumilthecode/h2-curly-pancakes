> [!summary] Quick View
> Data representation = how numbers and characters are stored/transmitted as bits.

## Bits and Bytes

- Bit: `0` or `1`
- Byte: usually 8 bits
- `n` bits can represent `2 ** n` values

| Bits | Values |
| ---- | ------ |
| 8 | 256 |
| 16 | 65,536 |
| 32 | 4,294,967,296 |

## Number Bases

Base `n` to denary:

```text
1011 base 2 = 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 11
```

Denary to base `n`:

- repeatedly divide by `n`
- collect remainders
- read remainders from last to first

## Hexadecimal

Base 16 uses `0`-`9` and `A`-`F`.

| Hex | Denary |
| --- | ------ |
| A | 10 |
| B | 11 |
| C | 12 |
| D | 13 |
| E | 14 |
| F | 15 |

## ASCII

- American Standard Code for Information Interchange
- 7-bit character set
- `2 ** 7 = 128` characters
- enough for standard keyboard characters, but not enough for all languages

```python
ord("4")  # 52
chr(65)   # "A"
```

## Unicode

- Represents characters from many languages.
- Python strings support Unicode.
- Unicode escape form looks like `\u062d`.

## UTF-8

UTF-8 is variable length.

| Leading bits | Bytes used |
| ------------ | ---------- |
| `0xxxxxxx` | 1 |
| `110xxxxx` | 2 |
| `1110xxxx` | 3 |
| `11110xxx` | 4 |

Examples:

| Character | Unicode hex | UTF-8 bytes |
| --------- | ----------- | ----------- |
| `$` | `24` | `00100100` |
| `£` | `A3` | `11000010 10100011` |
| `€` | `20AC` | `11100010 10000010 10101100` |

## Related

- [[basic python]]
