from bs4 import BeautifulSoup
import requests

for i in range(1,5):
    html_text = requests.get(f'https://reserved767.rssing.com/chan-65241722/all_p{i}.html').text

    soup = BeautifulSoup(html_text, 'lxml')
    Obituaries = soup.find_all('header', class_='cs-post-single-title')

    for obituary in Obituaries:
        published_datetime = obituary.find('span', class_='cs-post-meta-date').text
        obituary_date = obituary.find('h1').a.text

        print(f'''
        Obituary : {obituary_date}
        Published Date: {published_datetime}
        ''')