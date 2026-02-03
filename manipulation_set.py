
# Sets are mutable and unordered

my_set = {1,2,3,4,5,6}
print(my_set)

my_set.add(7)
print(my_set)

my_set.add(7) #you add element If that is already in the set, only one will be kept. In this case, we already have the number 5 in the set
print(my_set)

my_set.remove(7) # you can also do discard()
print(my_set)

#the defferent betweeen discard and remove The .remove() method will raise a KeyError if the element is not found, while the .discard() method will not:

my_set.clear()
print(my_set) #remove all the element from the set 


my_set = {1,2,3,4,5,6}
your_set = {2,3,4,6}

print(your_set.issuperset(my_set)) #False
print(my_set.issubset(your_set)) #False
print(my_set.isdisjoint(your_set)) # False  , The .isdisjoint() method checks if two sets are disjoint, which means they don't have any elements in common. In this case, that's False because my_set and your_set do have common elements – 2, 3, and 4
my_set | your_set # {1,2,3,4,5,6} , The union operator | returns a new set with all the elements from both sets
my_set & your_set # {2,3,4,6} , The intersection operator & returns a new set with only the elements that the sets have in common
my_set - your_set # {1,5} , The difference operator - returns a new set with the elements of the first set that are not in the other sets. In this example, the numbers 1 and 5 are in my_set but NOT in your_set
my_set ^ your_set # {1,5,6} , The symmetric difference operator ^ returns a new set with the elements that are either in the first or the second set, but not both. In this case, 1 and 5 are in my_set but not in your_set, so they are included. And the number 6 is in your_set but not in my_set, so it's included as well
my_set -= your_set
print(my_set) # {1,5}
print(6 in my_set) #False
print(1 in my_set) #True



