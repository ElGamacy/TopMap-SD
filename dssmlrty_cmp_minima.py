import re
import sys
import numpy as np
#import scipy.spatial.distance as dist

##########################
# atom records extractor #
######################################################################
def usage():

    s = """Calculates the Manhattan distance and prints our the top 
N most similar hits.

<target_index>: is the order of query molecule hash line in the input hashes file (i.e. the line number)


Usage:
# <dssmlrty_cmp>.py <target_index> <top_hits_number> <fp_file_name>
(e.g: dssmlrty_cmp_v04_mtrx.py 0 10000 all_mmnts_comt.log)

"""
    print(s)
######################################################################

##########################
# atom records extractor #
######################################################################
def extract_mmnts(line):

    raw_mmnts_ln = re.split('\s+', line.strip())
    raw_mmnts_arr = np.array(raw_mmnts_ln[1:]).astype(np.float32)
    mmnts_lst = [raw_mmnts_ln[0], raw_mmnts_arr]
    return mmnts_lst
######################################################################

####################################
# dissimilarity score calculation  #
######################################################################
def manhattan(mmnts_arr_1, mmnts_arr_2):

    man_dist = np.sum(np.abs(mmnts_arr_1 - mmnts_arr_2))
    return  man_dist
######################################################################

if __name__ == '__main__':
    try:
        i1 = int(sys.argv[1])
        i2 = int(sys.argv[2])
        in_fn = str(sys.argv[3])
        in_fl = open(in_fn, 'r')
    except:
        print("input or file open error,,, revise \'usage\'")
        usage()
        sys.exit()

################
# read moments #
######################################################################
mols_lst = [] # element is [mol_name, mmnts_arr]

for line in in_fl:
    if extract_mmnts(line):
        temp_mol = extract_mmnts(line)
        mols_lst.append(temp_mol)
######################################################################

top_str = ''
scr_lst = []
qry_mol = mols_lst[i1-1]
for trgt_mol in mols_lst:
    #tmp_pair = [trgt_mol[1], qry_mol[1]]
    #tmp_scr = float(dist.pdist([trgt_mol[1], qry_mol[1]], 'cityblock'))
    tmp_scr = manhattan(trgt_mol[1], qry_mol[1])
    scr_lst.append([tmp_scr, qry_mol[0], trgt_mol[0]])
print("Query structure name: " + qry_mol[0])
scr_lst.sort()
for k in scr_lst[0:i2-1]:
    top_str = top_str + str(k[2]) + ' ' + str(k[0]) + '\n' 
print(top_str)

