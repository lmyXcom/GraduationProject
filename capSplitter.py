# to divide captions into 2 files ( train set & val set + test set)
# Python 3.xx
# directory of img saved folder : foler_url
# cap file directory : csv_url
###########################################################################


import os
import csv

csv_url = 'D:/졸업작품/token_3000imgs.csv'

splits = ['train', 'val']
for split in splits:
    folder_url = 'C:/Users/Minyeong Lee/Downloads/sample_flickr30k/%s/' %split
    output_file = 'D:/졸업작품/token_3000imgs_%s.csv' %split
    with open(csv_url, 'r', newline='', encoding='utf-8') as csv_in_file:
        with open(output_file, 'w', newline='', encoding='utf-8') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            header = next(filereader)
            filewriter.writerow(header)
            for row_list in filereader:
                label = str(row_list[1]).split('.')[0]
                for root, dirs, files in os.walk(folder_url):
                    for fname in files:
                        imgname = fname.split('.')[0] #폴더 내 파일명
                        if imgname == label:
                            filewriter.writerow(row_list)
                        print('소작업 하나 마쳤습니다!')
print('모든 작업을 마쳤습니다.')