## from  numpy.random import randint

## somehow, adding pickle in requirement.txt returns error
## but without it in requirement.txt pickle seems to work in Heroku
import pickle
import numpy as np
from tensorflow.contrib.keras import models


placeholder = "__"
max_length = 37

class preprocess(object):
    def __init__(self,name):
        self.load_model(name)
        print("load_model")
        self.load_tokenizer(name)
        print("load tokenizer")

    def load_model(self,name):
        model = models.model_from_json(open(name + '_architecture.json').read())
        model.load_weights(name + '_weights.h5')
        self.model = model

    def load_tokenizer(self,name):
        # loading
        with open(name + '_tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)
        self.tokenizer = tokenizer

    def pad_pre_sequences(self,arr, maxlen):
        lines = []

        for iline in range(len(arr)):
            oline = arr[iline]
            lo = len(oline)
            if maxlen > lo:
                line = [0] * (maxlen - lo) + list(oline)
            else:
                line = oline[:maxlen]
            lines.append(line)
        lines = np.array(lines)
        return (lines)

    def predict(self,line):
        '''
        :param text: text mix of lower and upper
        :return:

        '''
        encoded = self.tokenizer.texts_to_sequences([line])[0]
        sequences = self.pad_pre_sequences([encoded], maxlen=max_length)
        probs = self.model.predict(sequences)[0]
        return (line + placeholder + "{:3.2f}".format(probs[2]))




#def predict(text):
#    ltext = text.split()
#    out = ""
#    for w in ltext:
#        out += w.lower() + " "
#    return (out + placeholder + str(randint(0,100,1)[0]))
