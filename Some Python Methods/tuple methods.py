thistuple = ("success","money","money","fame","fame")

#indexing a tuple
print(thistuple[2])

#changing the value of an element- cannot chneg- thrwing an error
# thistuple[1] = "popularity"
# print(thistuple)

#loop through a tuple - prints them one after another, not in a lis/tuple
for x in thistuple:
    print(x)

if "money" in thistuple:
    print('it is present')

print(len(thistuple))

#cannot add, append,remove a tuple
#but can delete the tuple completely

# del thistuple
# print(thistuple)

#using the thistuple() as an constructor to create a new tuple
thisnewtuple=(("humility","gratitute","acceptance"))
print(thisnewtuple)

#count() method to return the number of an item occurs
print(thistuple.count("fame"))

#index( searches the tuple for a value and returns the index of the value
print(thisnewtuple.index("humility"))

#returns the first location it finds
print(thistuple.index("fame"))

#returns an error if not present
#print(thistuple.index("no money"))