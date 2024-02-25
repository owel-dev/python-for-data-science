import sys


def main():
    """
    숫자를 받아 짝수인지 홀수인지 판별하여 출력합니다.

    Parameters:
    x (int): number

    Returns:
    y (str): "I'm Even. or I'm Odd."

    Example:
    >>> python3 whatis.py 12
    I'm Even
    """
    try:
        if len(sys.argv) == 1:
            return

        assert 2 == len(sys.argv), 'more than one argument is provided'
        num = int(sys.argv[1])

        if (num % 2 == 0):
            print("I'm Even.")
            return
        print("I'm Odd.")

    except AssertionError as error:
        print('AssertionError:', error)
    except ValueError:
        print('AssertionError: argument is not an integer')


if __name__ == "__main__":
    main()
