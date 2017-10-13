dataFile=open("randomThings/names.txt","r+")
data=dataFile.readlines()
for line in data:
    if line[0:-2]=="  ":
        data=data[0:-2]