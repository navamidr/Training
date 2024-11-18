thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


#dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x=thisdict.get("model")
print(x)