* 0x01. Python - if/else, loops, functions

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

Why Python programming is awesome
Why indentation is so important in Python
How to use the if, if ... else statements
How to use comments
How to affect values to variables
How to use the while and for loops
How is Python’s for different from C‘s?
How to use the break and continues statements
How to use else clauses on loops
What does the pass statement do, and when to use it
How to use range
What is a function and how do you use functions
What does return a function that does not use any return statement
Scope of variables
What’s a traceback
What are the arithmetic operators and how to use them

Tasks
0. Positive anything is better than negative nothing

1. The last digit

2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game

3. When I was having that alphabet soup, I never thought that it would pay off


0x01. Python - if/else, loops, functions
Python
 By: Guillaume
 Weight: 1
 Project will start Aug 8, 2023 6:00 AM, must end by Aug 9, 2023 6:00 AM
 Checker was released at Aug 8, 2023 12:00 PM
 An auto review will be launched at the deadline


Resources
Read or watch:

More Control Flow Tools (Read until “4.6. Defining Functions” included)
IndentationError
How To Use String Formatters in Python 3
Learn to Program
Learn to Program 2 : Looping
Pycodestyle – Style Guide for Python Code
man or help:

python3
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
Why indentation is so important in Python
How to use the if, if ... else statements
How to use comments
How to affect values to variables
How to use the while and for loops
How is Python’s for different from C‘s?
How to use the break and continues statements
How to use else clauses on loops
What does the pass statement do, and when to use it
How to use range
What is a function and how do you use functions
What does return a function that does not use any return statement
Scope of variables
What’s a traceback
What are the arithmetic operators and how to use them
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
C Scripts
Allowed editors: vi, vim, emacs
All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
All your files should end with a new line
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
You are not allowed to use global variables
No more than 5 functions per file
In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
The prototypes of all your functions should be included in your header file called lists.h
Don’t forget to push your header file
All your header files should be include guarded
More Info
Note: you do not need to understand lists yet.

Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Positive anything is better than negative nothing
mandatory
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

You can find the source code here
The variable number will store a different value every time you will run this program
You don’t have to understand what import, random. randint do. Please do not touch this code
The output of the program should be:
The number, followed by
if the number is greater than 0: is positive
if the number is 0: is zero
if the number is less than 0: is negative
followed by a new line
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
5 is positive
guillaume@ubuntu:~/0x01$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x01-python-if_else_loops_functions
File: 0-positive_or_negative.py
   
1. The last digit
(mandatory)
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
(mandatory)
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
   
3. When I was having that alphabet soup, I never thought that it would pay off
(mandatory)
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

4. Hexadecimal printing
(mandatory)
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

5. 00...99
(mandatory)
Write a program that prints numbers from 0 to 99.

6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
(mandatory)
Write a program that prints all possible different combinations of two digits.

7. islower
(mandatory)
Write a function that checks for lowercase character.

8. To uppercase
(mandatory)
Write a function that prints a string in uppercase followed by a new line.

9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
(mandatory)
Write a function that prints the last digit of a number.

10. a + b
(mandatory)
Write a function that adds two integers and returns the result.

11. a ^ b
(mandatory)
Write a function that computes a to the power of b and return the value.

12. Fizz Buzz
(mandatory)
Write a function that prints the numbers from 1 to 100 separated by a space.

13. Insert in sorted linked list
(mandatory)

14. Smile in the mirror
#advanced
Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.

15. Remove at position
#advanced
Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).

16. ByteCode -> Python #2
#advanced
Write the Python function def magic_calculation(a, b, c):
