import sys
from collections import defaultdict

def find_clumps(genome: str, k: int, l: int, t: int) -> list[str]:
    clump_patterns = set()
    n = len(genome)
    if n < l:
        return []

    counts = defaultdict(int)
    first_window = genome[:l]
    for i in range(l - k + 1):
        kmer = first_window[i:i + k]
        counts[kmer] += 1
        if counts[kmer] >= t:
            clump_patterns.add(kmer)

    for i in range(1, n - l + 1):
        outgoing = genome[i - 1:i - 1 + k]
        counts[outgoing] -= 1
        incoming = genome[i + l - k:i + l]
        counts[incoming] += 1
        if counts[incoming] >= t:
            clump_patterns.add(incoming)

    return list(clump_patterns)
