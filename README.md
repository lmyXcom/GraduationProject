< 졸업작품을 위한 Repository >


[기간]

2018.07 ~ 2018.08


[Reference]

https://github.com/kelvinxu/arctic-captions

https://github.com/jazzsaxmafia/show_attend_and_tell.tensorflow

https://github.com/yunjey/show-attend-and-tell    -> PRIMARY SOURCE

https://wikidocs.net/book/536



[진행 상황]

Step 1. Flickr30k 데이터셋 출처: http://web.engr.illinois.edu/~bplumme2/Flickr30kEntities/

Step 2. 캡션 파일을 네이버 파파고 통해 번역

Step 3. 번역 오류 검수

Step 4. 일단 소규모 데이터셋만 추출

Step 4.5. 운영체제 Linux/Ubuntu + Python2.7 구축 - GCP의 VM 사용

Step 5. 모델링 진입

Step 5.5 오류 수정 -> 거의 완료...

=====================================================================================

Step 6 소규모 돌리고 -> 돌아가는지 확인되면 -> 전체 데이터 돌리면서 hyperparameter 수치 수정

Step 7 raw data 수집x (시간 부족)

Step 8 caption data 학습 처리 과정에서 한글 오류로 인한 지연

=====================================================================================

[ 한글 인코딩 관련 ]
- 주석 방법 해결 안됨
- sys(reload) setdefaultencoding 이것도 안됨
- utf-8, cp949, euc-kr, u"한글한글" 다 안됨
1. blog.naver.com/jmpark1115/221351400002
2. blog.naver.com/qkaqjaos/221132822855


=============json 파일부터 잘못된것을 발견. 인코딩 다 다시 따져가면서 
