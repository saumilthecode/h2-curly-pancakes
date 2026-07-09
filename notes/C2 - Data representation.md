> [!summary] Quick View
> 2027 examinable core: represent positive integers in binary, decimal, and hexadecimal; use Unicode examples; use ASCII codes in programs.

## Syllabus Anchor

Aligned to 2027 H2 Computing `9569` data representation outcomes:

- convert positive integers between decimal, binary, and hexadecimal
- state uses of binary and hexadecimal
- show Unicode examples for different languages
- use ASCII character codes in programs

This is a notes page, not the full syllabus.

## Bits and Values

- Bit: one binary digit, `0` or `1`
- Byte: 8 bits
- `n` bits can represent `2 ** n` different patterns

| Bits | Number of patterns |
| ---- | ------------------ |
| 4 | `16` |
| 8 | `256` |
| 16 | `65,536` |

> [!tip]
> More bits means more unique patterns. It does not automatically mean the values are signed unless the question says so.

## Number Bases

| Base | Name | Digits | Example |
| ---- | ---- | ------ | ------- |
| 2 | binary | `0`, `1` | `1011` |
| 10 | decimal / denary | `0` to `9` | `255` |
| 16 | hexadecimal | `0` to `9`, `A` to `F` | `FF` |

Hex digit values:

| Hex | Decimal |
| --- | ------- |
| `A` | `10` |
| `B` | `11` |
| `C` | `12` |
| `D` | `13` |
| `E` | `14` |
| `F` | `15` |

## Base to Decimal

Multiply each digit by its place value.

```text
1011 base 2
= 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0
= 8 + 0 + 2 + 1
= 11
```

```text
2F base 16
= 2*16^1 + 15*16^0
= 32 + 15
= 47
```

## Decimal to Another Base

Repeated division method:

1. Divide by the target base.
2. Record the remainder.
3. Continue with the quotient.
4. Read remainders from bottom to top.

Example: convert decimal `246` to binary.

| Division | Quotient | Remainder |
| -------- | -------- | --------- |
| `246 / 2` | `123` | `0` |
| `123 / 2` | `61` | `1` |
| `61 / 2` | `30` | `1` |
| `30 / 2` | `15` | `0` |
| `15 / 2` | `7` | `1` |
| `7 / 2` | `3` | `1` |
| `3 / 2` | `1` | `1` |
| `1 / 2` | `0` | `1` |

```text
246 base 10 = 11110110 base 2
```

Example: convert decimal `51966` to hexadecimal.

| Division | Quotient | Remainder | Hex digit |
| -------- | -------- | --------- | --------- |
| `51966 / 16` | `3247` | `14` | `E` |
| `3247 / 16` | `202` | `15` | `F` |
| `202 / 16` | `12` | `10` | `A` |
| `12 / 16` | `0` | `12` | `C` |

```text
51966 base 10 = CAFE base 16
```

## Binary and Hex Shortcut

One hex digit is exactly 4 bits.

| Binary | Hex |
| ------ | --- |
| `0000` | `0` |
| `0001` | `1` |
| `1010` | `A` |
| `1111` | `F` |

Binary to hex:

```text
11110110
= 1111 0110
= F6
```

Hex to binary:

```text
2F
= 0010 1111
```

Drop leading zeros only when they are not needed for a fixed-width representation.

## Uses

Binary is used because digital circuits naturally represent two stable states:

- off/on
- low/high voltage
- false/true

Hexadecimal is used because it is a shorter way to write binary:

- memory addresses
- machine code
- colour codes, for example `#FF0000`
- byte values, for example `0x7F`

## Coding Base Conversions

For manual conversion questions, avoid `bin()`, `hex()`, and `int(value, base)` unless the question explicitly allows them.

Binary to decimal:

```python
def binary_to_decimal(bits):
    total = 0

    for i in range(len(bits)):
        power = len(bits) - 1 - i
        total += int(bits[i]) * 2 ** power

    return total
```

Decimal to binary:

```python
def decimal_to_binary(num):
    if num == 0:
        return "0"

    bits = ""

    while num > 0:
        bits = str(num % 2) + bits
        num = num // 2

    return bits
```

Hexadecimal to decimal:

```python
def hex_to_decimal(hex_string):
    digits = "0123456789ABCDEF"
    total = 0

    hex_string = hex_string.upper()

    for i in range(len(hex_string)):
        power = len(hex_string) - 1 - i
        total += digits.index(hex_string[i]) * 16 ** power

    return total
```

Decimal to hexadecimal:

```python
def decimal_to_hex(num):
    digits = "0123456789ABCDEF"

    if num == 0:
        return "0"

    result = ""

    while num > 0:
        result = digits[num % 16] + result
        num = num // 16

    return result
```

Quick checks:

```python
print(binary_to_decimal("11110110"))  # 246
print(decimal_to_binary(246))         # 11110110
print(hex_to_decimal("CAFE"))         # 51966
print(decimal_to_hex(51966))          # CAFE
```

## ASCII

ASCII maps characters to integer codes.

- ASCII is a 7-bit character set.
- `2 ** 7 = 128` possible codes.
- It is enough for basic English letters, digits, punctuation, and control codes.
- It is not enough for characters from many other languages.

Common examples:

| Character | Decimal code | Hex |
| --------- | ------------ | --- |
| `"A"` | `65` | `41` |
| `"a"` | `97` | `61` |
| `"0"` | `48` | `30` |
| `"4"` | `52` | `34` |
| `"$"` | `36` | `24` |

Python:

```python
ord("A")  # 65
chr(65)   # "A"
```

Useful pattern:

```python
digit = "7"
value = ord(digit) - ord("0")
print(value)  # 7
```

## Unicode

Unicode gives code points to characters from many languages and symbol sets.

Why Unicode is needed:

- ASCII only has 128 codes.
- Different languages need far more characters.
- A shared standard avoids different systems using different numbers for the same character.

Examples:

| Language | Unicode escape | Character / word |
| -------- | -------------- | ---------------- |
| Arabic | `\u062d\u0628` | حب |
| Chinese | `\u7231` | 爱 |
| Greek | `\u03b1\u03b3\u03ac\u03c0\u03b7` | αγάπη |
| Korean | `\uc0ac\ub791` | 사랑 |
| Russian | `\u043b\u044e\u0431\u043b\u044e` | люблю |

Python strings support Unicode:

```python
print("\uc0ac\ub791")  # 사랑
```

## Common Mistakes

- Reading division remainders from top to bottom instead of bottom to top.
- Forgetting that hex `A` to `F` represent decimal `10` to `15`.
- Dropping leading zeros when the question asks for a fixed number of bits.
- Using `int(value, base)` in a question that asks you to implement the conversion manually.
- Confusing ASCII with Unicode. ASCII is small; Unicode covers many languages.

## Exam Checklist

- Can convert binary to decimal using place values.
- Can convert hexadecimal to decimal using place values.
- Can convert decimal to binary using repeated division.
- Can convert decimal to hexadecimal using repeated division.
- Can group binary into 4-bit chunks for hex conversion.
- Can explain why binary is used by computers.
- Can explain why hexadecimal is used as a compact form of binary.
- Can use `ord()` and `chr()` for ASCII character codes.
- Can explain why Unicode is needed and give examples from different languages.

## Optional Context

UTF-8 is a common way to store or transmit Unicode as bytes. It is useful background, but the 2027 H2 Computing data representation outcome names Unicode examples, not UTF-8 byte decoding.

## Related

- [[basic python]]
