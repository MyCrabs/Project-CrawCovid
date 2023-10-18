from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options #To keep browser longer

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options= chrome_options)
driver.get("https://www.linkedin.com/home") 
sleep(2)

credential = open('login_credential.txt')
line = credential.readlines()

#Login_into_Linkedin
username = line[0]
password = line[1]
email_fied = driver.find_element(By.ID,'session_key')
email_fied.send_keys(username)
sleep(3)
password_fied = driver.find_element(By.ID,'session_password')
password_fied.send_keys(password)
Keys.RETURN
sleep(2)
#login_button = driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
#login_button.click()
#sleep(3)

search_field = driver.find_element(By.XPATH,'/html/body/div[5]/header/div/div/div/div[1]/input')
search_contain = line[2]
search_field.send_keys(line[2])
#search_contain = input('What information do tou want to find?')
#search_field.send_keys(search_contain)
search_field.send_keys(Keys.RETURN)# button Enter
print('Search successfully')
sleep(2)






