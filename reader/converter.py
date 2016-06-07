from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import numpy as np

class dataConverter:

    def __init__(self, colnames, datatype, data):
        self.colnames = colnames
        self.datatype = datatype
        self.data = np.copy(data)
        #print(self.data)
        #self.data = data
        
        #Parse column types 
        for i in range(parseData=nameLength):
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