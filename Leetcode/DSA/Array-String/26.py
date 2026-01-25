def removeDuplicates(nums) -> int:
    a, b = 0, 1
    while b < len(nums):
        print(f"{a=}, {b=}, {nums=}")
        if nums[a] == nums[b]:
            b += 1
        else:
            nums[a+1] = nums[b]
            a += 1
    return a+1


print(removeDuplicates([1, 1, 2, 3, 3, 5]))
# should be 2.
# [1,2]

