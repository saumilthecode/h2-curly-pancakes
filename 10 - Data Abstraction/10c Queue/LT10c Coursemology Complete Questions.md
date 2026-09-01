# LT 10c - Queue ADT (for 2026)

- **Source URL:** https://yijc.coursemology.org/courses/3257/assessments/88736
- **Extraction date:** 2026-09-01 (Asia/Singapore)

## Learning outcomes and core skills

Learning Objectives
2.1.1 Illustrate the use of and implement the create, insert, and delete operations for stacks and queues
Core Skills
Understand the mechanics of a queue data structure
Write constructors, getters and modifiers for a queue ADT

Please download the lecture slides and watch the lecture videos before attempting the lecture training!

Queue ADT (7:15 min)

Here, we use Concrete Examples in a few of our questions to better understand the Queue concept.
Please feel free to post questions via the comment box tagged to the lecture video. Have fun!

## Question 1: FIFO

A queue is an Abstract Data Type (ADT) that adds and removes data in a First In First Out (FIFO) manner. It is an ordered collection of elements. Elements are removed in the same order in which they are added.

Starting with an empty queue, the following numbers:

                        4, 3, 2 and 1

are added into it, from left to right.

What value is the number at the head/front of the queue?

### Options

- 4
- 3
- 2
- 1

## Question 2: FIFO

Starting with an empty queue, the following elements:

                           5, (1, 2), True, "3" and [4]

are added into it, from left to right.

What is the element at the tail/end of the queue?

### Options

- (1, 2)
- "3"
- 3
- 4
- [4]
- 5
- True

## Question 3: enqueue and dequeue

There are two important operations that a queue must support: enqueue and dequeue.

To add items to the queue, we enqueue them at the back (tail) of the queue, and to get the first element from the queue, we dequeue it from the front (head) of the queue.



Which sequence(s) of enqueue and dequeue operations will result in the following queue (H: head, T: tail)?


                                            1   2   3   4

                                            H             T

### Options

- enqueue 4, enqueue 3,  enqueue 2, enqueue 1
- enqueue 1, enqueue 2,  enqueue 3, enqueue 4
- dequeue, enqueue 1, enqueue 2,  enqueue 3, enqueue 4
- enqueue 1, enqueue 1, enqueue 2,  enqueue 3, enqueue 4, dequeue
- enqueue 1, enqueue 2,  enqueue 3, enqueue 4, enqueue 4, dequeue 4

### Diagrams

![Diagram 1](data:image/png;base64,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)

## Question 4: Implement the Queue ADT

Now, let us implement the queue ADT.

A queue can be implemented using a list, where the first element in the list is at the front/head of the queue and the last element is at the tail of the queue.


Define a constructor make_empty_queue() that takes no arguments and returns an empty queue.


Define another constructor make_queue(seq) that takes in a sequence seq and returns a queue representation of the sequence where the first element is at the front of the queue and the last element in the sequence is at the end of the queue.

 Lastly, define the predicate function is_empty(queue) that returns True if the queue is empty and False otherwise.

### Template attachment

`template.py` (Coursemology download; submitted contents intentionally excluded.)

### Public test cases

```text
Expression	Expected	


is_empty1

	

True

	


is_empty2

	

False

	


is_empty3

	

False

	


s1

	

[]

	


s2

	

[2, 4, 5]

	


s3

	

[3, 5, 7, 8]

	


s4

	

['s', 't', 'r', 'i', 'n', 'g']
```

## Question 5: Modifying a queue

Write program codes to implement the modifiers enqueue(queue,item) and dequeue(queue).

enqueue(queue,item) adds the item at the back of the queue.
dequeue(queue) removes the first item from the queue and returns the removed item. It will return None if the queue is empty.

Note: enqueue() and dequeue() will modify the queue, they should not return a new queue.




The following constructors and predicate are provided:

make_empty_queue(), make_queue(seq) and is_empty(queue).

### Template attachment

`template.py` (Coursemology download; submitted contents intentionally excluded.)

### Public test cases

```text
Expression	Expected	


first

	

None

	


second

	

1

	


third

	

2

	


fourth

	

3
```

## Question 6: Added Functionalities

Write program codes for the following accessors and modifier:

accessor front(queue) returns the first element from a queue. It does not remove the first element in the queue.
accessor size(queue) returns the number of elements in the queue.
modifier clear(queue) removes all elements in the queue. It does not return a new empty queue.



The following constructors and predicate are provided:

make_empty_queue(), make_queue(seq) and is_empty(queue).

### Template attachment

`template.py` (Coursemology download; submitted contents intentionally excluded.)

### Public test cases

```text
Expression	Expected	


front1

	

None

	


front2

	

2

	


front3

	

None

	


size1

	

0

	


size2

	

3
```

## Question 7: Cafe queue

The following constructors, accessors and modifiers for the Queue ADT are provided:
(You do not need to submit code for these functions.)

