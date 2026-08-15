> [!summary] Quick View
> The same value can be written in denary, binary or hexadecimal. Only the **base** changes, never the value.

> [!important] Syllabus scope
> Conversions are examined for **positive integers** between **denary, binary and hexadecimal** only.

## Bits and Bytes

- **Bit** — one binary digit, `0` or `1`
- **Byte** — 8 bits
- `n` bits give `2 ** n` different patterns

| Bits | Patterns |
| ---- | -------- |
| 8 | `256` |
| 16 | `65,536` |
| 32 | `4,294,967,296` |

## The Three Bases

| Base | Name | Digits | Example |
| ---- | ---- | ------ | ------- |
| 2 | binary | `0`, `1` | `11110110` |
| 10 | denary / decimal | `0`–`9` | `246` |
| 16 | hexadecimal | `0`–`9`, `A`–`F` | `F6` |

Moving one place left multiplies the place value by the base.

```text
base 2:   ...  128   64   32   16    8    4    2    1
base 10:  ... 1000  100   10    1
base 16:  ... 4096  256   16    1
```

## One Value, Three Ways

```text
binary        1     1     1     1     0     1     1     0
place       2^7   2^6   2^5   2^4   2^3   2^2   2^1   2^0
value       128    64    32    16     8     4     2     1
            ───   ───   ───   ───   ───   ───   ───   ───
            128 +  64 +  32 +  16 +   0 +   4 +   2 +   0  = 246
```

| Written as | Meaning | Value |
| ---------- | ------- | ----- |
| denary `246` | `2*100 + 4*10 + 6*1` | 246 |
| binary `11110110` | `128 + 64 + 32 + 16 + 4 + 2` | 246 |
| hex `F6` | `15*16 + 6*1` | 246 |

## Reference Table

| Denary | Binary | Hex |
| ------ | ------ | --- |
| `0` | `0000` | `0` |
| `1` | `0001` | `1` |
| `2` | `0010` | `2` |
| `3` | `0011` | `3` |
| `4` | `0100` | `4` |
| `5` | `0101` | `5` |
| `6` | `0110` | `6` |
| `7` | `0111` | `7` |
| `8` | `1000` | `8` |
| `9` | `1001` | `9` |
| `10` | `1010` | `A` |
| `11` | `1011` | `B` |
| `12` | `1100` | `C` |
| `13` | `1101` | `D` |
| `14` | `1110` | `E` |
| `15` | `1111` | `F` |

## MSB and LSB

```text
     1 1 1 1 0 1 1 0
     ▲             ▲
    MSB           LSB
   (2^7)         (2^0)
```

**MSB** = most significant bit, the leftmost, largest place value.
**LSB** = least significant bit, the rightmost, worth `1`.

## Any Base → Denary

Multiply each digit by its place value and add.

```text
1011 base 2  = 1*8 + 0*4 + 1*2 + 1*1     = 11
  2F base 16 = 2*16 + 15*1               = 47
```

## Denary → Any Base

Divide repeatedly, keep the remainders, then **read them upwards**.

```text
246 / 2 = 123  r 0   ┐
123 / 2 =  61  r 1   │
 61 / 2 =  30  r 1   │
 30 / 2 =  15  r 0   │  read
 15 / 2 =   7  r 1   │  UPWARDS
  7 / 2 =   3  r 1   │
  3 / 2 =   1  r 1   │
  1 / 2 =   0  r 1   ┘

246 = 11110110 base 2
```

Same method for hex, converting remainders `10`–`15` to `A`–`F`:

```text
51966 / 16 = 3247  r 14  -> E   ┐
 3247 / 16 =  202  r 15  -> F   │  read
  202 / 16 =   12  r 10  -> A   │  UPWARDS
   12 / 16 =    0  r 12  -> C   ┘

51966 = CAFE base 16
```

> [!warning]
> Two standard slips:
> - Reading the remainders **downwards**. The last remainder is the **first** digit of the answer.
> - **Stopping at 1.** Keep going until the quotient is `0` — `1 / 2 = 0 r 1` supplies the leading bit.

### Alternative: Sum of Weights

For denary → binary, subtract the largest place value that fits, repeatedly.

```text
47 : 32 fits  -> 1, left 15
     16 no    -> 0
      8 fits  -> 1, left 7
      4 fits  -> 1, left 3
      2 fits  -> 1, left 1
      1 fits  -> 1, left 0

47 = 00101111 base 2
```

Faster than division for small numbers, and it self-checks — the chosen weights must add back to the original.

## Binary ↔ Hex Shortcut

One hex digit is exactly 4 bits, so group from the right.

```text
Binary:   1111   0110          Hex:      2      F
            │      │                     │      │
Hex:        F      6           Binary:  0010   1111
```

Keep leading zeros when a fixed width is asked for.

## Why These Bases Are Used

**Binary** — digital circuits have two stable states: off/on, low/high voltage, false/true.

**Hexadecimal** — a compact way to write binary:

- 1 hex digit replaces 4 binary digits, so a byte is 2 characters instead of 8
- shorter values are easier for people to read, write and copy without error
- conversion to and from binary is direct, with no arithmetic

