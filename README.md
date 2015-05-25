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

This illustration was made for an Ubuntu system. Example mol2 files can be downloaded from any target dataset from the DUD-E (http://dude.docking.org/targets)

# step 1:
### download and extract the zipped package
unzip TopMap-SD-master

# step 2:
### fingerprint generation on a linux system
cd TopMap-SD-master/TopMap_v0.1linux_x86_64/
### fiingerprinting actives:
./TopMap_v0.1linux ../../actives_final.mol2 
### fiingerprinting decoys:
./TopMap_v0.1linux ../../decoys_final.mol2 
### contactenate output files:
cd ../../
cat actives_final.dat decoys_final.dat > all_fp.dat

# prerequisite:
Numpy library must be installed (http://www.numpy.org/) for the next step

# step 3:
### calculating dissimilarity and ranking similar molecules to a query and printing out the results to the stdout
### this calculates the command prints out the names and dissimilarity scores of top 50 similar hits using the first structure in the file (i.e. number 1) as query
Python TopMap-SD-master/dssmlrty_cmp_minima.py 1 50 all_fp.dat
