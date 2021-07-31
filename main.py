# Assignment - You need to write a Python application which will be run every hour, it will open some URL's in Linkedin and download 
# https://www.linkedin.com/in/strati-georgopoulos/detail/recent-activity/shares/
# Posts Images or Videos needs to be downloaded and the text with that.
# Now open your Linkedin account in chrome browser and your code should post the same image and text with your account.
# In a nutshell you are copy pasting other peoples post and posting with your id. 

# Technology to be used = Python + Selenium

# Note -  you can google and use any existing code from internet or github

# Tentative Timeline - 1 to 2 days. ideally it should be 1 day work.


from selenium import webdriver
import time
import requests
import bs4
from PIL import Image
import re

browser = webdriver.Chrome()

browser.get('https://www.linkedin.com/')

login = browser.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/div[2]/div[1]/input')
login.send_keys('')

password = browser.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/div[2]/div[2]/input')
password.send_keys('')

browser.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/button').click()

time.sleep(5)

try:
    browser.find_element_by_xpath('/html/body/div/div[1]/section/div[2]/div/article/footer/div/div/button').click()
except:
    pass
browser.get('https://www.linkedin.com/in/strati-georgopoulos/detail/recent-activity/shares/')
time.sleep(3)

cards = browser.find_elements_by_class_name("feed-shared-update-v2--minimal-padding")
headings = []
# reactions = []
pattern_head = "<span class='break-words'></span>"

for card in cards:
    card = card.get_attribute("innerHTML")   
    try:  # Append headings
        headings.append(re.search(pattern_head, card)[0])
    except:
        headings.append("None")
print(headings)
    # Append reactions
    # reactions.append(re.findall(pattern_reactions, card))

# imgs = browser.find_elements_by_tag_name('img')
# for i in imgs:
#     src = i.get_attribute('src')
#     print(src)

# div = browser.find_elements_by_class_name('ivm-image-view-model')
# for i in div:
#     img=i.find_element_by_tag_name('img')
#     print(img)

# text = browser.find_element_by_class_name('break-words')
# spn = text.get_attribute('span')
# print(spn)



# class="video-js media-player__player vjs-fluid vjs-1-1 media-player--use-mercado vjs-controls-enabled vjs-workinghover vjs-v7 vjs-layout-medium vjs-has-started vjs-playing vjs-user-inactive"
# class="ivm-view-attr__img--centered feed-shared-image__image lazy-image ember-view"
# ivm-image-view-model ember-view

# browser.get('https://www.linkedin.com/in/strati-georgopoulos/detail/recent-activity/shares/')

# url = "https://www.linkedin.com/in/strati-georgopoulos/detail/recent-activity/shares/"

# response = requests.get(url)
# soup = bs4.BeautifulSoup(response.content,"html.parser")

# images = soup.findAll('img',attrs={'class':'ivm-view-attr__img--centered feed-shared-image__image lazy-image ember-view'})


# for i in images:
#     img_url = i
#     img = Image.open(requests.get(img_url, stream = True).raw)
#     img.save()
# print("Done")
