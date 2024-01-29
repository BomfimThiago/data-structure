def odd_numbers_until_100():
    for i in range(1, 100, 2):
        yield i


def fibonacci_generator(n):
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


if __name__ == "__main__":
    for i in odd_numbers_until_100():
        print(i)

    for i in fibonacci_generator(10):
        print(i)
