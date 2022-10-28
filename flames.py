# Flames relationship calculator using python
name1 = input("enter your name: ")
n1 = name1.upper() #formatting the inputs
name2 = input("enter your partner's name : ")
n2 = name2.upper() #formatting the inputs
names1 = name1.replace(" ", "") #removing whitespaces
names2 = name2.replace(" ", "") #removing whitespaces
names1 = list(name1) #changing str to list for accessing it
names2 = list(name2) #changing str to list for accessing it

for x in names1[:]: #here x is item in names1
    if x in names2: # if x is availabe in names2 then remove it from both name 1 and 2
        names1.remove(x)
        names2.remove(x)
n = len(names1) + len(names2) # to find the index, we need to find the sum of both name 1 anf 2 lengths

lis = ["Friend", "Lover", "Affectionate", "Marriage", "Enemy", "Sibling"] 

while len(lis)>1: #in result we need to print index(value) from lis therefore (len(lis)>1)
    index = n%len(lis)-1   #calculating index
    if index >= 0:
        right = lis[index+1:] #spliting the list elements and using index we can remove the item from list
        left = lis[:index]
        lis = right + left # joining the list
    else:
        lis = lis[:len(lis)-1]
liss = str(lis).strip("['']")       # formatting the list for result 
print(f"{n1} is {liss} to {n2}") #result
# nxt goal is to develop this with GUI

#By - DineshTwen :)