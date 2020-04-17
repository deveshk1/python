# GOOGLE SEARCH in PYCHARM
# -----------------------------------
import webbrowser, sys
import pyperclip  # incase if we just copy and take input from clipboard

# sys module to pass argument in cmd line
# bcz cmd line arguments are saved in list variable argv
input = input("enter search value")
sys.argv
# [mapit.py,'222','valiencie','St.']
# check if cmd line arguments were passed


# if we dnt pass any argumnet then the legth of list will be
# 1, else length will be >1
if len(input) > 1:
    # ['mapit','870','valencia','St.'] -> '870 valencia st.' --->address
    # [index=0 ,index =1,index=2, index=3]
    address = ''.join(input)
    '''slice from index=1 to end and join with
        single space'''
else:
    address = pyperclip.paste()  # to paste from clipboard
# https://www.google.com/
webbrowser.open('https://www.google.com/maps/place/' + address)
# -------------------------------------------------------------------------
# google search by creating .py file in CMD LINE

#
# -----------------file =mapit.py ------------------------
#
# import webbrowser,sys
# import pyperclip #incase if we just copy and take input from clipboard
# #sys module to pass argument in cmd line
# #bcz cmd line arguments are saved in list variable argv
#
# sys.argv
# #[mapit.py,'222','valiencie','St.']
# #check if cmd line arguments were passed
#
#
# #if we dnt pass any argumnet then the legth of list will be
# #1, else length will be >1
# if len(sys.argv)>1:
#     #['mapit','870','valencia','St.'] -> '870 valencia st.' --->address
#     #[index=0 ,index =1,index=2, index=3]
#     address =' '.join(sys.argv[1:])
#     #slice from index=1 to end and join with
#      #   single space
# else:
#     address = pyperclip.paste() #to paste from clipboard
# #https://www.google.com/
# webbrowser.open('https://www.google.com/maps/place/'+ address)
#
# ------------------------------FILE = mapit.bat-----------location of file = C:\users\devesh\-----
#
# @py.exe C:\Users\DEVESH\mapit.py  %*

# open cmd line :  windows + R and type : mapit <address>  , then ENTER
#
##############
