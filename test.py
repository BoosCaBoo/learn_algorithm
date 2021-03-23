# 1
def func(number):
    return number[0]


# log n
def func2(n):
    if n <= 1:
        return
    else:
        print(n)
        func2(n/2)


# 0
def func3(numbers):
    for num in numbers:
        print(num)


# n * log(n)
def func4(n):
    for i in range(int(n)):
        print(i, end=' ')
    print()

    if n <= 1:
        return
    func4(n/2)


# n ** 2
def func5(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()


# 安定ソート stable sort ソート判定において同一とあると判断された入力データの順序がソート後も変わらない

l = [(1, 'Mike'), (5, 'Rina'), (2, 'Bill'), (4, 'emily'), (2, 'June')]


def stable(l):
    l[1], l[2] = l[2], l[1]
    l[2], l[4] = l[4], l[2]
    return l


l2 = [(1, 'Mike'), (5, 'Rina'), (2, 'Bill'), (4, 'emily'), (2, 'June')]


def unstable(l2):
    l[1], l[4] = l[4], l[1]
    return l2
