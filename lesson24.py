from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"100"))

option1=browser.find_element_by_id("book")
option1.click()

x_element=browser.find_element_by_id("input_value")
x=x_element.text
y=calc(x)

option2=browser.find_element_by_id("answer")
option2.send_keys(y)

option3=browser.find_element_by_id("solve")
option3.click()

