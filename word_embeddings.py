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


def is_context(w1, w2, phrases):
    res = False
    for l in phrases:
        if w1 in l and w2 in l:
            res = True
            break
    return res

def word_embeddings(words, phrases, rep):
    w = np.random.rand(len(words), prof)
    v = np.random.rand(len(words), prof)
    print w
    for repet in range(rep):
        # print 'repeat: ', repet
        for c in range(len(words)):
            # print 'context = ', c, ' de ', len(words)
            #Para reducir la complejidad, calculamos la sumatoria de exp de -distancia(w, v(contexto))
            r = 0.0
            for i in w:
                r += math.exp(math.tanh(np.dot(v[c],i))* -1)
            ##
            for o in range(len(words)):
                if c != o :
                    poc = math.exp(math.tanh(np.dot(w[o],v[c])) * -1) / r
                    err = 0.0
                    if is_context(words[c], words[o], phrases):
                        err = 1 - poc
                    else:
                        err = 0 - poc
                    v[o] = v[o] - (eta * err * w[c])

            w[c] = w[c] - (eta * sum(v) / len(v))
    return w


def we_context(w, v, words,phrases,rep):
    w = deepcopy(w)
    v = deepcopy(v)
    for c in range(len(phrases)):
        h = np.zeros(prof)
        for pal in phrases[c].split():
            h += v[words.index(pal)]
        div = 0.0
        for aux in w:
            div += math.exp(-1 * math.tanh(np.dot(aux, h)))
        for o in range(len(words)):
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

result = readFile("corpus_test.txt")
words = result['catalog']
phrases = result['context']
eta = 1
prof = 2
w = np.random.rand(len(words), prof)
v = np.random.rand(len(words), prof)
print w
X,Y = zip(*w)
plt.scatter(X,Y)
for label,x,y in zip(words,X,Y):
    plt.annotate(label, xy = (x,y))
plt.show()
wr = we_context(w,v,words,phrases, 10000000)
print w
print wr['w']
