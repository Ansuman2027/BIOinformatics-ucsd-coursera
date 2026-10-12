import sys
import random

def profile_most_probable_kmer(text: str, k: int, profile: dict[str, list[float]]) -> str:
    best_prob = -1.0
    best_kmer = text[:k]
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = 1.0
        for j, nuc in enumerate(kmer):
            prob *= profile[nuc][j]
        if prob > best_prob:
            best_prob = prob
            best_kmer = kmer
    return best_kmer

def score_motifs(motifs: list[str], k: int) -> int:
    score = 0
    t = len(motifs)
    for j in range(k):
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            counts[motif[j]] += 1
        score += t - max(counts.values())
    return score

def single_randomized_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    motifs = [seq[i:i + k] for seq, i in ((s, random.randint(0, len(s) - k)) for s in dna)]
    best_motifs = motifs
    best_score = score_motifs(best_motifs, k)
    
    while True:
        # Profile matrix with Laplace pseudocounts (+1)
        col_counts = [{nuc: 1.0 for nuc in 'ACGT'} for _ in range(k)]
        for motif in motifs:
            for col, nuc in enumerate(motif):
                col_counts[col][nuc] += 1.0
        denom = t + 4.0
        profile = {nuc: [col_counts[col][nuc] / denom for col in range(k)] for nuc in 'ACGT'}
        
        motifs = [profile_most_probable_kmer(seq, k, profile) for seq in dna]
        current_score = score_motifs(motifs, k)
        
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs
        else:
            return best_motifs

def randomized_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    best_motifs = None
    best_score = float('inf')
    
    # 400 restarts finds the optimal motifs reliably while staying well under 20s
    for _ in range(400):
        motifs = single_randomized_motif_search(dna, k, t)
        score = score_motifs(motifs, k)
        if score < best_score:
            best_score = score
            best_motifs = motifs
            
    return best_motifs
