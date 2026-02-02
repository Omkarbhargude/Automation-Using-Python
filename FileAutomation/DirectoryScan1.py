import os

def main():
    DirectoryName = input("Enter the name of directory : ")

    print("Contents of the directory are : ")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder Name : ",FolderName)

        for SubF in SubFolderName:
            print("SubFolder name : ",SubF)

        for fName in FileName:
            print("File name : ",fName)
if __name__ == "__main__":
    main()