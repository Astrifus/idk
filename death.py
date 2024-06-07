import sys
import math
import random as rand
from random import randint

n = input('pick a number and ill tell you if it is prime\n')
x = 0
y = 0
n = int(n)
m = n-1
o = n-1

while m % 2 == 0:
    m = m/2

a = o/m
s = math.log2(a)
s = int(s)

for i in range(0,5):
    b = randint(2,n-2)
    x = (b**m) % n
    for i in range(0,s):
        y = (x**2) % n
if y ==1 and x != 1 and x!= o:
            print("not prime")
elif y != 1:
        print ("not prime")
else:
    print("probably prime")