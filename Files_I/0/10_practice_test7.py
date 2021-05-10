# Write a program to find out the line no where python is present
log=True
i=1
with open("log_file.txt") as f:
    while log:
        log = f.readline()
        if "python" in log.lower():
            print(log)
            print(f"{i}")
        i+=1
