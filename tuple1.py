thistuple = ("apple", "banana", "cherry")
print(thistuple)

mytuple=("apple","banana","cherry","apple",)
print(mytuple)

print(type(mytuple))

tuple1=("apple",True,45,"true")
print(tuple1)
print(tuple1[1])


thistuple1= ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple1)
print(thistuple1[2:5])
print(thistuple1[-1])
print(thistuple1[-4:-1])

x = ("apple", "banana", "cherry")
print(x)
y=list(x)
print(type(y))
y.append("orange")
x=tuple(y)
print(type(x))
print(x)

#for loop

x = ("apple", "banana", "cherry")
for i in range(len(x)):
    print(x)
    print(x[2])

x = ("apple", "banana", "cherry")
i = 0
while i < len(x):
  print(x[i])
  i = i + 1

#join
tuple1=("a","b","c")
tuple2=(1,2,3,4)
tuple3=tuple1+tuple2
print(tuple3)
tuple4=tuple2+tuple1
print(tuple4)
mytuple=tuple1*2
print(mytuple)

