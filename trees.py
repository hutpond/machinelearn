#!/usr/bin/python

""" machine learn tree """

from math import log

def calc_shannon_ent(data_set):
    """ calculate Shannon Entropy
    """
    num_entries = len(data_set)
    label_counts = {}
    for featvec in data_set:
        current_label = featvec[-1]
        if current_label not in label_counts.keys():
            label_counts[current_label] = 0
        label_counts[current_label] += 1
    shannon_ent = 0.0
    for key in label_counts:
        prob = float(label_counts[key]) / num_entries
        shannon_ent -= prob * log(2, prob)
    return shannon_ent

def create_data_set():
    """ Create setting data
    """
    dataset = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataset, labels

if __name__ == '__main__':
    DATA, LABELS = create_data_set()
    ENTROPY = calc_shannon_ent(DATA)
    print(ENTROPY)
