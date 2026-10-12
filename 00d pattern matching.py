import sys

def pattern_matching(pattern: str, genome: str) -> list[int]:
    """Find all occurrences of a pattern in a genome."""
    positions = []
    k = len(pattern)
    for i in range(len(genome) - k + 1):
        if genome[i:i + k] == pattern:
            positions.append(i)
    return positions










if __name__ == "__main__":
    target = "ATAT"
    dna_seq = "GATATATGCATATACTT"
    matches = pattern_matching(target, dna_seq)
    print(f"Pattern '{target}' found at starting positions: {matches}")
