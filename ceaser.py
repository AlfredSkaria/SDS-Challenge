strng = input("Enter the string to encrypt:")
key = int(input("Enter key:"))
print("Your encrypted string:")
for i in strng:
    if(ord(i)>=97 and ord(i)<=122):
        j = (ord(i)-97+key) % 26
        m = j+97
    elif(ord(i)>=65 and ord(i)<=90):
        j = (ord(i) - 65 + key) % 26
        m = j + 65
    else:
        m=ord(i)
    print(chr(m),end="")