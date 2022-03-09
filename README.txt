Allison Valdez
March 6, 2022

Module Information:
Module 6: Mathematical Sequences due March 07, 2022.

Approach:
(Part 1: Catalan)
I solved the first part of the assignment recursively. I included 1 argument for
my function (called shape), and my function is called by a main method. I
controlled for the base case of encountering if a shape has 1 (or unlikely 0
sides). If my base case is encountered then I will simply return 1. However, if
the recursive part of the code is triggered then: for every index within the
shape's side the output is updated by the multiplication of the catalan number
at a specific index by the previous catalan number. I will then return the
output to make sure that my catalan number is able to print the output. Within
my main method I created a for loop to print the required output 15 times.

(Part 2: Pascal)
I controled for the base case when either a 1 or a 0 is encountered for
the first row. The program will return a 1 if either base case is encountered.
Within my else clause: I created a local variable to control for my current row,
and the recusive call to calculate the previous row (based on my function
argument - 1). I then created a for loop to iterate based on the previous
row. My for loop was supposed to calculate the current row based on the
previous row's two indexes (the current index and the one prior). I then update
the current row by incrementing it. I return my output so that my main method is
able to gather the most up-to-date calculation. Within my main method I created
a for loop to print the required output 10 times.

Known Bugs:
My Pascal.py file contains a known bug since it does not run properly. While it
correctly loops 10 times, it does not properly calculate the Pascal Triangle
recursively. I included print statements and troubleshooted to the best of my
ability, but I cannot find where I went wrong.