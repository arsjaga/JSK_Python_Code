import os


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None


def write_file(file_path, content, mode="w"):
    try:
        with open(file_path, mode, encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing file '{file_path}': {e}")
        return False


def append_file(file_path, content):
    return write_file(file_path, content, mode="a")


def file_exists(file_path):
    return os.path.exists(file_path)