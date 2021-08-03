from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(
    'C:/Users/x2815/selenium/NTU100Beautiful_crawler/chromedriver', options=chrome_options)

driver.get("https://www.facebook.com/")
acc = driver.find_element_by_xpath(
    '//*[@id="email"]')
psw = driver.find_element_by_xpath('//*[@id="pass"]')
acc.send_keys('< youraccount >')
psw.send_keys('< yourpassword > ')


driver.find_element_by_class_name('_6ltg').click()
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "facebook")))
    driver.get('https://www.facebook.com/NTU100Beauty/photos/?ref=page_internal')
except Exception as e:
    print('exception:', e)

'''
SCROLL_PAUSE_TIME = 0.5
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)
html = driver.page_source
time.sleep(2)
tr = driver.find_elements(
    By.XPATH, '//div/img[@src]')

print('aaaaaaa')
for t in tr:
    print(t.get_attribute('src')
          )
'''
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "facebook")))
    driver.get('https://www.facebook.com/NTU100Beauty')
except Exception as e:
    print('exception:', e)
SCROLL_PAUSE_TIME = 0.5
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)
html = driver.page_source
time.sleep(2)
tr = driver.find_element(By.XPATH, '//div[@role="feed"]')
posts = tr.find_elements(By.XPATH, '//a[@aria-label]')
for post in posts:
    print(post.get_attribute('href'))

print('success')
