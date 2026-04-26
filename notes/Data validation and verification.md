> [!important] Key Distinction
> - Validation checks whether data is sensible and reasonable.
> - Verification checks whether data matches the original source.

## Comparison

| Term           | What it means                                   | Example                                |
| -------------- | ----------------------------------------------- | -------------------------------------- |
| Verification   | checks that entered data matches the source     | double entry for password changes      |
| Validation     | checks that entered data is sensible            | age is between `0` and `99`            |

## Validation Techniques

| Technique                     | What it checks                               | Example                               |
| ---------------------------- | -------------------------------------------- | ------------------------------------- |
| Check digit                  | uses extra digits to verify the rest         | NRIC, ISBN, credit card               |
| Format check                 | checks the correct pattern / format          | date format, email format             |
| Length check                 | checks a fixed number of characters          | phone number, password length         |
| Lookup table / drop-down     | checks against a list of allowed values      | school name, day of the week          |
| Type check                   | checks the correct data type                 | digits only, letters only             |
| Spell check / autocorrect    | checks against a dictionary                  | product names, common words           |
| Presence check               | checks that a required field is not empty    | username must be filled in            |
| Range check                  | checks that data falls within limits         | age `0` to `99`, height `0.5` to `2.5` |

## Python Examples

| Check          | Example                                      |
| -------------- | -------------------------------------------- |
| Presence Check | `string != ""`                               |
| Range Check    | `79999999 < n < 100000000`                   |
| Length Check   | `len(string) < 6`                            |
| Type Check     | `string.isnumeric()` or `string.isalpha()`   |
| Format Check   | `email.endswith("@students.edu.sg")`         |


```python
a, b = b, a
```

This is an easier way to swap two variables.

## Related

- [[basic python]]
