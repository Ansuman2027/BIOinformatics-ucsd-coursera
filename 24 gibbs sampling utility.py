import sys
import random

def score_motifs(motifs: list[str], k: int) -> int:
    score = 0
    t = len(motifs)
    for j in range(k):
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for m in motifs:
            counts[m[j]] += 1
        score += t - max(counts.values())
    return score

def profile_random_kmer(dna_seq: str, k: int, profile: dict[str, list[float]]) -> str:
    n = len(dna_seq) - k + 1
    kmers = [dna_seq[i:i + k] for i in range(n)]
    probs = []
    
    for kmer in kmers:
        p = 1.0
        for j, nuc in enumerate(kmer):
            p *= profile[nuc][j]
        probs.append(p)
        
    total = sum(probs)
    if total == 0:
        return random.choice(kmers)
        
    weights = [p / total for p in probs]
    return random.choices(kmers, weights=weights, k=1)[0]

def single_gibbs_sampler(dna: list[str], k: int, t: int, n: int) -> list[str]:
    motifs = [seq[i:i + k] for seq, i in ((s, random.randint(0, len(s) - k)) for s in dna)]
    best_motifs = list(motifs)
    best_score = score_motifs(best_motifs, k)
    
    counts = {nuc: [1.0] * k for nuc in 'ACGT'}
    for m in motifs:
        for j, nuc in enumerate(m):
            counts[nuc][j] += 1.0
            
    for _ in range(n):
        i = random.randrange(t)
        old_motif = motifs[i]
        
        for j, nuc in enumerate(old_motif):
            counts[nuc][j] -= 1.0
            
        denom = (t - 1) + 4.0
        profile = {nuc: [c / denom for c in counts[nuc]] for nuc in 'ACGT'}
        
        new_motif = profile_random_kmer(dna[i], k, profile)
        motifs[i] = new_motif
        
        for j, nuc in enumerate(new_motif):
            counts[nuc][j] += 1.0
            
        cur_score = score_motifs(motifs, k)
        if cur_score < best_score:
            best_score = cur_score
            best_motifs = list(motifs)
            
    return best_motifs

def gibbs_sampler(dna: list[str], k: int, t: int, n: int) -> list[str]:
    best_motifs = None
    best_score = float('inf')
    
    num_starts = max(20, min(200, 20000 // n))
    
    for _ in range(num_starts):
        motifs = single_gibbs_sampler(dna, k, t, n)
        score = score_motifs(motifs, k)
        if score < best_score:
            best_score = score
            best_motifs = motifs
            
    return best_motifs












if __name__ == "__main__":
    # Example input data: list of DNA sequences, motif length (k), number of sequences (t), and iterations (N)
    dna = [
        "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
        "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
        "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
        "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
        "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
    ]
    k = 8
    t = len(dna)
    n = 100

    # Call the gibbs_sampler function to find the best motifs
    result = gibbs_sampler(dna, k, t, n)

    # Print each discovered motif on a new line
    print("\n".join(result))
