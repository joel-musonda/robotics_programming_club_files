#Lists

names = ["Alice", "Bob", "Charlie"]

#accessing list items
print(names[0]) #this will print "Alice"
print(names[0:2]) #this will print ["Alice", "Bob"]


#modifying list items

names[1] = "David" #this will change "Bob" to "David"
names.extend(["Eve", "Frank"]) #this will add "Eve" and "Frank" to the end of the list
names.insert(1, "Grace") #this will insert "Grace" at index 1
names.remove("Charlie") #this will remove "Charlie" from the list
names.pop() #this will remove the last item from the list
names.clear() #this will remove all items from the list
names.append("Heidi") #this will add "Heidi" to the end of the list
names.sort() #this will sort the list in alphabetical order
names.reverse() #this will reverse the order of the list



#list comprehension

green = ["Kabwe", "Rebecca", "Lisa", "penjani", "michael" , "Martha", "Micah" ]
blue = []

for name in green:
    if name.startswith("M"):
        blue.append(name)
        green.remove(name)
        print(blue)