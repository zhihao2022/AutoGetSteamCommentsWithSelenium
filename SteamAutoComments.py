from selenium import webdriver
import time
from bs4 import BeautifulSoup

browser = webdriver.Firefox(executable_path='D:/WorkAPP/BrowserDrivers/geckodriver.exe')

browser.get('https://steamcommunity.com/app/1111460/reviews/?browsefilter=toprated&snr=1_5_100010_')

t1 = time.time()
while time.time() - t1 < 3600:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        btn = browser.find_element_by_id('GetMoreContentBtn')
        btn.click()
    except:
        continue

html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
reviews = soup.find_all('div', {'class': 'apphub_Card'})
cnt = 0
for review in reviews:
    nick = review.find('div', {'class': 'apphub_CardContentAuthorName'})
    title = review.find('div', {'class': 'title'}).text
    hour = review.find('div', {'class': 'hours'}).text.split(' ')[0]
    link = nick.find('a').attrs['href']
    comment = review.find('div', {'class': 'apphub_CardTextContent'}).text
    with open('test_2.txt', 'a+', encoding='utf-8') as f:
        f.write(nick.text + '  ')
        f.write(title + '  ')
        f.write(hour + '  ')
        f.write(link + '  ')
        f.write(comment + '  ')
        f.write('\n\n\n')
        cnt+=1
        print(cnt)

browser.close()
