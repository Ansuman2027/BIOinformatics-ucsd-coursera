# University of California San Diego Bioinformatics Algorithms (Coursera)

 

A collection of Python implementations solving foundational problems in computational molecular biology. These scripts mirror the core algorithmic challenges covered in the UC San Diego , Coursera *Bioinformatics Specialization*, focusing on replication origin discovery, motif finding, pattern matching, and dynamic programming.

---

## Overview & Thematic Breakdown

### 1. Origin of Replication & Skew Analysis
Bacterial genomes initiate replication at a specific locus called $oriC$. Because DNA replication is asymmetric (leading vs. lagging strands), mutational pressures cause distinct nucleotide depletions—most notably, Guanine ($G$) tends to mutate into other bases on the lagging strand template.

* `01minimum skew.py`: Tracks the cumulative skew metric (#G - #C) across a linear scan of the genome. The point where the skew transitions from decreasing to increasing marks the minimum skew, providing an accurate estimate for the location of $oriC$.

---

### 2. Exact & Approximate String Matching
Regulatory sequences like DnaA boxes rarely stay 100% identical over evolutionary timescales; proteins recognize short binding sites even when a few point mutations (substitutions) occur.

* `00 pattern count.py`: A sliding-window counter that finds how often a specific $k$-mer occurs in a string, ensuring overlapping instances (like `GCG` inside `GCGCG`) are properly counted.
* `00b frequent words.py`: Uses a hash map to find the most frequent $k$-mers in a sequence. High-frequency words inside putative origin regions often correspond to functional binding sites.
* `00c reverse complement.py`: Generates the antiparallel reverse complement of a DNA string according to standard Watson-Crick pairing rules ($A \leftrightarrow T$, $C \leftrightarrow G$).
* `00d pattern matching.py`: A linear scan identifying all 0-based start coordinates of an exact target sequence across an entire genome.
* `00e find clumps.py`: Implements an efficient sliding window across a genome of length $L$ to locate $(L, t)$-clumps—$k$-mers appearing at least $t$ times within that local window.
* `02 hamming distance.py` & `17 hamming distance utility.py`: Compares two equal-length strings character-by-character using `zip()` to count mismatched positions.
* `03 approx pattern matching.py` & `18 approx pattern matching utility.py`: Locates all positions where a $k$-mer appears with at most $d$ mismatches (Hamming distance $\le d$).
* `04 approx pattern count.py` & `19 approx pattern count utility.py`: Tally of how many times a pattern appears allowing up to $d$ mismatches.
* `07Generate the $d$-Neighborhood of a String .py` & `16 generating neighborhood.py`: Recursively constructs the complete mutational search space (the $d$-neighborhood)—all distinct $k$-mers within Hamming distance $d$ of a seed sequence.
* `05frequent words with mismatches.py` & `20 frequent words with mismatches utility.py`: Combines sliding windows and neighborhood generation to identify the most abundant degenerate $k$-mers in a sequence.
* `06Frequent Words with Mismatches and Reverse Complements Problem.py` & `21 frequent words mismatches reverse complements utility.py`: Identifies consensus motifs by counting approximate matches simultaneously on both the forward and reverse-complement strands, accurately modeling double-stranded DNA protein binding.

---

### 3. Regulatory Motif Discovery
Transcription factors regulate batteries of genes by binding conserved promoter regions upstream of transcription start sites. These scripts explore multiple algorithmic strategies to isolate shared signals hidden across multiple DNA sequences.

* `08Motif Enumeration Problem.py` & `10 motif enumeration.py`: A brute-force exhaustive search that identifies all $(k, d)$-motifs present in every sequence of a dataset with at most $d$ substitutions.
* `11 median string.py`: Searches all $4^k$ possible nucleotide permutations to locate the consensus sequence that minimizes total Hamming distance across a set of promoter sequences.
* `12 profile most probable kmer.py`: Evaluates a nucleotide profile probability matrix (Position Weight Matrix) to identify the $k$-mer with the highest joint probability in a sequence.
* `13 greedy motif search.py`: Uses an iterative greedy strategy: sets a seed motif in the first sequence, constructs an evolving profile, and picks the best matching motif in each subsequent sequence.
* `14 greedy motif search with pseudocounts.py`: Refines greedy search by incorporating Laplace’s Rule of Succession (pseudocounts). Adding $+1$ to all nucleotide observation counts prevents unseen bases from dropping whole profile probabilities to zero.
* `15 distance between pattern and strings.py`: Computes the cumulative distance metric $d(\text{Pattern}, \text{DNA})$ by summing the closest match distances across all sequences in a collection.
* `23 randomized motif search utility.py` : A Monte Carlo Expectation-Maximization approach. It starts with random motif candidates, builds profile matrices with pseudocounts, and iteratively refines choices until local convergence, utilizing multiple restarts to find optimal global consensus scores.
* `24 gibbs sampling utility.py`: A Markov Chain Monte Carlo (MCMC) heuristic that updates one sequence at a time. By leaving one sequence out, computing a profile on the remaining $t-1$ motifs, and stochastically sampling a replacement motif, it effectively navigates around local minima.

---

### 4. Dynamic Programming Foundations
Sequence alignment methods rely on breaking problems into overlapping subproblems rather than relying on myopic greedy choices.
----+++
- `09The Change Problem.py` & `22 change problem utility.py`: Solves the classic coin change problem using bottom-up tabulation:

```text
min_coins[m] = min(min_coins[m - coin] + 1) for coin in coins


