import sys
import os
import time
import shutil

def DirectoryCopy(DirName, NewDir):

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
    
    Ret = os.makedirs(NewDir, exist_ok=True)

    if(Ret == False):
        print("Failed to create directory")
        return
    
    TotalCount = 0

    for Folder, SubFolder, FileName in os.walk(DirName):

        for fname in FileName:
            TotalCount = TotalCount + 1
            path = os.path.join(Folder, fname)
            destpath = os.path.join(NewDir, fname)

            shutil.copy2(path,destpath)

    fobj.write("Total files copied : "+str(TotalCount)+"\n")
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    if(len(sys.argv) < 3):
        print("Invalid number of inputs")
        return
    
    DirectoryCopy(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()