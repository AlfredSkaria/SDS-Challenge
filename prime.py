num = int(input("Enter the number:"))
arr = []
def prime(first,last,inc):

    c = 0
    for i in range(first,last,inc):   #for taking numbers
        for j in range(1,i+1,1):   #for checking primality
            if(i%j==0):             #Divisibility check by 2
                c=c+1
        if(c==2):
            arr.append(i)
            break
        c=0

prime(num-1,0,-1)
arr.append(num)
prime(num+1,num+100,1)
print (arr)

