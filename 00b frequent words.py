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








if __name__ == "__main__":
    dna_sequence = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    kmer_length = 4
    most_frequent = frequent_words(dna_sequence, kmer_length)
    print(f"Most frequent {kmer_length}-mers: {most_frequent}")
