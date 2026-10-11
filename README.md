Biological Context: In bacterial genomes, DNA replication starts at the origin of replication (oriC). Due to differences in mutation rates between the leading and lagging strands, Guanine (G) tends to be depleted relative to Cytosine (C) on the reverse half of the replication loop. The point where the cumulative difference between G and C (#G−#C) transitions from decreasing to increasing—the minimum skew—typically identifies the location of oriC.

Algorithm Mechanism:

It performs a single linear scan (O(n) time complexity) through the sequence.

It increments the skew count by +1 for G, decrements by −1 for C, and leaves it unchanged for A and T.

It dynamically tracks the lowest skew value seen so far and collects all 1-based indices that achieve this minimum.
----------------------------------------------------------------------------------------------------
This function calculates the Hamming distance between two equal-length DNA strings, which represents the total number of mismatched nucleotide positions between them.

Biological Context: In molecular biology and motif finding, DNA sequences such as transcription factor binding sites (regulatory motifs) rarely remain 100% identical across a genome due to point mutations (substitutions). The Hamming distance serves as a fundamental metric for quantifying genetic divergence, identifying approximate pattern matches, and finding consensus sequences with allowed mismatches.

Algorithm Mechanism:

It runs in linear time, O(n), where n is the length of the sequences.

It uses Python's zip() to align and iterate over both strings in parallel, character by character.

For each position, the boolean condition c1 != c2 evaluates to True (1) on a mismatch and False (0) on a match.

sum(...) aggregates all mismatches to yield the total distance.
--------------------------------------------------------------------------------------------------------
This function identifies all starting positions where a target k-mer pattern appears as a substring within a larger genomic text with at most d mismatches (Hamming distance ≤d).

Biological Context: In nature, regulatory regions such as DnaA boxes or transcription factor binding sites are rarely conserved perfectly. Over evolutionary time, mutations occur, meaning a regulatory protein can still recognize and bind to sequences that vary by a few nucleotides. Approximate pattern matching allows computational biologists to locate degenerated or mutated motifs across an entire genome rather than missing them with exact string matching.

Algorithm Mechanism:

It employs a sliding window of length k=len(pattern) across text, evaluating every possible starting position from index 0 to ∣text∣−k.

For each extracted k-mer window, it computes the Hamming distance between the window and pattern by comparing corresponding characters with zip().

If the count of mismatched bases is less than or equal to the threshold d, the 0-based starting index i is appended to the results.

It runs in O((∣text∣−k+1)⋅k) time complexity.


