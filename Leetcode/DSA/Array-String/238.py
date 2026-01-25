from typing import List

# unfinished


def productExceptSelf(nums: List[int]) -> List[int]:
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)
    for i in range(len(nums)):
        prefix[i] *= nums[i]
    for i in range(len(nums)-1, -1, -1):
        postfix[i] *= nums[i]
    return prefix, postfix


print(productExceptSelf(nums=[1, 2, 3, 4]))
# should be [24,12,8,6]
