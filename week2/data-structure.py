#1.  Create an empty list
my_list = []
print(my_list)
#2. Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#3.  Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print(my_list)
#4. Extend the list
my_list.extend([50, 60, 70])
print(my_list)
#5. Remove the last element
my_list.pop()
print(my_list)
#6.  Sort the list in ascending order
my_list.sort()
print(my_list)
#7.Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)