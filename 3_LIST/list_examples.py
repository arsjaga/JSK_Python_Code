sno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(sno)

# Append

sno.append(11)
print(sno)

#sno.append(11,12)
#print(sno)        #append() takes exactly one argument (2 given)


# Extend 

sno.extend([11,12])
print(sno)


# Insert

sno.insert(1,1.5)
print(sno)


print(sno[1])
print(sno[-2])
print(sno[0:4])
print(sno[-4:-1])