from selenium import webdriver
import getpass as gp 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
print("Facebook Login")
u=input("Enter Email/Phone")
p=gp.getpass("Enter the Password")  #For invisible password typing


driver = webdriver.Chrome('/home/logarithm/Downloads/chromedriver_linux64/chromedriver')    #Path for chrome driver
driver.get('https://www.facebook.com/')

username=driver.find_element_by_name('email')
password=driver.find_element_by_name('pass')
username.send_keys(u)
password.send_keys(p)


driver.find_element_by_id('loginbutton').click()   #Click Event on Login Button


print("Status Post")
post=input("Enter the status to post")
post=post + "\n" +"This Post is posted via a python script written by Rohan"


post_place=driver.find_element_by_css_selector('_1mf')

post_place.send_keys(post)

driver.find_element_by_name("_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft").click()  #Click Event on Share Button

print("Posted Sucessfully")