make_empty_queue(): returns a new empty queue
make_queue(seq): returns a queue with elements in the sequence seq
enqueue(q, item): adds an item to queue q
dequeue(q): removes and returns the first item from the queue q
front(q): returns the first element in the queue q
size(q): returns the size of the queue q
clear(q): clears all elements in the queue q
Note: is_empty(q) is not provided in the Queue ADT



Write program codes, using the given functions above, to create a queue to monitor the customers in the queue at a cafe outlet:

1) construct an empty queue, my_queue

2) customer 'Jane' joins the queue

3) customer 'Asyraf' joins the queue

4) Cafe out of coffee. All customers left the queue.

5) customer 'Sam' joins the queue

6) customer  'Sally' joins the queue

7) the barista served a customer

8) customer 'Wen Jie' joins the queue

9) customer 'Penelope' joins the queue

10) customer 'Thor' joins the queue

11) the barista served a customer

12) customer 'Loki' joins the queue

13) the barista served a customer

14) the manager asked for the no. of customers in the queue; assign it to size1

15) the barista served a customer

16) customer 'Tony' joins the queue

17) customer 'Bruce' joins the queue

18) the barista served 2 customers

19) the manager asked for the no. of customers in the queue; assign it to size2



Note: You must use the methods given in the Queue ADT and do not break the abstraction!

### Template attachment

`template.py` (Coursemology download; submitted contents intentionally excluded.)

### Public test cases

```text
Expression	Expected	


size1

	

3

	


size2

	

2

	


my_queue

	

['Tony', 'Bruce']
```

## Question 8: Printer Queue ADT

The following constructors, accessors and modifiers for the Queue ADT are provided:
(You do not need to submit code for these functions.)

make_empty_queue(): returns a new empty queue
make_queue(seq): returns a queue with elements in the sequence seq
enqueue(q, item): adds an item to queue q
dequeue(q): removes and returns the first item from the queue q
front(q): returns the first element in the queue q
size(q): returns the size of the queue q
clear(q): clears all elements in the queue q
is_empty(q) returns True if the queue is empty, and False otherwise



A network printer uses a queue data structure to manage the printing jobs sent to the printer.


Write program codes to implement the Printer Queue ADT using the functions provided in the Queue ADT:

1) Constructor:

make_print_queue(): returns an empty print queue



2) Modifiers:

send_job(printq, job): adds a new print job job to the rear of the print queue printq
print_job(printq): prints the first job, removes it from the print queue printq and returns the filename of the printed document; returns None if the print queue is empty
cancel_job(printq, job): removes a particular print job job from the queue; returns None if the print job is not found. (Note: If the same print job appears more than once in the print queue, the modifier cancel_job() will only remove the first one found in the print queue.)
clear_all(printq): that removes all the print jobs in the print queue printq.



3) Accessors:

next_job(printq): returns the print job at the front of printq without removing it from the print queue
num_jobs(printq): returns the number of print jobs in the print queue printq
is_pq_empty(printq): returns True if print queue is empty; Otherwise, returns False.


A printer job is represented by the filename of the document to be printed, e.g. "phys quiz.doc".

### Template attachment

`template.py` (Coursemology download; submitted contents intentionally excluded.)

### Public test cases

```text
Expression	Expected	


empty1

	

True

	


size1

	

2

	


print1

	

"phys quiz.doc"

	


next1

	

"chem quiz.doc"
```

## Question 9: Print Queue ADT (Extension)

The following constructors, accessors and modifiers for the Queue ADT are provided:
(You do not need to submit code for these functions.)

make_empty_queue(): returns a new empty queue
make_queue(seq): returns a queue with elements in the sequence seq
enqueue(q, item): adds an item to queue q
dequeue(q): removes and returns the first item from the queue q
front(q): returns the first element in the queue q
size(q): returns the size of the queue q
clear(q): clears all elements in the queue q
is_empty(q) returns True if the queue is empty, and False otherwise



This question is an extension of the previous question for the Print Queue ADT.

For this question, the ink level of the printer is being monitored with a counter; it is initialised as 100 at the start when the ink cartridge is full. The counter will decrease by 1 unit for each print job.

When the counter decreases to 0, the print_job(printq) will display a message to prompt the user to replace the ink cartridge using the modifier replace_cart(printq) and the counter will be reset to 100.

Write program code to modify the Print Queue ADT written in the previous question:

modify make_print_queue() return a list storing the print queue and a counter.
>>> canon_printer = make_print_queue()
>>> canon_printer          #output: [[], 100]
>>> canon_printer[0]       #output: []   #this is an empty print queue
>>> canon_printer[1]       #output: 100  #the cartridge is full initially

Note: The following codes will send two print jobs to the printer:

>>> send_job(canon_printer, "phys quiz.doc")
>>> send_job(canon_printer, "maths quiz.doc")
>>> canon_printer

#output:  [["phys quiz.doc","maths quiz.doc"], 100]



