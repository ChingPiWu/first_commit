import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRFptTXpJU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"
response = requests.get(url)
print(response)
print(len(response.text))

soup = BeautifulSoup(response.text, "html.parser")

topic_elements = soup.find_all("div", class_="W8yrY")
print(len(topic_elements))

list_of_news = list()
for topic_id, topic_element in enumerate(topic_elements):
    new_titles = topic_element.find_all('a', class_="gPFEn")
    # for new_title in new_title:
    #     print(new_title.text)
    #     print(new_title.get('href'))

    # print()

    medias = topic_element.find_all("div", class_="vr1PYe")
    # for media in medias:
    #     print(media.text)
    # print()

    public_times = topic_element.find_all("time", class_="hvbAAd")
    # for public_time in public_times:
    #     print(public_time['datetime'])
    # print()

    for media, new_title, public_time in zip(medias, new_titles, public_times):
        # print(media.text)
        # print(new_title.text)
        # print(public_time['datetime'])
        # print()

        list_of_news.append(
            {
                "topic_id": topic_id,
                "media": media.text,
                "title": new_title.text,
                "url": 'https://news.google.com'+new_title['href'][1:],
                "public_time": public_time['datetime']
            }
        )
print(len(list_of_news))
df = pd.DataFrame(list_of_news)
df.to_csv("news.csv")
