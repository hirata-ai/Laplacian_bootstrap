#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab as mecab

def wiki_mecab(wiki_data):
    for line in open(wiki_data):
        line = line.strip()
        if line == "" or line[0] == "<":
            if line == "</doc>":
                continue
            print line
            continue
        mt = mecab.Tagger("-Ochasen")
        print mt.parse(line)
    
if __name__ == "__main__":
    wiki_mecab(sys.argv[1])
