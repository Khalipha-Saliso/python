# changing lists

fruits = ["apple", "banana", "cherry"]

print(fruits[0])

fruits[1] = "blueberry"

print(fruits)

#adding and removing items in a list:

fruits = ["apple", "banana", "cherry"]

#add a value to our list:

fruits.append("kiwi")
print(fruits)

#to add in a certie position on the list

fruits.insert(1, "orange")
print(fruits)

#to remove an item off a list:

fruits.remove("banana")
print(fruits)

#sorting iteam using .sort method:

fruits.sort() #in decending order its .sort(revers=True)
print(fruits)