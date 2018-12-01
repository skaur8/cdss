import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import operator
import glob
import cdsmain as cm

train_label = open('optical_detector_train.csv')
pi = {}
for i in range(1,21):
    pi[i] = 0
lines = train_label.readlines()
total = len(lines)
for line in lines:
    val = int(line.split()[0])
    pi[val] += 1

for key in pi:
    pi[key] /= total
probability=join(format(k,v) for k,v in pi.items())

class BernoulliNBTextClassifier(object):

    def __init__(self):
        self._log_priors = None
        self._cond_probs = None
        self.values = None
        self.features = None

    def train(self, documents, labels):
        
        label_counts = Counter(labels)
        N = float(sum(label_counts.values()))
        self._log_priors = {k: log(v/N) for k, v in label_counts.iteritems()}

       
        X = [set(get_values(d)) for d in documents]

        self.values = set([f for values in X for f in values])

        self._cond_probs = {l: {f: 0. for f in self.values} for l in self._log_probs}

        for x, l in zip(X, labels):
            for f in x:
                self._cond_probs[l][f] += 1.

        for l in self._cond_probs:
            N = label_counts[l]
            self._cond_probs[l] = {f: (v + 1.) / (N + 2.) for f, v in self._cond_probs[l].iteritems()}
        train_label = open('optical_detector_train.csv')
        pi = {}
        for i in range(1,21):
            pi[i] = 0
        lines = train_label.readlines()
        total = len(lines)
        for line in lines:
            val = int(line.split()[0])
            pi[val] += 1

        for key in pi:
            pi[key] /= total
        probability=join(format(k,v) for k,v in pi.items())


    def prediction(self, text):
        x = get_features(text)

        predict = None
        max_ = float("-inf")

        for l in self._log_priors:
            log_sum = self._log_priors[l]
            for f in self.features:
                probability = self._cond_probs[l][f]
                log_sum += log(prob if f in x else 1. - prob)
            if log_sum > max_:
                max_ = log_sum
                predict = l

        return max

file_names = glob.glob('optical_detector_train.csv'.format(type_))
    for n in file_names:
        f = open(n)
        examples.append(f.read())
        predict.append('yes')
        f.close()
   
file_names = glob.glob('optical_detector_test.csv'.format(type_))
    for n in file_names:
        f = open(n)
        examples.append(f.read())
        predict.append('no')
        f.close()

return predict

file_names = glob.glob('optical_detector_train.csv'.format(type_))
    for n in file_names:
        f = open(n)
        examples.append(f.read())
        treatment.append('yes')
        f.close()
    
file_names = glob.glob('optical_detector_test.csv'.format(type_))
    for n in file_names:
        f = open(n)
        examples.append(f.read())
        treatment.append('no')
        f.close()
return treatment

train_sym, train_medhis = get_labeled_data('train')
test_sym, test_medhis = get_labeled_data('test')

nb = BernoulliNBTextClassifier(cm.val)
nb.train(train_sym, train_medhis)


