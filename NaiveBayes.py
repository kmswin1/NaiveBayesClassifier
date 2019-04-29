#-*- coding: euc-kr -*-

import pickle
import os
import sys
import numpy as np
import collections
sys.stdout.encoding

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
        self.pos = ""
        self.accuracy = 0.0

    def split_data(self):
        print(sys.stdout.encoding)
        f = open('blog_spam.txt', 'r')
        data = f.read()
        data = data.split('\n')
        for i in range(len(data)-1):
            temp = data[i].split('\t')
            if (temp[0] == 'tr'):
                self.train_data.append(temp)
            else:
                self.test_data.append(temp)
        print ("split done!")
        self.pos = self.train_data[0][1]
        f.close()

    def make_table(self):
        print ("make table")
        for k in range(len(self.train_data)):
            if self.train_data[k][1] == self.pos:
                for i in range(3, len(self.train_data[k])):
                    self.hamWords[self.train_data[k][i]] += 1
                    self.totalHam += 1
            else:
                for i in range(3, len(self.train_data[k])):
                    self.spamWords[self.train_data[k][i]] += 1
                    self.totalSpam += 1
        print ("making table done")

    def get_prob(self):
        self.split_data()
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
            f.write("get_prob complete\n")
        f.close()

    def smoothing(self):
        print ("smoothing start!")
        for key in self.spamWords.keys():
            if key not in self.hamWords.keys():
                self.hamWords[key] += 1

        for key in self.hamWords.keys():
            if key not in self.spamWords.keys():
                self.spamWords[key] += 1
        print ("smoothing done!")

    def test(self):
        result = ""
        with open("result.txt", 'w') as f:
            with open("log.txt", 'w') as log:
                for i in range(len(self.test_data)):
                    sum = 0
                    for k in range(3,len(self.test_data[i])):
                        sum += (self.hamLogLikelihood[self.test_data[i][k]] - self.spamLogLikelihood[self.test_data[i][k]])
                    if (self.prior + sum > 0):
                        result = self.test_data[i][2]+"\t정상\t"
                        f.write(result)
                        log.write("정상\n")
                        if self.test_data[i][1] == self.pos:
                            self.accuracy += 1.0
                    else:
                        result = self.test_data[i][2]+"\t스펨\t"
                        f.write(result)
                        log.write("스팸\n")
                        if self.test_data[i][1] != self.pos:
                            self.accuracy += 1.0
                self.accuracy = float(self.accuracy) / (float(self.totalHam)+float(self.totalSpam))
                print ("accuracy : %d") % self.ccuracy
                log.write(str(self.accuracy))
            log.close()
        f.close()