import sys

def reverse_complement(pattern: str) -> str:
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(pattern))









if __name__ == "__main__":
    dna_pattern = "AAAACCCGGT"
    rc = reverse_complement(dna_pattern)
    print(f"Original:           {dna_pattern}")
    print(f"Reverse Complement: {rc}")
