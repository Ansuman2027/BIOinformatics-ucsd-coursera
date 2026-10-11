import sys
from collections import defaultdict

# Please do not remove package declarations because these are used by the autograder.

def hamming_distance(p: str, q: str) -> int:
    return sum(c1 != c2 for c1, c2 in zip(p, q))

def reverse_complement(pattern: str) -> str:
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(comp[base] for base in reversed(pattern))

def neighbors(pattern: str, d: int) -> set[str]:
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for x in ('A', 'C', 'G', 'T'):
                neighborhood.add(x + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood

def frequent_words_mismatches_reverse_complements(text: str, k: int, d: int) -> list[str]:
    """Find the most frequent k-mers with up to d mismatches in a text, including reverse complements."""
    counts = defaultdict(int)
    
    for i in range(len(text) - k + 1):
        window = text[i:i + k]
        for neighbor in neighbors(window, d):
            counts[neighbor] += 1
            counts[reverse_complement(neighbor)] += 1
            
    if not counts:
        return []
        
    max_count = max(counts.values())
    return [kmer for kmer, count in counts.items() if count == max_count]
