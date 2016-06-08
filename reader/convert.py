import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class convertClass:
    
    def __init__(self, data):
        self.data = data
        self.data = self.data.replace('\A\s+', np.nan, regex=True).replace('', np.nan)
        
    def con(self):
        datCopy = self.data
        
        ID = datCopy.xs('ID', axis=1, level=1)
        
        for i in ID.columns:
            dat = []
            for row in ID[i]:
                if row is np.nan:
                    continue
                else:
                    temp = row[0]
                    temp = ord(temp)
                    dat.append(temp)
            
            dat1 = np.array(dat)
            #print("THIS IS DAT", dat)
            #print("THIS IS DAT2", dat1)
            sns_plot = sns.countplot(x=dat1)
            sns_plot = sns_plot.get_figure()
            #plt.show(pl)    
            sns_plot.savefig(i+".png")
                    #datCopy.replace(row,temp)
                    #datCopy.replace(row,temp)
        #print(datCopy)
                    #pl = sns.countplot(x=self.data.xs('ID', axis=1, level=1).LastName)
                    #plt.show(pl)
                    
                    #print((ord(row[0])))
                #if row is not 
                #if row is not NaN:
                #self.data.replace(ord(row[0]))