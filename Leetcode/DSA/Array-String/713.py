def numSubarrayProductLessThanK(nums, k: int) -> int:
    l = counter = 0
    curr = 1
    if k <= 1:
        return 0
    for r in range(len(nums)):
        curr *= nums[r]
        while curr >= k:
            curr //= nums[l]
            l += 1
        counter += r - l + 1

    return print(counter)


numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100)
