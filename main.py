import sys
import os
from reader import parser


def main(filepath):
    
    assert os.path.exists(filepath), "I did not find the file at, "+str(filepath)
    #f = open(filepath,'rb')
    print("Hooray we found your file!")
    cleanFile = parser.parseClass(filepath)
    cleanFile = cleanFile.parseData()
    cleanFile = cleanFile.categoricalEncoder()
    cleanFile = cleanFile.analyzeFile()
    print(cleanFile)
    #f.close()

if __name__ == "__main__":
    main(sys.argv[1])