def main():

    try:
        fobj = open("Hello.txt","w")
        print("File gets successfully opened")

        fobj.write("Jay Ganesh Marvellous...")

        fobj.close()

    except FileNotFoundError:
        print("Unable to open as there is no such file")

    finally:
        print("End of aplication")

if __name__ == "__main__":
    main()