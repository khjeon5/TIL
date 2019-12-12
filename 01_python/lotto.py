import requests
import random
from bs4 import BeautifulSoup
from datetime import datetime


#888회 로또번호 가져오기 
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=888'
response = requests.get(url)
lotto = response.json()
print(lotto)

#그 중에서 당첨번호 6개만 가져오기 
answer = []
for num in range(1,7):
    answer.append(lotto[f'drwtNo{num}'])
print(answer)

#랜덤으로 로또번호 생성하기 
num_list = [i for i in range(1,46)]
random_num = random.sample(num_list,6)
print(random_num)


#당첨번호와 랜덤번호 일치하는 정도에 따른 등수 표기하기 
count = 0
for i in answer:
    if i in random_num:
        count+=1
print(count)