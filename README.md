Biological Context: In bacterial genomes, DNA replication starts at the origin of replication (oriC). Due to differences in mutation rates between the leading and lagging strands, Guanine (G) tends to be depleted relative to Cytosine (C) on the reverse half of the replication loop. The point where the cumulative difference between G and C (#G−#C) transitions from decreasing to increasing—the minimum skew—typically identifies the location of oriC.

Algorithm Mechanism:

It performs a single linear scan (O(n) time complexity) through the sequence.

It increments the skew count by +1 for G, decrements by −1 for C, and leaves it unchanged for A and T.

It dynamically tracks the lowest skew value seen so far and collects all 1-based indices that achieve this minimum.
