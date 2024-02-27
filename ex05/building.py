import sys


def main():
    """
    문자열을 받아 문자열을 구성하는 문자들의 속성별 갯수를 출력합니다.

    Example:
    $> python building.py "Python 3.0, released in 2008,
    was a major revision that is not completely backwardcompatible with
    earlier versions.
    Python 2 was discontinued with version 2.7.18 in 2020."
    The text contains 171 characters:
    2 upper letters
    121 lower letters
    8 punctuation marks
    25 spaces
    15 digits
    """
    if len(sys.argv) == 1:
        return
    try:
        assert len(sys.argv) == 2, 'more than one argument is provided'
    except AssertionError as error:
        print(error)
        return
    string = sys.argv[1]
    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0
    digit_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            punct_count += 1
    print(f'{upper_count} upper letters')
    print(f'{lower_count} lower letters')
    print(f'{punct_count} punctuation marks')
    print(f'{space_count} spaces')
    print(f'{digit_count} digits')


if __name__ == "__main__":
    main()
