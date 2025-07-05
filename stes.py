#sets can add and remove but dont allow duplicates

my_set = {1, 2, 3, 4, 5}

print(my_set) 

#adding to a set

my_set.add (6)

print(my_set) 

#remove a from set

my_set.remove (3)

print(my_set) 

#operations in sest

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#union adds sets together and removes duplicates

union_set = set1 .union(set2)
print(union_set)

#intersection (finding common elment in two sets)

inter_set = set1.intersection(set2)
print(inter_set)

#difference finds elements present in one but not the other

diff_set = set1.difference(set2)
print(diff_set)