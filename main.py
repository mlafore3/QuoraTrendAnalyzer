import sys
import os
from reader import parser
from reader import converter


def main(filepath):
    
    assert os.path.exists(filepath), "I did not find the file at, "+str(filepath)
    #f = open(filepath,'rb')
    print("Hooray we found your file!")
    cleanFile = parser.parseClass(filepath)
    file = cleanFile.parseData()
    encodeFile = converter.dataConverter(file[0],file[1],file[2])
    encodeFile = encodeFile.sliceNdice()
    

if __name__ == "__main__":
    main(sys.argv[1])