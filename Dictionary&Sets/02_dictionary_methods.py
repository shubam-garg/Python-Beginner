dic={
    "abruptly":"Move Quickly",
    "shubam":"A King",
    "marks":[2,677,4434,2,7],
    "otherdic":{'friend':'fozi'},# nested dictionary
     1: [2,3]
}
print(type(dic.keys()))
print(list(dic.keys()))
print(dic.keys())# print the keys of dictionary
print(dic.values())# print the keys of dictionary
print(dic.items())# print the keys and values of dictionary
print(dic)
updatedic={
    "none":"empty",
    "shubam":"shilpa"  # update the value of existing keys
}
dic.update(updatedic) # add new keys and values in dictionary
print(dic)
print(dic.get("shubam")) 
print(dic.get("shub34")) # this function will return none a output if does not exist in dic
print(dic["shub34"])# this will through error if does not exist in dic
# better to use get function