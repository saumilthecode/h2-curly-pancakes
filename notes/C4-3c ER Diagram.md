> [!summary] Quick View
> An **ER diagram** (entity-relationship diagram) draws each **entity** as a box and each **relationship** as a line. A **crow's foot** on the line marks the **many** end.
> A relational database cannot hold a **many-to-many** relationship. Put a **linked entity** between the two, and it becomes two **one-to-many** relationships.
> Syllabus 3.3.5. The tables behind these diagrams are built in [[C4-3b Normalisation]].

## Entities and Attributes

An **entity** is a real-world object or concept that can be **distinctly identified**. It has **attributes** that describe its properties.

| Entity | Possible attributes |
| ------ | ------------------- |
| Student | student ID, name, date of birth, email address |
| Teacher | teaching subject, name, contact number, email address |
| Course | course code, course name, start and end date, number of students it can take |
| Library book | title, author, publisher, ISBN, cost, year of publication |

In the database an **entity becomes a table**, an **attribute becomes a field**, and one particular student is one record.

## The Three Relationships

Read every line **from both ends**: one of these has how many of those, and one of those has how many of these?

| Relationship | Drawn with | Read from both ends |
| ------------ | ---------- | ------------------- |
| **one-to-one** | a plain line | one car has one insurance policy. One policy belongs to one car |
| **one-to-many** | a crow's foot at the **many** end | one civics class has many students. One student belongs to only one civics class |
| **many-to-many** | a crow's foot at **both** ends | one student can join many CCAs. One CCA can be joined by many students |

```text
one-to-one       ┌─────┐          ┌───────────┐
                 │ Car │──────────│ Insurance │
                 └─────┘          └───────────┘

one-to-many      ┌────────┐          ┌─────────┐
                 │ Civics │─────────<│ Student │
                 └────────┘          └─────────┘
                    one                 many

many-to-many     ┌─────────┐          ┌─────┐
                 │ Student │>────────<│ CCA │
                 └─────────┘          └─────┘
                    many               many
```

The data shows the many-to-many: Adrian (`MatricNo` 2) and Bee Lay (5) each have two CCAs, and Choir has two students.

One-to-one is *"not very meaningful"* in this syllabus. The marks are in one-to-many and many-to-many.

> [!tip] From class, 11 Nov 2026: stand at one entity and look across
> Stand at `Customers`: one customer can have many orders, because they can order today and again tomorrow. Stand at `Orders`: one order belongs to one customer. So it is one-to-many, with the crow's foot at `Orders`.

## Many-to-Many Needs a Linked Entity

