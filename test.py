# -*- coding: utf-8 -*-
import pickle
import os

if __name__=='__main__':
    print ("start!!")
    print (os.getcwd())
    f = open('blog_spam.txt', 'r')
    lex = []
    while True:
        data = f.readline()
        data = data.split('\n')
        data = data[0].split('\t')
        if (data[0] == 'tr'):
            if (data[1] == '정상'):
                for i in range(3, len(data)):
                    if data[i] not in lex:
                        lex.append(data[i])
                    else:
                        for i in range(3, len(data)):
                            if data[i] not in lex:
                                lex.append(data[i])
        if not data: break
    f.close()
    with open("result.txt",'wb') as f:
        pickle.dump(lex, f)