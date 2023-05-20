import numpy as np
import matplotlib.pylab as plt

class FunctionLists:
    def step_function(self, x, x0):
        y= x > x0
        return y.astype(np.int)
    
    def responce_fit(self, x,x0,a,b):
        return a*(FunctionLists.step_function(self, x, x0)*(1-np.exp(-b*(x-x0)))+1)
    