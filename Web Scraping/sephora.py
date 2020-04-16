from selenium import webdriver
from time import sleep, strftime
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
from email.message import EmailMessage
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
chromedriver_path= 'C:\Program Files/chromedriver.exe'
driver= webdriver.Chrome(executable_path = chromedriver_path)

link= 'https://www.sephora.com/ca/en/shop/makeup-cosmetics'
driver.get(link)
driver.find_element_by_link_text("Just Arrived").click()

sleep(3)

SLEEP_TIME = 5
last_height=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(SLEEP_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
products=driver.find_elements_by_class_name('css-79elbk')
#product1= products[0]

all_products= []
for product in products:
        description=product.find_element_by_class_name('css-pelz90').text
        name=product.find_element_by_class_name('css-ktoumz').text    
        price= product.find_element_by_class_name('css-0').text
        product_info= {
            "Name": name, 
            "Price": price,
            "Description": description
        }
        
        all_products.append(product_info)
data=pd.DataFrame(all_products)
print(data)
data.to_excel('/Users/Ahmed/Desktop/Python Apps/Web Scraping/just_arrived_sephora.xlsx')
me= 'marwa.hegy@hotmail.com'
to = 'marwa.hegy@gmail.com'
password= 'sweetishmarwa_98'
excel_file = '/Users/Ahmed/Desktop/Python Apps/Web Scraping/just_arrived_sephora.xlsx'

msg= MIMEMultipart()
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('just_arrived_sephora.xlsx', 'rb').read())

encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="just_arrived_sephora.xlsx"')
msg.attach(part)
msg['Subject']= 'Sephora Just Arrived Scraper Bot, {} new products in store'.format(len(data))
# msg.set_content("{} new products arrvied in Sephora stores, see file attachment".format(len(data)))
msg["Date"]= formatdate(localtime=True)
msg["To"]='marwa.hegy@gmail.com'
msg["From"]= me
server= smtplib.SMTP('smtp.outlook.com', 587)
server.ehlo()
server.starttls()
server.login(me, password)

server.sendmail('marwa.hegy@hotmail.com', 'marwa.hegy@gmail.com',msg.as_string())
