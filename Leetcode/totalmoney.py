def totalMoney(n: int) -> int:
    res = 0
    monday = 1

    while n > 0:
        for day in range(min(n, 7)):
            res += monday + day
        n -= 7
        monday += 1

    return res


totalMoney(10)
