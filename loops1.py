a = 100
b = 368
if b > a:
  print("b is greater than a")


x=33
y=33
if x==y:
  print("x and y are equal")
elif x<y:
  print("y is greater than x")
else:
  print( "x is greater than y")


# while loops

i=0
while i<7:
  print(i)
  i+=1


#break
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

a=0
while a<3:
  print("hello")
  a+=1

i = 0
a = 'programmms'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
        
    print('Current Letter :', a[i])
    i += 1


# for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in range(2, 30, 3):
  print(x)

#nested for loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)