"""
fizzbuzz.py
Author: Daniel
Credit: <list sources used, if any>

Assignment:

Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for 
the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.

We will use a variation of this test in which the last number of 
the series isn't necessarily 100, and the two numbers being tested 
for multiples aren't necessarily three and five. For example, your 
program should behave just like this:

How many numbers shall we print? 25
For multiples of what number shall we print 'Fizz'? 3
For multiples of what number shall we print 'Buzz'? 5
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
"""

numbers = input(" How many numbers shall we print? ")
Fizz = input(" For multiples of what number shall we print 'Fizz'? ")
Buzz = input(" For multiples of what number shall we print 'Buzz'? ")



b = int(Buzz)
f = int(Fizz)
n = int(numbers)+1
a = list(range(1,n))

x = list(range(1,n))
for i in x:
    if i%f == 0 and i%b == 0:
        a[i-1] = "FizzBuzz"
    elif i%f == 0:
        a[i-1] = "Fizz"
    elif i%b == 0:
        a[i-1] = "Buzz"
        

for i in a:
    print(i)
    
   
#for i in range(1,n):
#    print(i)

#USE FOR STATEMENTS
