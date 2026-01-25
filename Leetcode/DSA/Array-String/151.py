class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.strip().split()
        # lst = s.split()
        # lst2 = [x for x in lst if x]
        return " ".join(lst[::-1])


print(Solution().reverseWords(s="a good   example"))
# should be "blue is sky the"
