# Q1. You will be given a list. You have to print a list whose 1st element should be largest and 
# 2nd should be the smallest then the 3rd should be 2nd largest and 4th should be 2nd smallest and so on.
lst = []
size=int(input("Enter the size of list : "))
for i in range(0,size):
    ele=int(input("Enter a Element : "))
    lst.append(ele)
print(lst)
for i in range(0,len(lst),2):
    for j in range(i+1,len(lst)):
        if lst[j]>lst[i]:
            lst[i],lst[j]=lst[j],lst[i]
    for k in range(i+2,len(lst)):
        if lst[i+1]>lst[k]:
            lst[i+1],lst[k]=lst[k],lst[i+1]
print(lst)