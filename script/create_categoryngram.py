#!/usr/bin/python
#-*-coding:utf-8-*-

import glob
import sys

def read_number(input_file):
    wiki_no_list = []
    for line in open(input_file):
        line = line.strip()
        number = line.split("\t")
        wiki_no_list.append(number[0])

    # for no in wiki_no_list:
    #     print no
    return(wiki_no_list)

def create_ngram(n, wiki_no_list):
    for dir_name in glob.glob("/Users/hirataai/tensor/data/Wikipedia/wiki_mecab/*"):
        file_name = dir_name + "/*"
        for mecab_data in glob.glob(file_name):
            doc_id = ""
            # print mecab_data
            line_count = 0
            sent_list = []
            for line in open(mecab_data):
                if "<doc id=" in line:
                    doc_id = line.split("\"")[1]
                    # print doc_id
                    continue
                if doc_id in wiki_no_list:

                    line = line.strip()
                    if line == "":
                        continue
                    # line_count += 1
                    # print line, line_count 
                    if line != "EOS":
                        mecab_result = line.split("\t")
                        # print mecab_result
                        if len(mecab_result) < 4:
                            continue
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
                        for num in range(n//2, len(sent_list) - n//2):
                            # print num
                            # print sent_list[num][0], sent_list[num][1]
                            if "名詞" in sent_list[num][1]:
                                # print sent_list[num][0], sent_list[num][1]
                                # print sent_list[num][0]
                                print "{}\t{} {}\t{} {}".format(sent_list[num][0], sent_list[num-2][0], sent_list[num-1][0], sent_list[num+1][0], sent_list[num+2][0])
                        sent_list = []

if __name__ == "__main__":
    n = 5
    wiki_no_list = read_number(sys.argv[1])
    create_ngram(n, wiki_no_list)
