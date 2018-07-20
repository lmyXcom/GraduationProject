# API 트래픽 초과시 이용할 임시 코드

rom selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://papago.naver.com"

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get(url)
html = urlopen(url).read()
soupData = BeautifulSoup(html, 'html.parser')

elem = driver.find_element_by_xpath('//*[@id="txtSource"]')
elem.send_keys("testing")

elem2 = driver.find_element_by_xpath('//*[@id="btnTranslate"]')
elem2.click()
''' 여기까지는 제대로 동작. 그러나 번역하기 버튼 누른 다음에 나오는 결과 텍스트가 파싱이 잘 안됨 '''

tList = soupData.select("##txtTarget > span")
print(tList)

driver.close()