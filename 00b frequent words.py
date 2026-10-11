import sys

def frequent_words(text: str, k: int) -> list[str]:
    counts = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        counts[kmer] = counts.get(kmer, 0) + 1
        
    if not counts:
        return []
        
    max_count = max(counts.values())
    return [kmer for kmer, count in counts.items() if count == max_count]
