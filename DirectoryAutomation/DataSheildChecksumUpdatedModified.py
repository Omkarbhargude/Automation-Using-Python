import sys
import os
import time
import schedule
import shutil
import hashlib

def Calculate_hash(path):

    hobj = hashlib.md5()

    fobj = open(path, "rb")

    while(True):
        data = fobj.read(1024)

        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source, Destination):
    
    Copied_Files = []

    print("Creating the backup folder for backup process")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):

        for file in files:
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # copy the files if its new or updated
            if((not os.path.exists(dest_path)) or (Calculate_hash(src_path) != Calculate_hash(dest_path))):
                shutil.copy2(src_path, dest_path)
                Copied_Files.append(relative)

    return Copied_Files   

def MarvellousDataSheildStart(Source = "Data"):
    BackupName = "MarvellousBackup"

    print("Backup Process Started Successfully at : ",time.ctime())

    files = BackupFiles(Source, BackupName)

    print("Report about the backup")
    for name in files:
        print(name)

        
def main():
    Border = "-"*55

    print(Border)
    print("----------- Marvellous Data Sheild System -------------")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : Time in minutes for periodic scheduling")
            print("Source Directory : Name of directory to backed up")

        else:
            print("Unable to proceed  as there is no such option")
            print("Please use --h or --u to get more details")


    # python demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside project logic")
        print("Time interval : ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])

        # apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataSheildStart, sys.argv[2])

        print("Data Sheild started successfully")
        print("Time interval in minutes: ",sys.argv[1])
        print("Press CTRL + C to stop the execution")

        # wait till abort
        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed  as there is no such option")
        print("Please use --h or --u to get more details")


    print(Border)
    print("----------- Thank you for using our script ------------")
    print(Border)

if __name__ == "__main__":
    main()