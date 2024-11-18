i = 1
while i < 6:
  print(i)
  i += 1

#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruit = ["apple", "banana", "cherry"]
for x in fruit:
  print(x) 
  if x == "banana":
    break
  
fruitsloop = ["apple", "banana", "cherry"]
for x in fruitsloop:
  if x == "banana":
    continue
  print(x)
