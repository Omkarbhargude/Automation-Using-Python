import sys
import os
import time
from pathlib import Path

def DirectoryScanner(DirName, OldExt, NewExt):

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
    
    TotalCount = 0
    fCount = 0
    
    for Folder, SubFolder, FileName in os.walk(DirName):

        for fname in FileName:
            TotalCount = TotalCount + 1

            if fname.endswith(OldExt):
                fCount = fCount + 1

                OldPath = os.path.join(Folder, fname)
                Newfile = fname.replace(OldExt, NewExt)
                NewPath = os.path.join(Folder, Newfile)

                os.rename(OldPath, NewPath)              

    fobj.write("Total files scanned : "+str(TotalCount)+"\n")
    fobj.write(f"Total files with {OldExt} scanned : "+str(fCount)+"\n")
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    if(len(sys.argv) < 4):
        print("Invalid number of inputs")
        return

    DirectoryScanner(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()