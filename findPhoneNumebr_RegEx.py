import re

message = 'call me on 415-444-5555 tomorrow or  555-777-7777'
phoneNumbRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#r' means raw string  , re.compile() to create  regex object
# \d is for numebric character
mo= phoneNumbRegex.search(message) #search() is to create match object mo
findal= phoneNumbRegex.findall(message)

print(mo) # search finds only 1st occrance
print(mo.group()) # search finds only 1st occrance
print(findal) #print(findal.group()) #findall finds all


phoneNumbRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo= phoneNumbRegex.search(message) #415
print('regex to get first set of number i.e 3 dgits ='+mo.group(1))


phoneNumbRegex = re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d')
#message = 'call me on (415)-444-5555 tomorrow or  555-777-7777'
mo= phoneNumbRegex.search('call me on (415)-444-5555') #415
print('regex to get phone (415) within bracker ='+mo.group())

#search a text pattern

batRegex = re.compile(r'bat(car|mobile|copter|man)')
str = 'batman has a batcopter'
mo = batRegex.search(str)
print(mo.group()) #batman
mo = batRegex.findall(str)
print(mo) #['man', 'copter']
