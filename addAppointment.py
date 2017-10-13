import random
import linecache
# add appointment
def addapp(subject,tutor,comm,date,start,end,cost):
    dataFile = open("data.txt", "a")
    dataFile.write("#" + "subject:"+subject+"\n")
    dataFile.write(">" + "tutor:"+tutor+"\n")
    dataFile.write(">" + "client:"+"N/A"+"\n")
    dataFile.write(">" + "comm:"+comm+"\n")
    dataFile.write(">" + "date:"+date+"\n")
    dataFile.write(">" + "start:"+start+"\n")
    dataFile.write(">" + "end:"+end+"\n")
    dataFile.write(">" + "cash:"+cost+"\n")
    dataFile.close()


# gets the number of files in a file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# adds random appointments to the data.txt file for testing
def addtest(repeats):
    for x in range(0,repeats):
        names = str(linecache.getline("randomThings/names.txt", random.randint(1, file_len("randomThings/names.txt")))[0:-1])
        classes = str(linecache.getline("randomThings/classes.txt",random.randint(1, file_len("randomThings/classes.txt")))[0:-1])
        addapp(classes + " " + str(random.randint(0, 999)), names, names + "@email.com",str(random.randint(1,12))+"-"+str(random.randint(1,28))+"-"+str(17), str(random.randint(1,1200)), str(random.randint(1201,2399)), "0")



addtest(5)