modify print_job(printq) to handle the following 3 cases:
1. if the print queue printq is empty, return None.
2. if the counter in printq is 0,  display a message 'Please replace the empty ink cartridge.' to prompt the user to replace the ink cartridge and returns False. No print job will be dequeued.
3. if the counter is more than 0, print the first job, remove it from the print queue printq, return the filename of the printed document and decrease the counter by 1.



write program code for the additional modifier replace_cart(printq) to mimic the replacement of the ink cartridge by resetting the counter to 100.



modify/create the other assessors : send_job(printq, job), cancel_job(printq, job), clear_all(printq), next_job(printq), num_jobs(printq), is_pq_empty(printq) to work with the new definition of the print queue.

### Template attachment

`template.py` (Coursemology download; submitted contents intentionally excluded.)

### Public test cases

```text
Expression	Expected	


canon_printer

	

[['document 102', 'document 103', 'document 104', 'document 105'], 99]

	


empty1

	

True

	


size1

	

105

	


size2

	

5

	


next2

	

"document 101"

	


print2

	

False

	


replace_cart(canon_printer)

	

None

	


print3

	

"document 101"

	


next3

	

"document 102"
```

## Question 10: Playlist

A song playlist uses a Queue ADT.

For the songs to be played in a loop, after playing the first song, it will be dequeued and enqueued at the back of the playlist.

Using the Queue ADT, write program code for the function current_song(playlist, minutes) to return the song in the playlist that will be played after a specified duration indicated by minutes.

Assume that the songs in the playlist are played in a loop. The duration of each song is 4 minutes with no time lag between the songs. (i.e. If we start playing the first song at 0-min, the first song will end and start the second song at the 4-min mark; the second song will end and play the third song at the 8-min mark, ...)

Consider the following playlist:

jay_chou = ('silent', 'rainbow', 'nocturne', 'excuse') with 'silent' as the first song in the playlist.

When the playlist is played in a loop, the songs will be played in the following sequence:

'silent', 'rainbow', 'nocturne', 'excuse', 'silent', 'rainbow', 'nocturne', 'excuse', 'silent', 'rainbow', 'nocturne', 'excuse', and so on....

>>> current_song(jay_chou, 22)         #output: 'rainbow'

The song playing at 22-min will be 'rainbow'.



The following constructors, accessors and modifiers for the Queue ADT are provided:
(You do not need to submit code for these functions.)

make_empty_queue(): returns a new empty queue
make_queue(seq): returns a queue with elements in the sequence seq
enqueue(q, item): adds an item to queue q
dequeue(q): removes and returns the first item from the queue q
front(q): returns the first element in the queue q
size(q): returns the size of the queue q
clear(q): clears all elements in the queue q
Note: is_empty(q) is not provided in the Queue ADT



Note:

Do not modify the playlist jay_chou.
Do not run the test cases consecutively, run one at a time.

### Template attachment

`template.py` (Coursemology download; submitted contents intentionally excluded.)

### Public test cases

```text
Expression	Expected	


current_song(jay_chou, 3)

	

silent

	


current_song(jay_chou, 4)

	

rainbow

	


current_song(jay_chou, 4.1)

	

rainbow

	


current_song(jay_chou, 7.9)

	

rainbow

	


current_song(jay_chou, 22)

	

rainbow

	


current_song(jay_chou, 45)

	

excuse

	


current_song(jay_chou, 90)

	

nocturne
```

## Question 11: Pass-the-Bomb Game

The game Pass-the-Bomb requires two parameters, lst and n.

The simulation below shows the game being played with 10 players, tup = ('Player1', 'Player2' ... 'Player10'), and with n=2:

The game starts with Player1 holding the bomb and it does not explode. Player1 will pass the bomb to Player2 and it does not explode.
Since n=2, the bomb will explode when it is passed to Player3.
The game continues with Player4 and Player5 getting the bomb without exploding and explodes when passed to Player6.
The game continues with Player7 and subsequently explodes with Player9, ...
The last surviving player will be declared the winner.




Using the Queue ADT provided, write program code for the function who_wins(tup,n) that returns the last surviving player in the tuple of players tup for the Pass-the-Bomb game with the parameter n.

You should start by using the input tuple tup to populate a queue first.


The following constructors, accessors and modifiers for the Queue ADT are provided:
(You do not need to submit code for these functions.)

make_empty_queue(): returns a new empty queue
make_queue(seq): returns a queue with elements in the sequence seq
enqueue(q, item): adds an item to queue q
dequeue(q): removes and returns the first item from the queue q
front(q): returns the first element in the queue q
size(q): returns the size of the queue q
clear(q): clears all elements in the queue q
is_empty(q) returns True if queue is empty and False otherwise

### Diagrams

![Diagram 1](https://yijc.coursemology.org/attachments/d1da434e-2982-41ba-b439-fee85d054e6a)

### Template attachment

`template.py` (Coursemology download; submitted contents intentionally excluded.)

### Public test cases

```text
Expression	Expected	


who_wins(players1, 2)

	

'Player4'

	


who_wins(players2, 4)

	

'Player3'
```
