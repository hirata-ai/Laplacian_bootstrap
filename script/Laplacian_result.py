#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import pickle
import argparse
import numpy as np

def laplacian_result(instance_index_pickle, result_file_pickle):
    index_instance_dic = {}

    f = open(instance_index_pickle, "r")
    instance_index = pickle.load(f)
    f.close()
    f = open(result_file_pickle, "r")
    result_array = pickle.load(f)
    f.close()
    
    sorted_result = np.argsort(result_array)[-1::-1]
    for i in instance_index:
        index_instance_dic[instance_index[i]] = i

    for i in range(101):
        print "{}:word:{}, score:{}".format(i, index_instance_dic[sorted_result[i]], result_array[sorted_result[i]])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="test")
    parser.add_argument("-r", "--result_file", type=str)
    parser.add_argument("-i", "--instance_index", type=str)
    args = parser.parse_args()
    
    #python Laplacian_result.py -i instance_index.pickle -r ../data/Laplacian_bootstrap_result/result_iter1.pickle
    laplacian_result(args.instance_index, args.result_file)
