import os

def DirectoryScanner(DirectoryName):
    print("Contents of the directory are : ")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder Name : ",FolderName)

        for SubF in SubFolderName:
            print("SubFolder name : ",SubF)

        for fName in FileName:
            print("File name : ",fName)

def main():

    DirectoryName = input("Enter the name of directory : ")

    DirectoryScanner(DirectoryName)
    
    
if __name__ == "__main__":
    main()