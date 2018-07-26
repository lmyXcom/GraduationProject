# 큰 이미지 데이터셋에서 소규모로 몇개만 뽑아오려고..

import pandas as pd
import os

dirFileslist = '파일명 있는 목록 csv파일의 경로면'
label = pd.read_csv(dirFileslist, skiprows=1, usecols=[1], names=['label'], encoding='utf-8', engine='python')
label_list = label.values.tolist()

# flatten list of list -> [[a], [b],..] 를 [a, b, ...]로 바꿈
import numpy as np
flat_label = np.array(label_list)
new_label = flat_label.flatten().tolist()

# 리스트의 중복 제거
def remove_duplicates(list):
    my_set = set()
    res=[]
    for e in list:
        if e not in my_set:
            res.append(e)
            my_set.add(e)
    return res
new_label = remove_duplicates(new_label)


# new_label의 숫자와 일치하는 파일명을 가진 이미지만 imgPath에서 찾아서 destDir 경로로 복사
import shutil
imgPath = '원래 이미지 파일 위치한 폴더의 경로'
destDir = '이름 일치하는 파일을 복사할 폴더의 경로'
for image in w:
    for num in new_label:
        num = str(num)
        print(num)
        imgPath2 = 'imgPath의 경로/%s.jpg' %num
        shutil.copy(imgPath2, destDir))
print('복사 완료')
