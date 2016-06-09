
#Code of convert
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os 
from . import exporter

class convertNplot:
    
    def __init__(self, data):
        self.data = data
        self.data = self.data.replace('\A\s+', np.nan, regex=True).replace('', np.nan)
        
    def plot(self):
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
            #temp1 = exportFile()
            
            sns_plot = sns.countplot(x=dat1)
            sns_plot = sns_plot.get_figure()
            #path = os.path.join('/exports')
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
            
        TIME = datCopy.xs('TIME', axis=1, level=1)
        for i in TIME.columns:
            dat = []
            for row in TIME[i]:
                if row is np.nan:
                    continue
                else:
                    temp = row
                    dat.append(temp)
            
            dat1 = np.array(dat)
            sns_plot = sns.countplot(x=dat1)
            sns_plot = sns_plot.get_figure()
            sns_plot.savefig("exports/"+i+".png")



















#CodeDump
import numpy as np
import csv

class dataConverter:
    
            
        #dict = {}
        #gen = (dict[i[0]] for i in datCopy.columns)
                    #for i in gen:
            #for i in range(0,3):
               # print(i)
    
    def __init__(self, data):
        self.colnames = colnames
        self.datatype = datatype
        self.indexer = indexer
        self.data = data
        self.convertID = []
        self.convertTime = []
        self.convertCat = []
        self.convertCont = []
        self.convertSensitive = []
        
        #Parse column types 
    def sliceNdice(self):
        
        for i in range(len(self.colnames)):
            if self.datatype[i].find("ID") == 0:
                self.convertID.append(i)
            elif self.datatype[i].find("CONT") == 0:
                self.convertCont.append(i)
            elif self.datatype[i].find("TIME") == 0:
               self.convertTime.append(i)
            else:
                self.convertCat.append(i)
                
        print("DataFile Column Order: ", self.datatype)
        print("ID", self.convertID)
        print("CONT", self.convertCont)
        print("TIME", self.convertTime)
        print("Cat", self.convertCat)
        
        #Grab sensitives
        for i in range(len(self.colnames)):
            if self.datatype[i].find("CAT/SENSITIVE")==0:
                self.convertSensitive.append(i)
            if self.datatype[i].find("CONT/SENSITIVE")==0:
                self.convertSensitive.append(i)
                
        print("Sensitive", self.convertSensitive)
        
    #Should convert sensitive first
        with open("output.csv", 'w') as f:
            writer = csv.writer(f)
         
            #print(self.data[row::]for row in self.data)
            #for row in self.data:
                #print(row[0])
            for col in self.convertID:
                for row in range(len(self.indexer)):
                    outputID = "".join(item[0] for item in self.indexer[row][col].split())
                    if outputID is not "":
                        outputID = ord(outputID[0])
                    else:
                        outputID == np.nan
                    #writer.writerows(row)

                    
            for col in self.convertCont:
                for row in range(len(self.indexer)):
                    outputCont = "".join(item[0] for item in self.indexer[row][col].split())
                    if outputCont is not "":
                        outputCont = float(outputCont[0])
                    else:
                        outputCont == np.nan
                    #writer.writerows(row)
    
            for col in self.convertCat:
                for row in range(len(self.indexer)):
                    outputCat = "".join(item[0] for item in self.indexer[row][col].split())
                    if outputCat is not "":
                        outputCat = ord(outputCat[0])
                    else: 
                        outputCat == np.nan
                    #writer.writerows(row)
        
            for col in self.convertTime:
                for row in range(len(self.indexer)):
                    outputTime = "".join(item[0] for item in self.indexer[row][col].split())
                    #writer.writerows(row)
            
       # for i, item in enumerate(self.colnames):
        #    print(outputCat)