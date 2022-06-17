from selenium import webdriver 
import os

link="https://suninjuly.github.io/file_input.html"
browser=webdriver.Chrome()
browser.get(link)

input_1=browser.find_element_by_name("firstname")
input_1.send_keys("Lionel")
input_2=browser.find_element_by_name("lastname")
input_2.send_keys("Messi")
input_3=browser.find_element_by_name("email")
input_3.send_keys("leomessi10@mail.ru")

current_dir=os.path.abspath(os.path.dirname(__file__))
file_path=os.path.join(current_dir,'l223.txt')
input_4=browser.find_element_by_id("file")
input_4.send_keys(file_path)

option=browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", option)
option.click()



