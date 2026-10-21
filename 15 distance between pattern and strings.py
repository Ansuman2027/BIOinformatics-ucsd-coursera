import sys


def hamming_distance(p: str, q: str) -> int:
    return sum(c1 != c2 for c1, c2 in zip(p, q))


def distance_between_pattern_and_strings(
    pattern: str, dna: list[str]
) -> int:
    """Returns the sum of the Hamming distances between pattern and each string in dna."""
    k = len(pattern)
    total_distance = 0

    for text in dna:
        min_hamming = float("inf")
        for i in range(len(text) - k + 1):
            kmer = text[i : i + k]
            dist = hamming_distance(pattern, kmer)
            if dist < min_hamming:
                min_hamming = dist
        total_distance += min_hamming

    return total_distance










if __name__ == "__main__":
    pattern = "AAA"
    dna_list = [
        "TTACCTTAAC",
        "GATATCTGTC",
        "ACGGCGTTCG",
        "CCCTAAAGAG",
        "CGTCAGAGGT",
    ]

    total_dist = distance_between_pattern_and_strings(pattern, dna_list)
    print(f"Total distance between pattern and strings: {total_dist}")
