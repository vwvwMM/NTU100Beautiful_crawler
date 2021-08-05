from bs4 import BeautifulSoup
import requests
import time


BASE_URL = 'https://mbasic.facebook.com/'
LOGIN_URL = 'https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8'
USERNAME = 'ttttrickortreat@gmail.com'
PASSWORD = 'Eric0620eric'

posts_to_scrape = 5

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
session = requests.Session()


def LOGGER(username, password):
    req = session.get(BASE_URL)
    soup = BeautifulSoup(req.text, 'html.parser')
    '''
    refs = soup.find_all('a')
    ref = refs[-1]['href']
    req = session.get(ref)
    print(ref)
    '''
    # login
    soup = BeautifulSoup(req.text, 'html.parser')
    LSD = soup.find('input', {'name': 'lsd'})['value']
    JAZO = soup.find('input', {'name': 'jazoest'})['value']
    MTS = soup.find('input', {'name': 'm_ts'})['value']
    LI = soup.find('input', {'name': 'li'})['value']
    form_data = {
        'lsd': LSD,
        'jazoest': JAZO,
        'm_ts': MTS,
        'li': LI,
        'try_number': 0,
        'unrecognized_tries': 0,
        'email': username,
        'pass': password
    }
    resp = session.post(LOGIN_URL, data=form_data)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup
# loged in
# access


def post_scraper(search_url, query_params):

    resp = session.get(search_url, params=query_params)
    soup = BeautifulSoup(resp.text, 'html.parser')
    IMFS = {'pictures':[]}
    if soup.find('h3'):
        IMFS['description'] = soup.find('div', {'id': 'objects_container'}).find_all('a')[
            1].parent.next_sibling.text
    else:
        print('this post is deleted')
        return None
    # use second pic because sometimes the first links to other posts
    img_url = soup.paragraph = soup.find('div', {'id': 'objects_container'}).find_all(
        'a')[1].parent.parent.parent.parent.next_sibling.find_all('a')[1]['href']
    resp = session.get(BASE_URL+img_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    while True:
        if not soup.find_all('img')[1]['src'] in IMFS['pictures']:
            IMFS['pictures'].append(soup.find_all('img')[1]['src'])
            #
            img_url = soup.find_all(
                'img')[1].parent.parent.next_sibling.find_all('a')[1]['href']
            resp = session.get(BASE_URL+img_url)
            soup = BeautifulSoup(resp.text, 'html.parser')
        else:
            print('all found')
            break
        if len(IMFS['pictures']) > 10:
            break
    return IMFS


def full_auto():
    ALL_DATA = {}
    soup = LOGGER(USERNAME, PASSWORD)
    JAZO = soup.find('input', {'name': 'jazoest'})['value']
    FBDTSG = soup.find('input', {'name': 'fb_dtsg'})['value']
    FLOW = soup.find('input', {'name': 'flow'})['value']
    NUXSOURCE = soup.find('input', {'name': 'nux_source'})['value']
    form_data = {
        'fb_dtsg': FBDTSG,
        'jazoest': JAZO,
        'flow': FLOW,
        'nux_source': NUXSOURCE
    }
    session.headers.update({'authority': 'mbasic.facebook.com'})
    resp = session.post(LOGIN_URL, data=form_data)
    soup = BeautifulSoup(resp.text, 'html.parser')
    st = soup.find('a')['href']
    num = 0
    if str.split('refid')[-1]:
        num = st.split('refid=')[-1]

    STRING = '台大百大正妹'
    STRING = str(STRING.encode('utf-8'))[2:-1]
    # search
    # the range of searching posts
    for i in range(1, posts_to_scrape):
        NUMBER = str(i)
        STRING = STRING.replace('\\x', '%')
        SEARCH_URL = 'https://mbasic.facebook.com/hashtag/'+'台大百大正妹ntu100beauty'+NUMBER
        PARAMS = {
            'refid': num,
            'query': ('#'+STRING+NUMBER)
        }
        ALL_DATA['beauty'+str(i)] = post_scraper(search_url=SEARCH_URL, query_params=PARAMS)
        session.get(BASE_URL)
    time.sleep(0.5)
    return ALL_DATA


if __name__ == '__main__':
    ALL_DATA = full_auto()
    print(ALL_DATA)


'''
PARAMS = {
    'refid': num,
    'query': '巫竑儒'
}
session.headers.update({'referer': BASE_URL})
resp = session.get(
    'https://mbasic.facebook.com/search/top/?q=%E5%B7%AB%E7%AB%91%E5%84%92&refid={}&_rdr', params=PARAMS)
soup = BeautifulSoup(resp.text, 'html.parser')
PROFILE = soup.find('div', {'id': 'BrowseResultsContainer'}).find_all('a')[
    0]['href']
resp = session.get(BASE_URL+PROFILE)
soup = BeautifulSoup(resp.text, 'html.parser')

resp = session.get('https://mbasic.facebook.com/reactions/picker/?ft_id=1098809383962859&origin_uri=https%3A%2F%2Fmbasic.facebook.com%2Fprofile.php%3Fid%3D100015014234107%26refid%3D46%26__xts__%255B0%255D%3D12.Abq5ICqZ2cYuvNSa7wIw3iwhghzAKVH51lCRvTnOn9ed1NVgMdyrpB_sDzx2cYUY3yRrqPqlhRHiO3u1UWk-Lam07wq0dA8nb-b9266sS_N8CrIl6kflw-368zmhT6vBfpsEqiq1TDMHzEO7w37DuylzybHwpL7Iclw6IXbGFaJkWUNPlsRX_n7JFyHP8CoutBloQWD-kAMh1FQ75YrZrbuw03ketzzSjdlr5rhLsIMgwC6Ufw0Shtzrdlw9hbK1-HJm3jXRNdBPFd5Il2N3nezxZvzhEfbUFuPLMMO2ijAlgrzj_X3f0S_SroCv7cNp7nK-l3MeNDcY_hHdd4EuKKE9AF_tg1qGUzg_TEv5darmmNb3nbFV6Qtk3IO9EqIG6roo1ICHrmGSGISio0cJI6F7_F3uJ1HBRBZcbsDDKJNzS4c38XBxfGjAPnPnBNJFB8n-WkLpPWsvODmOzLa26eufOilnCnjPKRPqa7o-7tAIZAC0GsY3kLdec7sGvq6U6Vx8uvesPyz4lwanwviv_Rgsz8sy04uQsYNNSsxlq9-NuNJYcM3_zhbqi5Bv7xT60CU%26fbt_id%3D1098809383962859%26lul&_ft_=mf_story_key.1098809383962859%3Atop_level_post_id.1098809383962859%3Atl_objid.1098809383962859%3Acontent_owner_id_new.100015014234107%3Athrowback_story_fbid.1098809383962859%3Apage_id.1747372898921603%3Aphoto_attachments_list.%5B1098803530630111%2C1098807870629677%2C1098808580629606%5D%3Astory_location.4%3Astory_attachment_style.album%3Atds_flgs.3%3Aott.AX9uAnNvq21ueBPQ%3Athid.100015014234107%3A306061129499414%3A2%3A0%3A1630479599%3A1777496805958400870&av=100007401426788&refid=17&__tn__=%2AW-R')
print(resp.text)
# name = '巫竑儒'
# print(name.encode('utf-8'))
'''
