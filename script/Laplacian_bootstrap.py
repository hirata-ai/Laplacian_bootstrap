#!/usr/bin/python
# -*-coding:utf-8-*-

import pickle
import math
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix
from scipy.io import mmwrite, mmread

# def make_adj_matrix(M):
#     return M.transpose().dot(M)

def Laplacian_bootstrap(M_matrix, instance_index_pickle, pattern_index_pickle, seed_word):
    alpha = 0.0001
    f = open(instance_index_pickle, "r")
    instance_index = pickle.load(f)
    f.close()
    print "instance file readed."
    # f = open(pattern_index_pickle, "r")
    # pattern_index = pickle.load(f)
    # f.close()
    # print "pattern file readed."
    seed_vec = np.zeros(len(instance_index)) #全て0で初期化
    seed_vec[instance_index[seed_word]] = 1  #seed_wordの位置だけ1を立てる
    M = mmread(M_matrix)
    print "instance-pattern matrix readed."
    D_diag = (M.dot(M.transpose()).sum(0).T / (len(instance_index) * len(pattern_index))) / math.sqrt(2)
    print "D_diag_length:{}".format(len(D_diag))
    D = lil_matrix((len(D_diag), len(D_diag)))
    D.setdiag(D_diag)

    M = M.tolil()
    instance_scorevec = seed_vec
    # L = lil_matrix(np.identity(len(D_diag))) - D.dot(M).dot(M.transpose()).dot(D)
    # instance_scorevec = alpha * np.dot(-L, instance_scorevec) + (1 - alpha) * seed_vec
    # print "D_shape:{}\tM_shape:{}".format(D.get_shape(), M.get_shape())
    L1 = D.dot(M)
    # print "L1:{}\n{}".format(type(L1), L1)
    L2 = L1.dot(M.transpose())
    # print "M2:{}\n{}".format(type(L2), L2)
    L3 = L2.dot(D)
    # print "M2:{}\n{}".format(type(L3), L3)
    # instance_scorevec = alpha * np.dot(-L3, instance_scorevec) + (1 - alpha) * seed_vec

    for t in range(10):
        # print "alpha:{}".format(alpha)
        # print "L3_shape:{}\nscore_vec_shape:{}".format(L3.get_shape(), instance_scorevec.shape)
        # print "-L3.dot(instance_scorevec):{}".format(-L3.dot(instance_scorevec))
        aa = alpha * -L3.dot(instance_scorevec)
        instance_scorevec = alpha * -L3.dot(instance_scorevec) + (1 - alpha) * seed_vec
        f = open("../data/Laplacian_bootstrap_result/result_iter{}.pickle".format(t+1), "w")
        pickle.dump(instance_scorevec, f)
        print "iter {}".format(t + 1)

    return instance_scorevec

if __name__ == "__main__":
    input_word = "東京"
    M = "/home/hirata/tensor_bootstrap/script/wiki_pattern_instance_Matrix.mtx"
    instance_index = "/home/hirata/tensor_bootstrap/script/instance_index.pickle"
    pattern_index  = "/home/hirata/tensor_bootstrap/script/pattern_index.pickle"
    output = Laplacian_bootstrap(M, instance_index, pattern_index, input_word)
    # print output
