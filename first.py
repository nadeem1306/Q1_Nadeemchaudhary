string=input()
arr=[]
three=[]
two=[]
for i in string:
    arr.append(i)
myarr=set(arr)
for i in myarr:
    if string.count(i)>2:
        three.append(i)
    if string.count(i)==2:
        two.append(i)
for i in range(len(string)):
    if string[i] in two:
        string=string.replace(string[i],"Z")
    if string[i] in three:
        string=string.replace(string[i],"X")
print(string)
