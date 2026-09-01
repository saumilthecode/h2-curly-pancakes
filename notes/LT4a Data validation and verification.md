> [!important] Key Distinction
> **Validation** — is the data *sensible, reasonable and allowable*?
> **Verification** — does the data *match the original source*?

Validation does **not** check whether data is accurate. `age = 35` is valid even if you are 17.

| Term | Checks | Example |
| ---- | ------ | ------- |
| Verification | entered data matches the source | typing a new password twice |
| Validation | entered data is sensible | age is between `0` and `99` |

**Two methods of verification:**

- **Double entry** — the data is typed twice and the two copies compared.
- **Visual check / proofreading** — the operator reads the entered data back against the source document.

## Validation Techniques

The seven named in the syllabus:

| Technique | What it checks | Example |
| --------- | -------------- | ------- |
| Existence check | the data is already in the system | username already registered |
| Format check | data follows the correct pattern | `ddmmyyyy`, email address |
| Length check | data has the required length | 8-digit phone number |
| Presence check | a required field is not left empty | username must be filled in |
| Range check | data falls within limits | `0 < age < 99` |
| Type check | data is the right type | digits only, letters only |
| Check digit | extra digit verifies the other digits | NRIC, ISBN, credit card |

Also taught in lecture:

| Technique | What it checks | Example |
| --------- | -------------- | ------- |
| Lookup table / drop-down | value is in a list of allowed values | school name, day of the week |
| Spell check / autocorrect | value matches a dictionary | product names |

## In Python

| Check | Code |
| ----- | ---- |
| Presence | `string != ""` |
| Range | `0 < age < 99` |
| Length | `len(string) == 8` |
| Type | `string.isnumeric()`, `string.isalpha()` |
| Format | `email.endswith("@students.edu.sg")` |
| Existence | `username in registered_users` |

> [!note]
> `input()` always hands you a `str`, so these examine **characters in a string**. That is what the course asks for here; convert afterwards if you need the number itself.

## Check Digits

An extra digit calculated from the others and appended to the number, so an error can be spotted on entry.

**Two types of error a check digit detects** — 2020 Q5(b)(iii), *"Name two types of error that check digits usually detect"* `[2]`:

- **Transcription error** — a single digit typed wrongly (`02757` → `02157`)
- **Transposition error** — two adjacent digits swapped (`02757` → `02575`)

> [!example]- Worked example — Modulus 11 check digit for `02757` (2020 Q5(c), `[3]`)
> Weights, starting from the first digit: `6, 5, 4, 3, 2`.
>
> ```text
> digit    0    2    7    5    7
> weight   6    5    4    3    2
>          -    -    -    -    -
>          0 + 10 + 28 + 15 + 14  = 67
>
> 67 mod 11 = 1
> check digit = 11 - 1 = 10  ->  written as 'X'
> ```
>
> So the full number is `02757X`.
>
> 2020 Q5(d) then asks for **two reasons** the field is stored as a **string, not an integer** `[2]`: the check digit can be `X`, which is not a digit; and a leading zero would be lost from an integer.

> [!tip]
> A check digit is a **checksum** applied to identification numbers — same idea as [[LT10d Hashing|Hashing]].

## Related

- [[LT4b Types of Errors and Test Cases]]
- [[LT10d Hashing]]
- [[LT1 basic python]]
