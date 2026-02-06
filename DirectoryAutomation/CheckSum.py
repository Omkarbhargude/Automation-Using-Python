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

def DirectoryCheckSum(DirName):

    Border = "-"*60

    timestamp = time.ctime()

    LogFileName = "Marvellous%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

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
    
    for Folder, SubFolder, FileName in os.walk(DirName):

        for fname in FileName:

            Ret = CalculateCheckSum(fname)
            print(Ret)

    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    if(len(sys.argv) > 3):
        print("Invalid number of inputs")
        return

    DirectoryCheckSum(sys.argv[1])

if __name__ == "__main__":
    main()