import sys
from collections import defaultdict

# Please do not remove package declarations because these are used by the autograder.

def hamming_distance(p: str, q: str) -> int:
    return sum(c1 != c2 for c1, c2 in zip(p, q))

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

def frequent_words_with_mismatches(text: str, k: int, d: int) -> list[str]:
    """Find the most frequent k-mers with up to d mismatches in a text."""
    counts = defaultdict(int)
    
    for i in range(len(text) - k + 1):
        window = text[i:i + k]
        for neighbor in neighbors(window, d):
            counts[neighbor] += 1
            
    if not counts:
        return []
        
    max_count = max(counts.values())
    return [kmer for kmer, count in counts.items() if count == max_count]











if __name__ == "__main__":
    sample_text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k_length = 4
    max_d = 1
    frequent_kmers = frequent_words_with_mismatches(sample_text, k_length, max_d)
    print(f"Most frequent {k_length}-mers with up to {max_d} mismatches: {frequent_kmers}")
