def profile_most_probable_kmer(text: str, k: int, profile: dict[str, list[float]]) -> str:
    """Identifies the most probable k-mer according to a given profile matrix.

    The profile matrix is given as one row per nucleotide, so profile["A"][i] is
    the probability of A in column i of the matrix.
    """
    max_prob = -1.0
    most_probable_kmer = text[:k]

    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = 1.0
        for j, nucleotide in enumerate(kmer):
            prob *= profile[nucleotide][j]
            
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer

    return most_probable_kmer
