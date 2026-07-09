> [!summary] Quick View
> Data representation = how numbers and characters are stored/transmitted as bits.

## Bits and Bytes

- Bit: `0` or `1`
- Byte: usually 8 bits
- `n` bits can represent `2 ** n` values
- More bits means more possible unique values.
- Fixed-length storage matters because computers must know how many bits belong to each value.

| Bits | Values |
| ---- | ------ |
| 8 | 256 |
| 16 | 65,536 |
| 32 | 4,294,967,296 |

> [!note]
> If a system uses 8-bit bytes, each byte can store one of `256` possible patterns, from `00000000` to `11111111`.

## Number Bases

Base `n` to denary:

```text
1011 base 2 = 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 11
```

Denary to base `n`:

- repeatedly divide by `n`
- collect remainders
- read remainders from last to first

## Common Bases

| Base | Name | Digits used | Example |
| ---- | ---- | ----------- | ------- |
| 2 | binary | `0`, `1` | `1011` |
| 8 | octal | `0` to `7` | `17` |
| 10 | denary / decimal | `0` to `9` | `255` |
| 16 | hexadecimal | `0` to `9`, `A` to `F` | `FF` |

Place values work the same way in every base:

```text
digits * base^position
```

Example:

```text
1011 base 2
= 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0
= 8 + 0 + 2 + 1
= 11
```

Another example:

```text
1000 base 3
= 1*3^3 + 0*3^2 + 0*3^1 + 0*3^0
= 27
```

## Denary to Another Base Trace

To convert denary `246` to binary:

| Step | Number | Remainder |
| ---- | ------ | --------- |
| 246 / 2 | 123 | 0 |
| 123 / 2 | 61 | 1 |
| 61 / 2 | 30 | 1 |
| 30 / 2 | 15 | 0 |
| 15 / 2 | 7 | 1 |
| 7 / 2 | 3 | 1 |
| 3 / 2 | 1 | 1 |
| 1 / 2 | 0 | 1 |

Read remainders from bottom to top:

```text
246 base 10 = 11110110 base 2
```

> [!important]
> The first remainder collected is the rightmost digit of the answer.

## Coding Base Conversions

For coding questions, do not use built-in conversion helpers such as `bin()`, `oct()`, `hex()`, or `int(value, base)`.
Using `int()` to turn a denary string into a number is allowed.

The two main coding patterns are:

- base to denary: multiply each digit by its place value
- denary to base: repeatedly divide and collect remainders

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

## Coding Pitfalls

- Handle denary `0`; repeated division otherwise returns an empty string.
- Convert digit characters with `int(...)` before arithmetic.
- For hexadecimal, use a lookup list because `A` to `F` are not normal denary digits.
- Do not reverse the final result after already prepending each remainder.
- Avoid naming variables `sum`, because it shadows Python's built-in `sum()`.

## Python Helpers

These helpers are allowed for character codes:

```python
ord("A")  # 65
chr(65)   # "A"
```

These are useful for checking understanding, but avoid them if the question asks you to code the conversion manually:

```python
bin(10)      # "0b1010"
oct(10)      # "0o12"
hex(255)     # "0xff"
int("1010", 2)  # 10
```

## ASCII

- American Standard Code for Information Interchange
- 7-bit character set
- `2 ** 7 = 128` characters
- standardised in the 1960s so different computers could represent characters consistently
- pronounced like "ask-key"
- enough for standard keyboard characters, but not enough for all languages
- contains 95 printable characters and 33 non-printable control codes

```python
ord("4")  # 52
chr(65)   # "A"
```

ASCII examples:

| Character | Denary | Hex | Binary |
| --------- | ------ | --- | ------ |
| `"A"` | `65` | `41` | `1000001` |
| `"4"` | `52` | `34` | `0110100` |
| `"$"` | `36` | `24` | `0100100` |

When 8-bit bytes became standard:

- ASCII still only needed the first 128 values.
- The remaining 128 values in one byte were not enough to represent all other languages.
- This limitation led to wider character sets such as Unicode.

## Unicode

