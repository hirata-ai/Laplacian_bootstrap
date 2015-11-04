#!/usr/bin/python
# -*-coding:utf-8-*-

import sys
import glob
from collections import defaultdict

def ngram_count(ngram_data):
    ngram_dic = defaultdict(int)
    # for dir_name in glob.glob("/work/hirata/wiki_2015/wiki_5gram/*"):
    #     file_name = dir_name + "/*"
    # for ngram_data in glob.glob(file_name):
    for line in open(ngram_data):
        line = line.strip()
        ngram_dic[line] += 1
    
    for ngram, number in sorted(ngram_dic.items(), key=lambda x:x[1], reverse=True):
        print "{}\t{}".format(ngram, number)

if __name__ == "__main__":
    ngram_count(sys.argv[1])
