import numpy as np
import pandas as pd

class convertClass:
    
    def __init__(self, data):
        self.data = data
        self.data = self.data.replace('\s+', np.nan, regex=True).replace('', np.nan)
        #print(self.data)
        
    def con(self):
        datCopy = self.data
        
        ID = datCopy.xs('ID', axis=1, level=1)
        
        for i in ID.columns:
            for row in ID[i]:
                if row is not np.nan:
                    temp = row[0]
                    temp = ord(temp)
                    datCopy.replace(temp)
                    print(datCopy)
                    
                    #print((ord(row[0])))
                #if row is not 
                #if row is not NaN:
                #self.data.replace(ord(row[0]))