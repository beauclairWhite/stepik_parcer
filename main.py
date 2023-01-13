import requests
from bs4 import BeautifulSoup

sum = 0

for i in range(1, 6):
  url = f'https://parsinger.ru/html/index{i}_page_1.html'
  response = requests.get(url=url)
  soup = BeautifulSoup(response.text, 'lxml')
  card_url = soup.find('a', class_='name_item')
  card_url = card_url['href']

  temp_list = []
  for c in card_url:
    if c == '_':
      break
    temp_list.append(c)

  new_card_url = ''.join(temp_list)
  
  for j in range(1, 33):
    url = f'https://parsinger.ru/html/{new_card_url}_{j}.html'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    a, b = 0, 0
    
    a = soup.find('span', id='price').text
    a = ''.join(c for c in a if c.isdigit())
    a = int(a)

    b = soup.find('span', id='in_stock').text
    b = ''.join(c for c in b if c.isdigit())
    b = int(b)

    sum+= a*b
    print(f'{i} {j} done')

print(sum)