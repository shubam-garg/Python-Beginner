# write a program which should work continue after not finding any file or error
def readFile(fileName):
    try:
        with open(fileName) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {fileName} is not found")

readFile("file1.txt")
readFile("file2.txt")
readFile("file3.txt")    