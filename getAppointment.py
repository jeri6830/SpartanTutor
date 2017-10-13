# retrieve an appointment
import linecache
name = "Karly"
dataFile=open("data.txt","r")
data=dataFile.readline()
while data!="":
    if data[0:1]=="#":
        for x in range(0,8):
            print data[1:-1]
            data=dataFile.readline()
    data=dataFile.readline()
def search(query,search):
    dataFile = open("data.txt", "r")
    data = dataFile.readline()
    counter=1
    while data != "":
        data=linecache.getline("data.txt",counter)
        if data.split(":")[0][1:] == query:
            