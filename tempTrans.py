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

'''
************ 시험용 코드 **************
import pandas as pd
from selenium import webdriver
import time
import progressbar
from selenium.common.exceptions import NoSuchElementException

def translation(sentence):

    papago_btn = driver.find_element_by_xpath('//*[@id="btnTranslate"]')
    papago_search = driver.find_element_by_xpath('//*[@id="txtSource"]')
    papago_search.send_keys(sentence)
    papago_btn.click()
    time.sleep(5)
    try:
        papago_result = driver.find_element_by_id('targetEditArea')
    except NoSuchElementException:
        return False
    result = papago_result.text
    papago_search.clear()

    return result

if __name__ == '__main__':
    en_path = 'C:/Users/Minyeong Lee/PycharmProjects/papago_trans/token_eng2.csv'
    driver_path = 'C:/chromedriver.exe'
    result_data = pd.read_csv(en_path, encoding = 'utf-8', error_bad_lines=False, names=['label', 'eng'])
    print(result_data.head(3))
    print(result_data.columns)
    # result_data = pd.read_csv(en_path, encoding = 'utf-8')

    translation_url = 'https://papago.naver.com/'  # papago
    driver = webdriver.Chrome(driver_path)
    pb = progressbar.ProgressBar()

    korea = []
    driver.get(translation_url)
    print('============================================')
    print(enumerate(result_data))
    # print(pb(enumerate(result_data)))
    print('=================반복 시작==================')
    for iteration, en in enumerate(result_data):
        print(iteration, en)
        korea.append(translation(en))
        if iteration % 1000 == 0:
            driver.refresh()
    ''' 오류나서 일단 지움
    for iteration, en in pb(enumerate(result_data)):
        korea.append(translation(en))
        num = num+1
        if num%1000 == 0:
            driver.refresh()
    '''

    print('translation end!')
    k = pd.Series(korea)
    print('list to series complete')
    result_data['k'] = k.values
    result_data.to_csv('token_kor.csv')
    print('all process clear')
'''
