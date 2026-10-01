> [!summary] Quick View
> A database stores related data in **tables**. Rows are **records**, columns are **fields**. A **primary key** picks out exactly one record.
> SQL is in [[C4-2 Basic SQL]].

> [!important] Syllabus scope: 3.3 Databases
> | Ref | Outcome | Where |
> | --- | ------- | ----- |
> | 3.3.1 | table, record and field | here |
> | 3.3.2 | primary, secondary, composite and foreign keys | here, except secondary |
> | 3.3.3–3.3.5 | redundancy, 3NF, ER diagrams | flat-file redundancy here (asked in the Mock Promo). The rest is C4-3, not taught yet |
> | 3.3.6–3.3.7 | NoSQL | not taught yet |
> | 3.3.8 | SQL statements | [[C4-2 Basic SQL]] |
>
> Every A-Level Paper 1 from 2020 to 2024, and the 2027 specimen, has a database question worth 19–27 marks, mostly normalisation and ER diagrams (C4-3).

## Why a Database

A **database** is a collection of related data, stored in an organised or logical manner: patient records, a supermarket's inventory, your contact list.

A **card index** has **one filing order**, so it can only be searched on one data item. Filed by name, finding *"the customer at 13 The High Street"* means reading every card.

Limitations of **flat files** (SLS A1):

- duplicate copies of the same data
- data inconsistency
- hard to update or change data
- hard to search or query

**Data redundancy**: the same data stored more than once, e.g. a course's title and venue repeated in every enrolment row. **Data inconsistency**: one copy gets changed but the others don't, so the same item ends up with conflicting values.

## Table, Record, Field

| Colour | Price | AmountSold | Stock |
| ------ | ----- | ---------- | ----- |
| Red | 0.50 | 40 | 30 |
| Green | 0.50 | 17 | 18 |
| Yellow | 0.80 | 57 | 43 |
| Blue | 0.90 | 24 | 66 |
| White | 0.85 | 36 | 39 |

**5 records** (rows), **4 fields** (columns). A record is one entry about one item. A field holds one attribute of it. SLS A3–A4 use this table without `AmountSold`: 5 records, 3 fields.

Rules for a table:

| Rule | Example |
| ---- | ------- |
| each value is **atomic** | one mobile number per record |
| each record is **unique** | the same row cannot appear twice |
| each field is **unique** | two numbers need `MobileNo1` and `MobileNo2` |
| order of fields and records **does not matter** | - |
| field names are **one word** | `MobileNo`, not `Mobile No` |

> [!warning]
> 2025 promo: **1m for "all fields single word"**.

### Table Description

```text
STUDENTS (RegNo, Name, Gender, MobileNo)
          ─────
```

In the exam the **primary key is underlined** and a **foreign key has a dashed underline**. SLS can't underline, so it types the key as `RegNo_`.

## Primary Key

A field that **uniquely identifies** one record. Its value **should not change over time**.

For `STUDENTS (RegNo, Name, Gender, MobileNo)`:

| Choice | Why |
| ------ | --- |
| `{RegNo}` | **best**: fewest fields, never repeats |
| `{RegNo, Name, MobileNo}` | works, but more than needed |
| `{Name}` | two students can share a name |
| `{MobileNo}` | two students can share a home number |
| `{Gender}` | many students share it |

Check what *could* repeat across all possible records. Ten sample rows can't show it.

A **candidate key** is any field (or set of fields) that could be the primary key, because its value uniquely identifies each record. Asked in the 2026 Mock.

### Composite Primary Key

Two or more fields that **together** identify a record. With no `RegNo`, the key becomes `{Name, MobileNo}`: two people may share a number, but they won't also share a name.

`{Name, Gender}` and `{Gender, MobileNo}` still repeat, so they fail.

### Foreign Key

A field that holds another table's primary key, linking the two tables.

```text
Customers (Id, FirstName, LastName, City, Country, Phone)
           ──
Orders (Id, OrderDate, CustomerID, ProductID, Quantity)
        ──             ----------  ---------
```

