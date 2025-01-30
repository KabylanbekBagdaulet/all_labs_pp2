thisset = {"apple", "banana", "cherry"}
print(thisset)
#2
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#3
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#4
set1 = {"abc", 34, True, 40, "male"}
#5
myset = {"apple", "banana", "cherry"}
print(type(myset))
#<class 'set'>

#ACCESS SET ITEMS

#1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#3
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#ADD ITEMS
#1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#REMOVE SET
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#3
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#4
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#LOOP SETS
#1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#JOIN SETS
#1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#3
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
#4
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
#5
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#6
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#7
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
#8
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
#9
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)







