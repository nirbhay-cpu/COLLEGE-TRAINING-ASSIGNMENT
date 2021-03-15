#  SENDER PHASE

print("MESSAGE SENDER:\nHello MIT CELL:")
print('Please enter k value to shift transform message:')
k=int(input())                                          # taking key value by sender
a=input('Now please type your message:')                # sender message

m=""
for i in a:                                             # taking one character at a time

    if i.isalnum():                                     # checking given conditions
        m=m+chr(ord(i)+k)
    elif i==" ":
        m+='@'
    elif i==".":
        m+="#"
    else:
        m+=i
print("You send- " ,m)                                  # printing decoded message

# RECEIVER PHASE


print("MESSAGE SENDER:\nHello instructor:")
print("You got a message: ",m)
k1=int(input("To read this in original type k value provided by Cell:-"))  # key value entered by receiver

if k == k1:                                                     # if both key is match then
    print("Original message: ",a)                               # original message is print
else:                                                           # otherwise incorrect key
    print("Incorrect key")


