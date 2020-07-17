import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

bst_name_1 = BSTNode(names_1[0])

# bst_name_2 = BSTNode(names_2[0])

for name in names_1:
    bst_name_1.insert(name)

# for name in names_2:
#     bst_name_2.insert(name)



duplicates = []  # Return the list of duplicates in this data structure
# containing = if bst_names_2.contains():
# what I want:
# for each node in list 2
# bst_names_1.contains(names_2 value)
# bst_name_2.for_each(bst_name_1.contains)


# bst_name_1.for_each(bst_name_2.contains)
# Replace the nested for loops below with your improvements

for name_2 in names_2:
    if bst_name_1.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
