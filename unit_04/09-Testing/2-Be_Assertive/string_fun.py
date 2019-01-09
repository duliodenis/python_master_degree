def is_palindrome(yarn):
    """Return whether or not a string is a palindrome.

    A palindrome is a word/phrase that's the same in
    both directions.
    """
    return yarn == yarn[::-1]