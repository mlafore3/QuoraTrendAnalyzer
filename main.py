import sys
import os
from Methods import parser, analyzeNexport, convert

#This method takes in a filepath argument and creates an parser class
#from the readNexport bin. This class activates the necessary prompts 
#and allows the modification of data file

def main(filepath):
    
    #make sure the filepath is found 
    assert os.path.exists(filepath), "I did not find the file at, "+str(filepath) + "Example Input: ~/path_to_file.csv"
    print("Your file was found!")
    
    #Instantiate a parseClass object that returns and stores a parsed file
    parsedFile = parser.parseClass(filepath).parseMethod()

    #Then plot the column diversity of the input file
    convert.convertNplotClass(parsedFile).plot()
    
    #Use the analyzeNexport class to intitiate a user prompt to let the user
    #analyze the parsed data file and modify its contents in a new file
    analyzeNexport.analyzeClass(parsedFile).busStation()

#run the main method if it is name and require a filepath argument 
if __name__ == "__main__":
    main(sys.argv[1])