import sys
import os
from readNexport import parser



def main(filepath):
    
    assert os.path.exists(filepath), "I did not find the file at, "+str(filepath) + "Example Input: ~/path_to_file.csv"
    print("Your file was found!")
    cleanFile = parser.parseClass(filepath)
    cleanFile.parseData()


if __name__ == "__main__":
    main(sys.argv[1])