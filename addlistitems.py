thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#output is ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#output is ['apple', 'orange', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']