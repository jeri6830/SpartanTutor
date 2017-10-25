import linecache
offset = 2;
def claim(appointmentnumber,client):
    with open("data.txt","r") as file:
        data=file.readlines()
    if data[appointmentnumber-1][0:1] == "#":
        data[appointmentnumber-1+offset]=">client:"+client+"\n"
        with open("data.txt","w") as file:
            file.writelines(data)

claim(1,"Steve")