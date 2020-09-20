def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # n is bigger than 1
    else:
        previous = 1
        sum = 1
        while n > 2:
            tmp = sum
            sum += previous
            n -= 1
            previous = tmp
        return sum


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # n is bigger than 1
    else:
        return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)


if __name__ == "__main__":
    for n in range(11):
        print(fibonacci_iterative(n), end=' ')
    print()
    for n in range(11):
        print(fibonacci_recursive(n), end=' ')
    print()

# 0 1 1 2 3 5 8 13 21 34 55
