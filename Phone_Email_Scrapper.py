
import re
import pyperclip  #for copy pasting text from clipboard

#TODO : create a regex for phone number
phoneRegex= re.compile(r'''
# 414-555-3333 ,555-3333 (414)555-3333 ,555-3333 ext  1234 , ext. 1234, x12344
(
((\d\d\d) | (\(\d\d\d\))) ? #area code (optional) entire area code can be optional so ? used
(\s|-)                  #first seperator
\d\d\d                        #first 3 digit
-                       #seperator
\d\d\d\d                #last 4 digit
(((ext(\.)?\s)|x) #extension word-part (optional)
(\d{2,5}))?               #ext with number part(optinal),,,, whole word-part + number part is optional together so ?
)
''',re.VERBOSE)  #in verbose mode we can have the code in multiline and along  with comments

#TODO : create a regex for email address
emailRegex= re.compile(r'''
#some.+thing@(\d{2,5}))?.com  can have . , +
[a-zA-Z0-9_.+]      #name part
@                     #@ symbol
[a-zA-Z0-9_.+]     #domain part

''',re.VERBOSE)
#TODO : get text off the clip board
text = pyperclip.paste()

#TODO : extract email/phone from this text

extractedPhone=phoneRegex.findall(text)
extractedEmail =emailRegex.findall(text)
#install sudo apt-get install xsel for copy paste mechanism

allPhone =[]
for phoneNo in extractedPhone:
    allPhone.append(phoneNo[0])

print(extractedEmail)
print(extractedPhone)


#TODO : copy extracted email.phone to clipboard

#join takes a list of string e.g:our phone no,  and joins to single string with \n in between
result = '\n'.join(allPhone)  +'\n'+ '\n'.join(extractedEmail)
pyperclip.copy(result)
