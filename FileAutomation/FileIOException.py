def main():
    try:
        open("Demo.txt")
        print("File gets successfully opened")

    except FileNotFoundError:
        print("Unable to open as there is no such file")

    finally:
        print("End of aplication")

if __name__ == "__main__":
    main()