The relational database you are learning cannot handle a many-to-many relationship. A field holds **one** value ([[C4-3b Normalisation#Step 1 First Normal Form|1NF]]), so `Student` cannot hold a list of CCAs and `CCA` cannot hold a list of students.

Introduce a **linked entity** between the two. It has one record for each pairing.

```text
before   ┌─────────┐                              ┌─────┐
         │ Student │>────────────────────────────<│ CCA │
         └─────────┘                              └─────┘

after    ┌─────────┐        ┌────────────┐        ┌─────────┐
         │ Student │───────<│ StudentCCA │>───────│ CCAInfo │
         └─────────┘        └────────────┘        └─────────┘
                            linked entity
```

| Line | Why it is one-to-many |
| ---- | --------------------- |
| `Student` to `StudentCCA` | one student record can have many `StudentCCA` records: Adrian and Bee Lay have two each |
| `CCAInfo` to `StudentCCA` | one CCA record can have many `StudentCCA` records: Choir has two. Each `StudentCCA` record points to only one CCA |

**Both crow's feet touch the linked entity.**

### What Goes in the Linked Entity

| Put in | Leave out |
| ------ | --------- |
| the **foreign keys** to both sides: `MatricNo`, `CCAName` | details of either side: the student's name, the CCA teacher |
| anything about the **pairing itself**: a loan's `BorrowDate`, an order's `Quantity` | |

Details stay in their own tables. Copying them in would bring back the redundancy.

## The Whole Database

The four normalised tables from [[C4-3b Normalisation#The Normalised Tables|C4-3b]] as one diagram: three entities and one linked entity, all joined by one-to-many relationships.

```text
┌────────┐       ┌─────────┐       ┌────────────┐       ┌─────────┐
│ Civics │──────<│ Student │──────<│ StudentCCA │>──────│ CCAInfo │
└────────┘       └─────────┘       └────────────┘       └─────────┘
```

## The Crow's Foot Follows the Foreign Key

The **many** end is always the table that **holds the foreign key**.

| Relationship | Many end | Foreign key it holds |
| ------------ | -------- | -------------------- |
| `Civics` to `Student` | `Student` | `CivicsClass*` |
| `Student` to `StudentCCA` | `StudentCCA` | `MatricNo*` |
| `CCAInfo` to `StudentCCA` | `StudentCCA` | `CCAName*` |

It works in both directions. Given a diagram, you know where each foreign key goes. Given table descriptions, you know where each crow's foot goes.

It also gives the order to **create** the tables: the "one" ends first, because the many end refers to them ([[C4-4 Advanced SQL#C4-4a Create Multiple Tables|C4-4a]]).

## Drawing One

1. **Find the entities:** the things the database keeps several facts about. A single fact, such as a borrow date, is an attribute.
2. **Pair them up.** For each related pair, read it from both ends and decide one-to-one, one-to-many or many-to-many.
3. **Replace each many-to-many** with a linked entity, unless the question says not to.
4. **Draw** the boxes, the lines and the crow's feet at the many ends. Use the question's names exactly.

## Exam

> [!important] 2025 Promo P1 Q4(a): ER diagram `[2]`
> One customer makes many bookings. One villa has many bookings.
>
> ```text
> ┌──────────┐        ┌─────────┐        ┌───────┐
> │ CUSTOMER │───────<│ BOOKING │>───────│ VILLA │
> └──────────┘        └─────────┘        └───────┘
> ```
>
> 1m the three entities · 1m both one-to-many links, with the many end at `BOOKING`. The table descriptions for part (b) are in [[C4-1 Introduction to Database#Exam|C4-1]].

> [!important] SLS C4-3c Library Q1–Q6
> A school library records each book's ISBN13, title, author, publisher and availability, each student's ID, name, class and email, and the borrow date and return date of each loan.
>
> **Q1 Entities:** `LibraryBook` and `Student`. `BorrowDate`, `ISBN13`, `Title` and `StudentName` are attributes.
>
> **Q2 Attributes of `LibraryBook`:** `ISBN13`, `Title`, `Author`, `Publisher`. `BorrowDate` belongs to the loan, `StudentName` to the student.
>
> **Q3 Attributes of `Student`:** `StudentID`, `Name`, `Email`, `Class`. Not `Author`.
>
> **Q4 `Student` and `LibraryBook`:** **many-to-many**. One student can borrow many books, and over time one book can be borrowed by many students.
>
> **Q5 The diagram with the linked entity `Loan`:** Option 2, both crow's feet at `Loan`.
>
> ```text
> ┌─────────┐        ┌──────┐        ┌─────────────┐
> │ Student │───────<│ Loan │>───────│ LibraryBook │
> └─────────┘        └──────┘        └─────────────┘
> ```
>
> | Option | What is wrong |
> | ------ | ------------- |
> | 1 | the second crow's foot is at `LibraryBook`, not `Loan` |
> | 3 | the crow's feet are at `Student` and `LibraryBook`, the two "one" ends |
> | 4 | `LibraryBook` is in the middle. The linked entity must sit between the other two |
>
> **Q6 Attributes of `Loan`:** `StudentID`, `BookISBN`, `BorrowDate`, `ReturnDate`: the two foreign keys, and the facts about the loan itself. `StudentName`, `StudentClass`, `BookTitle` and `BookAuthor` stay in their own tables.
>
> Worked from the lecture. SLS's own suggested answers are not in your archive.

> [!example]- SLS C4-3c Online Shopping Q1–Q3: draw it, then add the linked entity (try it first)
> ```text
> CUSTOMER: ID, Name, Email
> PRODUCT:  ID, Name, Description, UnitPrice
> ORDERS:   ID, CustID, ProductID, Quantity, DeliveryAddress, OrderDate
> ```
>
> *A customer may purchase many different items in a single order.*
>
> **Q1 Without a linked entity.** One customer places many orders, and an order belongs to one customer. One order holds many products, and one product appears in many orders.
>
> ```text
> ┌──────────┐        ┌────────┐        ┌─────────┐
> │ CUSTOMER │───────<│ ORDERS │>──────<│ PRODUCT │
> └──────────┘        └────────┘        └─────────┘
> ```
>
> **Q2 With the linked entity `OrderProduct`** between `ORDERS` and `PRODUCT`.
>
> ```text
> ┌──────────┐       ┌────────┐       ┌──────────────┐       ┌─────────┐
> │ CUSTOMER │──────<│ ORDERS │──────<│ OrderProduct │>──────│ PRODUCT │
> └──────────┘       └────────┘       └──────────────┘       └─────────┘
> ```
>
> **Q3 Table descriptions.**
>
> ```text
> CUSTOMER (ID_, Name, Email)
> PRODUCT (ID_, Name, Description, UnitPrice)
> ORDERS (ID_, CustID*, DeliveryAddress, OrderDate)
> OrderProduct (OrderID_*, ProductID_*, Quantity)
> ```
>
> `ProductID` and `Quantity` move into the linked entity, because they describe one product within one order. `DeliveryAddress` and `OrderDate` describe the whole order, so they stay. The question gives no name for the field that refers to `ORDERS.ID`, so `OrderID` is a choice.
>
> Compare [[C4-4 Advanced SQL]]: in `Northwind.db` each `Orders` record holds one product, so `Orders` itself is the linked entity between `Customers` and `Products`.
>
> Worked from the lecture. SLS's own suggested answers are not in your archive.

## Common Mistakes

- Crow's foot on the wrong end. Check it against the foreign key: the many end holds it.
- Reading a relationship from one end only.
- Leaving a many-to-many in the final diagram, or adding a linked entity when the question says not to.
- Drawing an attribute such as `BorrowDate` or `Title` as an entity.
- Putting the linked entity at one end of the chain instead of between the two entities.
- Copying details such as `StudentName` or `BookTitle` into the linked entity.
- Renaming the entities. Use the question's names exactly.

## Related

- [[C4-3b Normalisation]]
- [[C4-3a Introduction to Relational Database]]
- [[C4-1 Introduction to Database]]
- [[C4-4 Advanced SQL]]
