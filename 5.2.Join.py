def join(*lists, sep='-'):
    """
    The function Join is join N lists with the specified separator or '-' if no separator provided.
    :param lists: n lists
    :param sep: separator provided or '-' as default
    :return: joined list with the  separator
    """
    if not lists:
        raise ValueError("At least one list must be provided")

    joined_list = []
    for lst in lists:
        joined_list += lst
        joined_list.append(sep)
    # remove the last separator
    joined_list.pop()
    return joined_list


if __name__ == '__main__':
    # test join():
    list1, list2, list3 = ['a', 'b', 'c', 3, 4], [1, 2, 3, 'e'], ['x', 'y', 'z', 3, 4, 5]

    # Join the lists using '-' as the separator
    print(join(list1, list2, list3, sep='@'))

    # Join the lists using '/' as the separator
    print(join(list1, list2, list3, sep='/'))

    # Join the lists using the default separator '-'
    print(join(list1, list2, list3))

    # Error raise for empty lists value
    print(join())


