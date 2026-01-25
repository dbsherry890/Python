def scoreOfString(s: str) -> int:
    lst = [ord(x) for x in s]
    i = 0
    j = 1
    answer = 0
    while j < len(lst):
        answer += abs(lst[j] - lst[i])
        j += 1
        i += 1

    return answer


print(scoreOfString(s="hello"))
# should be 13
