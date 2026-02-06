import sys
import os
import time
import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()


    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirName):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateCheckSum(fname)

            if(CheckSum in Duplicate):
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate


def DirectoryCheckSum(DirName):

    Border = "-"*60

    timestamp = time.ctime()

    LogFileName = "Log.txt"
    

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This log file was created by Marvellous Automation"+"\n")
    fobj.write(Border+"\n")

    Ret = True

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    MyDict = FindDuplicate(DirName)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))
    Count = 0
    Cnt = 0

    # ------------------------------------------------------------------- #
    fobj.write("Names of duplicate files are : "+"\n")
    for value in Result:    
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
               os.remove(subvalue)
               fobj.write(subvalue+"\n")
               Cnt = Cnt + 1

        Count = 0
    
    # ------------------------------------------------------------------- #

    fobj.write("Total Duplicate files deleted : "+str(Cnt)+"\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    if(len(sys.argv) > 3):
        print("Invalid number of inputs")
        return

    DirectoryCheckSum(sys.argv[1])

if __name__ == "__main__":
    main()