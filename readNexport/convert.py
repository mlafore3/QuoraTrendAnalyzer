import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os 

class convertClass:
    
    def __init__(self, data):
        self.data = data
        self.data = self.data.replace('\A\s+', np.nan, regex=True).replace('', np.nan)
        
    def plot(self):
        datCopy = self.data
        
        ID = datCopy.xs('ID', axis=1, level=1)
        for i in ID.columns:
            dat = []
            for row in ID[i]:
                if row is np.nan:
                    continue
                else:
                    temp = row[0]
                    dat.append(temp)
            
            dat1 = np.array(dat)
            sns_plot = sns.countplot(x=dat1)
            sns_plot = sns_plot.get_figure()
            sns_plot.savefig("exports/"+i+".png")
            
        CAT = datCopy.xs('CAT', axis=1, level=1)
        for i in CAT.columns:
            dat = []
            for row in CAT[i]:
                if row is np.nan:
                    continue
                else:
                    temp = row[0]
                    dat.append(temp)
            
            dat1 = np.array(dat)
            sns_plot = sns.countplot(x=dat1)
            sns_plot = sns_plot.get_figure()
            sns_plot.savefig("exports/"+i+".png")
            
        CONT = datCopy.xs('CONT', axis=1, level=1)
        for i in CONT.columns:
            dat = []
            for row in CONT[i]:
                if row is np.nan:
                    continue
                else:
                    #temp = row[0]
                    dat.append(row)
            
            dat1 = np.array(dat)
            sns_plot = sns.countplot(x=dat1)
            sns_plot = sns_plot.get_figure()
            sns_plot.savefig("exports/"+i+".png")
            
        #FOR NOW THERE IS NO TIME CONVERSION 
    
    