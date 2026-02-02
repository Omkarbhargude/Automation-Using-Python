import sys
import os

def DirectoryScanner(DirName = "Marvellous"):
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
            print("File Name : ",fName)
            print("File Size : ",os.path.getsize(fName))
            
            # empty file found then delete
            if(os.path.getsize(fName) == 0):
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fName)

    Border = "-"*60
    print(Border)
    print("-------------------- Automation Report -------------------")
    print("Total files scanned : ",FileCount)
    print("Total empty files found : ",EmptyFileCount)
    print(Border)


                



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