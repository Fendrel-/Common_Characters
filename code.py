"""
Common Characters - Code Adventure

INTRODUCTION: 

Lets take a look at two strings and see if we can count the number of 
commmon characters using some Python. This sounds like a 
super easy task, but appearances can be deceiving. There is actually 
a lot more going on in an operation like this than it first seems. Let's
take a close look.


INSTRUCTIONS:

Create the logic for the function called common_characters. This function 
will take 2 strings as arguments, string1 and string2.

Your job is to check both strings for common characters and return the 
total number of common characters found. But keep in mind that once a 
character is found to be common, it can't be used in a second pair of 
common characters. So you could say we're looking for the total number 
of UNIQUE common characters.

So that:

  `common_characters('abcd', 'aabbcc') == 3;`


Here the strings have 3 common characters: one `a`, one `b`, and one `c`.
  

There are many ways to accomplish this. It can be done with conditionals, 
counters and recursion. It can be done with a loop, a simple search, and 
a counter. So feel free to experiment and explore. As is so often the case 
with code, there isn't just one right answer.


There are a number of steps to actually accomplishing this, so it can be 
helpful to begin by writing code comments that describe each individual 
step that your function should accomplish.

If you get stuck, reach out on the #code-adv-discuss channel. There's no 
shame in getting stuck. It happens to us all.  :)


TO RUN THE TESTS:
type the command below into the console and press enter.

  python code.py

"""

def common_characters(string1, string2):
    return 1 # fix me


if __name__ == '__main__':
    print("Test your code by running: 'python test.py' in the console")
