import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
html = requests.get(url, headers=headers).text
with open('zhihu_explore_html.txt', 'w', encoding='utf-8') as f:
    f.write(html)
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
top_recommend = doc('.top-recommend-feed .feed-item')
top_qustion = top_recommend.find('h2').text()
top_author = top_recommend.find('.author-link a').text()
print(top_author)
print(top_qustion)
#top_content = pq(top_recommend.find('.content').html()).text()
# with open('top_recommend.txt', 'a', encoding='utf-8') as file:
#     file.write('\n'.join([top_qustion, top_author,top_content]))
#     file.write(('=' * 50).join(['\n'] * 2))


for item in items:
    question = item.find('h2').text()  # get question
    author = item.find('.author-link-line a').text()  # get athor name
    answer = pq(item.find('.content').html()).text()

    with open('explore.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join([question, 'Author : '+author, answer]))
        f.write(('=' * 50).join(['\n'] * 2))
