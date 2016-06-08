import sys
import gc
import os
from reader import parser
from reader import converter


def main(filepath):
    
    assert os.path.exists(filepath), "I did not find the file at, "+str(filepath)
    #f = open(filepath,'rb')
    print("Hooray we found your file!")
    cleanFile = parser.parseClass(filepath)
    input = cleanFile.parseData()
    #print("0",input[0])
    #print("1",input[1])
    #print("2",input[2])
    print(converter.dataConverter(input[0],input[1],input[2]))
    #cleanFile.analyzeFile()
    #print(cleanFile)
    #f.close()

if __name__ == "__main__":
    main(sys.argv[1])