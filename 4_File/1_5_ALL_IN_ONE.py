import os

def open_file(filename, mode):
    try:
        return open(filename, mode)
    except Exception as e:
        print(f"Error in open file {filename} as {e}")
        return None

def read_file(filename):
    read_file = open_file(filename, 'r')
    if read_file:
        try:
            read_content = read_file.read()
            print(read_content)
        except Exception as e:
            print(f"Error Read file {filename} as {e}")
            return None
        finally:
            read_file.close()



def main():

    
    write_file = open("guest.csv", 'w')
    write_file.write("username\n")
    list_names = []
    input_names = str(input("Enter the Name : "))
    list_names.append(input_names)
    print(list_names)
    write_file.write(list_names[0] + "\n")
    write_file.close()

    read_file("guest.csv")



if __name__ == "__main__":
    main()