Seen in: memory addresses, machine code, colour codes (`#FF0000`), byte values (`0x7F`).

## Coding Conversions

> [!warning]
> When asked to implement a conversion, do **not** use `bin()`, `hex()`, `oct()` or `int(value, base)`. Using `int()` to turn a string into a number is fine.

```python
def base_to_denary(string, base):
    digits = "0123456789ABCDEF"
    total = 0
    for i in range(len(string)):
        power = len(string) - 1 - i
        total += digits.index(string[i].upper()) * base ** power
    return total


def denary_to_base(num, base):
    digits = "0123456789ABCDEF"
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        result = digits[num % base] + result   # prepend, so it reads correctly
        num = num // base
    return result
```

```python
base_to_denary("11110110", 2)   # 246
base_to_denary("CAFE", 16)      # 51966
denary_to_base(246, 2)          # '11110110'
denary_to_base(51966, 16)       # 'CAFE'
```

Prepending inside the loop is what reverses the remainders for you.

## ASCII

Maps characters to integer codes.

- 7-bit character set → `2 ** 7 = 128` codes
- 95 printable characters + 33 control codes
- enough for a standard English keyboard, not for other languages

| Character | Denary | Hex |
| --------- | ------ | --- |
| `"A"` | `65` | `41` |
| `"a"` | `97` | `61` |
| `"0"` | `48` | `30` |
| `"$"` | `36` | `24` |

```python
ord("A")   # 65
chr(65)    # "A"

digit = "7"
ord(digit) - ord("0")    # 7 — character digit to its number
```

> [!important] "Explain one limitation of ASCII" — 2 marks, asked 2024
> ASCII uses only 7 bits, so it can represent just **128 characters**. That is enough for English letters, digits and punctuation, but it **cannot represent characters from other languages** such as Chinese, Arabic or Greek, nor symbols like emoji.

## Unicode

A single standard giving a code point to characters from many languages and symbol sets.

**Why it's needed**

- ASCII has only 128 codes; even the spare 128 in a byte are nowhere near enough
- different systems otherwise use different numbers for the same character
- version 15 (2023) covers 304,115 characters from 161 languages

| Language | Escape | Character |
| -------- | ------ | --------- |
| Arabic | `حب` | حب |
| Chinese | `爱` | 爱 |
| Greek | `αγάπη` | αγάπη |
| Korean | `사랑` | 사랑 |
| Russian | `люблю` | люблю |

```python
print("사랑")    # 사랑
```

### ASCII vs Unicode

| Question | Answer |
| -------- | ------ |
| Values common to both? | The **first 128 code points are identical** — Unicode was designed to stay backwards compatible with ASCII. |
| Advantage of Unicode over ASCII? | It encodes far more characters, so text in **any language** plus symbols can be represented, not just English. One shared standard also means different systems agree on the same number for the same character. |

> [!example]- UTF-8 encoding
> Not named in the learning outcomes — but 2023 asked *"explain one advantage of using UTF-8 encoding rather than ASCII"* for 2 marks, and it was covered in the C2b lecture.
>
> **Advantage over ASCII:** UTF-8 can represent **every Unicode character**, so it handles any language, while remaining **backwards compatible** — the 128 ASCII characters still take a single byte, so no space is wasted on English text.
>
> UTF-8 stores a Unicode code point in 1–4 bytes. The **first** byte says how many bytes the character uses; every continuation byte starts `10`.
>
> | Bytes | First byte | Continuation bytes |
> | ----- | ---------- | ------------------ |
> | 1 | `0xxxxxxx` | — |
> | 2 | `110xxxxx` | `10xxxxxx` |
> | 3 | `1110xxxx` | `10xxxxxx` × 2 |
> | 4 | `11110xxx` | `10xxxxxx` × 3 |
>
> Encoding `£` (Unicode `A3`, `1010 0011`) — needs 11 bits padded across 2 bytes:
>
> ```text
> code point:  000 1010 0011
> byte 1: 110 00010
> byte 2: 10  100011   ->  1100 0010  1010 0011
> ```
>
> Decoding a stream — read the first byte's prefix to know how far the character extends:
>
> ```text
> 0010 0100   starts 0     -> 1 byte   -> 24   hex  ->  $
> 1100 0010   starts 110   -> 2 bytes  -> A3   hex  ->  £
> 1010 0011   continuation
> 1110 0010   starts 1110  -> 3 bytes  -> 20AC hex  ->  €
> 1000 0010   continuation
> 1010 1100   continuation
> ```

## Common Mistakes

- Reading division remainders downwards instead of upwards.
- Forgetting hex `A`–`F` are `10`–`15`.
- Dropping leading zeros when a fixed number of bits is asked for.
- Using `int(value, base)` in a question that asks you to implement the conversion.
- Confusing ASCII with Unicode — ASCII is 128 codes; Unicode covers many languages.

## Related

- [[LT1 basic python|basic python]]
- [[LT10b Stack|Stack]]
- [[LT10d Hashing|Hashing]]
