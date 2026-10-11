import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your approximate_pattern_count function here, along with any subroutines you need
def approximate_pattern_count(text: str, pattern: str, d: int) -> int:
    """Count the occurrences of a pattern in a text, allowing for up to d mismatches."""
    count = 0
    k = len(pattern)
    for i in range(len(text) - k + 1):
        window = text[i:i + k]
        mismatches = sum(c1 != c2 for c1, c2 in zip(pattern, window))
        if mismatches <= d:
            count += 1
    return count
