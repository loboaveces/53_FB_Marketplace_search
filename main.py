from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

FB_EMAIL = 'ADD EMAIL'
FB_PASSWORD= 'ADD PASSWORD'
SEARCH = 'something you wanna search'

chrome_driver_path = '/home/lobo/PycharmProjects/chromedriver_linux64/chromedriver'
# driver = webdriver.Chrome(executable_path=chrome_driver_path)


# Hide notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.get("https://www.facebook.com/")

#login to the account - email
login_box = driver.find_element_by_xpath('//*[@id="email"]')
login_box.send_keys(FB_EMAIL)
time.sleep(1)
login_box.send_keys(Keys.TAB)

#login to the account - password
login_box = driver.find_element_by_xpath('//*[@id="pass"]')
login_box.send_keys(FB_PASSWORD)
time.sleep(1)
login_box.send_keys(Keys.ENTER)

# Wait until page loads
time.sleep(10)

# Open Marketplace and search some text
# Change the city, search something in Marketplace and format the url for your search
driver.get(f'https://www.facebook.com/marketplace/santacruzdelasierra/search/?query={SEARCH}')


