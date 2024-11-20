from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import pandas as pd
import requests
import time

data = []
for i in range(1,17):
    url1 =f"https://www.elanka.com.au/obituaries/page/{i}"
                                                                                
    response = requests.get(url1)

    response = response.content

    soup = BeautifulSoup(response, 'html.parser')
    
    obituaries = soup.find_all('h2', class_='pld-post-title')

    for obituary in obituaries:
        info = obituary.a.text
        
        print(f'obituary : {info}')
        
        data.append(['', info])
       
        
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
    
    
url3 = "https://www.sundayobserver.lk/category/obituaries/"

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page()
    page.goto(url3)
    
    # Loop to click "load more" button until no more content can be loaded
    while True:
        try:
            # Wait for the "load more" button to be visible
            load_more_button = page.query_selector('a.penci-ajax-more-button') 
            if load_more_button:
                load_more_button.click()
                time.sleep(2)  # Wait for new content to load
                
                # Extract page content
                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')

                # Extract obituaries
                obituaries = soup.find_all('li', class_='list-post pclist-layout')

                for ob in obituaries:
                    date = ob.find('time', class_="entry-date published").text if ob.find('time', class_="entry-date published") else "Date not found"
                    note = ob.find('div', class_='item-content entry-content').p.text if ob.find('div', class_='item-content entry-content') else "Note not found"

                    print(f'''
                    Published Date: {date}
                    Obituary Note: {note}
                    ''')
                    
                    data.append([date,note])
                    
            else:
                break  # Exit the loop if no "load more" button is found
        except Exception as e:
            print(f"No more 'load more' button found or error occurred: {e}")
            break

    browser.close()
    
url4 = "https://www.dailynews.lk/2024/10/21/obituaries/657697/obituaries-332/"

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page()
    page.goto(url4)
    
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
df = pd.DataFrame(data, columns=['Obituary', 'Published Date'])
df.to_csv('AllWebsites_scraped_data.csv', index=False)
        