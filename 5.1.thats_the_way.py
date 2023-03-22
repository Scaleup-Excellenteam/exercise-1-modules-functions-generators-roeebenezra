import os


def that_is_the_way(path):
    """
    The function that_is_the_way takes a path as an argument and returns
     a list of files in that path that contain the substring 'deep'.

    :param path: path of directory to search in
    :return: list of matches
    """
    return [file for file in os.listdir(path) if 'deep' in file]


# print the search result
print(that_is_the_way(os.path.join('images')))

