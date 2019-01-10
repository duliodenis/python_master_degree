import itertools 
 
def is_palindrome(yarn):
    """Return whether or not a string is a palindrome.

    A palindrome is a word/phrase that's the same in
    both directions.
    """
    return yarn == yarn[::-1]


def get_anagrams(*yarn):
    """Return a list of anagrams for a string."""
    # If only one letter came in, return it
    if yarn:
        if len(yarn[0]) <= 1:
            return list(yarn)
    else:
        raise ValueError("Must provide at least two letters")

    # Get all of the words from the dictionary
    words = set([
        w.strip().lower() for w in open('words.txt')
    ])

    output = set()
    for thread in yarn:
        thread = thread.lower()
        # Find all possible anagrams
        for i in range(2, len(thread)):
            fibers = set(
                [''.join(w) for w in itertools.permutations(thread, i)]
            )
            output.update(fibers.intersection(words))

    # Finally, return all of the combinations that are in the dictionary
    return sorted(list(output))