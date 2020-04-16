from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path= 'C:\Program Files/chromedriver.exe'
driver= webdriver.Chrome(executable_path = chromedriver_path)


website = 'https://www.ca.kayak.com/flights/YUL-MNL/2020-08-21-flexible/2020-09-23?sort=bestflight_a'
driver.get(website)
# popup_xpath = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close")]'
# driver.find_elements_by_xpath(popup_xpath)[2].click()



element = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,'//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]' )))
print(len(element))
#button=element[9]
#driver.execute_script("arguments[0].click();", button)

# to load more pages, identify where the button is and add the click event to it

# def show_more_results():
#     try: 
#         show_more = '//a[@class="moreButton"]'
#         driver.find_element_by_xpath(show_more).click()
#         print('sleeping...')
#         sleep(randint(25,35))
#     except:
#         pass
    
# sleep(2)    
# show_more = '//a[@class="moreButton"]'
# driver.find_element_by_xpath(show_more).click()
