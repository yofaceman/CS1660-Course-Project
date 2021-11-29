import tarfile
import time
import os
#from google.cloud import storage
import glob
import shutil
import collections
import re
#from oauth2client.service_account import ServiceAccountCredentials

class Node:
    def __init__(self,title , occurence):
        self.title = title
        self.occurence = occurence  

    def toString(self):
      return self.title + ":\t" + str(self.occurence)


stopwords = set()
dataMap = {}
maxMap = {}
sortedMaxMap = []
fileList = []

with open("stopwords.txt") as sw:
    swlines = sw.readlines()
    for line in swlines:
        #print(line)
        line = line.upper().strip()
        stopwords.add(line)

#storage_client = storage.Client.from_service_account_json('docker-327322-8600d88d9e6e.json')
#bucket = storage_client.bucket("dataproc-staging-us-east1-1006853791664-q5dte3pd")
#blob = bucket.blob('user_input')

#blob.upload_from_filename(source_file_name)
#buckets = list(storage_client.list_buckets())
#print(buckets)

def readFiles():
    file_object = open('user_input', 'w')
    input_files = input("enter files here, if multiple files seperate each with a space: ")
    input_files = input_files.replace('\r', '')
    file_object.write(input_files)
    file_object.close()
    #blob.upload_from_filename("user_input")
    input_files = input_files.split(" ")
    
    try:
        if(os.path.isdir('InputData')):
            shutil.rmtree('InputData')
        ##print(input_files)
        for item in input_files:
            file = tarfile.open('Data/'+item)
            file.extractall('./InputData/'+item[:-7])
            file.close()
            #for root, dirs, files in os.walk(item[:-7]):
                #for fileName in files:
                    #fileList.append(fileName)
                    ##Send file to second application
        
        #blobs = bucket.list_blobs(prefix='InputData/')
        #for blobe in blobs:
            #blobe.delete()
        #upload_local_directory_to_gcs('InputData', bucket, 'InputData')
        loadPage()
    except Exception as e:
        print(e)




def loadPage():
    user_input = input("\nWould you like to...(Please type corresponding number)\n1. Input Different Files\n2. Load Engine \n")
    user_input = user_input.replace('\r', '')
    if(user_input == "1"):
        readFiles()
    elif(user_input == "2"):
        loadEngine()
    else:
        print("ERROR: You did not type either option '1' or option '2'")
        loadPage()
    



def loadEngine():
    loadDataFromGCP()
    #print(maxMap)
    #print(sortedMaxMap)
    print("\nEngine was loaded & Inverted indicies were constructed successfully!")
    user_input = input("Please Select Action...(type corresponding number)\n1.Search for Term\n2.Top-N\n")
    user_input = user_input.replace('\r', '')
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
    user_input = user_input.replace('\r', '')
    searchResultsPage(user_input, start)




def searchResultsPage(user_input, start):
    print("\nYou searched for the term:" + user_input.upper())
    
    if user_input.upper() not in dataMap.keys():
        print( "\n============================\n"+ user_input.upper()+" NOT FOUND IN INVERTED INDEX\n============================\n")
        x = input("Press [Enter] to go back to Search (or type 'EXIT' to quit the program)")
        x = x.replace('\r', '')
        if(x == "EXIT"):
            exit(0)

        loadEngine()

    print_value = dataMap[user_input.upper()]
    end = time.time()

    print("\n\nYour search was executed in {}ms\n\n".format((end-start)*1000))
    word = ""
    for no in print_value:
        word = word +  no.toString() + "\n"

    print("Document\t# ofOccurences\n" + word)
    print("\n\nYour search was executed in {}ms\n\n".format((end-start)*1000))

    x = input("Press [Enter] to go back to Search (or type 'EXIT' to quit the program)")
    x = x.replace('\r', '')

    if(x == "EXIT"):
        exit(0)

    loadEngine()




def nValuePage():
    user_input = input("\nEnter Your N Value\n")
    user_input = user_input.replace('\r', '')
    start = time.time()
    nValueResultsPage(user_input)




def nValueResultsPage(user_input):
    print("\nTop " + str(user_input) + " Frequent Terms")
    sortedMaxMap = (sorted(maxMap.items(), key =
             lambda kv:(kv[1], kv[0]))) 
    print("Term\tTotal Frequencies")
    for x in range(1,int(user_input) + 1):
        print(str(x) + ":" + sortedMaxMap[-x][0] + "\t" + str(sortedMaxMap[-x][1]))
    y =input("Press [Enter] to go back to Search (or type 'EXIT' to quit the program)\n")
    y = y.replace('\r','')
    if(y == "EXIT"):
        exit(0)
    loadEngine()




def upload_local_directory_to_gcs(local_path, bucket, gcs_path):
    assert os.path.isdir(local_path)
    print(local_path)
    for local_file in glob.glob(local_path + '/**', recursive=True):
        print(local_file)
        if os.path.isfile(local_file):
            blobe = bucket.blob(local_path)
            blobe.upload_from_filename(local_file)




def loadDataFromGCP():
    with open("ShakeOut") as f:
        lines = f.readlines()
        for line in lines:
            line.replace('\n', '')
            elements = re.split(' |:|\t|\n', line)
            key = elements[0]

            if(key in stopwords):
                continue

            sum = 0
            nodeList = collections.deque()
            for i in range(1,int((len(elements))/2)):
              n = Node(elements[2*i-1], int(elements[2*i]))
              nodeList.append(n)
              sum= sum + int(elements[2*i])
          
            word = ""
            for no in nodeList:
                word = word +  no.toString() + " "
            dataMap[key] = nodeList
            maxMap[key] = sum

    sortedMaxMap = (sorted(maxMap.items(), key =
             lambda kv:(kv[1], kv[0]))) 
    #print(maxMap)
    #print(dataMap)
    return sortedMaxMap
    

readFiles()
