from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plus_url = input('검색어를입력하세요.')
url = base_url + quote_plus(plus_url)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_img')

num = 1
for i in img:
   img_url = i['data-source']
   with urlopen(img_url) as f:
        with open('./img/' + plus_url + str(num) + '.jpg', 'wb') as h:
             img = f.read()
             h.write(img)
   num += 1
   
print('다운로드 완료')

#안녕하세요 + 바이바이