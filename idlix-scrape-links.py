from bs4 import BeautifulSoup
import requests


root = 'https://vip.idlixofficial.net/'
result = requests.get(root)
content = result.text


soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())


# get the wrapper div
wrapper = soup.find_all('div', class_='data dfeatur')

# list of links
links = []

# loop through the div movie wrapper
for element in wrapper:
    # get the <a href /> link inside the wrapper div
    link = element.find('a', href=True)

    # append list into links variabel
    links.append(link['href'])
  
# loop through link
for link in links:
    # send request to all links list, to get element that contains movie
    result_detail = requests.get(link)
    detail_content = result_detail.text

    soup = BeautifulSoup(detail_content, 'lxml')

    # get the div wrapper that contains useful movie info
    data_wrapper = soup.find('div', class_='data')

    # get movie title 
    title = data_wrapper.find('h1').get_text()

    # get movie date
    date = data_wrapper.find('span', class_="date").get_text()

    # get movie rating
    rating = data_wrapper.find("span", class_="dt_rating_vgs").get_text()

    # create new file with the name that based on movie title
    new_file = open(f"movie-list/{title}.txt", 'w',  encoding='utf-8')

    nl = '\n'

    new_file.write(f"name: f{title}{nl}date: {date}{nl}rating: {rating}")

    new_file.close()




