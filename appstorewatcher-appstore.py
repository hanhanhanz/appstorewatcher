#put chrome.exe path!!
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#ChromeOptions options = new ChromeOptions();

options = Options()
options.add_argument('--headless')
options.binary_location = "[chrome.exe path]"

driver = webdriver.Chrome(options=options)
urls = ['https://apps.apple.com/id/developer/tesla-inc/id582007916','https://apps.apple.com/id/developer/paypal-inc/id283646712']
a = []
print('===IOS_APPS===')
for url in urls:
	driver.get(url)
	time.sleep(2)	
	for i in range(1,20):
		try:
			#print(i)
			divs = driver.find_element(By.XPATH,'/html/body/div[3]/main/div[2]/section['+str(i)+']/div[2]')
			
			b = divs.text.split('\n')
			#print(a)
			for i in range(len(b)):
				a.append(b[i])
			
		except Exception as error:
			#print("An exception occurred:", error) # An exception occurred: division by zero
			continue
	#print('lol')
	
	for i in range(len(a)):
		if i % 2 == 0:
			print(a[i])
