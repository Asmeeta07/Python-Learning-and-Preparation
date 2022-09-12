#unordered and unindexed

thisset={"one","many","few"}
print(thisset)

#access the elements one at a time of the set by for loop

for x in thisset:
    print(x)   #since this is unordered the values are thrown randomly

#checking if an item in the set

if "many" in thisset:
    print("yes, its many")

#or, by using in

print("many" in thisset)

#cannot change items in the set but can add item/items to the set

thisset.add("hundreds")
print(thisset)

thisset.update(["thousands","couples"])   #aware of the square brackets
print(thisset)



#get the length of the set

print(len(thisset))

#remove a elemt from the set

thisset.remove("couples")
print(thisset)

#remove the item using discard without any errors

thisset.discard("couples")
print(thisset)

#if we pop we donot know what items get pops

thisset.pop()
print(thisset)

#clear all the elements in the set

thisset.clear()
print(thisset)

#use empty set as constructors to make new set

thisset = (("honey","baby"))
print(thisset)

#throws error coz this delete the complete set
# del thisset
# print(thisset)

#other methods
#copy() -return a copy of the set
#difference() returns  set containing the difference between 2 or more sets
#difference_update()