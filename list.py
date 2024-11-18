thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

list = ["apple", "banana", "cherry"]
print(list[1])

lt=["apple", "banana", "cherry"]
lt[1] = "blackcurrant"
print(lt)

list.insert(3,"watermelon")
print(list)
list.append("orange")
print(list)
list.remove("banana")
print(list)

#loop
thislist1 = ["apple", "banana", "cherry"]
for x in thislist1:
  print(x)

list1= ["apple", "banana", "cherry"]
i = 0
while i < len(list1):
  print(list1[i])
  i = i + 1

thislist2= ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist2.sort()
print(thislist2)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)