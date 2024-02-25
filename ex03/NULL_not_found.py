def NULL_not_found(object: any) -> int:
    if object != object:
        print(f'Cheese: {object} {type(object)}')
        return 0
    elif not object:
        if object is False:
            print(f'Fake: {object} {type(object)}')
        elif object == 0:
            print(f'Zero: {object} {type(object)}')
        elif object == '':
            print(f'Empty: {object} {type(object)}')
        else:
            print(f'Nothing: {object} {type(object)}')
        return 0
    print('Type not Found')
    return 1
