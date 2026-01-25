arr = [5, 3, 9, 8, 2, 1, 4, 6, 7]

for i in range(len(arr)):
    min = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min]:
            min = j
    tmp = arr[i]
    arr[i] = arr[min]
    arr[min] = tmp

print(arr)
