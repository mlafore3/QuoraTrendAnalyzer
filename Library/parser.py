import numpy as np 
import pandas as pd 
import csv

#the parseClass returns a parsed file object
class parseClass:
    
    def __init__(self, filepath):
        self.tuples = []
        self.data = []
        self.dataShape = 0
        self.filepath = filepath

#parses the file and returns a its data in a multi-level indexed pandas dataframe
    def parseMethod(self):
        
        with open(self.filepath, 'r' ) as csvfile:
            csvData = csv.reader(csvfile, delimiter=',')
            
            colnames = next(csvData)
            datatype = next(csvData)
            ar = [colnames,datatype]
            self.tuples = list(zip(*ar))
            index = pd.MultiIndex.from_tuples(self.tuples)
            
            for row in csvData:
                self.data.append(row)
            self.data = pd.DataFrame(self.data,columns=index)
            self.data = self.data.rename(columns=lambda x: x.replace(" ", ""))
            self.dataShape = self.data.shape

        nameLength = len(colnames)
        
        if nameLength != len(datatype):
            raise Exception('Number of columns is inconsistent with defined types')

        print('Dimensions:')
        print(self.dataShape)
        print('Column headings and data types')
        print(self.data.count())
        
        return self.data

