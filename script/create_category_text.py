#!/usr/bin/python
# -*-coding:utf-8-*-

import sys
import glob

def create_category_text(input_file):
    wiki_no_list = []
    for line in open(input_file):
        line = line.strip()
        number = line.split("\t")
        wiki_no_list.append(number[0])

    for dir_name in glob.glob("/Users/hirataai/tensor/data/Wikipedia/wiki_mecab/*"):
        file_name = dir_name + "/*"
        for mecab_data in glob.glob(file_name):
            doc_id = ""
            # print mecab_data
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
                        # word, morph = mecab_result[0], mecab_result[3]
                        # sent_list.append((word, morph))
                        # print sent_list
                        print line
                    if line == "EOS":
                        print line

if __name__ == "__main__":
    create_category_text(sys.argv[1])