- Represents characters from many languages.
- Python strings support Unicode.
- Unicode escape form looks like `\u062d`.
- originally designed around 16 bits per character
- later expanded beyond 16 bits so it could include more languages and historic scripts

Unicode examples:

| Language | Unicode escape | Character / word |
| -------- | -------------- | ---------------- |
| Arabic | `\u062d\u0628` | حب |
| Chinese | `\u7231` | 爱 |
| Greek | `\u03b1\u03b3\u03ac\u03c0\u03b7` | αγάπη |
| Korean | `\uc0ac\ub791` | 사랑 |
| Russian | `\u043b\u044e\u0431\u043b\u044e` | люблю |

Python example:

```python
"\uc0ac\ub791"
# "사랑"
```

The Korean word `사랑` uses two Unicode code units:

```text
\uc0ac \ub791
```

Each code unit can be viewed as hexadecimal digits:

```text
c0ac base 16
b791 base 16
```

## UTF-8

UTF-8 is variable length. It is used for transmitting or storing Unicode characters efficiently.

- ASCII characters use 1 byte.
- Other characters may use 2, 3, or 4 bytes.
- Continuation bytes start with `10`.
- The first byte tells how many bytes belong to the character.

| Leading bits | Bytes used |
| ------------ | ---------- |
| `0xxxxxxx` | 1 |
| `110xxxxx` | 2 |
| `1110xxxx` | 3 |
| `11110xxx` | 4 |

UTF-8 byte structure:

| Bytes | Pattern |
| ----- | ------- |
| 1 | `0xxxxxxx` |
| 2 | `110xxxxx 10xxxxxx` |
| 3 | `1110xxxx 10xxxxxx 10xxxxxx` |
| 4 | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

Examples:

| Character | Unicode hex | UTF-8 bytes |
| --------- | ----------- | ----------- |
| `$` | `24` | `00100100` |
| `£` | `A3` | `11000010 10100011` |
| `€` | `20AC` | `11100010 10000010 10101100` |

## UTF-8 Encoding Examples

Dollar sign `$`:

```text
Unicode hex: 24
Binary:      0100100
UTF-8:       00100100
```

It uses one byte because it fits the ASCII range.

Pound sign `£`:

```text
Unicode hex: A3
Binary:      10100011
Pad to 11 bits: 00010100011
UTF-8 pattern:  110xxxxx 10xxxxxx
UTF-8 bytes:    11000010 10100011
```

Euro sign `€`:

```text
Unicode hex: 20AC
Binary:      10000010101100
Pad to 16 bits: 0010000010101100
UTF-8 pattern:  1110xxxx 10xxxxxx 10xxxxxx
UTF-8 bytes:    11100010 10000010 10101100
```

## Decoding UTF-8 Byte Streams

Given this transmitted bit stream:

```text
001001001100001010100011111000101000001010101100
```

Group into bytes:

```text
00100100 11000010 10100011 11100010 10000010 10101100
```

Decode using leading bits:

| Byte(s) | Leading pattern | Character |
| ------- | --------------- | --------- |
| `00100100` | `0xxxxxxx` | `$` |
| `11000010 10100011` | `110xxxxx 10xxxxxx` | `£` |
| `11100010 10000010 10101100` | `1110xxxx 10xxxxxx 10xxxxxx` | `€` |

> [!note]
> A byte starting with `10` is a continuation byte, not the start of a new character.

## ASCII vs Unicode vs UTF-8

| Term | What it is |
| ---- | ---------- |
| ASCII | character set mapping 128 characters to numbers |
| Unicode | much larger character set assigning code points to characters |
| UTF-8 | encoding scheme for storing/transmitting Unicode as bytes |

## Exam Checklist

- Can calculate `2 ** n` possible values for `n` bits.
- Can convert base `n` to denary using place values.
- Can convert denary to base `n` using repeated division.
- Can explain why ASCII is limited.
- Can explain why Unicode is needed.
- Can identify UTF-8 1-byte, 2-byte, 3-byte, and 4-byte patterns.
- Can group a bit stream into bytes and decode characters using leading bits.
- Can write manual conversion functions without `bin()`, `oct()`, `hex()`, or `int(value, base)`.

## Related

- [[basic python]]
