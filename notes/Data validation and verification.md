
Data Verification
- Verification simply ensures that the data entered matches the original source
- prevent human error with double entry (pw changes)

Data Validation
==to check to ensure that data entered is sensible and reasonable. does not check the accuracy==

validation techniques

```mermaid
mindmap
  root((Validation Techniques))
    Check Digit
      check one or two digits to verify the other digits are correct
	      e.g. NRIC, ISBN, car plate number, credit card

    Format Check
      check that data is in the correct format
	      e.g. ddmmyyyy, NRIC

    Length Check
      check that the length is a certain number
	      e.g. phone number, credit card number

    Lookup Table / Drop-Down Menu
      looks up acceptable values in a table
	      e.g. valid school names, road names, days, salutations

    Type Check
      check that input is the correct type
	      e.g. isdigit, isalpha, alphanumeric

    Spell Check / Autocorrect
      check against a dictionary
	      e.g. technical terms, product names

    Presence Check
      check a required field is not null
	      e.g. value != ""

    Range Check
      check that data is within a restricted range
	      e.g. 0 < age < 99, 0.5 < height < 2.5
```



| Presence Check | string == ''                                    |
| -------------- | ----------------------------------------------- |
| Range Check    | 79999999 < n < 100000000                        |
| Length Check   | len(string) < 6:                                |
| Type Check     | type(eval("string")) or .isnumeric()/.isalpha() |
| Format Check   | [.find('@'):] == '@students.edu.sg':            |


a , b = b,a 
easier variable swap