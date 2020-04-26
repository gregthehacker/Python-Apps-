from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

url= 'https://wvv.filmgratuit.net/'

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

sleep(2)
# Get the list on the left
lists=driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[1]/div/div/div[1]/ul/li");
print(len(lists))
# list=lists[1]
# anchor=list.find_element_by_tag_name('a')
# print(anchor.get_attribute("href"));
links=[]
for list in lists:
    anchor= list.find_element_by_tag_name('a');
    link=anchor.get_attribute("href");
    links.append(link)
    
print(links)
