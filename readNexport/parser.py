import numpy as np 
import pandas as pd 
import csv
from . import convert
from sys import argv

class parseClass:
    
    def __init__(self, filepath):
        self.tuples = []
        self.data = []
        self.dataShape = 0
        self.filepath = filepath
        self.sensitiveData = []
        self.colHeader = []

    
    def __str__(self):
        return("Data dimensions", self.dataShape,"Header", self.headers)
        
                        
        
    def parseData(self):
        
        with open(self.filepath, 'r' ) as csvfile:
            csvData = csv.reader(csvfile, delimiter=',')
            
            colnames = next(csvData)
            datatype = next(csvData)
            ar = [colnames,datatype]
            self.tuples = list(zip(*ar))
            index = pd.MultiIndex.from_tuples(self.tuples)
            self.sensitiveData = [x[0] for x in self.tuples if "SEN" in x[1]]
            self.colHeader = [x[0] for x in self.tuples]
            
            for row in csvData:
                self.data.append(row)
            self.data = pd.DataFrame(self.data,columns=index)
            self.data = self.data.rename(columns=lambda x: x.replace(" ", ""))
            self.dataShape = self.data.shape
            #self.data = np.array(self.data)


        nameLength = len(colnames)
        
        if nameLength != len(datatype):
            raise Exception('Number of columns is inconsistent with defined types')

        print('Dimensions:')
        print(self.dataShape)
        print('Column headings and data types')
        print(self.tuples)
        print()
        print()
        print('Take a moment to review the plots showing diversity of the information found within each data column.')
        print('ID and Category Columns have been reduced to their first character.')  
        print('Sensitive information has been converted to numbers.') 
        print()
        print()

        self.conNplot()
    
    def conNplot(self):
        
        d = convert.convertNplot(self.data)
        d.plot()
        self.busStation()
        
    def busStation(self):
        
        print()
        print()
        print("sample, interrogate_column, write or exit ?" )
        print()
        function = input("What do you want to do? ")
        while function is not None:
            if function=="write":
                self.writeData()
            elif function=="intterogate_column":
                self.interrogate_column()
            elif function=="sample":
                self.sampleData()
            elif function=="exit":
                break
            else:
                self.busStation()
            return False
        
    def sampleData(self):
        print()
        print()
        s = set(self.sensitiveData)
        show = [x.replace(" ","") for x in self.colHeader if x not in s]
        sam = self.data.ix[:,show]
        print("This is a sample of the data")
        print(sam.sample(n=10))
        self.busStation()


            
        