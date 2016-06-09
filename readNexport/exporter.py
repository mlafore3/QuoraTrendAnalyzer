import os
import csv

class exportFile:
    
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
    
    def writeCSV(self):
        dataCSV = self.data
    
    def writePlot(self):
        sns_plot = self.data
        print(os.path.dirname(os.path.abspath(__file__)))