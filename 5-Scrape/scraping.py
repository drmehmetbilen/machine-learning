import requests
from bs4 import BeautifulSoup

import pandas as pd

base_url = "https://www.maku.edu.tr"
page_number_to_be_parsed = 10
base_news_url = "https://www.maku.edu.tr/tr/contents/47/{page_number}/-"
news_list = []

for page_number in range(1,page_number_to_be_parsed):
    
    page_address = base_news_url.replace("{page_number}",str(page_number))
    
    result = requests.get(page_address)
    soup = BeautifulSoup(result.text, "html.parser")

    news_raw = soup.select(".flex.flex-col.h-full.items-start")

    for news_i in news_raw:
        individual_news = news_i.select_one(".text-left.font-thin.text-maku_text-500")
        title = individual_news.text
        link = base_url+individual_news.get("href")
        
        individual_content = news_i.select_one(".flex.flex-1.text-sm.text-left.text-slate-400")
        content = individual_content.text
        
        parsed_news = {
            "title":title,
            "content":content,
            "link":link
        }
        news_list.append(parsed_news)


df = pd.DataFrame(news_list)
df.to_csv("data/maku_news.csv")
df.to_excel("data/maku_news.xlsx")