`Orders.CustomerID` refers to `Customers.Id`. In DB Browser, that link stops you deleting a customer who still has orders. See [[C4-2 Basic SQL#C4-2e Delete and Drop|C4-2e]].

## Exam

> [!important] SLS A5–A7: spot the key
> **A5** `BALLOONS (Colour_, Price, AmountSold, Stock)`: every colour appears once.
>
> **A6** `CustomerID`. Postal codes already repeat (`774321` twice), and a name can.
>
> **A7** `{CustomerID, Colour, Date}`. `CustomerID` + `Colour` repeats: `AB123` bought Red on 26/08 and 28/09. The rule *"not the same colour on the same day"* puts `Date` in the key. `Quantity` describes the sale. It cannot identify it.
>
> ```text
> SALE (CustomerID, Colour, Quantity, Date)
>       ──────────  ──────            ────
> ```

> [!important] 2025 Promo P1 Q4(a): ER diagram `[2]`
> One customer makes many bookings. One villa has many bookings.
>
> ```text
> CUSTOMER ──────< BOOKING >────── VILLA
> ```
>
> 1m the three entities · 1m both one-to-many links, with the "many" end at `BOOKING`.

> [!important] 2025 Promo P1 Q4(b): table descriptions `[3]`
> A villa-hire company: `CUSTOMER`, `VILLA`, `BOOKING`.
>
> ```text
> CUSTOMER (ID, name, email)
>           ──
> VILLA (ID, name, cost)
>        ──
> BOOKING (ID, customerID, villaID, startDate, numberOfDays)
>          ──  ----------  -------
> ```
>
> 1m all primary keys · 1m all foreign keys · 1m all fields single word. Three descriptions with none of these score 0.

> [!important] 2024 Promo P1 Q4: `OrderDetails` `[1+2+1+2]`
> `OrderDetails (CustomerID, ProductID, Quantity, UnitPrice, Date)`
>
> **(a)** Composite key `{CustomerID, ProductID, Date}`: `C004` bought `P2003` on both 14 and 15 Sep, so the first two alone repeat.
>
> ```text
> OrderDetails (CustomerID, ProductID, Quantity, UnitPrice, Date)
>               ──────────  ─────────                       ────
> ```
>
> **(b)** Two functions of a PK, 1m each:
> 1. It **uniquely identifies** a particular record.
> 2. Records are **sorted by the PK** for easy searching and retrieval.
>
> **(c)(i)** Add a field `OrderID` `[1]`. **(ii)** New PK `{OrderID}` (1m). Better because it's one value to give instead of three, and faster to sort and search on (1m).
>
> 2026 Mastery P1 Q4 repeats (a) and (b).

> [!example]- A-Level keys on link tables: 2020 Q6(b)(iii), 2021 Q2(d), 2023 Q4(b)
> A table that records *who is linked to what* needs both sides in its key.
>
> **2020 Q6(b)(iii)** `IsTaking (StudentID, CourseID)`: a student takes many courses, a course has many students. Key: both. `[1]`
>
> **2021 Q2(d)** `ProjectEmployee (ProjectID, EmployeeID, Hours)`: key `{ProjectID, EmployeeID}`. `[1]`
>
> **2023 Q4(b)** identify every primary and foreign key `[6]`:
>
> ```text
> Car (RegistrationNumber, Make, Model, CategoryName)
>      ──────────────────               ------------
> Category (CategoryName, DayRate)
>           ────────────
> Customer (DriverLicenceNumber, Name, Address, TelephoneNumber)
>           ───────────────────
> Hire (RegistrationNumber, DriverLicenceNumber, DateHired, DateExpectedBack, DateReturned)
>       ──────────────────  -------------------  ─────────
> ```
>
> A car goes out to one customer at a time, so `{RegistrationNumber, DateHired}` is enough for `Hire`'s key. `RegistrationNumber` is part of that key **and** a foreign key to `Car`.

> [!important] 2026 Mock Promo P1 Q5: course enrolments in a flat file `[2+2+2]`
> Fields `EnrolmentID, ParticipantName, CourseCode, CourseTitle, Venue`. Five records, and `C08` (Introduction to Coding, Lab 1) appears three times.
>
> **(a)** `Studio 2` is in the field **Venue** (1m). Record `E1044` is `E1044, Chen, C15, Robotics Basics, Lab 3` (1m).
>
> **(b)** **Redundancy**: the title and venue for `C08` are stored again in every `C08` row (1m). **Inconsistency**: change one copy without the others, and the same course has conflicting titles or venues (1m).
>
> **(c)** Candidate key **`EnrolmentID`**: its value uniquely identifies each record (1m). Not `ParticipantName`: the same name can appear in more than one record, as `Aisha` does (1m).

## Common Mistakes

- Picking a field that is unique in the sample but could repeat: names, postal codes, phone numbers.
- A composite key with a spare field that adds nothing.
- Spaces in field names.
- Counting the header row as a record.

## Related

- [[C4-2 Basic SQL]]
- [[LT4a Data validation and verification]]
