TopMap-SD
=========

A Shape-Distribution-based molecular topology mapping algorithm.


The software provided here is to be described soon in detail under the putative title:

"A fast topological analysis algorithm for large-scale similarity evaluations for ligands
and binding pockets"

Authors: Mohammad ElGamacy and Luc Van Meervelt.



Additional modification or custom updates requests are welcome and can
be communicated to the following email address: 

mohammad.elgamacy@vub.ac.be

Usage
=====

TopMap hashes molecular topolgies into a series of moments.
Molecular vectors records are generated in ./outfile.dat

- Input structural coordinates must be provided in mol2 format
    with the atomic partial charges assigned and preferrably
    exported/reformatted using OpenBabel.
    Essential records (@<TRIPOS):
        - MOLECULE
        - ATOM
        - BOND
- Input mol2 files can be input as gzipped (i.e. ".mol2.gz") files
- Output file contains the molecular descriptor vectors
    in text format (for portability reasons; UTF-8).
- Output data is flushed after each molecular calculations loop
    cycle, thus, the output file completeness can provide and
    indication of the computation progress.

Usage:
topmap[.exe] mol2_input_file[.gz]

Example
=======

An example scenario on a dataset from the DUD-E is presented below:

The example will shows the main steps of structural fingerprinting (without any conformational sampling steps) and running a simple search using a random query structure.

