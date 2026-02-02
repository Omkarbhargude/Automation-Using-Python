import hashlib
import os

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")          # binary mode

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)


    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()


def DirectoryWatcher(DirName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateCheckSum(fname)

            print(f"File name : {fname} Checksum : {CheckSum}")

def main():

    DirectoryWatcher()

if __name__ == "__main__":
    main()