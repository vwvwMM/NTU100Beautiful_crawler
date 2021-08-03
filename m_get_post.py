import requests
from bs4 import BeautifulSoup

# (not very important) these data provide web server with our device information. (though some website may check this part)
USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

CRAWL_URL = 'https://m.facebook.com/page_content_list_view/more/?page_id=101006785453798&start_cursor=6&num_to_fetch=4&surface_type=timeline'

session = requests.Session()
session.headers = {'user-agent' : USER_AGENT}

req = session.get(CRAWL_URL)

soup = BeautifulSoup(req.text, 'html.parser')

print(soup.prettify())



