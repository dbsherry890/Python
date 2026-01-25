"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well."""


def mySqrt(x: int) -> int:
    if x in [0, 1]:
        return x

    start, end = 1, x
    while start <= end:
        mid = start + ((end - start) // 2)
        if mid == x // mid:
            return mid
        elif mid > x // mid:
            end = mid - 1
        else:
            start = mid + 1

    return end


print(mySqrt(34))  # 5
