# Write a python program to replace or remove a given word from a string and strip it at the same time
def fun1(string, word):
    newstring=string.replace(word, "shilpa!") # for replace
#   newstring=string.replace(word, "") # for remove
    return newstring.strip()

s=("    shubi! How r u    ")
s1 = fun1(s, "shubi!")
print(s1)