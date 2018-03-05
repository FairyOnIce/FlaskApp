## from  numpy.random import randint

## somehow, adding pickle in requirement.txt returns error
## but without it in requirement.txt pickle seems to work in Heroku
import pandas as pd
import numpy as np
from tensorflow.contrib.keras import layers
from tensorflow.contrib.keras import models


placeholder = "__"
max_length = 32


def define_model(input_length, dim_out=3):
    dim_dense_embedding = 32
    hidden_unit_LSTM = 32
    vocab_size = 1001
    main_input = layers.Input(shape=(input_length,), dtype='int32', name='main_input')
    embedding = layers.Embedding(vocab_size, dim_dense_embedding,
                                 input_length=input_length)(main_input)
    x = layers.LSTM(hidden_unit_LSTM)(embedding)
    main_output = layers.Dense(dim_out, activation='softmax')(x)
    model = models.Model(inputs=[main_input],
                         outputs=[main_output])
    # compile network
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    print(model.summary())
    return (model)




class preprocess(object):
    def __init__(self,name):
        self.load_model(name)
        self.word_index, _ = self.get_word_index_from_csv()

    def load_model(self,name):
        model = define_model(32)
        model.load_weights(name + '_weights.h5')
        self.model = model

    def get_word_index_from_csv(self):
        tokenizer = pd.read_csv("tokenizer.csv")["tokenizer"].values
        word_index = {}
        index_word = {}
        for index, word in enumerate(tokenizer, 1):
            word_index[word] = index
            index_word[index] = word
        return (word_index, index_word)

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

    def texts_to_sequences(self,line):
        out = []
        for l in line.split():
            llower = l.lower()
            if llower in self.word_index.keys():
                out.append(self.word_index[llower])
        return (out)

    ## load model and tokenizer
    def predict(self,line):
        encoded = self.texts_to_sequences(line)
        sequences = self.pad_pre_sequences([encoded], maxlen=max_length)
        probs = self.model.predict(sequences)[0]

        return (line + placeholder + "{:3.2f}".format(probs[2]))




#def predict(text):
#    ltext = text.split()
#    out = ""
#    for w in ltext:
#        out += w.lower() + " "
#    return (out + placeholder + str(randint(0,100,1)[0]))
