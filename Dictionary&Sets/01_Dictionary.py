# Dic. is collection of key and value
#here key stands for word and value stands for meaning
dic={
    "Abruptly":"Move Quickly",
    "Shubam":"A King",
    "Marks":[2,677,4434,2,7],
    "otherdic":{'friend':'fozi'}# nested dictionary
}

dic['Marks']=[23,45]# it will change the value of marks
print(dic['otherdic']['friend'])
print(dic['Abruptly'])
print(dic['Marks'])