# -*- coding: utf-8 -*-
import pickle
import os
import sys
import numpy as np
import collections

class NaiveBayesClassifier():

    def __init__(self):
        self.hamLogLikelihood = collections.defaultdict(lambda :0)
        self.spamLogLikelihood = collections.defaultdict(lambda: 0)
        self.hamWords = collections.defaultdict(lambda: 0)
        self.spamWords = collections.defaultdict(lambda: 0)
        self.spamPrior = 0.0
        self.hamPrior = 0.0
        self.totalHam = 0.0
        self.totalSpam = 0.0
        self.prior = 0.0
        self.train_data = []
        self.test_data = []

    def split_data(self):
        f = open('blog_spam.txt', 'r')
        while True:
            data = f.readline()
            data = data.split('\n')
            data = data[0].split('\t')
            if (data[0] == 'tr'):
                self.train_data.append(data)
            else:
                self.test_data.append(data)
            if not data: break
        f.close()

    def make_table(self):
        for k in range(len(self.train_data)):
            if (self.train_data[i][1] == '정상'):
                for i in range(3, len(self.train_data[i])):
                    self.hamWords[self.train_data[i]] += 1
                    self.totalHam += 1
            else:
                for i in range(3, len(self.train_data[i])):
                    self.spamWords[self.train_data[i]] += 1
                    self.totalSpam += 1

    def get_prob(self):
        self.make_table()
        with open("log.txt", 'w') as f:
            f.write("make_table complete\n")
        f.close()
        self.smoothing()
        with open("log.txt", 'w') as f:
            f.write("smoothing complete\n")
        f.close()
        self.hamPrior = np.log(float(self.totalHam)/(float(self.totalHam)+float(self.totalSpam)))
        self.spamPrior = np.log(float(self.totalSpam)/(float(self.totalHam)+float(self.totalHam)))
        self.prior = self.hamPrior - self.spamPrior
        for key in self.hamWords.keys():
            self.hamLogLikelihood[key] = np.log(float(self.hamWords[key])/(float(self.hamWords[key])+float(self.spamWords[key])))
            self.spamLogLikelihood[key] = np.log(float(self.spamWords[key]) / (float(self.hamWords[key]) + float(self.spamWords[key])))
        with open("log.txt", 'w') as f:
            f.write("get_pro bcomplete\n")
        f.close()

    def smoothing(self):
        for key in self.spamWords.keys():
            if key not in self.hamWords.keys():
                self.spamWords[key] += 1

        for key in self.hamWords.keys():
            if key not in self.spamWords.keys():
                self.hamWords[key] += 1

    def test(self):
        result = ""
        with open("result.txt", 'w') as f:
            with open("log.txt", 'w') as log:
                for i in range(len(self.test_data)):
                    sum = 0
                    for k in range(3,len(self.test_data[i])):
                        sum += (self.hamLogLikelihood[self.test_data[i]] - self.spamLogLikelihood[self.test_data[i]])
                    if (self.prior + sum > 0):
                        result = self.test_data[2]+"\t정상\t"
                        f.write(sum)
                        log.write("정상\n")
                    else:
                        result = self.test_data[2]+"\t스펨\t"
                        log.write("스팸\n")
            log.close()
        f.close()