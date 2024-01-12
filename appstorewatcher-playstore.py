#put chrome.exe path!!
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

#ChromeOptions options = new ChromeOptions();
options = Options()
options.add_argument('--headless')
options.add_argument("--disable-logging")
#options.add_argument("--disable-crash-reporter")
#options.add_argument("--disable-extensions")
#options.add_argument("--disable-in-process-stack-traces")
#options.add_argument("--disable-dev-shm-usage")
options.add_argument("--log-level=OFF")
options.binary_location = "[chrome.exe path]"

driver = webdriver.Chrome(options=options)
urls = ['https://play.google.com/store/apps/developer?id=Tesla,+Inc.','https://play.google.com/store/apps/developer?id=PayPal+Mobile']
print('===ANDROID_APPS===')
for url in urls:
	driver.get(url)

	#divs = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div/div[1]/c-wiz/c-wiz/c-wiz/section/div/div/div/div[1]/div/div/div/a/div[2]/div/div[1]/span') 
	#print(divs.text)

	divs = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div/div')
	#for div in divs:
	a = divs.text.split('\n')
	a.pop(0)
	
	for i in range(len(a)):
		if (i % 4) == 0: 
			print(a[i])
