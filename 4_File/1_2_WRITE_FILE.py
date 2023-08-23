Name_List = ['jagadish','Ajith','Sundar','Harish','Ganesh','Arun']

FILE_NAME="source.txt"

sptr=open(FILE_NAME,"w")

for i in Name_List:
    sptr.write(i+",\n")
sptr.close()


#FILE_NAME="destnation.txt"

#dptr=open(FILE_NAME,"r")

#for i in sptr:
#    dptr.read('%s\n' %i)
#dptr.close()
