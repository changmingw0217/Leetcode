import sys

maxint = 2147483647
minint = -2147483648


def reverse1(x: int) -> int:
    if x > 0:
        li = list(str(x))
        li.reverse()

        re = ""
        for i in li:
            re += i

        print(int(re))

    else:
        x = - x
        li = list(str(x))
        li.reverse()

        re = ""
        for i in li:
            re += i

        print(-int(re))


def reverse(x):
    result = 0
    while x != 0:
        pop = x % 10
        print(pop)
        x = x // 10
        print(x)
        result = result * 10 + pop
        print(result)

    print(result)

reverse(123)
