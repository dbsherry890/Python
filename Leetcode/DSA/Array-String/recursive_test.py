def find_min(my_list, min=None):
    if not my_list:
        return min

    if not min or my_list[0] < min:
        min = my_list[0]
    return find_min(my_list[1:], min)


# print(len(lst))
find_min([42, 17, 2, -1, 67])


def is_palindrome(string):
    if len(string) <= 2:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


is_palindrome("abcba")


def multiplication(num_a, num_b):
    if num_a == 0 or num_b == 0:
        return 0

    return num_a + multiplication(num_a, num_b - 1)

# test cases
multiplication(3, 7)  # 21
# multiplication(5, 5) == 25
# multiplication(0, 4) == 0

