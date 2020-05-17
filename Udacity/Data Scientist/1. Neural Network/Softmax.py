import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    L_exp = np.exp(np.array(L))
    return list(L_exp/np.sum(L_exp))
