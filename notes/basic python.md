types

| int   | wholenumber |
| ----- | ----------- |
| float | decimals    |
| bool  | True/False  |
| str   | string      |
| None  | null        |

---
shortcuts 

| type()   | find out the type                                  |
| -------- | -------------------------------------------------- |
| upper()  | maker uppercase                                    |
| lower()  | make lowercase                                     |
| .index() | find the index of the character in the parenthesis |
| ord()    | unicode char number                                |

converters

| str()   | turn anything into a string           |
| ------- | ------------------------------------- |
| float() | turn anything into a float            |
| int()   | turn float into integer (no decimals) |

---
jargon

a = 10

value of 10 is assigned to a

---
operations

|* on a string multiplies it a number of times

| +   | plus                                    |
| --- | --------------------------------------- |
| -   | minus                                   |
| *   | multiply                                |
| **  | to the power of                         |
| /   | divide to a float (including remainder) |
| //  | floor divide (round down)               |
| %   | find the remainder (remainder only)     |

---
evals

| >   | left more then right      |
| --- | ------------------------- |
| <   | right more then left      |
| ==  | equal                     |
| !=  | not equals to             |
| >=  | greater then or equals to |
| <=  | less than or equals to    |
42 == 42 true
42 == 42.0 true (only true if decimal 0)
42 == "42" false

---
operators

| and    | True if both side of the and are True |
| ------ | ------------------------------------- |
| or     | True if either side is True           |
| not    | True if it is False                   |
| in     |                                       |
| not in |                                       |
|        |                                       |

---

| True  | 1   |
| ----- | --- |
| False | 0   |

---

Slicing

string = "HelloWorld"

string[2:5:1]

2 - start
5 - end
1- step (interval

negative indexing makes it go from the back