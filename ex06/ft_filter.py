# print(filter.__doc__)
def main(func, iter):
    return [ x for x in iter if func(x) == True ]

if __name__ == "__main__":
    print(main(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))