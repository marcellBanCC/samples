def min(x, y):
    if x < y:
        return x
    else:
        return y


# print(min(9, 9))


def max(values_list):
    max_value = values_list[0]
    for element in values_list[1:]:
        if element > max_value:
            max_value = element

    return max_value


# print(max([-12, -3, -45, -6, -32]))


def len(values_list):
    length = 0
    for _ in values_list:
        length += 1
    return length


# 2 * 3
# 2 + 2 * 2
# 2 + 2 + 2 * 1
# 2 + 2 + 2 + 2 * 0


def multiply(x, y):
    if y < 0:
        y = -y
        x = -x
    total = x
    while y != 1:
        total += x
        y -= 1
    return total


# print(multiply(-2, -3))


def pow(x, y):
    pass


def divmod(x, y):
    pass
