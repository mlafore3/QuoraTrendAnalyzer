import numpy as np 
#import pandas as pd 
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
        #print(str(filepath))
            csvData = csv.reader(csvfile, delimiter=',')
           
            colnames = next(csvData)
            datatype = next(csvData)
    
            self.indexer = list(csvData)
            #rownum = len(self.indexer)
            #self.indexLength = len(self.indexer)
            
            for row in csvData:
                self.data.append(row)
                
        self.data = np.array(self.data)
        self.dataShape = self.data.shape

            #pca = PCA(n_components=14)
            #pca.fit(df)
            
        nameLength = len(colnames)
        
        if nameLength != len(datatype):
            raise Exception('Number of columns is inconsistent with defined types')


        return(colnames, datatype, self.indexer)
    
    #def dataConverter(self, colnames, )