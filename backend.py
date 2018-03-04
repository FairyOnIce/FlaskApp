from  numpy.random import randint
from tensorflow.contrib import keras
import pickle

placeholder = "__"

def predict(text):
    '''

    :param text: text mix of lower and upper
    :return:

    '''
    ltext = text.split()
    out = ""
    for w in ltext:
        out += w.lower() + " "
    return (out + placeholder + str(randint(0,100,1)[0]))
