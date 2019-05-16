#This code is for form which has ONLY radio buttons!
from selenium import webdriver
import random 

#because i am using firefor browser!!
driver = webdriver.Firefox()
driver.get("")

#xpath values got from inspecting elements
xpath_start=""
xpath_mid_1=""
xpath_mid_2=""
xpath_end=""

#if conditions tailored according to the form!
while(True):
    #this one is for teacher code 
    for i in range(1,14):
        if i==12 or i==14:
            #this one is for each row in teacher's part
            for j in range(2,6):
                elem=driver.find_element_by_xpath(xpath_start+str(i)+xpath_mid_1+str(j)+xpath_mid_2+str(random.randint(2,5))+xpath_end)
                elem.click()
        elif i==1 or i==13 or i%2==0:
            #this one is for each row in teacher's part
            for j in range(2,7):
                elem=driver.find_element_by_xpath(xpath_start+str(i)+xpath_mid_1+str(j)+xpath_mid_2+str(random.randint(2,5))+xpath_end)
                elem.click()
        else:
            #this one is for each row in teacher's part
            for j in range(2,6):
                elem=driver.find_element_by_xpath(xpath_start+str(i)+xpath_mid_1+str(j)+xpath_mid_2+str(random.randint(2,5))+xpath_end)
                elem.click()
    elem=driver.find_element_by_xpath("")
    elem.click()
    driver.back()
