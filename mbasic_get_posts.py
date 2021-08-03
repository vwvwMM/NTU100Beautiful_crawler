import requests
from bs4 import BeautifulSoup

# (not very important) these data provide web server with our device information. (though some website may check this part)
USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

CRAWL_URL = 'https://mbasic.facebook.com/NTU100Beauty/'

session = requests.Session()
session.headers = {'user-agent' : USER_AGENT}

req = session.get(CRAWL_URL)

soup = BeautifulSoup(req.text, 'html.parser')

body = soup.find_all('div',id='timelineBody')[0]

recentPost=body.find_all('div',id="recent")[0]

posts=recentPost.find_all('div',{'data-ft':'{"tn":"*s"}'})

for post in posts:
    postText=post.find_all('p')[-1]
    print(postText.text)

# for recentpost in recentPost:
#     post=recentPost.find('div',class_="fd")
#     postText=post.find_all('p')[-1]
#     print(postText.text)



