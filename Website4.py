from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import pandas as pd

url = "https://www.dailynews.lk/2024/10/21/obituaries/657697/obituaries-332/"

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page()
    page.goto(url)
    
    data=[]
    
    try:
        # Optionally use a different load state or increase timeout
        page.wait_for_load_state('load', timeout=60000)  # Increased timeout
        page.wait_for_selector('.pcrlt-style-1', timeout=30000)  # Wait for content to appear

        content = page.content()
        soup = BeautifulSoup(content, 'html.parser')

        obituaries = soup.find_all('div', class_='item-related-inner')
        
        for obituary in obituaries:
            note = obituary.find('div', class_='related-content').h3.a.text
            date = obituary.find('div', class_='related-content').span.time.text
            
            print(f'''
                   Note: {note}
                   Date: {date}
                  ''')
            
            data.append([date,note])

    except Exception as e:
        print(f"Error: {e}")

    browser.close()

# Save DataFrame to CSV
df = pd.DataFrame(data, columns=['Date', 'Obituary Note'])
df.to_csv('website4_scraped_data.csv', index=False)
