import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

gene_color_dict = {
    'A':'b',
    'C':'r',
    'G':'g',
    'T':'y',
    }

padding = 0.5

def plot_genome_features(genome,feature_dicts=None, annotate=False):


    meta_labels = []

    fig = plt.figure(figsize=(10,5))
    ax1 = fig.add_subplot(111)

    #simply plotting genome and coloring by nucleotide
    #TODO: color by amino acid, electronegativity, hydophobicity etc.
    for g in gene_color_dict.keys():
        mask = [i for i in xrange(len(genome)) if genome[i] == g]
        ax1.scatter(mask,np.ones(len(mask))*.75,c=gene_color_dict[g],marker='s',s=5)
        if annotate == True:
            for m in mask:
                ax1.annotate(g, xy=(m-.5, .5), xytext=(m, .5),fontsize=5)

    # are we just plotting the genome?
    if isinstance(feature_dicts,list):

        heights = range(1,len(feature_dicts)+1) # heights to plot everything at
        n_elements = sum([1 for sublist in feature_dicts for item in sublist])
        colors = plt.cm.viridis(np.linspace(0, 1, n_elements)) #colors to plot things
        np.random.shuffle(colors) # gradient makes it hard to pick out colors
        print len(colors)
        c=0
        for this_height,this_feature in zip(heights,feature_dicts):
            if isinstance(this_feature,list):

                #there are sub_features to this feature

                sub_heights = np.arange(0,padding,padding/len(feature_dicts))
                meta_labels.append(this_feature[0][this_feature[0].keys()[0]]['meta_label'])
                for this_sub_height,feature_dict in zip(sub_heights,this_feature):
                    my_height = this_height+this_sub_height

                    for sub_feature in feature_dict.keys():
                        first=True
                        for start,stop in zip(feature_dict[sub_feature]['start_inds'],feature_dict[sub_feature]['stop_inds']):
                            if isinstance(start,int):
                                ax1.plot([start,stop],[my_height,my_height],color=colors[c], linewidth=3, label=feature_dict[sub_feature]['label'] if first == True else None)

                                first=False
                        c+=1

            elif isinstance(this_feature,OrderedDict):
                meta_labels.append(this_feature[this_feature.keys()[0]]['meta_label'])
                #there are no sub_features to this feature
                if 'custom label' in this_feature.keys():
                    my_label = this_feature['custom label']
                else:
                    my_label= 'unlabeled feature'
                first=True
                for sub_feature in this_feature.keys():
                    print sub_feature

                    for start,stop in zip(this_feature[sub_feature]['start_inds'],this_feature[sub_feature]['stop_inds']):
                        if isinstance(start,int):
                            ax1.plot([start,stop],[this_height,this_height],color=colors[c], linewidth=3,label=this_feature[sub_feature]['label'] if first == True else None)
                            first=False
                    c+=1


    ax1.set_xticks(np.arange(0,len(genome),len(genome)/10)) # a reasonable number of ticks
    ax1.set_xlabel('Nucleotide number')
    ax1.set_ylim([0,max(heights)+1])
    ax1.set_yticks(heights)
    ax1.set_yticklabels(meta_labels)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.xaxis.set_ticks_position('bottom')

    # Put a legend to the right of the current axis
    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))


def plot_match_count(match_count):

    fig = plt.figure(figsize=(10,5))
    ax1 = fig.add_subplot(111)

    ax1.plot(match_count,linewidth=2)

    ax1.set_xticks(np.arange(0,len(match_count),len(match_count)/10)) # a reasonable number of ticks
    ax1.set_xlabel('Nucleotide number')
    ax1.set_ylabel('Number of matching Nucleotides')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.xaxis.set_ticks_position('bottom')



