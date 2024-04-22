from bs4 import BeautifulSoup
import requests


page_one = 'https://vip.idlixofficial.net/trending/?get=tv'
result = requests.get(page_one)
content = result.text

soup = BeautifulSoup(content, 'lxml')

# get the wrapper div for pagination
wrapper = soup.find('div', class_="pagination")

# get lists of <a /> page link
link_lists = wrapper.find_all('a')

page_list = []

# loop through link lists but only get the first and second link 
for index in range(2):
    page_list.append(link_lists[index]['href'])

for index, request_link in enumerate(page_list):
    # create new request
    result_page = requests.get(request_link)
    content_page = result_page.text

    soup = BeautifulSoup(content_page, 'lxml')

    # movie content wrapper
    wrapper_content = soup.find_all('article', class_='item tvshows')

     # create new file with that name based on page number
    new_file = open(f"trending-series-list/page-{index + 1}.txt", 'w',  encoding='utf-8')

    nl = '\n'

    # looping through all wrapper_content
    for data_content in wrapper_content:
        # image element
        image_element =  data_content.find('img')

        # movie date and title wrapper
        data_wrapper =  data_content.find('div', class_="data")

        # image link
        movie_image_link = image_element['src']

        # title
        movie_title = data_wrapper.find('h3').get_text()

        # date
        movie_date = data_wrapper.find('span').get_text()

        # write all movie list into file
        new_file.write(f"name: {movie_title}{nl}date: {movie_date}{nl}Image link:{movie_image_link}{nl}{nl}")
    
    new_file.close()


    
       







