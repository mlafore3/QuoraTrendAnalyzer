import numpy as np 
import pandas as pd 
import csv
from .converter import dataConverter
from sklearn import preprocessing

class parseClass:
    
    def __init__(self, filepath):
        self.headers = []
        self.data = []
        self.dataShape = 0
        self.filepath = filepath
        self.indexer = []
        #self.indexLength = 0
                        
        
    def parseData(self):
        
        with open(self.filepath, 'r' ) as csvfile:
            csvData = csv.reader(csvfile, delimiter=',')
            
            colnames = next(csvData)
            datatype = next(csvData)
            ar = [colnames,datatype]
            tuples = list(zip(*ar))
            index = pd.MultiIndex.from_tuples(tuples)
            
            for row in csvData:
                self.data.append(row)
            self.data = pd.DataFrame(self.data,columns=index)
            self.data = self.data.rename(columns=lambda x: x.replace(" ", ""))
            #print(self.data)
            
        
            #print(self.data)
            
        #self.data = np.array(self.data)
        #self.dataShape = self.data.shape

        nameLength = len(colnames)
        
        if nameLength != len(datatype):
            raise Exception('Number of columns is inconsistent with defined types')


        return(self.data)        