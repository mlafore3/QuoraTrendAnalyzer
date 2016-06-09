from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from pandas.tools.plotting import radviz
import seaborn as sns 

class analysis:
    
    def __init__(self, data):
        self.data = data
        #print(self.data)
    
    def plotCol(self, ):
        pl = sns.countplot(x=self.data.xs('ID', axis=1, level=1).MiddleInitial)
        plt.show(pl)
        #plt.show()
        
        #ID = self.data.xs('ID', axis=1, level=1).MiddleInitial.value_counts()
        #ID = ID[:5]
        #print(ID)
        #plt.plot(ID)
        #plt.show()
        #self.data.xs('ID', axis=1, level=1).groupby('LastName').size().plot(kind='bar').show()
        #plt.show()
        #print(self.data.xs('CAT', axis=1, level=1))
        self.data.xs('CAT/SENSITIVE', axis=1, level=1)
        self.data.xs('TIME', axis=1, level=1)
        self.data.xs('CONT', axis=1, level=1)
        #self.data.xs('CONT/SENSITIVE', axis=1, level=1)