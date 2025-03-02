#1
from functools import reduce
import time


def mult(nums):
    return reduce(lambda x, y: x * y, nums)

nums = [1, 2, 3, 4]
print(mult(nums))

#2
def count(s):
    up = sum(1 for char in s if char.isupper())
    lo = sum(1 for char in s if char.islower())
    
    return up, lo


s = "Hello World!"
up, lo = count(s)
print("Upper:", up)
print("LOwer:", lo)

#3 
def pali(s):
    return s == s[::-1]
    
ss = input()
if(pali(ss)):
    print("YES")
else:
    print("NO")

#4
import math
def root(num):
    
    return math.sqrt(num)


nan = int(input())
time = int(input())
numroot = root(nan)
print(f"Square root of {nan} after {time} miliseconds is {numroot}")

#5

def all_true(t):
    return all(t)  #если все элменты тру

t1 = (1, 0, 1)
t2 = (True, False, False)
t3 = (1, 1, True)
print(all_true(t1))
print(all_true(t2))
print(all_true(t3))
