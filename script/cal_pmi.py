#!/usr/bin/python
# -*-coding:utf-8-*-

#pmiを計算してarrayを作るスクリプト

from collections import defaultdict
import pickle
import math
import numpy as np
from scipy.sparse import csr_matrix
from scipy.io import mmwrite

# def cal_pmi(mecab_file, pattern_file):
def cal_pmi(pattern_file, instance_file, pat_ins_file):
    instance_dic    = defaultdict(int)
    pattern_dic     = defaultdict(int)
    instance_index  = defaultdict(int)
    pattern_index   = defaultdict(int)
    pattern_ins_dic = defaultdict(dict)
    pmi_dic         = defaultdict(float)

    counts = 0
    for line in open(pattern_file):
        line = line.strip()
        pattern_list = line.rsplit("\t", 1)
        pattern = pattern_list[0]
        pattern_count = pattern_list[1]
        pattern_dic[pattern] = int(pattern_count)
        pattern_index[pattern] = counts
        counts += 1
    pattern_dump = open("pattern_index.pickle", "w")
    pickle.dump(pattern_index, pattern_dump)
    print "pattern readed."

    counts = 0
    for line in open(instance_file):
        line = line.strip()
        instance_list = line.split("\t")
        instance = instance_list[0]
        instance_count = instance_list[1]
        instance_dic[instance] = int(instance_count)
        instance_index[instance] = counts
        counts += 1
        # print instance,instance_count
    instance_dump = open("instance_index.pickle", "w")
    pickle.dump(instance_index, instance_dump)
    print "instance readed."

    max_pmi = None
    for line in open(pat_ins_file): #パターンと共起するインスタンスが一つしかないものや，頻度の少ないものは削除する
        line = line.strip()
        list_split = line.split("\t")
        instance = list_split[0]
        count = int(list_split[-1])
        pattern = "{}\t{}".format(list_split[1], list_split[2])

        if count < 10:
            continue

        pmi = math.log((float(instance_dic[instance])*float(pattern_dic[pattern])/count), 2)
        pattern_ins_dic[pattern][instance] = pmi
        # print pmi
        # M[instance_index[instance], pattern_index[pattern]] = pmi
        if max_pmi == None:
            max_pmi = pmi
        elif max_pmi < pmi:
            max_pmi = pmi
    print "pattern_instance readed."

    # for i in ins_pattern_dic:
    #     for j in ins_pattern_dic[i]:
    #         print i, j, ins_pattern_dic[i][j]

    # M = sparse.lil_matrix((len(instance_index), len(pattern_index)))
    data    = []
    row  = []
    col = []
    for pat, count in sorted(pattern_index.items(), key=lambda x:x[1]):
        if len(pattern_ins_dic[pat]) > 1:
            for ins in pattern_ins_dic[pat]:
                data.append(pattern_ins_dic[pat][ins]/max_pmi)
                row.append(instance_index[ins])
                col.append(pattern_index[pat])
        #     mini_data.append(pattern_ins_dic[ins][pat]/max_pmi)
        #     indices.append(pattern_index[pat])
        # data.extend(mini_data)
        # indptr.append(len(mini_data))

    data    = np.array(data)
    row  = np.array(row)
    col = np.array(col)
    # instance_dic = None
    # instance_index = None
    # pattern_dic = None
    # pattern_index = None
    
    M = csr_matrix((data, (row, col)), shape=(len(instance_index), len(pattern_index)))

    #できた行列Mの書き出し
    mmwrite("wiki_pattern_instance_Matrix", M)

if __name__ == "__main__":
    # pattern_file  = "/work/hirata/wiki_2015/test/test_pattern_count.txt"
    # instance_file = "/work/hirata/wiki_2015/test/test_noun_count.txt"
    # pat_ins_file  = "/work/hirata/wiki_2015/test/test_5gram.txt"
    pattern_file  = "/work/hirata/wiki_2015/wiki_pattern_count.txt"
    instance_file = "/work/hirata/wiki_2015/wiki_noun_count.txt"
    pat_ins_file  = "/work/hirata/wiki_2015/wiki_5gram_count.txt"
    cal_pmi(pattern_file, instance_file, pat_ins_file)
