'''
This program reads through the email and finds all the lines 
that contain From: and To: .

We will count the following:

usernames in the From: field
hosts in the From: field
usernames in the To: field
hosts in the To: field

We will print the different objects in csv format
'''
# To access STDOUT
import sys
#To access .writerows()
import csv

#Creating file handle to read file
fhand = open('mbox-short.txt')

# connect a csv.writer filehandle to STDOUT
cw = csv.writer(sys.stdout)

#Empty list to store information
fromto = []
fromAdd=[]
toAdd=[]
frUsers=[]
frHosts=[]
toUsers=[]
toHosts=[]

#Read through each line in the file, Strip white space
for line in fhand:
    line= line.rstrip()
    #If the line starts with From: then append the line to a list and split by the whitespace
    #Append the second character to a new list
    if line.startswith('From:'):
        fromto.append(line)
        frWords = line.split()
        fromAdd.append(frWords[1])
        
    #If the line starts with To: then append the line to a list and split by the whitespace
    #Append the second character to a new list    
    elif line.startswith('To:'):
        fromto.append(line)
        toWords = line.split()
        toAdd.append(toWords[1])

#go through each item in the list and split at the @ and append each item to a new list
for frItem in fromAdd:
    obj = frItem.rstrip()
    for x,y in [frItem.split('@')]:
        frUsers.append(x)
        frHosts.append(y)

#go through each item in the list and split at the @ and append each item to a new list    
for toItem in toAdd:
    obj = toItem.rstrip()
    for a,b in [toItem.split('@')]:
        toUsers.append(a)
        toHosts.append(b) 
#Create a dictionary
#Iterate throught the list and count each occurance and add the item and the occurance to the dictionary
fromUsers=dict()
for i in frUsers:
    fromUsers[i]=fromUsers.get(i,0)+1

#Print the header and use .writerows to display the information
print('--- FROM USER ---')
cw.writerows(sorted(fromUsers.items()))

#Create a dictionary
#Iterate throught the list and count each occurance and add the item and the occurance to the dictionary
fromHosts=dict()
for i in frHosts:
    fromHosts[i]=fromHosts.get(i,0)+1

#Print the header and use .writerows to display the information
print('--- FROM HOST ---')
cw.writerows(sorted(fromHosts.items()))

#Create a dictionary
#Iterate throught the list and count each occurance and add the item and the occurance to the dictionary
tooUsers=dict()
for i in toUsers:
    tooUsers[i]=tooUsers.get(i,0)+1
#Print the header and use .writerows to display the information
print('--- TO USER ---')
cw.writerows(sorted(tooUsers.items()))

#Create a dictionary
#Iterate throught the list and count each occurance and add the item and the occurance to the dictionary
tooHosts=dict()
for i in toHosts:
    tooHosts[i]=tooHosts.get(i,0)+1
#Print the header and use .writerows to display the information
print('--- TO HOST ---')
cw.writerows(sorted(tooHosts.items()))

# print(toAdd)
