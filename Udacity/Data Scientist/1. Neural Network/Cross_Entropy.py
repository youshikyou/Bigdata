import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
        #sum{y_i * ln(p_i) + (1-y_i)*ln(1-pi)} # 1~n
    return -np.sum(list(map(lambda y,p: y* np.log(p)+(1-y)*np.log(1-p),Y,P)))
    
    #Y = np.float_(Y)
    #P = np.float_(P)
    #-np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
