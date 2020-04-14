def isPhoneNumber(text): #415-333-5555
    if len(text)!=12:
        return False #incorrect size
    for i in range(0,3):
        if not text[i].isdecimal():
            return False #first 3 chars not num
    if text[3]!='-':
        return False #missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!= '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False #missing last 4 digit
    return True
message = 'call me on 415-444-5555 tomorrow or  555-777-7777' \
          'theere is 777-777-9898 andanfkbfd fgfd  888-999-000'
foundNo= False

# traverse through all the characters in "message string" ,
# if i =0 then it will grabe first 12 characters
#if i=1, then grab 12 chars from index i=1
#it will do so, untill it finds 12 character consisting of numbers
for i in range(len(message)):
    chunk =message[i:i+12] #slice method from i to i+12
    if isPhoneNumber(chunk):
        print('phone number found is '+ chunk)
        foundNo = True
if not foundNo:
    print('could not find the phone number')
