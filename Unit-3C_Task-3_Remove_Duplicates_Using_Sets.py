
my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print("Original List:", my_list)
# Remove duplicates by converting to a set
my_set = set(my_list)
print("Set after removing duplicates:", my_set)
# Convert back to a list if needed
my_unique_list = list(my_set)
print("List after removing duplicates:", my_unique_list)