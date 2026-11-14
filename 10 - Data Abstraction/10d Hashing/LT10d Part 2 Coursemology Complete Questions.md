# LT10d About Hashing (Part 2)

- **Source URL:** https://yijc.coursemology.org/courses/3257/assessments/88705
- **Extraction date:** 2026-09-01 (Asia/Singapore)

## Learning outcomes and core skills

Module 2: Data Structures and Algorithms

Implement hash table search.
Explain the operation of a hash table using suitable examples.
Apply an appropriate hash function to determine the storage location of a key.
Explain and apply collision resolution techniques (e.g. linear probing).
Trace insertion, search and retrieval operations in a hash table.
Compare the efficiency of hash table search with linear search and binary search using Big-O notation where appropriate.
Core Skills:
3. Write program code to create, initialize and populate a Hash Table using the Hash Function.
4. Use Separate Chain or Open Hashing to resolve Collisions.
5. Write program code to search for an item in a Hash Table. 

 

Please download the lecture slides and watch the lecture videos before attempting the lecture training!

Part 2 : About Hash Table (without Collision Resolution) - 11:36 min

Here, we use Dual Coding to experience facing the problem.
Please feel free to post questions via the comment box tagged to the lecture video. Have fun!

## Question 1: Hash Function and Hash Table (without Collision Resolution)

Refer to slide 2 to 6, write the following functions:

1. hash(string) : to compute the hash value without applying the modulo

2. init_table(n) : to create and initialize an empty Hash Table of size n

3. hashtable(seq) : to perform the following:

create and initialize an empty Hash Table of size n where n is the size of the array seq.
compute the hash value with modulo n, for each of the data in the array seq.
using the computed hash value, i, as the index, store the data in the Hash Table if it is empty at the index position, i.

### Template attachment

`template.py` (Coursemology download; submitted contents intentionally excluded.)

### Public test cases

```text
Expression	Expected	


data_table

	

['abcd', 'adcb', 'cdab', 'dbac', 'acbd']
```

## Question 2: Search a Hash Table (without Collision Resolution)

Refer to LT10d About Hashing (slide 9)

Write the Python code for the Search function for Hash Table (without Collision Resolution).



Note : The codes for the Hash Function and Table are provided in this question.

### Template attachment

`template.py` (Coursemology download; submitted contents intentionally excluded.)

### Public test cases

```text
Expression	Expected	


search(data_table, 'cdab') 

	

True

	


search(data_table, 'bdca')

	

False
```

## Question 3: [Application]: Hash Function and Table (without Collision)

- This is a new question (from past year A Level paper) unrelated to the previous question.
- You should start from scratch with no prior code provided. Coursemology will not have code from previous questions.
- Answer this question with these in mind.



[2018 YIJC Promo Exam Task 3.1 & 3.2]

In a supermarket, the grocery inventory database stores the item names in a hash table for easy search and retrieval.

The hash function uses the ASCII values of the characters in the item name to compute its hash value.

The following is an example of the computation:

ord('i')= 105           ord('n')= 110          ord('o')= 111



Task 3.1: Write a program code for this hash function.





keys1  provided is a sequence containing the name of the items.

Task 3.2: Write a program code hash_table(seq) to:

·       store the sequence of item names into a hash table of size 13. You should use the hash function, written in Task 3.1, to generate the indices.

·       return the hash table



You may assume that there is no collision and the hash function will generate different values for different item names.



Note : An empty string '' is used to denote a empty cell in the hash table.

### Diagrams

![Diagram 1](Coursemology%20question%20assets/diagram-004.png)

### Template attachment

`template.py` (Coursemology download; submitted contents intentionally excluded.)

### Public test cases

```text
Expression	Expected	


hash('onion')

	

1

	


hash('tomato')

	

10

	


hash('cabbage')

	

4

	


table1

	

['okra', 'onion', '', '', 'cabbage', '', 'mushroom', 'salt', '', 'cucumber', 'tomato', 'banana', 'orange']
```
