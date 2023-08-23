FILE_NAME="source.txt"

dptr=open(FILE_NAME,"r")

data=dptr.read()
print(data)

listVar=data.split(",")
print(listVar)

dptr.close()

