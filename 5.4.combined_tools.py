def interleave(*args):
    """
    The interleave function takes in an arbitrary number of
    iterables (using the *args syntax) and returns a list of
    the interleaved elements from those iterables.
    :param args: Any number of iterable arguments
    :return:
    """
    # Determine the length of the shortest iterable
    shortest_length = min(len(arg) for arg in args)

    # Interleave the iterables
    interleaved = [elem for pair in zip(*args) for elem in pair]

    # Add any remaining elements from each iterable
    for arg in args:
        remaining = arg[shortest_length:]
        interleaved.extend(remaining)

    return interleaved


def interleave_generator(*args):
    """
    The interleave_generator function takes in one or more iterables
     as arguments, and yields each element of these iterables in an interleaved fashion.

    :param args: Any number of iterable arguments.
    :return: The generator yields each element of this interleaved iterable.
    """
    # Determine the length of the shortest iterable
    shortest_length = min(len(arg) for arg in args)

    # Interleave the iterables
    interleaved = (elem for pair in zip(*args) for elem in pair)

    # Yield any remaining elements from each iterable
    for arg in args:
        remaining = arg[shortest_length:]
        for elem in remaining:
            yield elem

    # Yield any remaining elements from the interleaved iterator
    for elem in interleaved:
        yield elem


if __name__ == '__main__':
    # interleave() test:
    print(interleave('abcd', [1, 2, 3, 6], ('!', '@', '-', 'k')))

    # interleave_generator() test:
    for element in interleave_generator('abc', [1, 2, 3], ('!', '@', '#')):
        print(element, end=' ')
