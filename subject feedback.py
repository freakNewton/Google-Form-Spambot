from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random 

driver = webdriver.Firefox()
#file containing list of students
f=open('Class_List','r').readlines()
driver.get("------------your url----------")

#your form's xpath values
xpath_start=""
xpath_input_end=""
xpath_radio_mid=""
xpath_radio_end=""

while(True):
	line=random.choice(f)
	roll,name=line.split("\t")
	i=2;
	elem = driver.find_element_by_xpath(xpath_start+str(i)+xpath_input_end)
	elem.send_keys(name)
	i = i+1
	elem = driver.find_element_by_xpath(xpath_start+str(i)+xpath_input_end)
	elem.send_keys(roll)

	for j in range(4,10):
		elem=driver.find_element_by_xpath(xpath_start+str(j)+xpath_radio_mid+str(random.randint(1,3))+xpath_radio_end)
		elem.click()
	elem = driver.find_element_by_xpath("---------submit button---------")
	elem.click()
	elem = driver.find_element_by_xpath("---------another responce-------")
	elem.click()
