import numpy as np
import re
from collections import OrderedDict


def _calc_frame_shifts(inds,assume_0_ind=True):
    return [np.mod(ind) for ind in inds]


def find_perfect_match(genome,match_me,custom_label=None,meta_label=None,consider_fshift=True):


    inds = [g.start() for g in re.finditer(match_me, genome)]

    if consider_fshift:
        inds = [i for i in inds if np.mod(i,3)==0]

    match_dict = OrderedDict()

    match_dict[match_me] = dict()
    match_dict[match_me]['start_inds'] = inds
    match_dict[match_me]['stop_inds'] = [i+len(match_me) for i in inds]

    if custom_label is None:
        match_dict[match_me]['label'] = match_me
    else:
        match_dict[match_me]['label'] = custom_label

    if meta_label is None:
        match_dict[match_me]['meta_label'] = 'unlabeled feature'
    else:
        match_dict[match_me]['meta_label'] = meta_label

    return match_dict


def find_all_perfect_matches(genome,match_us,custom_labels=None,meta_label=None):

    match_dicts = []
    if meta_label is None:
        meta_label = "unlabeled feature"

    if isinstance(custom_labels,list):
        for match_me,label in zip(match_us,custom_labels):
            this_dict=find_perfect_match(genome,match_me, custom_label=label, meta_label=meta_label)
            match_dicts.append(find_perfect_match(genome,match_me, custom_label=label, meta_label=meta_label))

    else:
        for match_me in match_us:
            match_dicts.append(find_perfect_match(genome,match_me, meta_label=meta_label))

    return match_dicts

def n_matches_sw(genome,match_me,metric='sum'):

    match_count=np.zeros(len(genome)-len(match_me))

    for sw in xrange(len(genome)-len(match_me)):
        this_seg = genome[sw:sw+len(match_me)]
        match_count[sw] = np.sum([1 for i,j in zip(match_me,this_seg) if i ==j])

    if metric == 'pct':
        match_count = match_count/float(len(match_me))

    return match_count

def compare_genes(gene1,gene2):

    diff_dict = OrderedDict()

    #look for SNPs


    return diff_dict




