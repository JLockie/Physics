
RandomOverlappingWalks

An efficient method to sample polymer configurations is known as the "slithering snake". In this algorithm, one distinguishes both ends of the polymer: one is called the "head" and the other is the "tail". The algorithm then proceeds as follows:

   1. Remove the monomer (or final link) at the tail.
   2. Attempt to add a monomer to the head of the polymer, on one of the lattice sites which is a nearest-neighbor of the last monomer, excluding the site occupied bythe second-last monomer.
   3. If the attempt violates self-avoidance, return to the original configuration but interchange which end is the head and which is the tail.
   4. At every step, randomly decide which end is the head and which the tail. Formulate a code that operates to create a two-dimensional self-avoiding random walk using this algorithm. Run this code for 1000 such random walks. Plot the average squared end-to-end length of the polymer vs time.

