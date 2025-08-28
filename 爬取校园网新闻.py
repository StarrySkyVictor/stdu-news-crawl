from lxml import etree  
import requests  
from bs4 import BeautifulSoup  
from concurrent.futures import ThreadPoolExecutor, as_completed  

def fetch_news_content(info):  
    url = f'https://xcbnew.stdu.edu.cn/news/{info}'  
    response = requests.get(url)  
    soup = BeautifulSoup(response.text, 'html.parser')  

    title = soup.find("h2", itemprop="headline").get_text(strip=True)  
    div_content = soup.find('div', itemprop='articleBody')  
    text_content = div_content.get_text(strip=True)  

    return title, text_content  

# 第一步：获取新闻列表  
url = 'https://www.stdu.edu.cn/'  
response = requests.get(url)  
html = etree.HTML(response.text)  

http = []  

# 获取新闻列表  
news_list = html.xpath('//*[@id="Mod217"]/div/div/div[2]/ul[2]/li')  
for news in news_list:  
    href = news.xpath('.//a/@href')[0]   
    info = href.split('/')[-1]  
    http.append(info)  

# 第二步：并行获取每条新闻的详细内容  

with ThreadPoolExecutor(max_workers=15) as executor:  # 可以根据你的网络条件调整线程数  
    future_to_info = {executor.submit(fetch_news_content, info): info for info in http}  
    for future in as_completed(future_to_info):  
        title, text_content = future.result()  
        print(f'标题: {title}\n')  
        print(f'正文:\n{text_content}\n')  
        print(f'共{len(text_content)}个字符')  
        print('-' * 135)  


print(f'共{len(http)}篇新闻。')

'''from lxml import etree
import requests

url = 'https://www.stdu.edu.cn/'
response = requests.get(url)
html = etree.HTML(response.text)

http = []

# 获取新闻列表
news_list = html.xpath('//*[@id="Mod217"]/div/div/div[2]/ul[2]/li')
for news in news_list:
     href = news.xpath('.//a/@href')[0] 
     info = href.split('/')[-1]
     http.append(info)
print(http)

from bs4 import BeautifulSoup
import requests

for info in http:
    url = f'https://xcbnew.stdu.edu.cn/news/{info}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find("h2",itemprop="headline").get_text(strip=True)
    div_content = soup.find('div',itemprop='articleBody')  
    text_content = div_content.get_text(strip=True)  
    print(f'标题:{title}\n')
    print(f'正文:\n{text_content}\n')  
    print(f'共{len(text_content)}个字符')
    print('-'*135)

print(f'共{len(http)}篇新闻。')'''