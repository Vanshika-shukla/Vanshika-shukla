# find the largest element in a given list

list=[2,99,56,766]
list.sort()
print(list)
n=len(list)
print(list[n-1])

# a function to count the occurence of each element in a list

#list=[2,2,2,2,5,8,10,33,55,66,89,99]

def count_each(list,x):
    count=0
    n=len(list)
    for i in range(0,n):
        if(list[i]==x):
            count=count+1
    return count

list=[2,2,2,2,5,8,10,33,55,66,89,99]
print(count_each(list,2))

#python program to find the second largest number in  a list

numbers=[1,2,3,4,5,6,99,88,45]
numbers.sort()
n=len(numbers)

print(numbers[n-2])

#fxn to remove duplicate elements from list

def rem_dup(list,x):

    for element in list:
        if(element==x):
            list.remove(element)
            print(list)

list=[1,1,2,2,2,3,4]
rem_dup(list,2)

#sorting

list=[60,54,48,42,30,88,95]
list.sort()
print(list)

#function to find the sum of all elements of a list

def sum_add():
    n=len(list)
    sum=0
    for i in range(0,n):
        sum=sum+list[i]
    print(sum)

list=[1,2,3,4,5]
sum_add()


#common element between two list

a=[11,13,15,17]
b=[33,44,13,15,16,18,20]
z=[]

for i in a:
    if i in b:
        z.append(i)


print(z)


#median of the elemenets of a list

list=[2,6,1,34,65,92,55]
def median(list):
    list.sort()
    n=len(list)

    if(n%2==0):
        return list[n//2]
    else:
        a= list[n//2-1]
        b=list[n//2]
        return (a+b)/2


print(median(list))