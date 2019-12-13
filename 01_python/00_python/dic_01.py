#dictionart 만드는 방법
#1. 
my_dict = {'한국어':'안녕', '영어':'hi', '독일어':'Geten tag'}

#2.
my_dict2 = {}
my_dict2['한국어']='안녕'
my_dict2['영어']='hi'
my_dict2['독일어']='Genten tag'

#3.
my_dict3 = dict(한국어='안녕', 영어='hi', 독일어='Geten tag')

# print(my_dict)
# print(my_dict2)
# print(my_dict3)


area_code = {'서울':'02'}
area_code['경기도']='031'
# print(area_code)


# for key in area_code:
#     print(key)
#     print(area_code[key])

# for key,value in area_code.items():
#     print(key,value)


# for value in area_code.values():
#     print(value)



'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

hap=0
for value in score.values():
    hap+=value

avg = hap / len(score)
print(avg)


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 84,
        '국어': 90,
        '음악': 92
    },
    'b': {
        '수학': 83,
        '국어': 91,
        '음악': 77
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
avg =[]
for value in scores.values():
    hap = 0
    for value2 in value.values():
        hap += value2
    avg.append(hap/len(value))
average = sum(avg)/len(avg)
print(round(average,1))


print('==== Q3 ====')
# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

for key, value in city.items():
    temps = 0
    for t in value:
        temps += t
    temp = temps / len(value)
    print(f'{key}:{round(temp,2)}')

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
print('==== Q3-1 ====')
count = 0
for key, value in city.items():
    if count==0:
        hot_temp = max(value)
        cold_temp = min(value)
        hot_city = key
        cold_city = key
        count += 1
    else:
        if max(value)>hot_temp:
            hot_temp = max(value)
            hot_city = key
        if min(value)<cold_temp:
            cold_temp = min(value)
            cold_city = key
print(f'가장 더웠 던 도시는  {hot_city}:{hot_temp}')
print(f'가장 추웠 던 도시는  {cold_city}:{cold_temp}')

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
print('==== Q3-2 ====')

if 2 in city['서울']:
    print('2도 였던 적이 있습니다.')
else:
    print('2도 였던 적이 없습니다.')


# 아래에 코드를 작성해 주세요.



