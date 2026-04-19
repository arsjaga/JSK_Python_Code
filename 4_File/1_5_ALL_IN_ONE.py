import os
import file 

def collect_data():
    list_names = []
    input_names = str(input("Enter the Name : "))
    list_names.append(input_names)
    return list_names


def main():    
    write_file = file.open_file("guest.csv", 'w')
    file.write_file(write_file, "username\n")
    names = collect_data()
    write_file.write(names[0] + "\n")
    file.close_file(write_file)
    
    file.read_file("guest.csv")



if __name__ == "__main__":
    main()