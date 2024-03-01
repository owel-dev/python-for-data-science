# print(filter.__doc__)
def main(func, iter):
    return [x for x in iter if func(x) is True]


if __name__ == "__main__":
    arr = (1, 2, 3, 4, 5, 6, 8)
    print(main(lambda x: x % 2 == 0, arr))
    print(list(filter(lambda x: x % 2 == 0, arr)))
