import pickle
import os
import sys
import numpy as np

class NaiveBayesClassifier():

    def __init__(self):
        self.label = []
        self.docid = []
        self.lex = []
        self.likelihood = []
        self.prior = []

    def make_lex(self):
        def make_lex():
            f = open('blog_spam.txt', 'r')
            while True:
                data = f.readline()
                data = data.split('\n')
                data = data[0].split('\t')
                if (data[0] == 'tr'):
                    if (data[1] == '정상'):
                        for i in range(3, len(data)):
                            if data[i] not in self.lex:
                                self.lex.append(data[i])
                                self.label.append("정상")
                                self.docid.append(data[2])
                    else:
                        for i in range(3, len(data)):
                            if data[i] not in self.lex:
                                self.lex.append(data[i])
                                self.label.append("비정상")
                                self.docid.append(data[2])
                if not data: break
            f.close()
            return self.label, self.docid, self.lex