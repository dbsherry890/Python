def maxVowels(s: str, k: int) -> int:
    cur_count = 0
    n = len(s)
    vowels = "aeiou"

    # make the window
    for i in range(k):
        if s[i] in vowels:
            cur_count += 1
    cur_max = cur_count

    for i in range(k, n):
        if s[i] in vowels:
            cur_count += 1
        if s[i-k] in vowels:
            cur_count -= 1
        cur_max = max(cur_max, cur_count)

    return cur_max


print(maxVowels(s="abciiidef", k=3))
