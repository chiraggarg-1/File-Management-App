import os


def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename}: Created Successfully")
    except FileExistsError:
        print(f"File Name {filename} already exists!")

    except Exception as e:
        print("An Error Occurred")


def view_all_files():
    files = os.listdir()
    if not files:
        print("No Files Found!")
    else:
        print("files in Directory!")
        for file in files:
            print(file)


def delete_file(filename):
     try:
         os.remove(filename)
         print(f"{filename} has been Deleted Successfully!")

     except FileNotFoundError:
         print("File Not Found")

     except Exception as e:
         print("An error Occurred")




 def read_file(filename):
     try:
         with open('SampleFile.txt','r') as f:
             content = f.read()
             print(f"Content of '{filename}' :\n{content}")

     except FileNotFoundError:
             print(f"{filename} doesn't exist")

     except Exception as e:
             print('An error Occurred!')




 def edit_file(filename):
     try:
         with open('sample.txt' , 'a')  as f:
             content = input('Enter data to add =')
             f.write(content + '\n')
             print(f"{content} added to {filename} Successfully")

     except FileNotFoundError:
         print(f"{filename} doesn't Exist!")

     except Exception as E:
         print('An error Occurred!')




 def main():
     while True:
         print("FILE MANAGEMENT APP")
         print("1. CREATE A FILE")
         print("2. VIEW ALL FILES")
         print("3. DELETE A FILE")
         print("4. READ A FILE")
         print("5. EDIT A FILE")
         print("6. EXIT")

         choice = int(input("Enter Your Choice(1-6) = "))

         if choice == 1:
             filename = input("Enter the Filename to create a new File =")
             create_file(filename)

         elif choice == 2:
             view_all_files()

         elif choice == 3:
             filename = input("Enter the Filename You want to Delete =")
             delete_file(filename)

         elif choice == 4:
             filename = input("Enter the Filename You want to Read =")
             read_file(filename)

         elif choice == 5:
             filename = input("Enter the Filename You want to Edit =")
             edit_file(filename)

         elif choice == 6:
             print("CLOSING THE APP...")
             break

         else:
             print("INVALID INPUT")


if __name__ == "__main__":
    main()








