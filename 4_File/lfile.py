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

def write_file(filename, content):
    try:
        filename.write(content)
    except Exception as e:
        print(f"Error Write file {filename} as {e}")
        return None
    
def close_file(filename):
    try:
        filename.close()
    except Exception as e:
        print(f"Error close file {filename} as {e}")
        return None