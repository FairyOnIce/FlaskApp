import tensorflow
import keras

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
    return (text + placeholder + out)
