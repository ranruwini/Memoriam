from bs4 import BeautifulSoup
import requests
import pandas as pd

for i in range(1,5):
    html_text = requests.get(f'https://reserved767.rssing.com/chan-65241722/all_p{i}.html').text

    soup = BeautifulSoup(html_text, 'lxml')
    
    data =[]
    
    Obituaries = soup.find_all('header', class_='cs-post-single-title')

    for obituary in Obituaries:
        published_datetime = obituary.find('span', class_='cs-post-meta-date').text
        obituary_date = obituary.find('h1').a.text

        print(f'''
        Obituary : {obituary_date}
        Published Date: {published_datetime}
        ''')
        
        data.append([published_datetime,obituary_date])
        
# Save DataFrame to CSV
df = pd.DataFrame(data, columns=['Obituary', 'Published Date'])
df.to_csv('website2_scraped_data.csv', index=False)
