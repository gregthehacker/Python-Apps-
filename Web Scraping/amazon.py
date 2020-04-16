from selenium import webdriver
from time import sleep
chromedriver_path= 'C:\Program Files/chromedriver.exe'
driver= webdriver.Chrome(executable_path = chromedriver_path)

link= 'https://www.aliexpress.com/'
driver.get(link)
sleep(4)
driver.find_element_by_class_name('close-layer').click()
sleep(3)
driver.find_element_by_class_name('venue-festival-title').click()
sleep(1)
driver.find_element_by_link_text('Automobiles & Motorcycles').click()
sleep(4)
# try: 
driver.find_element_by_css_selector('a.next-dialog-close').click()
#     print("found pop up and closed it")
# except:
#     print("element not found")
sleep(1)
product_list=driver.find_elements_by_class_name('list-item')
product=product_list[0]

    
print(len(product_list))   
# print(product.find_element_by_class_name('item-title').get_attribute("text"))
# print(product.find_element_by_class_name('store-name').text)
# print(product.find_element_by_class_name('price-current').text)
# print(product.find_element_by_class_name('price-discount').text)
# print(product.find_element_by_class_name('shipping-value').text)
# print(product.find_element_by_class_name('rating-value').text)
# print(product.find_element_by_class_name('sale-value-link').text)
products= [] 
for product in product_list:
    sleep(1)
    title=product.find_element_by_class_name('item-title').get_attribute("text")
    store= product.find_element_by_class_name('store-name').text
    current_price=product.find_element_by_class_name('price-current').text
    discount=product.find_element_by_class_name('price-discount').text
    shipping_cost=product.find_element_by_class_name('shipping-value').text
    rating=product.find_element_by_class_name('rating-value').text
    quantity=product.find_element_by_class_name('sale-value-link').text
    product_item= {
            "Title": title,
            "Store_Name": store,
            "Current_Price": current_price,
            "Discount": discount,
            "Shipping_Cost": shipping_cost,
            "Rating": rating,
            "Quantity": quantity 
        }
        
    products.append(product_item)
    print(product_list)
 