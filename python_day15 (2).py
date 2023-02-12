import requests
import bs4

url = 'https://kin.naver.com/'
response = requests.get(url)

bs = bs4.BeautifulSoup(response.text, 'html.parser')

ul = bs.select_one('ul.ranking_list')
ul2 = bs.select_one('#rankingChart > ul:nth-child(2)')

title = ul.select("li>a.ranking_title")
title2 = ul2.select("li>a.ranking_title")

t1 = title[:3] # 1등~3등
t2 = title2[:3] # 4~6
t3 = title[3:] # 7~9
t4 = title2[3:] # 10~
list = t1 + t2 + t3 + t4

for i, t in enumerate(list):
    print(f'{i+1}. {t.text}')


# 응용 예제 (p.326)
#1
url = 'https://movie.naver.com/movie/sdb/rank/rpeople.naver'
res = requests.get(url)

bs = bs4.BeautifulSoup(res.text, 'html.parser')

tbody = bs.select_one('tbody')
title = tbody.select('td.title > a')

movie_in = [i.text for i in title]
print(movie_in)


# 2
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
res = requests.get(url)

bs = bs4.BeautifulSoup(res.text, 'html.parser')

tbody = bs.select_one('tbody')
tit3 = tbody.select('div.tit3 > a')

movie = [i.text for i in tit3]
for i, m in enumerate(movie):
    print(f'{i+1}위: {m}')


# 3
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
res = requests.get(url)

bs = bs4.BeautifulSoup(res.text, 'html.parser')

tbody = bs.select_one('tbody')
title = tbody.select('tr')

for i in title:
    for j in i.select('td.ac'):
        img = j.find('img')
        if img is not None:
            if img['alt'] == 'up':
                print(i.select_one('div.tit3 > a').text)