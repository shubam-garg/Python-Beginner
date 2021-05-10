# write program to mine a log file and find out whether it contains 'python'

with open("log_file.txt") as f:
    log = f.read().lower()
    # lower is used here to take whole file in lower case because python is k-sensitive

if 'python' in log:
    print("yes")
else:
    print("no")