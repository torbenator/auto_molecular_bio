import random
from collections import OrderedDict
promotors = {}

start_codons = ['ATG']
stop_codons = ['TAA','TAG','TGA']

common_promoters = {
    'T7':'TAATACGACTCACTATAGG',
    'SP6':'ATTTAGGTGACACTATAG',
    'T3':'ATTAACCCTCACTAAAGGG'
}



def generate_gene_sequence(g_length, features=None):

    gene_sequence = ''.join([random.choice("GCTA") for _ in xrange(g_length)])

    if features is None:
        return gene_sequence

    else:
        for feature_dict in features:
            gene_sequence = gene_sequence[:feature_dict['placement']]+feature_dict['sequence']+gene_sequence[feature_dict['placement']+len(feature_dict['sequence']):]
        return gene_sequence


