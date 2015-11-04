#!/usr/bin/python
# -*-coding:utf-8-*-

import sys
from collections import defaultdict

def count_ngram(input_file):
    ngram_dic = defaultdict(int)
    for line in open(input_file):
        line = line.strip()
        ngram_dic[line] += 1

    for ngram, number in sorted(ngram_dic.items(), key=lambda x:x[1], reverse=True):
        print "{}\t{}".format(ngram, number)

if __name__ == "__main__":
    count_ngram(sys.argv[1])
