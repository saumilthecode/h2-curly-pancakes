> [!summary] Quick View
> A **relational database** keeps data in separate tables that are **linked by keys**, so each fact is stored **once**.
> Storing a fact more than once is **data redundancy**. It causes three **anomalies**: update, deletion, insertion.
> **Functional** and **transitive dependencies** say which field decides which. [[C4-3b Normalisation]] uses them to remove the redundancy.
> Syllabus 3.3.3. Tables and keys are in [[C4-1 Introduction to Database]].

## Why Split into Tables

The lecture's video: an online shop for cat accessories keeps **one spreadsheet**, one row per order.

- Mary buys a cat leash. Later she buys three more, after moving house. Her address is now stored twice, with **different values**.
- Look her up and you get three addresses, and three different customers called Mary Johnson. Shipments go to the wrong place.

The fix is three smaller tables. `Orders` does not repeat the customer's details or the product's details. It **pulls in their IDs**.

```text
 Customers                  Orders                      Products
 ─────────                  ──────                      ────────
 CustomerID   <──────────   CustomerID                  ProductID
 Name                       ProductID    ──────────>    ProductType
 Address                    Date                        QuantityInStock
 ContactInfo                Quantity
```

A change of address is now made **in one place**. The connections between the tables are what make the database *relational*.

## Data Integrity

**Data integrity** is the **accuracy, consistency and reliability** of the data stored in a database. It ensures the data stays correct and unaltered during storage, retrieval and processing.

| Part | Means | Kept by |
| ---- | ----- | ------- |
| **Accuracy** | the data entered is accurate and free from errors | **validation rules** at data entry, so values are reasonable and within expected limits ([[LT4a Data validation and verification\|LT4a]]) |
| **Consistency** | the same data in several places agrees: all copies are updated together | **constraint rules** such as the primary key and foreign key |

## Data Redundancy

**Redundancy** is having **several copies of the same data**, within one table or across several tables.

| MatricNo | Name | Gender | CivicsClass | CivicsTutor |
| -------- | ---- | ------ | ----------- | ----------- |
| 1 | Alex | M | 22S01 | Peter Tan |
| 2 | Brandon | M | 22S01 | Peter Tan |
| 3 | Charles | M | 22S01 | Peter Tan |
| 4 | Dave | M | 22S01 | Peter Tan |
| 5 | Eliza | F | 22S05 | Jane Wong |
| 6 | Felicia | F | 22S11 | Mary Ng |
| 7 | George | M | 22S11 | Mary Ng |
| 8 | Hongli | M | 22S11 | Mary Ng |

*"Peter Tan tutors 22S01"* is one fact, stored four times. Two costs:

1. more **storage space and cost**
2. **inconsistency**, when the copies are not all updated properly

## The Three Anomalies

| Anomaly | Definition | On the table above |
| ------- | ---------- | ------------------ |
| **Update** | a data inconsistency that results from data redundancy and a **partial update** | 22S01's tutor changes to John Lim, but only Alex's record is updated |
| **Deletion** | the **unintended loss** of data due to the deletion of other data | Eliza is the only student in 22S05. Delete her and the tutor of 22S05 is lost |
| **Insertion** | the **inability to add** data because other data is absent | new student Yan Lin has no class yet, so her class and tutor are left out |

```text
UPDATE     22S01's tutor becomes John Lim, but only one record is changed

           1  Alex     M  22S01  John Lim     <- updated
           2  Brandon  M  22S01  Peter Tan    <- missed. Who tutors 22S01 now?

DELETION   Eliza leaves, so her record is deleted

           5  Eliza    F  22S05  Jane Wong    <- the only record of who tutors 22S05

INSERTION  Yan Lin joins before she is given a class

           9  Yan Lin  F  ?      ?            <- CivicsClass and CivicsTutor are omitted
```

All three come from the same fault: one table holds facts about **two different things**, students and classes. The deletion anomaly is *"an example of how combining information that does not really belong together into one table can cause problems"*.

The insertion anomaly also runs the other way. A new class 22S09 and its tutor cannot be recorded until a student joins it, because every record needs a `MatricNo`.

## Data Dependencies

A **dependency** is the relationship between attributes of a table. Two kinds matter, and both are needed for [[C4-3b Normalisation]].

### Functional Dependency

Y is **functionally dependent** on X when the value of X **uniquely determines** the value of Y.

```text
X → Y              MatricNo → Name
```

| Written | Read it as |
| ------- | ---------- |
| `MatricNo → Name` | `MatricNo` determines `Name`. `Name` is functionally dependent on `MatricNo` |

The thing **after** the arrow is the dependent one. Test it by asking: *if I tell you X, can you give me exactly one Y?*

| Try | Result |
| --- | ------ |
| `MatricNo` 5 → `Name`? | Eliza, and only Eliza. **Holds** |
| `Gender` M → `Name`? | Alex, Brandon, Charles… **Does not hold** |
| `CivicsClass` 22S11 → `CivicsTutor`? | Mary Ng every time. **Holds** |

