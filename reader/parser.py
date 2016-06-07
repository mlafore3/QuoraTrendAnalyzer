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
        
        self.convertID = []
        self.convertTime = []
        self.convertCat = []
        self.convertCont = []
        self.convertSensitive = []
        
        
        
    def parseData(self):
        
        with open(self.filepath, 'r' ) as csvfile:
        #print(str(filepath))
            csvData = csv.reader(csvfile, delimiter=',')
           
            names = next(csvData)
            types = next(csvData)
    
            self.indexer = list(csvData)
            #self.indexLength = len(self.indexer)
            
            for row in csvData:
                self.data.append(row)
                
            self.data = np.array(self.data)
            self.dataShape = self.data.shape

            #pca = PCA(n_components=14)
            #pca.fit(df)
            
        nameLength = len(names)
        
        if nameLength != len(types):
            raise Exception('Number of columns is inconsistent with defined types')

        # create header objects
        #for i in range(nameLength):
         #   self.headers.append(headNode(names[i],types[i]))

        #Parse column types 
        for i in range(nameLength):
            if types[i].find("ID") == 0:
                self.convertID.append(i)
            elif types[i].find("CONT") == 0:
                self.convertCont.append(i)
            elif types[i].find("TIME") == 0:
               self.convertTime.append(i)
            else:
                self.convertCat.append(i)
        print("DataFile Column Order: ", types)
        print("ID", self.convertID)
        print("CONT", self.convertCont)
        print("TIME", self.convertTime)
        print("Cat", self.convertCat)
        
        #Grab sensitives
        for i in range(nameLength):
            if types[i].find("CAT/SENSITIVE")==0:
                self.convertSensitive.append(i)
            if types[i].find("CONT/SENSITIVE")==0:
                self.convertSensitive.append(i)
        print("Sensitive", self.convertSensitive)
        
        #print(((self.convertSensitive>self.convertID)-(self.convertSensitive<self.convertID)))        

    #convert to sensitive should be first 
    def categoricalEncoder(self):
    
        for col in self.convertID:
            for row in range(len(self.indexer)):
                outputID = "".join(item[0] for item in self.indexer[row][col].split())
                if outputID is not "":
                    outputID = ord(outputID[0])
                    #print(outputID)
                else:
                    outputID == np.nan
                    

        for col in self.convertCont:
            for row in range(len(self.indexer)):
                outputCont = "".join(item for item in self.indexer[row][col].split())
                if outputCont is not "":
                    outputCont = ord(outputCont[0])
                else:
                    outputCont == np.nan
                    #print(output)

        for col in self.convertCat:
            for row in range(len(self.indexer)):
                outputCat = "".join(item for item in self.indexer[row][col].split())
                #print(outputCat)
                if outputCat is not "":
                    outputCat = ord(outputCat[0])
                else: 
                 outputCat == np.nan
                    #print(output)
    def analyzeFile(self):
        print(self)
        #for col in self.convertTime:
            #for row in range(len(self.indexer)):
                #print(self.indexer[row][col])
                #output = "".join(item[0] for item in self.indexer[row][col].split())
               # if output is not "":
                   # output = ord(output[0])
                    #print(output)
                    
        #for i in self.indexLength:
            #print(self.data[i])
        #for i in self.convertCont:
            #print(self.data[[i]])
            #for cell in self.data[i::]:
                #print(cell)
        
        
        
        #print("Sens", self.convertSensitive)
                #print(types[i])
               #idsJumble = enumerate(self.data[:, i])
               #print(idsJumble)
               #CategoricalEncoder.transform(self,idsJumble)
               #for value in idsJumble:
                    #if value is not None:
                        #new = ord(value[1])
                        #print(new)
               #         value = ord(value[1]))
                        #encode = preprocessing.LabelEncoder()
                        #print(Multicolumn(value))  
                    #ids = ids.astype(int(ord()))
                #print(ids.astype((int)
            #print(typeConverter.convertToInt(types[i]))
        #for rows in self.data:
         #   for item in rows:
                #print()
                #print(item)
                #if item.dtype == :
                    #print(item)
        #self.setupHeaders()
 #   def setupHeaders(self):
        
  #      for i, j in enumerate(self.headers):
   #         print(j)
                

        