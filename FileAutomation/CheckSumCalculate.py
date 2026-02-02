import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")          # binary mode

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)


    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()


def main():
    Ret = CalculateCheckSum("Demo.txt")

    print("CheckSum is : ",Ret)

if __name__ == "__main__":
    main()