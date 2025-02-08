mytuple = ("apple", "banana", "cherry")
#ordered,unchangable and allows duplicates

print(len(mytuple))

tuple1 = ("abc", 34, True, 40, "male")

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
  #the touple is unchangable,so Convert the tuple into a list, add "orange", and convert it back into a tuple:
  thistuple = ("apple", "banana", "cherry")
  y=list(thistuple)
  y.append("orange")
  thistouple=tuple(y)
  
  thistuple = ("apple", "banana", "cherry")
  y = ("orange",)
  thistuple += y

  print(thistuple)
