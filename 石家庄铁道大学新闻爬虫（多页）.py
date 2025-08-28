from playwright.sync_api import sync_playwright
from lxml import etree  
import requests  
from bs4 import BeautifulSoup  
from concurrent.futures import ThreadPoolExecutor, as_completed  

with sync_playwright() as p:
    base_url = "https://xcbnew.stdu.edu.cn/news"
    hrefs = []

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(base_url, timeout=60000)

    for i in range(3):# 爬取的页面数（以3页为例）

        links = page.locator('td[headers="categorylist_header_title"].list-title a').all()
        href = [link.get_attribute("href") for link in links if link.get_attribute("href")]
        hrefs.extend(href)
        page.get_by_label("转到第 下一页 页").first.click()
    
    browser.close()

    print(hrefs)

def fetch_news_content(info):  
    url = f'https://xcbnew.stdu.edu.cn/{info}'  
    response = requests.get(url)  
    soup = BeautifulSoup(response.text, 'html.parser')  

    title = soup.find("h2", itemprop="headline").get_text(strip=True) 
    time = soup.find("time", itemprop="datePublished").get_text(strip=True) 
    div_content = soup.find('div', itemprop='articleBody')  
    text_content = div_content.get_text(strip=True)  

    return title, time, text_content  

with ThreadPoolExecutor(max_workers=20) as executor:  # 可以根据你的网络条件调整线程数  
    future_to_info = {executor.submit(fetch_news_content, info): info for info in hrefs}  
    for future in as_completed(future_to_info):  
        title, time, text_content = future.result()  
        print(f'标题: {title}\n')  
        print(f'{time}\n')  
        print(f'正文:\n{text_content[:20]}\n')  
        print(f'共{len(text_content)}个字符')  
        print('-' * 135)  


print(f'共{len(hrefs)}篇新闻。')

