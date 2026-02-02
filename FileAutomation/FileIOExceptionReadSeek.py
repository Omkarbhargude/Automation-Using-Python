def main():

    try:
        fobj = open("Hello.txt","r")
        print("File gets successfully opened")

        print("Current offset is : ",fobj.tell())   # 0 offset

        fobj.seek(7)
        
        print("Current offset is : ",fobj.tell())   # 7 offset

        Data = fobj.read(10)
        
        print("Current offset is : ",fobj.tell())   # 17 offset

        print("Data from file is : ",Data)
        
        fobj.close()

    except FileNotFoundError:
        print("Unable to open as there is no such file")

    finally:
        print("End of aplication")

if __name__ == "__main__":
    main()