#!/usr/bin/python
# -*-coding:utf-8-*-

#wikipediaから取得した単語リストを綺麗にするスクリプト
import sys
import re

def wiki_extract(input_text):
    for line in open(input_text):
        line = line.strip()
        if line == "":
            continue
        if line[0] == "*":
            continue
        if "\\n" in line:
            line = line.split("\\n")[1]
        if "(" in line:
            line = re.split("\(.+", line)[0]
        print line
        if line[0] == "<":
            continue
        print line

if __name__ == "__main__":
    wiki_extract(sys.argv[1])
