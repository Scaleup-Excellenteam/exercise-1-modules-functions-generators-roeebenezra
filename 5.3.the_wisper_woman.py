import os.path
import re


def search_file_for_strings(file_path):
    """
    The function reads in a binary file at the provided file path
    and searches for secret messages within it.
    The secret messages are defined as strings of lowercase English letters that are at
    least 5 characters long and end with an exclamation point.
    To search for the secret messages, the function reads in the file in blocks of 1024 bytes,
    converts each block to a lowercase string containing only letters, and uses regular expressions
    to search for the secret messages within that string. The function yields each secret message found.

    :param file_path: 'logo.jpg' image path.
    :return: one secret message at a time.
    """
    with open(file_path, 'rb') as f:
        while True:
            # Read in a block of bytes
            block = f.read(1024)

            # Break if we've reached the end of the file
            if not block:
                break

            # Convert the block to a string of lowercase letters
            # (excluding non-letter characters)
            letters = re.sub(r'[^a-z]!', '', block.decode('utf-8', 'ignore').lower())

            # Use regular expressions to find all secret messages in the string
            secret_messages = re.findall(r'[a-z]{5,}!', letters)

            # Yield each secret message found
            for message in secret_messages:
                yield message


# Example usage
logo_name = 'resources/logo.jpg'
for message in search_file_for_strings(os.path.join(logo_name)):
    print(message)