### Transitive Dependency

A transitive dependency is formed by **two functional dependencies**. Z is transitively dependent on X when all three hold:

| Condition | Here |
| --------- | ---- |
| Y depends on X: `X → Y` | `MatricNo → CivicsClass` |
| X does **not** depend on Y | a class does not pick out one student: 22S01 has four |
| Z depends on Y: `Y → Z` | `CivicsClass → CivicsTutor` |

```text
 MatricNo ────────> CivicsClass ────────> CivicsTutor
    X                    Y                     Z
    └──────────── transitive: X → Z ───────────┘
```

So `CivicsTutor` is **transitively dependent** on `MatricNo`: it depends on the key only *through* `CivicsClass`.

> [!important] This is where the redundancy comes from
> The tutor is a fact about the **class**, but the table stores it once per **student**. Every student in 22S01 repeats `Peter Tan`. Moving `CivicsClass → CivicsTutor` into its own table stores it once. That step is **3NF** in [[C4-3b Normalisation#Step 3 Third Normal Form|C4-3b]].

## Exam

> [!important] SLS C4-3a Q1–Q2: definitions
> **Q1 Define data integrity.** The accuracy, consistency and reliability of the data stored in a database. It ensures that the data remains correct and unaltered during operations such as storage, retrieval and processing.
>
> **Q2 Define data redundancy.** Having several copies of the same data within a table or across several tables. It increases storage space and cost, and may cause inconsistent data when the copies are not updated properly.

> [!important] SLS C4-3a Q3–Q5: explain each anomaly
> State **what it is**, then show it with **values from a table**.
>
> **Q3 Update anomaly.** A data inconsistency that results from data redundancy and a partial update. The same data is stored in several records, so if the user updates one without realising it is stored elsewhere, the copies no longer agree. *If 22S01's tutor changes to John Lim and only Alex's record is updated, the table shows two different tutors for 22S01.*
>
> **Q4 Deletion anomaly.** The unintended loss of data due to the deletion of other data. *Eliza is the only student in 22S05, so deleting her record also loses the fact that Jane Wong is the tutor of 22S05.*
>
> **Q5 Insertion anomaly.** The inability to add data to the database due to the absence of other data. *New student Yan Lin has not been assigned a class, so her `CivicsClass` and `CivicsTutor` have to be omitted.*
>
> These answers use the lecture slides' wording. SLS's own suggested answers are not in your archive.

> [!important] 2026 Mock Promo P1 Q5(b): redundancy and inconsistency `[2]`
> Already examined on a flat file. The answer is in [[C4-1 Introduction to Database#Exam|C4-1]]: the title and venue of course `C08` are stored again in every `C08` row (redundancy), and changing one copy without the others leaves conflicting values (inconsistency).

> [!tip] From class, 11 Nov 2026: how theory marks are lost
> Knowing the idea is not enough. The answer has to be **phrased completely**. Read the sample answers and ask what is missing from each.
> When a question wants **two** advantages, list every one you know, then pick the two that fit the **context** given and are taught at this level.

> [!example]- Practice, written for these notes (not from a paper)
> `LOAN (LoanID, Member, ISBN, Title, Publisher)`
>
> | LoanID | Member | ISBN | Title | Publisher |
> | ------ | ------ | ---- | ----- | --------- |
> | 1 | Aisha | 111 | Dune | Ace |
> | 2 | Ben | 111 | Dune | Ace |
> | 3 | Chen | 222 | Emma | Penguin |
>
> - **Redundancy:** the title and publisher of ISBN 111 are stored twice.
> - **Update anomaly:** change the publisher of 111 in loan 1 only, and 111 has two publishers.
> - **Deletion anomaly:** delete loan 3, the only loan of 222, and the library no longer knows 222 is *Emma* by Penguin.
> - **Insertion anomaly:** a new book that nobody has borrowed cannot be added, because there is no `LoanID` for it.
> - **Transitive dependency:** `LoanID → ISBN → Title`. `ISBN` does not determine `LoanID`: 111 has loans 1 and 2.

## Common Mistakes

- Reading the arrow backwards. In `X → Y` it is **Y** that depends on X.
- Explaining an update anomaly without saying that **only some** of the copies were changed.
- Swapping deletion and insertion: deletion **loses** data you wanted to keep, insertion **cannot add** data you have.
- Judging a dependency from the sample rows alone. Ask what *could* happen: two students can share a name, so `Name → MatricNo` does not hold.
- Calling a repeated value redundancy when it is a **link**. After normalising, `22S01` still appears once per student. That is a foreign key doing its job.

## Related

- [[C4-1 Introduction to Database]]
- [[C4-3b Normalisation]]
- [[C4-3c ER Diagram]]
- [[LT4a Data validation and verification]]
