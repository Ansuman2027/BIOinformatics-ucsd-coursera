import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your hamming_distance function here, along with any subroutines you need
def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    return sum(c1 != c2 for c1, c2 in zip(p, q))










if __name__ == "__main__":
    seq1 = "GGGCCGTTGGT"
    seq2 = "GGACCGTTGAC"
    dist = hamming_distance(seq1, seq2)
    print(f"Hamming distance between {seq1} and {seq2}: {dist}")
