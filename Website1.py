import requests
from bs4 import BeautifulSoup
import pandas as pd

for i in range(1,17):
    url =f"https://www.elanka.com.au/obituaries/page/{i}"

    response = requests.get(url)

    response = response.content

    soup = BeautifulSoup(response, 'html.parser')
    
    data =[]

    obituaries = soup.find_all('h2', class_='pld-post-title')

    for obituary in obituaries:
        info = obituary.a.text
        
        print(f'obituary : {info}')
        
        data.append([info])

# Save DataFrame to CSV
df = pd.DataFrame(data, columns=['Information'])
df.to_csv('website1_scraped_data.csv', index=False)
