# -*- encoding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

def readFile(str):
    arch = open(str,'r')
    context = list()
    catalog = list()
    for line in arch:
        if line != "":
            for w in line.split():
                if w not in catalog:
                    catalog.append(w)
            context.append(line)
    return {'context':context,'catalog':catalog}





def we_context_mod(w, v, words,phrases,rep):
    w = deepcopy(w)
    v = deepcopy(v)
    for repet in range(rep):
        for o in range(len(words)):
            print o, ' of ', len(words)
            # h = np.zeros(prof)
            # for pal in phrases[c].split():
            #     h += v[words.index(pal)]
            # div = 0.0
            # for aux in w:
            #     div += math.exp(-1 * math.tanh(np.dot(aux, h)))
            for c in range(len(phrases)):
                ##
                h = np.zeros(prof)
                for pal in phrases[c].split():
                    h += v[words.index(pal)]
                div = 0.0
                for aux in w:
                    div += math.exp(-1 * math.tanh(np.dot(aux, h)))
                ##

                poc = math.exp(-1 * math.tanh(np.dot(w[o],h))) / div
                err = 0.0
                if words[o] in phrases[c]:
                    err = 1 - poc
                else:
                    err = 0 - poc

                v[o] = v[o] - (eta * err * h)

            for word in phrases[c].split():
                w[words.index(word)] -=  (eta * sum(v) / len(phrases[c].split()))

    return {'w': w, 'v':v}


result = readFile("corpus_WE.txt")
words = result['catalog']
phrases = result['context']
eta = 1
prof = 2
w = np.random.rand(len(words), prof)
v = np.random.rand(len(words), prof)

X,Y = zip(*w)
plt.scatter(X,Y)
# for label,x,y in zip(words,X,Y):
#     plt.annotate(label, xy = (x,y))
plt.show()
wr = we_context_mod(w,v,words,phrases, 20)

X,Y = zip(*wr['w'])
plt.scatter(X,Y)
# for label,x,y in zip(words,X,Y):
#     plt.annotate(label, xy = (x,y))
plt.show()
