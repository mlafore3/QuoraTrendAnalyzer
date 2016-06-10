import numpy as np 
import pandas as pd 
import csv
from . import convert
from sys import argv
import re

class parseClass:
    
    def __init__(self, filepath):
        self.tuples = []
        self.data = []
        self.dataShape = 0
        self.filepath = filepath
        self.sensitiveData = []
        self.colHeader = []
        self.datanp = []
    
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
            #self.datanp = np.array(self.data)


        nameLength = len(colnames)
        
        if nameLength != len(datatype):
            raise Exception('Number of columns is inconsistent with defined types')

        print('Dimensions:')
        print(self.dataShape)
        print('Column headings and data types')
        print(self.data.count())
        print()
        print()
        print('Take a moment to review the plots in the export folder. These show the diversity of information found within each data column.')
        print('ID and Category Columns have been reduced to their first character.')  
        print('Sensitive information has been converted to numbers.') 
        print()
        print()

        #self.conNplot()
    
    def conNplot(self):
        
        d = convert.convertClass(self.data)
        d.plot()
        self.busStation()
        
    def busStation(self):
        
        print()
        print()
        print("sample, interrogate or exit " )
        print()
        function = []
        function = input("What do you want to do? ")
        while function is not None:
            if function=="exit":
                print("You have chose to quite this program, GOODBYE !")
                raise SystemExit 
            elif function=="interrogate":
                self.interrogateColumn()
            elif function=="sample":
                self.sampleData()
            elif function=="sort":
                self.sort()
            elif function=="write":
                self.writeCSV()
            else:
                self.busStation()
        
    def sampleData(self):
        print()
        print()
        s = set(self.sensitiveData)
        show = [x.replace(" ","") for x in self.colHeader if x not in s]
        sam = self.data.ix[:,show]
        print("This is a random sample of the data")
        print(sam.sample(n=10))
        self.busStation()
        
    def interrogateColumn(self):
        print()
        print()
        print('Column names are: ')
        s = set(self.sensitiveData) 
        show = [x.replace(" ","") for x in self.colHeader if x not in s]
        print(show)
        temp = []
        temp = input("Which column(s) do you want to interrogate ? ")
        if temp=="exit":
            self.busStation()
        temp = temp.split()
    
        if list(set(temp).intersection(show)):
            datCopy = self.data
            datCopy= datCopy.rename(columns=lambda x: x.replace(" ", ""))        
            pizza = datCopy.ix[:,temp]
            cheese = pizza.apply(lambda x: x.value_counts()).T.stack()
            print(cheese)
        else:
            self.interrogateColumn()
        self.interrogateColumn()
        
        #s = set(self.colHeader)
       # while function is not None:
            #if function=="write":
                #self.writeCSV()

        
    def sort(self):
        print()
        print()
        print('Column names are: ')
        s = set(self.sensitiveData) 
        show = [x.replace(" ","") for x in self.colHeader if x not in s]
        print(show)
        temp = input("Which column(s) do you want to interrogate ? ")
        temp = temp.split()
        
        datCopy = self.data
        datCopy= datCopy.rename(columns=lambda x: x.replace(" ", ""))        
        pizza = datCopy.ix[:,temp]
        cheese = pizza.apply(lambda x: x.value_counts()).T.stack()
        print(cheese)
        
        self.busStation()
        
    def writeCSV(self):
        d = convert.convertClass(self.data)
        self.busStation()
    


            
        