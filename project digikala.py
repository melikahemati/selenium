#pip install selenium
import selenium
from selenium import webdriver
import time
mororgar=webdriver.Firefox()
mororgar.get('https://www.digikala.com/users/login/?backUrl=/')
shomareh='09367870938'
inputtext=mororgar.find_element(by='name',value='username')
inputtext.send_keys(shomareh)
buttonvorod=mororgar.find_element(by='xpath',value='/html/body/div[1]/main/div[2]/form/button')
buttonvorod.click()
codetaaeed=input('input the code')
inputsms=mororgar.find_element(by='xpath',value='/html/body/div[1]/main/div[2]/form/label/div/div/input')
inputsms.send_keys(codetaaeed)
time.sleep(5)
mororgar.get('https://www.digikala.com/profile/')
txtshomareh=mororgar.find_element(by='xpath',value='//*[@id="profileLayoutContainer"]/div/div[2]/div[1]/div[1]/div/div[2]/p[2]')
shomarehakhar=txtshomareh.text
if int(shomarehakhar)==int(shomareh):
    print('the test is successful for ',shomareh)
else:
     print('test was not good')
