''' write a program to generate multiple tables from 2 to 20 and write it in different files.
    Place thse files in a folder for 13 year old. '''

for i in range(2,21):
    with open(f"Tables/Muplication table of {i}.txt", "w") as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}\n")