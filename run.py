# -*- coding: utf-8 -*-
import NaiveBayes as nb
import numpy as np
import pickle
import os
import sys

if __name__ == "__main__":
    naive = nb.NaiveBayesClassifier()
    print ("start calculate prob!!")
    naive.get_prob()
    print ("calculate complete!")
    print ("start test!!")
    naive.test()
    print ("test end")
