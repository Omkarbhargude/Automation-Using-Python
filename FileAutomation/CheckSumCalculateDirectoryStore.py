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


def FindDuplicate(DirName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateCheckSum(fname)

            if(CheckSum in Duplicate):
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate

def DisplayResult(MyDict):

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            print(subvalue)

        print("Value of count is : ",Count)
        Count = 0

def DeleteDuplicate(Path = "Marvellous"):
    MyDict = FindDuplicate(Path)
    
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))
    Count = 0
    Cnt = 0


    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                print("Deleted file : ",subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1

        Count = 0

    print("Total deleted file : ",Cnt)

def main():

    DeleteDuplicate()

if __name__ == "__main__":
    main()