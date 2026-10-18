import sys

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

def has_approximate_match(pattern: str, text: str, d: int) -> bool:
    k = len(pattern)
    for i in range(len(text) - k + 1):
        if hamming_distance(pattern, text[i:i + k]) <= d:
            return True
    return False

def motif_enumeration(dna: list[str], k: int, d: int) -> list[str]:
    """Implements the MotifEnumeration algorithm."""
    if not dna:
        return []
        
    candidates = set()
    first_seq = dna[0]
    
    # Generate candidate k-mers from all d-neighbors of k-mers in the first sequence
    for i in range(len(first_seq) - k + 1):
        kmer = first_seq[i:i + k]
        for neighbor in neighbors(kmer, d):
            candidates.add(neighbor)
            
    # Verify each candidate exists with at most d mismatches in all sequences
    valid_motifs = []
    for candidate in sorted(candidates):
        if all(has_approximate_match(candidate, seq, d) for seq in dna):
            valid_motifs.append(candidate)
            
    return valid_motifs









if __name__ == "__main__":
    # Example input data: a list of DNA sequences, motif length (k), and allowed mismatches (d)
    dna = [
        "ATTTGGC",
        "TGCCTTA",
        "CGGTATC",
        "GAAAATT"
    ]
    k = 3
    d = 1

    # Call the motif enumeration function
    result = motif_enumeration(dna, k, d)

    # Print the resulting motifs separated by spaces
    print(" ".join(result))
