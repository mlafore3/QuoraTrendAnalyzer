import sys
import os
from readNexport import parser, convert, exporter
#from analysis import analyze
#from exporter import fileExport


def main(filepath):
    
    assert os.path.exists(filepath), "I did not find the file at, "+str(filepath) + "Ex. ~/path_to_file.csv"
    print("Your file was found!")
    cleanFile = parser.parseClass(filepath)
    file = cleanFile.parseData()
    temp = cleanFile.sortData()
    print(temp)
    #plot = analyze.visualAnalysis(cleanFile.parseData())
    #plot.plotCol()
    #co = convert.convertClass(cleanFile.parseData())
    #co.con()
    #encodeFile = converter.dataConverter(file[0],file[1],file[2], file[3])
    #encodeFile = encodeFile.sliceNdice()
    #print(encodeFile)

if __name__ == "__main__":
    main(sys.argv[1])