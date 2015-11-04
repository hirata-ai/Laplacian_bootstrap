#!/usr/bin/python
# -*-coding:utf-8-*-

#二つのファイルを読み込んで重複をカウントする
import sys

def count_overlap(file1, file2):
    file1_dic = {}
    for line in open(file1):
        line = line.strip()
        if line not in file1_dic:
            file1_dic[line] = 1

    for line in open(file2):
        line = line.strip()
        if line in file1_dic:
            print line

if __name__ == "__main__":
    count_overlap(sys.argv[1], sys.argv[2])
