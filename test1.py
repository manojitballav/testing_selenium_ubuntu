from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
 
# navigate to the application home page
driver.get("http://www.google.com")
# close the browser window

print "Done"

