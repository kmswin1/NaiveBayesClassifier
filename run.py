# -*- coding: utf-8 -*-
import NaiveBayes as nb
import numpy as np
import pickle
import os
import sys

if __name__ == "__main__":
    naive = nb.NaiveBayesClassifier()
    naive.get_prob()
    print ("get_prob")
    naive.test()
    print ("test")
