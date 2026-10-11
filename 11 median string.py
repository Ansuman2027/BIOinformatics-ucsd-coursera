import sys
import itertools

def hamming_distance(p: str, q: str) -> int:
    """Calculates the Hamming distance between two strings of equal length."""
    return sum(c1 != c2 for c1, c2 in zip(p, q))

def distance_pattern_to_text(pattern: str, text: str) -> int:
    """Finds the minimum Hamming distance between a pattern and any k-mer in text."""
    k = len(pattern)
    min_dist = float('inf')
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        dist = hamming_distance(pattern, kmer)
        if dist < min_dist:
            min_dist = dist
    return min_dist

def distance_pattern_to_dna(pattern: str, dna: list[str]) -> int:
    """Calculates d(Pattern, Dna) as the sum of distances from pattern to each sequence in dna."""
    return sum(distance_pattern_to_text(pattern, text) for text in dna)

def median_string(dna: list[str], k: int) -> str:
    """Identifies the median string of length k in a collection of longer strings."""
    distance = float('inf')
    median = ""
    
    # Iterate over all possible 4^k k-mers
    for pattern_tuple in itertools.product('ACGT', repeat=k):
        pattern = "".join(pattern_tuple)
        d = distance_pattern_to_dna(pattern, dna)
        if d < distance:
            distance = d
            median = pattern
            
    return median
