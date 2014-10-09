"""
Example 1:

Convert an integer representing bytes to its corresponding
'human-sized' interpretation.

Modified from: http://preview.tinyurl.com/o82qyay
"""
import sys


SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
}


def approximate_size(size, binary=False):
    """Convert a size in bytes to a more human-friendly format.

    If the binary option is set, use 1KB = 1024 bytes.
    Otherwise, 1KB = 1000 bytes.

    Returns a string indicating the rounded size and its unit,
    such as '1.00 KB' or '5.27 MiB'.
    """
    if size < 0:
        raise ValueError('Size must be non-negative.')

    multiple = 1024 if binary else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '%.2f %s' % (size, suffix)
            # return '{0:.2f} {1}'.format(size, suffix)
            # See alvinalexander.com/programming/printf-format-cheat-sheet

    raise ValueError('Size overflow: provided size is too large to name.')


def main():
    """This function runs when this is called as a script from the command line
    using python ./filename.py or equivalent.
    """
    is_int = False
    while not is_int:
        user_number = input('Enter size in bytes: ')
        try:
            user_number = int(user_number)
            is_int = True
        except ValueError:
            pass

    answer_line = 'Approximate size (1{unit} = {amt} bytes):'
    try:
        print()
        print(answer_line.format(**{'unit': 'KB', 'amt': 1000}),
              approximate_size(user_number).rjust(12))
        print(answer_line.format(**{'unit': 'KiB', 'amt': 1024}),
              approximate_size(user_number, True).rjust(12))
    except ValueError as e:
        sys.exit(str(e))


if __name__ == '__main__':
    main()
