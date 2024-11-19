import requests
from bs4 import BeautifulSoup
import pandas as pd

for i in range(1,17):
    url =f"https://www.elanka.com.au/obituaries/page/{i}"

    response = requests.get(url)

    response = response.content

    soup = BeautifulSoup(response, 'html.parser')

    obituaries = soup.find_all('h2', class_='pld-post-title')

    for obituary in obituaries:
        info = obituary.a.text
        
        print(f'obituary : {info}')
        
        # Create DataFrame
        df = pd.DataFrame(info)

# Save DataFrame to CSV
df.to_csv('output.csv', index=False)