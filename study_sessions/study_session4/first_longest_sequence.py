"""
1. Behavior: unit tests, documentation, function name, type hints
2. Implementation: comment what each line of code does (predictive stepping!)
3. Strategy pt. 1 - purpose: comment why each line of code exists
4. Strategy pt. 2 - connections: describe how different lines interact
5. strategy pt. 3 - goals: summarize the strategy using sub-goals
"""


def first_longest_sequence(b: list[int] = []) -> list[int]:
    """
    function that returns the first occurrence of the longest same sequence

    Args:
        b list[int]: the list to check for first longest same sequence

    Returns -> list[int]:
            a list of the first longest same sequence

    Examples:
    >>> first_longest_sequence([1, 2, 3, 4])
    [1]
    >>> first_longest_sequence([4, 3, 2, 1])
    [4]
    >>> first_longest_sequence([4, 4, 4, 4, 4, 4])
    [4, 4, 4, 4, 4, 4]
    >>> first_longest_sequence([4, 4, 3, 2, 2])
    [4, 4]
    >>> first_longest_sequence([])
    []

    """
    # store the length of the longest sequence found
    longest_sequence_length = 0

    # store the first occurrence of the longest sequence
    longest_sequence_start_index = 0

    # stores the index where the longest sequence starts.
    counter = 0

    # Process the entire list to find the longest sequence.

    while counter < len(b):
        # store the start of the current sequence
        occurrence = counter

        # Identify the length of the current sequence of identical elements.
        # - It checks by comparing current element and next element
        while counter + 1 < len(b) and b[counter] == b[counter + 1]:
            counter += 1

        # store the length of current sequence
        # To Compare the current sequence length to the longest found.
        current_sequence_length = counter - occurrence + 1

        # Ensure we always track the longest sequence.
        if current_sequence_length > longest_sequence_length:
            # - Update the longest sequence if the current sequence is longer.
            longest_sequence_length = current_sequence_length
            longest_sequence_start_index = occurrence

        # increment the counter to move to the next element in the list after the current sequence
        counter += 1

    # Return the longest sequence or an empty list if no sequence is found.
    # - Slice the list based on the first value of longest sequence and the length of it
    return (
        b[
            longest_sequence_start_index : longest_sequence_start_index
            + longest_sequence_length
        ]
        if longest_sequence_length > 0
        else []
    )


assert first_longest_sequence([1, 2, 3, 4]) == [1], "Test 1"
assert first_longest_sequence([4, 3, 2, 1]) == [4], "Test 2"
assert first_longest_sequence([]) == [], "Test 3"
assert first_longest_sequence([4, 4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4, 4], "Test 4"
assert first_longest_sequence([2, 6, 3, 8]) == [2], "Test 5"
assert first_longest_sequence([2, 3, 1, 6, 8]) == [2], "Test 6"
assert first_longest_sequence([0, 3, 2, 7]) == [0], "Test 7"
assert first_longest_sequence([2, 3, 4, 2, 7, 9, 4, 2]) == [2], "Test 8"
assert first_longest_sequence([2, 2, 3, 3, 3, 4, 4, 4, 4]) == [4, 4, 4, 4], "Test 9"
assert first_longest_sequence([2, 2, 3, 1, 4]) == [2, 2], "Test 10"
assert first_longest_sequence([3, 3, 3, 1, 4]) == [3, 3, 3], "Test 11"
assert first_longest_sequence([1, 1, 2, 2, 2, 5, 5, 5, 5, 3, 3, 3]) == [5, 5, 5, 5], (
    "Test 12"
)
assert first_longest_sequence([2, 2, 3, 4, 4]) == [2, 2], (
    "Test 13 - it returns the first longest sequence"
)
assert first_longest_sequence([4, 4, 3, 2, 2]) == [4, 4], (
    "Test 14 - it returns the first longest sequence"
)
assert first_longest_sequence([2, 2, 3, 2, 2]) == [2, 2], "Test 15"
print(first_longest_sequence([4, 4, 3, 2, 2]))  # Example test case
