nested_list = [[1, 2, 3], [4, 5], [6, 7]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)

list = []
for sublist in nested_list:
    for item in sublist:
        list.append(item)
print(list)
