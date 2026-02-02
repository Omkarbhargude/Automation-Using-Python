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
    
    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fName in FileName:
            fName = os.path.join(FolderName,fName)
            print("File Name : ",fName)
            print("File Size : ",os.path.getsize(fName))


def main():
    Border = "-"*53
    print(Border)
    print("---------- Marvellous Directory Automation ----------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of arguments")
        print("Please specify the name of directory")
        return

    DirectoryScanner(sys.argv[1])


if __name__ == "__main__":
    main()