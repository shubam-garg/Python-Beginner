# write a program to read the text from given file "rendom.txt" and any specific word.
with open("rendom.txt", "r") as f:
    z=f.read()
    if "am" in z:
        print("am word is in the file")
    else:
        print("am word is not present")