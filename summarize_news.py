import pandas as pd
from openai_chatgpt import complete_chat

news = pd.read_csv('news.csv')
# print(news.head())

# Sol 1:依照每一行去處理
# records = news.to_dict(orient='records')
# for record in records[:5]:
#     print(record['title'])

# Sol 2:


def summarize_google_news():
    groups = news.groupby('topic_id')
    summarizations = list()
    for gid, group in groups:
        # print(list(group['title']), '\n')
        temp = list(group['title'])
        message = "\n".join(temp)
        # print(message, '\n')

        summarization = complete_chat(message)
        print("Summarization:", summarization, '\n')
        summarizations.append(summarization)
    return summarizations


if __name__ == '__main__':
    summarize_google_news()
