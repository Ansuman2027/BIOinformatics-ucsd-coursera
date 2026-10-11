Biological Context: In bacterial genomes, DNA replication starts at the origin of replication (oriC). Due to differences in mutation rates between the leading and lagging strands, Guanine (G) tends to be depleted relative to Cytosine (C) on the reverse half of the replication loop. The point where the cumulative difference between G and C (#G−#C) transitions from decreasing to increasing—the minimum skew—typically identifies the location of oriC.

Algorithm Mechanism:

It performs a single linear scan (O(n) time complexity) through the sequence.

It increments the skew count by +1 for G, decrements by −1 for C, and leaves it unchanged for A and T.

It dynamically tracks the lowest skew value seen so far and collects all 1-based indices that achieve this minimum.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




This function calculates the Hamming distance between two equal-length DNA strings, which represents the total number of mismatched nucleotide positions between them.

Biological Context: In molecular biology and motif finding, DNA sequences such as transcription factor binding sites (regulatory motifs) rarely remain 100% identical across a genome due to point mutations (substitutions). The Hamming distance serves as a fundamental metric for quantifying genetic divergence, identifying approximate pattern matches, and finding consensus sequences with allowed mismatches.

Algorithm Mechanism:

It runs in linear time, O(n), where n is the length of the sequences.

It uses Python's zip() to align and iterate over both strings in parallel, character by character.

For each position, the boolean condition c1 != c2 evaluates to True (1) on a mismatch and False (0) on a match.

sum(...) aggregates all mismatches to yield the total distance


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


This function identifies all starting positions where a target k-mer pattern appears as a substring within a larger genomic text with at most d mismatches (Hamming distance ≤d).

Biological Context: In nature, regulatory regions such as DnaA boxes or transcription factor binding sites are rarely conserved perfectly. Over evolutionary time, mutations occur, meaning a regulatory protein can still recognize and bind to sequences that vary by a few nucleotides. Approximate pattern matching allows computational biologists to locate degenerated or mutated motifs across an entire genome rather than missing them with exact string matching.

Algorithm Mechanism:

It employs a sliding window of length k=len(pattern) across text, evaluating every possible starting position from index 0 to ∣text∣−k.

For each extracted k-mer window, it computes the Hamming distance between the window and pattern by comparing corresponding characters with zip().

If the count of mismatched bases is less than or equal to the threshold d, the 0-based starting index i is appended to the results.

It runs in O((∣text∣−k+1)⋅k) time complexity.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



This function computes the total frequency with which a target k-mer pattern occurs within a larger genomic text with up to d allowed mismatches (Hamming distance ≤d).

Biological Context: In computational genomics, determining the density of degenerate motifs is critical for identifying biological signals like replication origins (oriC) and regulatory promoters. Functional binding sites (such as DnaA boxes) frequently cluster together in high densities with slight point mutations; counting occurrences with tolerance for mismatches quantifies how strongly a specific motif family is enriched in a genomic region.

Algorithm Mechanism:

It shifts a fixed-size window of length k=len(pattern) across text, inspecting every starting index from 0 to ∣text∣−k.

For every k-mer window, it computes the Hamming distance relative to pattern using character-by-character comparison via zip().

If the total number of mismatched bases is ≤d, an integer counter increments by 1.

It operates in O((∣text∣−k+1)⋅k) time complexity and uses O(k) auxiliary space for the slice window.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



This pipeline discovers the most overrepresented k-mers (motifs) within a genomic sequence text, allowing each occurrence to vary by up to d mismatches.

Biological Context: Key regulatory signals—such as the DnaA boxes that trigger bacterial replication initiation—are rarely identical repeats. Instead, a master consensus motif operates across a family of degenerate variants scattered through the origin of replication. Finding the most frequent k-mers with mismatches pinpoints these biological consensus motifs even when the exact canonical sequence appears only rarely or not at all in the raw genome.

Algorithm Mechanism:

neighbors(pattern, d): A recursive subroutine generating the d-neighborhood—the set of all valid k-mers whose Hamming distance from the input pattern is at most d.

Frequency Array / Hash Map (defaultdict): Slides a window of length k across text. For every observed window, it expands its entire d-neighborhood and increments a shared tally for each neighbor.

Peak Selection: Evaluates the highest count (max(counts.values())) and extracts all candidate patterns achieving that maximum score.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



This algorithm discovers the most abundant k-mer patterns in a genomic sequence by tallying occurrences that allow up to d mismatches and simultaneously accounting for both the forward and reverse complementary strands.

Biological Context: DNA is double-stranded, and replication or transcription factors (such as the DnaA initiator protein) bind double-stranded DNA. Because these proteins can recognize binding motifs regardless of which strand carries the canonical sequence (5' to 3' on the forward strand or 5' to 3' on the reverse-complement strand), counting matches on both strands combined is the gold standard approach for identifying true functional motifs like DnaA boxes in bacterial replication origins (oriC).

Algorithm Mechanism:

reverse_complement(pattern): Inverts the nucleotide sequence direction and maps each base to its Watson-Crick complement (A ↔ T, C ↔ G).

neighbors(pattern, d): Recursively builds the complete d-neighborhood—every possible k-mer within a Hamming distance ≤d from the target window.

Bidirectional Neighborhood Tally: Slides a length-k window across text. For every valid neighbor of that window, it increments the count of both the neighbor and its reverse_complement(neighbor).

Peak Selection: Finds the maximum frequency value stored in the defaultdict and returns all k-mers matching that highest aggregate score.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



This algorithm generates the complete set of all k-mers whose Hamming distance from a target sequence s does not exceed a specified threshold d.

Biological Context: In motif finding, biological regulatory sites (such as DnaA boxes or transcription factor binding targets) are not strictly conserved and tolerate point substitutions. Rather than testing every theoretical sequence across the genome, generating the d-neighborhood constructs the exact space of all biologically acceptable mutational variants around an observed sequence motif.

Algorithm Mechanism:

Recursive Suffix Decomposition: The problem is broken down recursively by computing the neighborhood of the suffix s[1:].

Base Cases:

If d=0, the only string within distance 0 is the sequence itself ([s]).

If the string has length 1, any single nucleotide substitution is valid, returning all four bases (['A', 'C', 'G', 'T']).

Distance Budgeting:

If the suffix neighbor text has already used fewer than d mismatches relative to s[1:], the first position can be replaced with any nucleotide (A, C, G, or T).

If text has already exhausted all d allowed mismatches, the first position must strictly match the original first base s[0].

Deduplication: Uses a set() during construction to ensure each variant is unique before returning the final list.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



This algorithm finds all (k,d)-motifs shared across a collection of DNA sequences—identifying every k-mer that appears in every sequence in dna with at most d mismatches.

Biological Context: Regulatory sequences like transcription factor binding sites (TFBS) control gene expression across clusters of co-regulated genes. Because these binding sites are planted across upstream promoter regions of different genes, they are conserved yet degenerate (subject to point mutations). Motif enumeration solves the challenge of discovering these shared regulatory patterns across a set of related genomic sequences without prior knowledge of what the consensus motif looks like.

Algorithm Mechanism:

Candidate Generation: Any valid motif shared by all sequences must appear in the first sequence dna[0] with at most d mismatches. The algorithm extracts every k-mer from dna[0], builds its d-neighborhood via neighbors(), and collects these variants into a set of unique candidates.

Cross-Sequence Verification: For each candidate k-mer, has_approximate_match() checks whether an instance with ≤d mismatches exists within each remaining DNA sequence.

Pruning & Filtering: Using Python's all(), candidates that fail to appear in even one sequence are immediately discarded. Only those confirmed in every strand of dna are retained and returned.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


This algorithm computes the minimum number of coins needed to make a specific amount of money given a set of coin denominations.

Context & Motivation: A standard greedy approach (always picking the largest available coin) fails for arbitrary coin systems (e.g., making change for 40 with coins {25,20,10,5,1} gives 25+10+5 [3 coins] via greedy, but 20+20 [2 coins] is optimal). In bioinformatics, this problem serves as the introductory conceptual gateway to dynamic programming before tackling sequence alignment, string edit distances, and the Manhattan Tourist Problem.

Algorithm Mechanism:

Dynamic Programming (Bottom-Up Tabulation): It constructs an array min_num_coins of size money+1, where the entry at index m stores the minimum coins required to make change for amount m.

Base Case: min_num_coins[0] = 0 (zero coins needed to make change for 0). All other positions start at ∞.

Recurrence Relation: For every intermediate amount m from 1 to money and for each eligible coin (m≥coin):

min_num_coins[m]= 
coin
min
​
 (min_num_coins[m],min_num_coins[m−coin]+1)
Complexity: Runs in O(money⋅∣coins∣) time and consumes O(money) space.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


00 pattern count 
This algorithm computes the total number of times a specific k-mer (pattern) appears as a substring within a genomic sequence (text), accounting for overlapping occurrences.

Biological Context:
In computational genomics, identifying the origin of replication (oriC) begins with finding short, repeated DNA sequences (DnaA boxes) where initiator proteins bind to trigger replication. Because bacterial DNA replication machinery often targets repeated binding motifs clustered tightly together, accurately counting how frequently specific k-mers appear in a genome is the foundational step toward locating replication origins and identifying frequent regulatory words.

Algorithm Mechanism:

Sliding Window: It slides a window of fixed length k=len(pattern) across text from index 0 to ∣text∣−k.

Overlapping Evaluation: Unlike native string counting methods (such as Python’s .count(), which skips matched segments), extracting slices text[i:i + k] step-by-step ensures that overlapping occurrences (e.g., finding GCG twice in GCGCG) are fully captured.

Complexity: Runs in O((∣text∣−k+1)⋅k) time and requires O(1) additional space beyond substring slicing.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



00b frequent words

This algorithm finds the most frequently occurring $k$-mers of length $k$ in a genomic sequence (`text`).

Biological Context:
A single $k$-mer appearing randomly in a DNA sequence is not necessarily biologically meaningful, but a $k$-mer repeated unusually often within a replication origin (oriC) strongly suggests a biological function—specifically, a binding site for replication initiation proteins (such as DnaA boxes in *E. coli*). Identifying these frequent words helps pinpoint the exact binding motifs that cells use to regulate DNA replication.

Algorithm Mechanism:
- Frequency Map (Hash Table): Uses a dictionary to tally occurrences of every windowed substring of length $k$ across `text` in a single pass.
- Peak Frequency Extraction: Identifies `max_count` among all observed counts and collects all $k$-mers achieving this maximum value.
- Complexity:
  - Time Complexity: $O((\vert{}text\vert{} - k + 1) \cdot k)$ to extract and hash substrings of length $k$, plus $O(U)$ where $U \le 4^k$ is the number of unique $k$-mers to filter the maximal keys.
  - Space Complexity: $O(U \cdot k)$ auxiliary space to store unique $k$-mers in the dictionary.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


00c reverse complement

This algorithm computes the reverse complement of a given DNA sequence (`pattern`).

Biological Context:
DNA is double-stranded, oriented antiparallel (5' to 3' on one strand runs opposite to 3' to 5' on the other), and governed by Watson-Crick base pairing (A pairs with T, C pairs with G). Regulatory motifs such as DnaA binding boxes can reside on either the forward or the reverse strand. Because replication enzymes interact with double-stranded DNA, identifying candidate motifs requires searching for both a $k$-mer and its reverse complement.

Algorithm Mechanism:
- Complement Mapping: Maps each nucleotide to its base-pairing partner using a lookup dictionary: A $\leftrightarrow$ T and C $\leftrightarrow$ G.
- Directional Inversion: Iterates through the input string in reverse order (`reversed(pattern)`) to ensure the resulting sequence preserves the standard 5' to 3' reading direction.
- Complexity:
  - Time Complexity: $O(\vert{}pattern\vert{})$ to traverse and translate the sequence of length $\vert{}pattern\vert{}$.
  - Space Complexity: $O(\vert{}pattern\vert{})$ auxiliary space to construct and return the resulting reverse complement string.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

00d pattern matching

This algorithm locates all starting positions where a target sequence (`pattern`) occurs within a larger sequence (`genome`).

Biological Context:
Finding putative replication origins often requires locating every exact occurrence of a known regulatory motif (such as a 9-mer DnaA box) across an entire bacterial chromosome (e.g., *Vibrio cholerae*). By mapping the exact starting coordinates of these motifs, researchers can identify high-density clusters of binding sites, which typically mark the precise genomic location of *oriC*.

Algorithm Mechanism:
- Linear Scan (Exact Substring Matching): Slides a window of length $k = \text{len}(\text{pattern})$ across `genome` starting at index $0$ up to $\vert{}genome\vert{} - k$.
- Index Collection: Compares each genomic slice `genome[i:i + k]` against `pattern`. Whenever an exact match occurs, the 0-based starting index $i$ is appended to the results list.
- Overlapping Detection: Increments the index by $1$ after every comparison, ensuring that tandem or overlapping instances of the motif are detected.
- Complexity:
  - Time Complexity: $O((\vert{}genome\vert{} - k + 1) \cdot k)$ to extract and compare substrings across the genome.
  - Space Complexity: $O(M)$ auxiliary space, where $M$ is the number of matching indices recorded.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


00e find clumps

This algorithm finds all distinct $k$-mers that form an $(L, t)$-clump—appearing at least $t$ times within any sliding window of length $L$ across a given `genome`.

Biological Context:
Replication origins (*oriC*) are not characterized by solitary binding sites; rather, they contain dense clusters (clumps) of replication initiation motifs (DnaA boxes) packed within a relatively short region (typically around 500 base pairs). Finding clumps of $k$-mers that recur at least $t$ times inside an $L$-length window provides an unbiased, genome-wide scan to locate candidate *oriC* regions without requiring prior knowledge of the specific binding sequence.

Algorithm Mechanism:
- Sliding Window on Genome: Maintains a window of length $L$ moving across the genome from index $0$ to $\vert{}genome\vert{} - L$.
- Frequency Tracking (defaultdict): Computes the $k$-mer counts for the initial $L$-window. As the $L$-window slides right by 1 base at each step:
  - Decrements the count of the `outgoing` $k$-mer leaving the left boundary (`genome[i - 1 : i - 1 + k]`).
  - Increments the count of the `incoming` $k$-mer entering the right boundary (`genome[i + L - k : i + L]`).
- Clump Collection: Whenever an incoming $k$-mer's tally reaches or exceeds threshold $t$, it is added to a `set` to guarantee distinct results without duplicate reporting.
- Complexity:
  - Time Complexity: $O(L \cdot k + (\vert{}genome\vert{} - L) \cdot k) = O(\vert{}genome\vert{} \cdot k)$, drastically outperforming naive $O(\vert{}genome\vert{} \cdot L)$ window re-evaluations.
  - Space Complexity: $O(U \cdot k)$ auxiliary space, where $U \le 4^k$ is the number of distinct $k$-mers tracked in the frequency map.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


10 motif enumeration

This algorithm identifies all $(k, d)$-motifs—$k$-mers that appear in every sequence of a given collection of DNA strings with at most $d$ mismatches.

Biological Context:
Regulatory motifs (such as transcription factor binding sites) rarely appear as exact matches across different genes or organisms; evolutionary mutations introduce point mutations (substitutions). Consequently, finding conserved regulatory signals across a collection of upstream promoter regions requires searching for degenerate patterns that tolerate up to $d$ mismatches across every related sequence.

Algorithm Mechanism:
- Candidate Generation via $d$-Neighborhoods: Extracts every $k$-mer from the first DNA sequence and computes its $d$-neighborhood (all strings of length $k$ with Hamming distance $\le d$) using recursive neighborhood expansion. Every such neighbor serves as a candidate motif.
- Universal Sequence Validation: For each unique candidate, the algorithm checks whether an approximate match (Hamming distance $\le d$) exists within all remaining sequences in the dataset.
- Pruning and Filtering: Retains only candidates that appear with at most $d$ mismatches in every single sequence, returning the lexicographically sorted set of valid motifs.
- Complexity:
  - Candidate Generation: Generates at most $(|D_1| - k + 1) \cdot \binom{k}{d} 3^d$ candidates from the first sequence $D_1$.
  - Verification: Evaluating each candidate across $t$ sequences of length $N$ takes $O(t \cdot (N - k + 1) \cdot k)$ time.
  - Overall Time Complexity: $O\left(N \cdot \binom{k}{d} 3^d + |C| \cdot t \cdot N \cdot k\right)$, where $|C|$ is the number of unique candidates and $t$ is the number of sequences.
  - Space Complexity: $O(|C| \cdot k)$ auxiliary space to store candidate motifs and neighborhoods.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


11 median string

This algorithm finds a $k$-mer (`pattern`) that minimizes the total distance $d(\text{Pattern}, \text{DNA})$ across all sequences in a given DNA collection.

Biological Context:
When searching for regulatory motifs shared among co-regulated genes, transcription factor binding sites are rarely identical across promoters. Instead of demanding an exact motif match or a rigid threshold of mismatches, the median string approach searches for a consensus sequence that represents the evolutionary center—minimizing the total number of point mutations required to derive a binding site in every promoter sequence.

Algorithm Mechanism:
- Exhaustive Motif Search: Uses `itertools.product('ACGT', repeat=k)` to systematically evaluate all $4^k$ possible nucleotide combinations of length $k$.
- Sequence Distance Calculation: For each candidate $k$-mer, computes its distance to a single sequence by finding the minimum Hamming distance across all sliding windows of length $k$ (`distance_pattern_to_text`).
- Total Consensus Distance: Aggregates the minimum distances across all sequences in `dna` via $d(\text{Pattern}, \text{DNA}) = \sum d(\text{Pattern}, \text{seq})$.
- Median Selection: Tracks the minimal total distance and records the optimal $k$-mer that minimizes this sum.
- Complexity:
  - Search Space: Evaluates all $4^k$ possible candidates.
  - Evaluation Cost: Testing a single candidate against $t$ sequences of length $N$ takes $O(t \cdot (N - k + 1) \cdot k)$ operations.
  - Overall Time Complexity: $O(4^k \cdot t \cdot N \cdot k)$, where $t$ is the number of sequences and $N$ is their average length.
  - Space Complexity: $O(k)$ auxiliary space to generate and maintain candidate strings.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


