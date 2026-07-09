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

## Coding Base Conversions

For coding questions, do not use built-in conversion helpers such as `bin()`, `oct()`, `hex()`, or `int(value, base)`.
Using `int()` to turn a denary string into a number is allowed.

Binary to denary:

```python
def binary_to_denary(string):
    result = 0

    for i in range(len(string)):
        power = (len(string) - 1) - i
        result += int(string[i]) * 2 ** power

    return str(result)
```

Denary to binary:

```python
def denary_to_binary(string):
    num = int(string)
    if num == 0:
        return "0"

    result = ""

    while num != 0:
        remainder = num % 2
        num = num // 2
        result = str(remainder) + result

    return result
```

Base `n` to denary:

```python
def base_n_to_denary(string, n):
    result = 0

    for i in range(len(string)):
        power = (len(string) - 1) - i
        result += int(string[i]) * n ** power

    return str(result)
```

Denary to base `n`:

```python
def denary_to_base_n(string, n):
    num = int(string)
    if num == 0:
        return "0"

    result = ""

    while num != 0:
        remainder = num % n
        num = num // n
        result = str(remainder) + result

    return result
```

> [!note]
> These simple base `n` functions work cleanly when every digit can be represented as `0` to `9`.
> Use a lookup list for hexadecimal because values `10` to `15` are written as `A` to `F`.

## Hexadecimal

Base 16 uses `0`-`9` and `A`-`F`.

| Hex | Denary |
| --- | ------ |
| A   | 10     |
| B   | 11     |
| C   | 12     |
| D   | 13     |
| E   | 14     |
| F   | 15     |

Hexadecimal to denary:

```python
def hex_to_denary(string):
    hexa = ["0", "1", "2", "3", "4", "5", "6", "7",
            "8", "9", "A", "B", "C", "D", "E", "F"]
    result = 0

    for i in range(len(string)):
        power = (len(string) - 1) - i
        result += hexa.index(string[i]) * 16 ** power

    return str(result)
```

Denary to hexadecimal:

```python
def denary_to_hex(string):
    hexa = ["0", "1", "2", "3", "4", "5", "6", "7",
            "8", "9", "A", "B", "C", "D", "E", "F"]
    num = int(string)
    if num == 0:
        return "0"

    result = ""

    while num != 0:
        remainder = num % 16
        result = hexa[remainder] + result
        num = num // 16

    return result
```

Test cases:

```python
print(binary_to_denary("11111111") == "255")
print(denary_to_binary("246") == "11110110")
print(base_n_to_denary("1000", 3) == "27")
print(denary_to_base_n("521", 8) == "1011")
print(hex_to_denary("CAFE") == "51966")
print(denary_to_hex("51966") == "CAFE")
```

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
