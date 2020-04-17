#download geckodriver from https://github.com/mozilla/geckodriver/releases and paste the .exe in
#scripts folder of your python . e.g C:\Users\DEVESH\AppData\Local\Programs\Python\Python37\Scripts

from selenium import webdriver
try:

    browser = webdriver.Firefox() #to run this we need geckodriver in our system
except:
    print('Check for geckodriver in your system')
browser.get('http://automatetheboringstuff.com/')


#uncomment below if you want to search anything in broweser
# searchelement = browser.find_element_by_css_selector('.gLFyf')
# searchelement.send_keys('modi')
# searchelement.submit()

element = browser.find_element_by_css_selector('.main > div:nth-child(1) > blockquote:nth-child(5)')
print(element.text) #return a particular paragraph,  element.text converst html select to text at that point

element = browser.find_element_by_css_selector('html')  #prints everything of the page
print(element.text)
# browser.back()
# browser.back()
# browser.forward()
# browser.refresh()
#browser.quit()

# browser.get('https://www.google.com')
# element = browser.find_element_by_css_selector('.gLFyf')
# element.send_keys('shivesh')
# element.find_element_by_css_selector('.FPdoLc > center:nth-child(1) > input:nth-child(1)')
# element.click()  click() is used to click any link