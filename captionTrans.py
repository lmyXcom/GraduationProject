# 네이버 Papago NMT API 예제를 수정한 것

import os
import sys
import urllib.request
import csv

txtList = []

with open('파일명.csv', mode='r', encoding='utf-8') as f:  # 같은 폴더 내의 캡션 csv 파일로 대체
    reader = csv.reader(f)
    for row in reader:
        client_id = "네이버API_id"   # NAVER Developers에서 받은 Client ID 입력
        client_secret = "네이버API_secret"   # NAVER Developers에서 받은 Client Secret 입력
        encText = urllib.parse.quote(row[1])
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            finaltxt = response_body.decode('utf-8')
            korTrans = finaltxt.replace('{', '').replace('}', '').rsplit(':', 1)[-1].replace('"', '')
            txtList.append(korTrans)
        else:
            print("Error Code:" + rescode)
            
with open('result.csv', mode='w', newline='') as write_file:
    writer = csv.writer(write_file, delimiter=',')
    for txt in txtList:
        writer.writerow([txt])
