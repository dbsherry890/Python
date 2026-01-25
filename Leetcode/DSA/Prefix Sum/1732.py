def largestAltitude(gain):
    cur_alt = 0
    max_alt = 0
    for i in range(len(gain)):
        cur_alt += gain[i]
        max_alt = max(cur_alt, max_alt)

    return max_alt


print(largestAltitude(gain=[-5, 1, 5, 0, -7]))
# should be 1
