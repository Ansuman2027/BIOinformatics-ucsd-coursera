import sys

# Insert your neighbors function here, along with any subroutines you need
def hamming_distance(p: str, q: str) -> int:
    return sum(c1 != c2 for c1, c2 in zip(p, q))

def neighbors(s: str, d: int) -> list[str]:
    """Generate neighbors of a string within a given Hamming distance."""
    if d == 0:
        return [s]
    if len(s) == 1:
        return ['A', 'C', 'G', 'T']
    
    neighborhood = set()
    suffix_neighbors = neighbors(s[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(s[1:], text) < d:
            for x in ('A', 'C', 'G', 'T'):
                neighborhood.add(x + text)
        else:
            neighborhood.add(s[0] + text)
            
    return list(neighborhood)

# Alias to satisfy case variations in the test runner
Neighbors = neighbors










if __name__ == "__main__":
    # Example input: a pattern string and the maximum allowed Hamming distance d
    pattern = "ACG"
    d = 1

    # Call the neighbors function to generate the d-neighborhood
    result = neighbors(pattern, d)

    # Print the resulting neighboring strings separated by newlines (or spaces)
    print("\n".join(result))



