import sys
import os
import time

def DirectoryFileSearch(DirName, FileExt):

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

            if fname.endswith(FileExt):
                fCount = fCount + 1
                print(fname)


    fobj.write("Total files scanned : "+str(TotalCount)+"\n")
    fobj.write(f"Total files with {FileExt} scanned : "+str(fCount)+"\n")
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    if(len(sys.argv) > 3):
        print("Invalid number of inputs")
        return

    DirectoryScanner(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()