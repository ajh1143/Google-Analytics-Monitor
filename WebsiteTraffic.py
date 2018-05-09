from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import time

class GoogleAnalyticsTrafficMonitor(object):



    #Set Browser, add ability to switch/detect to other browser types
    #browser = webdriver.Firefox()
    browser = webdriver.Chrome()


    #Log In to Google Analytics
    login_address = input()   

    #Get
    browser.get(login_address)

    #Wait for response with sleep
    time.sleep(10)
    
    #Get Username and Password to log in
    username = input("Username")
    password = input("Password")

    #Locate login locations
    browser.find_element_by_id("")
    browser.find_element_by_id("")
    
    #Apply username/pass keys
    username.send_keys(username)
    password.send_keys(password)
    
    #Attempt Login
    login = browser.find_element_by_xpath("//*[@type='submit']")
    login.submit()
