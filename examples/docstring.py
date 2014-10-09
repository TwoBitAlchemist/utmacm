"""Docstring helper functions (including PEP 257 trim algorithm)"""
import sys


def trim(docstring):
    """
    This is the example algorithm for trimming docstrings proposed in PEP 257.
    http://legacy.python.org/dev/peps/pep-0257/#handling-docstring-indentation

    It has been modified to work with Python 2 and 3.
    """
    if not docstring:
        return ''
    try:
        maxint = sys.maxint     # Python2
    except AttributeError:
        maxint = sys.maxsize    # Python3
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = maxint
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < maxint:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)
