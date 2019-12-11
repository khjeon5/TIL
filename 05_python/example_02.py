import webbrowser
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# webbrowser.open("www.google.co.kr")
# webbrowser.open_new("www.naver.com")
# webbrowser.open_new_tab("www.github.co.kr")

# res = requests.get("http://www.naver.com")
# print(res.text)

url = "https://www.naver.com/"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
now = datetime.now()
search = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul> li .ah_k")
print(f'{now}')
for i, name in enumerate(search):
    print(f'{i+1}위 : {name.text}')

