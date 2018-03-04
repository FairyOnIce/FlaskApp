import numpy as np

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
    return (out + placeholder + str(np.random.randint(0,100,1)))
