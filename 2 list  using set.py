kllist1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
set_list2 = set(list2)
common_elements = [item for item in list1 if item in set_list2]

print("Common elements between the two lists are:", common_elements)
