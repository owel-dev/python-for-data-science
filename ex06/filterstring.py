import sys


def ft_filter(func, iter):
    return [x for x in iter if func(x) is True]


def main():
    try:
        assert len(sys.argv) == 3
        length = int(sys.argv[2])

        splits = sys.argv[1].split()
        ret = ft_filter(lambda x: len(x) > length, splits)
        print(ret)
    except (AssertionError, ValueError):
        print('AssertionError: the arguments are bad')
        return 1


if __name__ == "__main__":
    main()
