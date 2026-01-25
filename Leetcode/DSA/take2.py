arr = [6, 4, 8, 9, 7, 2, 3, 5]

for i in range(len(arr)):
    min = i
    for j in range(i+1, len(arr)):
        if arr[min] > arr[j]:
            min = j

    tmp = arr[i]
    arr[i] = arr[min]
    arr[min] = tmp

print(arr)

# min 0, i 0, j 1
# if 6 < 4,
