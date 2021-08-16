import tkinter.filedialog
from io import FileIO
import hashlib


# Format:
# FileMD5#First250kbFileMD5#FileSize#FileName

def md5(file: FileIO):
    file.seek(0)
    return hashlib.md5(file.read()).hexdigest()


def first_256kb_md5(file: FileIO):
    file.seek(0)
    return hashlib.md5(file.read(256 * 1024)).hexdigest()


def main():
    with tkinter.filedialog.askopenfile('rb') as file:
        p1 = md5(file)
        p2 = first_256kb_md5(file)
        file.seek(0)  # Pointer micro management
        p3 = len(file.read())
        p4 = file.name

    print(f"File MD5 is {p1}")
    print(f"First 256kb MD5 is {p2}")
    print(f"File length is {p3} bytes")
    print(f"File name is {p4}")
    print(f"The Hash is {p1}#{p2}#{p3}#{p4}")


main()
