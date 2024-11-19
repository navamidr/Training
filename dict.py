thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) 
car["color"] = "white"
print(x) 

x=car.values()
print(x)

x=car.items()
print(x)

thisdict["year"]=2019
print(thisdict)

thisdict["color"]="red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

for i in thisdict:
    print(i)

for x in thisdict.keys():
    print(x)

for i in thisdict.values():
    print(i)

for i in thisdict.items():
    print(i)

mydict=thisdict.copy()
print(mydict)


#nested 
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)