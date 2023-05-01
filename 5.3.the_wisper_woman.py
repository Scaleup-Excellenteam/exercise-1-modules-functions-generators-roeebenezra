import os.path
import re


def search_file_for_strings(file_path):
    """
    The search_file_for_strings function takes a file path as an argument and returns
    a generator that yields one secret message at a time.
    :param file_path: 'logo.jpg' image path.
    :return: one secret message at a time.
    """
    with open(file_path, 'rb') as f:
        # Read in a block of bytes
        block = f.read(1024)
        while block:
            block = f.read(1024)

            # Convert the block to a string of lowercase letters
            # (excluding non-letter characters)
            letters = re.sub(r'[^a-z]!', '', block.decode('utf-8', 'ignore').lower())

            # Use regular expressions to find all secret messages in the string
            secret_messages = re.findall(r'[a-z]{5,}!', letters)

            # Yield each secret message found
            for message in secret_messages:
                yield message


if __name__ == '__main__':
    logo_name = 'resources/logo.jpg'
    for message in search_file_for_strings(os.path.join(logo_name)):
        print(message)
