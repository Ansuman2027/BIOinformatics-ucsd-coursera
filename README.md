# University of California San Diego Bioinformatics Algorithms (Coursera)
<img width="1920" height="975" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/68409768-01a7-41b6-ad0d-78c4e69ea532" />

### Finding Hidden Messages in DNA (Bioinformatics I)

This repository contains my Python solutions to the algorithmic challenges from the UC San Diego Coursera Bioinformatics Specialization and Cogniterra platform. I wrote these scripts to understand how we can decode biological data programmatically covering everything from finding where DNA replication starts to building motif finders and dynamic programming algorithms.

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Ansuman2027/BIOinformatics-ucsd-coursera)

---


## 1. Origin of Replication & Skew Analysis

when a cell divides, it has to replicate its entire DNA. In circular bacterial genomes, this process starts at a specific spot called oriC. Because DNA replication happens asymmetrically on the leading and lagging strands, bases mutate differently over time specifically, Guanine tends to drop off on the lagging strand template.

* **01minimum skew.py**: This script tracks the cumulative skew score (G minus C count) step by step across the whole genome. The  spot where the skew graph hits its lowest point and starts giong back up gives  a reliable way to pinpoint where oriC is located.

---

## 2. Exact & Approximate String Matching

Proteins like DnaA and various transcription factors need to attach to specific short stretches of DNA (like DnaA boxes) to start biological processes. But these binding sites are not 100% identical everywhere, so we need tools that can search for exact matches as well as patterns with a few mutations.

* **00 pattern count.py**:  sliding window counter that checks how many times a target k-mer appears in a sequence, making sure it handles overlapping matches correctly.
 **00b frequent words.py**: Uses a dictionary/hash map to scan through windows and figure out which k-mers show up most often, which usually points  toward functional regulatory zones.
* **00c reverse complement.py**: Takes a DNA string and flips it into its antiparallel reverse complement following standard Watson-Crick pairing rules (A to T, C to G).
* **00d pattern matching.py**: Scans through an entire genome linearly to grab all the 0-based starting indexes where an exact target pattern appears.
* **00e find clumps.py**: scans a genome of length L to find clumps meaning k-mers that cluster together by appearing at least a set number of times inside that localized window.
* **02 hamming distance.py & 17 hamming distance utility.py**: Compares two strings of the exact same length side by side using code to count up how many mismatched letters there are.
* **03 approx pattern matching.py & 18 approx pattern matching utility.py**: Scans a genome to find all positions where a pattern matches with up to a specified number of mismatches allowed.
 **04 approx pattern count.py & 19 approx pattern count utility.py**: Counts the total frequency of a pattern across a sequence while factoring in substitutions.
* **07Generate the d-Neighborhood of a String.py & 16 generating neighborhood.py**: Recursively builds out the full mutational neighborhood every single valid k-mer that sits within a Hamming distance from a starting seed.
* **05frequent words with mismatches.py & 20 frequent words with mismatches utility.py**: Combines sliding windows with neighborhood generation to find the most common degenerate k-mers even when mutations are present.
* **06Frequent Words with Mismatches and Reverse Complements Problem.py & 21 frequent words mismatches reverse complements utility.py**: Searches for consensus motifs by tallying approximate matches across both the forward strand and its reverse complement at the same time, mimicking how double stranded DNA actually works .

---

## 3. Regulatory Motif Discovery
<img width="865" height="294" alt="GBTRGGGMCNRAMGTCCCCN" src="https://github.com/user-attachments/assets/adcc3f21-f989-4a85-85d7-006bfe3187f1" />

When cells respond to stress they turn on whole groups of genes at once by binding transcription factors to shared promoter regions upstream. Because these sequence motifs are short and noisy these scripts explore different ways to find them.

* **08Motif Enumeration Problem.py & 10 motif enumeration.py**:  script that checks every possible motif variant to see which ones appear across all input sequences with at most a set number of mismatches.
* **11 median string.py**: Tests all possible nucleotide combinations to find the single consensus sequence that keeps the total Hamming distance across all promoter sequences as low as possible
* **12 profile most probable kmer.py**: Takes a Position Weight Matrix probability profile and scans a DNA string to select the k-mer with the highest joint probability score
* **13 greedy motif search.py**: A greedy approach that starts by selecting candidate k-mers from the first sequence, builds an evolving profile matrix, and picks the best matching choices in every subsequent sequence.
* **14 greedy motif search with pseudocounts.py**: Upgrades the greedy search by adding pseudocounts (Laplace's Rule of Succession). This ensures that if a nucleotide has not been seen yet its probability does not drop to zero preventing division errors
* **15 distance between pattern and strings.py**: Calculate the cumulative distance metric by summing up the shortest Hamming distances between a pattern and every individual sequence in a dataset.
* **23 randomized motif search utility.py**: A Monte Carlo Expectation Maximization approach. It starts with random starting motifs, builds probability profiles with pseudocounts, and iteratively refines them until it converges, running multiple random restarts to avoid getting stuck in local optima
* **24 gibbs sampling utility.py**: A Markov Chain Monte Carlo sampling heuristic. Instead of updating everything at once, it leaves one sequence out, builds a profile from the rest, and stochastically samples a new motif to gradually zero in on the best alignment.

---

## 4. Dynamic Programming Foundations

Sequence alignment and dynamic programming approaches rely on breaking complex problems down into overlapping subproblems

* **09The Change Problem.py & 22 change problem utility.py**: Solves  coin change problem using bottom up tabulation to find the minimum coins needed for any given amount. This serves as the foundational logic for building up to biological sequence alignment algorithms like Needleman Wunsch and Smith Waterman.
