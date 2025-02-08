myset = {"apple", "banana", "cherry"}
#unorderd,unchangeable and doesnt allow duplicates
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#{'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#{True, 2, 'banana', 'cherry', 'apple'}
#True and 1 is considered the same value:

set1 = {"abc", 34, True, 40, "male"}

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
