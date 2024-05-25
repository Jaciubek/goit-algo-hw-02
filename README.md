# goit-algo-hw-02

Today, you will practice skills of correct application of data structures for specific tasks, which is extremely important for developing efficient algorithms and programs.

What are the key data structures you need to use?

a queue (the Queue class from the queue module), which will allow you to simulate the system of processing applications in a service center;
a two-way queue (queue from the collections module) to create a program that checks whether a given string is a palindrome.
Thus, the homework will consist of two independent tasks.

Task 1

You are to develop a program that simulates the acceptance and processing of requests: the program should automatically generate new requests (identified by a unique number or other data), add them to the queue, and then sequentially remove them from the queue for "processing", thus simulating the work of a service center.

Here is the pseudo-code for a task using a queue (Queue from the queue module in Python) for a request processing system:

import Queue

Create a queue of applications
queue = Queue()

The generate_request() function:
    Create a new request
    Add a request to the queue

Function process_request():
    If the queue is not empty:
        Remove a request from the queue
        Process the request
    Otherwise:
        Display a message that the queue is empty

The main cycle of the program:
    Until the user exits the application:
        Execute generate_request() to create new requests
        Execute process_request() to process requests

This pseudocode uses two main functions: generate_request(), which generates new requests and adds them to the queue, and process_request(), which processes requests by removing them from the queue. The main program loop performs these functions, simulating a constant flow of new requests and their processing.

Task 2

Your task is to develop a function that takes a string as input, adds all its characters to a two-way queue (deque from the collections module in Python), and then compares the characters at both ends of the queue to determine if the string is a palindrome. The program should correctly handle both even and odd-numbered strings and be case and space-insensitive.