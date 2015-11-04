#!/usr/bin/python
# -*-coding:utf-8-*-

import sys
import glob
from collections import defaultdict
import pickle

def count_wikinoun(mecab_data):
    count_noun = defaultdict(int)
    # for dir_name in glob.glob("/Users/hirataai/tensor/data/Wikipedia/wiki_mecab/*"):
    #     file_name = dir_name + "/*"
    #     for mecab_data in glob.glob(file_name):
    #         doc_id = ""
    #         # print mecab_data
    for line in open(mecab_data):
        if line != "EOS":
            mecab_result = line.split("\t")
            # print mecab_result
            if len(mecab_result) < 4:
                continue
            word, morph = mecab_result[0], mecab_result[3]
            if "名詞" in morph:
                count_noun[word] += 1
            # sent_list.append((word, morph))
            # print sent_list
        if line == "EOS":
            continue
    # f = open("/Users/hirataai/tensor/data/Wikipedia/data/wiki_noundict.dunp", "w")
    # pickle.dump(count_noun, f)
    
    for ins, count in sorted(count_noun.items(), key=lambda x:x[1], reverse=True):
        print "{}\t{}".format(ins, count)


if __name__ == "__main__":
    count_wikinoun(sys.argv[1])
