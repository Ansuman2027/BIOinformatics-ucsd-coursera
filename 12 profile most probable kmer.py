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









if __name__ == "__main__":
    # Example input data: a DNA text string, motif length k, and a profile probability matrix
    text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATCTAGCDCGAT"
    k = 3
    profile = {
        "A": [0.2, 0.4, 0.3],
        "C": [0.3, 0.1, 0.2],
        "G": [0.1, 0.3, 0.2],
        "T": [0.4, 0.2, 0.3]
    }

    # Call the function to find the most probable k-mer based on the profile matrix
    result = profile_most_probable_kmer(text, k, profile)

    # Print the resulting most probable k-mer
    print(result)
