import numpy as np 
import pandas as pd 
import csv

#this class takes in the parsed file object and helps the user
#interrogate their dataset modify the file and better understand 
#their data. 

class analyzeClass:
    
    def __init__(self, data):
        self.data = data
        self.sensitiveData = []
        self.colHeader = []
        self.sensitiveData = [x[0] for x in data if "SEN" in x[1]]
        self.colHeader = [x[0] for x in data]

    #the bus station method acts as a router for the user to access different methods
    def busStation(self):
        print('\n', "sample, interrogate, sort, write or exit ", '\n')
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
                self.sortData()
            elif function=="write":
                self.writeCSV()
            else:
                self.busStation()
                
    #sample dataset method
    def sampleData(self):
        s = set(self.sensitiveData)
        show = [x.replace(" ","") for x in self.colHeader if x not in s]
        sam = self.data.ix[:,show]
        print('\n',"This is a random sample of the data",'\n')
        print(sam.sample(n=10))
        self.busStation()
    
    #print a count table of column frequencies (most to least common)
    def interrogateColumn(self):
        print('\n', 'Column names are: ', '\n')
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
        
        self.busStation()
    
    #sort the dataset by a coloumn value
    def sortData(self):
        print('\n', 'Column names are: ', '\n')
        s = set(self.sensitiveData) 
        show = [x.replace(" ","") for x in self.colHeader if x not in s]
        print(show)
        temp = input("Put the data column you want sorted by as your first argument ! ")
        temp = temp.split()
        
        if list(set(temp).intersection(show)):
            datCopy = self.data
            datCopy= datCopy.rename(columns=lambda x: x.replace(" ", "")) 
            cheese=datCopy[temp]
            pizza = cheese.columns.values
            pizza = pizza.tolist()
            pinap = cheese.sort_values(by=pizza, ascending=True)
            print(pinap)
            
        self.busStation()
    
    #write a new datafile, sorted and dropping coloumns
    def writeCSV(self):
        s = set(self.sensitiveData)
        show = [x.replace(" ","") for x in self.colHeader if x not in s]
        slick=input("Type the columns you would like in your output or all ? ")
        slick = slick.split()
        sly =input("Type the column you want to order by or none ? ")
        sly = sly.split()
        important_question = input("Would you like to see the top of your dataframe before printing ? ")
        important_question = important_question.split()
        
#Funnelling responses to print output file the user desires 
####There has to be a better way to do this
        
        if "all" in slick:
            datCopy = self.data
            datCopy= datCopy.rename(columns=lambda x: x.replace(" ", "")) 
            
            if list(set(sly).intersection(show)):
                cheese=datCopy[sly]
                pizza = cheese.columns.values
                pizza = pizza.tolist()
                pinap = datCopy.sort_values(by=pizza, ascending=True)
                
                if "yes" in important_question:
                    print(pinap.head(n=10))
                    question = input("Do you still want to print file ? ")
                    
                    if "yes" in question:
                        pinap.to_csv("exports/output.csv")
                        self.busStation()
                    else:
                        self.busStation()
                else:
                    pinap.to_csv("exports/output.csv")
                    self.busStation()
            else:
                
                if "yes" in important_question:
                    print(datCopy.head(n=10))
                    question = input("Do you still want to print file ? ")
                    
                    if "yes" in question:
                        datCopy.to_csv("exports/output.csv")
                        self.busStation()
                    else:
                        self.busStation()
                else:
                    datCopy.to_csv("exports/output.csv")
                    self.busStation()
                
    
        elif list(set(slick).intersection(show)):
            datCopy = self.data
            datCopy= datCopy.rename(columns=lambda x: x.replace(" ", ""))        
            cheese = datCopy[slick]
            
            if list(set(sly).intersection(show)):
                cheesey=cheese[sly]
                pizza = cheesey.columns.values
                pizza = pizza.tolist()
                pinap = cheese.sort_values(by=pizza, ascending=True)
                
                if "yes" in important_question:
                    print(pinap.head(n=10))
                    question = input("Do you still want to print file ? ")
                    
                    if "yes" in question:
                        pinap.to_csv("exports/output.csv")
                        self.busStation()
                    else:
                        self.busStation()
                else:
                    pinap.to_csv("exports/output.csv")
                    self.busStation()
            else:
                cheese.to_csv("exports/output.csv")
                self.busStation()
        else:
            self.busStation()
