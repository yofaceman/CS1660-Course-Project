import tarfile
import time
import os

fileList = []

def readFiles():
    
    input_files = input("enter files here, if multiple files seperate each with a space: ")
    input_files = input_files.split(" ")
    
    try:
        ##print(input_files)
        for item in input_files:
            if(os.path.isdir(item[:-7])):
                for root, dirs, files in os.walk(item[:-7]):
                    for fileName in files:
                        fileList.append(fileName)
                        ##Send File to second application
                continue
            file = tarfile.open('Data/'+item)
            file.extractall('./'+item[:-7])
            file.close()
            for root, dirs, files in os.walk(item[:-7]):
                for fileName in files:
                    fileList.append(fileName)
                    ##Send file to second application

        x = 1
        print('\n\nTHIS IS THE LIST OF FILES TO BE INDEXED\n\n')
        for file in fileList:
            print(str(x)+'.'+file)
            x = x+1
        print('\n\nTHIS IS THE LIST OF FILES TO BE INDEXED\n\n')
        loadPage()
    except Exception as e:
        print(e)

def loadPage():
    user_input = input("\nWould you like to...(Please type corresponding number)\n1. Input Different Files\n2. Load Engine \n")
    if(user_input == "1"):
        readFiles()
    elif(user_input == "2"):
        loadEngine()
    else:
        print("ERROR: You did not type either option '1' or option '2'")
        loadPage()
    
def loadEngine():
    print("\nEngine was loaded & Inverted indicies were constructed successfully!")
    user_input = input("Please Select Action...(type corresponding number)\n1.Search for Term\n2.Top-N\n")
    if(user_input == "1"):
        searchPage()
    elif(user_input == "2"):
        nValuePage()
    else:
        print("ERROR: You did not type either option '1' or option '2'")
        loadEngine()

def searchPage():
    user_input = input("\nEnter Your Search Term\n")
    start = time.time()
    searchResultsPage(user_input, start)

def searchResultsPage(user_input, start):
    print("\nYou searched for the term:" + user_input)
    time.sleep(1)
    end = time.time()
    print("\nYour search was executed in {}ms".format((end-start)*1000))
    x = input("Press [Enter] to go back to Search (or type 'EXIT' to quit the program)")
    if(x == "EXIT"):
        exit(0)
    loadEngine()

def nValuePage():
    user_input = input("\nEnter Your N Value\n")
    start = time.time()
    nValueResultsPage(user_input)

def nValueResultsPage(user_input):
    print("\nTop-N Frequent Terms")
    x =input("Press [Enter] to go back to Search (or type 'EXIT' to quit the program)\n")
    if(x == "EXIT"):
        exit(0)
    loadEngine()

readFiles()
