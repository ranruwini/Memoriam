from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time
import pandas as pd

url = "https://www.sundayobserver.lk/category/obituaries/"

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page()
    page.goto(url)
    
    data =[]

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
    
# Save DataFrame to CSV
df = pd.DataFrame(data, columns=['Date', 'Obituary Note'])
df.to_csv('website3_scraped_data.csv', index=False)

