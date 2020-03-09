## Takes email address of receiver and email content
## Automatically sends email and closes
## Make sure to replace emailAddress/password variables
## With the email/password necessary to log in
## Designed to be used with Protonmail

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time, sys

# Replace emailAddress/password with login info
emailAddress = '....@....'
password = '.......'

if len(sys.argv) > 1:
    emailTo = sys.argv[1]
    
    if len(sys.argv) > 2:
        emailContent = ' '.join(sys.argv[2:])  
    else:
        emailContent = sys.argv[2]

    browser = webdriver.Firefox()
    browser.get('https://protonmail.com/')

    linkElem = browser.find_element_by_xpath("//*[contains(text(), 'LOG IN')]")
    linkElem.click()

    usernameTest = browser.find_element_by_id('username')
    usernameTest.send_keys(emailAddress)

    passElem = browser.find_element_by_id('password')
    passElem.send_keys(password)
    passElem.submit()

    try:
        WebDriverWait(browser, 10).until(EC.title_contains('Inbox'))
        testElem = browser.find_element_by_css_selector('.compose')
        testElem.click()
        # print(browser.title)
        time.sleep(1)

        recAddress = ActionChains(browser)
        recAddress.send_keys(emailTo)
        recAddress.send_keys(Keys.ENTER)
        recAddress.send_keys(Keys.TAB)
        recAddress.send_keys('Still testing 123')
        recAddress.send_keys(Keys.TAB)
        recAddress.pause(1)
        recAddress.send_keys(emailContent)
        recAddress.perform()
        
    except TimeoutError:
        print('Time ran out!!!')

submitEmail = browser.find_element_by_css_selector('button.mobileFull:nth-child(4)')
submitEmail.click()
browser.quit()