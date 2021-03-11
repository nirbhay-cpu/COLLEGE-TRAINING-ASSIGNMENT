str=input("Enter string\n")       # Taking input string
s1=set()
l2=[]
str=str.lower()                   #  convert string into lower case
a,e,i,o,u=0,0,0,0,0
for j in str:                     # taking each character and check if it is an vowel .
                                  # If it is an vowel then increase respective counter and add in set s1
    if 'a' == j:
        a+=1
        s1.add("a")
    elif "e" == j:
        e+=1
        s1.add("e")
    elif "o" == j :
        o+=1
        s1.add("o")
    elif "i" == j :
        i+=1
        s1.add("i")
    elif "u" == j :
        u+=1
        s1.add("u")

for j in s1:                     # Now, check which vowels are occur and append their corresponding occurence value in list
    if j=="a":
        l2.append(a)
    if j=="e":
        l2.append(e)
    if j=="i":
        l2.append(i)
    if j=="o":
        l2.append(o)
    if j=="u":
        l2.append(u)

print(s1,"\n",l2)             # printing set amd list




