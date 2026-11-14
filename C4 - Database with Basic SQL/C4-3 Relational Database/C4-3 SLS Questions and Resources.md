# C4-3 Relational Database: SLS Questions and Resources

- Source: https://vle.learning.moe.edu.sg/class-group/assignment/attempt/5365af90-5a04-4bbf-a877-6fbcb285e14b
- Archived and verified: 12 November 2026
- Prompt-only questions: 20 (C4-3a: 5; C4-3b: 6; C4-3c Library: 6; C4-3c Online Shopping: 3)

This archive excludes personal answers, uploaded student work, marks, submission state, suggested answers and feedback. All multiple-choice options are preserved without indicating selections or correctness.

C4-4 SLS contains no activities and links to [C4-4 Coursemology](https://yijc.coursemology.org/courses/3257/assessments/88878); its seven prompts are saved separately in `../C4-4 Advanced SQL/C4-4 Coursemology Questions.md`.

## Teaching resources

- C4-3a slides: [C4-3a_Introduction_to_Relational_Database.pdf](Slides/C4-3a_Introduction_to_Relational_Database.pdf)
- C4-3b slides: [C4-3b_Normalisation.pdf](Slides/C4-3b_Normalisation.pdf)
- C4-3c ER Diagram: the live SLS overview says to download slides, but it contains no slide attachment. No C4-3 resource folder was found in the inspected Coursemology Trainings material folder. This slide file is not available in the verified sources.
- C4-4 slides: [C4-4_Advanced_SQL.pdf](../C4-4%20Advanced%20SQL/Slides/C4-4_Advanced_SQL.pdf)
- All four lecture videos and their English timestamped transcripts: [Video index](../Shared%20Resources/C4-3%20and%20C4-4%20Video%20Transcript%20Index.md).
- Supplementary video linked in C4-3a slides, p. 2: https://www.youtube.com/watch?v=znw_rnnnWjY, transcript saved in `../../notes/transcripts`.
- C4-3b Q6 source normalisation worksheet: [local original XLSX export](C4-3b%20Normalisation%20source%20worksheet.xlsx), with [source and integrity checks](Source%20Resources/C4-3b%20Normalisation%20source%20worksheet%20-%20Source.md). Online source: https://docs.google.com/spreadsheets/d/12YvEdui-ni-GEARH-qEYN9BPN18Z5FaC/edit .

## C4-3a Introduction to Relational Database

### Question 1

Define 'Data Integrity' in database.

### Question 2

Define 'Data Redundancy' in a database.

### Question 3

Explain 'Update Anomaly' in a database.

### Question 4

Explain 'Deletion Anomaly' in a database.

### Question 5

Explain 'Insertion Anomaly' in a database.

## C4-3b Normalisation

### Question 1

Why is there a need for normalization of data?

Options, in source order:

- To make sure the data are normal.
- To reduce data redundancy
- To prevent data loss
- To prevent data inconsistency

### Question 2

Explain why the following table 'Invoice' is not in 1NF and describe how to normalise it to 1NF.

![Question 2 source diagram](Source%20Resources/C4-3%20SLS%20question%20assets/C4-3b-Q2-1.png)

### Question 3

Explain why the table 'InvoiceDetail' is not in 2NF and describe how to normalise it to 2NF.

If you intend to split the table 'InvoiceDetail' into multiple tables, state the Table Descriptions, indicating the Primary Key (using underscore '_') and Foreign Key (using asterisk '*').

![Question 3 source diagram](Source%20Resources/C4-3%20SLS%20question%20assets/C4-3b-Q3-1.jpg)

### Question 4

Explain why the table 'Invoice' is not in 3NF and describe how to normalise it to 3NF.

If you intend to split the table 'InvoiceDetail' into multiple tables, state the Table Descriptions, indicating the Primary Key (using underscore '_') and Foreign Key (using asterisk '*').

![Question 4 source diagram](Source%20Resources/C4-3%20SLS%20question%20assets/C4-3b-Q4-1.png)

### Question 5

Explain why the following tables are fully normalised.

![Question 5 source diagram](Source%20Resources/C4-3%20SLS%20question%20assets/C4-3b-Q5-1.png)

### Question 6

Normalize the following to 3NF.

Provide the Table Descriptions of the fully normalised database.

The link to the soft copy of this table can be found here. Make a copy and work on normalising the data.

The Table Descriptions should be written in the following format:

TABLENAME (Attribute1_, Attribute2*, ...)

Use an underscore ('_') to denote the Primary Key and an asterisk ('*') for the Foreign Key.

![Question 6 source diagram](Source%20Resources/C4-3%20SLS%20question%20assets/C4-3b-Q6-1.png)

Source link (here): https://docs.google.com/spreadsheets/d/12YvEdui-ni-GEARH-qEYN9BPN18Z5FaC/edit?usp=sharing&ouid=114646725839433423054&rtpof=true&sd=true

## C4-3c ER Diagram: Library Database

### Question 1

The purpose of this database is to allow students to borrow books from the school library.
This database records information about students, the books, and loan details.
Information regarding the book like ISBN13, title, author, publisher and its availability for borrowing are recorded.
The students' ID, name, class, and email are also in the database.
The borrow date and return date are recorded for the loan records.

Which of the following are the entities?

Options, in source order:

- Option 1: LibraryBook
- Option 2: BorrowDate
- Option 3: ISBN13
- Option 4: Title
- Option 5: Student
- Option 6: StudentName

### Question 2

For the entity LibraryBook, which of the following are the possible attributes?

Options, in source order:

- Option 1: BorrowDate
- Option 2: ISBN13
- Option 3: Title
- Option 4: StudentName
- Option 5: Author
- Option 6: Publisher

### Question 3

For the entity Student, which of the following are the possible attributes?

Options, in source order:

- Option 1: StudentID
- Option 2: Name
- Option 3: Email
- Option 4: Class
- Option 5: Author

### Question 4

If the students can borrow books from the library.

What type of relationship is there between the Student and the LibraryBook entities?

Options, in source order:

- Option 1: One-to-One relation
- Option 2: One-to-Many relation
- Option 3: Many-to-One relation
- Option 4: Many-to-Many relation

### Question 5

A relational database is unable to handle a many-to-many relationship between two entities
A link-entity, LOAN, is introduced to decompose the many-to-many relationship between STUDENT and LibraryBook.

Which of the following is the correct ER diagram with a link-entity between the Student and LibraryBook entities?

Options, in source order:

- Option 1

  ![Question 5 option 1](Source%20Resources/C4-3%20SLS%20question%20assets/C4-3c-Library-Q5-option1-1.png)
- Option 2

  ![Question 5 option 2](Source%20Resources/C4-3%20SLS%20question%20assets/C4-3c-Library-Q5-option2-1.png)
- Option 3

  ![Question 5 option 3](Source%20Resources/C4-3%20SLS%20question%20assets/C4-3c-Library-Q5-option3-1.png)
- Option 4

  ![Question 5 option 4](Source%20Resources/C4-3%20SLS%20question%20assets/C4-3c-Library-Q5-option4-1.png)

### Question 6

Which of the following are the possible attributes of the linked-entity Loan?

Options, in source order:

- Option 1: StudentID
- Option 2: StudentName
- Option 3: StudentClass
- Option 4: BookISBN
- Option 5: BookTitle
- Option 6: BookAuthor
- Option 7: BorrowDate
- Option 8: ReturnDate

## C4-3c ER Diagram: Online Shopping Database

### Question 1

Upload a file with your answer. You can attach up to 10 files.

The database contains the following information:

CUSTOMER: ID, Name, Email
PRODUCT: ID, Name, Description, UnitPrice
ORDERS: ID, CustID, ProductID, Quantity, DeliveryAddress, OrderDate

Note: A customer may purchase many different items in a single order.

Draw the Entity-Relation (ER) diagram for this online shopping database.

Do not introduce linked-entity for any many-to-many relationship.

You may use  https://www.draw.io/ or any other tools to construct the ER diagram.

### Question 2

Upload a file with your answer. You can attach up to 10 files.

The database contains the following information:

CUSTOMER: ID, Name, Email
PRODUCT: ID, Name, Description, UnitPrice
ORDERS: ID, CustID, ProductID, Quantity, DeliveryAddress, OrderDate

Note: A customer may purchase many different items in a single order.

Draw the full ER diagram including a linked-entity OrderProduct for the many-to-many relationship between the ORDERS and PRODUCT entities.

You may use  https://www.draw.io/ or any other tools to construct the ER diagram.

### Question 3

The database contains the following information:

CUSTOMER: ID, Name, Email
PRODUCT: ID, Name, Description, UnitPrice
ORDERS: ID, CustID, ProductID, Quantity, DeliveryAddress, OrderDate

Note: A customer may purchase many different items in a single order.

Write the Table Descriptions for all the entities including the linked-entity, OrderProduct.

Use the following format:

TABLENAME (attribute1_, attribute2*, ...)

Follow the descriptors of the attributes given in the question exactly.

Place underscore (_)for the Primary Key (PK), and place asterisk (*) to denote the Foreign Key.

