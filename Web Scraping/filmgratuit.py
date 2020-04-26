from selenium import webdriver
from time import sleep
chromedriver_path= 'C:\Program Files/chromedriver.exe'
driver= webdriver.Chrome(executable_path = chromedriver_path)

link= 'https://wvv.filmgratuit.net/'
driver.get(link)
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