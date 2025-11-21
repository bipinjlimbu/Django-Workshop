#List
List = [10, 20, 30, 40, 50]
print("Original List:", List)
List.pop()
print("List after pop():", List)
List.remove(20)
print("List after remove():", List)
List.append(60)
print("List after append():", List)
List.insert(2, 25)
print("List after insert():", List)
List.sort()
print("List after sort():", List)
List.reverse()
print("List after reverse():", List)
print("Length of List is:", len(List))

#Tuple
myTuple = []
Tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", Tuple)
print("Length of Tuple is:", len(Tuple))
print("Index of 30 in Tuple is:", Tuple.index(30))
print("Count of 20 in Tuple is:", Tuple.count(20))

#Appending elements from Tuple to a List and creating a new Tuple
for i in Tuple:
    myTuple.append(i)
print("New Tuple after appending elements from original Tuple:", myTuple)
myTuple.append(60)
Tuple = tuple(myTuple)
print("New Tuple:", Tuple)

#Set
mySet = {10, 20, 30, 40, 50}
print("Original Set:", mySet)
mySet.add(60)
print("Set after add():", mySet)
mySet.remove(20)
print("Set after remove():", mySet)
mySet.discard(100) #no error while removing non-existing element
print("Set after discard():", mySet)
yourSet = {40, 50, 60, 70, 80}
unionSet = mySet.union(yourSet)
print("Union of two Sets:", unionSet)
intersectionSet = mySet.intersection(yourSet)
print("Intersection of two Sets:", intersectionSet)