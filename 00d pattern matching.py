import sys

def pattern_matching(pattern: str, genome: str) -> list[int]:
    """Find all occurrences of a pattern in a genome."""
    positions = []
    k = len(pattern)
    for i in range(len(genome) - k + 1):
        if genome[i:i + k] == pattern:
            positions.append(i)
    return positions
