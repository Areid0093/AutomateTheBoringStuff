from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://protonmail.com/')

linkElem = browser.find_element_by_xpath("//*[contains(text(), 'LOG IN')]")
linkElem.click()

usernameTest = browser.find_element_by_id('username')
usernameTest.send_keys('throwawaytester123@protonmail.com')

passElem = browser.find_element_by_id('password')
passElem.send_keys('tester123')
passElem.submit()

try:
    WebDriverWait(browser, 10).until(EC.title_contains('Inbox'))
    testElem = browser.find_element_by_css_selector('.compose')
    testElem.click()
    # print(browser.title)
    time.sleep(1)

    recAddress = ActionChains(browser)
    recAddress.send_keys('throwawaytester123@protonmail.com')
    recAddress.send_keys(Keys.ENTER)
    recAddress.send_keys(Keys.TAB)
    recAddress.send_keys('Still testing 123')
    recAddress.send_keys(Keys.TAB)
    
    # composerElem = ActionChains(browser)
    recAddress.send_keys('Is this working?')
    recAddress.perform()
    
    time.sleep(2)
except TimeoutError:
    print('Time ran out!!!')

# submitEmail = browser.find_element_by_css_selector('button.mobileFull:nth-child(4)')
# submitEmail.click()