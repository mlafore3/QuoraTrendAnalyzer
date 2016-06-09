import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os 
from . import exporter

class convertNplot:
    
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
            #temp1 = exportFile()
            
            sns_plot = sns.countplot(x=dat1)
            sns_plot = sns_plot.get_figure()
            #path = os.path.join('/exports')
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
            
        TIME = datCopy.xs('TIME', axis=1, level=1)
        for i in TIME.columns:
            dat = []
            for row in TIME[i]:
                if row is np.nan:
                    continue
                else:
                    temp = row
                    dat.append(temp)
            
            dat1 = np.array(dat)
            sns_plot = sns.countplot(x=dat1)
            sns_plot = sns_plot.get_figure()
            sns_plot.savefig("exports/"+i+".png")