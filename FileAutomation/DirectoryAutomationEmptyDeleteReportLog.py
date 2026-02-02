import sys
import os

def DirectoryScanner(DirName = "Marvellous"):
    Border = "-"*60

    fobj = open("Marvellous.log","w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation"+"\n")
    fobj.write("This is a directory cleaner script"+"\n")
    fobj.write(Border+"\n")

    Ret = False

    Ret = os.path.exists(DirName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    FileCount = 0
    EmptyFileCount = 0
    for FolderName, SubFolder, FileName in os.walk(DirName):
        
        for fName in FileName:
            FileCount = FileCount + 1

            fName = os.path.join(FolderName,fName)
            
            # If empty file found then delete
            if(os.path.getsize(fName) == 0):
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fName)

    fobj.write(Border+"\n")
    fobj.write("Total files scanned : "+str(FileCount)+"\n")
    fobj.write("Total empty files found : "+str(EmptyFileCount)+"\n")
    fobj.write(Border+"\n")

    fobj.close()

# --------------------------------------------------------------------------                
def main():
    Border = "-"*60
    print(Border)
    print("-------------- Marvellous Directory Automation --------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of arguments")
        print("Please specify the name of directory")
        return

    DirectoryScanner(sys.argv[1])

    print(Border)
    print("-------------- Marvellous Directory Automation --------------")
    print(Border)


if __name__ == "__main__":
    main()