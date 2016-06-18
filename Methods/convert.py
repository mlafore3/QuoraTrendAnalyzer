import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os 

#a class that converts sensitive information for protection and plots 
#coloumn distributions 

class convertNplotClass:
    
    #instantiates the data and replaces empty columns with NA 
    def __init__(self, data):
        self.data = data
        self.data = self.data.replace('\A\s+', np.nan, regex=True).replace('', np.nan)
    
    #uses the seaborn package to plot column distributions for each datatype 
    def plot(self):
        print('\n','Take a moment to review the plots in the export folder. These show the diversity of information found within each data column.')
        print('ID and Category Columns have been reduced to their first character.')  
        print('Sensitive information has been converted to numbers.') 
        print('At this time, this program does not support plots of Time categories', '\n')
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
    
    