# comp@com 2

# Python–SQLite Data Retrieval

- A Python program must first establish the standard database connection and cursor before executing SQL commands; retrieved database content can then be processed in Python rather than checked manually through DB Browser.
- Use `fetchone()` when a query is expected to return one record, such as selecting all fields from a product table where `ID = 1`. The returned item’s data type should be inspected carefully rather than assumed to be a string or list.
- Use `fetchall()` when a query may return multiple records, such as selecting the entire customer table. The result is a collection of rows, described as a tuple of tuples, and should be iterated through one row at a time.
- Successfully fetching records allows later computation and manipulation, including summing values, calculating averages, and performing other processing in Python.
- Queries are not limited to one table. Advanced SQL can retrieve data from multiple tables by linking primary and foreign keys and applying appropriate conditions.
- Slides 20 and 21 were identified as important practice material: slide 20 covers `fetchone()` and `fetchall()`, while slide 21 provides query practice even though the questions are not submitted.

# Primary Keys and Indexing

- A primary key is a field, or combination of fields, whose values uniquely identify a specific record. Answers should use the term “record” rather than vague descriptions such as “specific data” or “row information.”
- A primary key can be a single field when that field is inherently unique, such as an identity-card number. It can also be a composite primary key when several fields are required to distinguish records, such as an identity-card number combined with a withdrawal date.
- Composite primary keys are valid but may make indexing and retrieval slower because multiple fields must be handled together.
- The instructor explained that database systems maintain indexes associated with primary keys to support efficient searching. Sorted or indexed data enables binary-search-style retrieval rather than slower linear searching.
- Primary-key values must not be null because the field must identify and support retrieval of every record. A blank primary key is invalid conceptually and would be marked wrong in an assessment even if the classroom software accepts it.
- SQLite or DB Browser may allow a text primary key to be omitted without displaying an error because SQLite does not strictly enforce this constraint in the demonstrated case. This permissive behavior should not be treated as correct database design; other DBMS products enforce primary-key and `NOT NULL` rules more strictly.

# Auto-Increment Behavior

- Two table designs were compared: one with an integer primary key but no explicit `AUTOINCREMENT`, and another whose integer primary key was explicitly defined with `AUTOINCREMENT`.
- SQLite may still generate sequential integer IDs when an ID is omitted from a table that does not explicitly use `AUTOINCREMENT`. Although this appears convenient, relying on that implicit behavior was identified as poor practice because it does not provide the same protection against ID reuse.
- In a table defined with `AUTOINCREMENT`, an explicit ID may still be inserted manually. For example, after automatically generating IDs 1 and 2, ID 5 can be supplied directly.
- After the manual insertion of ID 5, subsequent omitted IDs were generated as 6, 7, and 8. The demonstration showed that automatic numbering continues from the previously used sequence rather than reverting to 3.
- Auto-increment is appropriate for integer fields, not text fields such as identity-card numbers. Incrementing a text value has no meaningful numeric sequence.
- The key distinction is not simply whether SQLite can generate IDs in both designs; it is whether the system preserves a reliable record of previously used IDs and prevents deleted identifiers from being recycled.

# Deleted IDs and Identifier Reuse

- In the table without explicit `AUTOINCREMENT`, deleting the last record with ID 6 and then inserting new records caused ID 6 to be reused for a different record. Later records received IDs 7 and 8.
- Reusing a deleted ID is dangerous because the same identifier can refer to two different entities over time. A request to update “record 6,” for example, could be interpreted as referring either to the deleted historical record or the new record that inherited ID 6.
- Once an identifier has been assigned, it should remain associated with its original entity even after that entity is deleted. The deleted identifier should therefore be discarded rather than recycled.
- In the explicitly auto-incrementing table, ID 8 was deleted, but subsequent inserts received IDs 9 and 10. ID 8 was not reused.
- This behavior implies that SQLite maintains sequence information outside the visible table and remembers the highest previously allocated auto-increment value even after its record has been removed.
- Differences in table definitions can explain why two students appear to insert the same records but receive different IDs. Understanding the mechanism is important for debugging and for designing databases deliberately rather than merely following syntax.

# Foreign Keys, Deletion, and DBMS Constraints

- Foreign keys preserve referential integrity between related tables such as Product, Customer, and Order. A product or customer referenced by an order should not be deleted while the dependent order still exists.
- Products that have never been referenced by an order may be deleted without issue. Products already used in an order may trigger a constraint error because deleting them would leave the order referring to nonexistent data.
- It may be possible to create an order table while omitting its foreign-key declarations, but doing so removes the protection that prevents invalid deletions and broken relationships.
- A DBMS does more than store tables and records: it enforces rules governing primary keys, foreign keys, insertion, updates, deletion, naming, and other constraints. Different products, including Oracle, Microsoft Access, and SQLite-based tools, vary in how strictly and comprehensively they enforce these rules.
- Field names should be single identifiers without spaces. Multiword names should use camel case, such as `myName`, or underscores, such as `my_name`; hyphens should not be used.
- Reliable database administration requires conceptual mastery because mistakes can affect connected operations such as sales, inventory, finance, warehouse records, and delivery orders. Understanding constraints enables a developer or database manager to diagnose inconsistent outputs and design for a specific purpose.

# Learning Resources and AI Guidance

- Students were instructed to organize downloaded PDFs and other materials into subject-specific folders rather than leaving everything in the Downloads folder, particularly to avoid difficulty locating resources during future examination preparation.
- The current SLS study guide includes or will centralize the relevant questions, videos, and lesson resources. The SQL injection and race-condition videos were identified as content for the next lesson.
- A class OneNote had not yet been created because its structure was still being decided. Once available, it is intended to centralize PDFs, study guides, instructions, and links so students do not always need to search through SLS.
- AI should be used for an explicit purpose rather than applied indiscriminately. Appropriate examples included brainstorming activity ideas, searching and summarizing information, generating a first draft, and critiquing or evaluating student-created work.
- A first AI-generated draft should be treated as a starting point, not a final submission. The example given was providing the intended points for a thank-you card, reviewing the generated wording, and then writing the actual card personally.
- AI can critique existing work by identifying missing details, unclear transitions, weak language, or areas requiring elaboration. It can also assist with production tasks such as voice-over replacement, chaptering, and summarization.
- Some activities require genuine personal input and should involve no AI. Students should ask both “When should AI be used?” and “What specific purpose is it serving?” before using it in computing or other subjects.

# Next Steps

- Students must complete all C5A basic SQL and C5B Python-with-SQL work, with particular attention to the retrieval exercises involving `fetchone()`, `fetchall()`, and query practice from slides 20 and 21.
- Students must finish the current SLS/SRS concept-clarification questions, mark the activity complete, and submit or finalize it as directed; the remaining class time was allocated for this work.
- Students must return to the Cosmology materials and complete the outstanding C5A work after finishing the SLS activity.
- Students should retain notes on primary keys, null restrictions, integer auto-increment behavior, deleted-ID reuse, and foreign-key deletion constraints because these concepts are needed to explain and debug differing database outputs.
- The teacher committed to making the PDF slides available through the learning resources and indicated that the study guide was being placed at the end of the SLS activity after the questions.
- The next lesson will cover race conditions and SQL injection using the videos already identified in the study guide.
