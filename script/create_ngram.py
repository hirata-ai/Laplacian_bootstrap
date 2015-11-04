#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

def create_ngram(n, mecab_data):
    line_count = 0
    sent_list = []
    for line in open(mecab_data):
        line = line.strip()
        if line == "":
            continue
        # line_count += 1
        # print line, line_count 
        if line[0] == "<":
            continue
        if line != "EOS":
            mecab_result = line.split("\t")
            word, morph = mecab_result[0], mecab_result[3]
            sent_list.append((word, morph))
            # print sent_list
        if line == "EOS":
            # line_count = 0
            # if len(sent_list) < n:
            #     sent_list = []
            #     continue
            # print len(sent_list)
            for num in range(0, n//2):
                sent_list.insert(0, ("</b>", ""))
                sent_list.append(("</e>", ""))
            for num in range(n//2 + 1, len(sent_list) - n//2):
                # print num
                # print sent_list[num][0], sent_list[num][1]
                if "名詞" in sent_list[num][1] and "名詞-数" not in sent_list[num][1] and "記号" not in sent_list[num][1]:
                    # print sent_list[num][0], sent_list[num][1]
                    # print sent_list[num][0]
                    print "{}\t{} {}\t{} {}".format(sent_list[num][0], sent_list[num-2][0], sent_list[num-1][0], sent_list[num+1][0], sent_list[num+2][0])
            sent_list = []

if __name__ == "__main__":
    #python create_ngram.py /work/hirata/wiki_2015/wiki_mecab.txt > /work/hirata/wiki_2015/wiki_5gram.txt
    n = 5
    create_ngram(n, sys.argv[1])
