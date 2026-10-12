import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your minimum_skew function here, along with any subroutines you need
def minimum_skew(genome: str) -> list[int]:
    """Find positions in a genome where the skew diagram attains a minimum."""
    current_skew = 0
    min_skew = 0
    min_positions = [0]
    
    for i, base in enumerate(genome, start=1):
        if base == 'G':
            current_skew += 1
        elif base == 'C':
            current_skew -= 1
            
        if current_skew < min_skew:
            min_skew = current_skew
            min_positions = [i]
        elif current_skew == min_skew:
            min_positions.append(i)
            
    return min_positions












if __name__ == "__main__":
    sample_genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
    min_indices = minimum_skew(sample_genome)
    print(f"Positions where skew achieves minimum: {min_indices}")



