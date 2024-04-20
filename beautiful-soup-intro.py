from bs4 import BeautifulSoup
import requests

website = 'https://vip.idlixofficial.net/'
result = requests.get(website)
content = result.text


soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())


# get the wrapper div
wrapper = soup.find_all('div', class_='data dfeatur')


# open a file
new_file = open("title.txt", "w",  encoding='utf-8')

for element in wrapper:
    # get the <h3> title inside the wrapper div
    title_text = element.find('h3').get_text()
    new_file.write(title_text + '\n')


new_file.close()



