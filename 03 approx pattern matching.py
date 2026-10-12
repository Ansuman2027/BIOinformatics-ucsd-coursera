import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your approximate_pattern_matching function here, along with any subroutines you need
def approximate_pattern_matching(pattern: str, text: str, d: int) -> list[int]:
    """Find all starting positions where Pattern appears as a substring of Text with at most d mismatches."""
    positions = []
    k = len(pattern)
    for i in range(len(text) - k + 1):
        substring = text[i:i + k]
        mismatches = sum(c1 != c2 for c1, c2 in zip(pattern, substring))
        if mismatches <= d:
            positions.append(i)
    return positions








if __name__ == "__main__":
    query_pattern = "ATTCTGGA"
    genome_text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACCCACGGGGTCTGCCAACCTCACCC"
    max_mismatches = 3
    result = approximate_pattern_matching(query_pattern, genome_text, max_mismatches)
    print(f"Starting positions with at most {max_mismatches} mismatches: {result}")
