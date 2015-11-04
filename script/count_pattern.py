#!/usr/bin/python
# -*-coding:utf-8-*-

import sys
from collections import defaultdict
import pickle

def wiki_count_pattern(ngram_data):
    count_pattern = defaultdict(int)
    for line in open(ngram_data):
        line = line.strip()
        line_split = line.split("\t")
        instance = line_split[0]
        pattern  = "{}\t{}".format(line_split[1], line_split[2])
        count    = int(line_split[-1])
        count_pattern[pattern] += count
    # f = open("/Users/hirataai/tensor/data/Wikipedia/data/wiki_noundict.dunp", "w")
    # pickle.dump(count_noun, f)
    
    for pat, count in sorted(count_pattern.items(), key=lambda x:x[1], reverse=True):
        print "{}\t{}".format(pat, count)


if __name__ == "__main__":
    wiki_count_pattern(sys.argv[1])
