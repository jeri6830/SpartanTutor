# retrieve an appointment
import linecache
appointmentSize=8
def search(query,subject):
    dataFile = open("data.txt", "r")
    data = dataFile.readline()
    counter=1-appointmentSize
    returnme=[]
    while data != "":
        print counter
        if(data[0:1]=="#"):
            counter+=appointmentSize
        if data.split(":")[0][1:] == query:
            if data.split(":")[1][:-1] == subject:
                print("found target")
                returnme.append(counter)
        data=dataFile.readline()
    return returnme


def getappointment(mynumber):
    returnme=[]
    if(linecache.getline("data.txt",mynumber))[0:1]=="#":
        for x in range(0,appointmentSize,1):
            data=linecache.getline("data.txt",mynumber+x).split(":")[1][:-1]
            returnme.append(data)
    return returnme