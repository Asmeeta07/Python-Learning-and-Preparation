# print("Hello")
#
# import keyword
# print(keyword.kwlist)

# for loop
thislist=["hair","nose","eyes"]
# for x in thislist:
#     print(x)

#if loop
if "hair" in thislist:
    print('yes, it is present')
    #find the length of the list
    print(len(thislist))

#add an element to the end of the list
thislist.append("mouth")
print(thislist)

#add an element at a particular position
thislist.insert(1,"hands")
print(thislist)

#remove an item from the list
thislist.remove("eyes")
print(thislist)

#pop method removes from a specific place or last item if not specified
thislist.pop(2)
print(thislist)

#del keyword removes from the specific index
del thislist[1]
print(thislist)

# #comppletely delete the list
# del thislist
# print(thislist)

#clear method empties the list
thislist.clear()
print(thislist)
#a list can be in empty state
#the list() constructor to make a new list

thislist = list(("apple","banana","cherry"))
print(thislist)

thislist.reverse()
print(thislist)

#sort the list in ascending order
thislist.sort()
print(thislist)