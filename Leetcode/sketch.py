from typing import List


class Solution:
    def twoSum(self, nums=[2, 7, 11, 15], target=18):
        hashMap = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[val] = i

    def containsNearbyDuplicate(self, nums=[1, 2, 3, 1], k=3) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i

        return False

    def isIsomorphic(self, s="egg", t="add") -> bool:
        char_index_s = {}
        char_index_t = {}

        for i in range(len(s)):
            if s[i] not in char_index_s:
                char_index_s[s[i]] = i

            if t[i] not in char_index_t:
                char_index_t[t[i]] = i

            if char_index_s[s[i]] != char_index_t[t[i]]:
                return False

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum())  # Output: [1, 2]
    # print(sol.isIsomorphic())
