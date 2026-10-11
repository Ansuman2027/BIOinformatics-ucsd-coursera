import sys


def make_profile(motifs: list[str]) -> dict[str, list[float]]:
    k = len(motifs[0])
    t = len(motifs)
    profile = {base: [0.0] * k for base in "ACGT"}

    for motif in motifs:
        for i, char in enumerate(motif):
            profile[char][i] += 1.0

    for base in "ACGT":
        for i in range(k):
            profile[base][i] /= t

    return profile


def profile_most_probable_kmer(
    text: str, k: int, profile: dict[str, list[float]]
) -> str:
    max_prob = -1.0
    best_kmer = text[:k]

    for i in range(len(text) - k + 1):
        kmer = text[i : i + k]
        prob = 1.0
        for j, char in enumerate(kmer):
            prob *= profile[char][j]
        if prob > max_prob:
            max_prob = prob
            best_kmer = kmer

    return best_kmer


def score_motifs(motifs: list[str]) -> int:
    k = len(motifs[0])
    t = len(motifs)
    total_score = 0

    for j in range(k):
        counts = {"A": 0, "C": 0, "G": 0, "T": 0}
        for motif in motifs:
            counts[motif[j]] += 1
        max_count = max(counts.values())
        total_score += t - max_count

    return total_score


def greedy_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    best_motifs = [string[:k] for string in dna]
    best_score = score_motifs(best_motifs)

    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i : i + k]]

        for j in range(1, t):
            current_profile = make_profile(motifs)
            next_motif = profile_most_probable_kmer(dna[j], k, current_profile)
            motifs.append(next_motif)

        current_score = score_motifs(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs
