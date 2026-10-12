import os
from datetime import datetime
timestamp=0
Diary_File="Personal_Diary.txt"

def write_Entry():
    try:
        entry=input("Write your Diary entry:")
        with open(Diary_File,"a") as f:
            f.write("\n ",entry)
            timestamp=datetime.now().strftime("%y-%m-%d %H:%M:%S")
        print("Your entry has been saved at ",timestamp)


    except PermissionError:
        print("Error Message: You do not have permission to write to this file.")

    except Exception as e:
        print("An unexpected Error occured",e)

def View_Entry():
    try:
        if not os.path.exists(Diary_File):
            print("No File Found")
            return

        with open(Diary_File,"r") as f:
           content=f.read()
           
        print("Your Diary entries are:\n","Last saved on",timestamp)
        print(content)
    except FileNotFoundError:
            print("Error: Diary file could not be found")
    except PermissionError:
            print("Error:Permission Denied")
    except Exception as e:
            print("An unexpected error occured",e)

def main():
    while True:
        print("\n-----Personal Diary Option")
        print("1.  Write a new Entry")
        print("2.  View Previous Entries")
        print('3.  Exit')

        option=input("Select an Option 1-3:   ")
        if option=="1":
                write_Entry()
        elif option=="2":
                View_Entry()
        elif option=="3":
                print("Goodbye!")
                break
        else:
                print("Invalid Choice. Please choose 1,2 or 3")

main()