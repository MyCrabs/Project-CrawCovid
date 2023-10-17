from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import datetime 
import os,time

print('-Finishing importing pakage')

#Step1 : LogIn To TopCV
driver = webdriver.Chrome()
url = 'https://covid19.gov.vn/'
time.sleep(10)
driver.get(url)

#email_field = driver.find_element_by_name('email')
#email_field.send_keys('thanhduy190903@gmail.com')

# password_field = driver.find_element_by_name('password')
# password_field.send_keys('01264636597Duyen')