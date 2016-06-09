import numpy as np 
import pandas as pd 
import csv
from . import convert

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
            self.data = pd.DataFrame(self.data,columns=index, )
            self.data = self.data.rename(columns=lambda x: x.replace(" ", ""))
            self.dataShape = self.data.shape
            #self.data = np.array(self.data)


        nameLength = len(colnames)
        
        if nameLength != len(datatype):
            raise Exception('Number of columns is inconsistent with defined types')

        print('Dimensions:')
        print(self.dataShape)
        print('Column headings and data types')
        print(tuples)
        print('Take a moment to review the plots showing diversity of the information found within each data column.')
        print('ID and Category Columns have been reduced to their first character.')  
        print('Sensitive information has been converted to numbers.')
        
        self.conNplot()
    
    def conNplot(self):
        
        d = convert.convertNplot(self.data)
        d.plot()
        self.sliceNdice()
        
    def sliceNdice(self):
        continue 
        
        