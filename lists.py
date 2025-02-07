mylist = ["apple", "banana", "cherry"]
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#it allows duplicate values

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#output is 3
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#string,int and boolean data types
list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#output is <class 'list'>

#List is a collection which is ordered,changable and allows duplicates 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#['cherry','orange','kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#['apple','blackcurrant','watermelon','orange','kiwi','mango']