**Objective**
  
Web scraping - retrieve data from different targeted websites to a centralized location
(obituary notices - historical data) --- write a script to retrieve data

**Web Scraping with Python + Beautiful Soup library**    

**1-	Australian - https://www.elanka.com.au/obituaries/**    

Time:  around 1 minute

![image](https://github.com/user-attachments/assets/e589b199-0961-4b9e-a0c4-e0cab9ebb4a0)

**2 - Canada (Times of Lanka) - https://reserved767.rssing.com/chan-65241722/all_p1.html**   

Time:  around 20 seconds

 ![image](https://github.com/user-attachments/assets/0a734d16-9369-4a5e-9c9a-c5de890f8821)

**3 - LK (Sunday Times) - https://www.sundayobserver.lk/category/obituaries/**

Time:  around 35 seconds

 ![image](https://github.com/user-attachments/assets/b41f1955-07e7-45b7-ab2f-358a15162555)

**4 - LK (Daily News Archive) - https://www.dailynews.lk/2024/10/21/obituaries/657697/obituaries-332/**

Time:  around 10 seconds

 ![image](https://github.com/user-attachments/assets/eda9507a-9c7b-4325-81e8-2a8fdc25b61a)

**Advantages** <br><br>
**1.	Easy to Learn and Use** <br>
It requires minimal code to extract elements from an HTML page using CSS selectors, tags, classes, and IDs. <br>
 <br>**2.	Flexible HTML Parsing** <br>
It can handle poorly structured or "broken" HTML pages and convert them into a navigable parse tree, making it robust for web scraping tasks involving unpredictable page structures. <br>
 <br>**3.	Integration with Other Libraries** <br>
Beautiful Soup can be combined with other libraries like requests (for fetching web content) and pandas (for data manipulation), providing a powerful data extraction and processing workflow. <br>
 <br>**4.	Efficient for Static Pages** <br>
Ideal for extracting data from static web pages where content doesn’t change dynamically after initial loading, avoiding the overhead of dealing with JavaScript-heavy content. <br>
 <br>**5.	Open Source and Community Support** <br>
Beautiful Soup is free, open-source, and has a strong community of users and contributors who provide extensive documentation, examples, and support. <br><br>

**Disadvantages**  <br><br>
**1.	Limited Handling of JavaScript Content** <br>
Beautiful Soup does not support JavaScript execution, making it ineffective for scraping dynamically loaded content (e.g., pages that use AJAX calls). This may require using tools like Selenium, Playwright, or Scrapy for JavaScript-heavy sites. <br>
 <br>**2.	Slower Performance for Large-scale Scraping** <br>
Beautiful Soup is slower compared to more advanced libraries like lxml or frameworks like Scrapy when handling large datasets or performing concurrent scraping tasks. <br>
It works best for small to medium-sized tasks but may not scale as effectively as more comprehensive solutions. <br>
 <br>**3.	Requires Additional Libraries for HTTP Requests** <br>
Beautiful Soup is purely an HTML/XML parsing library and does not handle HTTP requests directly. You'll need to use requests or similar libraries to fetch content from the web. <br>
 <br>**4.	Potential for Website Blocking** <br>
Like all web scraping methods, frequent or large-scale scraping attempts can result in being blocked by websites that detect and prevent automated access, requiring careful rate-limiting, user-agent rotation, and respect for robots.txt directives. <br>
 <br>**5.	Manual Handling of Complex Structures** <br>
While Beautiful Soup makes HTML parsing easier, complex web pages with nested structures may require detailed manual handling and inspection of the DOM, which can be time-consuming. <br>
 <br>**6.	Compliance and Legal Risks** <br>
Web scraping using Beautiful Soup does not inherently comply with website terms of service or legal regulations (e.g., terms prohibiting scraping). Careful attention is needed to ensure ethical and lawful scraping practices. <br>
